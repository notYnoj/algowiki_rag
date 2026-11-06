\(=lim_{\epsilon\downarrow 0}\frac{1}{\epsilon}\mathbb{E}\big[\big(\theta_j-\mu_{t-1,j}-\epsilon c-(e_j+\epsilon d)^\top(\theta-\mu_{t-1})\big)^+\big|p_{t-1}\big]\)<br>
\(=lim_{\epsilon\downarrow 0}\frac{1}{\epsilon}\mathbb{E}\big[\big(-\epsilon c-\epsilon d^\top(\theta-\mu_{t-1})\big)^+\big|p_{t-1}\big]\)<br>
\(=\mathbb{E}\big[\big(-c-d^\top(\theta-\mu_{t-1})\big)^+\big|p_{t-1}\big].\)

Hence the directional derivative of the expected mismatch loss at \((\mu_{t-1,j},e_j)\) in direction (_c,d_) is

\(c\left[k-\sum_{i\neq j}\Phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)\right]-d^\top\Sigma_{t-1}\sum_{i\neq j}\frac{\phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)}{\sigma_{t-1,ij}}(e_i-e_j)+\mathbb{E}\big[\big(-c-d^\top(\theta-\mu_{t-1})\big)^+\big|p_{t-1}\big].\)

By convexity, \((\mu_{t-1,j},e_j)\) is a minimizer if and only if this directional derivative is nonnegative for every (_c,d_). At **_d_**=**0** this requires and is equivalent to

\(0\le k-\sum_{i\neq j}\Phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)\le 1.\) (C.1)

Now, for any fixed **_d_**, taking the infimum of the directional derivative over _c_ gives

\(\phi\big(\Phi^{-1}\big[k-\sum_{i\neq j}\Phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)\big]\big)\sqrt{d^\top\Sigma_{t-1}d}-d^\top\Sigma_{t-1}\sum_{i\neq j}\frac{\phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)}{\sigma_{t-1,ij}}(e_i-e_j).\)

Requiring this to be nonnegative for every **_d_** is equivalent to

\(\left(\sum_{i\neq j}\frac{\phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)}{\sigma_{t-1,ij}}(e_i-e_j)\right)^\top\Sigma_{t-1}\left(\sum_{i\neq j}\frac{\phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)}{\sigma_{t-1,ij}}(e_i-e_j)\right)\le\phi\big(\Phi^{-1}\big[k-\sum_{i\neq j}\Phi\big(\frac{\mu_{t-1,i}-\mu_{t-1,j}}{\sigma_{t-1,ij}}\big)\big]\big)^2.\) (C.2)

Therefore, \((\mu_{t-1,j},e_j)\) is a minimizer if and only if (C.1) and (C.2) hold. \(\square\)

_Proof of Corollary 1._ For part (i), by Theorem 1(ii), it is enough to verify the two optimality conditions.

We first consider the condition \(\mathbb{E}[\kappa_{q_t,b_t}(\theta)|p_{t-1}]=0\).

\(\mathbb{E}\big[\kappa_{q_t,b_t}(\theta)\big|p_{t-1}\big]=\mathbb{E}\left[\sum_{i=1}^I\unknown\left\{\theta_i>a_{q_t,b_t}(\theta)\right\}-k\big|p_{t-1}\right]=\sum_{i=1}^I\mathbb{P}\big(\theta_i>a_{q_t,b_t}(\theta)\big|p_{t-1}\big)-k.\)

We next compute these probabilities

\(\mathbb{P}\big(\theta_i>a_{q_t,b_t}(\theta)\big|p_{t-1}\big)=\mathbb{P}\big((e_i-b_t)^\top(\theta-\mu_{t-1})>q_t-\mu_{t-1,i}\big|p_{t-1}\big)=1-\Phi\big(\frac{q_t-\mu_{t-1,i}}{\sigma_{t-1,i}}\big)=\Phi(z_{t-1,i}).\)

Substituting this back gives

\(\mathbb{E}\big[\kappa_{q_t,b_t}(\theta)\big|p_{t-1}\big]=\sum_{i=1}^I\Phi(z_{t-1,i})-k.\)

We next verify the covariance condition in Theorem 1(ii). Expanding \(\kappa_{q_t,b_t}\) and using \(\mathbb{E}[\theta_\ell-\mu_{t-1,\ell}|p_{t-1}]=0\),

\(\text{Cov}\big(\theta_\ell,\kappa_{q_t,b_t}(\theta)\big|p_{t-1}\big)=\sum_{i=1}^I\mathbb{E}\big[(\theta_\ell-\mu_{t-1,\ell})\unknown\left\{\theta_i>a_{q_t,b_t}(\theta)\right\}\big|p_{t-1}\big].\)

