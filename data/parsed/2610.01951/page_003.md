<tbc>the pairwise-distinct-means corollary only for the tie-breaking variant covered by Jourdan et al. \[9\]. For the guarded algorithm, we prove the expected bound for any number of arms under a unique best arm. We also identify a limitation of one natural proof route for groups of equal-mean suboptimal arms: a single pointwise comparison of two penalized indices cannot by itself give a tail bound strong enough to ensure a finite expected time to reach the stabilized regime.

## 2 Related Work

### Fixed-confidence identification and allocation tracking.

Fixed-confidence best-arm identification has progressed from elimination-style methods to information-theoretic, instance-dependent analyses \[15, 3, 1, 11\]. The characteristic-time formulation of Kaufmann et al. \[14\] and Track-and-Stop of Garivier and Kaufmann \[4\] connect lower bounds to an adaptive rule that tracks a globally optimal allocation. Methods based on Lower/Upper Confidence Bounds (LUCB), together with KL-based refinements, form another major family \[10, 12, 7\]. Our setting fixes the best-arm sampling fraction at \(\beta\) and uses local leader-challenger updates rather than tracking the full optimal allocation.

### Top-two methods.

Top-two algorithms repeatedly compare a current leader with a selected challenger. They were introduced in Bayesian form by Russo \[16\], studied in fixed-confidence settings by Shang et al. \[17\], and developed into a frequentist bounded-reward framework by Jourdan et al. \[9\]. EB-TCI is the empirical-best member of that framework. We specialize it to Bernoulli rewards and analyze the exact logarithmically penalized challenger, rather than an unpenalized rule, a Gaussian approximation, or a different top-two construction. The Gaussian TTUCB result of Jourdan and Degenne \[8\] is the closest existing non-asymptotic analysis.

### Time-uniform concentration and stopping-time tails.

Our concentration arguments build on mixture martingales and time-uniform confidence bounds, often called confidence sequences \[13, 5, 6\]. A key step converts armwise KL confidence sequences into uniform control of pairwise Bernoulli GLR statistics at the effective sample size of the two arms. Separate work has emphasized that correctness and high-probability stopping bounds do not automatically imply a sharp expected stopping time \[2\]. Our analysis reflects this distinction: we first study the algorithm in the stabilized regime, and then separately bound how long it takes to enter that regime, both in probability and in expectation. The error guarantee for the GLR stopping rule is taken from Jourdan et al. \[9\]; termination and the finite-time behavior of the challenger counts are proved here. Appendix A records the precise role of each result used from prior work.

## 3 Setting and Algorithm

We consider a Bernoulli bandit with \(K\ge 2\) arms and mean vector \(\mu=(\mu_1,\dots,\mu_K)\in(0,1)^K\). We assume a unique best arm, \(i^\star=argmax_{i\in[K]}\mu_i\). After _t_ pulls, _N<sub>t,i</sub>_ denotes the number of times arm _i_ has been sampled, and \(\widehat{\mu}_{t,i}\) denotes its empirical mean. Unless stated otherwise, all finite-set argmax and argmin operations use one fixed deterministic tie-breaking rule; the experiments use the smallest-index rule. Corollary 6.5 is the only exception: it invokes a result of Jourdan et al. \[9\] for the tie-breaking convention covered by their theorem.

For \(p\in[0,1]\) and \(q\in(0,1)\), write

\(d(p,q):=plog\frac{p}{q}+(1-p)log\frac{1-p}{1-q},\)

with the conventions 0log0=0 and 1log1=0. When both arguments are in (0,1), this is the Bernoulli Kullback–Leibler divergence _d(p,q_)=KL(Ber(_p),_Ber(_q_)).

We use two related evidence statistics. For any distinct arms _i_ and _j_, the symmetric two-sample generalized likelihood-ratio statistic is \(V_t(i,j):=inf_{x\in(0,1)}\left\{N_{t,id}(\widehat{\mu}_{t,i},x)+N_{t,j}d(\widehat{\mu}_{t,j},x)\right\}.\) The value is symmetric in _i_ and _j_. Equivalently, the infimum may be taken over \[0,1\] using the standard boundary convention for Bernoulli KL. Replacing the empirical means by the true means gives the corresponding population quantity \(V_t^\mu(i,j):=inf_{x\in(0,1)}\left\{N_{t,id}(\mu_i,x)+N_{t,j}d(\mu_j,x)\right\}.\)

