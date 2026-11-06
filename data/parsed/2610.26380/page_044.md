<tbc>_Proof of Theorem 1._ \(\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})=ka_{q,\mathbf{b}}(\unknown)-\sum_{i\in S_k}\theta_i+\sum_{i=1}^I(\theta_i-a_{q,\mathbf{b}}(\unknown))^+\), so with \(\mathbb{E}[a_{q,\mathbf{b}}(\unknown)|p_{t-1}]=q\),

\(\mathbb{E}[\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})|p_{t-1}]=kq-\sum_{i\in S_k}\mu_{t-1,i}+\sum_{i=1}^I\mathbb{E}\big[(\theta_i-a_{q,\mathbf{b}}(\unknown))^+\big|p_{t-1}\big].\)

For each fixed \(\unknown\), \((\theta_i-a_{q,\mathbf{b}}(\unknown))^+\) is the positive part of an affine function of (_q,**b**_), hence convex. Summing, taking expectations, and adding the linear term _kq_ preserves convexity, so the expected mismatch loss is convex in (_q,**b**_).

We next show that the minimum is attained. Using \((x-y)^+\ge x^+-|y|\) in the definition of mismatch loss,<tbc>

\(\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})\ge ka_{q,\mathbf{b}}(\unknown)^++(I-k)\big(-a_{q,\mathbf{b}}(\unknown)\big)^+-\sum_{i=1}^I|\theta_i|\ge min\{k,I-k\}\big|a_{q,\mathbf{b}}(\unknown)\big|-\sum_{i=1}^I|\theta_i|.\)

<tbc>Moreover, since \(a_{q,\mathbf{b}}(\unknown)=q+\mathbf{b}^\top(\unknown-\mu_{t-1})\),

\(\mathbb{E}\big[\big|a_{q,\mathbf{b}}(\unknown)\big|\big|p_{t-1}\big]\ge|q|,2\mathbb{E}\big[\big|a_{q,\mathbf{b}}(\unknown)\big|\big|p_{t-1}\big]\ge\sqrt{\frac{2}{\pi}}\sqrt{\mathbf{b}^\top\Sigma_{t-1}\mathbf{b}}.\)

Since \(\Sigma_{t-1}\) is positive definite, the expected mismatch loss therefore tends to infinity as \(\|(q,\mathbf{b})\|_2\rightarrow\infty\). Since it is finite and convex, hence continuous, it attains a minimum.

It remains to characterize any minimizer not of the form \((\mu_{t-1,j},\mathbf{e}_j)\). For such a pair, for every _i_, either \(\mathbf{b}\neq\mathbf{e}_i\), in which case \(\theta_i-a_{q,\mathbf{b}}(\unknown)\) is a nondegenerate Gaussian, or **_b_**=**_e_**_<sub>i</sub>_ and \(q\neq\mu_{t-1,i}\), in which case \(\theta_i-a_{q,\mathbf{b}}(\unknown)=\mu_{t-1,i}-q\neq 0\). Thus,<tbc>

\(\mathbb{P}\big(\theta_i=a_{q,\mathbf{b}}(\unknown)\big|p_{t-1}\big)=0\text{for every}i,\)

<tbc>so the expected mismatch loss is differentiable at (_q,**b**_). Differentiating under the expectation gives<tbc>

\(\frac{\partial}{\partial q}(\theta_i-a_{q,\mathbf{b}}(\unknown))^+=-\mathbb{1}\{\theta_i>a_{q,\mathbf{b}}(\unknown)\},\frac{\partial}{\partial\mathbf{b}}(\theta_i-a_{q,\mathbf{b}}(\unknown))^+=-\mathbb{1}\{\theta_i>a_{q,\mathbf{b}}(\unknown)\}(\unknown-\mu_{t-1}).\)

<tbc>Summing over _i_, the indicators add to \(\kappa_{q,\mathbf{b}}(\unknown)+k\), giving

\(\frac{\partial}{\partial q}\mathbb{E}[\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})|p_{t-1}]=k-\mathbb{E}\big[\kappa_{q,\mathbf{b}}(\unknown)+k\big|p_{t-1}\big]=-\mathbb{E}\big[\kappa_{q,\mathbf{b}}(\unknown)\big|p_{t-1}\big],\)<br>
\(\frac{\partial}{\partial\mathbf{b}}\mathbb{E}[\mathcal{M}(\unknown;S_k,a_{q,\mathbf{b}})|p_{t-1}]=-\mathbb{E}\big[(\unknown-\mu_{t-1})\{\kappa_{q,\mathbf{b}}(\unknown)+k\}\big|p_{t-1}\big]=-\mathbb{E}\big[(\unknown-\mu_{t-1})\kappa_{q,\mathbf{b}}(\unknown)\big|p_{t-1}\big],\)

where the last equality uses \(\mathbb{E}[\unknown-\mu_{t-1}|p_{t-1}]=0\). The \(\ell\)th component of the second derivative is \(-\text{Cov}(\theta_\ell,\kappa_{q,\mathbf{b}}(\unknown)|p_{t-1})\). Thus, for any pair not of the form \((\mu_{t-1,j},\mathbf{e}_j)\), setting both derivatives to zero gives the conditions in Theorem 1(ii), which are necessary and sufficient for optimality by convexity.

We next characterize when an exceptional point in Theorem 1(i) is a minimizer. Fix _j_ and consider \((q,\mathbf{b})=(\mu_{t-1,j},\mathbf{e}_j)\). For any direction (_c,**d**_), the directional derivative of the _j_th positive-part term is<tbc>

\(lim_{\epsilon\downarrow 0}\frac{\mathbb{E}\big[\big(\theta_j-a_{\mu_{t-1,j}+\epsilon c,\mathbf{e}_j+\epsilon\mathbf{d}}(\unknown)\big)^+\big|p_{t-1}\big]-\mathbb{E}\big[\big(\theta_j-a_{\mu_{t-1,j},\mathbf{e}_j}(\unknown)\big)^+\big|p_{t-1}\big]}{\epsilon}\)

