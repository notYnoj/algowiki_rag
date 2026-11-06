<tbc>corrections do not, in general, preserve unbiasedness. These empirical frequencies are specific to the distribution, estimator, and sample sizes considered.

## 6.3 Comparison with high-precision reference covariances

In  2, <o>_C_</o><sub>n</sub> is compared with an empirical covariance computed from the same _R_=1000 replications, so the reference itself carries Monte Carlo error of the same order as the quantity being assessed. We therefore ran a second study in which the reference covariance is computed much more precisely and in which three covariance estimators are compared. Three designs were considered:

(i) independent variables, _X_∼Exp(1) and _Y_∼Gumbel(0,1), for which Theorem 3.4 gives the exact \(4\times 4\) L-comoment block;<tbc>

(ii) the Gaussian design above with \(\rho=0.6\); and<tbc>

(iii) a Gaussian copula with correlation 0.6 and generalized extreme-value margins with location 0, scale 1, and shape \(\xi=0.2\), which have a heavy upper tail and finite variance.

Design (iii) represents the skewed, heavy-tailed data that motivate L-moment methods. For each design and \(n\in\{20,30,50\}\), the reference covariance _C<sub>n</sub>_ was computed from 10<sup>6</sup> independent replications of \(\widehat{\mathbf{M}}_n\); this requires only the sample moments, not their covariance estimators. In design (i), the reference agreed with Theorem 3.4 to within 0.3% of the corresponding standard deviations for all ten distinct entries of the \(4\times 4\) block, which also confirms the closed form numerically.

We then generated _R_=20000 further samples for each setting and computed three estimators: the unbiased estimator \(\widehat{C}_n\), its PSD projection \(\widehat{C}_n^+\), and the projection-based estimator \(\widehat{\Omega}_n/n\) of Theorem 4.4. For a generic estimator \(\widetilde{C}_n\),  3 reports the largest absolute standardized difference between the Monte Carlo mean of \(\widetilde{C}_n\) and _C<sub>n</sub>_ over the 36 distinct entries, with standard errors that combine the Monte Carlo errors of both quantities; the relative bias (RB); and the relative root mean squared error (RMSE). To make entries of different scales comparable, let \(\Psi_n=\text{diag}(C_n)\) and, for a \(p\times p\) matrix _A_ with _p_=8, let \(\|A\|_*=\|\Psi_n^{-1/2}A\Psi_n^{-1/2}\|_F\) be the Frobenius norm after each entry has been divided by the product of the corresponding reference standard deviations. Then

\(\text{RB}=100\times\frac{\|\mathbb{E}(\widetilde{C}_n)-C_n\|_*}{\|C_n\|_*},\text{RMSE}=\frac{\{\mathbb{E}(\|\widetilde{C}_n-C_n\|_*^2)\}^{1/2}}{\|C_n\|_*},\)

where the expectations are Monte Carlo averages over the _R_ samples. Thus RB measures the systematic error of an estimator, and RMSE measures its total error, both relative to the size of _C<sub>n</sub>_; an RMSE of one means that the typical estimation error is as large as _C<sub>n</sub>_ itself on the standardized scale.

