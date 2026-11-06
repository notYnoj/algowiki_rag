<tbc>it multiplies one two-dimensional block against another. Recent Intel CPUs provide such an engine through Intel Advanced Matrix Extensions (AMX) [19]. Figure 2 shows the engine and how the batched scan maps onto it. AMX provides two-dimensional _tile_ registers and tile-multiply instructions that multiply a block of queries by a block of vector codes, accumulating a dense result block. This shape matches the IVF distance scan. For each probed cluster, the database vectors form a contiguous candidate block, and the queries that probe the cluster form the other dimension of the matrix multiply.

AMX, however, directly supports only low-precision operands such as INT8 and BF16. This operand restriction creates the central precision problem for AMX-based high- recall ANN search. CABANA [27] demonstrates the performance opportunity by mapping the cluster-aware IVF fine scan to AMX-efficient matrix multiplication, but it still scans a lossy BF16 code because that format is directly supported by AMX. This leaves the precision problem unresolved and harms retrieval quality since recall is limited. KatoANN instead keeps the scan compute-bound on the matrix engine by decomposing each SQ16 code into two INT8 planes and using AMX multiply-add operations to compute near-exact distances, despite AMX’s lack of native SQ16 support.

**Comparison with existing approaches.**  1 summarizes the design space. CABANA is fast and memory- efficient but can limit recall. IVF-Flat preserves accurate distances but incurs high compute and memory costs. ScaNN recovers recall through reranking but stores both compact codes and raw vectors. ADSampling and DADE reduce arithmetic but do not map cleanly to dense AMX execution. KatoANN combines high recall, high throughput, and a small<tbc>

<tbc>memory footprint by deriving both its inexpensive ranking distance and near-exact refinement distance from one resident SQ16 code.

## 3 KATOANN DESIGN

### 3.1 System Overview

KatoANN is a partition-family ANN search system built around one design principle. Each database vector is stored only once, as a resident SQ16 code, and every scan stage derives its distances from that code. This principle eliminates the common split between a compact lossy scan code and a second raw vector copy for refinement. The remaining challenge is to make this higher-precision code fast on a CPU matrix engine that natively favors low-precision operands. KatoANN addresses this challenge by turning the IVF scan into a dense batched matrix computation and by paying the full SQ16 distance only where it is needed.

The design proceeds by removing the cost that would otherwise appear after the previous step.

\(\bullet\) First, AMX can efficiently execute dense low-precision matrix multiplies, but it does not natively support the SQ16 precision required for high recall. KatoANN therefore splits each SQ16 coordinate into two byte planes whose four INT8 partial products recombine into the SQ16 dot product. This makes near-exact SQ16 distance available on a low-precision matrix engine.<tbc>

\(\bullet\) Second, computing this full SQ16 distance for every probed candidate would waste computation, because most candidates are far from the final top-_K_. KatoANN therefore uses a recall-adaptive rank-then-refine cascade. A cheap<tbc>

q0
Batched coarse search ($ 3.4)
Batched byte-split fine scan ($ 3.2)
Rank
Refine
qn
Full dims
Query batch
High bytes
Centroids
Top-K
query
OR
Prefix dims
High recall
Cluster 0
: q1, q3, q4...
code
Cluster 3
: q0, q2, q7... Moderate recall
Low bytes query code
Survivors
Feeding the matrix engine ($ 3.3)
Matrix engine

**Figure 4: The KatoANN query pipeline. A batched coarse-search kernel scores all centroids and chooses the clusters to probe. The fine scan then groups queries by probed cluster, ranks all probed candidates with a cheap high-byte key, and, when the recall target requires higher precision, refines only the survivors with the full SQ16 byte-split distance. Both ranking and refinement use the same resident SQ16 code, so KatoANN keeps no raw- vector copy. On high-dimensional data, the ranking pass reads only a rotated prefix.**

