high-byte pass ranks all candidates, and the full SQ16 distance is paid only for the survivors. At low and moderate targets the ranking alone suffices and the low-byte plane is never read; high targets enable the refinement.<tbc>

\(\bullet\) Third, batching only helps if many queries reuse the same loaded database block. KatoANN therefore schedules the IVF scan by cluster rather than by query and stores code blocks in the tile-major layout consumed by AMX. This turns the scan from a single-query streaming loop into a dense query-by-code matrix multiply, increasing code reuse and keeping the matrix engine busy.<tbc>

\(\bullet\) Fourth, once the fine scan becomes fast, other costs become visible. KatoANN applies the same batched SQ16 scan to coarse search, avoiding an additional approximate router and its routing error (§3.4). It also keeps top-_K_ selection off the critical path so scalar heap updates do not stall the matrix engine (§3.4). For high-dimensional embeddings, a dimension cascade shortens the ranking pass itself, cutting the per-candidate work to a rotated prefix of the coordinates (§3.5).

**Life of a query batch.** Figure 4 shows how a batch moves through KatoANN. A serving batch first enters the coarse search, which scores the batch against all centroids and selects the nprobe nearest clusters per query. KatoANN then inverts the schedule from query order to cluster order. Each cluster is scanned once, in one dense matrix multiply against all the queries that probe it. The fine scan orders the probed candidates by the high-byte key. At lower recall targets this ordering already yields the final top-_K_; at higher ones the top \(S=R\cdot K\) per query continue into the full SQ16 refinement, where _R_ is the survivor factor determined by a one- time calibration. For high-dimensional data, the calibration also chooses the prefix length _d_<sub>0</sub> per recall target.

## 3.2 Byte-Split and Rank-then-Refine

**SQ16 as the scan code.** The matrix engine reaches its highest throughput on low-precision operands such as INT8 and BF16. Using those formats directly is fast, but it can blur the close-distance candidates that decide recall near exact KNN. KatoANN therefore stores each coordinate as a 16-bit scalar- quantized code, SQ16, as Figure 5 (a) illustrates. Unlike BF16, which spends many bits on exponent range, SQ16 uses the full 16-bit grid to resolve values within the data range. The resulting distance is not bit-identical to FP32, but it is near- exact for ANN ranking in our target regime. The problem is that AMX has no native 16-bit integer matrix multiply. The byte split below is what lets KatoANN keep SQ16 precision while still executing on the engine’s INT8 path.

Let an SQ16 coordinate be written as _x_=2<sup>8</sup>_x<sub>h</sub>+x<sub>l</sub>_ and _q_=2<sup>8</sup>_q<sub>h</sub>+q<sub>l</sub>_. Then the dot product decomposes as

\(\langle q,x\rangle=2^{16}\langle q_h,x_h\rangle+2^8\big(\langle q_h,x_l\rangle+\langle q_l,x_h\rangle\big)+\langle q_l,x_l\rangle.\) (3)

Each term is an INT8 matrix multiply over byte planes, and the shifted sum reconstructs the full SQ16 dot product. For _L_<sub>2</sub>, KatoANN combines this dot product with cached per- vector terms and per-batch query terms:

\(\|q-x\|^2=\|q\|^2+\|x\|^2-2\langle q,x\rangle.\) (4)

The affine SQ16 scale and zero point are applied after recombination; terms independent of the query are cached with the vector code.

**Why two byte planes suffice.** The byte split does not approximate the SQ16 code. It is the exact two-byte representation of the code. Thus, four partial products are enough to reconstruct the SQ16 dot product, with no additional rounding after SQ16 quantization. Each INT8 tile multiply accumulates into INT32; KatoANN promotes the partial sums before the 2<sup>8</sup> and 2<sup>16</sup> shifts, avoiding overflow for the dimensions we target. For UINT8-native datasets, KatoANN dispatches directly to the native byte dot product. For cosine distance, KatoANN uses the same path on normalized vectors.

**One code, two precisions.** The full byte split provides the precision needed for high recall while naturally exposing a cheaper ranking key. The high-by-high term \(\langle q_h,x_h\rangle\) is one of the four SQ16 partial products and, together with cached high-byte norms, gives the exact _L_<sub>2</sub> distance between the high-byte truncations of the query and database vector. This key is not computed from a separate lossy representation. It comes from the same SQ16 code and requires reading only the high-byte plane. Thus, KatoANN can first rank candidates using a partial view of the SQ16 code and compute the full SQ16 distance only where necessary.

**Rank all, refine few.** Computing all four INT8 product streams for every probed candidate would waste most of<tbc>

(a) SQ16 byte-split
(b) Rank-then-refine cascade
Query q
x
All probed candidates N
qh ql
Xh
High-byte ranking: one INT8 tile-multiply
q = 28 qh + ql
X = 28 xh + xl
hh
hl
lh
ll
Survivors S = R K
Same SQ16 code
INT8 216 + ( INT8 + INT8 28 + INT8 qhxh
Full SQ16 refinement: four INT8 tile-multiplies
qhxh
qhxh
Full SQ16 dot product

**Figure 5: The SQ16 rank-then-refine mechanism. (a) Each SQ16 coordinate is stored as high and low byte planes; four INT8 tile-multiply streams reconstruct the full SQ16 dot product. (b) KatoANN ranks all** _N_ **probed candidates with the high-byte product, then pays the full four-term SQ16 distance only for** _S_ **survivors. Both stages use the same SQ16 code, reducing work from** 4_N_ **to** _N_+4_S_ **without a raw-vector copy.**

