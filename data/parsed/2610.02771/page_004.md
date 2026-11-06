### 1.3 Related work

#### Fixed-confidence best-arm identification.

The fixed-confidence PAC framework for bandits and foundational sample-complexity lower bounds for pure exploration were developed in \[6, 22\]. A large subsequent literature developed gap-adaptive algorithms and instance-dependent complexity measures, including successive elimination methods \[14\], LUCB-style subset-selection algorithms \[13\], UGapE-type candidate-challenger algorithms \[7\], and time-uniform confidence methods such as lil’UCB \[12\]. Information-theoretic lower bounds and asymptotically optimal sampling rules were developed in \[15, 8\]. The closest algorithmic template to ours is the UGapE framework of Gabillon et al. \[7\], which compares a candidate arm against its strongest challenger using confidence intervals. All of these works assume direct access to the realized reward at each round, so empirical means and confidence intervals can be formed directly; our setting drops this assumption.

#### Quantized feedback and communication-limited learning.

Communication limits have motivated a broad line of work on statistical inference and learning from quantized or few-bit messages \[4, 2, 3, 24\]. A particularly relevant subproblem is mean estimation from compressed, distributed, or one-bit observations \[16, 5, 18, 1\]. In bandit problems, limited communication has been studied in regret minimization and distributed exploration settings \[25, 10, 11\]. Our setting differs in that the objective is fixed-confidence best-arm identification, the feedback consists of adaptive one-bit set queries, and the rewards are only assumed to have finite variance. This weak moment assumption is what forces clipping and leads to the logarithmic penalty analyzed in this paper.

#### 1-bit mean estimation and threshold queries.

The fundamental statistical task underlying our approach is estimating the mean of a real-valued distribution from binary threshold comparisons. Lau and Scarlett \[21\] recently established order-optimal rates for this problem in the finite-variance regime, achieving the sample complexity \(O((\sigma^2/\beta^2)log(\sigma/\beta)log(1/\gamma))\); crucially, they show that the \(log(\sigma/\beta)\) factor is unavoidable with only a second-moment assumption, since the distribution need not have known bounded support. Our 1-bit estimator matches this rate up to the loglog overhead of time-uniform validity, and our lower bound shows that the same \(log(\sigma/\Delta)\) penalty transfers directly to the BAI problem. In contrast to standalone mean estimation, fixed-confidence BAI requires confidence guarantees that remain valid under adaptive arm selection, elimination, and stopping. Thus, the role of our randomized-threshold primitive is not to improve the standalone mean-estimation rate, but to provide an anytime confidence sequence that can be embedded directly into candidate-challenger BAI algorithms. The 1-bit framework also connects to the quantile bandit setting \[19\], which uses 1-bit feedback to identify the arm with the best quantile rather than the best mean.

## 2 A 1-bit mean estimator

We develop the 1-bit mean-estimation primitive through a three-stage construction. First, we establish a tail-integral identity that expresses the mean of a clipped variable as an integral of threshold probabilities. Second, we introduce a randomized thresholding scheme that allows us to estimate this integral using only a single bit per sample while maintaining a controlled bias-variance tradeoff. Finally, we derive a time-uniform confidence sequence for the mean, which enables the estimator to be used in adaptive, data-dependent stopping rules. We also discuss the sample complexity of the estimator in Corollary 6, and compare with the baseline of \[21\] in Remark 7.

Fix one arm and suppress the arm index. Let _X_ have mean \(\mu\), variance at most \(\sigma^2\), and let _c_ be an anchor point satisfying \(|\mu-c|\le\sigma\). Define the centered variable _W_:=_X-c_. Then

\(\mathbb{E}[W]=\mu-c,\mathbb{E}[W^2]\le Var(W)+(\mathbb{E}[W])^2\le 2\sigma^2.\)

Thus _W_ has controlled second moment and is centered near zero. Our task is now to estimate E\[_W_\], and hence \(\mu\), using only 1-bit threshold information.

