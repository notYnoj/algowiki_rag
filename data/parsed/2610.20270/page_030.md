We prove the following quantitative form. Under the hypotheses of Theorem F.1, an orbit starting with \(\mathrm{dist}(z^0,\mathrm{Fix}T)\le t_0\sqrt{g_\mathrm{min}/g_\mathrm{max}}\) satisfies

\(\mathrm{dist}_G(z^k,\mathrm{Fix}T)\le\rho^k\mathrm{dist}_G(z^0,\mathrm{Fix}T),\rho^2=1-\frac{1-\alpha}{\alpha}\bar{c}^2\frac{g_\mathrm{min}}{g_\mathrm{max}}\in(0,1),\) (F.1)

for any \(0<\bar{c}\le c\) small enough that \(\rho>0\). In the Euclidean norm, \(\mathrm{dist}(z^k,\mathrm{Fix}T)\le\sqrt{g_\mathrm{max}/g_\mathrm{min}}\rho^k\mathrm{dist}(z^0,\mathrm{Fix}T)\), and the iterates converge R-linearly to a point of Fix_T_. Every orbit converges to a fixed point and eventually enters such a neighborhood, so the conclusions hold eventually from any initialization.

_Proof._ The averagedness inequality \[BC17\] is

\(\|Tz-z_\star\|_G^2\le\|z-z_\star\|_G^2-\frac{1-\alpha}{\alpha}\|Tz-z\|_G^2(z_\star\in\mathrm{Fix}T).\)

Taking a _G_-nearest fixed point and using norm equivalence with the error bound gives \(\mathrm{dist}_G(Tz,\mathrm{Fix}T)^2\le\rho^2\mathrm{dist}_G(z,\mathrm{Fix}T)^2\) whenever \(\mathrm{dist}(z,\mathrm{Fix}T)\le t_0\). The initial condition gives \(\mathrm{dist}_G(z^0,\mathrm{Fix}T)\le\sqrt{g_\mathrm{min}}t_0\), and Fejér monotonicity preserves it, so \(\mathrm{dist}(z^k,\mathrm{Fix}T)\le t_0\) for every _k_; this proves (F.1) and its Euclidean form. Nonexpansiveness gives \(\|Tz-z\|_G\le 2\mathrm{dist}_G(z,\mathrm{Fix}T)\), so the step lengths have a geometrically summable tail and the iterates converge R-linearly to some point of Fix_T_. For an arbitrary starting point, averagedness gives boundedness and square summability of \(\|Tz^k-z^k\|_G\). A cluster point is fixed by continuity. Fejér monotonicity relative to it gives convergence of the whole sequence, which therefore eventually enters the neighborhood above.

Q-linear contraction is asserted in the _G_ metric; norm equivalence yields R-linear distance and iterate bounds in the original coordinates, not necessarily one-step contraction in every equivalent norm.

## F.2 ADMM and exact sGS-ADMM share one shadow map

The shared shadow representation of this subsection was established in the afterimage paper \[KY26a,  1 and Appendix A.2\]; we spell it out in the present notation, since the error-bound transfer of §5 acts on it. Note that for \(\tau\neq 1\) the map \(T_{\sigma,\tau}\) is _not_ the scalar relaxation \((1-\tau)\mathrm{Id}+\tau T_{\sigma,1}\); the multiplier step rescales the two orthogonal residual components blockwise. For \(\sigma>0\) and \(0<\tau<2\), exact ADMM on the dual SDP (3.1) is

\(\lambda^{k+1}=(\mathcal{A}\mathcal{A}^*)^{-1}\big[\sigma^{-1}b-\mathcal{A}(\sigma^{-1}X^k+S^k-C)\big],\) (F.2)

\(S^{k+1}=\Pi_+\big(C-\mathcal{A}^*\lambda^{k+1}-\sigma^{-1}X^k\big),\) (F.3)

\(X^{k+1}=X^k+\tau\sigma(\mathcal{A}^*\lambda^{k+1}+S^{k+1}-C).\) (F.4)

Define the shadow \(Z^k:=\mathsf{P}^\perp X^k+X_b-\sigma\mathsf{P}S^k-\sigma\mathsf{P}^\perp C\). Substitution in the first two equations gives

\(S^{k+1}=-\sigma^{-1}\Pi_-(Z^k),\) (F.5)

because \(\sigma(C-\mathcal{A}^*\lambda^{k+1})-X^k=-Z^k\) (check the R and N components separately using (F.2)); and the multiplier update reduces to the filter

\(X^{k+1}=(1-\tau)X^k+\tau\Pi_+(Z^k).\) (F.6)

