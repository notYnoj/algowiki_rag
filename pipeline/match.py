import json

from pipeline.embed import search
from pipeline.extract import call_llm

#match a paper to algowikis problems (use embeddings to find closest probelms and match em)

MATCH_INSTRUCTIONS = """You are helping maintain AlgoWiki, a catalog of algorithmic problems and the best known algorithms for them.

Below is one result extracted from a new paper, and a numbered list of AlgoWiki problems that look similar. Each AlgoWiki problem lists the algorithms AlgoWiki already has for it (name, year, time complexity).

1. Pick the AlgoWiki problem that is the SAME problem as the paper's result (same problem and same setting). If none of them is the same problem, use null.
2. If you picked one, compare the paper's bound with the best bound AlgoWiki lists for that problem:
   - "improves": the paper's bound is asymptotically better
   - "matches": same bound
   - "worse": the paper's bound is asymptotically worse
   - "unclear": the bounds use different parameters or models and cannot be compared directly
   If you picked null, the verdict is "new problem".

Return only a JSON object in this shape:
{
  "candidate": the number of the matching AlgoWiki problem, or null,
  "algowiki_best": "the best bound AlgoWiki lists for that problem, or null",
  "verdict": "improves" | "matches" | "worse" | "unclear" | "new problem",
  "reason": "one sentence"
}"""


def known_algorithms(family, variation, rows):
    return [(r["algorithm"], r["year"], r["time_complexity"])
            for r in rows if r["family"] == family and r["variation"] == variation]


def build_match_prompt(result, candidates, rows):
    lines = [MATCH_INSTRUCTIONS, "", "Paper result:",
             f"  problem: {result.get('problem')}",
             f"  bound: {result.get('bound')} ({result.get('bound_type')})",
             f"  quote: {result.get('quote')}",
             "", "AlgoWiki problems:"]
    for i, (family, variation) in enumerate(candidates, start=1):
        lines.append(f"{i}. {family}: {variation}")
        for name, year, time in known_algorithms(family, variation, rows)[:10]:
            lines.append(f"   - {name}, {year}, {time}")
    return "\n".join(lines)


def match_result(result, rows, k=5):
    # retrieve: the k AlgoWiki problems most similar to the paper's problem
    query = f"{result.get('problem') or ''}. {result.get('problem family') or ''}"
    candidates = search(query, k)

    # generate: the LLM picks the match and compares the bounds
    content, usage, finish_reason = call_llm(build_match_prompt(result, candidates, rows))
    answer = json.loads(content)

    choice = answer.get("candidate")
    if isinstance(choice, int) and 1 <= choice <= len(candidates):
        family, variation = candidates[choice - 1]
    else:
        family, variation = None, None

    return {"family": family, "variation": variation,
            "algowiki_best": answer.get("algowiki_best"),
            "verdict": answer.get("verdict"),
            "reason": answer.get("reason")}
