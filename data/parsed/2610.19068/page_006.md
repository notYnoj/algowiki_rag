## 4.3 Discovery as the Binding Constraint

Trajectory fidelity (at least 96%, Figure 4e) confirms the planner almost always selects from the retrieved set, making retrieval the bottleneck. As a result, architecture choice at retrieval time fully determines downstream behavior: PtR’s planner generates more ambitious plans on G3 (4.1 intended steps, 1.4 APIs named vs. 3.6 steps, 1.1 APIs) and uses a higher fraction of retrieved APIs (27-29% vs. 21-27%), reflecting the broader, more coherent candidate sets produced by stub-guided retrieval.

PtR’s discovery call adds ∼75-104% token overhead (Appendix E,  8); on G1 this hurts (-0.072 recall) while on G2 it pays off (+0.042 recall). Beyond token cost, this discovery call sits on the critical path: because discovery and retrieval are sequential, PtR adds one full LLM round-trip of latency before retrieval and planning begin, so the overhead is both a token cost and a wall-clock latency penalty. Complexity- adaptive routing (using RtP for G1, PtR for G2/G3) saves ∼16% of total inference tokens, or ∼36% of the PtR discovery-call overhead, with no retrieval quality loss relative to always selecting the better architecture per subset, and eliminates the extra round-trip entirely for G1-type queries. The crossover maps naturally onto single-tool vs. multi-tool intent; practical proxies computable before any LLM call include query length, clause count, named-entity density, and the presence of conjunctive sub-goals -- all of which correlate with the G1/G2 split in ToolBench. Most directly, RtP’s own top-1 cosine similarity is a zero-cost routing signal already produced by the pipeline: a high top-1 score indicates the query names an API directly (high Intent-Registry Coupling, G1-like) and can stay with RtP, whereas a low or diffuse score indicates abstract multi-step intent (G2/G3-like) that benefits from PtR’s stub decomposition -- so a simple threshold on this score routes queries with no extra model and no extra call. We leave empirical validation of such classifiers<tbc>

(a) Selection Rate
(b) Plan Complexity
(c) Selected API Overlap
40
7
0.6
PtR
PtR steps
PtR APIs selected
35
RtP
RtP steps
RtP APIs selected
6
0.5
30
5
0.403
25
0.4
% of retrieved APIs used
4
0.3
0.293
20
3
0.277
15
Count
Jaccard similarity
10
2
0.2
5
1
0.1
0
0
0.0
G1
G2
G3
G1
G2
G3
G1
G2
G3
(d) Planner Recovery When Retrieval Fails
(e) Trajectory Fidelity
PtR (uses wrong tools)
PtR (uses wrong tools)
PtR (refuses)
PtR (refuses)
100
PtR
100
RtP
% of queries with retrieval miss
% selected from retrieved set
80
98
60
96
40
94
20
92
0
90
G1
G2
G3
G1
G2
G3

**Figure 4** Agent trajectory divergence across subsets: (a) selection rate = fraction of retrieved APIs the planner uses; (b) plan complexity = mean intended steps and APIs named; (c) Jaccard overlap of planner-selected API sets across architectures; (d) planner behavior when retrieval completely misses all Ground-Truth APIs; (e) trajectory fidelity = fraction of planner selections drawn from the retrieved set.

