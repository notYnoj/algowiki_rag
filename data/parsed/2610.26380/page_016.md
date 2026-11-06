<tbc>of Bayesian updating. Then we define the surrogate loss associated with evaluation (_i,j_) as the expected mismatch loss, with expectation taken with respect to <o>_p_</o><sub>t</sub>(_i,j_),

\(\mathbb{E}_{\unknown\sim\overline{p_t}(i,j)}\big[\mathcal{M}\big(\unknown;S_k^*\big(\unknown_{t-1}\big),a_{q_t,\mathbf{b}_t}\big)\big].\) (8)

In (8), the current prior and the threshold determine which items’ uncertainty is consequential, while \(\overline{\Sigma_t}((i,j),p_{t-1})\) determines how much of that uncertainty is expected to remain after evaluation (_i,j_). Lemma 2 gives an explicit expression for \(\overline{\Sigma_t}((i,j),p_{t-1})\).

LEMMA 2. _Starting with prior_ \(N(\unknown_{t-1},\Sigma_{t-1})\)_, let_ \(\unknown_{t-1,0}:=\theta_0\) _and, for evaluation_ \((i,j)\in\mathcal{I}\)_, define_<tbc>

\(\alpha_{t,ij}:=\frac{\beta_j(\mu_{t-1,i}-\mu_{t-1,j})}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\text{\textit{and}}\delta_{t,ij}:=\frac{\beta_j^2\sigma_{t-1,ij}^2}{1+\beta_j^2\sigma_{t-1,ij}^2}\frac{\phi(\alpha_{t,ij})^2}{\Phi(\alpha_{t,ij})\Phi(-\alpha_{t,ij})}.\)

<tbc>_Then the expected posterior covariance is_<tbc>

\(\overline{\Sigma_t}((i,j),p_{t-1})=\Sigma_{t-1}-\frac{\delta_{t,ij}}{\sigma_{t-1,ij}^2}\Sigma_{t-1}(\mathbf{e}_i-\mathbf{e}_j)(\mathbf{e}_i-\mathbf{e}_j)^\top\Sigma_{t-1}.\) (9)

<tbc>Here \(\delta_{t,ij}\) is the expected proportion of the variance of \(\theta_i-\theta_j\) reduced by the evaluation. This depends on how uncertain the outcome is a priori, the variance of \(\theta_i-\theta_j\), and the evaluation accuracy. The covariance terms in (9) determine how the information learned about (_i,j_) indirectly affects our posterior about other items through correlation. Plugging in the expected covariance in (9), the surrogate loss in (8) is<tbc>

\(\mathbb{E}_{\unknown\sim\overline{p_t}(i,j)}\big[\mathcal{M}\big(\unknown;S_k^*\big(\unknown_{t-1}\big),a_{q_t,\mathbf{b}_t}\big)\big]=kq_t-\sum_{\ell\in S_k^*(\unknown_{t-1})}\mu_{t-1,\ell}+\sum_{\ell=1}^I\mathbb{E}_{\unknown\sim\overline{p_t}(i,j)}\big[(\theta_\ell-a_{q_t,\mathbf{b}_t}(\unknown))^+\big].\)

<tbc>On the right-hand side, only the last term depends on (_i,j_), which can be thought of as the controllable part of the surrogate loss. Let \(\sigma'_{t,\ell}(i,j)\) and \(z'_{t,\ell}(i,j)\) denote the analogues of \(\sigma_{t-1,\ell}\) and \(z_{t-1,\ell}\) from (7) and Corollary 1 computed under the expected posterior. The controllable surrogate loss can be written as

\(\mathcal{L}((i,j)|p_{t-1}):=\sum_{\ell=1}^I\mathbb{E}_{\unknown\sim\overline{p_t}(i,j)}\big[(\theta_\ell-a_{q_t,\mathbf{b}_t}(\unknown))^+\big]\)<br>
\(=\sum_{\ell=1}^I\big[(\mu_{t-1,\ell}-q_t)\Phi(z'_{t,\ell}(i,j))+\sigma'_{t,\ell}(i,j)\phi(z'_{t,\ell}(i,j))\big].\) (10)

For later use, let \(\mathcal{L}_\ell((i,j)|p_{t-1})\) denote the \(\ell\)th term of (10). The allocation rule in §4 chooses, in each round, the evaluation whose resulting decrease in surrogate loss per unit of resource is largest.

## 4. Sequential evaluation allocation

We next use the surrogate loss to construct the sequential evaluation policy. §4.1 derives the marginal decrease in the surrogate per evaluation and the allocation rule based on it, §4.2 gives the sequential procedure, and §4.3 establishes that the policy is asymptotically consistent, meaning EOC \(\rightarrow 0\) as \(R\rightarrow\infty\).

