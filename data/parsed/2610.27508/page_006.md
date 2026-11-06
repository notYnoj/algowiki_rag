<tbc>the work on candidates that cannot enter the final top-_K_. Figure 5 (b) shows how KatoANN separates ranking from refinement. Phase 1 ranks all probed candidates using the high-byte key, requiring one INT8 product stream per candidate. If this ranking is sufficient for the target recall, KatoANN directly returns its top-_K_. Otherwise, Phase 2 selects the top _S=R-K_ candidates from the high-byte ranking, computes their full four-term SQ16 distances, and chooses the final top-_K_ from the refined set.

**Calibrating the cascade.** The survivor factor _R_ is calibrated for each index and recall target. Using a labeled query sample, calibration jointly sweeps npprobe and _R_, with the full byte-split scan serving as the precision reference. npprobe determines coverage by controlling which clusters are scanned, whereas _R_ determines how many candidates within those clusters receive the full SQ16 distance. The calibration selects the smallest _R_, including no refinement, that reaches the target recall.

**Why the cascade stays near the cost of a lossy pass.** For _N_ probed candidates, a full byte-split scan performs four INT8 product streams per candidate, for a total cost of 4_N_. The cascade instead performs one stream for all candidates and four streams for only the \(R\cdot K\) survivors, yielding dominant work of _N_ + 4_RK_. Because the INT8 ranking pass also packs more coordinates into each tile than a BF16 pass, its bulk scan is no more expensive than a conventional low-precision scan over the same candidates. The additional SQ16 work is confined to a small survivor set and is incurred only when the target recall requires refinement.

## 3.3 Feeding the Matrix Engine

The SQ16 cascade reduces arithmetic, but it only helps if the matrix engine is kept busy. KatoANN uses two mechanisms for this feed problem. As illustrated in Figure 6, cluster-to- query inversion creates reuse across queries that probe the same list, and the VNNI-order code layout makes each AMX tile load contiguous.

**Cluster-to-query inversion.** AMX multiplies a query tile, the A-tile, by a code tile, the B-tile, and accumulates a block of distances. To use this shape efficiently, the scan needs many queries to share the same code tile. A naive per-query IVF loop does the opposite; it scans the probed lists of each query separately, so codes stream repeatedly with little reuse and the query tile is often underfilled. KatoANN therefore groups work by cluster. For each cluster _c_, it gathers the _M<sub>c</sub>_ queries in the batch that probe _c_ and scans the cluster once against those queries. The expected reuse is

\(M_c\approx\frac{B\cdot\text{nprobe}}{\text{nlist}},\) (5)

up to skew in centroid popularity, where _B_ is the request batch size. When _M<sub>c</sub>_ is large, a loaded code block is reused across many queries, increasing arithmetic intensity and moving the scan toward the compute-bound regime. When _M<sub>c</sub>_ is small, KatoANN still executes the same loop with shorter tiles rather than padding all clusters to a fixed size. The scan is blocked so that the active query tile and code tile stay close to the core while the inverted list is streamed.

**VNNI-order multi-bit code layout.** Cluster-to-query inversion creates the right computation, but the engine can still stall if each B-tile has to be assembled from scattered memory locations. A dimension-major layout is natural for a single-query SIMD loop, because it stores the coordinates of one vector consecutively. For AMX, however, the B-tile consumes a byte stripe across a block of database codes and dimensions. If the codes remain in dimension-major order, the runtime must gather strided pieces to form every tile. KatoANN therefore stores each cluster in a VNNI-order tensor whose innermost block matches the B-tile stripe. The build cost is a permutation pass per cluster. At query time, each tile load reads a contiguous byte stripe, and the same layout serves both the high-byte ranking pass and the full byte-split refinement.

## 3.4 Batched Coarse Search and Selection

**The new bottleneck.** IVF search first chooses the nearest centroids, then scans their inverted lists. When the fine scan is slow, the centroid scan and top-_K_ maintenance are usually hidden behind the scan cost. After the SQ16 cascade and AMX batching reduce the fine-scan cost, these surrounding stages become visible and can cap throughput. KatoANN therefore applies the same design rule to the rest of<tbc>

(a) Cluster-to-query inversion
Reused by M, c queries
B-tile
C1 codes
q1
C1
C3
C1
q1
q3
q2
C2
C3
Invert
C2
q2
q3
A-tile
C-tile
by cluster
q3
C1
C2
C3
q1
q2
queries
(b) VNNI-order layout
V1 code
V2 code
V3 code
Dimension-major packing
D
D3
D n
D
D3
D n
D
D3
D n
Strided tile pieces
Build-time permutation
B-tile
Contiguous tile stripe
Tile-major packing
D
D
D
D
D
D
D

**Figure 6: How KatoANN feeds AMX. (a) Cluster-to- query inversion groups the queries that probe the same inverted list, so one loaded code block is reused across an effective batch** _M<sub>c</sub>_**. (b) VNNI-order layout stores exactly the byte stripe consumed by an AMX B-tile contiguously, avoiding scatter-gather tile construction.**

