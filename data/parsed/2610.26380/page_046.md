<tbc>For each _i_, the variables \(\theta_\ell-\mu_{t-1,\ell}\) and \((e_i-b_t)^\top(\theta-\mu_{t-1})\) are jointly Gaussian. Thus,

\(\mathbb{E}\big[(\theta_\ell-\mu_{t-1,\ell})\unknown\big\{\theta_i>a_{q_t,b_t}(\theta)\big\}\big|p_{t-1}\big]\)<br>
\(=\frac{e_\ell^\top\Sigma_{t-1}(e_i-b_t)}{\sigma_{t-1,i}^2}\mathbb{E}\big[(e_i-b_t)^\top(\theta-\mu_{t-1})\unknown\big\{(e_i-b_t)^\top(\theta-\mu_{t-1})>q_t-\mu_{t-1,i}\big\}\big|p_{t-1}\big]\)<br>
\(=\frac{\phi(z_{t-1,i})}{\sigma_{t-1,i}}e_\ell^\top\Sigma_{t-1}(e_i-b_t)=w_{t-1,i}e_\ell^\top\Sigma_{t-1}(e_i-b_t).\)

Therefore,

\(\mathrm{Cov}\big(\theta_\ell,\kappa_{q_t,b_t}(\theta)\big|p_{t-1}\big)=\sum_{i=1}^Iw_{t-1,i}e_\ell^\top\Sigma_{t-1}(e_i-b_t)=e_\ell^\top\Sigma_{t-1}\left(\sum_{i=1}^Iw_{t-1,i}e_i-\left(\sum_{i=1}^Iw_{t-1,i}\right)b_t\right).\)

Thus, taking

\(b_t=\frac{\sum_{i=1}^Iw_{t-1,i}e_i}{\sum_{i=1}^Iw_{t-1,i}},\text{equivalently}b_{t,i}=\frac{w_{t-1,i}}{\sum_{\ell=1}^Iw_{t-1,\ell}},\)

makes the covariance zero for every \(\ell=1,\dots,I\). Hence both optimality conditions of Theorem 1 are satisfied, proving part (i).

For part (ii), set **_b_**=**0**, so only the constant threshold _q_ is optimized. By convexity, the optimum is characterized by the first-order condition<tbc>

\(0=\frac{\partial}{\partial q}\mathbb{E}\big[\mathcal{M}(\theta;S_k,a_{q,\mathbf{0}})\big|p_{t-1}\big]=k-\sum_{i=1}^I\mathbb{P}(\theta_i>q|p_{t-1})=k-\sum_{i=1}^I\Phi\left(\frac{\mu_{t-1,i}-q}{\sigma_{t-1,i0}}\right).\)

<tbc>Therefore the optimal constant threshold \(q_i^\mathrm{con}\) satisfies

\(\sum_{i=1}^I\Phi\left(\frac{\mu_{t-1,i}-q_t^\mathrm{con}}{\sigma_{t-1,i0}}\right)=k.\) □

_Proof of Lemma 2._ Fix an evaluation \((i,j)\in\mathcal{I}\). By the definition of expected posterior covariance and the law of total covariance,

\(\overline{\Sigma_t}((i,j),p_{t-1})=\mathrm{Cov}(\theta|p_{t-1})-\mathrm{Cov}\big(\mathbb{E}[\theta|X_{ij},p_{t-1}]\big|p_{t-1}\big)=\Sigma_{t-1}-\mathrm{Cov}\big(\mathbb{E}[\theta|X_{ij},p_{t-1}]\big|p_{t-1}\big).\)

Thus, we need the covariance of the posterior mean across the two possible outcomes. We compute this from the probability of each outcome and its resulting posterior mean.

First consider the outcome probabilities. Let _Z∼N_(0,1) be independent of \(\theta\). Then

\(\mathbb{P}(X_{ij}=x|p_{t-1})=\mathbb{E}\big[\Phi\big(x\beta_j(\theta_i-\theta_j)\big)\big|p_{t-1}\big]\)<br>
\(=\mathbb{P}\big(Z\le x\beta_j(\theta_i-\theta_j)\big|p_{t-1}\big)\)<br>
\(=\mathbb{P}\left(\frac{Z-x\beta_j(\theta_i-\theta_j-\mu_{t-1,i}+\mu_{t-1,j})}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\le\frac{x\beta_j(\mu_{t-1,i}-\mu_{t-1,j})}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\big|p_{t-1}\right)\)<br>
\(=\Phi\left(\frac{x\beta_j(\mu_{t-1,i}-\mu_{t-1,j})}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\right)=\Phi(x\alpha_{t,ij}).\)

