<tbc>longer even be formed \[WGY10, OCPB16\]. Boolean moment relaxations sit squarely in that regime, with a moderate PSD block (the moment matrix of size 7,261 above) and equality constraints quadratic in its size (the 17.9 million above). A splitting iteration needs only one eigendecomposition of the moment matrix, plus an affine projection through a factorization computed once; its local convergence rate is therefore the relevant measure of hardness.

## Exact but degenerate.

Can a splitting method--ADMM \[GM76\], its symmetric Gauss-Seidel variant sGS-ADMM \[CST17\], or PDHG \[CP11\]--converge locally linearly on the exact relaxation? These methods are sublinear in the worst case \[DY17, ZAdK24\], and locally linear under regularity conditions at the limit point they select \[HSZ18, KJY25, Jia26, DLY26, LHL<sup>+</sup>26\]. Unfortunately, exact Boolean relaxations sit in a known harder class: _degenerate_ SDPs. Suppose _f_ has a unique Boolean minimizer _x<sub>⋆</sub>_ and order _d_ is uniquely rank-one exact, so the moment optimum is the single rank-one matrix \(X_\star=b_d(x_\star)b_d(x_\star)^\top\). Then, this optimum is primal degenerate whenever \(d\ge 2\), in the standard SDP sense \[AHO97\] (§2). Moreover, once one SOS certificate is strictly complementary--the generic case (§6)--the optimal Gram matrices form a positive-dimensional compact convex set S_<sub>⋆</sub>_ whose relative boundary consists of certificates that lose rank. A first-order method is free to converge to such a singular boundary certificate, where the pointwise regularity toolbox breaks down and no local linear rate can be concluded.

## Two unusual observations.

Practice, however, does not match this pessimism, and Figure 1 shows the phenomenon that motivates this paper. On the second-order moment relaxation of a BQP instance with _n_=20, exact ADMM started cold converges to a KKT point whose certificate is _not_ strictly complementary, yet the fixed-point residual still enters a sharp linear phase (Figure 1(a)). This behavior was recorded as an open question in \[KJY25\]. Nor is it an accident of one trajectory. On a second quotient instance, one hundred runs initialized near sampled _singular_ optimal fixed points (Figure 1(b)) all converge locally linearly (Figure 1(c)). A dual Riemannian method reports similar behavior on BQP relaxations \[WHX25\], and the effect persists for higher-degree objectives (Appendix H). For general degenerate SDPs, by contrast, the pessimism is justified by explicit examples that lose local linear convergence altogether \[Jia26, CST16, KY26b, KY26a\]. Exact Boolean relaxations thus appear to carry a hidden benign structure, which this paper identifies and proves.

101
Zk1 F
10-4
10-9
0
2000
4000
iteration k

55
number of samples
30
25
13
1
1
0
68
69
70
71
72
rank(Zi)

10-2
Zk1 F
10-5
10-8
0
2000
4000
iteration k

(a) cold start, non-SC limit

(b) ranks of the endpoints \(\bar{Z}_i\)

(c) 100 near-singular warm starts

Figure 1: Benign degeneracy on second-order moment relaxations of two BQP instances with _n_=20. (a) Exact ADMM (\(\sigma=100\), all-zeros start) on the standard relaxation (_N_=231) of the instance of \[KJY25\]: the limiting pair is _not_ strictly complementary, yet the residual enters a sharp linear phase once the primal rank is identified (dotted line). (b)-(c) One hundred runs on the quotient relaxation of §2 of a second instance (_N_=211), each started at a small random perturbation of a sampled singular optimal endpoint \(\bar{Z}_i\) (Appendix H): the endpoints are singular and mutually distinct (b), and every run converges locally linearly (c).

