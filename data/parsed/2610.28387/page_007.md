takes _m_ distinct pairs _z_<sub>1</sub>_,...,z<sub>m</sub>_ and sorts them by their _y_ values. Let _x_<sub>\[1\]</sub>_,...,x_<sub>\[_m_\]</sub> be the corresponding _x_ values, that is, the concomitants within these _m_ pairs. The kernel combines these concomitants with the coefficients inside the expectations in (2.4). The order-two symmetric kernel is therefore<tbc>

\(H_2^{[XY]}(z_1,z_2)=\frac{x_{[2]}-x_{[1]}}{2}=\frac{(x_1-x_2)\mathrm{sgn}(y_1-y_2)}{2},\) (2.5)

<tbc>where sgn(_t_) equals 1, 0, or -1 according as _t\>_0, _t_=0, or _t\<_0, and the order-three symmetric kernel is

\(H_3^{[XY]}(z_1,z_2,z_3)=\frac{x_{[1]}-2x_{[2]}+x_{[3]}}{3}.\) (2.6)

The kernels \(H_m^{[YX]}\) are obtained by exchanging the roles of the _x_ and _y_ coordinates. The kernel \(H_2^{[XY]}\) lies between two familiar kernels: replacing sgn(_y_<sub>1</sub>-_y_<sub>2</sub>) by _y_<sub>1</sub>-_y_<sub>2</sub> in (2.5) gives the kernel (_x_<sub>1</sub>-_x_<sub>2</sub>)(_y_<sub>1</sub>-_y_<sub>2</sub>)/2 of the sample covariance, and replacing _x_<sub>1</sub>-_x_<sub>2</sub> by sgn(_x_<sub>1</sub>-_x_<sub>2</sub>) gives the kernel sgn(_x_<sub>1</sub>-_x_<sub>2</sub>)sgn(_y_<sub>1</sub>-_y_<sub>2</sub>) of Kendall’s tau. All these kernels are symmetric, that is, invariant under permutations of their arguments, because the pairs are first sorted by one coordinate. Symmetric kernels of this kind are standard in U-statistic theory (Hoeffding, 1948; Serfling, 1980; Lee, 1990), which is the main tool of this paper; the facts used repeatedly are collected in Appendix A.

We now construct estimators of the L-comoments from the sample. Since the two directions are estimated from the same pairs, we treat them jointly in vector form. Write

\(\unknown_m=(\lambda_m^{[XY]},\lambda_m^{[YX]})^\mathsf{T},H_m=(H_m^{[XY]},H_m^{[YX]})^\mathsf{T}.\)

For an index set \(I=\{i_1,\dots,i_m\}\subset\{1,\dots,n\}\), write _Z<sub>I</sub>_=(_Z_<sub>_i_<sub>1</sub></sub>_,...,Z<sub>i<sub>m</sub></sub>_), so that **_H_**_<sub>m</sub>(Z<sub>I</sub>_)=**_H_**_<sub>m</sub>(Z_<sub>_i_<sub>1</sub></sub>_,...,Z<sub>i<sub>m</sub></sub>_); by symmetry, the order of the indices does not matter.

For _m_=2,3 and \(a\in\{[XY],[YX]\}\), the kernel \(H_m^a\) evaluated at any _m_ distinct pairs has mean \(\lambda_m^a\); that is,<tbc>

\(\mathbb{E}\{H_m(Z_I)\}=\unknown_m.\)

<tbc>This follows from (2.4), and a proof is given in Appendix B.1. We therefore estimate \(\unknown_m\) by the complete U-statistic

\(\widehat{\unknown}_m=\genfrac(){pt}{2}{n}{m}^{-1}\sum_{I\subset\{1,\dots,n\},|I|=m}H_m(Z_I),m=2,3,\) (2.7)

which averages the kernel over all \(\genfrac(){pt}{2}{n}{m}\) subsets of size _m_. This estimator is unbiased for \(\unknown_m\). Each kernel is a linear combination of _x_ values or of _y_ values, so it is square integrable when \(\mathbb{E}(X^2+Y^2)<\infty\). Serfling and Xiao (2007) also gave this U-statistic representation.

The sample means <o>_X_</o> and <o>_Y_</o> are U-statistics of order one with kernels \(H_1^{[XY]}(z)=x\) and \(H_1^{[YX]}(z)=y\); they are included in the covariance matrix of Section 4.

