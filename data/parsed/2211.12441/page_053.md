<tbc>extracted from \(\mathrm{MinInv}(T,\rho)\) with straightforward calculations. This completes the reduction.

### Approximation Algorithms.

If we relax our requirements to an approximate answer, we can approximate MinRInv in polynomial time using existing approximation algorithms for weighted minimum feedback arc set. The best known such algorithm achieves an approximation ratio of _O_(log_n_loglog_n_) on a graph with _n_ vertices \[ENSS98\]. Adapting this algorithm for minimizing inversions in trees produces an approximation factor of _O_(log(deg(_T_))loglog(deg(_T_))) for \(\mathrm{MinInv}(T,\rho)\). Under the unique games conjecture, there does not exist a constant-factor approximation algorithm for minimum feedback arc set on arbitrary digraphs \[GHM<sup>+</sup>11\].

In the special case of tournament graphs, which have exactly one edge of weight 1 between every pair of vertices, there are efficient constant factor approximation algorithms for minimum arc feedback set. Some of these also apply to weighted tournaments, where for every pair of vertices _v<sub>i</sub>,v<sub>j</sub>_, the nonnegative edge weights _w<sub>ij</sub>,w<sub>ji</sub>_ satisfy _w<sub>ij</sub>+w<sub>ji</sub>_=1. This case corresponds to the scenario of computing \(\mathrm{MinRInv}(T_v,\rho)\) where all leaf sets _L<sub>i</sub>_ of siblings have the same size. \[KS10\] gives an algorithm with runtime \(O^*(2^{O(\sqrt{\mathrm{OPT}})})\), given that the optimal answer is OPT. \[KMS07\] also gives an approximation algorithm in the case where \(w_{ij}+w_{ji}\in[b,1]\) for some _b\>_0: For any \(\epsilon>0\), the algorithm produces a \((1+\epsilon)\)-approximation of OPT in time \(n2^{\tilde{O}(1/(\epsilon b)^{12})}\). For the problem of computing \(\mathrm{MinRInv}(T_v,\rho)\), the parameter _b_ represents the ratio between the smallest and largest possible values of \(|L_i|\cdot|L_j|\).

### Wilcoxon test.

As a final remark we point out an alternate way of computing \(\Pi_T(\rho)\) in the special case of the Mann-Whitney trees of Figure 2. The number of cross inversions \(\mathrm{XInv}_\rho(A,B)\) can be written in terms of the rank sum \(W_B\doteq\sum_{y\in B}\rho(y)\) as follows, where \(a\doteq|A|\) and \(b\doteq|B|\):

\(\mathrm{XInv}_\rho(A,B)=ab+\frac{b(b+1)}{2}-W_B.\) (37)

The quantity _W<sub>B</sub>_ is known as the Wilcoxon rank-sum statistic for differences between random variables. Because of the relationship (37) the Wilcoxon test is equivalent in power to the Mann- Whitney test. However, the evaluation based on the efficient computation of cross inversions (especially in the case of unbalanced set sizes _a_ and _b_) is superior to the evaluation based on the rank sum _S<sub>B</sub>_, as the latter presumes sorting the combined set \(X=A\sqcup B\).

## Acknowledgements

We would like to thank Greta Panova, Robin Pemantle, and Richard Stanley for pointers regarding Gaussian polynomials, Stasys Jukna for answering questions about the complexity measure _N_, and the anonymous reviewers for helpful suggestions. We appreciate the partial support for this research by the U.S. National Science Foundation under Grants No. 2137424 and 2312540. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

A preliminary version of this paper appears in the Proceedings of the 2023 ACM-SIAM Symposium on Discrete Algorithms \[HvMM23\].

