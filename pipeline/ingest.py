from pathlib import Path
import json
import os

base = Path("data/parsed")

def ingest_page(path):
    page_num = int(path.stem.split("_")[1]) 
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return None
    return {"page": page_num, "text": text}
    pass

def ingest_pdf(folder):
    pages = []
    for md in sorted(folder.glob("page_*.md")):
        res = ingest_page(md)
        if res is None:
            continue
        pages.append(res)

    doc = {
        "paper": folder.name,
        "pages": pages,
        "n_words": sum(len(p["text"].split()) for p in pages),
    }

    out_dir = Path("data/docs")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / f"{folder.name}.json", "w", encoding="utf-8") as file:
        json.dump(doc, file, indent=4, ensure_ascii=False)
    return doc

def ingest_pdfs():
    pdfs = Path("data/parsed")
    for folder in sorted(p for p in pdfs.iterdir() if p.is_dir()):
        ingest_pdf(folder)

