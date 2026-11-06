6/{_n(n_-1)}. For (_m,s_)=(3,3), the counts are \(3\genfrac(){pt}{2}{n-3}{2}\), 3(_n_-3), and 1, with denominator \(\genfrac(){pt}{2}{n}{3}\), giving exactly the three coefficients in (3.6). Symmetry of the resulting covariance gives the lower-left block as the transpose of the upper-right block.

Theorem 3.1 does not yet give the covariance in a form that can be evaluated. It expresses \(\mathrm{Cov}(\widehat{\unknown})\) through the matrices \(\unknown_{ms,c}\), and each entry of \(\unknown_{ms,c}\) is a covariance of conditional kernels. These conditional kernels are defined in (3.1) only as conditional expectations. To evaluate the covariance, they must be written as explicit functions of their arguments. For _c=m_ this is immediate, because \(M_{m,m}^a=H_m^a\). The remaining conditional kernels, _M_<sub>2,1</sub>, _M_<sub>3,2</sub>, and _M_<sub>3,1</sub>, are derived in Section 3.1. With them, every entry of \(\unknown_{ms,c}\) becomes the expectation of a known function of (_X,Y_), as illustrated by Corollary 3.2 and Theorem 3.4.

## 3.1 The conditional kernels needed in the covariance

We now give the conditional kernels _M_<sub>2,1</sub>, _M_<sub>3,2</sub>, and _M_<sub>3,1</sub> in closed form for the \[_XY_\] direction. Write \(\mu_X=\mathbb{E}(X)\), _u<sub>y</sub>=F<sub>Y</sub>(y_), and \(Q_X(y)=\mathbb{E}(X\mathbf{1}(Y\le y))\), where **1**(_A_) denotes the indicator of the event _A_. Then<tbc>

\(M_{2,1}^{[XY]}(x,y)=\frac{1}{2}\{x(2u_y-1)+\mu_X-2Q_X(y)\}.\) (3.7)

<tbc>For two fixed pairs with \(y_\ell<y_h\), let \(x_\ell\) and _x<sub>h</sub>_ be the concomitants of \(y_\ell\) and _y<sub>h</sub>_, respectively, and put \(u_\ell=F_Y(y_\ell),u_h=F_Y(y_h)\). Then<tbc>

\(M_{3,2}^{[XY]}(z_1,z_2)=\frac{1}{3}\{(1-3u_\ell)x_\ell+(3u_h-2)x_h+\mu_X-3[Q_X(y_h)-Q_X(y_\ell)]\}.\) (3.8)

<tbc>Finally let

\(R_X(y)=\mathbb{E}(XP'_2(F_Y(Y))\mathbf{1}(Y\ge y)),\) (3.9)

\(K_X=\mathbb{E}(XF_Y(Y)P'_2(F_Y(Y))).\)

Then

\(M_{3,1}^{[XY]}(x,y)=\frac{1}{3}\{xP_2(u_y)+2\lambda_3^{[XY]}+R_X(y)-K_X\}.\) (3.10)

For the reverse direction, exchange _X_ and _Y_ . All three expressions follow by conditioning on where the _y_ values of the remaining pairs fall relative to the given _y_ values; this determines the position of each pair in the ordering by _y_ and hence the coefficient of its _x_ value in the kernel. Detailed case-by-case derivations are given in Appendix B.

The simplest case is _m=s=c_=2, in which the conditional kernel is the kernel itself, \(M_{2,2}^a=H_2^a\). The following corollary shows that \(\unknown_{22,2}\) then reduces to elementary moments of (_X,Y_).

