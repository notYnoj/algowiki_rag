<tbc>no first-order information about whether the threshold has overshot or undershot. Next, Corollary 1 gives an explicit fixed-point characterization of \((q_t^*,b_t^*)\) in our Gaussian setting, which uses the following notation.

\(\sigma_{t-1,i}^2:=\mathbb{V}\left(\theta_i-a_{q,b}(\theta)\big|p_{t-1}\right)=(e_i-b)^\top\Sigma_{t-1}(e_i-b),\sigma_{t-1,ij}^2:=\mathbb{V}\left(\theta_i-\theta_j\big|p_{t-1}\right)=(e_i-e_j)^\top\Sigma_{t-1}(e_i-e_j),\) (7)

where **_e_**<sub>0</sub>=**0**, so \(\sigma_{t-1,i0}^2=\Sigma_{t-1,ii}\) is the variance of item _i_. We use this notation because, going forward, we will care more about the variance of items relative to the threshold \(\sigma_{t-1,i}^2\) than about an item’s variance \(\sigma_{t-1,i0}^2\).

COROLLARY 1. _Define_ \(z_{t-1,i}:=\frac{\mu_{t-1,i-q}}{\sigma_{t-1,i}}\) _and_ \(w_{t-1,i}:=\frac{\phi(z_{t-1,i})}{\sigma_{t-1,i}}\) .<tbc>

(_i)_ _The optimality conditions of Theorem 1(ii) are satisfied by_ \((q_t^*,b_t^*)\) _such that_<tbc>

<tbc>\(\sum_{i=1}^I\Phi(z_{t-1,i})=k,b_{t,i}^*=\frac{w_{t-1,i}}{\sum_{\ell=1}^Iw_{t-1,\ell}}\text{\textit{for}}i=1,\dots,I.\)<tbc>

_(ii)_ _If the threshold is restricted to be constant (i.e., **b**_=**0**_), so that_ \(a_{q,\mathbf{0}}(\theta)=q\)_, the optimal threshold_ \(q_t^{con}\) _satisfies_<tbc>

<tbc>\(\sum_{i=1}^I\Phi\left(\frac{\mu_{t-1,i}-q_t^{con}}{\sigma_{t-1,i0}}\right)=k.\)<tbc>

<tbc>To lighten notation, we write (_q<sub>t</sub>,b<sub>t</sub>_) for the optimal pair \((q_t^*,b_t^*)\). Each _b<sub>t,i</sub>_ describes how the threshold responds to movements in item _i_’s utility. Since \(b_{t,i}\propto w_{t-1,i}=\phi(z_{t-1,i})/\sigma_{t-1,i}\), this response is concentrated on items likely near the top-_k_ boundary. In this sense, the optimal threshold can be viewed as a first-order proxy for the random top-_k_ threshold: it moves linearly with the items that are most informative about where the threshold lies. Moreover, because \(\sum_{i=1}^Ib_{t,i}=1\), the difference \(\theta_i-a_{q_t,b_t}(\theta)\) depends only on the relative utilities, not on \(\overline{\theta}\). Thus, mismatch loss does not reward reducing decision-irrelevant uncertainty about \(\overline{\theta}\), putting ratings and comparisons on the same footing in line with the intuition of §3.1. Note that the special case constructed in §3.1 is in the set of affine thresholds: subtracting \(\overline{\theta}\) corresponds to **_b_**=**1**_/I_.

## 3.3. The surrogate loss

As discussed above, we treat the expected mismatch loss \(\mathbb{E}[\mathcal{M}(\theta;S_k^*(\mu_{t-1}),a_{q_t,b_t})|p_{t-1}]\) as a static objective fixed at state _p_<sub>_t_-1</sub> and use it to estimate how valuable each potential evaluation will be. We fix \(\mu_{t-1}\), \(S_k^*(\mu_{t-1})\), and (_q<sub>t</sub>,b<sub>t</sub>_) and value an evaluation (_i,j_) through the uncertainty it is expected to reduce. Accordingly, define its expected posterior covariance after evaluation (_i,j_)

\(\overline{\Sigma_t}((i,j),p_{t-1}):=\sum_{x\in\{-1,1\}}\mathbb{P}(X_{ij}=x|p_{t-1})\text{Cov}\left(\theta|X_{ij}=x,p_{t-1}\right),\)

and \(\overline{p_t}(i,j):=N\left(\mu_{t-1},\overline{\Sigma_t}((i,j),p_{t-1})\right)\). We call <o>_p_</o><sub>t</sub>(_i,j_) the _expected posterior_, since both of its moments are the expected posterior moments: the expected covariance, and the mean by the martingale property<tbc>

