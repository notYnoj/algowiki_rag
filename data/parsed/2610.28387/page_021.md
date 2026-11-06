**Theorem 4.8** (Disjoint-subset unbiased covariance construction)**.** _Let_ \(U_{n,m}^a\) _and_ \(U_{n,s}^b\) _be any two of the following complete U-statistics: the sample means (order one, with kernels_ \(H_1^{[XY]}(z)=x\) _and_ \(H_1^{[YX]}(z)=y\)_), the sample L-comoments (_\(a\in\{[XY],[YX]\}\)_), and the marginal sample L-moments (_\(a\in\{[XX],[YY]\}\)_, with the kernels_ \(H_m^{[XX]}\) _and_ \(H_m^{[YY]}\) _of Corollary 4.5) of orders two and three. The kernel orders are_ \(m,s\in\{1,2,3\}\)_. For_ \(n\ge m+s\)_, define_<tbc>

\(D_{ms,n}^{ab}=\frac{1}{\genfrac(){pt}{2}{n}{m}\genfrac(){pt}{2}{n-m}{s}}\sum_{|I|=m}\sum_{|J|=sI\cap J=\emptyset} H_m^a(Z_I)H_s^b(Z_J).\) (4.12)

<tbc>_Then_

\(\widehat{C}_{ms,n}^{ab}=U_{n,m}^aU_{n,s}^b-D_{ms,n}^{ab},\mathbb{E}(\widehat{C}_{ms,n}^{ab})=\mathrm{Cov}(U_{n,m}^a,U_{n,s}^b).\) (4.13)

_In particular, the conditions are_ \(n\ge 2,3,4\) _for the order pairs_ (1,1),(1,2),(1,3)_, respectively, and_ \(n\ge 4,5,6\) _for_ (2,2),(2,3),(3,3)_. Thus the entire enlarged covariance, including the_ \(6\times 6\) _sampling covariance matrix of the sample means and L-comoments, admits an exactly unbiased estimator for_ \(n\ge 6\).

_Proof._ The U-statistics \(U_{n,m}^a,U_{n,s}^b\) are unbiased for \(\lambda_m^a,\lambda_s^b\). Every term of \(D_{ms,n}^{ab}\) evaluates the first kernel on _I_ and the second kernel on _J_, where (_I,J_) is a disjoint pair of index sets. Since the pairs are independent, for each term<tbc>

\(\mathbb{E}(H_m^a(Z_I)H_s^b(Z_J))=\mathbb{E}(H_m^a(Z_I))\mathbb{E}(H_s^b(Z_J))=\lambda_m^a\lambda_s^b.\)

<tbc>The denominator in (4.12) is the number \(\genfrac(){pt}{2}{n}{m}\genfrac(){pt}{2}{n-m}{s}\) of such disjoint pairs, hence \(\mathbb{E}(D_{ms,n}^{ab})=\lambda_m^a\lambda_s^b\). Finally

\(\mathbb{E}(\widehat{C}_{ms,n}^{ab})=\mathbb{E}(U_{n,m}^aU_{n,s}^b)-\lambda_m^a\lambda_s^b\)<br>
\(=\mathrm{Cov}(U_{n,m}^a,U_{n,s}^b).\)

Exchanging the roles of _I_ and _J_, together with the two statistics, shows that \(\widehat{C}_{sm,n}^{ba}=\widehat{C}_{ms,n}^{ab}\), so the assembled matrix is symmetric.

Unbiasedness holds entry by entry and on average over repeated samples, so the matrix computed from the observed sample need not be PSD. PSD and positive-definite corrections are given in Section 5.2.

**Corollary 4.9** (First-order consistency)**.** _Assume_ \(\mathbb{E}(X^2+Y^2)<\infty\)_, and let_ \(\widehat{C}_n\) _be the full unbiased covariance estimator of_ \(\widehat{T}_n\) _assembled from_ (4.13)_, for_ \(n\ge 6\)_. Then_<tbc>

\(n\widehat{C}_n-\rightarrow^{\mathrm{a}.\mathrm{s}.}\Omega,n\widehat{C}_n-\widehat{\Omega}_n-\rightarrow^p0.\) (4.14)

