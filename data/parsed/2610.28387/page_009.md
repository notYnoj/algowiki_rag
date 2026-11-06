## Overlap identity.

Since sample L-comoments are U-statistics, their covariances follow from a standard identity of U-statistic theory. The idea is as follows. Each sample L-comoment is an average of kernel values over subsets of the pairs. Consider one kernel value of \(\widehat{\lambda}_m^a\), computed from a subset _I_ of _m_ pairs, and one kernel value of \(\widehat{\lambda}_s^b\), computed from a subset _J_ of _s_ pairs. If _I_ and _J_ have no pair in common, the two kernel values are independent, because the pairs are independent; hence their covariance is zero. If _I_ and _J_ share \(c\ge 1\) pairs, the two kernel values are dependent only through these _c_ shared pairs. Given the shared pairs, the two kernel values are independent, so their covariance is the covariance of their conditional means given the shared pairs.

We therefore define the conditional mean of a kernel given _c_ of its pairs, which we call a conditional kernel. For \(a\in\{[XY],[YX]\}\) and \(1\le c\le m\), let

\(M_{m,c}^a(z_1,\dots,z_c)=\mathbb{E}(H_m^a(Z_1,\dots,Z_m)|Z_1=z_1,\dots,Z_c=z_c),\) (3.1)

which averages the kernel over the remaining _m-c_ pairs. In particular, \(M_{m,m}^a=H_m^a\). By the law of iterated expectations and \(\mathbb{E}\{H_m^a(Z_1,\dots,Z_m)\}=\lambda_m^a\) (Section 2),<tbc>

\(\mathbb{E}\{M_{m,c}^a(Z_1,\dots,Z_c)\}=\lambda_m^a.\)

<tbc>The case _c_=1 plays a special role. The function \(M_{m,1}^a(z)\) is the mean of the kernel when one of its _m_ pairs is fixed at _z_, and it is called the _first projection_ of the kernel \(H_m^a\) (Hoeffding, 1948; Serfling, 1980). The name comes from the fact that

\(\frac{m}{n}\sum_{i=1}^n\{M_{m,1}^a(Z_i)-\lambda_m^a\}\) (3.2)

is the projection of \(\widehat{\lambda}_m^a-\lambda_m^a\) onto sums of the form \(\sum_{i=1}^ng(Z_i)\), that is, the sum of functions of single observations that is closest to \(\widehat{\lambda}_m^a-\lambda_m^a\) in mean square. This sum determines the leading term of the covariance of \(\widehat{\lambda}_m^a\) (Section 4). Let each of _a_ and _b_ denote one of the two directions, \[_XY_\] or \[_YX_\], and let each of _m_ and _s_ denote one of the orders, 2 or 3. For \(1\le c\le min(m,s)\), define

\(\Gamma_{ms,c}^{ab}=Cov\{M_{m,c}^a(Z_1,\dots,Z_c),M_{s,c}^b(Z_1,\dots,Z_c)\}=\mathbb{E}(M_{m,c}^aM_{s,c}^b)-\lambda_m^a\lambda_s^b.\) (3.3)

By the argument above, \(\Gamma_{ms,c}^{ab}\) is the covariance between a kernel value of \(\widehat{\lambda}_m^a\) and a kernel value of \(\widehat{\lambda}_s^b\) whose subsets share exactly _c_ pairs. For fixed _m_, _s_, and _c_, we collect the four values of \(\Gamma_{ms,c}^{ab}\) in the \(2\times 2\) matrix

\(\unknown_{ms,c}=\left(\begin{array}{ c c }
\Gamma_{ms,c}^{[XY][XY]} & \Gamma_{ms,c}^{[XY][YX]} \\
\Gamma_{ms,c}^{[YX][XY]} & \Gamma_{ms,c}^{[YX][YX]}
\end{array}\right).\)

Its rows correspond to the direction of the order-_m_ kernel, and its columns correspond to the direction of the order-_s_ kernel. The matrix \(\unknown_{mm,c}\) is symmetric, but \(\unknown_{23,c}\) need not be<tbc>

