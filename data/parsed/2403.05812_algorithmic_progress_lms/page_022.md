We are assuming that the models from different papers are uncorrelated, and that different models from the same paper have a correlation coefficient of \(\rho\). If we order the models such that all the models from the same paper form a contiguous range of indices, then the correlation matrix looks block diagonal, where each block has 1s on the diagonal and \(\rho\) for the off-diagonal terms. The matrix elements that are not in blocks are all zero. For example, one example correlation matrix is:

\(\left(\begin{array}{ c c c c c c c }
1 & \rho & 0 & 0 & 0 & 0 & 0 \\
\rho & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & \rho & \rho & \rho \\
0 & 0 & \rho & 1 & \rho & \rho \\
0 & 0 & \rho & \rho & 1 & \rho \\
0 & 0 & \rho & \rho & \rho & 1
\end{array}\right)\) (16)

As we can see, we need to determine both the inverse and the determinant of the correlation matrix _P_ in order to calculate the negative log-likelihood. While this can be done using standard libraries, the matrices that we are considering here are quite sparse, and thus it is more efficient to simplify our calculations here. We detail the calculations in sections I.2 and I.3.

## I.1 Results

To determine confidence intervals, we bootstrap this model based on clustering over 100 iterations, in similar fashion to the main results. This yields a median doubling time of 8.1 months, with a 95% confidence interval of 2.9 to 13.8 months, which is consistent with our core estimates. In practice \(\rho\) is typically on the order of 0.45, which suggests that the degree of autocorrelation is not very strong. We report our parameter estimates in  9.

## I.2 Determinant

In order to obtain the overall determinant for _P_ we first work this out for a single block. In particular, the determinant of each \((n+1)\times(n+1)\) block _B<sub>n</sub>_ is given by

\(detB_{n+1}=(1-\rho)^n(1+n\rho).\) (17)

We prove this by considering the associated matrix directly:

\(B_{n+1}=\left(\begin{array}{ c c c c c c c }
1 & \rho & \dots & \rho & \rho & \rho \\
\rho & 1 & \dots & \rho & \rho \\
\vdots &  & \ddots &  &  & \vdots \\
\rho & \rho & \dots & 1 & \rho \\
\rho & \rho & \dots & \rho & 1
\end{array}\right)\) (18)

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\alpha_\text{const}\) & 0.839

(0.691) & -1.181,1.307 \\
\(\alpha_\text{const,PTB}\) & -0.069

(0.378) & -0.684,0.801 \\
\(\alpha_\text{const,WT2}\) & 0.742

(0.390) & 0.049,1.553 \\
\(\alpha_\text{year}\) & 0.026

(0.065) & -0.160,0.034 \\
\(\alpha_\text{param}\) & 0.076<sup>∗</sup>

(0.040) & 0.064,0.203 \\
\(\beta_\text{const}\) & 0.861<sup>∗</sup>

(0.429) & 0.117,1.559 \\
\(\beta_\text{const,PTB}\) & 0.191

(0.304) & -0.232,0.873 \\
\(\beta_\text{const,WT2}\) & -1.081

(0.881) & -3.092,0.168 \\
\(\beta_\text{year}\) & 0.016

(0.027) & 0.005,0.095 \\
\(\beta_\text{data}\) & 0.031<sup>∗</sup>

(0.009) & 0.018,0.043 \\
\end{tabular}

9: Parameter estimates from the model described in equation 8, but estimated using the clustering approach described in equation 15. Estimates are rounded to 3 decimal places. We report 95% confidence intervals for all of the parameter estimates by bootstrapping 100 iterations. \* corresponds to a p value below 5%.

