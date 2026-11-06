_Proof._ We evaluate the determinant of the Matroid Laplacian \(\mathcal{L}_\cap=U_1DU_2^T\) using the Cauchy-Binet formula (see Theorem 2.5) and substitute \(det(D_S)=\prod_{e\in S}x_eY^{W+wt(e)}\) and \(\alpha_S\) to get:

\(det(\mathcal{L}_\cap)=det\big(U_1(DU_2^T)\big)=\sum_{S\subseteq E|S|=kr}det\big((U_1)_S\big)det\big((U_2)_S\big)det(D_S)=Y^{krW}\sum_{S\subseteq E|S|=kr}\alpha_S\big(\prod_{e\in S}x_e\big)Y^{wt(S)}.\)

By Theorem 3.2, if _S_ is dependent in either \(M_j^{\vee k}\), then (_U<sub>j</sub>)<sub>S</sub>_ does not have full column rank, and so \(\alpha_S=0\). This restricts the sum to common bases. Next, if _S_ is a common basis, then by the probabilistic claim in Theorem 3.2, each (_U<sub>j</sub>)<sub>S</sub>_ has full column rank with probability at least \(1-1/(kr)^{\Omega(1)}\), and so \(\alpha_S\neq 0\) with at least this probability.

For the final claim, let **_wt_**<sub>min</sub> denote the minimum weight of a common basis of \(M_1^{\vee k}\) and \(M_2^{\vee k}\). Then, the coefficient of \(Y^{krW+wt_\mathrm{min}}\) is \(\sum_{S^*}\alpha_{S^*}\prod_{e\in S^*}x_e\), where the sum is over minimum-weight common bases. The above is a nonzero polynomial of degree _kr_ since distinct bases contribute distinct monomials in {_x<sub>e</sub>_}, and with high probability at least one minimum-weight common basis _S_<sup>∗</sup> satisfies \(\alpha_{S^*}\neq 0\). By the Schwartz-Zippel lemma, it evaluates to a nonzero value with probability 1-_kr/_|F|. Therefore, we get that with probability \(1-\frac{1}{(kr)^{\Omega(1)}}\), isolating the smallest exponent of _Y_ in \(det(\mathcal{L}_\cap)\) and subtracting _krW_ yields **_wt_**<sub>min</sub>.

## 3.1.1 Sensitivity Oracle for Sparse Linear Matroids

We now consider the sensitivity problem for the _k_-packing problem in the setting of sparse linear matroids. To obtain _k_ disjoint common bases of two matroids _M_<sub>1</sub> and _M_<sub>2</sub>, we find a common basis of full rank _kr_ in the _k_-fold union of these matroids. The main technical tool for this proceeds by analyzing the determinant of the mixed Laplacian using Theorem 3.4. In the static setting, this determinant evaluates to a non-zero polynomial with high probability if and only if a valid _k_-packing exists, and its minimum degree extracts the minimum weight of such a packing.

We formalize this in the sensitivity setting by utilizing the data structure from Theorem A.2 to handle sparse updates to the base representations of the matroids.

**Theorem 3.5.** _Let M_<sub>1</sub>=(_E,_I<sub>1</sub>) _and M_<sub>2</sub>=(_E,_I<sub>2</sub>) _be two sparse linear matroids of rank r defined on a common ground set E of size m, with a weight function_ \(wt:E\rightarrow[-W,W]\)_. Let A_<sub>1</sub> _and A_<sub>2</sub> _be their respective_ \(r\times m\) _linear representation matrices over a field_ F.

_Then, for any_ \(k\ge 1\)_, there exist sensitivity oracles that, given a set of_ \(\delta\) _updates to A_<sub>1</sub>_,A_<sub>2</sub>_, and wt, answer k-packing queries for the updated matroids_ \(M'_1\) _and_ \(M'_2\) _as follows:_

1. **_Decision Oracle:_** _Decides if a k-packing set S exists. Recall that a subset_ \(S\subseteq E,|S|=kr\) _is said to be k-packing if it can be partitioned into k common bases of_ \(M'_1\) _and_ \(M'_2\) _respectively, where the partitioning corresponding to each of the matroids may differ. This oracle requires_ \(O(k^2m+(kr)^\omega)\) _preprocessing time, O(km_+(_kr_)<sup>2</sup>log(_kr_)) _space, and answers queries in_ \(O((k^2\delta)^\omega)\) _time._<tbc>

_2._ **_Weighted Oracle:_** _Returns the exact total weight of a minimum-weight k-packing set S. This oracle requires_ \(\widetilde{O}(k^2m+W(kr)^3)\) _preprocessing time, O(km+W(kr_)<sup>3</sup>log(_kr_)) _space, and answers queries in_ \(\widetilde{O}(W\cdot kr\cdot(k^2\delta)^\omega)\) _time._

_Proof._ Let _U_<sub>1</sub> and _U_<sub>2</sub> be the \(kr\times mk\)-fold randomized union representation matrices for _M_<sub>1</sub> and _M_<sub>2</sub> respectively, as obtained by Theorem 3.2. Let _D_ be the \(m\times m\) diagonal weight matrix with \(D_{e,e}=x_eY^{W+wt(e)}\), and define the \(kr\times kr\) mixed Laplacian matrix as \(\mathcal{L}_{pack}:=U_1DU_2^T\). Suppose the base representations _A_<sub>1</sub>_,A_<sub>2</sub> and the weight function undergo at most \(\delta\) changes. We first bound<tbc>

