## 1 Introduction

Arguably the most fundamental graph problems in fine-grained complexity are concerned with finding small cliques of various kinds, especially triangles (3-cliques). Among the large class of problems that are known to be _subcubic equivalent_ to the All-Pairs Shortest Paths (APSP) problem, the most basic such problem is Negative Triangle: find a triangle with negative edge sum in an edge-weighted graph [37]. Both the quadratic-time hardness of the infamous 3SUM problem and the cubic-time hardness of the APSP problem imply several hardness hypotheses for triangle problems:

the hypothesis that the Exact Triangle problem, of finding a triangle with edge sum zero [38] in an edge-weighted graph, requires _n_<sup>3-_o_(1)</sup> time, and

the hypothesis that the All-Edges Sparse Triangle problem, of determining whether each edge in an _n_-node graph with max degree at most \(n^\delta\) participates in a triangle, requires \(n^{1+2\delta-o(1)}\) time [39].

Similarly, for the All-Edges Sparse Monochromatic Triangle problem, where we have an _n_-node graph with colors on its edges and maximum degree at most \(n^\delta\) and we want to determine which edges participate in monochromatic triangles, it is known that the problem requires \(n^{1+2\delta-o(1)}\) time under both the APSP and the 3SUM hypotheses [31, 39].

Already from the work of Fredman in 1976 [24] leading up to the work of Williams [40] on APSP, it has been known that Negative Triangle can be solved in _o(n_<sup>3</sup>) time on _n_-node graphs, with the best known running time being \(n^3/2^{\Omega(\sqrt{logn})}\) [40]. In contrast, there have been no reported improvements over the obvious running times for All-Edges Sparse Triangle, Exact Triangle, and All-Edges Sparse Monochromatic Triangle. In this paper, we present improved algorithms for all three of these problems.

Our Results for Triangles in Sparse Graphs. For a parameter \(\delta\in(0,1/2]\), the All-Edges Sparse Triangle problem asks: _given an n-node graph where each node has degree at most_ \(n^\delta\)_, decide whether each edge of the graph is in a triangle._

Although for dense graphs, it is well-known that matrix multiplication leads to faster algorithms [6], the best known algorithm for All-Edges Sparse Triangle simply enumerates all pairs of neighbors from each node, taking \(O(n^{1+2\delta})\) time. Under standard fine-grained hardness assumptions, there is a matching lower bound. The work of P ̆atra ̆cu [32] showed that the problem requires \(n^{1+2\delta-o(1)}\) time under the 3SUM hypothesis. Vassilevska W. and Xu [39] showed the same lower bound holds under the Exact Triangle Hypothesis (the hypothesis being that the problem requires _n_<sup>3-_o_(1)</sup> time). We note that this reduction incurs an _O_(log_n_) factor, and therefore shaving a log factor from All-Edges Sparse Triangle does not immediately carry over to Exact Triangle. Chan, Vassilevska W. and Xu [14] gave a similar conditional lower bound assuming that either APSP or 3SUM over the reals cannot be solved in \(n^{3-\varepsilon}\) time or \(n^{2-\varepsilon}\) time, respectively.

We present the first improvement over the trivial algorithm for the problem. To keep ourselves honest (disallowing arbitrary multiplications and disallowing arbitrary lookup tables of size 2_<sup>w</sup>_), our computational model will be the Word RAM model with AC0 operations on words of _w_ bits. That is, our unit-time operations are restricted to those that computed on a constant number of _w_-bit words, by a poly(_w_)-size AC0 circuit. (Note \(w=\Theta(logn)\) is the standard choice.) This is a standard model; see Section 2 for more details.

Please observe we are making a _restriction_ on the standard Word RAM model. When \(w\le\delta logn\) for \(\delta<1\), our algorithms can be implemented with lookup tables for practically any reasonable random-access model with constant-time lookup. Our theorems imply not

