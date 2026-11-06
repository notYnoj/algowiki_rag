_Proof._ We invoke the subset sensitivity oracle from Theorem 3.7 on _M_<sub>1</sub>=_M_<sub>graph</sub> and _M_<sub>2</sub>=_M_<sub>graph</sub>. The rank of both matroids is _r=n_-1, the packing parameter is _k_, and the susceptible set size is \(\sigma=|E_Q|\). A query consists of _f_ edge updates, modifying at most _f_ diagonal entries in the representation. Substituting these parameters directly into the bounds of Theorem 3.7 yields the result. \(\square\)

## 8.2.3 Colorful Spanning Trees

A colorful spanning tree is a 1-packing of common bases of the graphic matroid _M_<sub>graph</sub> and the color-partition matroid _M_<sub>color</sub>. We keep the reduction presented in Theorem 5.8 unchanged and confine updates to a fixed susceptible set _E<sub>Q</sub>_ of size \(\sigma\) (which may include edges not currently in _E_, each assigned to one of the _n_-1 color classes), representing edges whose presence, cost, or color can change. Since queries introduce no auxiliary structures, the susceptible set for the data structure is exactly _E<sub>Q</sub>_, and modifying _f_ elements toggles or re-weights exactly _f_ diagonal entries.

**Theorem 8.9.** _Let G_=(_V,E,c_) _be an undirected colored graph with a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles for any set of updates_ \(U\subseteq E_Q\) _of size at most f:_

_Proof._ We invoke Theorem 3.7 on _M_<sub>graph</sub> and _M_<sub>color</sub> with _k_=1, rank _r=n_-1, and susceptible set size \(\sigma=|E_Q|\). A query modifies at most _f_ diagonal entries. Substituting these parameters directly into the bounds of Theorem 3.7 yields the result. \(\square\)

## 8.2.4 Packing Spanning Forests

Let _E<sub>Q</sub>_ be a susceptible set of size \(\sigma\) (which may include edges not currently in _E_), representing edges that can be dynamically inserted or deleted. Modifying _f_ elements toggles _f_ diagonal entries in the covering Laplacian.

**Theorem 8.10.** _Let_ \(k\ge 1\) _be an integer, and G_=(_V,E_) _be an undirected graph with n vertices and a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Let_ \(E_0=E\cup E_Q\)_. There exists a subset sensitivity oracle that, for any set of edge insertions or deletions_ \(U\subseteq E_Q\) _of size at most f (where the updated active edge count_ \(m_{curr}\le k(n-1)\)_), answers queries on G+U with high probability:_

_Proof._ We invoke the subset sensitivity covering oracle from Theorem 3.11 on the graphic matroid _M_<sub>graph</sub>. The rank of the matroid is _r=n_-1, the covering parameter is _k_, and the susceptible set size is bounded by \(\sigma=|E_Q|\).

A query consists of up to _f_ edge insertions or deletions confined to the set _E<sub>Q</sub>_. In the algebraic framework of Theorem 3.11, inserting or deleting an edge corresponds to toggling its respective<tbc>

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O(\sigma^2(kn)^{\omega-2}+(kn)^\omega)\) & \(O(\sigma^2)\) & \(O(f^\omega)\) & _Whether G+U has k edge-disjoint spanning trees_ \\
_Weighted_ & \(\widetilde{O}(W\sigma^2(kn)^{\omega-1}+W(kn)^{\omega+1})\) & \(\widetilde{O}(Wkn\cdot\sigma^2)\) & \(\widetilde{O}(Wkn\cdot f^\omega)\) & _Min total cost of such k-spanning trees_ \\
\end{tabular}

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O(\sigma^2n^{\omega-2}+n^\omega)\) & \(O(\sigma^2)\) & \(O(f^\omega)\) & _Whether G+U has a colorful spanning tree_ \\
_Weighted_ & \(\widetilde{O}(W\sigma^2n^{\omega-1}+Wn^{\omega+1})\) & \(\widetilde{O}(Wn\sigma^2)\) & \(\widetilde{O}(Wnf^\omega)\) & _Min cost of a colorful spanning tree_ \\
\end{tabular}

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O(k^2|E_0|+\sigma^2(kn)^{\omega-2}+(kn)^\omega)\) & \(O(\sigma^2)\) & \(O(f^\omega)\) & _Whether G+U partitions into k forests_ \\
\end{tabular}

