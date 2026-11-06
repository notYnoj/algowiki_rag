_Therefore, for any random variable Y defined on a product space_ \(\Omega_1\times\Omega_2\times\Omega_3\) _satisfying the integrability conditions,_ \(\sum_{\alpha\subset\{1,2,3\}}(-1)^{|\alpha|}\Phi(\mathbb{E}^\alpha Y)\ge 0\)_. Reciprocally, this guarantees the non-negativity of D_<sup>2</sup>_B<sub>k</sub>, for any_ \(k\in\{1,\dots,n-2\}\) _and any S. According to \[23, Theorem 2\], this happens if and only if there exist_ \(a,b,c\in\mathbb{R}\) _with_ \(a\ge 0\) _and_ \(\Phi:x\mapsto ax^2+bx+c\)_. So for any function_ \(\Phi\) _that is not of this form, the K<sub>k</sub>’s and the J<sub>k</sub>’s (defined as the variations of B<sub>k</sub>’s) are not always non-negative: for some functions S they are negative._<tbc>

_(iii)_ _It is tempting to use the representation of completely monotone functions for the_ \(B'_ks\)_. Unfortunately, a completely monotone finite sequence may not be the restriction of a completely monotone function._<tbc>

_(iv)_ _From the decomposition of the variance one easily gets the decomposition of the covariance of square integrable S and_ \(T:\mathbb{R}^n\rightarrow\mathbb{R}\)_, as a polarization identity gives:_<tbc>

<tbc>\(Cov(S,T)=\sum_{k=1}^nB_k(S,T),\)<tbc>

<tbc>_where_<tbc>

\(B_k(S,T)=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}S(T^{i_1,\dots,i_{k-1}}-T^{i_1,\dots,i_k})=\mathbb{E}\frac{1}{2n!}\sum_{i\in\mathfrak{S}_n}(S-S^{i_k})(T^{i_1,\dots,i_{k-1}}-T^{i_1,\dots,i_k})\)<br>
\(=\mathbb{E}\frac{1}{2n!}\sum_{i\in\mathfrak{S}_n}(T-T^{i_k})(S^{i_1,\dots,i_{k-1}}-S^{i_1,\dots,i_k}).\)

_To get a symmetrical formula of the variance, let for any_ \(i_1,\dots i_k\in\{1,\dots,n\}\), \(S^{\widetilde{i_1},\dots,\widetilde{i_k}}\) _be as_ \(S^{i_1,\dots,i_k}\)_, but with_ \(X''_k\) _in place of_ \(X'_k\)_, where the_ \(X''_k\)_’s have same distribution as the X<sub>k</sub>’s and are independant of all previous random variables. Then,_

\(B_k(S,T)=\mathbb{E}\frac{1}{2n!}\sum_{i\in\mathfrak{S}_n}\Delta_{i_k}(T^{\widetilde{i_1},\dots,\widetilde{i_k-1}})\Delta_{i_k}(S^{i_1,\dots,i_{k-1}}).\)

## 2 Connections with decompositions of the variance

### 2.1 Connection with a more general decomposition of the variance

Let _U_<sub>1</sub>_,...,U<sub>n</sub>_ be random variables taking values in (0,1) and independent of _X_<sub>1</sub>_,...,X<sub>n</sub>_,\(X'_1,\dots,X'_n\). For any \(\alpha\in[0,1]\), let \(X^{(\alpha)}\) be the vector with coordinates \(X_i^{(\alpha)}:=\mathbb{1}_{\alpha\le U_i}X_i+\mathbb{1}_{\alpha>U_i}X'_i\), \(1\le i\le n\). Then,<tbc>

\(\mathrm{Var}S=\mathbb{E}\left(S(X^{(0)})\left(S(X^{(0)})-S(X^{(1)})\right)\right),\)

<tbc>and it is tempting to rewrite this last term as an integral. Let us assume that each _U<sub>i</sub>_ has a density \(\nu_i\). For any \(0\le\alpha<\alpha'\le 1\), denote by \(A_{\alpha,\alpha^\prime}\) the random set of indices \(i\in\{1,\dots,n\}\) such that \(\alpha\le U_i<\alpha'\). Then, conditioning on the cardinality of \(A_{\alpha,\alpha^\prime}\), applying the Cauchy-Schwarz inequality and an inductive argument lead to:

\(\left|\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha^\prime)})\right)-\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha)})\right)\right|\le 2\mathbb{E}(S^2)\mathbb{P}\left(|A_{\alpha,\alpha^\prime}|>0\right)\)<br>
\(\le 2\mathbb{E}(S^2)\mathbb{E}|A_{\alpha,\alpha^\prime}|\)<br>
\(=2\mathbb{E}(S^2)\sum_{i=1}^n\int_\alpha^{\alpha^\prime}\mathrm{d}\nu_i.\)

Therefore, \(\alpha\mapsto\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha)})\right)\) is absolutely continuous, its derivative is well defined almost everywhere, integrable, and

\(\mathrm{Var}S=\mathbb{E}\left(S(X^{(0)})S(X^{(0)})\right)-\mathbb{E}\left(S(X^{(0)})S(X^{(1)})\right)=-\int_0^1\frac{\mathrm{d}}{\mathrm{d}\alpha}\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha)})\right)\mathrm{d}\alpha.\) (2.1)

