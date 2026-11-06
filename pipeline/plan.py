from pipeline.embed import load_rows, search
from pipeline.extract import call_llm
import json
from pathlib import Path



def recent_problems(n):
    rows = load_rows()
    kept_rows = []
    for row in rows:
        if row["source_tab"] == "New Entries to Sheet 1":
            kept_rows.append(row)
    
    kept_rows.sort(key = lambda x: -int(x["source_row"])) 
    ret = []
    for i in range(len(kept_rows)):
        if len(ret) == n:
            break
        else:
            cur = (kept_rows[i]["family"], kept_rows[i]["variation"])
            if cur not in ret:
                ret.append(cur)
    return ret


def gather_context(family, variation, rows):
    related = search(f"{family}: {variation}", 6)
    related = [p for p in related if p != (family, variation)]
    known = []
    for row in rows:
        if row["family"] == family and row["variation"] == variation:
            known.append( (row["algorithm"], row["year"], row["time_complexity"]) )

    return known, related



def build_plan_prompt(family, variation, related, known):
    # instructions + the problem + its known algorithms + related problems

    #Claude <3:
    PLAN_INSTRUCTIONS = """You are helping maintain AlgoWiki, a catalog of algorithmic problems and the best known algorithms for them.

Below is one problem from AlgoWiki, the algorithms AlgoWiki already lists for it (name, year, time complexity), and a few related problems.

Write 3 arXiv search queries that would find recent papers giving a new or faster algorithm, or a new lower bound, for THIS problem.

Rules for the queries:
- Each query is a short keyword phrase of 2 to 6 words, using words that would appear in a paper's title or abstract.
- Use the problem's standard technical name, plus another common name for it if one exists.
- Do not include years, author names, quotation marks, or AND/OR.
- Use the related problems only for wording ideas. Every query must still be about THIS problem.

Return only a JSON object in this shape:
{
  "queries": ["query 1", "query 2", "query 3"],
  "why": "one sentence: what new result these queries look for, given the best known algorithm listed below"
}"""

    problem_line = f"Problem: {family}: {variation}"
    known_algorithms = "Known Algorithms:\n"
    for prob in known:
        known_algorithms+=f" {prob[0]}, {prob[1]}, {prob[2]} \n"
    
    related_problems = "Related Problems:\n"
    for relate in related:
        related_problems+=f" {relate[0]}, {relate[1]} \n"
    
    return PLAN_INSTRUCTIONS + "\n\n" + problem_line + "\n\n" + known_algorithms + "\n" + related_problems

def plan(n=10):
    # collect tasks, save to data/plan/tasks.json
    rows = load_rows()
    r_probs = recent_problems(n)
    tasks = []
    for prob in r_probs:
        known, related = gather_context(prob[0], prob[1], rows)
        prompt = build_plan_prompt(prob[0], prob[1], related, known)
        raw = call_llm(prompt)
        content, usage, finish_reason = raw
        result = json.loads(content)
        result["family"] = prob[0]
        result["variation"] = prob[1]
        tasks.append(result)
    out_dir = Path("data/plan")
    out_dir.mkdir(parents = True, exist_ok = True)
    with open("data/plan/tasks.json", mode = "w", encoding = "utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

    return tasks