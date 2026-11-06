<tbc>Similarly, \(\widehat{b}(t)=P(t)b=\overline{S_k}\overline{S_k^\top}b-t\overline{S_k}\overline{S_k^\top}ES_k\Lambda_k^{-1}S_k^\top b+O(t^2)\).

Regarding the nonzero eigenvalues of \(\widehat{A}(t)\), the matrix \(\widehat{A}(t)=P(t)A(t)\), is analytic for all sufficiently small _t_. Standard perturbation theory therefore applies to each simple nonzero eigenvalue of \(\widehat{A}(0)\). In particular, the _O(t_<sup>2</sup>) term in the matrix expansion above does not affect the first-order eigenvalue and eigenvector coefficients. The unperturbed matrix \(\widehat{A}(0)=\overline{S_k}\overline{\Lambda_k}\overline{S_k^\top}\) has, by Assumption 3.1, _n-k_ simple eigenpairs \((\lambda_i,s_i)\) for _i=k_+1_,...,n_. Applying the first-order perturbation (3.5) to \(\widehat{A}(t)\) gives, for _i=k_+1_,...,n_,<tbc>

\(\widehat{\lambda}_i(t)=\lambda_i+ts_i^\top\overline{S_k}\overline{S_k^\top}E\overline{S_k}\overline{S_k^\top}s_i+O(t^2)=\lambda_i+ts_i^\top Es_i+O(t^2)=\lambda_i(t)+O(t^2),\)

<tbc>where we used \(\overline{S_k}\overline{S_k^\top}s_i=s_i\). Let \(W_i=\text{diag}(\underbrace{0,\dots,0}_{k\text{times}},\lambda_{k+1},\dots,\lambda_{i-1},\lambda_{i+1},\dots,\lambda_n)\), then the same first-order perturbation formula for the eigenvectors gives

\(\widehat{s}_i(t)=s_i+t\underline{S_i}(\lambda_iI_{n-1}-W_i)^{-1}\underline{S_i^\top}\overline{S_k}\overline{S_k^\top}E\overline{S_k}\overline{S_k^\top}s_i+O(t^2)=s_i+t\underline{S_i}D_i\underline{S_i^\top} Es_i+O(t^2).\)

□

## 3.3. Perturbation analysis of the preconditioned matrix.

The perturbation expansions for the eigenvectors of \(U^\theta A(t)U^\theta\) involve the factors \(1/(\lambda_i-\theta)\) for _i=k_+1_,...,n_, so obtaining estimates that are uniform in the scaling parameter requires \(\theta\) to stay a fixed positive distance away from the nondeflated eigenvalues. We formalize this through the following set.

Definition 3.4. _Let_ \(\gamma_0\) _be the smallest spectral gap_ \(\gamma_0:=min_{1\le i\le n-1}(\lambda_i-\lambda_{i+1})\) _which is positive by Assumption_ 3.1_. For a fixed_ \(k\in\{1,\dots,n-1\}\) _and_ \(\delta>0\)_, define_

(3.20) \(\Theta_\delta:=\left\{\theta\in[\lambda_n,\lambda_k]|min_{i=k+1,\dots,n}|\theta-\lambda_i|\ge\delta\right\}.\)

Note that, since the eigenvalues of _A_ are ordered decreasingly,

\(min_{i=k+1,\dots,n}|\lambda_k-\lambda_i|=\lambda_k-\lambda_{k+1}\ge\gamma_0.\)

Thus, \(\lambda_k\in\Theta_{\gamma_0}\). Decreasing \(\delta\) relaxes the separation condition, so \(\Theta_{\gamma_0}\subseteq\Theta_\delta\) whenever \(0<\delta\le\gamma_0\). Hence, \(\lambda_k\in\Theta_\delta\) and \(\Theta_\delta\) is nonempty. We henceforth fix \(0<\delta\le\gamma_0\) and choose \(\theta\in\Theta_\delta\), ensuring a distance of at least \(\delta\) from \(\lambda_{k+1},\dots,\lambda_n\).

Throughout the remainder of the paper, an estimate \(R(t,\theta)=O(t^2)\) stated uniformly for \(\theta\in\Theta_\delta\) means that there exist constants _C\>_0 and \(\hat{t}>0\), both independent of \(\theta\), such that<tbc>

\(\|R(t,\theta)\|\le Ct^2,\text{for every}\theta\in\Theta_\delta\text{and}0\le t\le\hat{t}.\)

<tbc>We now turn to the asymptotic analysis of the eigenvalues and eigenvectors of the preconditioned matrix \(U^\theta A(t)U^\theta\). For conciseness, set

\(A^\theta(t):=U^\theta A(t)U^\theta,\lambda_i^\theta(t):=\lambda_i(A^\theta(t)),s_i^\theta(t):=s_i(A^\theta(t)).\)

In this analysis, eigenvalue indices denote local perturbation branches rather than decreasing numerical order: indices 1_,...,k_ label the branch issued from the eigenvalue \(\theta\), while each index _i=k_+1_,...,n_ labels the branch issued from \(\lambda_i\).

