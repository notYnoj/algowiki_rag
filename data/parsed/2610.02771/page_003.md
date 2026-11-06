Both the arm choice and the query set may depend on the entire past history, so the interaction is fully adaptive. This is the same 1-bit set-query model used in the lower-bound construction. In the algorithmic part of the paper, we only use randomized threshold queries, which form a particularly simple subclass of measurable set queries.

### Objective.

Fix an accuracy parameter \(\varepsilon>0\). We define the set of \(\varepsilon\)-optimal arms by

\(A_\varepsilon(\nu):=\{k\in\mathcal{A}:\mu_k\ge\mu^\star-\varepsilon\}.\)

A 1-bit best-arm identification algorithm consists of an adaptive query strategy, a stopping time \(\tau\), and a recommendation \(\widehat{k}\in\mathcal{A}\). It is said to be \((\varepsilon,\delta)\)-PAC if \(Pr_\nu(\tau<\infty)=1\) and \(Pr_\nu\big(\widehat{k}\notin A_\varepsilon(\nu)\big)\le\delta\) for every bandit instance \(\nu=(\nu_1,\dots,\nu_K)\) satisfying the above assumptions. Equivalently, with probability at least \(1-\delta\), the output arm satisfies \(\mu_\widehat{k}\ge\mu^\star-\varepsilon\).

This \(\varepsilon\)-relaxed objective is natural in our setting. It allows the learner to stop once it has ruled out all arms that are worse than the optimum by more than \(\varepsilon\), without spending additional samples to separate nearly tied arms. In particular, when \(\varepsilon<\Delta_{k^\star}\), the set \(A_\varepsilon(\nu)\) reduces to {_k<sup>⋆</sup>_}, and the \((\varepsilon,\delta)\)-PAC requirement becomes exact best-arm identification.

## 1.2 Contributions

### A time-uniform 1-bit mean-estimation primitive for adaptive BAI.

In Section 2, we formulate a randomized-threshold mean-estimation primitive based on a clipped tail-integral identity (Lemma 2). The resulting estimator admits confidence sequences that are valid uniformly over time (Theorem 5), which is essential for BAI because the number of samples collected from each arm is random and data-dependent. As a standalone mean estimator, its sample complexity matches the optimal finite- variance 1-bit mean-estimation rate of Lau and Scarlett \[21\], up to the standard iterated-logarithmic price of time-uniform validity (Corollary 6). The contribution here is structural rather than rate-level: rather than improving the standalone mean-estimation rate, we provide a BAI-ready confidence sequence that remains valid under adaptive arm selection and stopping.

### Fixed-confidence BAI algorithms under 1-bit feedback.

In Section 3, we show how to turn the above primitive into fixed-confidence BAI algorithms. The first algorithm, FIXEDCLIP-1BITBAI, uses a single clipping level tuned to the target accuracy \(\varepsilon\). It is simple and fully anytime, but its sample complexity contains an additional mixed term caused by the range of the clipped 1-bit statistic (Theorem 8). The second algorithm, RESTARTPHASEDCLIP-1BITBAI, uses phased adaptive clipping: it proceeds from coarse to fine resolutions and chooses the clipping level according to the current resolution. This removes the fixed-clipping mixed term and yields the main gap-adaptive upper bound of the paper (Theorem 10). Both algorithms are \((\varepsilon,\delta)\)-PAC, and their sample complexities are compared in Subsection 3.3.

### A matching information-theoretic lower bound for 1-bit BAI.

In Section 4, we prove a worst- case lower bound for fixed-confidence BAI under 1-bit set queries. The construction is closely related in spirit to multiscale hard instances for finite-variance 1-bit mean estimation of Lau and Scarlett \[21\], but is formulated directly as a _K_-arm BAI lower bound and combined with a change-of-measure argument for adaptive stopping. For a _K_-arm instance with all suboptimal gaps equal to \(\Delta\), we show that any algorithm that is \(\delta\)-correct over the instance class must have an expected stopping time of at least \(\Omega\left((K-1)\frac{\sigma^2}{\Delta^2}log\frac{\sigma}{\Delta}log\frac{1}{\delta}\right)\) (Theorem 12). This demonstrates that the \(\Theta(log\frac{\sigma}{\Delta})\) penalty is an unavoidable consequence of the 1-bit feedback constraint, proving that our algorithm is asymptotically optimal up to a loglog factor.

### Empirical validation.

Section 5 evaluates our 1-bit mean estimator and best-arm identification algorithms. For standalone estimation, our randomized estimator achieves lower mean absolute error and a smaller bias floor than the finite-variance baseline of Lau and Scarlett \[21\]. In the tested bandit settings, phased adaptive clipping uses fewer queries than fixed clipping on instances with heterogeneous gaps.

In the remainder of this paper, the main text presents and discusses our primary theoretical and numerical results, while all formal proofs, detailed algorithms, and experimental configurations are deferred to the appendix.

