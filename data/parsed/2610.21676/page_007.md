<tbc>monotonically decreasing weights \(\alpha_1>\cdots>\alpha_L\):

\(w_{uv}=\sum_{q:u,v\in R_q}\alpha_{\ell(q,u,v)},\)<br>
\(\ell(q,u,v)=min\{\ell:max(\rho_q(u),\rho_q(v))\le\kappa_\ell\}.\)

This weighting makes the segment layout reflect the documents most likely to be requested together by the retriever, while still retaining weaker evidence from the tail of a wider result list. For multi-round retrieval traces, edges are added both within a round and across adjacent rounds, capturing the locality needed by iterative RAG queries.

The partitioning goal is to group documents so that high- weight edges stay inside a bounded CCS segment:

\(max_{\{S_i\}}\sum_l\sum_{(u,v)\in E,u,v\in S_i}w_{uv}\text{s.t.}|S_i|\le B.\)

This is balanced graph partitioning [28] and admits direct off-the-shelf solvers. RPAG partitions each connected component of the co-retrieval graph; small components become segments directly, while larger components are split by METIS into roughly equal-sized parts. The result is a document- to-segment assignment that the CCS writer materializes as segment files and a packed doc\_map. Because the objective mentions only document IDs and query co-occurrence, it is independent of the ANN engine that will later produce those IDs.

A pure co-retrieval graph covers only documents observed in the training log. Treating unobserved documents as arbitrary isolated vertices would make their placement unstable and would waste segment capacity on weak evidence. Con- Store therefore uses a hybrid assignment: documents with sufficient co-retrieval support are placed by RPAG, while cold or unseen documents inherit an embedding k-means placement. This fallback is not a separate online path; it is resolved once when the CCS files are written, so every query still uses the same constant-time doc-id-to-segment lookup.

**Page-aware intra-segment refinement.** Segment membership decides which documents can be fetched together;<tbc>

<tbc>the order inside a segment decides whether those documents share the same SSD pages. We therefore apply a page-aware refinement, RPAG, after the hybrid RPAG/k-means assignment. RPAG preserves each segment’s document set and constructs a second co-retrieval graph only among documents already assigned to that segment. It uses the same prefix-weighted evidence as above inside each existing segment, but now the objective is linear ordering rather than partitioning: co-retrieved documents should appear near each other in the segment’s content block so that GCF can cover them with one or a few page-aligned read windows.

For each touched segment, RPAG greedily packs the intra- segment graph. It starts from the document with the largest weighted degree, then repeatedly appends the strongest unplaced neighbor of the current document; when a connected component is exhausted, it resumes from the highest-degree remaining document. The CCS writer then rewrites the segment’s content bytes and local id order according to this permutation, leaving untouched segments byte-identical. This step does not change recall or segment membership: it only converts the locality that RPAG exposes at segment granularity into page locality that the page-aware GCF planner can consume.

## 5.3 Workload-Adaptive Segment Reorganization (WASR)

RPAG’s layout can become stale when queries begin retrieving different documents together. We propose _Workload- Adaptive Segment Reorganization_ (WASR) to adapt the layout to these workload shifts. A background controller regroups selected segments only when recurring co-retrieval patterns reveal degraded locality and the expected I/O savings justify rewriting them. Queries continue using the constant-time doc\_map of their current layout version while reorganization runs.

**Learning recurring locality.** Real workloads often exhibit skewed popularity, with popular queries and entities revisited. A learned layout benefits only when document pairs are retrieved together again. WASR measures _pair recurrence r<sub>t</sub>_: the fraction of epoch _t_’s co-retrieval edge weight contributed by pairs seen in earlier epochs. It retains k-means placement without confirmed co-retrieval evidence and avoids rewriting for unpredictable workloads.

**Online co-retrieval monitor.** The monitor identifies recurring pairs while aging out obsolete evidence. It samples completed queries’ _final_ top-_K_ lists, not provisional ANN candidates, and aggregates each epoch of _E_ queries into a time bucket. For documents _u_ and _v_, their recent edge weight is

\(w_t(u,v)=\sum_{a=0}^{W-1}\gamma^ac_{t-a}(u,v),\)

D1
D2
D3
Dn
Query Dataset
Raw Content File
(Insertion order)
Train split
RPAG partition
RPAG Build
Trace Generation
Segment Assignment
Cross-hop Co-Retrieval Graph
H1
3
7
12
5
Page-aware Local Reorder
H2
7
9
12
30
Rank prefix α
2 pages
1 page
1
.3
.1
.03
Hot doc
Head pair
METIS cut
Cold K-Means
Tail pair
4 KB page
seg_ *.cvs + Doc_Map
Hot top-K doc
Cross-hop
B: Seg. capacity
Doc (Seg, Idx)

**Figure 7.** RPAG layout pipeline.

