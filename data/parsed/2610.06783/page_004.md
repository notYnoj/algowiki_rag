Both 3SUM and APSP reduce to the Exact Triangle problem (given a tripartite graph with integer edge weights, is there a triangle whose three weights sum to zero?) [VW13, VW10, VW18]. Through Exact Triangle, both reduce to online Set Disjointness (from the list above), and even to its offline version, in which the query pairs are given in advance together with the sets [VX20, CX24]; for 3SUM, direct reductions are also known [Păt10, KPP16, JX23, ABF23]. In graph terms, offline Set Disjointness is the All-Edges Sparse Triangle problem: given a graph with _m_ edges, decide for every edge whether it lies in a triangle.

All-Edges Sparse Triangle thus inherits the hardness of both 3SUM and APSP, and it is in turn the source of the conditional lower bounds for Set Disjointness data structures, dynamic graph problems, and other problems [Păt10, AV14, KPP16, GLP19]. Many came to regard it as one of the most reliably hard problems in fine-grained complexity, and the evidence seemed good.

All-Edges Sparse Triangle can be solved in _O(m_<sup>3/2</sup>) time just by listing all triangles [IR78, CN85], and a high-degree/low-degree split combined with matrix multiplication [AYZ97] improves this to \(O(m^{2\omega/(\omega+1)})\), where \(2\le\omega<2.372\) is the matrix multiplication exponent.<sup>3</sup> Even if \(\omega=2\), this is _m_<sup>4/3</sup>. On the graphs the reductions produce, which have _n_ vertices of degree about \(\sqrt{n}\), this equals the brute-force running time _n_<sup>2</sup> conjectured to be optimal. Matrix multiplication only seemed useful for dealing with dense inputs, whereas these instances ask for a sparse set of outputs, and it seemed plausible that no technique could do better.

However, a reduction from _A_ to _B_, proved in order to show that _B_ is hard, is also an algorithm for _A_ whenever _B_ turns out to be easy. In this paper we give a new algorithm for a _lopsided_ version of All-Edges Sparse Triangle, in which the graph is tripartite and one of the three parts is significantly smaller than the other two. Most known reductions to All-Edges Sparse Triangle can be slightly modified to produce such instances.

As a consequence, all of the problems in the list above (and many more), except for CNF-SAT and Orthogonal Vectors, have polynomially faster algorithms than before:

• 3SUM: deterministic _O(n_<sup>1.9992</sup>) time for integers of polynomial size (Theorem 22), and for real numbers, a Las Vegas algorithm with _O(n_<sup>1.998</sup>) expected time whose only operations on real numbers are comparisons, additions, and subtractions (Theorem 35).<tbc>

• **APSP**: deterministic _O(n_<sup>2.9995</sup>) time for polynomially bounded integer weights, and the same bound for the (min,+)-product (Theorem 22), and for real weights, Las Vegas algorithms with _O(n_<sup>2.998</sup>) expected time, again using only comparisons, additions, and subtractions on real numbers (Theorem 35).<tbc>

• **Directed Unweighted APSP**: a deterministic algorithm running in \(O(n^{2+\mu-\varepsilon^{\prime\prime}})\) time for some constant \(\varepsilon''>0\), where \(\mu<0.5275\) is defined by \(\omega(1,\mu,1)=1+2\mu\), and \(\omega(1,\mu,1)\) is the exponent of multiplying an \(n\times n^\mu\) by an \(n^\mu\times n\) matrix. Note that \(\widetilde{O}(n^{2+\mu})\le O(n^{2.5275})\) is the longstanding running time of Zwick’s algorithm. This is the first improvement over Zwick’s algorithm that does not come from faster rectangular matrix multiplication, and it refutes the Directed Unweighted APSP hypothesis [CVX21, CVX23, Fis26] (Theorem 34).<tbc>

• **Tree Edit Distance**: _O(n_<sup>2.9995</sup>) time for polynomially bounded integer costs via the tight reduction of [NPS<sup>+</sup>25].<tbc>

• **Online Set Disjointness**: for \(D\le N^{0.12}\), a deterministic data structure whose pre- processing time is polynomially less than _N_<sup>2</sup> and whose query time is polynomially less<tbc>

<sup>3</sup>Triangle detection in _n_-vertex graphs has long been known to be reducible to matrix multiplication [IR78].

