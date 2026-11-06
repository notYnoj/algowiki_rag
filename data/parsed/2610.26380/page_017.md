## 4.1. Marginal scores

Consider an arbitrary round _t_ for which we write L((_i,j_)) and \(\mathcal{L}_\ell((i,j))\) for the losses in (10), leaving the dependence on _p_<sub>_t_-1</sub> implicit. Let \(\mathcal{L}(0)=\sum_{\ell=1}^I\mathcal{L}_\ell(0)\) be the loss before any evaluation, obtained by replacing \(\sigma'_{t,\ell}(i,j)\) and \(z'_{t,\ell}(i,j)\) with \(\sigma_{t-1,\ell}\) and \(z_{t-1,\ell}\). To choose what evaluation to conduct we compute the decrease in surrogate loss per unit of resource

\(\psi_{t,ij}:=\frac{\mathcal{L}(0)-\mathcal{L}((i,j))}{r_J}\)

for each evaluation, then evaluate \(\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_t}\psi_{t,ij}\). This procedure, Surrogate Allocation (SA), is given in Algorithm 1.

**Algorithm 1** Surrogate Allocation (SA)

**Input:** \(\mu_{t-1},\Sigma_{t-1},R_t\ge\mathrm{min}(r_0,r_1)\)

1: Compute a minimizing threshold (_q<sub>t</sub>,b<sub>t</sub>_) via Theorem 1 and Corollary 1

2: Compute L(0)

3: **for** \((i,j)\in\mathcal{I}\) with \(r_j\le R_t\)

4: Compute \(\overline{\Sigma_t}((i,j),p_{t-1})\) by (9)

5: Compute L((_i,j_)) by (10)

6: \(\psi_{t,ij}\leftarrow[\mathcal{L}(0)-\mathcal{L}((i,j))]/r_J\)

7: **return** an evaluation in \(\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_t}\psi_{t,ij}\)

To get insight into what drives the evaluation choice, we write the surrogate marginal decrease explicitly.

\(\psi_{t,ij}=\frac{\mathcal{L}(0)-\mathcal{L}((i,j))}{r_J}=\frac{1}{r_J}\sum_{\ell=1}^I\int_{(\sigma_{t,\ell}^\prime(i,j))^2}^{\sigma_{t-1,\ell}^2}\frac{\partial\mathcal{L}_\ell}{\partial v}dv=\frac{1}{r_J}\sum_{\ell=1}^I\int_0^{1-\frac{(\sigma_{t,\ell}^\prime(i,j))^2}{\sigma_{t-1,\ell}^2}}\frac{\sigma_{t-1,\ell}}{2\sqrt{1-s}}\phi\left(\frac{z_{t-1,\ell}}{\sqrt{1-s}}\right)ds.\) (11)

The upper limit in the integral corresponds to the proportion of item \(\ell\)’s uncertainty (relative to the threshold) reduced by conducting evaluation (_i,j_). To see this more clearly, by Lemma 2 we have

\(1-\frac{(\sigma_{t,\ell}^\prime(i,j))^2}{\sigma_{t-1,\ell}^2}=\delta_{t,ij}\mathrm{Corr}\big(\theta_i-\theta_j,\theta_\ell-a_{q_t,b_t}(\theta)\big)^2,\)

where \(\delta_{t,ij}\) is the expected proportion of the variance of \(\theta_i-\theta_j\) reduced by the evaluation. The squared term measures how much of the variance reduction of (_i,j_) transfers to item \(\ell\) through correlation.

The integrand measures how valuable it is to reduce item \(\ell\)’s uncertainty for our objective. It is the instantaneous decrease in expected mismatch loss per additional proportion of its variance removed. The \(\phi(z_{t-1,\ell})\) term is large when we are highly uncertain about which side of the top-_k_ threshold item \(\ell\) lies on, which occurs when either the mean \(\mu_{t-1,\ell}\) is close to the expected threshold level _q<sub>t</sub>_ or when \(\sigma_{t-1,\ell}\) is large. The additional standard deviation term \(\sigma_{t-1,\ell}\) scales this uncertainty by how far the item’s utility may be from the threshold, reflecting that selection mistakes are penalized by their magnitude.

Put together, (11) scores an evaluation by how much its uncertainty reduction impacts expected mismatch loss across all items. The integrand captures how valuable reducing item \(\ell\)’s uncertainty (relative to the threshold) is, and the upper limit of the integral captures how much of this item’s uncertainty is reduced by evaluating (_i,j_), either directly when \(\ell\in\{i,j\}\) or indirectly through correlation when \(\ell\notin\{i,j\}\).

