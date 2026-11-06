import json
import os
import time
from pathlib import Path

import requests

URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "nvidia/nemotron-3.5-super-vl-120b-a12b"
API_KEY = os.environ.get("NVIDIA_API_KEY_NEMOTRON")
if not API_KEY:
    raise RuntimeError("NVIDIA_API_KEY_NEMOTRON not set: open a new terminal")

DOCS_DIR = Path("data/docs")
OUT_DIR = Path("data/extracted")

#claude <3
INSTRUCTIONS = """You are helping maintain AlgoWiki, a catalog of algorithmic problems and the best known bounds for them.

Read the paper below. Pages are separated by lines like "=== Page 3 ===".

Report only results that THIS paper proves: new algorithms or improved bounds (running time, space, approximation ratio, or lower bounds).
Do NOT report bounds the paper cites from earlier work. Do NOT report intermediate lemmas.

Return only a JSON object in this shape:
{
  "claims_new_result": true or false,
  "results": [
    {
      "problem": "name of the problem",
      "problem family": "name of the problem family if found in the paper, otherwise null",
      "bound": "the bound in LaTeX",
      "bound_type": "time upper bound" | "space upper bound" | "lower bound" | "approximation" | "other",
      "deterministic": true | false | null,
      "previous_best": "best earlier bound the paper compares against, or null",
      "quote": "one sentence copied character for character from the paper that states this result",
      "page": page number where the quote appears
    }
  ]
}

If the paper proves no new result, return {"claims_new_result": false, "results": []}."""


def build_prompt(doc):
    pages = []
    for page in doc["pages"]:
        pages.append(f"=== Page {page['page']} ===\n{page['text']}")
    pdf = "\n\n".join(pages)
    prompt = INSTRUCTIONS + "\n\n" + pdf

    return prompt


def call_llm(prompt):

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 16000,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY,
        "content-type": "application/json",
    }

    #keep retrying until it works: rate limits (429/402), server errors (5xx), network drops
    #wait 2s / 4s / 8s ... capped at 60s between tries
    attempt = 0
    while True:
        try:
            response = requests.post(URL, json = payload, headers = headers, timeout = 600)
        except requests.RequestException as e:
            print(f" network error ({e}), retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            attempt += 1
            continue
        if response.status_code == 200:
            choice = response.json()["choices"][0]
            return (choice["message"]["content"], response.json().get("usage"), choice["finish_reason"])
        if response.status_code in (402, 429) or response.status_code >= 500:
            print(f"  HTTP {response.status_code}, retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            attempt += 1
            continue
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:500]}")

def verify_quotes(result, doc):
    for r in result["results"]:
        page = r["page"]
        found = False
        for item in doc["pages"]:
            if item["page"] == page:
                found = True
                text = " ".join(item["text"].split()) 
                quote = " ".join(r["quote"].split())
                text = text.replace('_', '')
                text= text.replace('*', '')
                quote = quote.replace('_', '')
                quote = quote.replace('*', '')
                if quote not in text:  
                    return False
        if not found:
            return False
    return True

def extract_pdf(path):
    out_path = OUT_DIR / path.name
    if os.path.exists(out_path) or os.path.exists(Path("data/hallucinations") / path.name):
        return
    
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    
    prompt = build_prompt(doc)
    res = call_llm(prompt)
    content, usage, finish_reason = res 
    if finish_reason == "length":
        print(f"  WARNING: {path.name} hit max_tokens, reply is cut off")
    result = json.loads(content)
    
    if not verify_quotes(result, doc):
        print(f"  WARNING: {path.name} had a hallcuination, response is written in data/hallucinations")
        out_dir_here = Path("data/hallucinations")
        out_dir_here.mkdir(parents=True, exist_ok=True)
        result["paper"] = doc["paper"]
        result["usage"] = usage
        with open(out_dir_here / path.name, "w", encoding = "utf-8") as f:
            json.dump(result, f, indent = 2, ensure_ascii=False)
        return

    result["paper"] = doc["paper"]
    result["usage"] = usage
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False) 



    #if it exsists skip
    # load the doc, then build the prompt, call llm, and then load
    #verify, if bad add it somewhere else, otherwise just dump it into a directory of its own

def extract_pdfs():
    for pdf_path in sorted(DOCS_DIR.glob("*.json")):
        extract_pdf(pdf_path)
        print(f"Worked on pdf at: {pdf_path.name}\n")

    #loop over docs, call extract_pdf, print a summary line