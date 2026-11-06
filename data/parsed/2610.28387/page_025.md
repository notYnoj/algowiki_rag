eigenvalue. Hence \(\mathbb{E}(\widehat{C}_n^+)-\mathrm{Cov}(\widehat{T}_n)\) is PSD, and it is nonzero whenever \(\widehat{C}_n\) is indefinite with positive probability. When the estimate must be inverted, a positive-definite (PD) correction is needed as well.

_Remark_ 5.4 (PSD and positive-definite correction). Write _C<sub>n</sub>_ for the true finite-sample covariance matrix of the moment vector, for example \(C_n=\mathrm{Cov}(\widehat{T}_n)\). The eigenvalue truncation below is the nearest symmetric PSD matrix in Frobenius norm (Higham, 1988); related eigenvalue- constrained covariance estimation is discussed by Liu et al. (2014). Write \(\mathcal{S}_n=n\widehat{C}_n=V_n\mathrm{diag}(d_{1n},\dots,d_{pn})V_n^\mathsf{T}\). Its PSD correction replaces _d<sub>jn</sub>_ by \(d_{jn}^+=\mathrm{max}(d_{jn},0)\); since _C<sub>n</sub>_ is PSD, projection also gives \(\|\widehat{C}_n^+-C_n\|_F\le\|\widehat{C}_n-C_n\|_F\). For inversion, choose \(\varepsilon_n>0\) with \(\varepsilon_n\rightarrow 0\) and define

\(\widehat{C}_n^\mathrm{PD}=\frac{1}{n}V_n\mathrm{diag}\{\mathrm{max}(d_{1n},\varepsilon_n),\dots,\mathrm{max}(d_{pn},\varepsilon_n)\}V_n^\mathsf{T}.\) (5.8)

Then \(\widehat{C}_n^\mathrm{PD}\succ 0\) for any observed data set and \(n\widehat{C}_n^\mathrm{PD}\rightarrow\Omega\) almost surely. If \(\Omega\succ 0\), the inverse of the corrected _scaled_ covariance converges to \(\Omega^{-1}\). When \(\Omega\) is singular, PD regularization does not make a consistent estimator of a nonexistent \(\Omega^{-1}\). Neither PSD nor PD correction generally retains finite-sample unbiasedness.

The statistical properties of the two corrections can be summarized as follows.

(a) _Consistency._ Both corrections preserve first-order consistency: \(n\widehat{C}_n^+\rightarrow\Omega\) by Corollary 5.3, and \(\|n\widehat{C}_n^\mathrm{PD}-n\widehat{C}_n^+\|_F\le p^{1/2}\varepsilon_n\rightarrow 0\) because the two matrices differ only in eigenvalues below \(\varepsilon_n\).<tbc>

(b) _Unbiasedness._ Neither correction is unbiased. Since \(\widehat{C}_n^\mathrm{PD}\unknown\widehat{C}_n^+\unknown\widehat{C}_n\) in the Loewner order, both corrections shift the estimator upward, and the shift is nonzero on the event that \(\widehat{C}_n\) is indefinite.  3 shows that this bias is small for the PSD projection.<tbc>

(c) _Singular limit._ If \(\Omega\) is singular, for example when some linear combination of the moments has a degenerate first-order projection, the corrected matrices remain consistent for \(\Omega\). Their smallest eigenvalues, however, tend to zero, and inverse-covariance weighting is ill-posed in the limit. A generalized inverse or a reduced moment vector is then more appropriate than inversion of \(\widehat{C}_n^\mathrm{PD}\).<tbc>

(d) _Role of_ \(\varepsilon_n\). The floor \(\varepsilon_n\) guarantees invertibility for any observed data set and bounds the condition number of \(n\widehat{C}_n^\mathrm{PD}\) by \(\mathrm{max}_jd_{jn}/\varepsilon_n\); the condition \(\varepsilon_n\rightarrow 0\) ensures that the regularization vanishes asymptotically. A larger floor stabilizes the inverse at the cost of more upward bias. Our implementation uses \(\varepsilon_n=n^{-1}p^{-1}\sum_j|d_{jn}|\), which is _O(n_<sup>-1</sup>); in the Gaussian design of Section 6.3, its median is 0.020 and 0.008 for _n_=20 and 50, about 1% of the largest eigenvalue of \(n\widehat{C}_n\).<tbc>

