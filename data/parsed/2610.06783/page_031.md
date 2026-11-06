## 3.1 The Lopsided All-Edges Sparse Triangle problem

We define a lopsided (rectangular) version of the well-studied problem All-Edges Sparse Triangle. When viewed in graph terms, Theorem 5 counts the triangles through prescribed pairs of vertices in a tripartite graph whose middle part is small, and thus in particular can be used to solve All-Edges Sparse Triangle in such graphs.

**Definition 13** (Lopsided All-Edges Sparse Triangle, Lop-AE-SparseTri(_n,D_))**.** We are given an unweighted undirected tripartite graph with two parts _A_ and _B_ of _n_ vertices each and a middle part _M_ of at most _D_ vertices, with arbitrary edges in \(M\times A\) and \(M\times B\). Let \(W\subseteq A\times B\) be the set of edges between _A_ and _B_. Decide, for every edge \((a,b)\in W\), whether it lies in a triangle with some vertex of _M_, that is, whether _a_ and _b_ have a common neighbor in _M_.

In this notation, the usual All-Edges Sparse Triangle problem is the balanced case _D=n_ (after the standard reduction to tripartite graphs), except that one asks about every edge of the graph, not only those between _A_ and _B_, and that the running time is measured in terms of the number _m_ of edges. We think of _W_ as being polynomially smaller than _n_<sup>2</sup> and _D_ as polynomially smaller than _n_, so the instance is sparse in this sense. The brute-force algorithm solves Lop-AE-SparseTri(_n,D_) in _O_(|_W|D_) time. If \(D\le n^{0.321}\), then, since \(0.321\le\alpha\left[\text{VXXZ24}\right]\),<sup>7</sup> fast rectangular matrix multiplication can solve the problem in _n_<sup>2+_o_(1)</sup> time even when |_W_|=_n_<sup>2</sup>. We will beat both |_W|D_ and _n_<sup>2</sup> for \(D=n^\varepsilon\) and \(|W|=n^2/\sqrt{D}\) with a constant \(\varepsilon>0\), and this will suffice to refute both the 3SUM and the APSP hypotheses.

Some of the known reductions, such as those from the real-valued problems in Section 5.2, reduce to the counting version of All-Edges Sparse Triangle, which asks for the number of<tbc>

<sup>7</sup>Here \(\alpha\) denotes the supremum of the constants \(\alpha\in(0,1]\) such that \(n\times n^\alpha\) by \(n^\alpha\times n\) matrices can be multiplied using _n_<sup>2+_o_(1)</sup> operations.

3SUM
APSP
(Thm. 22)
(Thm. 22)
[CH20, VW13], Thm. 21(a)
[VW10, VW18, VW13], Thm. 21(b)
Exact Triangle
(Thm. 19)
[VX20, CX24, FKP24], Thm. 17
Lopsided All-Edges Sparse Triangle
(Cor. 15), (Cor. 16)
Straightforward (Sec. 3.1)
Certain entries of a thin matrix product
(Thm. 5), (Cor. 26)

Figure 8: The reductions of this section. Each arrow is a reduction, labeled with the prior work it follows and with the statement here that proves it. Each box gives two running times: the first follows from Theorem 5, and the second from its stronger form, Corollary 26. We reprove only the reduction from Exact Triangle to Lopsided All-Edges Sparse Triangle, deterministically and for the parameters of the matrix theorem; the reductions from 3SUM and APSP are cited as they are. The running times in the two bottom boxes assume \(n\ge D^{18}\) and \(|W|\le n^2/\sqrt{D}\).

