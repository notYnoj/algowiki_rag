where **_R_**_<sub>n</sub>_ collects the canonical terms of orders two and three. Since **_R_**_<sub>n</sub>_ has mean zero, \(\mathbb{E}(\|\mathbf{R}_n\|^2)=\mathrm{tr}\{\mathrm{Cov}(\mathbf{R}_n)\}=\mathrm{tr}(B_2)/\genfrac(){pt}{2}{n}{2}+\mathrm{tr}(B_3)/\genfrac(){pt}{2}{n}{3}=O(n^{-2})\). Hence \(\sqrt{n}\mathbf{R}_n\rightarrow 0\) in probability. The ordinary multivariate central limit theorem and Slutsky’s lemma therefore give the stated limit.

By (4.8), the covariance matrix of the sample means and the cross-covariances (4.9) between the sample means and the sample L-comoments are exactly the corresponding blocks of \(\Omega/n\) for every _n_. The correction terms \(B_2/\genfrac(){pt}{2}{n}{2}\) and \(B_3/\genfrac(){pt}{2}{n}{3}\) appear only in the \(4\times 4\) block of the sample L-comoments. The reason is that a sample mean is a U-statistic of order one, so its kernel can share at most one pair with any other kernel; only the overlap _c_=1, which gives the leading term, then occurs in (3.4).

## 4.2 A consistent estimator of the leading covariance

For asymptotic inference, only the leading term \(\Omega/n\) in (4.8) is needed, because the remaining terms are of order _n_<sup>-2</sup>. The leading term has a simple structure: by (4.7), \(\Omega\) is the covariance matrix of the centered and scaled first projections \(\unknown(Z)\). We therefore estimate \(\Omega\) by the sample covariance matrix of estimated first projections. A matrix of this form is PSD for any observed data set, not only on average or in the limit, which is convenient when the estimate must be inverted.

The first projection \(M_{m,1}^a(z)\) (Section 3) is the mean of the kernel \(H_m^a\) when one of its _m_ pairs is fixed at _z_ and the other _m_-1 pairs are drawn from the distribution of (_X,Y_). Its empirical version replaces this distribution by the other observations. For the _i_th observation, we keep _Z<sub>i</sub>_ as the fixed pair and average the kernel over all subsets _J_ of _m_-1 of the remaining _n_-1 observations:

\(\widehat{M}_{m,1}(Z_i)=\genfrac(){pt}{2}{n-1}{m-1}^{-1}\sum_{J\subset\{1,\dots,n\}\backslash\{i\}|J|=m-1}\mathbf{H}_m(Z_i,Z_J),i=1,\dots,n.\) (4.10)

Thus \(\widehat{M}_{m,1}(Z_i)\) is the average of all kernel values that involve the _i_th pair, and it measures the contribution of that pair to \(\widehat{\unknown}_m\); indeed, \(n^{-1}\sum_{i=1}^n\widehat{M}_{m,1}(Z_i)=\widehat{\unknown}_m\). For a symmetric matrix _A_, we write \(A\unknown 0\) if _A_ is PSD and \(A\succ 0\) if _A_ is positive definite; for symmetric _A_<sub>1</sub> and _A_<sub>2</sub>, \(A_1\unknown A_2\) means \(A_1-A_2\unknown 0\), which defines the Loewner order. The exact finite-sample covariance, including _B_<sub>2</sub> and _B_<sub>3</sub>, is estimated without bias in Section 4.3.

**Theorem 4.4** (PSD consistent covariance estimator)**.** _Assume_ \(\mathbb{E}(X^2+Y^2)<\infty\)_. With_ \(\widehat{M}_{m,1}\) _in_ (4.10)_, define_ \(\widehat{\unknown}_i\) _and_ \(\widehat{\Omega}_n\) _by_

\(\widehat{\unknown}_i=\left(\begin{array}{ c }
Z_i-\overline{Z} \\
2\{\widehat{M}_{2,1}(Z_i)-\widehat{\unknown}_2\} \\
3\{\widehat{M}_{3,1}(Z_i)-\widehat{\unknown}_3\}
\end{array}\right),\widehat{\Omega}_n=\frac{1}{n}\sum_{i=1}^n\widehat{\unknown}_i\widehat{\unknown}_i^\mathsf{T}.\) (4.11)

