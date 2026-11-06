\[BCR19\] presented an _f_-sensitivity oracle of _O_(2_<sup>f</sup>n_<sup>2</sup>) space that reports the strongly connected components of a graph after _f_ failures in \(\widetilde{O}(2^fn)\) query time. In contrast, for the simpler decision problem of testing whether the updated graph remains strongly connected (_k_=1 case), our oracle uses only _O(n_<sup>2</sup>log_n_) space and answers queries in \(O(f^\omega)\) time.

## 5.2 Sensitivity Oracles for _k_-Disjoint Spanning Trees

We now apply our algebraic framework to the problem of finding _k_ edge-disjoint spanning trees in an undirected graph. Let _G_=(_V,E,**c**_) be an undirected graph with _n_ vertices, _m_ edges, and integer edge costs in \[-_W,W_\]. A spanning tree is a maximal acyclic subgraph of _G_, containing exactly _n_-1 edges. We can formulate the problem of finding _k_ edge-disjoint spanning trees as a matroid packing problem by utilizing the standard graphic matroid _M_<sub>graph</sub> of rank _r=n_-1.

**Lemma 5.5.** _An undirected graph G contains k edge-disjoint spanning trees if and only if there exists a set_ \(S\subseteq E\) _of size k(n_-1) _that can be partitioned into k common bases of M_<sub>1</sub> _and M_<sub>2</sub>_, where we set both M_<sub>1</sub> _and M_<sub>2</sub> _to M_<sub>graph</sub>.

_Proof._ For the forward direction, suppose _G_ contains _k_ edge-disjoint spanning trees _T_<sub>1</sub>_,...,T<sub>k</sub>_. Let \(S=\bigcup_{i=1}^kE(T_i)\). Because each _T<sub>i</sub>_ is a spanning tree, its edge set _E(T<sub>i</sub>_) forms a basis in _M_<sub>graph</sub>. Since the trees are edge-disjoint, the sets _E(T_<sub>1</sub>)_,...,E(T<sub>k</sub>_) are pairwise disjoint and perfectly partition _S_. Because _M_<sub>1</sub> and _M_<sub>2</sub> are identical to _M_<sub>graph</sub>, each _E(T<sub>i</sub>_) is trivially a common basis of both matroids. Furthermore, the total size of _S_ is exactly \(\sum_{i=1}^k(n-1)=k(n-1)\).

For the converse, suppose there exists a set \(S\subseteq E\) of size _k(n_-1) that can be partitioned into _k_ disjoint sets _B_<sub>1</sub>_,...,B<sub>k</sub>_, where each _B<sub>i</sub>_ is a common basis of _M_<sub>1</sub> and _M_<sub>2</sub>. Since _M_<sub>1</sub>=_M_<sub>graph</sub>, each set _B<sub>i</sub>_ must be a basis of the graphic matroid, meaning the edges in _B<sub>i</sub>_ form a spanning tree of _G_. Because the sets _B_<sub>1</sub>_,...,B<sub>k</sub>_ partition _S_, they share no edges and are pairwise disjoint. Therefore, the subgraphs induced by _B_<sub>1</sub>_,...,B<sub>k</sub>_ constitute exactly _k_ edge-disjoint spanning trees in _G_. ▂

### Query Reduction

An update set _U_ consists of at most _f_ operations (edge insertions, edge deletions, or cost changes). Because the columns of _A_<sub>graph</sub> correspond directly to the edges of _G_, inserting, deleting, or re-weighting an edge modifies exactly one column in the representation matrix. Therefore, _f_ updates in _G_ translate directly to at most \(\delta=f\) column updates. Unlike the arborescence problem, there is no dynamic root vertex, so no auxiliary query edges need to be processed.

**Theorem 5.6.** _Let G_=(_V,E,**c**_) _be an n-vertex undirected graph with integer edge costs in_ \[-_W,W_\]_, and let_ \(k\ge 1\)_. There exist the following sensitivity oracles that, for any_ \(U\in E^f\)_, answer queries on G+U with high probability:_

_Proof._ We invoke the matroid packing oracles from Theorem 3.5 on _M_<sub>1</sub>=_M_<sub>graph</sub> and _M_<sub>2</sub>=_M_<sub>graph</sub>. Both matroids have rank _r=n_-1 and their representation matrices are structurally column-sparse.

When a query _U_ arrives, we incorporate the _f_ structural updates. Because each edge update modifies at most one column in the base representations, the total number of base updates is \(\delta\le f\). Substituting _r=n_-1 and the update bound \(\delta=f\) directly into the complexity bounds of Theorem 3.5 yields the stated preprocessing, space, and query bounds. ▂

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O((kn)^\omega)\) & _O_((_kn_)<sup>2</sup>log_n_) & _O_((_fk_<sup>2</sup>)<sup>\(\omega\)</sup>) & _Whether G+U has k edge-disjoint spanning trees_ \\
_Weighted_ & \(\widetilde{O}(W(kn)^3)\) & _O(W(kn_)<sup>3</sup>log_n_) & \(\widetilde{O}(Wkn(fk^2)^\omega)\) & _Min total cost of such k-spanning trees_ \\
\end{tabular}

