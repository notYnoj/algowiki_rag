import csv
import json
import sys
from pathlib import Path

from pipeline.embed import load_rows, build_index #index is the n dimension encoding of problems
from pipeline.plan import gather_context, build_plan_prompt #gather context by searching the vector database then build the plan prompt by calling our builder
from pipeline.extract import call_llm, extract_pdf
from pipeline.agents import collect_candidates, triage
from pipeline.arxiv import download_pdf
from pipeline.parse import process_pdf
from pipeline.ingest import ingest_pdf
from pipeline.match import match_result

SAMPLE_CSV = Path("data/algowiki/sample_problems.csv")
PROBLEMS_PATH = Path("data/algowiki/problems.json")   # every (family, variation), written by build_index()
TASKS_PATH = Path("data/plan/tasks.json")
DOWNLOADS_PATH = Path("data/agents/downloads.json")
REVIEW_CSV = Path("data/review/candidates.csv")

PER_QUERY = 10              # arXiv results per query per search round
MIN_PAPERS_PER_TASK = 10    # keep searching until each problem has at least this many kept papers
MAX_SEARCH_ROUNDS = 10      # at most 10 rounds x PER_QUERY results per query, then accept fewer


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def sample_problems():
    with open(SAMPLE_CSV, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    problems = []
    for row in rows:
        key = (row["family"], row["variation"])
        if key not in problems:
            problems.append(key)
    return problems


def all_problems():
    # the FULL dataset: every (family, variation) in AlgoWiki
    return [(p["family"], p["variation"]) for p in load_json(PROBLEMS_PATH)]


def make_tasks(problems, rows):
    # plan: AlgoWiki context -> LLM writes arXiv queries for each problem
    # saves after every problem, so a crash / Ctrl-C resumes where it stopped
    tasks = load_json(TASKS_PATH) if TASKS_PATH.exists() else []
    done = {(t["family"], t["variation"]) for t in tasks}
    for family, variation in problems:
        if (family, variation) in done:
            continue
        print(f"[plan] {family}: {variation}")
        try:
            known, related = gather_context(family, variation, rows)
            content, usage, finish_reason = call_llm(build_plan_prompt(family, variation, related, known))
            task = json.loads(content)
        except Exception as e:
            print(f"  FAILED planning {family}: {variation}: {e}")
            continue
        task["family"] = family
        task["variation"] = variation
        tasks.append(task)
        save_json(TASKS_PATH, tasks) #we save tasks after we finish them
    return tasks


def find_papers(tasks):
    # agents: search arXiv, LLM checks whcih papers to keep and download, download the kept papers
    # keeps paging through arXiv (start = 0, 10, 20, ...) until the problem has MIN_PAPERS_PER_TASK
    # kept papers, or arXiv runs out of results, or MAX_SEARCH_ROUNDS is hit
    # saves after every problem, so a crash / Ctrl-C resumes where it stopped
    downloads = load_json(DOWNLOADS_PATH) if DOWNLOADS_PATH.exists() else []
    for task in tasks:
        have = [d for d in downloads if d["family"] == task["family"] and d["variation"] == task["variation"]]
        if len(have) >= MIN_PAPERS_PER_TASK:
            continue
        print(f"[agents] {task['family']}: {task['queries']} ({len(have)} papers so far)")
        seen = {d["id"] for d in have} #set 
        try:
            for search_round in range(MAX_SEARCH_ROUNDS):
                candidates = collect_candidates(task, PER_QUERY, search_round * PER_QUERY)
                if not candidates:
                    break   # arXiv has no more results for these queries
                new = [c for c in candidates if c["id"] not in seen]
                seen.update(c["id"] for c in new)
                if not new:
                    continue
                for paper in triage(task, new):
                    path = download_pdf(paper["id"])
                    print(f"  downloaded {paper['id']}: {paper['reason']}")
                    entry = {"family": task["family"], "variation": task["variation"],
                             "id": paper["id"], "reason": paper["reason"], "path": str(path)}
                    have.append(entry)
                    downloads.append(entry)
                if len(have) >= MIN_PAPERS_PER_TASK:
                    break
        except Exception as e:
            print(f"  FAILED searching {task['family']}: {e}")
        if len(have) < MIN_PAPERS_PER_TASK:
            print(f"  only found {len(have)} relevant papers for {task['family']}: {task['variation']}")
        save_json(DOWNLOADS_PATH, downloads)
    return downloads


def read_paper(pdf_path):
    # parse -> ingest -> extract; returns (extracted dict, quote check passed?)
    # no page limit: every paper is parsed, however long
    process_pdf(pdf_path)
    ingest_pdf(Path("data/parsed") / pdf_path.stem)
    extract_pdf(Path("data/docs") / f"{pdf_path.stem}.json")

    good = Path("data/extracted") / f"{pdf_path.stem}.json"
    flagged = Path("data/hallucinations") / f"{pdf_path.stem}.json"
    if good.exists():
        return load_json(good), True
    return load_json(flagged), False


def review_rows(download, extracted, quote_ok, rows):
    base = {"paper": download["id"], "searched_for": f"{download['family']}: {download['variation']}"}
    if not extracted.get("claims_new_result"):
        return [{**base, "verdict": "no new result claimed"}]

    out = []
    for result in extracted["results"]:
        m = match_result(result, rows)
        matched = f"{m['family']}: {m['variation']}" if m["family"] else "NOT_MATCHED"
        out.append({**base,
                    "problem_in_paper": result.get("problem"),
                    "new_bound": result.get("bound"),
                    "matched_algowiki_problem": matched,
                    "algowiki_best": m["algowiki_best"] if m["algowiki_best"] else "NOT_MATCHED",
                    "verdict": m["verdict"],
                    "reason": m["reason"],
                    "quote": result.get("quote"),
                    "page": result.get("page"),
                    "quote_check": "passed" if quote_ok else "FAILED",
                    "approve": ""})
    return out


def write_review(review):
    fields = ["paper", "searched_for", "problem_in_paper", "new_bound", "matched_algowiki_problem",
              "algowiki_best", "verdict", "reason", "quote", "page", "quote_check", "approve"]
    REVIEW_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(REVIEW_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(review)


if __name__ == "__main__":
    if not Path("data/algowiki/vectors.npy").exists():
        print("[embed] building the AlgoWiki index")
        build_index()

    rows = load_rows()
    
    tasks = make_tasks(all_problems(), rows)
    downloads = find_papers(tasks)

    review = []
    for download in downloads:
        print(f"[paper] {download['id']}")
        try:
            got = read_paper(Path(download["path"]))
            if got is None:
                continue
            extracted, quote_ok = got
            review.extend(review_rows(download, extracted, quote_ok, rows))
            write_review(review)   # save as we go, the full run takes days
        except Exception as e:
            print(f"  FAILED on {download['id']}: {e}")

    write_review(review)
    print(f"[review] {len(review)} rows -> {REVIEW_CSV}")
