discovery model (temperature=0, retrieval budget _k_=5). Let T be the tool registry, _q_ the user query, _d<sub>t</sub>_ the documentation of tool _t_, \(\mathrm{sim}(\cdot,\cdot)\) the cosine similarity between embeddings, and \(\pi(\cdot)\) the agent’s execution plan given a retrieved tool set.

**RtP** embeds the raw query and retrieves the top-_k_ most similar APIs: \(R_{\mathrm{RtP}}(q)=\mathrm{TopK}_{t\in\mathcal{T}}\mathrm{sim}(q,d_t)\); the planner then produces plan \(\pi_{\mathrm{RtP}}(q,R_{\mathrm{RtP}}(q))\).

**PtR** first sends _q_ to the planner _without_ any tool definitions, generating stubs _S(q_)={_s_<sub>1</sub>_,...,s<sub>m</sub>_} (JSON objects with a hypothesized tool name and reasoning). Each stub is embedded and matched against the index; the union of top-_k_ results (deduplicated, re-ranked) forms \(R_{\mathrm{PtR}}(q)=\mathrm{TopK}_{t\in\mathcal{T}}\mathrm{max}_{s\in S(q)}\mathrm{sim}(s,d_t)\), which is passed back to the planner to produce \(\pi_{\mathrm{PtR}}(q,R_{\mathrm{PtR}}(q))\).

An unfiltered baseline is infeasible at this scale: ToolBench categories contain up to 4,455 APIs (Sports) and 3,583 (Data), and Ground-Truth APIs are distributed across each category such that any fixed-size truncation misses them in the vast majority of cases.

## 2.2 Data and Metrics

ToolBench (Qin et al., 2024b) provides three test subsets: **G1** (single-tool, _n_=200), **G2** (intra-category multi- tool, _n_=200), and **G3** (cross-category multi-tool, _n_=100; smaller set, so G3 differences have lower statistical power). We report retrieval **recall** and **precision** computed at the fixed budget _k_=5 against the Ground- Truth API set from each query’s ToolBench gold trajectory (all APIs executed in the reference solution). RtP retrieval is deterministic (the query is embedded by GTE-base, a fixed model, and matched against the FAISS index via exact nearest-neighbor search; no LLM call, no sampling), so its precision and recall carry no run-to-run variance and are reported without a standard deviation. All remaining quantities -- PtR’s precision and recall, and pass rate for both architectures -- are averaged over 4 independent runs and reported as mean \(\pm\)std, since both stub generation and planner output vary across runs. Statistical comparisons use a one-sample _t_-test for precision and recall (PtR’s 4-run mean vs. the deterministic RtP value) and a two-sample _t_-test for pass rate. All experiments use the full 46,984-API registry unless otherwise noted.

_Evaluation proxy._ We evaluate against ToolBench gold trajectories as a retrieval proxy rather than end-to-end API execution. Trajectory fidelity (at least 96%; §4.3) supports this as a valid proxy for planner behavior: the planner almost always selects from the retrieved set, so retrieval quality upper-bounds task completion. Parameter correctness and final answer quality are not assessed and constitute a limitation noted in §5.

(a) Recall & Precision: Complexity-Dependent Crossover
(b) Per-Query Recall: Win/Loss/Tie Counts
0.45
RtP Recall
PtR Recall
1.0
RtP wins
RtP wins
RtP Precision
PtR Precision
Tie
0.40
0.8
0.35
104
101
61
0.30
0.6
Fraction of queries
Score
0.25
0.4
33
69
0.20
23
0.2
0.15
63
30
16
0.10
0.0
G1 (single-tool)
G2 (multi-tool intra)
G3 (multi-tool cross)
G1 (single-tool)
G2 (multi-tool intra)
G3 (multi-tool cross)

**Figure 2** Complexity-dependent crossover. (a) Both recall (solid) and precision (dashed) flip from RtP-dominant on G1 to PtR-dominant on G2/G3. (b) Per-query recall win/loss counts: RtP wins more queries on G1 (63 vs. 33); PtR wins more on G2 (69 vs. 30).

