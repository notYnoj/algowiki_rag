import requests
import numpy as np
import csv
import json
import os
import time

EMBED_URL = "https://integrate.api.nvidia.com/v1/embeddings"
EMBED_MODEL = "nvidia/nemotron-3-embed-1b"
API_KEY = os.environ.get("NVIDIA_API_KEY_NEMOTRON")


def load_rows():
    with open("data/algowiki/algorithms_clean.csv", mode = "r", newline = "", encoding = "utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows

def group_rows(rows):
    problems = {}
    for row in rows:
        key = (row["family"], row["variation"])
        problems.setdefault(key, []).append(row)
    return problems

def create_embedding_string(probelms):
    embeddings = []
    for key, value in probelms.items():
        family, variation = key
        domain = value[0]["domain"]
        names = ", ".join([a["algorithm"] for a in value[:6]])
        embedding = f"{family}: {variation}. Domain: {domain}. Known algorithms: {names}"
        embeddings.append(embedding)
    return embeddings

#it should be chill i dont wanna write that long ass for loop anymore
def embed_texts(texts, input_type):
    headers = {"Authorization": "Bearer " + API_KEY,
               "accept": "application/json", "content-type": "application/json"}
    payload = {"model": EMBED_MODEL, "input": texts, "input_type": input_type,
               "encoding_format": "float", "truncate": "NONE"}
    #keep retrying until it works: rate limits (429/402), server errors (5xx), network drops
    attempt = 0
    while True:
        try:
            response = requests.post(EMBED_URL, json=payload, headers=headers, timeout=120)
        except requests.RequestException as e:
            print(f" network error ({e}), retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            attempt += 1
            continue
        if response.status_code == 200:
            return [d["embedding"] for d in response.json()["data"]]
        if response.status_code in (402, 429) or response.status_code >= 500:
            print(f"  HTTP {response.status_code}, retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            attempt += 1
            continue
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:300]}")


def build_index():
    rows = load_rows()
    problems = group_rows(rows)
    text = create_embedding_string(problems)
    all_embeddings = []
    for chunk in range(0, len(text), 50):
        all_embeddings.extend(embed_texts(text[chunk:chunk+50], "passage"))
    
    vectors = np.array(all_embeddings)
    np.save("data/algowiki/vectors.npy", vectors)

    info = [{"family": fam, "variation": var} for (fam, var) in problems.keys()]
    with open("data/algowiki/problems.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

def search(query, k):
    vectors = np.load("data/algowiki/vectors.npy")
    with open("data/algowiki/problems.json", encoding="utf-8") as f:
        problems = json.load(f)
    q = np.array(embed_texts([query], "query")[0])
    #multiply q by vectors
    scores = vectors @ q
    #get top k thru matmul and sorting
    top = np.argsort(scores)[::-1][:k]
    ret = []
    for i in top:
        fam = problems[i]["family"]
        var = problems[i]["variation"]
        ret.append( (fam, var) )
    return ret

