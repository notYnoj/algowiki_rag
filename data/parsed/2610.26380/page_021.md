<tbc>For the batching setting, let _T_ denote the _fixed_ number of rounds and let \(B_t\ge min\{r_0,r_1\}\) denote the budget for round _t_, with \(\sum_{t=1}^TB_t=R\). Let _n(t_) denote the batch chosen in this round, where _n<sub>ij</sub>(t_) is the number of evaluations of (_i,j_).

## 6.1. Surrogate batch construction

Choosing the batch that minimizes the surrogate loss in each round is an integer program that quickly becomes intractable as the batch budget grows. We therefore build a batch by committing to one evaluation at a time. The first evaluation is chosen as in the fully sequential problem, by maximizing the marginal decrease in surrogate loss per unit of resource from §4.1. However, unlike the sequential problem, we must choose subsequent evaluations before observing the outcomes of the evaluation already committed to the batch. If we continued to use the original marginal scores, we would value each evaluation as if it were the only one in the batch, allocating multiple evaluations to reduce the same uncertainty.

Consider the choice of the second evaluation. Suppose the first evaluation committed to the batch is (_i,j_). Although we have not yet observed its outcome, we can account for the information we expect to learn from it through its expected posterior covariance. By Lemma 2,

\(\overline{\Sigma_t}((i,j),p_{t-1})=\Sigma_{t-1}-\frac{\delta_{t,ij}}{\sigma_{t-1,ij}^2}\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}.\)

This covariance reflects the uncertainty expected to remain _after_ the first evaluation. To choose the second evaluation, we use this covariance in place of \(\Sigma_{t-1}\) and recompute the marginal scores from §4.1, keeping \(\mu_{t-1}\) and (_q<sub>t</sub>,b<sub>t</sub>_) fixed. Each candidate evaluation is scored by its _additional_ reduction in surrogate loss, accounting for the information we already expect to learn from the first. We choose the evaluation with the highest marginal score per unit of resource.

We next extend this approach to constructing an entire batch. The complication is that computing the expected posterior covariance after several committed evaluations requires taking the weighted average over their (many) possible joint outcomes. Instead, we approximate it by repeatedly applying the single-evaluation expected covariance update, using the updated expected covariance from the evaluations already committed.

Formally, let _n_ denote the matrix recording the evaluations committed so far in the batch, where _n<sub>ij</sub>_ corresponds to the number of evaluations of (_i,j_). Define _F<sup>ij</sup>_ as a matrix of the same size as _n_, with \(F_{ij}^{ij}=1\) and zero elsewhere. Let \(\Sigma'_t(n)\) denote our approximation of the expected posterior covariance, with \(\Sigma'_t(0)=\Sigma_{t-1}\). After adding evaluation (_i,j_) to the batch, it updates according to

\(\Sigma'_t(n+F^{ij})=\Sigma'_t(n)-\frac{\delta'_{t,ij}(n)}{(\sigma_{t,ij}^\prime(n))^2}\Sigma'_t(n)(e_i-e_j)(e_i-e_j)^\top\Sigma'_t(n),\) (12)

where \((\sigma_{t,ij}^\prime(n))^2\) and \(\delta'_{t,ij}(n)\) are computed as in Lemma 2, using \(\Sigma'_t(n)\) in place of \(\Sigma_{t-1}\).

Let \(\mathcal{L}(0;\Sigma'_t(n))\) be the surrogate loss before adding another evaluation and \(\mathcal{L}((i,j);\Sigma'_t(n))\) be the loss after adding (_i,j_). The marginal score of (_i,j_) is

\(\psi_{t,ij}(n)=\frac{\mathcal{L}(0;\Sigma'_t(n))-\mathcal{L}((i,j);\Sigma'_t(n))}{r_j}.\) (13)

