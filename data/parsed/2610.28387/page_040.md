The diagonal terms contribute \(n(\ell_s^X/n)(\ell_m^Y/n)=\ell_s^X\ell_m^Y/n\), and the _n(n_-1) off-diagonal terms contribute \(\ell_s^X\ell_m^Y/\{n(n-1)\}\). Their sum is

\(\frac{\ell_s^X\ell_m^Y}{n}+\frac{\ell_s^X\ell_m^Y}{n(n-1)}=\frac{\ell_s^X\ell_m^Y}{n-1}.\)

Together with the within-direction sums this proves Theorem 3.4, including the otherwise easily overlooked nonzero cross-direction covariances.

## C Rank-prefix computation of the exact unbiased covariance

Here we justify the complexity assertion of Proposition 5.1. The combinatorial argument uses fixed-order U-statistic incidence counting (Serfling, 1980); the range-sum implementation uses two-dimensional prefix tables (Crow, 1984). Write the _p_ kernels in one vector, with orders \(m_a\in\{1,2,3\}\). For \(|K|=c\le m_a\) define the uncentered incidence sums

\(\mathcal{I}_{a,K}=\sum_{I\supseteq K|I|=m_a}H_{m_a}^a(Z_I),N_a=\genfrac(){pt}{2}{n}{m_a},U_a=\mathcal{I}_{a,\emptyset}/N_a.\) (C.1)

Then \(A_{m_a,K}^a=\mathcal{I}_{a,K}-\genfrac(){pt}{2}{n-c}{m_a-c}U_a\). Consequently, only singleton, pair, and triple incidence products are required in (5.2). The order-one and order-two incidence sums are immediate after _O(n_<sup>2</sup>) pairwise evaluations.

For the order-three kernels, fix a pair _i\<j_, and denote its ordered _Y_ -ranks by \(\ell_Y<h_Y\). The third observation _k_ belongs to one of the three open _Y_ -rank intervals \([1,\ell_Y-1]\), \([\ell_Y+1,h_Y-1]\), or \[_h<sub>Y</sub>_+1_,n_\]. Within each interval the forward kernel is an affine function

\(H_3^{[XY]}(Z_i,Z_j,Z_k)=(aX_k+b)/3,a\in\{1,-2,1\},\)

where _b_ depends only on the fixed pair and on its rank interval. One-dimensional cumulative counts and sums of _X_ in increasing _Y_ -rank order therefore evaluate the forward component of _F<sub>ij</sub>_ in constant time for each pair.

The reverse component follows analogously from cumulative counts and sums of _Y_ in _X_-rank order. The endpoints are _excluded_: neither _k=i_ nor _k=j_ has a rank in any of the three open intervals for the relevant ranking coordinate. Thus no separate endpoint subtraction is required.

For cross-direction products, partition the third observation by both its _X_- and _Y_ -rank intervals, giving nine open rank rectangles. In each rectangle the two kernels have the forms (_aX<sub>k</sub>+b)/_3 and (_cY<sub>k</sub>+d)/_3. Their product is<tbc>

\(\frac{acX_kY_k+adX_k+bcY_k+bd}{9},\)

