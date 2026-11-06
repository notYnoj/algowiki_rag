_Then_ \(\widehat{\Omega}_n\unknown 0\) _for any observed data set, and_ \(\widehat{\Omega}_n\rightarrow^p\Omega\) _as_ \(n\rightarrow\infty\)_. The lower-right_ \(4\times 4\) _block of_ \(\widehat{\Omega}_n\) _consistently estimates B_<sub>1</sub>_, not the exact finite-sample covariance_ \(\mathrm{Cov}(\widehat{\unknown})\).

The proof, given in Appendix D, approximates the empirical first projections in mean square and then applies the law of large numbers.

**Corollary 4.5** (Augmentation by marginal L-moments)**.** _The overlap identity_ (3.4) _and the projection-based consistent estimator in Theorem 4.4 remain valid, entrywise, after appending any finite collection of univariate sample L-moments of orders two and three from either margin._

For example, the ratio \(\widehat{\tau}_2^{[XY]}=\widehat{\lambda}_2^{[XY]}/\widehat{\lambda}_2(X)\) requires the covariance of \(\widehat{\lambda}_2^{[XY]}\) and the sample L-scale \(\widehat{\lambda}_2(X)\). The sample L-scale is the U-statistic with kernel \(H_2^{[XX]}(z_1,z_2)=|x_1-x_2|/2\), that is, (2.5) with _Y_ replaced by _X_; its first projection \(M_{2,1}^{[XX]}\) is (3.7) with _Y_ replaced by _X_. The overlap identity gives

\(\mathrm{Cov}\big(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_2(X)\big)=\frac{4(n-2)}{n(n-1)}\mathrm{Cov}\big\{M_{2,1}^{[XY]}(Z),M_{2,1}^{[XX]}(Z)\big\}\)<br>
\(+\frac{2}{n(n-1)}\big[\frac{1}{4}\mathbb{E}\big\{(X-X')|X-X'|\mathrm{sgn}(Y-Y')\big\}-\lambda_2^{[XY]}\lambda_2(X)\big],\)

where \((X',Y')\) is an independent copy of (_X,Y_). The projection estimator of its leading term is

\(\frac{4}{n^2}\sum_{i=1}^n\big\{\widehat{M}_{2,1}^{[XY]}(Z_i)-\widehat{\lambda}_2^{[XY]}\big\}\big\{\widehat{M}_{2,1}^{[XX]}(Z_i)-\widehat{\lambda}_2(X)\big\},\widehat{M}_{2,1}^{[XX]}(Z_i)=\frac{1}{n-1}\sum_{j\neq i}\frac{|X_i-X_j|}{2}.\)

_Proof._ Write \(\widehat{\lambda}_m(X)\) for the univariate sample L-moment of order _m_. It is the complete U- statistic with kernel \(H_m^{[XX]}\), obtained from \(H_m^{[XY]}\) in (2.5)-(2.6) by replacing _Y_ with _X_; for example, \(H_2^{[XX]}(z_1,z_2)=|x_1-x_2|/2\). Define \(H_m^{[YY]}\) and \(\widehat{\lambda}_m(Y)\) in the same way. These kernels are symmetric, have means \(\lambda_m(X)\) and \(\lambda_m(Y)\), and are square integrable when \(\mathbb{E}(X^2+Y^2)<\infty\).

_Overlap identity._ The derivation of (3.4) in Section 3 uses only that the two statistics are complete U-statistics of the same iid pairs with symmetric kernels. Hence (3.4) holds for \(a,b\in\{[XY],[YX],[XX],[YY]\}\), with \(M_{m,c}^a\) and \(\Gamma_{ms,c}^{ab}\) defined by (3.1) and (3.3).

_Projection estimator._ Append to \(\widehat{\unknown}_i\) in (4.11) the components \(m\{\widehat{M}_{m,1}^a(Z_i)-\widehat{\lambda}_m(X)\}\) for _a_=\[_XX_\] and \(m\{\widehat{M}_{m,1}^a(Z_i)-\widehat{\lambda}_m(Y)\}\) for _a_=\[_YY_\], where \(\widehat{M}_{m,1}^a\) is (4.10) with the kernel \(H_m^a\). The enlarged \(\widehat{\Omega}_n=n^{-1}\sum_i\widehat{\unknown}_i\widehat{\unknown}_i^\mathsf{T}\) is an average of outer products and is therefore PSD. The proof in Appendix D uses only two properties of each component: the mean-square bound (D.1), which holds for any symmetric square-integrable kernel of order _m_, and the law of large numbers. Both hold for the appended components, so \(\widehat{\Omega}_n\) converges in probability to the covariance matrix of the enlarged vector of centered and scaled first projections.

**Corollary 4.6** (Extension to fourth-order L-comoments)**.** _Theorem 4.4 remains valid for the enlarged vector that also contains_ \(\widehat{\lambda}_4^{[XY]}\) _and_ \(\widehat{\lambda}_4^{[YX]}\)_, with the corresponding components_ \(4\{\widehat{M}_{4,1}(Z_i)-\widehat{\lambda}_4^a\}\), \(a\in\{[XY],[YX]\}\)_, in_ \(\widehat{\unknown}_i\)_, provided_ \(n\ge 5\) _and the kernel of order four is taken from_ (2.4).

