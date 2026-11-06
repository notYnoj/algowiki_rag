<tbc>by restricting the couplings to be GMMs on \(\mathbb{R}^d\times\mathbb{R}^d\). More precisely, given \(\mu_0,\mu_1\in\mathrm{GMM}_d\), one can define<tbc>

\(\mathrm{MW}_2^2(\mu_0,\mu_1):=\mathrm{inf}_{\pi\in\Pi^\mathrm{GMM}(\mu_0,\mu_1)}\int_{\mathbb{R}^{2d}}\|y_0-y_1\|_2^2\mathrm{d}\pi(y_0,y_1),\) (13)

<tbc>where \(\Pi^\mathrm{GMM}(\mu_0,\mu_1)\) denotes the set of probability measures in GMM<sub>2_d_</sub> with marginals \(\mu_0\) and \(\mu_1\). The problem is well-defined since this set contains the product measure \(\mu_0\otimes\mu_1\). The authors show that MW<sub>2</sub> defines a distance between elements of GMM<sub>_d_</sub>. Moreover, if \(\mu_0=\sum_{k=1}^{K_0}w_k^{(0)}\mu_k^{(0)}\) and \(\mu_1=\sum_{\ell=1}^{K_1}w_\ell^{(1)}\mu_\ell^{(1)}\), where \((w_k^{(0)})_k\in\triangle_{K_0}\) and \((w_\ell^{(1)})_\ell\in\triangle_{K_1}\), and \(\mu_k^{(0)},\mu_\ell^{(1)}\) are Gaussian measures, then it can be shown (\[DD20, Proposition 4\]) that<tbc>

\(\mathrm{MW}_2^2(\mu_0,\mu_1)=\mathrm{min}_{P\in\Pi(w_0,w_1)}\sum_{k,\ell} P_{kl}\mathrm{W}_2^2(\mu_k^{(0)},\mu_\ell^{(1)}),\) (14)

<tbc>where \(\Pi(w_0,w_1)\) is the set of \(K_0\times K_1\) matrices with non-negative entries and marginals _w_<sub>0</sub> and _w_<sub>1</sub>:<tbc>

\(\Pi(w_0,w_1)=\left\{P\in\mathcal{M}_{K_0,K_1}(\mathbb{R}^+);\forall k,\sum_jP_{kj}=w_k^{(0)}\text{and}\forall j,\sum_kP_{kj}=w_j^{(1)}\right\}.\)

<tbc>This discrete formulation makes MW<sub>2</sub> very easy to compute in practice, even in high dimensions. Indeed, the W<sub>2</sub> distance between two Gaussian measures \(\mu=\mathcal{N}(m,\Sigma)\) and \(\tilde{\mu}=\mathcal{N}(\tilde{m},\tilde{\Sigma})\) admits a closed-form expression:

\(\mathrm{W}_2^2(\mu,\tilde{\mu})=\|m-\tilde{m}\|_2^2+\mathrm{tr}\left(\Sigma+\tilde{\Sigma}-2\left(\Sigma^\frac{1}{2}\tilde{\Sigma}\Sigma^\frac{1}{2}\right)^\frac{1}{2}\right),\) (15)

where \(M^\frac{1}{2}\) denotes the unique positive semidefinite square root of the positive semidefinite matrix _M_. If the parameters of the GMMs \(\mu_0\) and \(\mu_1\) are known, computing Eq. (14) amounts to evaluating \(K_0\times K_1\) Wasserstein distances between Gaussians and solving a discrete transport problem of size \(K_0\times K_1\). It is also possible to define barycentres for MW<sub>2</sub> \[DD20; TDG24\], which leads to a similar discrete formulation. Given point clouds, \[DD20\] suggest using EM to fit GMMs to the data, allowing comparison of the point clouds with EM-\(\mathrm{MW}_2^2\).

## 3.2 Stability of \(\mathrm{MW}_2^2\) With Respect to GMM Parameters

To study the stability of the MW<sub>2</sub> distance with respect to the GMM parameters, we leverage a discrete OT stability result from \[TFD24\]. To relate this problem to discrete OT stability, we see \(\mathrm{MW}_2^2(\mu_0,\mu_1)\) as a particular discrete Kantorovich problem with cost matrix \(C_{k_0,k_1}:=\|m_{k_0}^{(0)}-m_{k_1}^{(1)}\|_2^2+d_\mathrm{BW}^2(\Sigma_{k_0}^{(0)},\Sigma_{k_1}^{(1)})\), where we recall the expression of the Bures-Wasserstein distance on \(S_d^+(\mathbb{R})\):

\(\forall\Sigma,\Sigma'\in S_d^+(\mathbb{R}),d_\mathrm{BW}(\Sigma,\Sigma'):=\sqrt{\mathrm{Tr}(\Sigma+\Sigma'-2(\Sigma^{1/2}\Sigma'\Sigma^{1/2})^{1/2})}.\) (16)

We show that if the GMM parameters are sufficiently close (thanks to EM convergence for instance), then the \(\mathrm{MW}_2^2\) costs will also be close thanks to the stability result from \[TFD24\]. While general sample complexity results for the EM algorithm are not available, assuming a certain rate of convergence towards the true parameters, this result shows that the precision obtained using EM translates into a precision on the \(\mathrm{MW}_2^2\) distance. This key observation is a first step towards guaranteeing the quality of \(\mathrm{MW}_2^2\) as a loss function with respect to the data. We formulate two results: first, Proposition 3.1 quantifies the decrease of \(\mathrm{MW}_2^2(\hat{\mu},\mu)\) when \(\hat{\mu}\) is an estimator of \(\mu\); then, Proposition 3.2 quantifies the decrease of \(|\mathrm{MW}_2^2(\hat{\mu},\hat{\mu})-\mathrm{MW}_2^2(\mu_0,\mu_1)|\) when \(\hat{\mu}\) are estimators of \(\mu_i\) for \(i\in\{0,1\}\). We defer the proofs to Appendix A.2.

**Proposition 3.1.** Consider GMM parameters \((\hat{w},\hat{m},\hat{\Sigma})\in\triangle_K\times\mathbb{R}^{K\times d}\times S_d^{++}(\mathbb{R})^K\) of a GMM \(\hat{\mu}\) as estimators of \((w,m,\Sigma)\in\triangle_K\times\mathbb{R}^{K\times d}\times S_d^{++}(\mathbb{R})^K\) which are parameters of a target GMM<tbc>

