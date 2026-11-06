<tbc>_Proof._ By Proposition 2.2 and Lemma 2.1, applied to (3.2), we have

\(\left\|x^*(t)-x_\ell^{[\mathrm{D}]}(t)\right\|_{A(t)}^2=\mathrm{min}_{p\in\mathbb{P}_\ell(0)}\left\|p(\overline{\Delta_k}(t))\overline{Q_k}(t)^\top\left(z^*(t)-z_0\right)\right\|_{\overline{\Delta_k}(t)}^2=\left\|p_\ell^{(t)}(\overline{\Delta_k}(t))\overline{Q_k}(t)^\top\left(z^*(t)-z_0\right)\right\|_{\overline{\Delta_k}(t)}^2,\text{(3.18)}\)

where _z_<sup>∗</sup>(_t_) denotes a solution of (3.2). The component of _z_<sup>∗</sup>(_t_) in R(<o>_Q_</o><sub>k</sub>(_t_)) satisfies \(\overline{Q_k}(t)^\top z^*(t)=\overline{\Delta_k}(t)^{-1}\overline{Q_k}(t)^\top\widehat{b}(t)\). Therefore,<tbc>

\(\overline{Q_k}(t)^\top\left(z^*(t)-z_0\right)=\overline{\Delta_k}(t)^{-1}\overline{Q_k}(t)^\top\widehat{b}(t)-\overline{Q_k}(t)^\top z_0=\overline{\Delta_k}(t)^{-1}\overline{Q_k}(t)^\top(\widehat{b}(t)-\widehat{A}(t)z_0).\)

<tbc>where we used \(\widehat{A}(t)=\overline{Q_k}(t)\overline{\Delta_k}(t)\overline{Q_k}(t)^\top\). Substituting this identity into (3.18),

\(\left\|x^*(t)-x_\ell^{[\mathrm{D}]}(t)\right\|_{A(t)}^2=\left\|p_\ell^{(t)}(\overline{\Delta_k}(t))\overline{\Delta_k}(t)^{-1}\overline{Q_k}(t)^\top(\widehat{b}(t)-\widehat{A}(t)z_0)\right\|_{\overline{\Delta_k}(t)}^2=\sum_{i=k+1}^n\frac{\widetilde{\zeta}_i(t)^2}{\widehat{\lambda}_i(t)}p_\ell^{(t)}(\widehat{\lambda}_i(t))^2.\)

□

We now present the asymptotic expansion of \(\widehat{A}(t)=P(t)A(t)\), along with its associated nonzero eigenvalues and corresponding eigenvectors, as well as \(\widehat{b}(t)=P(t)b\).

Lemma 3.3. _Under Assumption_ 3.1_, for sufficiently small_ \(t\ge 0\),

\(\widehat{A}(t)=\overline{S_k}\overline{\Lambda_k}\overline{S_k^\top}+t\overline{S_k}\overline{S_k^\top}E\overline{S_k}\overline{S_k^\top}+O(t^2),\widehat{\lambda}_i(t)=\lambda_i(t)+O(t^2),\text{\textit{for}}i=k+1,\dots,n,\widehat{s}_i(t)=s_i+t\underline{S_i}D_i\underline{S_i^\top} Es_i+O(t^2),\text{\textit{for}}i=k+1,\dots,n,\widehat{b}(t)=\overline{S_k}\overline{S_k^\top}b-t\overline{S_k}\overline{S_k^\top}ES_k\Lambda_k^{-1}S_k^\top b+O(t^2),\)

_where_ \(\overline{\Lambda_k}:=\mathrm{diag}(\lambda_{k+1},\dots,\lambda_n)\) _and D<sub>i</sub> is a diagonal matrix such that_<tbc>

\([D_i]_{jj}=\left\{\begin{array}{ c c }
0, & \text{\textit{for}}j=1,\dots,k, \\
1/(\lambda_i-\lambda_j), & \text{\textit{for}}j=k+1,\dots,n:j\neq i.
\end{array}\right.\)

<tbc>_Proof._ We first expand the projector _P(t_). Since \(S_k^\top V(t)=S_k^\top(A+tE)S_k=\Lambda_k+tS_k^\top ES_k\), a first-order expansion of the inverse gives

(3.19) \((S_k^\top V(t))^{-1}=\Lambda_k^{-1}-t\Lambda_k^{-1}S_k^\top ES_k\Lambda_k^{-1}+O(t^2).\)

Using this expansion in the definition of _P(t_) yields

\(P(t)=I_n-V(t)(S_k^\top V(t))^{-1}S_k^\top\)<br>
\(=I_n-(S_k\Lambda_k+tES_k)(\Lambda_k^{-1}-t\Lambda_k^{-1}S_k^\top ES_k\Lambda_k^{-1})S_k^\top+O(t^2)\)<br>
\(=I_n-S_kS_k^\top+tS_kS_k^\top ES_k\Lambda_k^{-1}S_k^\top-tES_k\Lambda_k^{-1}S_k^\top+O(t^2)\)<br>
\(=\overline{S_k}\overline{S_k^\top}-t(I_n-S_kS_k^\top)ES_k\Lambda_k^{-1}S_k^\top+O(t^2).\)

Hence, \(P(t)=\overline{S_k}\overline{S_k^\top}-t\overline{S_k}\overline{S_k^\top}ES_k\Lambda_k^{-1}S_k^\top+O(t^2)\). We now use the expression of _P(t_) to expand \(\widehat{A}(t)\) and \(\widehat{b}(t)\),

\(\widehat{A}(t)=P(t)A(t)=\overline{S_k}\overline{S_k^\top}(A+tE)-t\overline{S_k}\overline{S_k^\top}ES_k\Lambda_k^{-1}S_k^\top(A+tE)+O(t^2)\)<br>
\(=\overline{S_k}\overline{\Lambda_k}\overline{S_k^\top}+t\overline{S_k}\overline{S_k^\top}E(I_n-S_kS_k^\top)+O(t^2)\)<br>
\(=\overline{S_k}\overline{\Lambda_k}\overline{S_k^\top}+t\overline{S_k}\overline{S_k^\top}E\overline{S_k}\overline{S_k^\top}+O(t^2).\)

