import requests
import os
from pathlib import Path
import pypdfium2 as pdfium
import io
import base64
import time 
import json

TARGET_HEIGHT = 2048
MAX_WIDTH = 1664

DROP_TYPES = {"Page-header", "Page-footer", "Bibliography"}

#Get API Keys and URLS
url = "https://integrate.api.nvidia.com/v1/chat/completions"
API_KEY = os.environ.get('NVIDIA_API_KEY_NEMOTRON')


#take pdfs render their pages and then parse the text into markdown
def render_page(pdf, page_num):
    page = pdf[page_num-1]
    width, height = page.get_size()
    scale_height = float(TARGET_HEIGHT) / float(height)
    sclae_width = float(MAX_WIDTH) / float(width)
    image = page.render(scale = min(scale_height, sclae_width)).to_pil()
    return image

def base64_encoding(pil_image):
    b_buf = io.BytesIO()
    pil_image.save(b_buf, format = "PNG")
    return base64.b64encode(b_buf.getvalue()).decode() #takes the buffer, converts it to base64 then turns it back into a string

#Payload and request
def send_payload(image):
    payload = {
        "messages": [{"role": "user", "content": [{"type": "image_url", "image_url": {"url": "data:image/png;base64," + image}}]}],
        "model": "nvidia/nemotron-parse",
        "frequency_penalty": 0, # no penatly for token appearence
        "max_tokens": 8192, #endpoint max context is 9000 tokens (prompt + completion)
        "presence_penalty": 0,
        "stream": False, #send it back once its all complete
        "temperature": 0,
    }
    headers = {
        "accept": "application/json", #send as json
        "Authorization": "Bearer " + API_KEY,
        "content-type": "application/json"
    }
    
    #keep retrying until it works: rate limits (429/402), server errors (5xx), network drops
    #wait 2s / 4s / 8s ... capped at 60s between tries
    #other errors (400 bad request, 401 bad key) can't fix themselves, so raise those
    attempt = 0
    while True:
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=240) #send it w/ timeout 4 min
        except requests.RequestException as e:
            print(f" network error ({e}), retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            if attempt < 5:
                attempt += 1
            continue
        if response.status_code == 200:
            return response.json()
        #if im rate limited i want to keep adding more time which is why we do 2/4/8/... 60
        if response.status_code in (402, 429) or response.status_code >= 500:
            print(f"  HTTP {response.status_code}, retrying...")
            time.sleep(min(2 ** (attempt + 1), 60))
            if attempt < 5: 
                attempt += 1
            continue
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:500]}")


def extract_elements(res):
    #why is json so sad </3
    return json.loads(res["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"])[0]
    

def to_markdown(elements):
    text= ""
    for ele in elements:
        if ele["type"] in DROP_TYPES:
            continue
        text+= (ele["text"] + ('\n\n'))
    return text

#parses every page of a pdf and saves each one to data/parsed/<paper>/page_NNN.md
def process_pdf(path):
    out_dir = Path("data/parsed") / path.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(path)

    try:
        for i in range(1, len(pdf)+1):
            out_file = out_dir / f"page_{i:03d}.md"
            if os.path.exists(out_file):
                continue
            image = render_page(pdf, i)
            encoded = base64_encoding(image)
            res = send_payload(encoded)
            if res["choices"][0]["finish_reason"] == "length":
                print(f"  WARNING: page {i} hit max_tokens, saved text is cut off")
            elements = extract_elements(res)
            markdown = to_markdown(elements)
            with open(out_file, 'w', encoding = "utf-8") as file:
                file.write(markdown)
    finally:
        pdf.close()

def parse():
    throw = input("Ensure all pdfs are in data/papers. Click enter when ready\n")
    pdfs = sorted(Path("data/papers").glob("*.pdf"))
    for pdf in pdfs:
        process_pdf(pdf)
    