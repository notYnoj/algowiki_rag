<tbc>cost. The growing advantage is consistent with the _O(n_<sup>2</sup>) arithmetic complexity established in Proposition 5.1; the three measured sizes alone do not constitute a complexity proof.

## 6.2 Finite-sample behavior of the unbiased estimator

For each \(n\in\{20,30,50\}\), we computed in each of _R_=1000 replications both the unbiased covariance estimate \(\widehat{C}_n^{(b)}\) and the corresponding moment vector \(\widehat{\mathbf{M}}_n^{(b)}\). The mean of the covariance estimates was compared with the sample covariance of the replicated moment vectors,

\(\overline{C_n}=R^{-1}\sum_{b=1}^R\widehat{C}_n^{(b)},C_{n,\mathrm{MC}}=\frac{1}{R-1}\sum_{b=1}^R(\widehat{\mathbf{M}}_n^{(b)}-\overline{\mathbf{M}_n})(\widehat{\mathbf{M}}_n^{(b)}-\overline{\mathbf{M}_n})^\mathsf{T}.\)

Both quantities estimate the same finite-sample sampling covariance, but their difference is subject to Monte Carlo variation.  2 reports the root mean squared entrywise difference, the relative Frobenius difference \(\|\overline{C_n}-C_{n,\mathrm{MC}}\|_F/\|C_{n,\mathrm{MC}}\|_F\), and the largest absolute standardized difference among the 36 distinct entries. For each entry, the standardized difference is \(z=(\bar{c}-c)/\mathrm{se}\), where \(\bar{c}\) is the entry of <o>_C_</o><sub>n</sub>, _c_ is the corresponding entry of _C<sub>n,</sub>_MC, and se is the Monte Carlo standard error of \(\bar{c}-c\). We also report the fraction of covariance estimates having a negative minimum eigenvalue.

The standardized discrepancies are moderate (maximum absolute values 1.71, 2.57, and 2.88), and the simulation findings do not contradict the exact unbiasedness established in Theorem 4.8. The RMS differences decrease over the three sample sizes, but the relative Frobenius differences do not decrease monotonically; the simulation should not be interpreted as demonstrating a general rate of convergence. In particular, the empirical reference covariance is itself estimated with Monte Carlo error.

The proportion of non-PSD unbiased estimates drops from 99.0% at _n_=20 to 29.3% at _n_=50 in this Gaussian design. The median minimum eigenvalue changes from \(-5.96\times 10^{-4}\) to \(1.45\times 10^{-5}\). This illustrates the distinction between finite-sample unbiasedness and the samplewise PSD property, and motivates the eigenvalue corrections in Remark 5.4. Such<tbc>

\begin{tabular}{cccccc}
_n_ & Max. |_z_| & RMS diff. & Rel. Frobenius diff. & Non-PSD (%) & Median min. eigenvalue \\
20 & 1.708 & 0.000926 & 0.0770 & 99.0 & \(-5.957\times 10^{-4}\) \\
30 & 2.571 & 0.000464 & 0.0611 & 82.2 & \(-6.909\times 10^{-5}\) \\
50 & 2.885 & 0.000400 & 0.0920 & 29.3 & \(1.454\times 10^{-5}\) \\
\end{tabular}

2: Monte Carlo diagnostics for the exactly unbiased covariance estimator (_R_=1000, \(\rho=0.6\)).

_Note._ Max. |_z_| is the largest standardized Monte Carlo difference among the 36 distinct covariance entries; it is descriptive rather than a simultaneous test. Non-PSD is the observed percentage of indefinite estimates (negative minimum eigenvalue). The simulation seed was 20261018.

