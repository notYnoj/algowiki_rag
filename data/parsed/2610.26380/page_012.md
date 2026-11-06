<tbc>The KG policy then selects an evaluation according to

\(argmax_{(i,j)\in\mathcal{I}:r_j\le R_t}\frac{V_\text{myopic}((i,j)|p_{t-1})}{r_J}.\)

However, binary data can cause the KG policy to get "stuck" (Li et al. 2024). If the estimated top-_k_ set is sufficiently separated from the rest, no evaluation outcome can directly change the posterior top-_k_ set because the information a single binary outcome can carry is bounded, and with it how far the posterior means can move. This can occur frequently even when the top-_k_ set is far from certain. When this happens, KG has no basis to choose among evaluations, and a fallback rule, such as random allocation, is needed. This is not an issue with unbounded observations, such as a Gaussian likelihood, where there is always a possibility that a single evaluation can provide overwhelmingly positive/negative evidence that changes the posterior top-_k_ set.

## 3. Surrogate objective

Developing the surrogate objective combines two ideas. The first is to establish the expected mismatch loss and connect it to EOC. The second is how it drives evaluation choices. We treat the expected mismatch loss as a static objective fixed at state _p_<sub>_t_-1</sub>, using it to identify where uncertainty reduction is most valuable holding the current means fixed. The remainder of this section proceeds as follows. To provide insight into how the mismatch loss was developed, §3.1 presents our initial, simpler, intuition-based version, which then leads to the formal development in §3.2 that rigorously connects the surrogate to EOC and yields an improved form. Finally, §3.3 develops the resulting surrogate loss.

### 3.1. Mismatch loss: from intuition

Recall from the introduction that mismatch loss is defined as the expected magnitude of the inclusion errors of \(S_k^*(\mu_{t-1})\) and the exclusion errors of \(\{1,\dots,I\}\backslash S_k^*(\mu_{t-1})\). Measuring the magnitude of each error requires an anchor, a top-_k_ threshold against which they are measured. However, given the prior, the number of items above a given threshold is a random variable. A natural approach is therefore to choose a threshold such that, in expectation, the number of items above it is _k_.

More explicitly, at each evaluation round _t_, fix a threshold _q_ on the utility scale such that, in expectation, _k_ items have utility above _q_ under the prior _p_<sub>_t_-1</sub>. Then for each item \(i\in S_k^*(\mu_{t-1})\) the loss is \(\mathbb{E}[(q-\theta_i)^+]\), the expected amount it falls short of the top-_k_ threshold, and similarly for each item \(i\notin S_k^*(\mu_{t-1})\) the loss is \(\mathbb{E}[(\theta_i-q)^+]\), the expected amount it exceeds the top-_k_ threshold. We refer to the sum of these losses as the (informal) _expected mismatch loss_

\(\sum_{i\in S_k^*(\mu_{t-1})}\mathbb{E}\big[(q-\theta_i)^+\big|p_{t-1}\big]+\sum_{i\notin S_k^*(\mu_{t-1})}\mathbb{E}\big[(\theta_i-q)^+\big|p_{t-1}\big].\) (5)

The policy then chooses the evaluation whose resulting uncertainty reduction on \(\theta\) reduces expected mismatch loss the most per unit of resource. Two things make this conceptually attractive. First, it naturally directs evaluations toward items near the current expected top-_k_ cutoff (_q_) and toward items with substantial prior<tbc>

