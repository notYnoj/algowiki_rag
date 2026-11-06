<tbc>We next compute the posterior mean. By Bayes’ rule,

\(\mathbb{E}[\theta|X_{ij}=x,p_{t-1}]-\mu_{t-1}=\frac{\mathbb{E}\big[(\theta-\mu_{t-1})\mathbb{P}(X_{ij}=x|\theta)\big|p_{t-1}\big]}{\mathbb{P}(X_{ij}=x|p_{t-1})}=\frac{\mathbb{E}\big[(\theta-\mu_{t-1})\Phi\big(x\beta_j(\theta_i-\theta_j)\big)\big|p_{t-1}\big]}{\Phi(x\alpha_{t,ij})}.\)

It remains to evaluate the numerator.

\(\mathbb{E}\big[(\theta-\mu_{t-1})\Phi\big(x\beta_j(\theta_i-\theta_j)\big)\big|p_{t-1}\big]\)<br>
\(=\mathbb{E}\big[(\theta-\mu_{t-1})\unknown\{Z\le x\beta_j(\theta_i-\theta_j)\}\big|p_{t-1}\big]\)<br>
\(=\frac{x\beta_j\Sigma_{t-1}(e_i-e_j)}{1+\beta_j^2\sigma_{t-1,ij}^2}\mathbb{E}\big[\big(x\beta_j(\theta_i-\theta_j-\mu_{t-1,i}+\mu_{t-1,j})-Z\big)\unknown\{Z\le x\beta_j(\theta_i-\theta_j)\}\big|p_{t-1}\big]\)<br>
\(=\frac{x\beta_j\Sigma_{t-1}(e_i-e_j)}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\int_{-x\alpha_{t,ij}}^\infty u\phi(u)du\)<br>
\(=\frac{x\beta_j\phi(\alpha_{t,ij})}{\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\Sigma_{t-1}(e_i-e_j).\)

The second equality uses the covariance \(\mathrm{Cov}(\theta,x\beta_j(\theta_i-\theta_j)-Z|p_{t-1})=x\beta_j\Sigma_{t-1}(e_i-e_j)\) and variance \(1+\beta_j^2\sigma_{t-1,ij}^2\). The third equality standardizes the Gaussian, and the last uses \(\phi'(u)=-u\phi(u)\) and symmetry of \(\phi\).

Substituting into the posterior mean gives

\(\mathbb{E}[\theta|X_{ij}=x,p_{t-1}]-\mu_{t-1}=\frac{x\beta_j\phi(\alpha_{t,ij})}{\Phi(x\alpha_{t,ij})\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\Sigma_{t-1}(e_i-e_j).\)

We can now compute the covariance term. By the law of total expectation, \(\mathbb{E}[\mathbb{E}[\theta|X_{ij},p_{t-1}]|p_{t-1}]=\mu_{t-1}\), so

\(\mathrm{Cov}\big(\mathbb{E}[\theta|X_{ij},p_{t-1}]\big|p_{t-1}\big)\)<br>
\(=\sum_{x\in\{-1,1\}}\mathbb{P}(X_{ij}=x|p_{t-1})\left(\mathbb{E}[\theta|X_{ij}=x,p_{t-1}]-\mu_{t-1}\right)\left(\mathbb{E}[\theta|X_{ij}=x,p_{t-1}]-\mu_{t-1}\right)^\top\)<br>
\(=\frac{\beta_j^2\phi(\alpha_{t,ij})^2}{1+\beta_j^2\sigma_{t-1,ij}^2}\left(\sum_{x\in\{-1,1\}}\Phi(x\alpha_{t,ij})\big[\frac{x}{\Phi(x\alpha_{t,ij})}\big]^2\right)\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}\)<br>
\(=\frac{\beta_j^2\phi(\alpha_{t,ij})^2}{1+\beta_j^2\sigma_{t-1,ij}^2}\left(\frac{1}{\Phi(\alpha_{t,ij})}+\frac{1}{\Phi(-\alpha_{t,ij})}\right)\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}\)<br>
\(=\frac{\beta_j^2\phi(\alpha_{t,ij})^2}{(1+\beta_j^2\sigma_{t-1,ij}^2)\Phi(\alpha_{t,ij})\Phi(-\alpha_{t,ij})}\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}\)<br>
\(=\frac{\delta_{t,ij}}{\sigma_{t-1,ij}^2}\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}.\)

Here we used _x_<sup>2</sup>=1, \(\Phi(\alpha_{t,ij})+\Phi(-\alpha_{t,ij})=1\), and the definition of \(\delta_{t,ij}\). Substituting back into the expected posterior covariance yields

\(\overline{\Sigma_t}((i,j),p_{t-1})=\Sigma_{t-1}-\frac{\delta_{t,ij}}{\sigma_{t-1,ij}^2}\Sigma_{t-1}(e_i-e_j)(e_i-e_j)^\top\Sigma_{t-1}.\) □

