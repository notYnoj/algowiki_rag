The estimator (2.7) also has a simple weighted-sum form. Let _X_<sub>\[_q:n_\]</sub> be the concomitant of the _q_th smallest _Y_ value in the sample; as in Section 2, _X_<sub>\[_q:n_\]</sub> is not the _q_th order statistic of the _X_ values. Then the complete U-statistic (2.7) can be written as a weighted sum of the concomitants (Serfling and Xiao, 2007, Section 3.3):

\(\widehat{\lambda}_m^{[XY]}=\sum_{q=1}^nw_{m,q}X_{[q:n]},w_{2,q}=\frac{2q-n-1}{n(n-1)},w_{3,q}=\frac{6q^2-6(n+1)q+(n+1)(n+2)}{n(n-1)(n-2)}.\) (2.8)

The weights follow by counting how often each pair occupies each position in the kernels; Appendix B gives the details. The weights _w_<sub>2_,q_</sub> require \(n\ge 2\), and the weights _w_<sub>3_,q_</sub> require \(n\ge 3\). They satisfy \(\sum_qw_{m,q}=0\). To make the estimating equations (2.7) and (2.8) more concrete, Appendix B.3 restates both in elementary terms, gives the equivalent probability- weighted-moment form of (2.8), and evaluates both for a sample of size five.

We collect the four L-comoments and their estimators as

\(\unknown=(\lambda_2^{[XY]},\lambda_2^{[YX]},\lambda_3^{[XY]},\lambda_3^{[YX]})^\unknown,\widehat{\unknown}=(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_2^{[YX]},\widehat{\lambda}_3^{[XY]},\widehat{\lambda}_3^{[YX]})^\unknown.\)

By (2.7), \(\widehat{\unknown}\) is unbiased for \(\unknown\). Serfling and Xiao (2007, Proposition 8) showed that, under second-moment assumptions, the sample L-comoments of one direction are asymptotically multivariate normal. Their asymptotic covariance matrix is the corresponding block of _B_<sub>1</sub>_/n_ in Theorem 4.1 below. This approximation can be poor for the sample sizes at which L- comoments are typically used. In hydrology, for example, at-site records often contain only 20 to 50 observations, and Section 6.3 shows that the asymptotic covariance then understates the finite-sample covariance. Moreover, applications such as discordancy and homogeneity tests combine L-comoments of several orders and both directions. They therefore require the whole matrix \(\mathrm{Cov}(\widehat{\unknown})\). In current practice, this matrix is approximated by simulation from a fitted parametric model (Chebana and Ouarda, 2007). For these reasons, the main aim of this paper is to derive the exact finite-sample form of \(\mathrm{Cov}(\widehat{\unknown})\) for every fixed _n_, without a parametric model, and to estimate this matrix unbiasedly and efficiently from the data. First-order covariance approximations for the ratios \(\tau_m^{[XY]}\) and \(\tau_m^{[YX]}\) of Section 2 are given in Appendix E.

## 3 Exact finite-sample covariance

In this section we derive the exact finite-sample covariance matrix \(\mathrm{Cov}(\widehat{\unknown})\) for any fixed _n_, without assuming a parametric form for the dependence between _X_ and _Y_ . Theorem 3.1 expresses this matrix through the conditional means of the kernels defined below. Section 3.1 gives these conditional means explicitly, and Section 3.2 obtains the covariance in closed form when _X_ and _Y_ are independent.

