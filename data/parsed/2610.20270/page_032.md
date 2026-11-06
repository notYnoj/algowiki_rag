_Consequently, if the canonical residual with_ \(\sigma=\eta_x\) _satisfies_ (3.9)_, then there are c_<sub>P</sub>_,t_<sub>P</sub>_\>_0 _with_ \(\|\delta_\mathrm{P}(w)\|\ge c_\mathrm{P}\mathrm{dist}(w,\mathcal{W}_\star)\) _whenever_ \(\mathrm{dist}(w,\mathcal{W}_\star)\le t_\mathrm{P}\)_, where_ \(\delta_\mathrm{P}:=T_\mathrm{P}-\mathrm{Id}\).

_Proof._ The linear part of \(\Phi\) is \(\mathsf{M}_\Phi=\left[\begin{array}{ c }
\mathrm{Id} \\
\mathcal{A} \\
0
\end{array}\right]\). If \(X+\eta_x\mathcal{A}^*\lambda=0\) and A_X_=0, then \(\mathcal{A}\mathcal{A}^*\lambda=0\), so \(\lambda=0\) and _X_=0. Hence the square map is invertible, with explicit inverse \(X=X_b+\mathcal{A}^\dagger r+\mathsf{P}^\perp(Z+\eta_xC)\), \(\lambda=\eta_x^{-1}(\mathcal{A}\mathcal{A}^*)^{-1}\mathcal{A}(Z-X+\eta_xC)\). At a fixed point, A_X=b_ and \(X=\Pi_+(X-\eta_xS)\) with \(S=C-\mathcal{A}^*\lambda\)--exactly the KKT conditions--so the image of the fixed set is as claimed. Since \(X^+=\Pi_+(Z)\), decomposing by \(\mathsf{P},\mathsf{P}^\perp\) gives<tbc>

\(X^+-X=r^\|(Z)-r_{\eta_x}^\perp(Z)-\mathcal{A}^\dagger r,r^+=\mathcal{A}r^\|(Z),\lambda^+-\lambda=\eta_y\big(r-2\mathcal{A}r^\|(Z)\big),\)

<tbc>and \(Z^+-Z=X^+-X+\eta_x\mathcal{A}^*(\lambda^+-\lambda)\) proves (5.2). For injectivity of \(\mathsf{L}_{\eta_x,\eta_y}\), suppose the image is zero. The second component gives \(r=\mathcal{A}R^\|\). Substituting into the first gives \(-R^\perp-\eta_x\eta_y\mathcal{A}^*\mathcal{A}R^\|=0\), whose two terms lie in the orthogonal spaces N and R. Hence \(R^\perp=0\) and \(\mathcal{A}R^\|=0\), which forces \(R^\|=0\) and then _r_=0. Equal finite dimensions give the isomorphism; neither invertibility uses the step-size inequality. Finally, let \(\ell:=\sigma_\mathrm{min}(\mathsf{L}_{\eta_x,\eta_y})>0\), \(a_\Phi:=\sigma_\mathrm{min}(\mathsf{M}_\Phi)>0\), \(b_\Phi:=\|\mathsf{M}_\Phi\|_\mathrm{op}\). Whenever \(\mathrm{dist}_F(Z,\mathcal{Z}_\star^{\eta_x})\le t_{\eta_x}\), orthogonality of the residual components gives

\(\|\Phi T_\mathrm{P}\Phi^{-1}(Z,r)-(Z,r)\|\ge\ell\sqrt{\|\delta_{\eta_x}(Z)\|_F^2+\|r\|_2^2}\ge\ell\mathrm{min}\{c_{\eta_x},1\}\mathrm{dist}\big((Z,r),\mathcal{Z}_\star^{\eta_x}\times\{0\}\big).\)

Moreover \(\Phi\) is affine, so \(a_\Phi\mathrm{dist}(w,\mathcal{W}_\star)\le\mathrm{dist}(\Phi w,\Phi\mathcal{W}_\star)\le b_\Phi\mathrm{dist}(w,\mathcal{W}_\star)\), and the transformed displacement is \(\mathsf{M}_\Phi\delta_\mathrm{P}(w)\). One may therefore take \(c_\mathrm{P}=(a_\Phi/b_\Phi)\ell\mathrm{min}\{c_{\eta_x},1\}\) and \(t_\mathrm{P}=t_{\eta_x}/b_\Phi\).

For a fixed instance, invertibility already supplies the positive constants; uniform invertibility would be needed only for constants uniform over a family of data and step sizes.

**Proposition F.4** (PDHG parameter-dependent metric)**.** _If_ \(\theta:=\sqrt{\eta_x\eta_y}\|\mathcal{A}\|_\mathrm{op}<1\)_, then T_<sub>P</sub> _is firmly nonexpansive in_ \(\mathsf{G}_\mathrm{P}:=\left[\begin{array}{ c c }
\eta_x^{-1}\mathrm{Id} & \mathcal{A}^* \\
\mathcal{A} & \eta_y^{-1}I_m
\end{array}\right]\succ 0\)_, and one may take_ \(g_\mathrm{min}^\mathrm{P}=(1-\theta)/\mathrm{max}\{\eta_x,\eta_y\}\) _and_ \(g_\mathrm{max}^\mathrm{P}=(1+\theta)/\mathrm{min}\{\eta_x,\eta_y\}\) _in Theorem F.1._

_Proof._ The cross term obeys \(2|\langle\mathcal{A}X,\lambda\rangle|\le\theta(\eta_x^{-1}\|X\|_F^2+\eta_y^{-1}\|\lambda\|_2^2)\), which gives the metric bounds. Define the KKT operator \(\mathsf{F}_\mathrm{KKT}(X,\lambda):=\big(C-\mathcal{A}^*\lambda+N_{\mathbb{S}_+^p}\big(X)\), A_X-b_\(\big)\). It is monotone, because its linear part \((X,\lambda)\mapsto(-\mathcal{A}^*\lambda,\mathcal{A}X)\) is skew-adjoint and the normal-cone map \(N_{\mathbb{S}_+^p}\) is monotone. Direct substitution from the PDHG update gives \(0\in\mathsf{F}_\mathrm{KKT}(w^+)+\mathsf{G}_\mathrm{P}(w^+-w)\), the preconditioned proximal-point form of PDHG \[CP11, OV20\]; monotonicity applied to two such inclusions gives \(\|w^+-\bar{w}^+\|_{\mathsf{G}_\mathrm{P}}^2\le\langle w^+-\bar{w}^+,w-\bar{w}\rangle_{\mathsf{G}_\mathrm{P}}\), which is firm nonexpansiveness.

_Proof of Theorem 5.2._ Apply Theorem F.1 with \(\alpha=1/2\), Theorems F.3 and F.4. R-linear convergence of the slack follows from \(S^k=C-\mathcal{A}^*\lambda^k\) and Lipschitz continuity.

## G Genericity

Two clarifications on scope. First, genericity is asserted in the full coefficient space P_<sub>n</sub>_; a structured subfamily (sparse, low-degree, or symmetric) is measure-zero and needs its own relative-genericity argument. Second, full row rank of A_<sub>d</sub>_ is a representation choice made once and for all in Theorem B.1, not a property supplied by genericity. Under an arbitrary split in (6.1), the vectors _w<sub>A</sub>_ can be linearly dependent, and the kernel of _S_<sub>int</sub> can be strictly larger than span{_u_}. The convention stated in §6 is what makes them a basis of \(u^\perp\).

