Projecting the next shadow onto R and N then yields \(\mathsf{P}Z^{k+1}=\mathsf{P}Z^k-r^\|(Z^k)\) and \(\mathsf{P}^\perp Z^{k+1}=\mathsf{P}^\perp Z^k-\tau r_\sigma^\perp(Z^k)\), which is the shadow recursion \(T_{\sigma,\tau}\) of §5.

The exact sGS variant \[CST17\] inserts a second equality solve: \(\lambda^{k+1/2}\) by (F.2), then _S_<sup>_k_+1</sup> by (F.3) with \(\lambda^{k+1/2}\), then \(\lambda^{k+1}\) by (F.2) with _S_<sup>_k_+1</sup>, then (F.4). The same shadow gives (F.5), while the last two equations give

\(X^{k+1}=(\mathrm{Id}-\tau\mathsf{P})X^k+\tau X_b+\tau\sigma\mathsf{P}^\perp(S^{k+1}-C),\) (F.7)

whose N projection again yields \(\mathsf{P}^\perp Z^{k+1}=\mathsf{P}^\perp Z^k-\tau r_\sigma^\perp(Z^k)\); the R projection of the shadow depends only on _S_<sup>_k_+1</sup> and matches ADMM. Thus both algorithms share the recursion \(T_{\sigma,\tau}\); the shadow records only the pair \((\mathsf{P}^\perp X^k,\mathsf{P}S^k)\), not all of (_X<sup>k</sup>,S<sup>k</sup>_).

## F.3 Parameter-dependent metric and rates for the shadow map

**Proposition F.2** (A parameter-dependent metric for the shadow map)**.** _For_ \(0<\tau<2\), \(T_{\sigma,\tau}\) _is_ \(\alpha_\tau\)_-averaged with_ \(\alpha_\tau=\mathrm{max}\{1,\tau\}/2\) _in the metric_ \(\mathsf{G}_\tau:=\mathsf{P}+\tau^{-1}\mathsf{P}^\perp\)_, whose eigenvalues bound it between_ \(\mathrm{min}\{1,\tau^{-1}\}\) _and_ \(\mathrm{max}\{1,\tau^{-1}\}\) _times the Frobenius metric._

_Proof of Theorem F.2._ Write \(T_{\sigma,\tau}=\mathrm{Id}-\mathsf{D}_\tau R_0\) with \(R_0:=\mathrm{Id}-T_{\sigma,1}\), which is firmly nonexpansive because the canonical DR map is \[BC17\]. Put _e=Z-W_ and _v=R_<sub>0</sub>_Z-R_<sub>0</sub>_W_, so \(\langle e,v\rangle\ge\|v\|_F^2\). With \(\mathsf{G}_\tau=\mathsf{D}_\tau^{-1}\), self-adjointness gives

\(\|e-\mathsf{D}_\tau v\|_{\mathsf{G}_\tau}^2=\|e\|_{\mathsf{G}_\tau}^2-2\langle e,v\rangle+\langle v,\mathsf{D}_\tau v\rangle\le\|e\|_{\mathsf{G}_\tau}^2-\big(\frac{2}{\mathrm{max}\{1,\tau\}}-1\big)\|\mathsf{D}_\tau v\|_{\mathsf{G}_\tau}^2,\)

using \(\langle v,\mathsf{D}_\tau v\rangle\le\mathrm{max}\{1,\tau\}\|v\|_F^2\le\mathrm{max}\{1,\tau\}\langle e,v\rangle\). This is the averagedness inequality with \(\alpha_\tau=\mathrm{max}\{1,\tau\}/2<1\) for \(\tau<2\); the metric bounds are the two eigenvalues of \(\mathsf{G}_\tau\).

_Proof of Theorem 5.1._ Combine (5.1), Theorem F.2, and Theorem F.1: the shadow distance contracts eventually Q-linearly in \(\mathsf{G}_\tau\) and the shadow converges R-linearly to some \(\bar{Z}=\bar{X}-\sigma\bar{S}\in\mathcal{Z}_\star\) (in the Boolean case \(\bar{X}=X_\star\)). For the raw variables: projections are Lipschitz, so \(\Pi_+(Z^k)\rightarrow\bar{X}\) and \(S^{k+1}\rightarrow\bar{S}\) R-linearly by (F.5). For ADMM, (F.6) is a stable linear recurrence with factor \(|1-\tau|<1\). Hence \(X^k\rightarrow\bar{X}\) R-linearly at any rate \(\widehat{\rho}\in(\mathrm{max}\{\rho,|1-\tau|\},1)\); the enlargement also absorbs the \(k\rho^k\) term when the two rates coincide. Then (F.2) transfers R-linear convergence to \(\lambda^{k+1}\), whose limit is the unique multiplier of \(\bar{S}\). For sGS-ADMM, (F.7) gives the exact contraction \(\mathsf{P}X^{k+1}-X_b=(1-\tau)(\mathsf{P}X^k-X_b)\). The component \(\mathsf{P}^\perp X^k=\mathsf{P}^\perp Z^k+\sigma\mathsf{P}^\perp C\) is read off the shadow. Together with the equality-solve formulas, this proves R-linear convergence of all raw sequences.

## F.4 PDHG: chart, factorization, and metric

Recall the chart of §5:

\(\Phi(X,\lambda)=(Z,r),Z:=X-\eta_x(C-\mathcal{A}^*\lambda),r:=\mathcal{A}X-b.\) (F.8)

The chart is consistent with, but does not require, the known PDHG-DR equivalences \[OV20\]. Throughout, _T_<sub>P</sub> is the PDHG map of §5, and \(\mathcal{Z}_\star^{\eta_x}\), \(\delta_{\eta_x}\), \(c_{\eta_x}\), \(t_{\eta_x}\) denote the fixed-point set, the residual, and the constants of (3.9) at \(\sigma=\eta_x\).

**Proposition F.3** (Exact PDHG transfer)**.** _Under surjectivity of_ A _and_ \(\eta_x,\eta_y>0\)_, the chart_ (F.8) _is an affine bijection mapping_ W_<sub>⋆</sub>_=Fix_T_<sub>P</sub> _onto_ \(\mathcal{Z}_\star^{\eta_x}\times\{0\}\)_, and_ (5.2) _holds with the linear isomorphism_<tbc>

\(\mathsf{L}_{\eta_x,\eta_y}(R^\|,R^\perp,r)=\left(\begin{array}{ c }
R^\|-R^\perp-\mathcal{A}^\dagger r-\eta_x\eta_y\mathcal{A}^*(2\mathcal{A}R^\|-r) \\
\mathcal{A}R^\|-r
\end{array}\right),(R^\|,R^\perp,r)\in\mathcal{R}\times\mathcal{N}\times\mathbb{R}^m.\) (F.9)

