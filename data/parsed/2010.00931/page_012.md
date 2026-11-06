The existence of a leaf centroid follows by a similar argument as the existence of the classical centroid (see e.g. \[Sla78, BGHK92, Wan15\]). (Informally) start at an arbitrary non-leaf node _x_ and as long as _S_\\_x_ has a component with too many leaves, move _x_ along the edge towards this component. By standard data structuring, a leaf centroid can be found in linear time; for completeness we give a proof in Appendix A.

The following observation connects leaf-sets with boundaries.

**Observation 6.** _Let S_\[_A_\] _be a subtree of S. Then the set of leaves of_ \(\mathtt{ch}(\delta_S(A))\) _is_ \(\delta_S(A)\).

_Proof._ Let \(x\in\delta(A)\), and suppose that _x_ is not a leaf of \(\mathtt{ch}(\delta(A))\). Then _x_ is on the path between two nodes \(u,v\in\delta(A)\backslash\{x\}\). Let \((u,u'),(v,v')\in\mathtt{cut}(A)\). As _S_\[_A_\] is connected, there is a path between \(u'\) and \(v'\) that lies completely within _S_\[_A_\]. The path between _u_ and _v_ consists of exactly this path, with _u_ prepended and _v_ appended. This means that \(x\in A\), a contradiction.

Conversely, let \(x\notin\delta(A)\). If \(x\in\mathtt{ch}(\delta(A))\), then _x_ must lie on a path between two nodes \(u,v\in\delta(A)\). This means that _x_ is not a leaf of \(\mathtt{ch}(\delta(A))\).

We proceed with the main lemma of this subsection.

**Lemma 3.** _Given a search tree T on S, for arbitrary_ \(k\ge 3\) _we can find in time_ O(_n_<sup>2</sup>) _a k-cut search tree T_<sup>∗</sup> _on S, so that_ \(\mathtt{depth}_{T^*}(x)\le(1+\epsilon_k)\cdot\mathtt{depth}_T(x)\) _for all_ \(x\in V(S)\)_, where_

\(\varepsilon_k=\frac{1}{\left\lceil\frac{k}{2}\right\rceil-1}.\)

Algorithm 1 transforms _T_ into _T_<sup>∗</sup> (with the call Fix(_T,r_), where _r_=`root`(_T_)). The basic idea is the following: for a given node _x_ of _T_ (initially the root), we check whether _T<sub>x</sub>_ has a boundary size smaller than _k_. If yes, we simply recurse on the subtrees. Otherwise, we transform _T<sub>x</sub>_ by replacing the root _x_ with a node _v_ (by rotating _v_ to the top), such as to minimize the maximum boundary size of the subtrees rooted at the children. After the transformation, we recurse on the children of the new tree. (Note that when the boundary size is exactly _k_, node _v_ may happen to be _x_ in which case no rotation is necessary.)

The rest of this subsection is dedicated to the proof of Lemma 3. We remark that we only need Algorithm 1 as an _existence proof_ for good _k_-cut trees, and its running time does not affect the running time of our approximation algorithm.

## Correctness.

We consider the boundary size of the subtrees in each recursive call.

**Lemma 4.** _Let_ \(x\in V(S)\) _and let c be a child of x in T. Then_ \(|\delta(T_c)|\le|\delta(T_x)|+1\).

_Proof._ By Lemma 2, we have \(\delta(T_c)\subseteq\delta(T_x)\cup\{x\}\), so \(|\delta(T_c)|\le|\delta(T_x)|+1\).

**Lemma 5.** _Let_ \(x\in V(S)\) _with_ \(|\delta(T_x)|\ge k\)_, let_ \(T'\) _be the tree produced in Line 10 or Line 12 of Algorithm 1, let v be the leaf centroid of_ \(\mathtt{ch}(\delta(T_x))\) _and let c be a child of v in_ \(T'\)_. Then_<tbc>

\(|\delta(T'_c)|\le\left\lfloor\frac{|\delta(T_x)|}{2}\right\rfloor+1.\)

