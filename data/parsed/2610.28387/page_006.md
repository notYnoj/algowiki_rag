<tbc>Yitzhaki and Schechtman, 2013; Carcea and Serfling, 2015). The third L-comoment is<tbc>

\(\lambda_3^{[XY]}=6\mathrm{Cov}\{X,W\},W=\{F_Y(Y)-1/2\}^2.\)

<tbc>It is a rank-based analogue of the coskewness \(\mathbb{E}\{(X-\mu_X)(Y-\mu_Y)^2\}\) (Rubinstein, 1973; Harvey and Siddique, 2000), obtained by replacing \(Y-\mu_Y\) with _F<sub>Y</sub>(Y_)-1/2 (Serfling and Xiao, 2007, Section 3.1.4). Since _F<sub>Y</sub>(Y_) is uniform on (0,1), E(_W_)=1/12, and therefore

\(\lambda_3^{[XY]}=6\{\mathbb{E}(XW)-\mathbb{E}(X)\mathbb{E}(W)\}=6\mathbb{E}\{X(W-1/12)\}.\)

The weight _W_-1/12 is positive when _F<sub>Y</sub>(Y)\<_0.21 or _F<sub>Y</sub>(Y)\>_0.79, that is, when _Y_ lies in one of its two tails. The weight is negative when _Y_ lies in the central part of its distribution. Hence \(\lambda_3^{[XY]}>0\) when _X_ is on average larger for values of _Y_ in its tails than for values of _Y_ near its median, and \(\lambda_3^{[XY]}<0\) in the opposite case. For example, \(\lambda_3^{[XY]}=0\) for the bivariate normal distribution, because E(_X|Y_) is linear in _Y_ and _W_ is symmetric about the median of _Y_ . This is why \(\lambda_3^{[XY]}\) plays the role of a coskewness: like \(\mathbb{E}\{(X-\mu_X)(Y-\mu_Y)^2\}\), it is positive when large values of _X_ occur with extreme values of _Y_ in either direction. Unlike the univariate L-skewness, the L-coskewness \(\lambda_3^{[XY]}\) is not unit-free: it has the units of _X_ and is invariant to monotone transformations of _Y_ . However, the ratio \(\tau_3^{[XY]}=\lambda_3^{[XY]}/\lambda_2(X)\) is unit-free, because its numerator and its denominator both have the units of _X_.

When _Y=X_, the L-comoments reduce to the univariate L-moments. The Gini covariance has been studied extensively as a single measure (Yitzhaki and Schechtman, 2013). In applications, however, L-comoments of several orders are used jointly, for example in multivariate regional frequency analysis (Chebana and Ouarda, 2007; Akinsoji et al., 2026) and copula estimation (Brahimi et al., 2015). Such joint use requires the joint sampling covariance of the estimated L-comoments, which is the subject of this paper.

## 2.3 Estimation of L-comoments

To estimate \(\lambda_m^{[XY]}\) from a sample, we follow the approach of Hosking (1990) for univariate L-moments. Each univariate L-moment is the expectation of a simple function of a conceptual sample of size _m_. For example, \(\lambda_2(X)=\frac{1}{2}\mathbb{E}(X_{2:2}-X_{1:2})\). For two observations _x<sub>i</sub>_ and _x<sub>j</sub>_, the corresponding function is \(\frac{1}{2}(x_{2:2}-x_{1:2})=\frac{1}{2}|x_i-x_j|\). Averaging it over all pairs of observations gives the unbiased estimator

\(\widehat{\lambda}_2(X)=\genfrac(){pt}{2}{n}{2}^{-1}\sum_{i<j}\frac{1}{2}|x_i-x_j|.\)

Higher-order sample L-moments are obtained in the same way from subsamples of size _m_ (Hosking, 1990).

L-comoments are estimated by the same principle. The function that is averaged over subsamples is called a kernel. Write _z<sub>i</sub>_=(_x<sub>i</sub>,y<sub>i</sub>_) for an observed pair. A kernel of order _m_<tbc>

