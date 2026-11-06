## 4.2. The sequential procedure

Now that we have an algorithm to choose the next evaluation, we lay out the full sequential evaluation procedure in Algorithm 2. It takes a family of policies {EVALUATIONRULE<sup>_R<sub>t</sub>_</sup>} that map the state and budget to an affordable evaluation. For now, the evaluation rule can be thought of as SA, but we write it in general form as we will introduce a different evaluation rule for the endgame in §5. It also assumes the posterior update comes from a BELIEFUPDATE procedure implementing an approximate inference method from Approximation 1.

**Algorithm 2** Sequential procedure

**Input:** prior \((\mu_0,\Sigma_0)\), _R_, {EVALUATIONRULE<sup>_R<sub>t</sub>_</sup>}

1: \(t\leftarrow 1,R_1\leftarrow R\)

2: **while** \(R_t\ge min(r_0,r_1)\)

3: \((i_t,j_t)\leftarrow\text{EVALUATIONRULE}^{R_t}(\mu_{t-1},\Sigma_{t-1})\)

4: Observe outcome _X<sub>t</sub>_

5: \((\mu_t,\Sigma_t)\leftarrow\text{BELIEFUPDATE}(\mu_{t-1},\Sigma_{t-1},(i_t,j_t),X_t)\)

6: \(R_{t+1}\leftarrow R_t-r_{j_t}\)

7: \(t\leftarrow t+1\)

8: \(T\leftarrow t-1\)

9: **return** \(S_k^*(\mu_T)\)

## 4.3. Asymptotic consistency

A natural concern with a policy based on a static objective is that it may reach a state from which, even with an infinite remaining budget, some items outside the final top-_k_ choice retain a positive probability of belonging to the true top-_k_. We show that this can never be the case for Algorithm 2 with EVALUATIONRULE<sup>_R<sub>t</sub>_</sup> = SA: in particular, the algorithm is asymptotically consistent, meaning EOC \(\rightarrow 0\) as \(R\rightarrow\infty\), under two mild assumptions.

ASSUMPTION 1. _The true link function_ \(g:\mathbb{R}\rightarrow(0,1)\) _is continuous, symmetric (g_(-_x)=_1-_g(x)), strictly increasing, and log-concave._

Assumption 1 is satisfied by the probit link we use \((g=\Phi)\) and allows for more general links.

ASSUMPTION 2. _Let_ \((\mu_t^*,\Sigma_t^*)\) _denote the exact first two moments of the posterior (which are generally unavailable in closed form). The approximate posterior moments_ \((\mu_t,\Sigma_t)\) _satisfy:_ (i) _there exist constants_ \(0<\chi_-\le\chi_+<\infty\) _such that, almost surely, for all sufficiently large t,_ \(\chi_-\Sigma_t^*\unknown\Sigma_t\unknown\chi_+\Sigma_t^*\), (ii) \(sup_t\|\mu_t\|_\infty<\infty\) _almost surely, and_ (iii) \(\mathbb{E}[\|\mu_T-\mu_T^*\|_\infty]\rightarrow 0\) _as_ \(R\rightarrow\infty\)_, where_ \(\|\cdot\|_\infty\) _is the L-infinity norm._

Assumption 2 says that whatever method we use in the BELIEFUPDATE step eventually yields a "good" estimate of the first two moments of the true posterior given the collected data.

THEOREM 2. _Under Assumptions 1 and 2, Algorithm 2 with_ EVALUATIONRULE<sup>_R<sub>t</sub>_</sup>=SA _satisfies_

\(\mathbb{E}\left[\sum_{i\in S_k^*(\theta)}\theta_i-\sum_{i\in S_k^*(\mu_T)}\theta_i\right]\rightarrow 0\text{\textit{as}}R\rightarrow\infty.\)

