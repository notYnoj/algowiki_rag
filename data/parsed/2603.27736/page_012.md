**Application 3: Conditional Lower Bounds.** Finally, our conditional lower bounds follow from the doubling reduction when appropriately generalized to _rectangular_ matrices (see Corollary 5.9). Besides applying this big hammer, most of the individual reductions require only simple or previously known ideas. One exception is Theorem 1.16. See Section 6 for details and Figure 1 for the resulting web of reductions.

**Even More Applications?** Overall, we are confident that our new low-rank APSP algorithm will find more applications in the future--perhaps in the design of more fine-grained reductions, or, even more ambitiously, perhaps even as a step towards challenging the APSP Hypothesis.

## 1.4.3 Subcubic Algorithm for Low-Rank Min-Plus Product

The proof of Theorem 1.18 is extremely involved. It builds on the recent algorithm for APSP with few distinct edge weights per node due to Abboud, Fischer, Jin, Vassilevska W., and Xi \[4\], which itself is already a complicated chain of reductions, and adds more layers to the chain. Even worse: To obtain the

n3+o(1) APSP Strong APSP [90] Lem. 5.7 Lem. 5.13 n-Uniform n-Universe MinPlus(n, n, n) MinPlus(n, n, n) Cor. 5.4 n2.5+o(1) Lem. 5.7 Lem. 5.13 n-Universe MinPlus(n, n, n) n-Universe MinPlus(n, n, n) Sec. 6 [33] [73] Min-Max Product Dir. Unw. APSP Node-Weighted APSP, Row-Monotone Min-Plus Product, Min-Equality Product, [95, 96, 26] All-Pairs Bottleneck Paths, All-Pairs Nondecreasing Paths, Approximate APSP (without Scaling),

**Figure 1.** Illustrates our fine-grained reductions and resulting lower bounds assuming that \(\omega=2\). Each arrow symbolizes a (tight) fine-grained reduction. Unlabeled arrows correspond to trivial reductions. The dashed arrows are conditioned on the additive combinatorics Hypothesis 1.12.

