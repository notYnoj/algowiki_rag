_d_ can be expressed as a set of 3 constraints \(r_\eta(x,y)\le d\), \(s_{\epsilon,\theta}(x,y)\le d\) and \(t_{\epsilon,\zeta}(x,y))\le d\). From Proposition 3.3 and Remark 3.1, the last two constraints can be formulated as second-order cone constraints, and the first one is linear.

## 3.5 Relaxation of the DCMCF problem

Constraints (11) provide a reformulation of the delay constraints (3) of the DCMCF problem based on the function _f_. From this reformulation and the convex envelope of the function _f_, the delay constraints of the DCMCF problem can be relaxed as:

\(\sum_{a\in p}\check{f}_\mathcal{X}(\frac{b^k}{c_a}x_p^k,\frac{y_a}{c_a})\le d^kb^kx_p^k\forall k\in K,p\in P^k\) (16)

where _u<sub>a</sub>_ (resp. \(u_p^k\)) is an upper bound of _y<sub>a</sub>_ (resp. \(x_p^k\)), and _l<sub>a</sub>_ is (resp. \(l_{a,p}^k\)) a lower bound on _y<sub>a</sub>_ (resp. \(y_a-b^kx_p^k\)). Details about the computation of these parameters are deferred to Section 3.6.

Using the analytical expression of \(\check{f}\), and adding a variable \(d_a^{pk}\) to express the term \(\frac{1}{b^ku_p^k}\check{f}_\mathcal{X}(\frac{b^k}{c_a}x_p^k,\frac{y_a}{c_a})\), we get the following relaxation of DCMCF:

