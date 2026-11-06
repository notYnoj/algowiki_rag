symmetric. These matrices are the building blocks of Theorem 3.1: the blocks of \(\mathrm{Cov}(\widehat{\unknown})\) in (3.5) and (3.6) are linear combinations of them.

To combine these covariances, we count the pairs of subsets (_I,J_) by the number _c_ of shared pairs. Pairs with _c_=0 contribute nothing, and each pair with \(c\ge 1\) contributes \(\Gamma_{ms,c}^{ab}\). This gives the _overlap identity_ (see Hoeffding, 1948; Lee, 1990; Serfling, 1980, Chapter 5):

\(\mathrm{Cov}(\widehat{\lambda}_m^a,\widehat{\lambda}_s^b)=\sum_{c=1}^{\mathrm{min}(m,s)}\omega_{ms,c}(n)\Gamma_{ms,c}^{ab},\omega_{ms,c}(n)=\frac{\genfrac(){pt}{2}{m}{c}\genfrac(){pt}{2}{n-m}{s-c}}{\genfrac(){pt}{2}{n}{s}},\) (3.4)

where \(\omega_{ms,c}(n)\) is the proportion of subsets _J_ of size _s_ that share exactly _c_ pairs with a fixed subset _I_ of size _m_. The identity holds for kernels of any fixed order.

In this paper we apply the overlap identity (3.4) to the second and third sample L-comoments, that is, to the U-statistics with the order-two kernels \(H_2^a\) in (2.5) and the order-three kernels \(H_3^a\) in (2.6). The second L-comoment \(\lambda_2^{[XY]}\) is twice the Gini covariance of _X_ with respect to _Y_ . The third L-comoment \(\lambda_3^{[XY]}\) measures whether _X_ is larger when _Y_ lies in its tails than when _Y_ lies near its median (Section 2). For these two orders, Theorem 3.1 below gives every entry

\(\mathrm{Cov}(\widehat{\lambda}_m^a,\widehat{\lambda}_s^b),m,s\in\{2,3\},a,b\in\{[XY],[YX]\},\)

of \(\mathrm{Cov}(\widehat{\unknown})\) explicitly. These entries include covariances between the two directions, such as \(\mathrm{Cov}(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_2^{[YX]})\), and covariances between orders, such as \(\mathrm{Cov}(\widehat{\lambda}_2^{[XY]},\widehat{\lambda}_3^{[XY]})\).

We now state the main result of this section. It expresses the exact covariance matrix of \(\widehat{\unknown}\) for every \(n\ge 3\) in terms of the \(2\times 2\) matrices \(\unknown_{ms,c}\).

**Theorem 3.1** (Explicit joint covariance for orders two and three)**.** _For every_ \(n\ge 3\)_, the covariance of_ \(\widehat{\unknown}\) _is exactly_<tbc>

\(\mathrm{Cov}(\widehat{\unknown})=\left(\begin{array}{ c c }
\unknown_{22,n} & \unknown_{23,n} \\
\unknown_{23,n}^\mathsf{T} & \unknown_{33,n}
\end{array}\right),\) (3.5)

<tbc>_where_

\(\unknown_{22,n}=\frac{4(n-2)}{n(n-1)}\unknown_{22,1}+\frac{2}{n(n-1)}\unknown_{22,2},\) (3.6)

\(\unknown_{23,n}=\frac{6(n-3)}{n(n-1)}\unknown_{23,1}+\frac{6}{n(n-1)}\unknown_{23,2},\)<br>
\(\unknown_{33,n}=\frac{9(n-3)(n-4)}{n(n-1)(n-2)}\unknown_{33,1}+\frac{18(n-3)}{n(n-1)(n-2)}\unknown_{33,2}+\frac{6}{n(n-1)(n-2)}\unknown_{33,3}.\)

_Proof._ The identity (3.4) is standard (see (A.1) in Appendix A), so only the coefficients \(\omega_{ms,c}(n)\) need to be computed to complete the blocks (3.6) of the covariance matrix (3.5). For (_m,s_)=(2,2), the overlap counts are 2(_n_-2) and 1, with denominator _n(n_-1)/2, yielding 4(_n_-2)/{_n(n_-1)} and 2/{_n(n_-1)}. For (_m,s_)=(2,3), the counts are \(2\genfrac(){pt}{2}{n-2}{2}=(n-2)(n-3)\) and _n_-2, with denominator \(\genfrac(){pt}{2}{n}{3}=n(n-1)(n-2)/6\); these yield 6(_n_-3)/{_n(n_-1)} and<tbc>

