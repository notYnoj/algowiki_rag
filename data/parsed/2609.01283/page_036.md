pairs by _E_. For _e_=(_u,v_), the two columns corresponding to _e_ are (_e<sub>u</sub>,e<sub>v</sub>_) respectively. For every edge \(e=(u,v)\in E\), set the following entries in _A_:

\(A[u_k,e_u]=x_{u_k,e};A[v_l,e_v]=x_{v_l,e}\forall k\in[\alpha(u)],l\in[\alpha(v)].\)

Rest of the entries are set to 0. It can be seen that there are no repeated non-zero entries in _A_. Now, we show the following:

**Lemma 7.1.** _A graph G contains an_ \(\alpha\)_-factor if and only if the linear matroid M represented by A admits a parity base. Furthermore, there is a bijection between the_ \(\alpha\)_-factors of G and the parity bases of M._

_Proof._ We first prove the forward direction. Let \(H\subseteq E\) be an \(\alpha\)-factor of _G_. It can be seen that |_H_|=_N/_2 and hence, _H_ induces an \(N\times N\) submatrix _A_\[_H_\], formed by selecting the column pairs of _A_ corresponding to _H_. Since \(|\delta_H(v)|=\alpha(v)\) for all \(v\in V\) , we can define a perfect matching \(\pi\) between the set V and the columns of _H_ by mapping each copy \(v_j\in\mathcal{V}\) to a unique column _e<sub>v</sub>_ for some \(e\in H\cap\delta_H(v)\). Since each indeterminate appears exactly once in the entire matrix _A_, the monomial \(\prod_{v_j\in\mathcal{V}}A_{v_j,\pi(v_j)}\) in the Leibniz expansion of det(_A_\[_H_\]) does not get cancelled. Thus, \(det(A[H])\neq 0\), meaning the pairs corresponding to _H_ form a parity base.

For the other direction, assume there exists a parity base of _M_ corresponding to the edge set \(H\subseteq E\). Note that since rank(_M_)=_N_, we have that |_H_|=_N/_2. We now show by contradiction that for all \(v\in V\) , \(|\delta_H(v)|=\alpha(v)\). Suppose this is not true. Then, there exists a vertex \(w\in V\) such that \(|\delta_H(w)|\neq\alpha(w)\). Since |_H_|=_N/_2 and \(\sum_{v\in V}\alpha(v)=N\), we can assume without loss of generality that \(|\delta_H(w)|>\alpha(w)\). Define the set _C_ as the collection of columns of _A_ indexed by the set of edges \(\{e_w|e\in\delta_H(w)\}\). Since \(|\delta_H(w)|>\alpha(w)\), we have that \(|C|>\alpha(w)\). By the definition of _A_, there exist at most \(\alpha(w)\) rows (corresponding to the copies \(\{w_1,w_2,\dots,w_{\alpha(w)}\}\)) that have non-zero entries for the column vectors in _C_. Hence, the set of columns in _C_ can span a subspace of rank at most \(\alpha(w)\). Since \(|C|>\alpha(w)\), the columns in _C_ are linearly dependent. This implies _A_\[_H_\] is singular, and therefore the pairs corresponding to _H_ do not form a parity basis, which is a contradiction. □

Since the edges of _G_ correspond to the pairs in _M_, the following corollary of Theorem 7.1 is immediate in the weighted setting:

**Corollary 7.2.** _The cost of the minimum cost_ \(\alpha\)_-factor of G is equal to the weight of minimum- weight parity basis of M, if they exist._

## 7.2 Sensitivity Oracles for \(\alpha\)-Factors and Matchings

In this subsection we extend the algebraic formulation of \(\alpha\)-factors to support edge updates. For any set of _f_ edge insertions, deletions, or cost changes, the oracle reports whether an \(\alpha\)-factor exists in the updated graph and, in the weighted setting, the weight of a minimum-cost one. We consider two cases. First, in Section 7.2.1, we assume the degree bounds are _k_-bounded, i.e. \(max_v\alpha(v)\le k\), and work directly with the sensitivity oracle for _c_-sparse linear matroid parity. Then, in Section 7.2.2, we remove this assumption and handle arbitrary \(\alpha\) by reducing an update on _G_ to an update on an _auxiliary graph_ whose size is governed by _f_ rather than by \(max_v\alpha(v)\). Throughout, we let \(N=\sum_v\alpha(v)\). Furthermore, we instantiate the indeterminates in linear representation of \(\alpha\)-factor as uniformly random samples from a sufficiently large finite field, and our results would hold with high probability due to the Schwartz-Zippel lemma.

