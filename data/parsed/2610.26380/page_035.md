## Appendix contents

**A Batching extension 35**<tbc>

A.1 Surrogate batch construction ..... 35<tbc>

A.2 The batched endgame ..... 36<tbc>

**B Supplements to §2 41**<tbc>

B.1 Derivations of calibration formulas ..... 41<tbc>

**C Proofs of results in §3 43**<tbc>

**D Proof of Theorem 2 48**<tbc>

D.1 Notation ..... 48<tbc>

D.2 Proof roadmap ..... 49<tbc>

D.3 Supporting lemmas ..... 50<tbc>

D.4 Proof of Theorem 2 ..... 57<tbc>

**E Supplement to §7 59**<tbc>

E.1 Allocations over the budget ..... 59<tbc>

E.2 Allocation of SA versus KG ..... 64<tbc>

E.3 Comparison to external benchmarks ..... 66

## Appendix A: Batching extension

In this section we present the additional technical details regarding the batching extension of §6.

### A.1. Surrogate batch construction

Throughout the construction of a batch, we hold \(\mu_{t-1}\), \(S_k^*(\mu_{t-1})\), and (_q<sub>t</sub>,b<sub>t</sub>_) fixed, as in §3.3. For a candidate batch _n_, its expected posterior covariance is<tbc>

\(\overline{\Sigma_t}(n,p_{t-1}):=\mathbb{E}\big[\text{Cov}(\theta|p_t)\big|n,p_{t-1}\big].\)

<tbc>Here _p<sub>t</sub>_ denotes the posterior after observing the outcomes of _n_ and the expectation is over all possible outcomes of the batch. For a round budget _B<sub>t</sub>_, substituting this covariance into the surrogate gives the integer program

\(min_n\sum_{\ell=1}^I\mathbb{E}_{\theta\sim N\left(\mu_{t-1},\overline{\Sigma_t}(n,p_{t-1})\right)}\big[\left(\theta_\ell-a_{q_t,b_t}(\theta)\right)^+\big]\text{s.t.}\sum_{(i,j)\in\mathcal{I}}r_jn_{ij}\le B_t,n_{ij}\in\mathbb{Z}_{\ge 0}\text{for all}(i,j)\in\mathcal{I}.\) (A.1)

As in (10), we have dropped the terms that do not depend on _n_. We approximately solve (A.1) by constructing the batch one evaluation at a time, as in Algorithm 4. To choose each additional evaluation, we approximate the expected posterior covariance in the objective by \(\Sigma'_t(n)\) using (12).

