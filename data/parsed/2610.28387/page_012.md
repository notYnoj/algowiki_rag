**Corollary 3.2** (Explicit order-two overlap matrix)**.** _Let Z_=(_X,Y_) _and_ \(Z'=(X',Y')\) _be independent copies of the bivariate random vector. Then_

\(\unknown_{22,2}=\left(\begin{array}{ c c }
\frac{1}{2}\mathrm{Var}(X)-(\lambda_2^{[XY]})^2 & \frac{1}{4}\mathbb{E}(|X-X'||Y-Y'|)-\lambda_2^{[XY]}\lambda_2^{[YX]} \\
\frac{1}{4}\mathbb{E}(|X-X'||Y-Y'|)-\lambda_2^{[XY]}\lambda_2^{[YX]} & \frac{1}{2}\mathrm{Var}(Y)-(\lambda_2^{[YX]})^2
\end{array}\right).\) (3.11)

_Proof._ By (3.3) with \(M_{2,2}^a=H_2^a\), the entries of \(\unknown_{22,2}\) are \(\Gamma_{22,2}^{ab}=\mathbb{E}\{H_2^a(Z,Z')H_2^b(Z,Z')\}-\lambda_2^a\lambda_2^b\). Since _Y_ has a continuous distribution, \(\mathrm{Pr}(Y=Y')=0\), so \(\{\mathrm{sgn}(Y-Y')\}^2=1\) with probability one. Hence \(\{H_2^{[XY]}(Z,Z')\}^2=(X-X')^2/4\) with probability one. Because \(\mathbb{E}\{(X-X')^2\}=2\mathrm{Var}(X)\), the expectation of \(\{H_2^{[XY]}(Z,Z')\}^2\) is Var(_X)/_2. Subtracting \((\lambda_2^{[XY]})^2\) gives the upper-left entry of (3.11); exchanging _X_ and _Y_ gives the lower-right entry. For the off-diagonal entries,

\(H_2^{[XY]}(Z,Z')H_2^{[YX]}(Z,Z')=\frac{1}{4}(X-X')\mathrm{sgn}(X-X')(Y-Y')\mathrm{sgn}(Y-Y')\)<br>
\(=\frac{1}{4}|X-X'||Y-Y'|.\)

Taking expectations and subtracting \(\lambda_2^{[XY]}\lambda_2^{[YX]}\) gives the upper-right entry \(\Gamma_{22,2}^{[XY][YX]}\). The lower-left entry \(\Gamma_{22,2}^{[YX][XY]}\) is the same, because the product is symmetric in the two directions.

_Remark_ 3.3 (Gini covariances). Since \(\lambda_2^{[XY]}=2\mathrm{Cov}\{X,F_Y(Y)\}\), the estimator \(\widehat{G}^{[XY]}=\widehat{\lambda}_2^{[XY]}/2\) is the U-statistic estimator of the Gini covariance _G_<sup>[_XY_]</sup>=Cov{_X,F<sub>Y</sub>(Y_)} of _X_ with respect to _Y_ (Schechtman and Yitzhaki, 1987); \(\widehat{G}^{[YX]}\) and _G_<sup>[_YX_]</sup> are defined by exchanging _X_ and _Y_ . Dividing \(\unknown_{22,n}\) in Theorem 3.1 by four and using Corollary 3.2, we obtain, for \(a,b\in\{[XY],[YX]\}\) and the conditional kernels \(M_{2,1}^a\) in (3.7),

\(\mathrm{Cov}(\widehat{G}^a,\widehat{G}^b)=\frac{n-2}{n(n-1)}\mathrm{Cov}\{M_{2,1}^a(Z),M_{2,1}^b(Z)\}+\frac{1}{2n(n-1)}\Gamma_{22,2}^{ab}.\) (3.12)

In particular,

\(\mathrm{Var}(\widehat{G}^{[XY]})=\frac{n-2}{n(n-1)}\mathrm{Var}\{M_{2,1}^{[XY]}(Z)\}+\frac{1}{2n(n-1)}\big\{\frac{1}{2}\mathrm{Var}(X)-4(G^{[XY]})^2\big\},\)<br>
\(\mathrm{Cov}(\widehat{G}^{[XY]},\widehat{G}^{[YX]})=\frac{n-2}{n(n-1)}\mathrm{Cov}\{M_{2,1}^{[XY]}(Z),M_{2,1}^{[YX]}(Z)\}\)<br>
\(+\frac{1}{2n(n-1)}\big\{\frac{1}{4}\mathbb{E}(|X-X'||Y-Y'|)-4G^{[XY]}G^{[YX]}\big\}.\)

When _X_ and _Y_ are independent, Theorem 3.4 below gives \(\mathrm{Var}(\widehat{G}^{[XY]})=(n+1)\mathrm{Var}(X)/\{12n(n-1)\}\) and \(\mathrm{Cov}(\widehat{G}^{[XY]},\widehat{G}^{[YX]})=\lambda_2(X)\lambda_2(Y)/\{4(n-1)\}\). An unbiased estimator of (3.12) is obtained by dividing the corresponding \(2\times 2\) block of the unbiased estimator in Theorem 4.8 by four.

For the univariate Gini mean difference, which corresponds to _Y=X_, the exact variance and an unbiased estimator of it are classical (Nair, 1936; Lomnicki, 1952; Glasser, 1962; Zenga<tbc>

