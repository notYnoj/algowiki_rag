import os
import time
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
import json

API_URL = "https://export.arxiv.org/api/query"
PDF_URL = "https://arxiv.org/pdf/"
PAPERS_DIR = Path("data/papers")
NS = {"a": "http://www.w3.org/2005/Atom"}


def build_query(query):
    words = query.split()
    ret = "all:"
    for word in words:
        ret+= f"{word} AND all:"
    return (ret.removesuffix(' AND all:'))



def parse_entry(entry):
    start = entry.find("a:id", NS).text
    _, _, after = start.partition("/abs/")
    id_ = after.rsplit("v", 1)[0]
    title_2 = entry.find("a:title", NS).text
    title = " ".join(title_2.split())
    abst = entry.find("a:summary", NS).text
    abstract = " ".join(abst.split())
    pub = entry.find("a:published", NS).text
    published = pub[:10]

    return {"id": id_, "title":title, "abstract" : abstract, "published" : published}



#keep retrying a GET until it works: rate limits (429), server errors (5xx, arXiv sends 503 when busy), network drops
def get_until_ok(link, params=None, timeout=60):
    attempt = 0
    while True:
        try:
            res = requests.get(link, params=params, timeout=timeout)
        except requests.RequestException as e:
            print(f" network error ({e}), retrying...")
            time.sleep(min(3 * 2 ** attempt, 60))
            attempt += 1
            continue
        if res.status_code == 200:
            return res
        if res.status_code == 429 or res.status_code >= 500:
            print(f"  HTTP {res.status_code} from arXiv, retrying...")
            time.sleep(min(3 * 2 ** attempt, 60))
            attempt += 1
            continue
        raise RuntimeError(f"arXiv HTTP {res.status_code} for {link}")


#start = how many results to skip, so we can go past the first max_results
def search_arxiv(query, max_results=10, start=0):
    params = {
        "search_query": build_query(query),
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    res = get_until_ok(API_URL, params=params, timeout=60)

    root = ET.fromstring(res.text)
    papers = [parse_entry(e) for e in root.findall("a:entry", NS)]
    time.sleep(3)
    return papers


def download_pdf(arxiv_id):
    path = PAPERS_DIR / f"{arxiv_id.replace('/', '_')}.pdf" #old-style ids like cs/0611037 have a slash
    if os.path.exists(path):
        return path
    
    PAPERS_DIR.mkdir(parents = True, exist_ok=True)
    res = get_until_ok(PDF_URL + arxiv_id, timeout = 180)

    with open(path, "wb") as f:
        f.write(res.content)
    
    time.sleep(3)
    return path