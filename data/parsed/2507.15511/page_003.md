## Bridging Theory and Practice with IC-SubsetSum.

We address this gap. Let \(\Sigma(S)=\{\sum_{i\in T}a_i:T\subseteq[n]\}\) be the set of _distinct_ subset sums and write \(U=|\Sigma(S)|\). Because deciding (_S,t_) reduces to a simple membership query once \(\Sigma(S)\) is known, this list is an _information-theoretically minimal certificate_. Our new algorithm IC-SubsetSum deterministically enumerates every element of \(\Sigma(S)\) _exactly once_, prunes duplicates on the fly, and halts in deterministic worst-case time \(O(U\cdot n^2)\). We further show this can be improved to an expected time of \(O(U\cdot n)\) using randomization. Thus its runtime is provably bounded by a function of the certificate size, marking the first algorithm for Subset-Sum whose complexity scales with the true structural difficulty of the input. We build upon the algorithm initially introduced in the ‘Beyond Worst-Case Subset Sum’ framework \[Sal25\], now formalized under the IC-SubsetSum model.

## Contributions.

Our work makes four contributions:

• **Certificate-sensitive enumeration.** We design and analyse IC-SubsetSum, the first deterministic algorithm to construct the certificate \(\Sigma(S)\) with a runtime of \(O(U\cdot n^2)\) that adapts to the instance’s structure. We also present a randomized variant that achieves an expected runtime of \(O(U\cdot n)\).<tbc>

• **A guaranteed worst-case improvement.** We prove that IC-SubsetSum runs in \(O^*(2^{n/2-\varepsilon})\) time, with \(\varepsilon=log_2(\frac{4}{3})\), by combining double meet-in-the-middle with _Controlled Aliasing_ under a fixed count-based canonical expansion policy (CNF; see §5.2, App. E). This yields a deterministic speedup over classical meet-in-the-middle on _all_ inputs.<tbc>

• **Refined lower-bound methodology.** We formalise a "collision-free" promise variant of Subset-Sum and show that classical ETH/SETH reductions only rule out 2<sup>_n/_2</sup> algorithms on that structure-resistant slice. Future reductions must certify low collision entropy.<tbc>

• **Template for other problems.** We discuss how the certificate-sensitive viewpoint can guide new algorithms for knapsack, partition, and beyond.

## Advantage over Dynamic Programming.

The certificate-sensitive bound provides an exponential advantage over classical dynamic programming (DP) on instances with large numeric range but low structural complexity. For example, consider an instance _S_ with _n_-1 elements equal to 1, and one large element _L_=2_<sup>n</sup>_. For a target _t=L_, the DP runtime is \(O(n\cdot t)=O(n\cdot 2^n)\). In contrast, the number of unique subset sums for _S_ is only _U=O(n_), yielding a polynomial runtime of \(O(U\cdot n^2)=O(n^3)\) for IC-SubsetSum. Furthermore, the underlying enumeration framework supports anytime and online operation, allowing for interruption and incremental updates; these features are detailed in our companion technical paper \[Sal25\].

Unlike prior algorithms whose performance depends on less precise proxies (e.g., numeric range, pseudo-polynomial bounds, or number of solutions), our solver’s runtime is provably governed exactly by \(U=|\Sigma(S)|\) for every instance--the first such result treating _U_ as a formal instance-complexity certificate.

## Relation to Companion Papers.

This paper lays the foundational theoretical groundwork for the Certificate-Sensitive framework, building upon the algorithmic and empirical results presented in our technical companion paper \[Sal25\]. The framework’s approach is shown to be broadly applicable in two other companion papers, released concurrently, that extend it to the 0-1 Knapsack problem \[Sala, forthcoming\] and the 3-SAT problem \[Salb, forthcoming\].

