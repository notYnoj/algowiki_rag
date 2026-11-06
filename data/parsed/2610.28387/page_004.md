## 2 Directional L-comoments and sample constructions

### 2.1 Definitions

Let _Z<sub>b</sub>_=(_X<sub>b</sub>,Y<sub>b</sub>_), _b_=1_,...,n_, be independent and identically distributed (iid) pairs from a continuous bivariate distribution. The two coordinates of each pair may be dependent. We refer to _X_ and _Y_ as the marginal variables, or simply the margins, and to _F<sub>X</sub>_ and _F<sub>Y</sub>_ as their marginal distribution functions. We write \(\mu_X=\mathbb{E}(X)\) and \(\mu_Y=\mathbb{E}(Y)\), and _Z_=(_X,Y_) denotes a generic pair with the same distribution as _Z<sub>b</sub>_. Assume \(\mathbb{E}(X^2+Y^2)<\infty\) whenever covariance is considered.

For _m_=2,3,4, the _m_th L-moment of _X_ (Hosking, 1990) can be written as

\(\lambda_m(X)=\mathbb{E}(XP_{m-1}\{F_X(X)\}),\) (2.1)

where _P_<sub>_m_-1</sub> is the shifted Legendre polynomial of degree _m_-1 on \[0,1\], given by

\(P_1(u)=2u-1,P_2(u)=6u^2-6u+1,P_3(u)=20u^3-30u^2+12u-1.\) (2.2)

Here \(\lambda_2(X)\) is the L-scale of _X_, \(\lambda_3(X)\) measures the skewness of _X_, and \(\lambda_4(X)\) measures the kurtosis of _X_. The ratios \(\lambda_3(X)/\lambda_2(X)\) and \(\lambda_4(X)/\lambda_2(X)\) are the L-skewness and the L-kurtosis of _X_ (Hosking, 1990).

Replacing _F<sub>X</sub>(X_) by _F<sub>Y</sub>(Y_) in (2.1) defines the L-comoments of Serfling and Xiao (2007), a bivariate extension of L-moments.

**Definition 2.1** (Directional L-comoments)**.** For _m_=2,3,4, the _m_th directional L-comoment of _X_ with respect to _Y_ and that of _Y_ with respect to _X_ are

\(\lambda_m^{[XY]}=\mathbb{E}(XP_{m-1}\{F_Y(Y)\}),\lambda_m^{[YX]}=\mathbb{E}(YP_{m-1}\{F_X(X)\}).\) (2.3)

In the \[_XY_\] direction, that is,

\(\lambda_2^{[XY]}=\mathbb{E}[X\{2F_Y(Y)-1\}],\)<br>
\(\lambda_3^{[XY]}=\mathbb{E}[X\{6F_Y(Y)^2-6F_Y(Y)+1\}],\)<br>
\(\lambda_4^{[XY]}=\mathbb{E}[X\{20F_Y(Y)^3-30F_Y(Y)^2+12F_Y(Y)-1\}],\)

and the \[_YX_\] direction is obtained by exchanging _X_ and _Y_ .

The two directional L-comoments \(\lambda_m^{[XY]}\) and \(\lambda_m^{[YX]}\) are not equal in general, which is why we call them "directional" (asymmetric in the terminology of Serfling and Xiao (2007)). Since only directional L-comoments are considered in this paper, we simply call them L-comoments from now on; the direction is indicated by the superscript \[_XY_\] or \[_YX_\].

