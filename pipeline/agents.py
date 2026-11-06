import json
from pathlib import Path

from pipeline.arxiv import search_arxiv, download_pdf
from pipeline.extract import call_llm

TASKS_PATH = Path("data/plan/tasks.json")
OUT_PATH = Path("data/agents/downloads.json")

TRIAGE_INSTRUCTIONS = """You are helping maintain AlgoWiki, a catalog of algorithmic problems and the best known algorithms for them.

Below is one problem from AlgoWiki and a list of arXiv papers (id, title, abstract) found by keyword search.

For each paper, decide whether it could contain a result about THIS problem: an algorithm, a running time or space bound, an approximation ratio, or a lower bound. The result may be the paper's main result or a side result (a corollary, an application, or a special case).

Rules:
- Keep a paper if it is about this problem, a special case of it, or a generalization of it.
- Keep a paper if you are unsure. A later step reads the full text, so a wrong keep only costs time, but a wrong drop loses the paper AND RELEVANT INFORMATION.
- Drop a paper only if it is CLEARLY about a different problem or CLEARLY irrelevant.
- Use ONLY the ids listed below. DO NOT invent ids. 

Return only a JSON object in this shape:
{
  "keep": [
    {"id": "the arXiv id exactly as given", "reason": "one short sentence"}
  ]
}

If no paper should be kept, return {"keep": []}."""

def load_tasks():
    tasks = []
    with open(TASKS_PATH, "r") as f:
        tasks = json.load(f)
    return tasks

def collect_candidates(task, per_query=10, start=0):
    candidates = {}
    for query in task["queries"]:
        for paper in search_arxiv(query, per_query, start):
            candidates[paper["id"]] = paper
    return list(candidates.values())
        



def build_triage_prompt(task, candidates):
    ret = TRIAGE_INSTRUCTIONS + "\n\n"
    ret += f"Problem: {task["family"], task["variation"]}\n"
    ret+= f"The candidates are:\n"
    for cand in candidates:
        ret+=f"id: {cand['id']} \n Candidate Title: {cand["title"]}\n Candidate Abstract: {cand["abstract"]}"
        ret+="\n\n"
    
    return ret 



def triage(task, candidates):

    content, usage, finish_reason = call_llm(build_triage_prompt(task, candidates))
    results = json.loads(content)
    kept = []
    for result in results["keep"]:
        cur_id = result["id"]
        for cand in candidates:
            if cand["id"] == cur_id:
                kept.append(result)
                break
    return kept


def run_agents():
    OUT_PATH.parent.mkdir(parents = True, exist_ok=True)

    downloads = []

    for task in load_tasks():
        candidates = collect_candidates(task)
        kept_papers = triage(task, candidates)
        for paper in kept_papers:
            path = download_pdf(paper["id"])
            downloads.append({"family" : task["family"], "variation" : task["variation"], "id" : paper["id"], "reason" : paper["reason"], "path" : str(path)})
    
    with open(OUT_PATH, "w", encoding = "utf-8") as f:
        json.dump(downloads, f, indent=2, ensure_ascii=False)
    
    return downloads