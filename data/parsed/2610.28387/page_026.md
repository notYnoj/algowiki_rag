## 6 Numerical experiments

We assess the computational efficiency of the quadratic-time algorithm (Sections 6.1 and 6.4) and the finite-sample behavior of the exactly unbiased covariance estimator (Sections 6.2 and 6.3). The accuracy of the first-order ratio approximation is examined in Appendix E.1. Throughout this section, \(\widehat{\mathbf{M}}_n=(\widehat{\mathbf{T}}_n^\mathsf{T},\widehat{\lambda}_2(X),\widehat{\lambda}_2(Y))^\mathsf{T}\) denotes the eight-dimensional vector of the sample means, the four sample L-comoments, and the two marginal sample L-scales, and \(C_n=\mathrm{Cov}(\widehat{\mathbf{M}}_n)\) denotes its exact finite-sample covariance matrix.

Sections 6.1 and 6.2 use independent bivariate Gaussian pairs with unit marginal variances and correlation \(\rho=0.6\). These experiments were run in R 4.5.2 on an Intel Core i5-5200U (2.20 GHz, two physical cores/four logical processors), with 8 GB RAM and Windows 10 Education; times are elapsed wall-clock times. For the timing comparison, both methods use the same simulated dataset at each _n_; the Monte Carlo study uses _R_=1000 independent samples per sample size.

The experiments in Section 6.3 and Appendix E.1 were run with an independent vectorized implementation in Python 3.13 with NumPy 2.5 on a Linux server (Intel Xeon, 2.1GHz, two cores, 8GB RAM). This implementation reproduces direct enumeration of the disjoint-subset estimator to within \(4\times 10^{-16}\) for \(6\le n\le 9\).

### 6.1 Computational efficiency

The direct reference method evaluates the disjoint-subset expression in Theorem 4.8; the fast method evaluates the algebraically equivalent rank-prefix implementation in Proposition 5.1. Both produce the full \(8\times 8\) estimate of _C<sub>n</sub>_ for the vector \(\widehat{\mathbf{M}}_n\).  1 reports elapsed times on the same computer.

The observed speedup increases from 5.73 at _n_=20 to 86.65 at _n_=50, while numerical discrepancies stay below \(3\times 10^{-16}\). Thus, on these datasets, the fast algorithm returns the same covariance estimates to floating-point precision at substantially lower computational<tbc>

\begin{tabular}{ccccc}
_n_ & Direct (s) & Fast (s) & Speedup & Max. absolute difference \\
20 & 0.2100 & 0.0367 & 5.73 & \(8.98\times 10^{-17}\) \\
30 & 1.6400 & 0.0900 & 18.22 & \(2.39\times 10^{-16}\) \\
50 & 22.5300 & 0.2600 & 86.65 & \(2.68\times 10^{-16}\) \\
\end{tabular}

1: Computation of the full \(8\times 8\) exactly unbiased covariance matrix.

_Note._ Each time is the median of three measurements, except for the direct method at _n_=50, measured once. The fast method was batched to reduce timer-resolution effects. Speedup is Direct/Fast. The final column is the largest entrywise absolute difference between the computed matrices; seed 20261017 was used for the Gaussian samples.

