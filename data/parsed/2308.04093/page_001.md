# 0-1 Knapsack in Nearly Quadratic Time

**Abstract**

We study pseudo-polynomial time algorithms for the fundamental _0-1 Knapsack_ problem. Recent research interest has focused on its fine-grained complexity with respect to the number of items _n_ and the _maximum item weight w_<sub>max</sub>. Under (min,+)-convolution hypothesis, 0-1 Knapsack does not have \(O((n+w_\mathrm{max})^{2-\delta})\) time algorithms (Cygan-Mucha-Węgrzycki-Włodarczyk 2017 and Künnemann-Paturi-Schneider 2017). On the upper bound side, currently the fastest algorithm runs in \(\widetilde{O}(n+w_\mathrm{max}^{12/5})\) time (Chen, Lian, Mao, and Zhang 2023), improving the earlier \(O(n+w_\mathrm{max}^3)\)-time algorithm by Polak, Rohwedder, and Węgrzycki (2021).

In this paper, we close this gap between the upper bound and the conditional lower bound (up to subpolynomial factors):

\(\bullet\) The 0-1 Knapsack problem has a deterministic algorithm in \(O(n+w_\mathrm{max}^2\mathrm{log}^4w_\mathrm{max})\) time.

Our algorithm combines and extends several recent structural results and algorithmic techniques from the literature on knapsack-type problems:

1. We generalize the "fine-grained proximity" technique of Chen, Lian, Mao, and Zhang (2023) derived from the additive-combinatorial results of Bringmann and Wellnitz (2021) on dense subset sums. This allows us to bound the support size of the useful partial solutions in the dynamic program.

2. To exploit the small support size, our main technical component is a vast extension of the "witness propagation" method, originally designed by Deng, Mao, and Zhong (2023) for speeding up dynamic programming in the easier unbounded knapsack settings. To extend this approach to our 0-1 setting, we use a novel pruning method, as well as the two-level color-coding of Bringmann (2017) and the SMAWK algorithm on tall matrices.

<sup>∗</sup>cejin@mit.edu. Supported by NSF CCF-2129139, CCF-2127597, and a Siebel Scholarship.

Ce Jin<sup>∗</sup> MIT

