## 2.2. Sequential evaluation process

Building on the generative model, we next describe how the sequential decision process unfolds. In each round _t_=1,2_,..._, the decision-maker chooses an evaluation \((i_t,j_t)\in\mathcal{I}\), a rating or a pairwise comparison, and observes its outcome \(X_t\in\{-1,1\}\) before choosing the next evaluation. Let _r_<sub>0</sub>_\>_0 and _r_<sub>1</sub>_\>_0 be the per-evaluation resource cost of ratings and comparisons, respectively, where the resource could be monetary or capacity (time it takes to conduct an evaluation). Let _R_ denote the total evaluation budget and _R<sub>t</sub>_ the budget left at the start of round _t_, so _R_<sub>1</sub>=_R_. An evaluation (_i,j_) is affordable in round _t_ when \(r_j\le R_t\). After conducting the chosen evaluation, its cost is deducted from the remaining budget, _R_<sub>_t_+1</sub>=_R<sub>t</sub>-r<sub>j<sub>t</sub></sub>_, where _j<sub>t</sub>_=min(_j<sub>t</sub>,_1). The process continues until no evaluation is affordable. Let _T_ denote the (random) total number of evaluations conducted, so \(T:=min\{t\ge 0:R_{t+1}<min(r_0,r_1)\}\).

In round _t_, after the outcome is observed, we update the posterior according to

\(p_t(\theta)\propto p_{t-1}(\theta)\Phi\big(X_t\beta_{j_t}(\theta_{i_t}-\theta_{j_t})\big)\propto p_0(\theta)\prod_{s=1}^t\Phi\big(X_s\beta_{j_s}(\theta_{is}-\theta_{js})\big),\)

where _p_<sub>0</sub> is the prior of \(\theta\) at _t_=0. The posterior after any round _t_ is denoted by _p<sub>t</sub>_ and hence its prior is the posterior of the previous round, _p_<sub>_t_-1</sub>. Figure 1 illustrates the sequential process. Since the Gaussian prior is

not conjugate to the probit likelihood<sup>1</sup>, the posterior after each round is generally non-Gaussian. One option is to carry out posterior inference by Markov Chain Monte Carlo (MCMC). However, MCMC yields posterior samples rather than a posterior with a functional form, and to formulate the round-_t_ evaluation allocation problem we rely on a closed-form approximation of _p_<sub>_t_-1</sub>. It is therefore natural to use an approximate inference method such as expectation propagation (Minka 2001, Herbrich et al. 2006), Laplace approximation (Tierney and Kadane 1986), or variational inference (VI) (Jordan et al. 1999) with a multivariate Gaussian variational family.

APPROXIMATION 1. _After each round t, approximate_ \(p_t\approx N(\mu_t,\Sigma_t)\) _using one of the approximate inference methods above. We refer to this Gaussian approximation as the posterior._

We now define the terminal objective, expected opportunity cost (EOC), which we adopt for reasons discussed in the introduction. To write EOC it is convenient to let \(S_k^*(\theta)\) denote the set of indices of the _k_ largest

<sup>1</sup> Exact conjugacy is available through the unified skew-normal family, but computing its moments involves multivariate Gaussian CDFs whose dimension grows with the data (Durante 2019).

(Pt-1, Rt) (it, jt) Xt t=T prior choose evaluation evaluate update beliefs select k t<T Figure 1 The sequential evaluation process.

