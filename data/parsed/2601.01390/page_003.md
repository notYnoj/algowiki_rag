canonical subsets. The quality of the halver with respect to the original subsets would indeed suffer, but since there are not too many canonical subsets overall and their sizes are small, the construction is cheaper. But how to generate good canonical subsets? Our idea is to adapt Koiliaris and Xu’s deterministic algorithm for this purpose! Putting these pieces together in the right way, the whole solution turns out to be relatively simple, describable in 3 pages (see Section 2).

### Other consequences.

Our new idea on halver construction can help derandomize other algorithms, too. We mention two applications:

1. Bringmann and Nakos \[BN20\] and Bringmann, Fischer, and Nakos \[BFN25\] recently obtained randomized _output-sensitive_ algorithms for the all-targets version of the subset sum problem, running in \(\widetilde{O}(|\mathrm{OUT}|^{4/3})\) and \(\widetilde{O}(|\mathrm{OUT}|\sqrt{n})\) time respectively. (Standard dynamic programming \[Bel57\] can be made to run in \(\widetilde{O}(|\mathrm{OUT}|n)\) time.) Our technique can derandomize both algorithms with the same time bound up to polylogarithmic factors in _n_ and _t_.<tbc>

2. Cygan, Mucha, Węrzycki, and Włodarczyk \[CMWW19\] gave a randomized reduction showing that if the min-plus convolution problem for _n_ elements could be solved in \(O(n^{2-\varepsilon})\) time, then the 0-1 knapsack problem for items with positive integer weights bounded by _t_ and positive real profits could be solved in randomized \(\widetilde{O}(t^{2-\varepsilon^\prime})\) time. Our technique provides a derandomization of this result. (Derandomizing reductions have gained more attention recently; e.g., see \[CH20, CX24, FKP24\].) In particular, this implies a deterministic \(O(t^2/2^{\Omega(\sqrt{\mathrm{log}t})})\)-time algorithm for 0-1 knapsack, by using Chan and Williams’ deterministic min-plus matrix multiplication algorithm \[CW21\] together with a known reduction from min-plus matrix multiplication to convolution \[BCD<sup>+</sup>14\].

The second application above follows immediately by our technique (see Appendix A). The first application is more interesting, however, and requires additional new ideas, as we can no longer apply Koiliaris and Xu’s approach to generate canonical subsets (see Section 3).

### Notation.

Let \[_u_\] denote {0,1_,...,u_}. For a set _S_ of integers, let \(\sigma(S)=\sum_{s\in S}s\). Define

\(\Sigma_i(X)=\{y:\exists S\subseteq X\text{with}|S|=i\text{and}\sigma(S)=y\}.\)

Let \(\Sigma_{\le k}(X):=\bigcup_{i\in[k]}\Sigma_i(X)\), and \(\Sigma(X)=\Sigma_{\le\infty}(X)\). The all-targets version of the subset sum problem is to compute \(\Sigma(X)\cap[t]\) for a given _t_.

## 2 An \(\widetilde{O}(t)\)-Time Algorithm

In this section, we present a deterministic \(\widetilde{O}(t)\)-time algorithm for all-targets subset sum.

### 2.1 Preliminaries: Review of Koiliaris and Xu’s algorithm

Many previous work on subset sum starts by considering the related problem of computing \(\Sigma_{\le k}(X)\) (or a superset) for a given _k_. Bringmann \[Bri17\] solved this version of the problem in randomized \(\widetilde{O}(ku)\) time, where _u_=max(_X_), whereas Koiliaris and Xu \[KX19\] solved it in deterministic \(\widetilde{O}(k^2u)\) time. We first review Koiliaris and Xu’s solution, as we will need it later. Their approach is a binary divide-and-conquer, using convolutions as a subroutine. We describe a simplified version below, running in \(\widetilde{O}(k^3u)\) time, which is good enough for our application; we reinterpret the divide-and-conquer in terms of dyadic intervals.

