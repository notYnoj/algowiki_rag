<tbc>\(v\in V_H\backslash\{t^*\}\) to have out-degree at most one in (_V<sub>H</sub>,C<sub>i</sub>_), and independence in _M_<sub>in</sub> forces every \(v\in V_H\backslash\{s^*\}\) to have in-degree at most one. Hence (_V<sub>H</sub>,C<sub>i</sub>_) is a disjoint union of directed paths and cycles, and any nontrivial path must start at _s_<sup>∗</sup> and end at _t_<sup>∗</sup>. Since |_S_|=_k(N_-1) and each \(|C_i|\le N-1\), equality holds throughout, so each _C<sub>i</sub>_ contains at most one (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-path together with vertex-disjoint cycles and self-loops. Because _s_<sup>∗</sup> has out-degree \(\lambda\) and \(k-\lambda\) self-loops (similarly for _t_<sup>∗</sup>), exactly \(\lambda\) of these _C<sub>i</sub>_’s contain an (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-path. The disjointness of the _C<sub>i</sub>_’s then yields \(\lambda\) edge-disjoint (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-paths in _H_. □

We now return to the sensitivity setting. Let _G_=(_V,E,**c**_) be a directed graph with _n_ vertices, _m_ edges, and integer edge costs in \[-_W,W_\]. Let \(k\in[1,n]\) be a fixed integer. For any query (_s,t,U_) with \(s,t\in V\) and _U_ a set of _f_ edge insertions or deletions, our goal is to determine \(\lambda^*:=min(k,\lambda_{G+U}(s,t))\) and the minimum total cost of an (_s,t_)-flow of value \(\lambda^*\).

## Preprocessing

We construct an auxiliary graph _G_<sup>∗</sup> on _N=n_+2 vertices by introducing a super- source _s_<sup>∗</sup> and a super-sink _t_<sup>∗</sup>, and augmenting the edge set with _k_ zero-cost self-loops at each vertex \(v\in V\) , yielding _M=m+kn_ edges in total. We then invoke the preprocessing of Theorem 3.5 on the partition matroids _M_<sub>out</sub>_,M_<sub>in</sub> associated with _G_<sup>∗</sup>, instantiating both the decision oracle (for unweighted queries) and the weighted oracle (for min-cost queries).

As linear representations \(A_{out},A_{in}\in\{0,1\}^{(N-1)\times M}\) are column-sparse, the decision oracle requires \(O((kn)^\omega)\) preprocessing time and _O_((_kn_)<sup>2</sup>log_n_) space, while the weighted oracle requires \(\widetilde{O}(W(kn)^3)\) preprocessing time and _O(W(kn_)<sup>3</sup>log_n_) space.

## Query Reduction

For any \(s,t\in V\) and \(\lambda\le k\), let \(E_{s,t,\lambda}\) consist of: (i) \(\lambda\) zero-cost parallel edges from _s_<sup>∗</sup> to _s_, (ii) \(\lambda\) zero-cost parallel edges from _t_ to _t_<sup>∗</sup>, and (iii) \(k-\lambda\) zero-cost self-loops at each of _s_<sup>∗</sup> and _t_<sup>∗</sup>. By Theorem 4.1, _G+U_ admits \(\lambda\) edge-disjoint (_s,t_)-paths if and only if the matroids _M_<sub>out</sub>_,M_<sub>in</sub> on the edge set of \(G^*+U+E_{s,t,\lambda}\) admit a _k_-packing of common bases.

The matroid representations of \(G^*+U+E_{s,t,\lambda}\) differ from those of _G_<sup>∗</sup> on _O(f_) edges from _U_ together with the parallel-edge and self-loops in \(E_{s,t,\lambda}\). By Theorem 3.6, the parallel edges/self-loops in \(E_{s,t,\lambda}\) contribute only _O(k_<sup>2</sup>) entries to the additive update of L<sub>pack</sub>. Hence the total update size is \(\delta=O(fk^2)\). We thus obtain the following result.

**Theorem 4.2.** _Let G_=(_V,E,**c**_) _be an n-vertex directed graph with integer costs in_ \[-_W,W_\]_, and_ \(k\in[1,n]\)_. Then there exist the following sensitivity oracles that, for any query_ \((s,t,U)\in V^2\times E^f\)_, answer queries on G+U with high probability:_

_Proof._ We instantiate the matroid intersection packing oracles of Theorem 3.5 on the partition matroids _M_<sub>out</sub>_,M_<sub>in</sub> associated with the auxiliary graph _G_<sup>∗</sup>. Recall from the query reduction above that finding \(\lambda\) edge-disjoint (_s,t_)-paths in _G+U_ reduces to deciding whether _M_<sub>out</sub>_,M_<sub>in</sub> on the edge set \(G^*+U+E_{s,t,\lambda}\) admit a _k_-packing of common bases. By Theorem 3.6, the parallel-edge and self-loops in \(E_{s,t,\lambda}\) together with the _f_ updates in _U_ yield an additive update of size \(\delta=O(fk^2)\) to the packing Laplacian.

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Bounded Flow_ & \(O((kn)^\omega)\) & \(O((kn)^2logn)\) & \(O((fk^2)^\omega logk)\) & \(\lambda^*=min(k,\lambda_{G+U}(s,t))\) \\
_Nearest Min-Cut_ & \(O((kn)^\omega)\) & \(O((kn)^2logn)\) & \(O((fk^2)^\omega n)\) & _NMC_<sub>_G+U_</sub>(_s,t_) _(if_ \(\lambda^*<k\)_)_ \\
_Min-Cost Flow_ & \(\widetilde{O}(W(kn)^3)\) & \(O(W(kn)^3logn)\) & \(\widetilde{O}((fk^2)^\omega kWn)\) & _Min-cost for flow of value_ \(\lambda^*\) \\
\end{tabular}

