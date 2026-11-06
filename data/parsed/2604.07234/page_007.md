<tbc>We can choose _a_ and _b_ so as to agree with the null variant of the Random Subsequence Model as much as possible by insisting that the entries of _B_ have the same mean and variance as they would in the Random Subsequence Model. This amounts to choosing _a_=1_,b_=1/2, which corresponds to the entries of _B_ being i.i.d. Exponential(2). In Figure 2, we plot the exact solution (1.9) alongside the numerical solution of (1.4) for the null Random Subsequence Model. The fact that the two curves are very close suggests that the Strict-Weak Polymer Model may be fruitful to study to gain insight on the Random Subsequence Model. We pose some open problems in this direction in Section 5.

## 1.3. Outline of the proofs.

We now sketch the proofs of the main results, focusing on the key mechanisms that drive the analysis and postponing the technical details to the body of the paper.

### 1.3.1. _Proof overview of Theorem 1.1 and Corollary 1.2._

The convergence statements in (1.6) and (1.7) are essentially obtained in Section 2 by invoking the superadditive ergodic theorem on the log-partition function of the model. In the planted model, \(logZ_{X,\text{BDC}_{1-\alpha}(X)}\) is genuinely superadditive, and a coupling between \(\text{BDC}_{1-\alpha}(X)\) and a uniform length-_M_ subsequence transfers the weak limit to the fixed-length planted model. Rare occurrences can break this superadditivity in the null model, so we instead prove the weak law by directly exploiting the self-replicating structure of the subsequence count. We also obtain the first lower bound of (1.8) by encoding embeddings of \(S_{X^\prime,Y}\) via _skip vectors_, which record at each step how many occurrences of the current target bit are passed over a greedy embedding procedure. Realizing a vector with _s_ total skips is equivalent to requiring that a sum of _M+s_ i.i.d. Geom(1/2) random variables be at most _N_.

The main content of Theorem 1.1 is therefore the strict chain of quenched-annealed gaps given across (1.6) and (1.8), and we focus here on the ideas behind its proof. Our strategy is to recast separation between

0.7
annealed upper bound simulation lower bound
0.6
0.5
0.4
value
0.3
0.2
0.1
0.0
0.0
0.2
0.4
0.6
0.8
1.0
p

Figure 1. Our lower (green) and upper (blue) bounds on the uniform capacity of the deletion channel, together with a simulation-based computation of the true capacity curve (orange). All curves equal log2 at _p_=0 since the _y_-axis is in nats. The green curve is obtained by combining the lower bound \((log2-h(p))\unknown\{p\le 1/2\}\) from [DG01] with Corollary 1.2 (the dotted line means that the inequality is strict). The blue curve is obtained from Theorem 1.3 and (1.3). The orange curve is obtained by numerically solving (1.4) up to _N_=10,000.

