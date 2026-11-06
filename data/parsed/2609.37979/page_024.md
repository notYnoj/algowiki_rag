exist a _G<sub>i</sub>_ with \(f_\Delta(G_i)=f_\Delta(H)\) and \(OPT(G_i)\neq OPT(H)\). By using the same argument as above, we obtain that the probability of this happening is at most \(\frac{3k}{p}\le k^{-1}n^{-log(n)}\). Thus, our success probability is at least 1-_k_<sup>-1</sup>_n_<sup>-log(_n_)</sup> and there w.h.p with respect to the query size _n_.

**Reconstruction:** Assume that for each graph \(G_i\in\mathcal{S}\) containing a negative triangle, we are provided with a multiset of edge-weights \(W_i:=\{w_1^{(i)},w_2^{(i)},w_3^{(i)}\}\) that form such a triangle. Suppose the algorithm is queried on a graph _H_ such that \(P_\Delta(H)\equiv P_\Delta(G_i)\) for some \(G_i\in\mathcal{S}\). By Lemma 6.5, _H_ must also contain a triangle with the identical multiset of edge-weights _W<sub>i</sub>_; i.e., such a triangle has total weight \(w_1^{(i)}+w_2^{(i)}+w_3^{(i)}<0\).

To find this specific negative triangle in _H_, we construct an auxiliary tripartite graph \(H'\) with vertex sets _V_<sub>1</sub>_,V_<sub>2</sub>_,V_<sub>3</sub>, where each _V<sub>j</sub>_ is a copy of _V(H_). For every vertex \(v\in V(H)\), let _v<sub>j</sub>_ denote its copy in _V<sub>j</sub>_. For every edge {_u,v_} in _H_ with weight \(w_1^{(i)}\), we add an undirected unweighted edge {_u_<sub>1</sub>_,v_<sub>2</sub>} to \(H'\). Similarly, for every edge {_u,v_} in _H_ with weight \(w_2^{(i)}\), we add an undirected unweighted edge {_u_<sub>2</sub>_,v_<sub>3</sub>} to \(H'\), and for every edge with weight \(w_3^{(i)}\), we add an undirected unweighted edge {_u_<sub>3</sub>_,v_<sub>1</sub>} to \(H'\). Observe that any triangle in \(H'\) must consist of one vertex from each partition. Thus, an unweighted triangle in \(H'\) corresponds to a triangle in _H_ with the desired edge-weights. Since triangle detection in unweighted graphs can be performed in \(O(n^\omega)\) time \[Ita77\], we can find the negative triangle in _H_ in \(O(n^\omega)\) total time.

## 6.2 Constrained Spanning Tree

**Definition 6.6** (Constrained Spanning Tree (CST) Problem \[AAN82, RG96\])**.** Let _G_=(_V,E,c,d,B_) be an undirected graph with two non-negative edge-weight functions<tbc>

\(c:E\rightarrow\mathbb{R}_{\ge 0}\text{and}d:E\rightarrow\mathbb{R}_{\ge 0},\)

<tbc>and let \(B\in\mathbb{R}_{\ge 0}\) be a budget. The Constrained Spanning Tree _Problem_ asks to find a spanning tree \(T\subseteq E\) that

\(\text{minimizes}c(T):=\sum_{e\in T}c(e)\)<br>
\(\text{subject to}\sum_{e\in T}d(e)\le B.\)

A spanning tree satisfying the constraint is called _budget-feasible_. The optimal value is _OPT(G_) for the optimal value of a problem instance _G_. If no spanning-tree satisfies the budget constraint then \(OPT(G)=\infty\).

Two problem instances _G_=(_V,E,c,d,B_) and \(G'=(V',E',c',d',B')\) of CST are isomorphic if \(B=B'\) their underlying graphs are isomorphic. Note that an isomorphism has to preserve vertex attributes and edge attributes. Therefore, CST is closed under isomorphism.

Note that each edge \(e\in E\) is associated with two different attributes _c(e_) and _d(e_). We combine these two attributes and say that \(w(e):=\alpha_G^E(e)=(c(e),d(e))\) is the weight of the edge _e_. Note that isomorphism respect weights.

Like in the CSP case, we need to develop a method to find a spanning with certain weight constraints via polynomials. To this end, we associate a formal variable _x<sub>w</sub>_ with every distinct edge weight _w_. The _spanning tree polynomial_ of _G_ is defined as

\(P_{ST}(G):=\sum_{w_1\le\cdots\le w_{n-1}}c_{w_1,\dots,w_{n-1}}(G)\prod_{i=1}^{n-1}x_{w_i}\)

where _c_<sub>_w_<sub>1</sub>_,...,w_<sub>_n_-1</sub></sub>(_G_) is the number of spanning trees with the weight multiset {_w_<sub>1</sub>_,...,w_<sub>_n_-1</sub>}. Note that this polynomial is closely related to the _Kirchhoff polynomial_ (See \[CY00\]).

