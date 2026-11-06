3SUM-hard problems
computational geometry: three collinear points (hence minimum-area triangle), point covering, motion planning [GO95], polygon containment [BHP01] strings: jumbled indexing [ACLL14], local alignment [AVW14] set-intersection and set-disjointness data structures [Pät10, KPP16] (for universes larger than in Theorem 3) approximate distance oracles [ABKZ22, ABF23]
Dynamic graph problems [Pät10, AV14, KPP16]: reachability, shortest paths, subgraph connectivity, matching,
3SUM class [GO95, VW10, VW18, FKP24, Pät10, CH20, DGS20, LPV20, CVX23, FJX25]
(min, +)-Convolution class [CMWW19,
All-Edges Sparse Triangle (balanced, m4/3), triangle 3SUM, GeomBase, All-Numbers 3SUM, Convolution-3SUM, 3-Linear [BIS17, CMWW19]
KPS17]: Superadditivity Testing, MaxConv Upper Bound, Unbounded and 0/1 Knapsack with capacity t (time in terms of n + t)
[Pät10, KPP16, VX20, DKPV20, CX24], and 4-cycle listing [ABKZ22, JX23]
Degeneracy Testing (e.g. 3AP), #3SUM; MonoConvolution (baseline n1.5)
[BCD+14]
Zero-Weight k-Clique folding [NP85] here: O(nk-E)
Exact Triangle #Exact Triangle [CVX23] here: truly subcubic
APSP class [VW10, VW18, RV11, AGV15, AGV23, BGMW20, NPS+25, TT00, BDT16]
[VW13, APSP, (min, +)-product, Negative Min-Weight Triangle, Metricity, (min, +)-Product Verification, Minimum Weight Cycle, Replacement Paths, Second Shortest Simple Path, Radius, Median, Betweenness Centrality (for unique shortest paths), Tree Edit Distance, Maximum Subarray
[VX20, CX24, FKP24], Sec. 3.2
Real-valued problems Lopsided All-Edges Sparse Triangle
Sec. 5.2
Definitions 13 and 14
here: truly subquadratic for D = n, E < 0.12
here: truly subcubic
[CVX22]: real 3SUM, real APSP and (min, +)- product, real Exact Triangle
Min/Max- Weight k-Clique folding [NP85] here: O(nk-E)
Directed unweighted APSP (and weights loge n) [CVX21]
Thm. 24, Sec. 5.4
Remark 23
Sec. 5.4
here: truly subquadratic and truly subcubic (Las Vegas)
Hinted OMv [vdBNS19], thin regime: v-hinted Mv, Mv-hinted Mv, uMv-hinted uMv here: polynomially faster than conjectured
3XOR here: truly subquadratic
new, polynomially faster algorithm reductions no longer give evidence of hardness
here: polynomially faster than conjectured
Unaffected: SETH, Orthogonal Vectors, OMv without hints, k-SUM and k-XOR for k 4, 3SUM-Indexing
A B: B is hard under A
A B: A uses the data structure version of our algorithm for B (Theorem 24)

Figure 1: Problems affected by our algorithm, which solves the problem in the orange box (Lopsided All-Edges Sparse Triangle) directly. The problems inside each of the three thick- bordered blue boxes (3SUM class, Exact Triangle, and APSP class) are pairwise equivalent under fine-grained reductions (for MonoConvolution, whose baseline is _n_<sup>1.5</sup>, this means \(O(n^{1.5-\varepsilon})\) time), and we omit the arrows between them. Problems in gray boxes are reached from 3SUM, APSP, or Exact Triangle only by one-way reductions, so our result gives no faster algorithms for them, but these reductions no longer give evidence of hardness. The new algorithms are deterministic except where marked. Citations are to the reductions; for the problems in the top rows, the cited papers contain many more problems of the same kind.

