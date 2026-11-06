<tbc>\[\(\underline{\mathrm{t}}\)\] A DEFLATION-BASED PRECONDITIONER FOR PCG 7<tbc>

<tbc>Define \(R(t):=\left(\lambda_i(t)I_{n-1}-\underline{\underline{\Lambda_i}}\right)^{-1}\). Using the expression of _s<sub>i</sub>(t_) in (3.10) gives

(3.15) \(d(t)=tR(t)\left(a(t)\underline{S_i^\top} Es_i+\underline{S_i^\top} E\underline{S_id}(t)\right).\)

Subtracting \(tR_0\underline{S_i^\top} Es_i\) from (3.15) yields

(3.16) \(d(t)-tR_0\underline{S_i^\top} Es_i=t\big(R(t)-R_0\big)\underline{S_i^\top} Es_i+tR(t)\left((a(t)-1)\underline{S_i^\top} Es_i+\underline{S_i^\top} E\underline{S_id}(t)\right).\)

The resolvent identity gives \(R(t)-R_0=\left(\lambda_i-\lambda_i(t)\right)R(t)R_0\). Since \(|\lambda_i-\lambda_i(t)|\le t\|E\|_2\), \(\|R(t)\|_2\le 2/g_i\) and ∥_R_<sub>0</sub>∥<sub>2</sub>=1_/g<sub>i</sub>_, we thus deduce,

(3.17) \(\|R(t)-R_0\|\le\frac{2t\|E\|_2}{g_i^2}.\)

Using the triangular inequality in (3.16), and (3.17), (3.11) and (3.14), we obtain

\(\left\|d(t)-tR_0\underline{S_i^\top} Es_i\right\|_2\le t\|R(t)-R_0\|_2\|E\|_2+t\|R(t)\|_2\left(|a(t)-1|\|E\|_2+\|E\|_2\|d(t)\|_2\right)\)<br>
\(\le\frac{2t^2\|E\|_2^2}{g_i^2}+\frac{8t^3\|E\|_2^3}{g_i^3}+\frac{4t^2\|E\|_2^2}{g_i^2}\le\frac{8t^2\|E\|_2^2}{g_i^2}.\)

where we have used \(\|\underline{S_i^\top} Es_i\|\le\|E\|_2\), \(\|\underline{S_i^\top} E\underline{S_i}\|\le\|E\|_2\), and the last inequality uses \(t\|E\|_2/g_i\le 1/4\). Combining this together with to (3.13), (3.14) and (3) completes the proof. □

To keep the analysis simple, in the remainder of the paper, we make the following assumption on the matrix _A_.

Assumption 3.1. _The eigenvalues of the matrix A are all simple._

**3.2. Deflated CG for the perturbed system.** In this section, we analyze deflated CG on the perturbed system (3.1).

Let \(1\le k\le n-1\). For sufficiently small \(t\ge 0\), let \((\widehat{\lambda}_i(t),\widehat{s}_i(t))\), _i=k_+1_,...,n_, denote the nonzero eigenpairs of \(\widehat{A}(t)=P(t)A(t)\), where the eigenvectors are chosen orthonormal and the pairs are indexed by continuation from the eigenpairs \((\lambda_i,s_i)\) of _A_ at _t_=0. Collecting them, we define

\(\overline{Q_k}(t)=[\widehat{s}_{k+1}(t),\dots,\widehat{s}_n(t)]\text{and}\overline{\Delta_k}(t)=\mathrm{diag}(\widehat{\lambda}_{k+1}(t),\dots,\widehat{\lambda}_n(t)),\)

so that \(\widehat{A}(t)=\overline{Q_k}(t)\overline{\Delta_k}(t)\overline{Q_k}(t)^\top\). The next theorem gives an explicit expression for the energy-norm error of deflated CG, based on Proposition 2.2 and Lemma 2.1.

Theorem 3.2. _Let_ \(1\le\ell<n-k\) _and let z_<sub>0</sub> _be any starting vector. Assume that the deflated CG iterate_ \(x_\ell^{[D]}(t)\) _is well defined for sufficiently small_ \(t\ge 0\)_. Then,_

\(\left\|x^*(t)-x_\ell^{[D]}(t)\right\|_{A(t)}^2=\sum_{i=k+1}^n\frac{\widetilde{\zeta}_i(t)^2}{\widehat{\lambda}_i(t)}p_\ell^{(t)}(\widehat{\lambda}_i(t))^2,\)

_where_ \(\widetilde{\zeta}_i(t):=\widehat{s}_i(t)^\top\left(\widehat{b}(t)-\widehat{A}(t)z_0\right)\)_, x_<sup>∗</sup>(_t_) _is the exact solution of_ (3.1)_, and_

\(\{p_\ell^{(t)}\}=\mathrm{arg}\mathrm{min}_{p\in\mathbb{P}_\ell(0)}\|p(\overline{\Delta_k}(t))\overline{Q_k}(t)^\top(z^*(t)-z_0)\|_{\overline{\Delta_k}(t)}^2.\)

