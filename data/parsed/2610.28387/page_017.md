## 4.1 Exact covariance including sample means

The first multivariate L-moment is the mean vector (Serfling and Xiao, 2007). Including it is important for subsequent multivariate L-moment estimation, in particular when location parameters are unknown. Put \(\overline{Z}=n^{-1}\sum_{i=1}^nZ_i\) and \(\widehat{\mathbf{T}}_n=(\overline{Z^\mathsf{T}},\widehat{\unknown^\mathsf{T}})^\mathsf{T}\).

**Theorem 4.2** (Exact covariance including sample means)**.** _Assume_ \(\mathbb{E}(X^2+Y^2)<\infty\)_. Define the six-dimensional first-order projection and its covariance by_

\(\phi(z)=\left(\begin{array}{ c }
z-\mathbb{E}(Z) \\
2\mathbf{a}(z) \\
3\mathbf{b}(z)
\end{array}\right),\Omega=\mathbb{E}(\phi(Z)\phi(Z)^\mathsf{T}).\) (4.7)

_For every_ \(n\ge 3\),

\(\mathrm{Cov}(\widehat{\mathbf{T}}_n)=\frac{\Omega}{n}+\left(\begin{array}{ c c }
0_{2\times 2} & 0_{2\times 4} \\
0_{4\times 2} & \frac{B_2}{\genfrac(){pt}{2}{n}{2}}+\frac{B_3}{\genfrac(){pt}{2}{n}{3}}
\end{array}\right).\) (4.8)

_More generally, for any square-integrable W=h(Z_) _and m_=2,3,

\(\mathrm{Cov}\big(\overline{W},\widehat{\lambda}_m^a\big)=\frac{m}{n}\mathrm{Cov}\big(W,M_{m,1}^a(Z)\big),a\in\{[XY],[YX]\}.\) (4.9)

_Proof._ Write _W<sub>i</sub>=h(Z<sub>i</sub>_). Expand the covariance of \(\overline{W}=n^{-1}\sum_iW_i\) and the complete U-statistic \(\widehat{\lambda}_m^a\):

\(\mathrm{Cov}(\overline{W},\widehat{\lambda}_m^a)=\frac{1}{n\genfrac(){pt}{2}{n}{m}}\sum_{i=1}^n\sum_{|I|=m}\mathrm{Cov}\{W_i,H_m^a(Z_I)\}\)<br>
\(=\frac{m}{n}\mathrm{Cov}\{W_1,H_m^a(Z_1,\dots,Z_m)\}\)<br>
\(=\frac{m}{n}\mathrm{Cov}\{W,M_{m,1}^a(Z)\}.\)

The first equality uses independence for terms with \(i\notin I\); exactly \(m\genfrac(){pt}{2}{n}{m}\) terms have \(i\in I\). The final equality conditions on the common pair. Since **_a_** and **_b_** are centered, these cross- covariances equal the off-diagonal blocks of \(\Omega/n\). The sample-mean covariance is Cov(_Z)/n_, and the remaining \(4\times 4\) block is (4.5), proving (4.8).

**Corollary 4.3** (Asymptotic normality)**.** _Assume_ \(\mathbb{E}(X^2+Y^2)<\infty\)_, and let_ \(\mathbf{T}=(\mathbb{E}(Z)^\mathsf{T},\unknown^\mathsf{T})^\mathsf{T}\)_. Then_ \(\sqrt{n}(\widehat{\mathbf{T}}_n-\mathbf{T})\) _converges in distribution to_ \(N_6(0,\Omega)\)_. The matrix_ \(\Omega\) _may be singular; the normal law is then supported on a lower-dimensional subspace._

_Proof._ The Hoeffding expansions in the proof of Theorem 4.1 give<tbc>

\(\widehat{\mathbf{T}}_n-\mathbf{T}=\frac{1}{n}\sum_{i=1}^n\phi(Z_i)+\mathbf{R}_n,\)

