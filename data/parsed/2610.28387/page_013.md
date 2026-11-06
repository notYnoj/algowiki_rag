et al., 2004); see Langel and Tillé (2013) for a survey of variance estimation for the Gini index. For the Gini covariance and the Gini correlation, Schechtman and Yitzhaki (1987) gave the U-statistic estimator, its asymptotic normality, and a consistent estimator of the asymptotic variance. Later work has used asymptotic variances or jackknife variance estimates (Yitzhaki and Schechtman, 2013; Kattumannil et al., 2022), and tests based on the difference between the two directional Gini coefficients have used bootstrap approximations (Shelef and Schechtman, 2019). The exact variance of a single estimator has the general form given by Hoeffding (1948), and, under independence, the permutation variance of \(\widehat{G}^{[XY]}\) follows from the theory of generalized correlation coefficients (Daniels, 1944; Kendall and Gibbons, 1990). What we add is an explicit form of the exact joint covariance (3.12) of the two directional estimators for an arbitrary bivariate distribution, together with an unbiased estimator of it; we have not found these results in the literature.

## 3.2 Exact covariance when _X_ and _Y_ are independent

Independence of _X_ and _Y_ is the natural null hypothesis when the L-comoments are used to test for dependence, for example in a test of \(\lambda_2^{[XY]}=\lambda_2^{[YX]}=0\). Under independence, the matrices \(\unknown_{ms,c}\) simplify, and Theorem 3.1 yields a closed form that depends only on the marginal variances and the marginal L-moments. This closed form also provides an exact reference for the numerical experiments in Section 6. Define \(\ell_m^X=\lambda_m(X)\), \(\ell_m^Y=\lambda_m(Y)\), and<tbc>

\(a_n=\frac{n+1}{3n(n-1)},b_n=\frac{(n+1)(n+2)}{5n(n-1)(n-2)}.\) (3.13)

<tbc>**Theorem 3.4** (Exact covariance matrix under independence)**.** _If X and Y are independent, written_ \(X\perp Y\)_, and both X and Y are continuous with finite second moments, then the covariance matrix in Theorem 3.1 equals_

\(\left(\begin{array}{ c c c c }
a_n\text{Var}(X) & \ell_2^X\ell_2^Y/(n-1) & 0 & \ell_3^X\ell_2^Y/(n-1) \\
\ell_2^X\ell_2^Y/(n-1) & a_n\text{Var}(Y) & \ell_2^X\ell_3^Y/(n-1) & 0 \\
0 & \ell_2^X\ell_3^Y/(n-1) & b_n\text{Var}(X) & \ell_3^X\ell_3^Y/(n-1) \\
\ell_3^X\ell_2^Y/(n-1) & 0 & \ell_3^X\ell_3^Y/(n-1) & b_n\text{Var}(Y)
\end{array}\right).\) (3.14)

_In particular, the estimators_ \(\widehat{\lambda}_2^{[XY]}\) _and_ \(\widehat{\lambda}_2^{[YX]}\) _of the two directions have the positive covariance_ \(\ell_2^X\ell_2^Y/(n-1)\)_, although X and Y are independent._

Under independence, the population L-comoments vanish: by (2.3),

\(\lambda_m^{[XY]}=\mathbb{E}(X)\mathbb{E}[P_{m-1}\{F_Y(Y)\}]=0,m\ge 2,\)

because _F<sub>Y</sub>(Y_) is uniform on (0,1) and \(\int_0^1P_{m-1}(u)du=0\). Their estimators, however, are computed from the same _n_ pairs: \(\widehat{\lambda}_2^{[XY]}\) weights the _X_ values by the ranks of the _Y_ values,<tbc>

