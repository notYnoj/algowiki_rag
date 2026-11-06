<tbc>error bound from Section 4 (represented by a solid line). For reference, the accuracy of the classical _O(n_<sup>3</sup>) algorithm is shown with a dotted gray line. We see here that our main stability bound is descriptive and, moreover, that it accurately ranks the three algorithms in terms of expected accuracy.

An alternative version of these plots is presented in Figure 4, where each panel now corresponds to a different algorithm and the plotted curves correspond to different choices of _A_ and _B_. In addition to the random input matrices discussed above, these plots include results for a "worse-case" option.<sup>12</sup> Corresponding "worse-case" inputs are algorithm dependent, constructed to maximize the error given a set of encoding matrices. To do this, we first construct (nonzero) inputs _A_ and _B_ with entries in {0,-1,1} chosen to maximize

\(max_r\sum_k\sum_s\big|W_{rs}(\varepsilon_k)\big|\big|a^TU_s(\varepsilon_k)\big|\big|b^TV_s(\varepsilon_k)\big|,\) (5.1)

where _U<sub>s</sub>_ and _V<sub>s</sub>_ are the _s_-th columns of the encoding matrices _U_ and _V_ (which describe the base-case algorithm) and _a_ and _b_ are vectorized copies of _A_ and _B_. Since the base case here is only \(\langle 3,3,3\rangle\), these matrices can be found via an exhaustive search. We then take Kronecker powers of _A_ and _B_ to obtain "worse- case" inputs of arbitrary size. Recalling (1.7), the idea here is to encourage each intermediate product _C<sub>j</sub>_<tbc>

<sup>12</sup>We use the term "worse-case" instead of "worst-case" since we make no claim that these inputs are actually the most difficult for our algorithms.

Floating-point error vs the theoretical bound, by input distribution
Unif(-1, 1)
Unif(0, 1)
100
100
10-10
10-10
Error
Error
10-20
10-20
1
2
3
4
5
1
2
3
4
5
Recursion level L (matrix size n = 3L)
Recursion level L (matrix size n = 3L)
N(0, 1)
100
Smirnov (3,3,3;20)
Schönhage (3,3,3;21)
Our (3,3,3;21)
10-10
Smirnov bound
10-10
Schönhage bound
Error
Our (3,3,3;21) bound classical O(n3) product
10-20
1
2
3
4
5
Recursion level L (matrix size n = 3L)

Figure 3: Measured and theoretical accuracy of three APA algorithms for \(\langle 3,3,3\rangle\) matrix multiplication applied to various input matrices, as measured by the normalized error \(\|\widehat{C}-C\|/(\|A\|\|B\|)\) and compared to the bounds from Theorem 4.7. The panels share a vertical scale, and the solid curves are identical in all three.

