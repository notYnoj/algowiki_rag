# Maximum Common Subgraphs

13<tbc>

<tbc>_V(K_) such that \(\{a,b\}\notin E(K)\subseteq E(G)\). By definition, there are distinct indices \(i,j\in\{1,\dots,n\}\) such that \(\{a_i,b_i\}\in E(G_i)\) but \(\{a_j,b_j\}\notin E(G_j)\). Note that \(\{\varphi_i(a_1),\varphi_i(b_1)\}=\{a_i,b_i\}\) and \(\{\varphi_j(a_1),\varphi_j(b_1)\}=\{a_j,b_j\}\). Hence, \(\{\varphi_i(a_1),\varphi_i(b_1)\}\in E(G_i)\) implies \(\{a_1,b_1\}\in E(G_1)\) while \(\{\varphi_j(a_1),\varphi_j(b_1)\}\notin E(G_j)\) implies \(\{a_1,b_1\}\notin E(G_1)\); a contradiction. Thus, _K_ is a complete subgraph in _G_. Assume now, for contradiction, that _K_ is not a maximal clique. Hence, there is a complete subgraph \(\tilde{K}\) in _G_ such that \(K\unknown\tilde{K}\). Let \(x\in V(\tilde{K})\backslash V(K)\) and consider the graph \(K'\) that is induced by the vertices in \(V(K)\cup\{x\}]\). By definition, _x_ is adjacent to each vertex _w_ in _K_. Hence, either _p<sub>i</sub>(x_) is adjacent to _p<sub>i</sub>(w_) for all \(i\in\{1,\dots,n\}\) or _p<sub>i</sub>(x_) is not adjacent to _p<sub>i</sub>(w_) for all \(i\in\{1,\dots,n\}\). It is now a straightforward task to verify that \(V(H_i)\cup\{p_i(x)\}\) induces a subgraph \(H'_i\) in _G<sub>i</sub>_ such that \(H_i\unknown H'_i\) and such that \(H'_i\simeq H'_j\); a contradiction to the maximality of _H_. Consequently, _K_ must be a maximal clique in _G_.

To establish Proposition 1 we need the following result.

**Lemma 2.** _If K is a clique in_ \(\star_{i=1}^nG_i\)_, then the graph H induced by the vertex set_ \(\{p_i(w)|w\in V(K)\}\) _in G<sub>i</sub> is a common induced subgraph of G_<sub>1</sub>_,...,G<sub>n</sub> of size_ |_V(H_)|=|_V(K_)| _for every_ \(i\in\{1,\dots,n\}\).

_Proof._ Suppose that there is a clique _K_ in \(G:=\star_{i=1}^nG_i\). Since _K_ is a complete graph, definition of the ⋆-product implies that distinct vertices \(\tilde{u}=(\tilde{u}_1,\dots,\tilde{u}_n)\) and \(\tilde{w}=(\tilde{w}_1,\dots,\tilde{w}_n)\) in _K_ differ in each of their _i_-th coordinates, i.e., \(\tilde{w}_i\neq\tilde{u}_i\) for all \(i\in\{1,\dots,n\}\). Thus, we may assume w.l.o.g. that each vertex \(\tilde{v}\in V(K)\) has coordinates \(\tilde{v}=(v,\dots,)\); just relabel the vertices in _V(G<sub>i</sub>_), \(1\le i\le n\), if needed. Hence, \(\{\tilde{w},\tilde{u}\}\in E(K)\) implies that either \(\{w,u\}\in E(G_i)\) for all \(i\in\{1,\dots,n\}\) or \(\{w,u\}\notin E(G_i)\) for all \(i\in\{1,\dots,n\}\). Thus, the subgraph _H<sub>i</sub>_ incuded by \(\{w|\tilde{w}\in V(K)\}\) in each _G<sub>i</sub>_ satisfy \(H_i\simeq H_j\) for all \(i,j\in\{1,\dots,n\}\). Thus, _H_:=_H_<sub>1</sub> is a common subgraph of _G_<sub>1</sub>_,...,G<sub>n</sub>_. Since distinct vertices \(\tilde{u}\) and \(\tilde{w}\) in _K_ differ in their _i_-th coordinates, we have |_V(K_)|=|_V(H_)|. The latter arguments, in particular, imply that a common subgraph _H_ of _G_<sub>1</sub>_,...,G<sub>n</sub>_ is isomorphic to the graph induced by the vertex set \(\{p_i(w)|w\in V(K)\}\) in _G<sub>i</sub>_ for every \(i\in\{1,\dots,n\}\).

We may note that maximal cliques in \(\star_{i=1}^nG_i\) may not "correspond" to maximal common induced subgraphs of _G_<sub>1</sub>_,...,G<sub>n</sub>_ (see Fig. 4). Nevertheless, the result holds for maximum common induced subgraphs.

**Proposition 1.** _Let G_<sub>1</sub>_,...,G<sub>n</sub> be graphs and let_ K _be the set of all maximal cliques K in_ \(\star_{i=1}^nG_i\)_. In addition, let H be the subgraph induced by the vertex set_ \(\{p_i(w)|w\in V(K)\}\) _in G<sub>i</sub> for some fixed_ \(K\in\mathcal{K}\)_. Then the following two statements are equivalent._

1. _H is a MVCS subgraph of G_<sub>1</sub>_,...,G<sub>n</sub>._<tbc>

_2._ _K is a maximum clique within the set_ K.

_Proof._ Let _G_<sub>1</sub>_,...,G<sub>n</sub>_ be graphs and let K be the set of all maximal cliques _K_ in \(\star_{i=1}^nG_i\). Suppose that _H_ is an MVCS of _G_<sub>1</sub>_,...,G<sub>n</sub>_. Since _H_ has maximum size,

