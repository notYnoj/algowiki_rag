<tbc>Given this random assignment, we need to evaluate \(P_\Delta(G)\) at \(\mathbf{r}=(r_{w_1},\dots,r_{w_m})\) in \(\widetilde{O}(n^\omega)\) time. To this end, we construct an \(n\times n\) matrix _A_ where _A<sub>u,v</sub>=r_<sub>_w(u,v_)</sub> if \((u,v)\in E(G)\), and 0 otherwise. The value of the polynomial evaluated at **r** is simply \(\frac{1}{6}\mathrm{Tr}(A^3)\) which is equal to the sum of weighted triangles in the graph with adjacency matrix _A_ and can be computed via fast matrix multiplication in \(\widetilde{O}(n^\omega)\) query time.

To summarize, during the preprocessing phase, we evaluate \(P_\Delta(G_i)(\mathbf{r})\) for each prior _G<sub>i</sub>_ and store this field element as its invariant representation. This requires \(\widetilde{O}(kn^\omega)\) total preprocessing time. When we receive a query graph _H_, we evaluate \(P_\Delta(H)(\mathbf{r})\) using the exact same random assignment **r** in \(\widetilde{O}(n^\omega)\) time. We then simply find a prior graph _G<sub>i</sub>_ that evaluates to the identical scalar value and return its precomputed solution _OPT(G<sub>i</sub>_). This takes \(\widetilde{O}(n^\omega)\) query time.<sup>9</sup> We can guarantee that, with high probability<sup>6</sup>, the random point **r** chosen during the preprocessing phase is such that, for every _i_, \(P_\Delta(G_i)(\mathbf{r})=P_\Delta(H)(\mathbf{r})\) if and only if \(P_\Delta(G_i)\equiv P_\Delta(H)\). Thus, the answer given in the query phase is correct with high probability.

Additionally, if the actual negative triangle _T<sub>i</sub>_ in _G<sub>i</sub>_ is provided, we can find a negative triangle in _H_ by reducing the problem to unweighted triangle detection, which takes \(O(n^\omega)\) time \[Ita77\]. (Roughly speaking, this is done by detecting an unweighted triangle in a tripartite graph consisting only of edges whose weights match those of _T<sub>i</sub>_.)

To solve the Constrained Spanning Tree (CST) problem, we similarly define the _spanning tree polynomial_ of a graph _G_ as

\(P_{ST}(G):=\sum_{w_1\le\cdots\le w_{n-1}}c_{w_1,\dots,w_{n-1}}(G)\prod_{i=1}^{n-1}x_{w_i}\)

where _c_<sub>_w_<sub>1</sub>_,...,w_<sub>_n_-1</sub></sub>(_G_) is the number of spanning trees with the weight multiset {_w_<sub>1</sub>_,...,w_<sub>_n_-1</sub>}.

We leverage the fact that this multivariate polynomial can be efficiently evaluated at a random point _r_ by invoking Kirchhoff’s Matrix Tree Theorem. Specifically, this evaluation reduces to computing the determinant of a randomized Laplacian matrix, which takes \(\widetilde{O}(n^\omega)\) time via fast matrix multiplication. If the optimal tree _T<sub>i</sub>_ in _G<sub>i</sub>_ is provided, we can reconstruct a corresponding optimal tree _T_ in _H_ via matroid intersection in polynomial time \[Sch03\], and specifically in \(\widetilde{O}(m\sqrt{n})\) time via recent advancements \[BMNT23, CLS<sup>+</sup>19, GS85\]. Full details and the formal algebraic constructions are deferred to Section 6.2.

<sup>9</sup>There are some polylogarithmic factors needed to guarantee high success rate and for searching for the desired graph _G<sub>i</sub>_.

