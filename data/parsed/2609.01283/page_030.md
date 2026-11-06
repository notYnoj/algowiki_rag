• _M_<sub>graph</sub>: _A subset_ \(S\subseteq E_H\) _is independent if its edges do not form any cycles in the underlying undirected graph. This is represented over a field_ F _by its incidence matrix_ \(A_\mathrm{graph}\in\{-1,0,1\}^{(N-1)\times M}\)_, where rows are indexed by V<sub>H</sub>_\\{_z}, and for an edge e_=(_u,v), the e-th column has_ -1 _at row u (if_ \(u\neq z\)_) and_ 1 _at row v (if_ \(v\neq z\)_)._<tbc>

• _M_<sub>part</sub>: _A subset_ \(S\subseteq E_H\) _is independent if every vertex_ \(v\in V_H\backslash\{z\}\) _has at most one incoming edge in S. This is represented by a matrix_ \(A_\mathrm{part}\in\{0,1\}^{(N-1)\times M}\)_, where rows are indexed by V<sub>H</sub>_\\{_z}. A column for edge e_=(_u,v_) _has a_ 1 _at row v (if_ \(v\neq z\)_) and_ 0 _elsewhere._

The following theorem by Edmonds \[Edm03\] establishes an equivalence between _k_-disjoint arborescences and packing _k_-common bases of the specified matroids.

**Theorem 5.2** (\[Edm03\])**.** _A directed graph H contains k-edge-disjoint z-rooted arborescences if and only if there exists a set_ \(S\subseteq E_H\) _of size k(N_-1) _that can be partitioned into k bases of M_<sub>graph</sub> _as well as M_<sub>part</sub> _(the partitioning may differ)._

We now return to our sensitivity setting. Let _G_=(_V,E,**c**_) be a directed graph with _n_ vertices and integer edge costs in \[-_W,W_\]. For any query pair (_s,U_), where \(s\in V\) and _U_ is a set of _f_ edge updates (insertions or deletions), our goal is to determine if _G+U_ contains _k_ edge-disjoint _s_-rooted arborescences, and compute the minimum possible total cost of such a family.

## Query Reduction

We construct an auxiliary graph _G_<sup>∗</sup> by adding a new isolated dummy root vertex _z_, setting \(V(G^*)=V\cup\{z\}\) and _E(G_<sup>∗</sup>)=_E_. For any target root \(s\in V\) , let _E<sub>s,z</sub>_ denote a set of _k_ zero-cost parallel edges directed from _z_ to _s_. Finding _k_-disjoint _s_-rooted arborescences in _G+U_ is equivalent to finding _k_-disjoint _z_-rooted arborescences in _G_<sup>∗</sup>+_U+E<sub>s,z</sub>_, which by Theorem 5.2 maps directly to a _k_-packing on _M_<sub>graph</sub> and _M_<sub>part</sub>.

**Theorem 5.3.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with integer edge costs in_ \[-_W,W_\]_, and let_ \(k\ge 1\)_. There exist the following sensitivity oracles that, for any_ \(s\in V\) _and any_ \(U\in E^f\)_, return the corresponding outputs on G+U with high probability:_

_Proof._ We invoke the matroid packing oracles from Theorem 3.5 on _M_<sub>graph</sub> and _M_<sub>part</sub>. For the auxiliary graph _G_<sup>∗</sup> with _N=n_+1 vertices, both matroids have rank _r=n_.

When a query (_s,U_) arrives, we incorporate the _f_ structural updates in _U_ and the _k_ parallel query edges _E<sub>s,z</sub>_. By Theorem 3.6, inserting the _k_ parallel edges in _E<sub>s,z</sub>_ only contributes _O(k_<sup>2</sup>) entries to the additive update of the packing Laplacian L<sub>pack</sub>. The _f_ standard edge updates contribute _O(fk_<sup>2</sup>) entries. Thus, the total additive update matrix has \(\delta=O(fk^2)\) non-zero entries. Substituting _r=n_ and the effective update bound \(\delta=O(fk^2)\) into the query bounds of Theorem 3.5 yields the stated bounds.

Theorem 5.3, together with the fact that a directed graph is _k_-strongly connected if and only if there exists a _k_-packing of arborescences rooted at an arbitrarily chosen vertex _s_ in both _G_ and its reverse, yields the following result.

**Corollary 5.4** (_k_-Strong-Connectivity Oracle)**.** _For any n-vertex directed graph G, there exists an f-sensitivity oracle that, given any update set_ \(U\subseteq E^f\)_, reports (with high probability) whether or not G+U is k-strongly-connected. The oracle can be constructed in_ \(O((kn)^\omega)\) _preprocessing time, uses O_((_kn_)<sup>2</sup>log_n_) _space, and answers each query in_ \(O((fk^2)^\omega)\) _time._

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O((kn)^\omega)\) & _O_((_kn_)<sup>2</sup>log_n_) & _O_((_fk_<sup>2</sup>)<sup>\(^\omega)\)</sup> & _Whether G+U has k-disjoint s-rooted arborescences_ \\
_Weighted_ & \(\widetilde{O}(W(kn)^3)\) & _O(W(kn_)<sup>3</sup>log_n_) & \(\widetilde{O}(Wkn\cdot(fk^2)^\omega)\) & _Min total cost of such k-arborescences_ \\
\end{tabular}

