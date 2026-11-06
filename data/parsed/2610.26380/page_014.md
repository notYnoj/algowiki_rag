<tbc>loss small, then the resulting EOC will also be small. The bound holds with equality, for example, for the threshold \(a(\unknown)=\frac{1}{2}(\theta^{(k)}+\theta^{(k+1)})\). However, taking the expectation of mismatch loss is not tractable when the threshold is a function of such order statistics. We therefore restrict _a_ to a family of functions that allows for tractable analysis and find, within that family, the threshold function that gives the tightest bound on EOC.

The expected mismatch loss \(\mathbb{E}[\mathcal{M}(\unknown;S_k,a)|p_{t-1}]\) has terms of the form \(\mathbb{E}[(\theta_i-a(\unknown))^+|p_{t-1}]\). Since \(\unknown|p_{t-1}\) is Gaussian, the difference \(\theta_i-a(\unknown)\) is Gaussian whenever the threshold is affine in \(\unknown\), and the terms \(\mathbb{E}[(\theta_i-a(\unknown))^+|p_{t-1}]\) then have expressions amenable to analysis. This motivates the affine family of thresholds

\(a_{q,\mathbf{b}}(\unknown):=q+\mathbf{b}^\top(\unknown-\unknown_{t-1}),q\in\mathbb{R},\mathbf{b}\in\mathbb{R}^I,\)

where _q_ is the expected threshold level, and **_b_** governs how the threshold moves with the utilities. The difference \(\theta_i-a_{q,\mathbf{b}}(\unknown)\) is then \((\mu_{t-1,i}-q)+(\mathbf{e}_i-\mathbf{b})^\top(\unknown-\unknown_{t-1})\), a constant mean term \(\mu_{t-1,i}-q\) plus a mean-zero Gaussian term. By Lemma 1 any choice of (_q,**b**_) gives an upper bound for EOC, and a pair \((q_t^*,\mathbf{b}_t^*)\) that minimizes the expected mismatch loss gives the tightest upper bound for EOC within the affine threshold family. Before giving the optimality conditions for \((q_i^*,\mathbf{b}_t^*)\) in Theorem 1, it is convenient to define the following. Let \(\kappa_{q,\mathbf{b}}(\unknown):=\left|\{i:\theta_i>a_{q,\mathbf{b}}(\unknown)\}\right|-k\) denote the (random) deviation between the number of items above the threshold and its target _k_. That is, \(k+\kappa_{q,\mathbf{b}}(\unknown)\) is the number of items that exceed the threshold.

THEOREM 1. _The expected mismatch loss_ \(\mathbb{E}[\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})|p_{t-1}]\) _is convex in_ (_q,**b**_) _and attains a minimum. A pair_ \((q_t^*,\mathbf{b}_t^*)\) _is a minimizer only if either_

(_i)_ \((q_t^*,\mathbf{b}_t^*)=(\mu_{t-1,j},\mathbf{e}_j)\) _for some j=_1_,...,I, or_<tbc>

_(ii)_ \((q_t^*,\mathbf{b}_t^*)\neq(\mu_{t-1,j},\mathbf{e}_j)\) _for every j=_1_,...,I, and_<tbc>

<tbc>\(\mathbb{E}\big[\kappa_{q_t^*,\mathbf{b}_t^*}(\unknown)\big|p_{t-1}\big]=0\text{\textit{and}}\mathrm{Cov}\big(\theta_\ell,\kappa_{q_t^*,\mathbf{b}_t^*}(\unknown)\big|p_{t-1}\big)=0\text{\textit{for every}}\ell=1,\dots,I.\)<tbc>

<tbc>_Conversely, any pair satisfying_ (ii) _is a minimizer._

Case (i) arises when **_b_**=**_e_**_<sub>j</sub>_, so \(\theta_j-a_{q,\mathbf{b}}(\unknown)=\mu_{t-1,j}-q\) and \(\mathbb{E}[(\theta_j-a_{q,\mathbf{b}}(\unknown))^+|p_{t-1}]=(\mu_{t-1,j}-q)^+\) is not differentiable at \(q=\mu_{t-1,j}\). In the Appendix, we derive the necessary and sufficient condition for when such an exceptional point would be optimal. Otherwise, any optimum is characterized by (ii), which will capture most practical cases. We henceforth refer to any minimizer satisfying (ii) as an optimal affine threshold and focus our discussion and interpretation on this case.

Theorem 1 says that the optimal affine threshold satisfies the following two properties. First, in expectation, _k_ items will have their utility above it. Second, the covariance between each item’s utility and the deviation \(\kappa_{q,\mathbf{b}}(\unknown)\) is 0. If \(\kappa_{q,\mathbf{b}}\) were positively (negatively) correlated with \(\theta_\ell\), then when item \(\ell\)’s utility is larger than expected, in expectation more (fewer) than _k_ items would be above the threshold, meaning that the threshold is not moving up enough (is moving up too much) with item \(\ell\). At the optimum, no such _linear_ dependence remains: the threshold moves with \(\unknown\) in a way such that knowing that any particular item is high or low gives<tbc>

