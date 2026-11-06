<tbc>\[toc\] A DEFLATION-BASED PRECONDITIONER FOR PCG 5<tbc>

<tbc>The CG minimization property for (2.3) now gives

□

\(\left\|\widetilde{y}^*-\widetilde{y}_\ell\right\|_{\overline{\Delta_k}}^2=\mathrm{min}_{p\in\mathbb{P}_\ell(0)}\|p(\overline{\Delta_k})\left(\widetilde{y}^*-\widetilde{y}_0\right)\|_{\overline{\Delta_k}}^2=\mathrm{min}_{p\in\mathbb{P}_\ell(0)}\|p(\overline{\Delta_k})\overline{Q_k^\top}\left(z^*-z_0\right)\|_{\overline{\Delta_k}}^2.\)

**3. Deflated CG and PCG for a perturbed system.** Let _A(t_)=_A+tE_, where \(t\ge 0\) and _E_ is symmetric with \(\|E\|_F=1\). Since _A_ is SPD, _A(t_) is SPD for sufficiently small values of _t_. In this section, we compare the scaled spectral preconditioner in \[6\] with deflated CG when solving the perturbed linear system<tbc>

(3.1) \(A(t)x=b.\)

<tbc>Let \(1\le k\le n-1\). For deflated CG, we use the subspace _W=S<sub>k</sub>_=\[_s_<sub>1</sub>_,...,s<sub>k</sub>_\], formed by the eigenvectors associated with the _k_ largest eigenvalues \(\lambda_1,\lambda_2,\dots,\lambda_k\) of _A_. Set _V(t_)=_A(t)S<sub>k</sub>_ and \(P(t)=I_n-V(t)\left(S_k^\top V(t)\right)^{-1}S_k^\top\). The projected system is<tbc>

(3.2) \(\widehat{A}(t)z=\widehat{b}(t),\)

<tbc>where \(\widehat{A}(t):=P(t)A(t)\) and \(\widehat{b}(t):=P(t)b\). The \(\ell\)-th iterate of deflated CG is given by

(3.3) \(x_\ell^{[\mathrm{D}]}(t)=S_k\left(S_k^\top V(t)\right)^{-1}S_k^\top b+P(t)^\top z_\ell(t),\)

where \(z_\ell(t)\) is the iterate of CG when solving (3.2).

Let \(\theta>0\) and \(\Lambda_k:=\mathrm{diag}(\lambda_1,\dots,\lambda_k)\), the scaled spectral preconditioner is defined by \(U^\theta=I_n+S_k\left(\sqrt{\theta}\Lambda_k^{-1/2}-I_k\right)S_k^\top\). The associated preconditioned system is

(3.4) \(U^\theta A(t)U^\theta y=U^\theta b,x=U^\theta y.\)

Similarly, the \(\ell\)th iterate of PCG is \(x_\ell^{[\mathrm{P}]}(t)=U^\theta y_\ell(t)\), where \(y_\ell(t)\) is the iterate of CG when solving (3.4) starting from _y_<sub>0</sub>.

**3.1. Perturbation analysis.** In this section, we introduce the perturbation results to quantify how eigenvalues and eigenvectors change with _t_ and to control the gap terms in our subsequent comparison of the energy-norm errors of PCG and deflated CG. We first recall the first-order perturbation theory for simple eigenvalues and eigenvectors of symmetric matrices. These classical results (see, e.g., \[26\]) describe how the eigenpairs \(\{\lambda_i(t),s_i(t)\}\) of _A(t_) evolve with small _t_. For _i_=1_,...,n_ and if \(\lambda_i\) is simple, then

(3.5) \(\lambda_i(t)=\lambda_i+ts_i^\top Es_i+O(t^2),s_i(t)=s_i+t\underline{S_i}(\lambda_iI_{n-1}-\underline{\underline{\Lambda_i}})^{-1}\underline{S_i^\top} Es_i+O(t^2),\)

where \(\underline{\underline{\Lambda_i}}=\mathrm{diag}(\lambda_j)_{j\neq i}\), and \(\underline{S_i}\in\mathbb{R}^{n\times(n-1)}\) is obtained by removing the _i_th column from the eigenvector matrix of _A_. Second-order remainder estimates for eigenpairs are known; see, e.g., \[19, Ch. II\]. For our analysis, we provide a short self-contained proof for symmetric matrices. The resulting bound involves only concrete constants and an explicit range of validity for _t_, both expressed in terms of the spectral gap, without relying on contour integration.

Proposition 3.1. _Let_ \(i\in\{1,\dots,n\}\)_, and assume that_ \(\lambda_i\) _is simple. Let_ \(g_i:=\mathrm{min}_{j\neq i}|\lambda_i-\lambda_j|>0\) _be the spectral gap around_ \(\lambda_i\)_. Then, for every_ \(t\in[0,g_i/(4\|E\|_2)]\)_, A(t_) _admits a simple eigenpair_ \(\{\lambda_i(t),s_i(t)\}\) _such that_<tbc>

\(\left|\lambda_i(t)-\lambda_i-ts_i^\top Es_i\right|\le\frac{4\|E\|_2^2}{g_i}t^2,\left\|s_i(t)-s_i-t\underline{S_i}(\lambda_iI_{n-1}-\underline{\underline{\Lambda_i}})^{-1}\underline{S_i^\top} Es_i\right\|_2\le\frac{12\|E\|_2^2}{g_i^2}t^2.\)

<tbc>**Cahier du GERAD G-2026-70**

