# On the Optimal Bounds for Noisy Computing

Banghua Zhu, Ziao Wang, Nadim Ghaddar, Jiantao Jiao, Lele Wang

**Abstract**

We revisit the problem of computing with noisy information considered in Feige et al. (1994), which includes computing the OR function from noisy queries, and computing the MAX, SEARCH, and SORT functions from noisy pairwise comparisons. For _K_ given elements, the goal is to correctly recover the desired function with probability at least \(1-\delta\) when the outcome of each query is flipped with probability _p_. We consider both the adaptive sampling setting where each query can be adaptively designed based on past outcomes, and the non- adaptive sampling setting where the query cannot depend on past outcomes. The prior work provides tight bounds on the worst-case query complexity in terms of the dependence on _K_. However, the upper and lower bounds do not match in terms of the dependence on \(\delta\) and _p_. We improve the lower bounds for all the four functions under both adaptive and non-adaptive query models. Most of our lower bounds match the upper bounds up to constant factors when either _p_ or \(\delta\) is bounded away from 0, while the ratio between the best prior upper and lower bounds goes to infinity when \(p\rightarrow 0\) or \(p\rightarrow 1/2\). On the other hand, we also provide matching upper and lower bounds for the number of queries in expectation, improving both the upper and lower bounds for the variable-length query model.

### I. INTRODUCTION

The problem of computing with noisy information has been studied extensively since the seminal work (Feige et al., 1994), which considers four problems:

• Computing the OR function of _K_ bits from noisy observations of the bits;

• Finding the largest (or top-_N_) element among _K_ real-valued elements from noisy pairwise comparisons;

• Searching the rank of a new element in an ordered list of _K_ elements from noisy pairwise comparisons;

• Sorting _K_ elements from noisy pairwise comparisons.

Feige et al. (1994) is based on a simple noise model where each observation goes through a binary symmetric channel BSC(_p_), i.e. for each observation, with probability _p_ we see its flipped outcome, and with probability 1-_p_ we see its true value. They provide upper and lower bounds for the query complexity in terms of the total number of elements _K_, the noise probability _p_, and the desired confidence level \(\delta\) when adaptive querying is allowed. They establish the optimal query complexity in terms of dependence with respect to _K_. However, the exact sample/query complexity with respect to all parameters \(K,\delta\), and _p_ is still not fully understood. In this paper, we revisit the problem of computing under noisy observations in both the adaptive sampling and non-adaptive sampling settings. We aim to close the gap in the existing bounds and illustrate the difference in query complexity between adaptive sampling and non-adaptive sampling.

Taking the problem of computing the OR function of _K_ bits as an example, assume that there are _K_ bits \((X_1,\cdots,X_K)\in\{0,1\}^K\). The OR function is defined as

\(\text{OR}(X_1,\cdots,X_K)=\left\{\begin{array}{ c c }
1, & \text{if}\exists k\in[K],X_k=1 \\
0, & \text{otherwise.}
\end{array}\right.\) (1)

The question is simple when we can query each bit noiselessly. In this case, _K_ queries are both sufficient and necessary since it suffices to query each bit once. And thus there is no benefit in applying adaptive querying

Banghua Zhu is with the Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, Berkeley, CA 94720, USA (email: banghua@berkeley.edu). Ziao Wang is with the Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC V6T1Z4, Canada (email: ziaow@ece.ubc.ca). Nadim Ghaddar is with the Department of Electrical and Computer Engineering, University of California San Diego, La Jolla, CA 92093, USA, (email: nghaddar@ucsd.edu). Jiantao Jiao is with the Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, Berkeley, CA 94720, USA (email: jiantao@berkeley.edu). Lele Wang is with the Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC V6T1Z4, Canada (email: lelewang@ece.ubc.ca). A shorter version of this work is accepted at the 2023 IEEE International Symposium on Information Theory.

