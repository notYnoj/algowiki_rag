## 4.2 Correctness analysis

We first establish that TryAdd preserves the forest structure (Fact 1, Corollary 1), then that component connectivity is invariant under edge swaps (Lemma 3), and finally that HandleAddition preserves _k_-edge-connectivity (Lemma 4, Theorem 5).

**Fact 1.** _Let F_=(_V,E<sub>F</sub>_) _be a spanning forest and let_ \(e=\{u,v\}\notin E_F\).

1. _If u and v are in different connected components of F, then_ \((V,E_F\cup\{e\})\) _is a forest._<tbc>

_2._ _If u and v are in the same connected component and P<sub>uv</sub> is the path connecting them in F, then for any_ \(e'\in P_{uv}\)_, the graph_ \((V,(E_F\cup\{e\})\backslash\{e'\})\) _is a spanning forest._

**Corollary 1.** _Let F_=(_V,E<sub>F</sub>_) _be the forest represented by Link-Cut tree LC, and let e_={_u,v_} _be an edge not in E<sub>F</sub>. After executing_ TryAdd(_LC, u, v), the forest represented by LC remains a valid spanning forest._

**Lemma 3.** _Let F<sub>i</sub>_=(_V,E<sub>i</sub>_) _be a spanning forest and let_ \(F'_i\) _be the forest obtained by replacing an edge_ \(\{u,\text{parent}(u)\}\in E_i\) _with an edge_ \(\{u,v\}\notin E_i\)_, where u and v are in the same connected component of F<sub>i</sub>. For any pair of vertices_ \(x,y\in V\)_, x and y are connected in F<sub>i</sub> if and only if they are connected in_ \(F'_i\).

_Proof._ Let _C_ be the component of _F<sub>i</sub>_ containing _u_ and _v_. Removing {_u,_parent(_u_)} partitions _V(C_) into two subsets: _V<sub>u</sub>_, the vertices of the subtree rooted at _u_, and _V(C_)\\_V<sub>u</sub>_. Since \(v\in V(C)\backslash V_u\), adding {_u,v_} reconnects these two subsets into a single connected component. No edges incident to vertices outside _V(C_) are affected, so the remaining components of _F<sub>i</sub>_ are unchanged.

**Lemma 4.** _If vertices_ \(u,v\in V\) _are connected in forest F<sub>k</sub>, then they are connected in every preceding forest F<sub>j</sub> for_ \(1\le j<k\).

_Proof._ Fix _j_ with \(1\le j<k\). Since the forests _E_<sub>1</sub>_,...,E_<sub>|_E_|</sub> are pairwise edge-disjoint and _j\<k_, we have \(E_k\subseteq E\backslash\left(\bigcup_{i=1}^{j-1}E_i\right)\). If _u_ and _v_ are connected in _F<sub>k</sub>_, there exists a path \(P_{uv}\subseteq E_k\), and by the inclusion above, \(P_{uv}\subseteq E\backslash\left(\bigcup_{i=1}^{j-1}E_i\right)\). Since _F<sub>j</sub>_ is a maximal spanning forest of \(E\backslash\left(\bigcup_{i=1}^{j-1}E_i\right)\) (Lemma 2.5 in \[12\]), _u_ and _v_ are connected in _F<sub>j</sub>_.

The following theorem is the central correctness result for HandleAddition algorithm; its proof combines Lemmas 3 and 4.

**Theorem 5.** _Let_ \(G'=\left(V,\bigcup_{i=1}^kE_i\right)\) _be the sparse certificate maintained by Algorithm 3. If_ HandleAddition_(e<sub>new</sub>) discards an edge e<sub>old</sub>_={_u,v_} _(e_\(_{new}\neq e_{old}\)_), then_ \(\lambda(u,v;(G'\cup\{e_{new}\})\backslash\{e_{old}\})\ge k\).

_Proof._ We maintain the following invariant: after every TryAdd operation, each forest _F<sub>j</sub>_ (\(1\le j\le k\)) is a maximal spanning forest of \(E\backslash(\bigcup_{i=1}^{j-1}E_i)\), and the forests _E_<sub>1</sub>_,...,E<sub>k</sub>_ remain pairwise edge-disjoint. The invariant holds initially by the Nagamochi-Ibaraki construction (Lemma 2). We first show it is preserved by HandleAddition, then use it to conclude _e<sub>old</sub>_ redundancy.

We will consider two cases. First, let us assume that TryAdd(_LC<sub>j</sub>_, _x_, _y_) returns null value (edge is absorbed into forest _F<sub>j</sub>_). The edge {_x,y_} connects two connected components of _F<sub>j</sub>_. Since two connected components of _F<sub>j</sub>_ are connected by {_x,y_}, any edge from \(\bigcup_{i=j+1}^kE_i\) still induce a cycle in _F<sub>j</sub>_, so _F<sub>j</sub>_ remains maximal. For each _l\>j_, the edges are moved between forests with edge sets _E_<sub>1</sub>_,E_<sub>2</sub>_,...,E<sub>j</sub>_ - contained in \(\bigcup_{i=1}^{l-1}E_i\) - and the new edge _e<sub>new</sub>_ is present in _E_ and _E_<sub>1</sub>. Thus, the set of available edges \(E\backslash\bigcup_{i=1}^{l-1}E_i\) remains unchanged, so _F<sub>l</sub>_ remains maximal for _l\>j_.

Now, assume that TryAdd(_LC<sub>j</sub>_, _x_, _y_) returns non-null value (edge was displaced). The operation replaces one edge in _E<sub>j</sub>_ with another, and by Lemma 3 the connected components of _F<sub>j</sub>_ are unchanged. Disjointness is maintained because the displaced edge is removed from _E<sub>j</sub>_ before being passed to the next forest. Before the operation, _F<sub>j</sub>_ is a maximal spanning forest of \(E\backslash\left(\bigcup_{i=1}^{j-1}E_i\right)\), so every edge in \(\bigcup_{i=j+1}^kE_i\) induces a cycle in _F<sub>j</sub>_. Since TryAdd<tbc>

