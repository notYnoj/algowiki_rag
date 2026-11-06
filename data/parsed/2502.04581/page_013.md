_where_ \(Q_1,\dots Q_{k-3}\in\{\exists,\forall\}\) _and_ \(k\ge 3\)_, can be solved in time_ \(O(n^{k-1-\epsilon_P})\) _for an_ \(\epsilon_P>0\).

The combination of Lemma 11 and Lemma 12, thus suffice to prove Theorem 4.

**The** 3-SUM completeness of formulas with inequality dimension at most 3

As a first idea, one could try to solve problems of different quantifier structures by just counting witnesses. Consider in the following the example \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\).

Assume we are promised that the formula \(\forall a\in A\forall b\in B\exists c\in C\psi(a,b,c)\) satisfies a kind of _disjointness_ property, specifically that for every \((a,b)\in A\times B\) there exists at most one \(c\in C\) such that \(\psi(a,b,c)\). Then satisfying the formula boils down to checking whether the number of witnesses (_a,b,c_) satisfying \(\psi(a,b,c)\) equals to \(|A|\cdot|B|\).

To create this _disjointness_ effect, we use the following geometric approach: We show that one can re-interpret the formula as \(\forall a\in A\forall b\in B:a+b\in\bigcup_{c^\prime\in C^\prime} V(c')\), where \(A,B,C'\subseteq\mathbb{Z}^3\), \(C'\) is a set of size _O(n_) and \(V(c')\) is an orthant associated to \(c'\). Using an adapted variant of [23], we decompose this union of orthants in R<sup>3</sup> (which we may equivalently view as sufficiently large congruent cubes) into a set R of _O(n_) _disjoint_ boxes. Thus, it remains to notice that the resulting problem - i.e., for all \(a\in A,b\in B\) is there a box \(R\in\mathcal{R}\) such that _a+b_ is contained in _R_ - is a \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\) formula with the desired disjointness property, which can be handled as argued above. For the class \(\mathsf{FOP}_\mathbb{Z}(\exists\exists)\), we perform a slightly more involved argument. The classes \(\mathsf{FOP}_\mathbb{Z}(\exists\exists)\) and \(\mathsf{FOP}_\mathbb{Z}(\forall\exists)\) reduce to 3-SUM regardless of the inequality dimension due to Theorem 1 and Lemma 9.

## 3 _k_-SUM is complete for existential FOP<sub>Z</sub> formulas

We begin with a simple completeness theorem that _k_-SUM is complete for the class of problems \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\). Since _k_-SUM is indeed a \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\)-formula, it remains to show a fine- grained reduction from any \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\) formula to _k_-SUM. The proofs in this section are deferred to the full version. As a first step towards this Theorem, we consider how to reduce a conjunction of _m_ linear inequalities to a vector _k_-SUM instance.

\(\blacktriangleright\) **Lemma 13.** _Consider vectors_ \(a_1\in\{-U,\dots,U\}^{d_1},\dots,a_k\in\{-U,\dots,U\}^{d_k}\)_, integers_ \(S_1,\dots,S_m\in\{-U,\dots,U\}\)_, for each_ \(i\in\{1,\dots,m\},j\in\{1,\dots,k\}\)_, vectors_ \(c_{i,j}\in\mathbb{Z}^{d_j}\)_, and a formula_

\(\psi:=\wedge_{i=1}^m\left(\sum_{j=1}^kc_{i,j}^Ta_j\ge S_i\right).\)

_There exist O_(1) _time computable functions_ \(f_1^{\ell,\psi},\dots,f_k^{\ell,\psi},g^{\ell,\psi,W}\) _such that the following statements are equivalent_

**2.** _There are_ \(\ell\in\{1,\dots,\lceil log_2(M)\rceil\}^m,W\in\{1,\dots,k\}^m\) _such that_ \(f_1^{\ell,\psi}(a_1)+\cdots+f_k^{\ell,\psi}(a_k)=g^{\ell,\psi,W}(S_1,\dots,S_m)\).

_Moreover, if the second item holds, there is a unique choice of such_ \(\ell\) _and W._

Essentially the above lemma enables a reduction from a conjunction of inequality checks to a conjunction of equality checks. We can now continue with our completeness theorem.

\(\blacktriangleright\) **Theorem 1** (_k_-SUM is \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\)-complete)**.** _Let_ \(k\ge 3\) _and assume that k-SUM can be solved in time T<sub>k</sub>_SUM(_n). For any problem P in_ \(\mathsf{FOP}_\mathbb{Z}(\exists^k)\)_, there exists some c such that P can be solved in time O(T<sub>k</sub>_SUM(_n_)log_<sup>c</sup>n)._

1. _The formula_ \(\wedge_{i=1}^m\left(\sum_{j=1}^kc_{i,j}^Ta_j\ge S_i\right)\) _holds._

