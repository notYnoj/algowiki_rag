There are \(\genfrac(){pt}{2}{n-1}{m-1}\) such subsets, so dividing by this number gives (4.10) and hence (5.3); see also (A.3).

_Step 2._ By the probability-weighted-moment representation of Hosking (1990), with order statistics replaced by concomitants (Serfling and Xiao, 2007, Proposition 7), the sample L-comoment of order _m_ is \(\sum_{k=0}^{m-1}p_{m-1,k}^*b_k\), where \(b_k=n^{-1}\sum_{q=1}^n\genfrac(){pt}{2}{q-1}{k}\genfrac(){pt}{2}{n-1}{k}^{-1}v_q\); see also Appendix B.3. Collecting the coefficient of _v<sub>q</sub>_ gives the weights (5.4) with _N=n_.

_Step 3._ Delete the observation with _Y_ -rank _r_. The remaining _n_-1 concomitants, in the order of their _Y_ values, are _v_<sub>1</sub>_,...,v_<sub>_r_-1</sub>_,v_<sub>_r_+1</sub>_,...,v<sub>n</sub>_. In the reduced sample, _v<sub>q</sub>_ has rank _q_ if _q\<r_ and rank _q_-1 if _q\>r_. Applying the weights (5.4) with _N=n_-1 therefore gives

\(U_{n-1}^{[XY],(-i)}=\sum_{q<r}w_{m,q}^{(n-1)}v_q+\sum_{q>r}w_{m,q-1}^{(n-1)}v_q=A_{r-1}+S_{r+1}.\)

_Step 4._ Sorting each ranking coordinate costs _O(n_log_n_). The weights \(w_{m,q}^{(n-1)}\), the prefix sums _A_<sub>0</sub>_,...,A_<sub>_n_-1</sub>, and the suffix sums _S_<sub>2</sub>_,...,S_<sub>_n_+1</sub> each take _O(n_) operations, after which each leave-one-out statistic (5.6) takes _O_(1) operations. The sample means are handled by <o>_X_</o><sup>(-_i_)</sup>=(_n<o>X</o>-X<sub>i</sub>)/(n_-1). Finally, (5.3) gives all empirical first projections in _O(n_) operations, and \(\widehat{\Omega}_n\) in _O(np_<sup>2</sup>) operations for a moment vector of dimension _p_. We also verified (5.6) and (5.3) against direct enumeration of all subsets for _m_=2,3,4.

## 5.2 PSD and positive-definite corrections

Unbiasedness holds entry by entry and on average over repeated samples. It does not imply that the matrix computed from the observed sample is PSD: the assembled estimator can have negative eigenvalues, especially for small _n_ ( 3). We therefore consider its PSD correction. Let \(\|A\|_F=\{\mathrm{tr}(A^\mathsf{T}A)\}^{1/2}=(\sum_{i,j}a_{ij}^2)^{1/2}\) denote the Frobenius norm. The PSD correction \(\widehat{C}_n^+\) of a symmetric matrix \(\widehat{C}_n\) is its Frobenius projection onto the set of PSD matrices (Higham, 1988), that is, the PSD matrix _A_ that minimizes \(\|A-\widehat{C}_n\|_F\). If \(\widehat{C}_n=V\mathrm{diag}(d_1,\dots,d_p)V^\mathsf{T}\) is the spectral decomposition, where _p_ is the dimension of the moment vector, then \(\widehat{C}_n^+=V\mathrm{diag}\{\mathrm{max}(d_1,0),\dots,\mathrm{max}(d_p,0)\}V^\mathsf{T}\); that is, the negative eigenvalues are replaced by zero.

**Corollary 5.3** (PSD correction)**.** _Under the conditions of Corollary 4.9,_ \(\widehat{C}_n^+\unknown 0\) _for any observed data set and_

\(n\widehat{C}_n^+\longrightarrow^{\mathrm{a}.\mathrm{s}.}\Omega.\) (5.7)

_Proof._ Projection onto the closed convex set of PSD matrices is continuous and commutes with multiplication by a nonnegative scalar, so \(n\widehat{C}_n^+=(n\widehat{C}_n)^+\). Since \(n\widehat{C}_n\rightarrow\Omega\) almost surely by Corollary 4.9 and \(\Omega\unknown 0\), we obtain \((n\widehat{C}_n)^+\rightarrow\Omega^+=\Omega\) almost surely.

The PSD correction thus retains first-order consistency, but it generally does not preserve exact unbiasedness. Indeed, \(\widehat{C}_n^+-\widehat{C}_n\) is PSD and is nonzero whenever \(\widehat{C}_n\) has a negative<tbc>

