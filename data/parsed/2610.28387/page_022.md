_Proof._ For orders \(m,s\le 3\), let _V<sub>c,n</sub>_ average \(H_m^a(Z_I)H_s^b(Z_J)\) over pairs of index sets with \(|I\cap J|=c\). With \(p_{c,n}=\genfrac(){pt}{2}{m}{c}\genfrac(){pt}{2}{n-m}{s-c}/\genfrac(){pt}{2}{n}{s}\) and \(V_{0,n}=D_{ms,n}^{ab}\), the overlap decomposition gives

\(\widehat{C}_{ms,n}^{ab}=\sum_{c=1}^{min(m,s)}p_{c,n}\{V_{c,n}-V_{0,n}\}.\)

For each fixed _c_, _V<sub>c,n</sub>_ is a symmetrized U-statistic of order _m+s-c_ with an integrable product kernel, by Cauchy-Schwarz. The strong law of large numbers for fixed-order U-statistics (Serfling, 1980) gives \(V_{c,n}\rightarrow v_c\) almost surely. Moreover, \(np_{1,n}\rightarrow ms\) and \(np_{c,n}\rightarrow 0\) for \(c\ge 2\). Since \(v_0=\lambda_m^a\lambda_s^b\) and conditioning on the shared observation gives \(v_1=\mathbb{E}(M_{m,1}^a(Z)M_{s,1}^b(Z))\), we obtain

\(n\widehat{C}_{ms,n}^{ab}\longrightarrow^{\mathrm{a}.\mathrm{s}.}ms\mathrm{Cov}\{M_{m,1}^a(Z),M_{s,1}^b(Z)\}.\)

Applied to every entry of the enlarged moment vector, this limit is \(\Omega\). Theorem 4.4 then gives the second assertion in (4.14).

## 5 Computation of the covariance estimators

An R implementation of all estimators in this section, including the quadratic-time unbiased estimator, the projection estimator, and the PSD and PD corrections, is publicly available at `https://github.com/palakorn-seenoi/sample\_Lcomom`.

### 5.1 Fast evaluation of the covariance estimators

Direct evaluation of the disjoint-subset estimator (4.12) enumerates pairs of disjoint index sets and requires _O(n_<sup>6</sup>) operations for the order-three/order-three block. In this section we show that the same estimator can be computed in _O(n_<sup>2</sup>) time. The next identity is a computational specialization of the inclusion-exclusion principle, not a new unbiasedness theorem. Our implementation uses static two-dimensional rank-prefix tables, the technique of summed-area tables (Crow, 1984) and integral images (Viola and Jones, 2004).

**Proposition 5.1** (Overlap representation and efficient evaluation)**.** _For_ \(m,s\in\{1,2,3\}\) _and the kernels in Theorem 4.8, set_ \(\widetilde{H}_m^a(Z_I)=H_m^a(Z_I)-U_{n,m}^a\) _and_<tbc>

\(A_{m,K}^a=\sum_{I\supseteq K|I|=m}\widetilde{H}_m^a(Z_I),|K|\le m.\) (5.1)

<tbc>_For_ \(n\ge m+s\)_, the exactly unbiased estimator satisfies_

\(\widehat{C}_{ms,n}^{ab}=\frac{\sum_{c=1}^{min(m,s)}(-1)^{c+1}\sum_{|K|=c}A_{m,K}^aA_{s,K}^b}{\genfrac(){pt}{2}{n}{m}\genfrac(){pt}{2}{n-m}{s}}}.\) (5.2)

