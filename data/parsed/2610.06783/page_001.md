Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs

**Abstract**

We give the first polynomial improvements over the textbook algorithms for 3SUM and All-Pairs Shortest Paths (APSP): we show how to deterministically solve 3SUM on _n_ integers of polynomial size in _O(n_<sup>1.9992</sup>) time and APSP on directed _n_-vertex graphs with polynomially bounded integer weights in _O(n_<sup>2.9995</sup>) time. This refutes the 3SUM and APSP hypotheses of fine-grained complexity theory. Using known reductions, we also refute the real-valued versions of the 3SUM and APSP hypotheses, the Exact Triangle hypothesis, the Zero-Weight _k_-Clique hypotheses, and the three rectangular hinted Online Matrix–Vector conjectures of van den Brand, Nanongkai, and Saranurak, and we give polynomial speedups for a variety of other problems.

All of these results follow from a single new algorithm for thin matrix products. Let _X_ be an \(N\times D\) integer matrix and _Y_ a \(D\times N\) integer matrix with \(D\le N^{1/18}\), and let _W_ be any set of at most \(N^2/\sqrt{D}\) positions. We compute the entries (_XY_)[_I,J_], \((I,J)\in W\), in _O(N_<sup>2</sup>_/D_<sup>0.063</sup>) operations, which is polynomially less than the time needed to write down _XY_ or to compute \(N^2/\sqrt{D}\) inner products one by one. We design this algorithm by modifying a variant of Coppersmith’s rectangular matrix multiplication algorithm, built from a ten- multiplication identity of Schönhage, to perform only the operations needed for the entries in _W_, and show that few operations are needed. Interpreted as a graph algorithm, this solves the All-Edges Sparse Triangle problem in truly subquadratic time on sparse lopsided tripartite graphs where two parts have _n_ vertices but one part has \(n\varepsilon\) vertices for \(\varepsilon<0.12\). By known reductions, Exact Triangle, and hence 3SUM and APSP, reduce to this problem. We also give a data structure version that answers queries for single entries of _XY_, not known in advance.

We view this as a great success for fine-grained complexity, whose main focus has been reductions that uncover connections between problems. So far these reductions have mostly served to infer conditional hardness, since 3SUM and APSP themselves resisted improvement for so long. But reductions are also algorithms, and they allow a single new technique to speed up a wide range of problems at once. This opens new directions in both algorithm design and complexity.

_Claude, an AI model developed by Anthropic, discovered the algorithm that refutes the_ 3_SUM, APSP, and Exact Triangle hypotheses. The authors then worked to understand, simplify, strengthen, and extend the algorithm, derive additional consequences, and make the presentation accessible. See "Acknowledgments and Methodology" for how the result was found and shared with the authors. The authors take full responsibility for this paper._

_Claude also verified this paper’s main results using the Lean 4 proof assistant with the Mathlib library._

arXiv:2610.06783v1 [cs.DS] 5 Oct 2026

Josh Alman Columbia University

Virginia Vassilevska Williams MIT

