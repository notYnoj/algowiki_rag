In both applications, the learner chooses the threshold before the fresh sample is drawn. We constrain the response to one bit and assume the threshold can be supplied through a downlink or a programmable comparator. Thus these mechanisms support the queries used by our algorithms.

We focus on distribution-free fixed-confidence BAI under a finite-variance assumption. The main challenge is that under 1-bit feedback, best-arm identification can no longer rely on direct empirical estimates of arm means. Even estimating the mean of a single arm becomes nontrivial: one must reconstruct a real-valued quantity from binary threshold queries while controlling both stochastic variance and approximation bias. Under only a second-moment assumption, this naturally leads to a clipping or truncation step \[20, 21\], and hence to a nontrivial bias–variance tradeoff. In the bandit setting, this difficulty is compounded by adaptivity: the learner must compare arms and decide when to stop using confidence intervals that remain valid uniformly over time, even though the number of pulls allocated to each arm is itself data-dependent. A fixed-target 1-bit mean estimator is not directly sufficient for a per-pull rule whose local sample counts are random and data-dependent. One needs either a time-uniform confidence sequence, as in Theorem 5, or an outer wrapper that invokes fixed-target estimators at prespecified checkpoints with simultaneous confidence control, as in phased successive elimination.

Our approach is organized around this clipping difficulty. The clipping level controls a bias-variance tradeoff: a larger level reduces clipping bias but enlarges both the variance proxy and the almost-sure range of the 1-bit estimator. The ideal choice therefore depends on the scale at which arms must be distinguished, a scale governed by the unknown gaps. We address this through a 1-bit estimator with time-uniform validity, embedded into two complementary BAI strategies: a fixed clipping level tuned to the target accuracy, and a phased adaptive scheme that matches the clipping level to the current statistical scale. Finally, we prove a _K_-arm equal-gap lower bound showing that the logarithmic penalty is intrinsic to finite-variance 1-bit feedback. It matches the leading _K_, gap, and confidence dependence of the phased upper bound on these worst-case instances, up to lower-order loglog factors.

## 1.1 Problem setting

We study fixed-confidence best-arm identification under 1-bit feedback. The learner is given a finite collection of arms A={1,2_,...,K_}. Pulling arm \(k\in\mathcal{A}\) produces an i.i.d. reward drawn from an unknown distribution \(\nu_k\) on R with mean \(\mu_k:=\mathbb{E}_{X\sim\nu_k}[X]\).

Throughout the paper, we assume that there is a known variance proxy \(\sigma>0\) such that<tbc>

\(\mathrm{Var}_{X\sim\nu_k}(X)\le\sigma^2\text{for all}k\in\mathcal{A}.\)

<tbc>In addition, for each arm _k_ we assume that we are given an anchor point _c<sub>k</sub>_ satisfying

\(|\mu_k-c_k|\le\sigma.\)

We assume that the best arm is unique, and denote it by \(k^\star=\mathrm{argmax}_{k\in\mathcal{A}}\mu_k\), and \(\mu^\star:=\mu_{k^\star}\).

**Remark 1** (Role of assumptions)**.** _The variance bound is the basic moment assumption under which our 1-bit estimator operates. The anchor condition plays a different role: it gives a localization of each arm mean, which is exactly what allows the 1-bit estimator to work efficiently. This localization can itself be obtained by the preliminary 1-bit routine_ MEDIANEST_, using at most_ \(O\left(K\mathrm{log}\frac{K\lambda}{\delta\sigma}\right)\) _threshold queries if_ \(\mu\in[-\lambda,\lambda]\) _with known_ \(\lambda\)_; see Appendix A. Furthermore, while we use_ \(|\mu_k-c_k|\le\sigma\) _for convenience, an anchor distance of_ \(|\mu_k-c_k|\le O(\sigma)\) _is adequate and only alters the constant factors in the bounds, as detailed in the Appendix A._

For every suboptimal arm \(k\neq k^\star\), define the gap \(\Delta_k:=\mu^\star-\mu_k>0\), and for the optimal arm define \(\Delta_{k^\star}:=\mathrm{min}_{j\neq k^\star}\Delta_j\). These gaps quantify the intrinsic difficulty of the instance: small gaps mean that the learner must distinguish arms with very close means, and hence must collect more information before stopping.

### 1-bit interaction model.

The learner does not observe rewards directly. Instead, at round _t_, it chooses an arm \(k_t\in\mathcal{A}\) together with a measurable query set \(A_t\subseteq\mathbb{R}\). The agent then observes a fresh reward sample \(X_{k_t,t}\sim\nu_{k_t}\) and returns only the single bit<tbc>

\(Y_t=\mathbf{1}\{X_{k_t,t}\in A_t\}\in\{0,1\}.\)

