Because edges are sampled i.i.d. from the Bernoulli Ber(_p<sub>t</sub>_) distribution at each step _t_, the symmetry implies that the subsample of edges is a uniform sample of _k_ edges. Using Lemma 5.4, each sample _G(p<sub>t</sub>_) takes \(p_t\cdot\widetilde{O}(m)+\widetilde{O}(n)\) queries and \(\widetilde{O}(n^2)\) time in expectation. Summing this over \(0\le t\le r\) gives an upper bound of \(2p_r\cdot\widetilde{O}(m)+\widetilde{O}(nr)\) queries and \(\widetilde{O}(n^2r)\) time. Using the fact that the probability that _G(p_) has less than _k_ edges for _p_=2_k/m_, is at most _e_<sup>-_k/_4</sup>, we can conclude that \(p_r\le 4k/m\) with probability at least 1-_e_<sup>-_k/_4</sup>. So the expected number of queries is upper bounded by \(\widetilde{O}(nr+k)=\widetilde{O}(n+k)\) and the running time by \(\widetilde{O}(n^2r)=\widetilde{O}(n^2)\) using the fact that \(r\le O(logn)\).

Using Lemma 5.5 with \(k=\widetilde{O}(n/\varepsilon^2)\), we can obtain a random subgraph _H_ of the unknown graph _G_ to get such a sample of edges using \(\widetilde{O}(n/\varepsilon^2)\) queries, and hence apply existing approximations for all heavy subgraph problems.

The results in this section do not generalize to the weighted case when the edges of the graph have unknown non-negative weights. We address this issue by giving some preliminary results under additional structural assumptions and slightly stronger oracle models--see Section D.3--but the general question remains wide open.

See Section D.4 for some illustrative examples which show some separation between the capabilities of the cut comparison and cut value query oracles.

## Appendix

### A Omitted Content from Section 2

In this section, we give omitted proofs and other discussion from Section 2. In particular, we show that the "certification" problem, where we have to write the shortest certificate of some point _y_<sup>∗</sup> being the optimizer of \(\langle w^*,x\rangle\) over points \(x\in\mathcal{P}\), can be directly related to the conic dimension. We present this discussion since it helps motivate and demystify the definition further. We then give the proofs omitted from Section 2.

The notion of conic dimension is intimately related the notion of _inference dimension_ given in \[KLMZ17\]. They defined it as being the size of a largest "inference-independent" set where none of the inequalities are implied by the others. Our definition is very similar to theirs, with two minor differences: (a) we restrict to linear optimization, and (b) we consider sequences where each comparison is not implied by the previous ones. Since implications using linear inequalities has a natural geometric visualization as a cone, we call it _conic dimension_.

#### A.1 The Certification Problem

Before addressing the optimization problem, we ask whether it is even possible to certify optimality efficiently. Suppose we wish to prove that some point \(y\in\mathcal{P}\) is the optimal solution, i.e., \(y\in argmin_{x\in\mathcal{P}}\langle w^*,x\rangle\), or equivalently, that

\(\langle w^*,x-y\rangle\ge 0\forall x\in\mathcal{P}.\) (12)

We want to use as few comparisons as possible.

1. A _y-certificate_ is a collection C of index pairs (_i,j_) such that for all \(w\in\mathbb{R}^d\), we have that<tbc>

\((\langle w,x_i-x_j\rangle\ge 0\forall(i,j)\in\mathcal{C})\Rightarrow(\langle w,x-y\rangle\ge 0\forall x\in\mathcal{P})\) \(\text{(13)}\)

