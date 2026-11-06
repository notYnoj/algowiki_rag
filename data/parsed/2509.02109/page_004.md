## 2 Differentiation of the Expectation-Maximisation Algorithm

In this section, we study automatic differentiation methods for the Expectation-Maximisation (EM) algorithm, which can be used to fit a Gaussian Mixture Model (GMM) to a dataset _X_. This allows us to understand how the mixture changes when the data are modified (Fig. 1, left). Differentiable EM is used in various optimisation and learning applications, such as capsule networks \[HSF18\] and generative clustering \[AM25\]. Differentiable EM can also serve as an intermediate layer in distribution matching tasks (e.g. colour transfer, texture generation, and style transfer); see the particle flow illustration (Fig. 1, right), where we minimise a repulsive energy \(\mathcal{E}(X)=\sum_{k<\ell} V(\mu_k(X)-\mu_\ell(X))\), with \(V(x)=(\frac{1}{\|x\|}-1)^2\) and \((\mu_k(X))_{1\le k\le K}\) the means in the fitted GMM.

### 2.1 Main Ideas of the EM Algorithm

The EM algorithm \[DLR77\] attempts to fit a GMM to a dataset \(X=(x_1,\cdots,x_n)\in\mathbb{R}^{n\times d}\), with a fixed number of components _K_. We introduce the (hidden) quantities \(Y\in\unknown 1,K\unknown^n\) which encode the component index of each sample _x<sub>i</sub>_. The GMM parameters \(\theta:=(w,(m_k)_k,(\Sigma_k)_k)\) lie in the space \(\Theta:=\triangle_K\times(\mathbb{R}^d)^K\times(S_d^{++}(\mathbb{R}))^K\), where \(\triangle_K\) is the _K_-simplex defined as

\(\triangle_K:=\left\{w\in(0,1)^K|\sum_{k=1}^Kw_k=1\right\},\) (1)

and \(S_d^{++}(\mathbb{R})\) is the set of symmetric positive definite matrices. We will denote by \(\mu(\theta)\) the GMM probability measure of parameters \(\theta\). Given \(X\in\mathbb{R}^{n\times d}\) and \(Y\in\unknown 1,K\unknown^n\), the complete likelihood and its logarithm are respectively

\(L_\theta(X,Y)=\prod_{i=1}^n\prod_{k=1}^K\left(w_kg_{m_k,\Sigma_k}(x_i)\right)^{\unknown(Y_i=k)},\ell_\theta(X,Y)=\sum_{i=1}^n\sum_{k=1}^K\unknown(Y_i=k)log\left(w_kg_{m_k,\Sigma_k}(x_i)\right),\) (2)

where \(g_{m_k,\Sigma_k}\) is the Gaussian density with mean _m<sub>k</sub>_ and covariance \(\Sigma_k\) (recalled in Eq. (24)). Note that \(\ell_\theta\) cannot be optimised in \(\theta\) directly since we do not know the hidden variables _Y_ . The EM algorithm \[DLR77\] maximises the log-likelihood by iterating two steps over \(\theta_t\), first computing the "responsibilities" \(\gamma_{ik}(\theta_t)\) which are the posterior probabilities of the hidden quantities _Y<sub>i</sub>_ given the data _X_ and the current parameters \(\theta_t=(w^{(t)},(m_k^{(t)})_k,(\Sigma_k^{(t)})_k)\in\Theta\):

\(\gamma_{ik}(\theta_t)=\mathbb{P}_{(\mathbf{X},\mathbf{Y})\sim\mu(\theta_t)^{\otimes n}}\left[\mathbf{Y}_i=k|\mathbf{X}=X\right]=\left[w_k^{(t)}g_{m_k^{(t)},\Sigma_k^{(t)}}(x_i)\right]/\left[\sum_{\ell=1}^Kw_\ell^{(t)}g_{m_\ell^{(t)},\Sigma_\ell^{(t)}}(x_i)\right].\) (3)

The next iteration \(\theta_{t+1}\) corresponds to a maximisation of \(\ell_\theta(X,Y)\) with the unknown variables _Y_ replaced by the posterior probabilities \(\gamma_{ik}(\theta_t)\), which leads to the following closed-form expressions<tbc>



Figure 1: Left: sensitivity of the EM output to perturbation. Right: particle flow with repulsive energy.

