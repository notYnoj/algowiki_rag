_Proof._ By definition, the _k_-fold union matroid \(M_\text{graph}^{\vee k}\) defines a set \(S\subseteq E\) as independent if and only if _S_ can be partitioned into _k_ disjoint sets \(S_1\unknown\cdots\unknown S_k\) such that each _S<sub>i</sub>_ is independent in the base matroid _M_graph. Since independence in _M_graph means the edge set is a forest, setting _S=E_ implies that the entire graph can be partitioned into _k_ disjoint forests if and only if _E_ is an independent set in \(M_\text{graph}^{\vee k}\). □

Note that a necessary condition for a graph to be partitionable into _k_ forests is that the total number of edges satisfies \(m\le k(n-1)\). If the number of active edges ever exceeds _k(n_-1), the graph trivially cannot be partitioned into _k_ forests.

#### Query Reduction

An update set _U_ consists of at most _f_ operations (edge insertions or deletions). Because the columns of _A_graph correspond directly to the edges of _G_, inserting or deleting an edge modifies exactly one column in the representation matrix. Therefore, _f_ updates in _G_ translate to exactly \(\delta\le f\) column updates.

**Theorem 5.10.** _Let G_=(_V,E_) _be an undirected graph with n vertices, and_ \(k\ge 1\)_. There exists a sensitivity oracle that, given any set of updates U consisting of at most f edge insertions or deletions (such that the updated active edge count m<sub>curr</sub> remains bounded by k(n_-1)_), answers queries on G+U with high probability:_

_Proof._ We invoke the matroid covering oracle from Theorem 3.10 on the graphic matroid _M_graph. The rank of the matroid is _r=n_-1.

When a query _U_ arrives, we incorporate the _f_ structural edge updates. Because each edge update inserts or deletes exactly one column in the base representation matrix _A_graph, the total number of column updates is \(\delta\le f\). We substitute the rank _r=n_-1 and the update bound \(\delta=f\) directly into the complexity bounds of Theorem 3.10. The preprocessing time is \(O((k(n-1))^\omega)=O((kn)^\omega)\), the space is _O_((_kn_)<sup>2</sup>log_n_), and the query time required to re-evaluate the determinant of the augmented matrix \(U'_{aug}\) is \(O((\delta k)^\omega)=O((fk)^\omega)\). By Theorem 5.9, this determinant is non-zero if and only if the updated graph can be partitioned into _k_ forests. □

## 6 Sensitivity Oracles for Matroid Parity

In this section, we study the _Matroid Parity_ (also known as _Matroid Matching_) problem, for linear matroids. The matroid parity problem was introduced by Lawler \[Law76\] as a common generalization of two fundamental combinatorial optimization problems: Matroid Intersection and Graph Matching. Although the matroid parity problem is intractable for general matroids \[JK82, Lov80\], it admits a polynomial time algorithm if the underlying matroid is linear \[Lov80\].

### 6.1 Algebraic tion and Enumeration

Let _M_ be a linear matroid of (even) rank _r_ over a field F, defined on a ground set of _m_ disjoint pairs of elements _E_={(_a_<sub>1</sub>_,b_<sub>1</sub>)_,...,(a<sub>m</sub>,b<sub>m</sub>_)}, and let \(wt:E\rightarrow[-W,W]\) be a weight function (the weights are associated with the pairs in _E_). The Linear Matroid Parity (LMP) problem asks whether there exists a selection of exactly _r/_2 pairs such that the union of all _r_ selected elements forms a basis of _M_. Such a valid selection is called a _parity basis_. The _weighted_ version asks for the minimum total weight of a parity basis, if one exists.

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Decision_ & \(O((kn)^\omega)\) & _O_((_kn_)<sup>2</sup>log_n_) & _O_((_kf_)<sup>\(\omega\)</sup>) & _Whether G+U partitions into k forests_ \\
\end{tabular}

