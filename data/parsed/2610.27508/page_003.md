<tbc>systems commonly scan compressed or low-precision codes instead of raw vectors. For example, ScaNN \[18\] scores candidates using compact asymmetric-hashing codes, while Faiss \[11\] provides IVF variants based on scalar quantization (SQ) and product quantization (PQ). These codes reduce memory traffic but introduce distance error. The error matters most among nearby candidates, where small score differences determine whether a true neighbor enters the result. At high recall, increasing the number of probed clusters may therefore stop helping because quantization error becomes the limiting factor.

**Reranking adds memory and compute costs.** A common solution is to scan compact codes and rerank the survivors using raw vectors or another more accurate representation. This recovers recall but requires storing the accurate representation alongside the compact codes. It also introduces a second distance pass whose cost grows with the survivor set at higher recall targets.

Other approaches preserve accurate distances while terminating comparisons after enough dimensions have been examined \[10, 13\]. Although they avoid arithmetic on many candidates, their candidate-dependent and branch-heavy execution does not map well to dense batched computation.

## 2.2 A Case of AMX-Accelerated ANN

KatoANN is an AMX-accelerated ANN search system. We here explain why AMX with batching is the right approach.

**Batching changes the scan to compute-bound.** One assumption for the bandwidth bound is that each loaded vector code serves a single query. However, modern ANN search in data centers should handle multiple concurrent<tbc>

<tbc>queries that can probe the same inverted lists. Therefore, after cluster-aware grouping \[27\], a block of vector codes can be loaded once and multiplied against an effective group of _M_<sub>eff</sub> queries that probe the same list. The arithmetic intensity then rises from _I_≈1 to _I≈M_<sub>eff</sub>, because the same bytes are reused across many queries. By Eq. 1, the scan becomes _compute-bound_ once

\(M_\mathrm{eff}\unknown M^\star=\frac{\pi}{\beta}.\) (2)

Here _M_<sub>eff</sub> is not the total request batch size, but the number of queries that reuse the same candidate block after cluster- aware grouping. When this reuse is large enough, throughput is determined by how many multiply-add operations the CPU can execute, not by how few bytes each vector code stores. At that point, the scan no longer needs to sacrifice precision just to reduce memory traffic.

Figure 3 measures this transition with a BF16 distance kernel on our AMX server (_d_=1024, 2M vectors, 32 threads); CABANA reports the same shape at low dimension. At a batch of 16 queries, AMX delivers only 1.3\(\times\) the AVX-512 rate; as each loaded code block serves more queries, the gap widens to about 14\(\times\) at a batch of 1,024. The engine alone therefore buys little, and the cross-query reuse is what lifts the scan off the bandwidth roof.

**AMX matches distance scans.** A compute-bound batched scan requires a unit that can execute many multiply-add operations in parallel. The AVX-512 SIMD units that existing IVF systems use for the scan compute multiply-add operations over one-dimensional vector registers. A matrix engine executes far more operations per instruction, because<tbc>

\begin{tabular}{cccccc}
 & \multicolumn{5}{c}{ADS/DADE} \\
 & CABANA \[27\] & IVF-Flat \[11\] & \[10, 13\] & ScaNN \[18\] & KatoANN \\
Resident data & BF16 & FP32 & FP32/projection & lossy+FP32 & SQ16 \\
High recall & \<|unk|\> & \<|unk|\> & \(\triangle\) & \<|unk|\> & \<|unk|\> \\
High throughput & \(\triangle\) & \<|unk|\> & \(\triangle\) & \<|unk|\> & \<|unk|\> \\
Memory efficiency & \<|unk|\> & \<|unk|\> & \(\triangle\) & \<|unk|\> & \<|unk|\> \\
AMX-friendly & \<|unk|\> & \(\triangle\) & \<|unk|\> & \<|unk|\> & \<|unk|\> \\
\end{tabular}

(a) Intel AMX organization
C-tile (distances)
tmm0=A
INT8 or BF16
TMUL
tmm1=B
64 Bytes
tmm2=C
A-tile
B-tile
tmm7
Tile register file
16 rows
(b) IVF cluster scan
Q1
V1
Cluster 1
Q16
V16
M queries
Cluster 2
Cluster 3
QM
VN
Queries (M x dim)
Cluster 2 (N x dim)

AMX (TDPBF16PS)
AVX-512 (VDPBF16PS)
103
Throughput (Mpairs/s)
14 x
104
103
16
64
256
1024
Query batch (tile rows)

**Figure 2: Intel AMX and a batched IVF distance scan. (a) AMX provides two-dimensional tile registers and tile-multiply instructions. (b) Queries grouped by probed cluster form one input matrix, and the vector codes in that cluster form the other.**

**Figure 3: BF16 distance-kernel throughput vs. query batch. AMX gains little over AVX-512 at small batches; cross-query reuse widens the gap to about 14\(\times\).**

** 1: Comparison to existing approaches.**

