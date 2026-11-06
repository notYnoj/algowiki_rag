<tbc>Lemma 28 helps to extend query lower bounds based on average sensitivity to larger classes. Suppose we have established a good lower bound on the sensitivity \(s(\Pi_T)\) for a class _C_ of trees. Consider a class \(C'\) obtained by taking a tree _T_ in class _C_ and replacing some of the subtrees _T<sub>v</sub>_ by other subtrees \(T'_v\) on the same number of leaves. For this new class \(C'\) the same lower bound on the sensitivity of inversion minimization applies modulo the Lipschitz loss. For example, Theorem 6 holds by virtue of a lower bound of the form \(s(\Pi_T)\ge(n-1)-clog(n)\) for every binary tree _T_ with _n_ leaves, where _c_ is a universal constant. If we allow some of the subtrees of _T_ to be replaced by, say freely arrangeable ones on the same leaves, applying Lemma 28 for each of the modified subtrees in sequence shows that the resulting new tree \(T'\) has

\(s(\Pi_{T^\prime})\ge s(\Pi_T)-\frac{\alpha n(\alpha n-1)}{n}\ge(n-1)-clog(n)-\alpha^2(n-1)=(1-\alpha^2)(n-1)-clog(n),\)

where \(\alpha\) denotes the fraction of leaves that belong to one of the replaced subtrees.

In fact, the notion of average sensitivity is robust with respect to the following, more refined type of surgery. From any tree _T_, let _R_ be a connected subset of _T_ that includes no leaves. Let \(T'\) be the subtree rooted at the LCA of _R_ (\(T'\) contains all of _R_), and let \(T'_1,\dots,T'_k\) be the disjoint maximal subtrees of \(T'\) that are strictly below _R_. Let \(R'\) be any tree that has _k_ leaves. Replace \(T'\) by \(R'\), and then replace the leaves of \(R'\) by \(T'_1,\dots,T'_k\).

The effect is that the region _R_ has been "reshaped" to look like \(R'\), but the rest of _T_ is unaffected. The cost of such a surgery is at most (_n_-1) times the probability that a uniformly random pair of distinct leaves has their LCA in _R_. The bound follows from thinking of sensitivity as (_n_-1) times the probability that a uniformly random edge in the full permutahedron is bichromatic. Provided the LCA of the affected leaves is outside _R_, then we get sensitivity before the surgery if and only if we get it after the surgery. Surgeries can be iterated, and the costs accumulate additively. In combination with our strong lower bound on the average sensitivity of binary trees (Lemma 36), this allows for a robust sense in which "mostly-binary" trees have high average sensitivity.

## 5 Refined Sensitivity Approach for Binary Trees

In this section we show how to refine the sensitivity approach for lower bounds on the query complexity of the problem \(\Pi_T\) of inversion minimization on trees in the important special case of binary trees _T_. In Section 5.1 we first develop a criterion for when a particular ranking \(\rho\) is sensitive to a particular adjacent-rank transposition \(\tau\). We then analyze the root sensitivity of binary trees in Section 5.2 and finally establish a strong lower bound on the average sensitivity in Section 5.3. An application of the Sensitivity Lemma then yields Theorem 6.

### 5.1 Sensitivity criterion

Recall the decomposition of the objective function \(MinInv(T,\rho)\) into contributions attributed to each node _v_ of degree deg_<sub>T</sub>(v)\>_1, as given by (5) in Section 4.2. In the case of binary trees, the contribution of node _v_ can be calculated simply as

\(MinRInv(T_v,\rho)=min(XInv_\rho(L_1,L_2),XInv_\rho(L_2,L_1)),\) (6)

where _u_<sub>1</sub> and _u_<sub>2</sub> denote the two children of _v_, and \(L_1\doteq L(T_{u_1})\) and \(L_2\doteq L(T_{u_2})\) their leaf sets. This simplicity makes a precise analysis of sensitivity feasible, as we will see next.

