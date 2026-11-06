<tbc>\(\mathrm{GMM}_d^+(\infty)\) of GMMs with positive weights on R_<sup>d</sup>_, as in \[LMS18\]. Given two Gaussian mixtures \(\mu=\sum_{k_0=1}^{K_0}w_{k_0}^{(0)}g_{k_0},\nu=\sum_{k_1=1}^{K_1}w_{k_1}^{(1)}g_{k_1}\in\mathrm{GMM}_d^+(\infty)\), and regularisation parameters \((\lambda_0,\lambda_1)\in(0,+\infty)^2\), the unbalanced GMM-OT cost is defined as:

\(\mathrm{UMW}_2^2(\mu,\nu;\lambda_0,\lambda_1):=\mathrm{min}_{\pi\in\mathbb{R}_+^{K_0\times K_1}}\sum_{k_0,k_1}\pi_{k_0,k_1}\mathrm{W}_2^2(g_{k_0},g_{k_1})+\lambda_0\mathrm{KL}(\pi\mathbf{1}|w_0)+\lambda_1\mathrm{KL}(\pi^\top\mathbf{1}|w_1),\) (21)

where we recall that for \(a,b\in(0,+\infty)^K\), the Kullback-Leibler divergence is \(\mathrm{KL}(a|b):=\sum_ka_k\mathrm{log}(\frac{a_k}{b_k})\). We have seen that MW<sub>2</sub> is a particular discrete Kantorovich problem, and likewise the unbalanced GMM-OT distance UMW<sub>2</sub> is simply an unbalanced discrete OT problem with a particular cost matrix.

Given the numerical challenges of optimising the weights in the balanced formulation (see the discussion in Section 3.3), we introduce this variant as a possibly more stable alternative. We suspect that the underlying geometry on the weights induced by unbalanced OT \[LMS18; Chi+18b\] is more amenable to optimisation: we compare balanced and unbalanced flows in Appendix A.9.1 of the supplementary material. Furthermore, unbalanced OT has been shown by \[Fat+21a\] to be stable with respect to minibatch sampling, which is paramount for large-scale machine learning applications.

## 4 Illustrations and Quantitative Study of Gradient Methods

### 4.1 Practical Implementation

For practical implementation of the EM algorithm, some specific implementation strategies are required to ensure numerical stability, in particular when computing gradients. The first technique is applied in the E step, and consists in computing the responsibilities \(\gamma_{ik}(\theta_t)\) in logarithmic space and using the so-called "log-sum-exp trick"<sup>3</sup> to compute the normalisation in Eq. (3). Furthermore, to stabilise the (differentiable) expression of the Gaussian density \(g_{m,\Sigma}(x)\), we leverage the Cholesky decomposition of the covariance matrix \(\Sigma\), which uniquely decomposes \(\Sigma=LL^\top\) where \(L\in\mathbb{R}^{d\times d}\) is a lower triangular matrix. In particular, the computation of the inverse is simplified by solving triangular systems, and the determinant of \(\Sigma\) is simply \(\mathrm{det}\Sigma=(\prod_aL_{aa})^2\) (which we compute in logarithmic space as well).

Another important implementation aspect concerns a differentiable implementation of the matrix square root of symmetric positive semidefinite matrices. This is required in the computation of the Bures distance Eq. (16) for the MW<sub>2</sub> distance. Unfortunately, the naive implementation using the spectral decomposition suffers from numerical instability when eigenvalues are very close in value<sup>4</sup>. Leveraging an explicit formula for the gradient of the matrix square root (detailed in Appendix A.8), we circumvent these numerical issues by implementing our own differentiable square root function with an explicit gradient.

As is done in scikit-learn’s implementation of the EM algorithm, we have an optional regularisation term \(\varepsilon_r\ge 0\) for the covariance matrices \(\Sigma_k\) to ensure positive-definiteness. The idea is to replace the update \(\Sigma_k^{(t+1)}\) with \(\Sigma_k^{(t+1)}+\varepsilon_rI_d\) to enforce a minimum eigenvalue of \(\varepsilon_r\). This regularisation was particularly crucial for numerical stability in higher-dimensional cases where the covariances were almost singular, which led to exploding gradients. In the larger-scale examples from Section 5, we chose a heuristic which sets \(\varepsilon_r:=10^{-4}\times s_\mathrm{max}\), where _s_<sub>max</sub> is the largest eigenvalue of the covariances of a GMM fitted on the target data.

### 4.2 Flow of \(\mathrm{EM}-\mathrm{MW}_2^2\) with Fixed Weights in 2D

In this section, we illustrate the use of differentiable EM for OT by numerically computing the flow (i.e. gradient descent) of the following energy:

\(\mathcal{E}_T:=X\in\mathbb{R}^{n\times 2}\longmapsto\mathrm{MW}_2^2(\mu(F_X^T(\theta_0)),\nu),\) (22)

<sup>3</sup>for instance, see this blog post for an explanation of this well-known trick. <sup>4</sup>as explained in the PyTorch documentation for `torch.linalg.eigh()`.

