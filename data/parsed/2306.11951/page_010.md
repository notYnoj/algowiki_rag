<tbc>_2)_ \(\Theta(\frac{K}{1-H(p)}+\frac{Klog(1/\delta)}{D_\text{KL}(p\|1-p)})\) _for computing_ MAX;<tbc>

_3)_ \(\Theta(\frac{log(K)}{1-H(p)}+\frac{log(1/\delta)}{D_\text{KL}(p\|1-p)})\) _for computing_ SEARCH;<tbc>

_4)_ \(\Theta(\frac{Klog(K)}{1-H(p)}+\frac{Klog(K/\delta)}{D_\text{KL}(p\|1-p)})\) _for computing_ SORT.

The proof is deferred to Appendix J. The matching upper bound for SEARCH is given in (Gu and Xu, 2023) in the regime when _p_ is some constant that is bounded away from 0 and 1/2, where they make it tight even for the dependency on the constant. Our results for the other three functions improve both existing upper and lower bounds, and provide tight query complexity with all parameters in the variable-length setting. (Wang et al., 2023) initiates the study for constant-wise matching bounds for SORT when \(\delta=\Omega(K^{-1})\), which is achieved by (Gu and Xu, 2023). Our bounds are tight up to constant for arbitrarily small \(\delta\).

**Algorithm 1** Variable-length tournament for computing OR with noise

1: **Input:** Target confidence level \(\delta\).

2: Set \(\mathcal{X}=(X_1,X_2,\cdots,X_K)\) as the list of all bits with unknown value.

3: **for** iteration \(i=1:\lceil log_2(K)\rceil\) **do**

4: **for** iteration \(j=1:\lceil|\mathcal{X}|/2\rceil\) **do**

5: Set _a_=1/2, \(\tilde{\delta}_i=\delta^{2(2i-1)}\).

6: **while** \(a\in(\tilde{\delta}_i,1-\tilde{\delta}_i)\) **do**

7: Query the (2_j_-1)-th element once.

8: If observe 1, update \(a=\frac{(1-p)a}{(1-p)a+p(1-a)}\). Otherwise update \(a=\frac{pa}{pa+(1-p)(1-a)}\).

9: If \(a\le\tilde{\delta}_i\), remove the (2_j_-1)-th element, otherwise remove the 2_j_-th element.

10: Break when X only has one element left.

11: Set _a_=1/2.

12: **while** \(a\in(\delta,1-\delta)\) **do**

13: Query the only left element in X element once.

14: If observe 1, update \(a=\frac{(1-p)a}{(1-p)a+p(1-a)}\). Otherwise update \(a=\frac{pa}{pa+(1-p)(1-a)}\).

15: If \(a\le\delta\), return 0, otherwise return 1.

We provide the upper bound algorithm for computing OR in Algorithm 1. For the upper bound, one major difference is that to compare two elements with error probability at most \(\delta\), one needs \(\mathcal{O}(log(1/\delta)/D_\text{KL}(p\|1-p)+1/(1-2p))\) queries in expectation, which can be achieved by keep comparing the two elements until the posterior distribution reaches the desired confidence level (see e.g. Lemma 13 of Gu and Xu (2023)). But the best known bound for fixed-length is \(\mathcal{O}(log(1/\delta)/(1-H(p))\) (Feige et al., 1994). This makes it simpler to achieve tight rate for variable length.

In Algorithm 1, we adapt the noisy comparison oracle in Gu and Xu (2023) to noisy query oracle on each element, and combine with the original fixed-length algorithm in Feige et al. (1994). In each round, the algorithm eliminates half of the elements in the current set by querying the elements with odd indices. If the (2_j_-1)-th element is determined to be 1, the 2_j_-th element will be removed without being queried. If the (2_j_-1)-th element is determined to be 0, it will be removed from the list. Thus after O(log(_K_)) rounds, we have only one element left in the set, and it suffices to query this element to determine the output of OR function.

## VII. CONCLUSIONS AND FUTURE WORK

For four noisy computing tasks -- the OR function from noisy queries, and the MAX, SEARCH, and SORT functions from noisy pairwise comparisons -- we tighten the lower bounds for fixed-length noisy computing and provide matching bounds for variable-length noisy computing. Making the bounds match exactly in the fixed-length setting remains an important open problem.

## ACKNOWLEDGEMENTS

The authors would like to thank Yanjun Han for insightful discussions on the information-theoretic lower bounds. This work was supported in part by the NSERC Discovery Grant No. RGPIN-2019-05448, the NSERC Collaborative Research and Development Grant CRDPJ 54367619, NSF Grants IIS-1901252 and CCF-1909499.

