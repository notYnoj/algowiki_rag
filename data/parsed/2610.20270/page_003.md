## 1 Introduction

### Problem statement.

Consider the pseudo-Boolean optimization (PBO): given a real polynomial _f_ in _n_ variables, compute

\(\mathrm{OPT}(f):=\mathrm{min}_{x\in\{\pm 1\}^n}f(x).\) (1.1)

Since \(x_i^2=1\) on the cube, we always represent _f_ by its unique square-free (multilinear) polynomial. Problem (1.1) is a broad modeling language for discrete optimization \[BH02\]. Already at degree two it contains MAX-CUT, unconstrained binary quadratic optimization (QUBO) \[KHG<sup>+</sup>14\], and ground states of Ising spin glasses, which are NP-hard to compute \[Bar82\]; higher degrees cover Boolean constraint satisfaction. Semidefinite programming (SDP) relaxations have been central to this problem class since the Goemans-Williamson approximation algorithm for MAX-CUT \[GW95\].

### The Moment-SOS hierarchy.

The canonical family of semidefinite relaxations for (1.1) is the Moment-SOS hierarchy \[Las01, Par03, Lau03a\]. At order _d_, a true probability distribution on the cube is replaced by a degree-2_d_ pseudo-moment sequence, represented by a positive-semidefinite (PSD) moment matrix; the dual PSD variable is a sum-of-squares (SOS) Gram certificate. In the language of theoretical computer science, this is the degree-2_d_ pseudoexpectation / SOS proof-system view \[BS14, Moi20\]. The order-_d_ value _p<sub>d</sub>(f_) is defined at every _admissible_ order, \(2d\ge\mathrm{deg}f\), and satisfies

\(p_d(f)\le\mathrm{OPT}(f),p_{d_\mathrm{min}}(f)\le p_{d_\mathrm{min}+1}(f)\le\cdots,d_\mathrm{min}(f):=\mathrm{max}\{1,\lceil\mathrm{deg}f/2\rceil\},\) (1.2)

and the hierarchy is exact at order _n_ on the finite cube \[Lau03a\] (see also Theorem 6.1). We call the relaxation _exact_ at order _d_ if _p<sub>d</sub>(f_)=OPT(_f_), and _uniquely rank-one exact_ if in addition its moment SDP has the unique optimizer \(b_d(x_\star)b_d(x_\star)^\top\), where _x<sub>⋆</sub>_ is the Boolean minimizer and _b<sub>d</sub>_ is the monomial vector, as elaborated in §2.

### Worst-case looseness versus empirical low-order exactness.

How large must _d_ be? Worst- case theory is discouraging: the cut polytope of the complete graph needs relaxation order \(\lceil n/2\rceil\) \[Lau03b\], knapsack-type instances carry \(\Omega(n)\) SOS-degree lower bounds \[Gri01\], and random _k_-CSPs keep large gaps even at order \(\Omega(n)\) \[Sch08\]. Computational practice tells a different story. On unconstrained binary quadratic optimization, order two often delivers the exact solution or a very good approximation \[HKS25\]. BQP relaxations are a standard testbed for scalable low-rank solvers \[YLCT23, HTT26, HTT25, WHX25\]. The second-order Boolean relaxation, reported empirically exact on random QUBO, has been solved at _n_=120 variables, a moment matrix of size 7,261 with about 17.9 million equality constraints \[WH25\], and certifiably exact low-order relaxations are routine in robotics and perception \[RCBL19, BKGJ18, YC22, KXS<sup>+</sup>24\]. Most hierarchy theory asks how large _d_ must be before exactness. The empirical picture motivates a complementary question:

_Once a low-order Moment-SOS relaxation is exact,_<br>
_how hard is the resulting semidefinite program to solve?_

### Why first-order methods.

For SDPs of small and medium size, interior-point methods are the solver of choice. They need few iterations \[DK02\] and reach high accuracy. Under strict complementarity they even converge locally superlinearly \[AHO98, LSZ98\]. But each conventional interior-point iteration forms and factors a dense matrix whose dimension is the number of equality constraints. First-order splitting methods target the large-scale regime where this matrix can no<tbc>

