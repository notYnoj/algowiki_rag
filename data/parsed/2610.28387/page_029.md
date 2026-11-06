<tbc>The unbiased estimator performs as the theory predicts. It shows no detectable bias: its largest standardized difference is at most 3.07 over 36 correlated entries, and its relative bias, which is itself subject to Monte Carlo error, is below 2% in every setting, including the heavy-tailed design. In the independent design, its mean also agrees with the exact block of Theorem 3.4. The frequencies of non-PSD estimates in the Gaussian design (98.9%, 81.4%, and 29.7%) agree closely with those in  2, which were obtained with the R implementation and different random numbers. Projection onto the PSD cone removes the indefiniteness at the cost of a small bias at _n_=20, with standardized differences up to about 6 and relative bias below 2%, and it changes the estimator very little for \(n\ge 30\).

The projection-based estimator \(\widehat{\Omega}_n/n\), in contrast, is systematically biased, because it targets only the leading term \(\Omega/n\) of (4.8). At _n_=20 its diagonal entries understate the true variances by up to about 14%; its relative bias decreases from 7-13% at _n_=20 to 3-5% at _n_=50, and its largest standardized differences remain between 5 and 29. Nevertheless, it has the smaller relative RMSE in all nine settings, by 6-16% relative to \(\widehat{C}_n\), because it is less variable.  3 therefore does not show that the unbiased estimator is uniformly better in small samples; the two estimators exhibit a bias-variance trade-off.

If the aim is to minimize the bias of the estimated finite-sample covariance, the unbiased estimator, or its PSD projection, is preferable; this is the relevant criterion when standard errors should not be understated or when covariance estimates are averaged over many sites or samples, because random errors then average out whereas the bias of \(\widehat{\Omega}_n/n\) does not. If<tbc>

\begin{tabular}{cccccccccccc}
 & & & & \multicolumn{3}{c}{Unbiased \(\widehat{C}_n\)} & \multicolumn{2}{c}{PSD \(\widehat{C}_n^+\)} & \multicolumn{3}{c}{Projection \(\widehat{\Omega}_n/n\)} \\
Design & _n_ & Non-PSD (%) & Max. |_z_| & RB & RMSE & Max. |_z_| & RB & Max. |_z_| & RB & RMSE \\
Independent & 20 & 99.4 & 2.32 & 1.15 & 1.399 & 5.08 & 1.71 & 29.44 & 8.54 & 1.194 \\
Independent & 30 & 81.9 & 1.30 & 0.48 & 1.127 & 1.93 & 0.66 & 20.44 & 5.28 & 1.017 \\
Independent & 50 & 18.4 & 2.12 & 0.70 & 0.853 & 2.12 & 0.70 & 14.67 & 3.37 & 0.803 \\
Gaussian & 20 & 98.9 & 2.62 & 0.69 & 0.929 & 6.07 & 1.37 & 25.15 & 7.23 & 0.784 \\
Gaussian & 30 & 81.4 & 2.18 & 0.57 & 0.728 & 2.23 & 0.58 & 18.96 & 4.66 & 0.653 \\
Gaussian & 50 & 29.7 & 3.07 & 0.56 & 0.545 & 3.07 & 0.56 & 13.37 & 2.99 & 0.512 \\
GEV copula & 20 & 99.4 & 1.42 & 1.81 & 2.898 & 1.61 & 1.80 & 10.68 & 12.92 & 2.432 \\
GEV copula & 30 & 86.4 & 1.14 & 0.89 & 2.636 & 1.14 & 1.00 & 6.67 & 7.04 & 2.345 \\
GEV copula & 50 & 32.3 & 0.69 & 0.49 & 2.188 & 0.68 & 0.50 & 5.29 & 4.55 & 2.042 \\
\end{tabular}

3: Comparison of covariance estimators with high-precision reference covariances (_R_=20000; reference from 10<sup>6</sup> replications). RB and RMSE are the relative bias (%) and the relative root mean squared error defined in Section 6.3.

_Note._ Max. |_z_| is taken over the 36 distinct entries of the \(8\times 8\) matrix. In the independent design, the largest absolute standardized difference between the mean of \(\widehat{C}_n\) and the exact block of Theorem 3.4 over its ten distinct entries is 2.05, 0.94, and 2.67 for _n_=20,30,50. Seed 20261018 (NumPy generator).

