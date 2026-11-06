\(\text{DCMCF}_\text{Big-M}:\mathrm{max}\gamma\)<br>
\((1),(2),(22),(24)\)<br>
\(x_p^k\le u_p^kz_p^k\forall k\in K,p\in P^k\) (26)

\(\sum_{a\in p}\frac{1}{c_a-y_a}\le d^kz_p^k+d_p^{kmax}(1-z_p^k)\forall p\in P^k\) (27)

\(z_p^k\in\{0,1\}\forall k\in K,p\in P^k.\) (28)

Note that the strength of the Big-M relaxation strongly depends on the tightness of the \(d_p^{kmax}\) bounds. However, the DCMF<sub>Big-M</sub> formulation enables a straightforward implementation of branch-and-bound approaches using commercial solvers. Tighter relaxations of the delay constraints such as the one proposed in Section 3.5 can also be included in the DCMF<sub>Big-M</sub> problem to provide a more efficient relaxation of DCMF.

## 4.2 A disjunctive-programming-based relaxation

We describe a relaxation proposed in [16] and we prove that DCMF<sub>env</sub> provides tighter bounds than the disjunctive-programming-based relaxation.

The delay constraint related to a path _p_ is relaxed as follows. The authors consider the convex envelope of \(\Gamma_0_p^k\cup\Gamma_1_p^k\) where

\(\Gamma_0_p^k=\left\{\left(z_p^k,(y_a)_{a\in p}\right):z_p^k=0,l_a\le y_a\le u_a,\forall a\in p\right\},\text{and}\)<br>
\(\Gamma_1_p^k=\left\{\left(z_p^k,(y_a)_{a\in p}\right):z_p^k=1,l_a\le y_a\le u_a,\forall a\in p,\sum_{a\in p}\frac{1}{c_a-y_a}\le d^k\right\}.\)

Then they derive the following relaxation of the DCMF problem:

\(\text{DCMCF}_\text{red}\mathrm{max}\gamma\)<br>
\((1),(2),(22),(24),(26),\)<br>
\(\sum_{a\in p}\frac{z_p^k^2}{c_az_p^k-y_{a_p^k}}\le z_p^kd^k\forall k\in K,p\in P^k\) (29)

\(y_a-(1-z_p^k)u_a\le y_{a_p^k}\le y_a\forall k\in K,p\in P^k,a\in p\) (30)

\(z_p^kl_a\le y_{a_p^k}\le z_p^ku_a\forall k\in K,p\in P^k,a\in p\) (31)

\(z_p^k\ge 0\forall k\in K,p\in P^k.\) (32)

