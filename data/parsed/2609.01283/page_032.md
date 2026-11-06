## 5.3 Sensitivity Oracles for Colorful Spanning Trees

We now apply our algebraic matroid intersection framework (1-packing) to the colorful spanning tree problem. Let _G_=(_V,E,c_) be an undirected graph with _n_=|_V_| vertices and integer costs in \[-_W,W_\]. The edge set _E_ is partitioned into exactly _n_-1 disjoint color classes, \(E=C_1\unknown C_2\unknown\cdots\unknown C_{n-1}\). A _colorful spanning tree_ is a spanning tree of _G_ containing exactly one edge from each color class.

**Definition 5.7** (Graphic and Color Partition Matroids)**.** _The matroids M_<sub>graph</sub> _and M_<sub>color</sub> _on the common ground set E, both of rank r=n_-1_, are defined as follows:_

• _M_<sub>graph</sub>: _A subset_ \(S\subseteq E\) _is independent if its edges do not form any cycles in G. We fix an arbitrary orientation of G and represent M_<sub>graph</sub> _over_ F _by its truncated incidence matrix_ \(A_\mathrm{graph}\in\{-1,0,1\}^{(n-1)\times|E|}\).<tbc>

• _M_<sub>color</sub>: _A subset_ \(S\subseteq E\) _is independent if it contains at most one edge from each color class C<sub>i</sub>. Its linear representation over_ F _is an_ \((n-1)\times|E|\) _matrix A_<sub>color</sub>_, where rows are indexed by the n_-1 _color classes. For any edge_ \(e\in E\)_, its corresponding column has a_ 1 _at the row corresponding to its color class, and_ 0 _elsewhere._

An undirected graph _G_ contains a colorful spanning tree if and only if there exists a set \(S\subseteq E\) of size _n_-1 that forms a 1-packing of common bases in _M_<sub>graph</sub> and _M_<sub>color</sub>.

### Query Reduction

An update set _U_ consists of at most _f_ operations (edge insertions, deletions, or cost/color changes). Because the columns of the representation matrices correspond directly to edges, modifying an edge or its color translates to updating exactly one column in the matrices (specifically, swapping the incident vertices in _A_<sub>graph</sub> and moving the 1 between color rows in _A_<sub>color</sub>). Thus, _f_ updates in _G_ translate directly to \(\delta\unknown f\) column updates.

**Theorem 5.8.** _Let G_=(_V,E,c_) _be an undirected colored graph. Then there exist the following sensitivity oracles that, given any set of updates U consisting of at most f edge insertions, deletions, or color changes, answer queries on G+U with high probability:_

_Proof._ We apply Theorem 3.5 with _k_=1. Both matroids have rank _r=n_-1 and their representation matrices are column-sparse. Substituting _k_=1, _r=n_-1, and the base update bound \(\delta=f\) into Theorem 3.5 yields the stated preprocessing, space, and query bounds. \(\square\)

## 5.4 Sensitivity Oracles for Packing Spanning Forests

We now apply our algebraic matroid covering framework to the problem of packing spanning forests. Let _G_=(_V,E_) be an undirected graph with _n_ vertices and _m_ edges. The _forest packing problem_ (also known as the arboricity problem) asks whether the entire active edge set _E_ can be partitioned into _k_ disjoint forests.

To utilize our matroid covering framework, we establish the direct equivalence between partitioning the edge set into _k_ forests and covering the ground set with _k_ independent sets of _M_<sub>graph</sub>.

**Lemma 5.9.** _The edges of an undirected graph G_=(_V,E_) _can be partitioned into k forests if and only if the edge set E is independent in the k-fold union matroid_ \(M_\mathrm{graph}^{\vee k}\).

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O(n^\omega)\) & _O(n_<sup>2</sup>log_n_) & \(O(f^\omega)\) & _Whether G+U has a colorful spanning tree_ \\
_Weighted_ & \(\widetilde{O}(Wn^3)\) & _O(Wn_<sup>3</sup>log_n_) & \(\widetilde{O}(Wnf^\omega)\) & _Min cost of a colorful spanning tree_ \\
\end{tabular}

