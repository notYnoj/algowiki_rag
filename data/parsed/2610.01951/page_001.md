# Sharp Non-Asymptotic Analysis of the Penalized Challenger in \(\beta\)-EB-TCI for Bernoulli Bandits

**Abstract**

Top-two algorithms are simple and effective for fixed-confidence best-arm identification, but their sharp non-asymptotic behavior is still not well understood. We study this problem for Bernoulli bandits through \(\beta\)-EB-TCI, the empirical-best top-two rule of Jourdan et al. [9], whose challenger is chosen using a Bernoulli transportation cost with a logarithmic count penalty. We prove that, after the empirical leader has become the true best arm and its sampling fraction stays close to \(\beta\), the stopping time is \(T_\beta^\star(\mu)log(1/\delta)\) up to lower-order concentration terms. We also show that, in this regime, every challenger is sampled linearly often. Thus, for the original algorithm without forced exploration, the main remaining difficulty is to control when the empirical leader becomes permanently correct. These results imply a non-asymptotic high-probability bound for all Bernoulli instances with a unique best arm. If the algorithm satisfies a finite-mean sufficient-exploration condition, the bound further yields the sharp expected sample complexity. In particular, this gives the sharp expectation result for the unguarded Bernoulli rule when all arm means are pairwise distinct, using the sufficient-exploration result of Jourdan et al. [9]. Finally, if we add a mild forced-exploration rule that contributes only \(O(\sqrt{Kt})\) pulls up to time _t_, we obtain a self-contained expected sample-complexity theorem for any number of arms under the unique-best-arm assumption. We also identify a limitation of proof strategies that try to handle equal suboptimal means through a single index-comparison argument.

### 1 Introduction

Stochastic bandits model sequential decision-making under uncertainty. At each round, a learner chooses an arm, observes a reward, and uses the accumulated data to decide what to sample next. We study fixed-confidence best-arm identification for a Bernoulli bandit with a unique best arm \(i^\star=argmax_{i\in[K]}\mu_i\). A strategy stops at a random time \(\tau_\delta\) and recommends \(\widehat{i}_{\tau_\delta}\). It is \(\delta\)-correct if

\(\mathbb{P}_\mu(\tau_\delta<\infty)=1\text{and}\mathbb{P}_\mu(\widehat{i}_{\tau_\delta}\neq i^\star)\le\delta.\)

The goal is to minimize the expected number of samples while preserving both termination and the target error probability. We use _finite-confidence_ for guarantees that hold at each fixed \(\delta\), rather than only in the asymptotic limit \(\delta\rightarrow 0\).

A central benchmark is the instance-dependent characteristic time. Algorithms such as Track-and-Stop achieve the globally optimal leading-order sample complexity by tracking an optimal allocation online [14, 4]. Doing so requires repeatedly solving or approximating a global optimization problem. In this paper, the best arm is instead assigned a prescribed asymptotic sampling fraction \(\beta\in(0,1)\). The constrained characteristic time \(T_\beta^\star(\mu)\) is defined so that \(1/T_\beta^\star(\mu)\) is the largest worst-case information<tbc>

Nam Nguyen 1,2 Tuan Dam1,∗ 1Hanoi University of Science and Technology, Hanoi, Vietnam 2Center for AI Research, VinUniversity, Hanoi, Vietnam ∗Correspondence to: Tuan Dam <tuandq@soict.hust.edu.vn>

