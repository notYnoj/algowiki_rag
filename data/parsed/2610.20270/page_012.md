_Remark_ 4.4 (Uniqueness cannot be dropped in the Boolean theorem). Theorem 3.2 needs no uniqueness, but Theorem 4.3 does. For _f(x_)=1-_x_<sub>1</sub> on \(\{\pm 1\}^2\) at full order, the two minimizers \((1,\pm 1)\) make both X_<sub>⋆</sub>_ and S_<sub>⋆</sub>_ segments, and a strictly complementary pair exists. Take the endpoint whose primal factor is the moment matrix of the point mass at the first minimizer. Along the cross direction that couples the second minimizer with a nonminimizer, the residual is of order \(2t^2/\sigma\) while the distance to Z_<sub>⋆</sub>_ is \(\sqrt{2}t\) (Appendix E.5). The dual identity fails there, and the direction lies in \(\mathcal{C}(\bar{Z})\backslash T_{\mathcal{Z}_\star}(\bar{Z})\). The same happens for every nonconstant full-order objective with two or more minimizers. Unique rank-one exactness rules out such directions.

## 5 Consequences for Splitting Methods

This section converts the error bound (3.9) into convergence rates for exact ADMM, exact sGS- ADMM, and fixed-step PDHG; details are in Appendix F.

### ADMM and exact sGS-ADMM share one shadow map.

Exact ADMM on the dual SDP with penalty \(\sigma>0\) and multiplier step \(\tau>0\), and its exact symmetric Gauss-Seidel variant \[GM76, CST17\], both reduce to one common recursion in the shadow coordinate \(Z^k:=\mathsf{P}^\perp X^k+X_b-\sigma\mathsf{P}S^k-\sigma\mathsf{P}^\perp C\). The recursion is \(Z^{k+1}=T_{\sigma,\tau}(Z^k)\) with \(T_{\sigma,\tau}-\mathrm{Id}=-\mathsf{D}_\tau(r^\|+r_\sigma^\perp)\) and \(\mathsf{D}_\tau:=\mathsf{P}+\tau\mathsf{P}^\perp\) (established in \[KY26a\]; re-derived in Appendix F.2). The multiplier step only rescales the two orthogonal residual components, so, with \(\delta_{\sigma,\tau}:=T_{\sigma,\tau}-\mathrm{Id}\),

\(\|\delta_{\sigma,\tau}(Z)\|_F\ge\mathrm{min}\{1,\tau\}\|\delta_\sigma(Z)\|_F\ge\mathrm{min}\{1,\tau\}c_\sigma\mathrm{dist}_F(Z,\mathcal{Z}_\star)\) (5.1)

throughout the tube of (3.9): the setwise error bound transfers verbatim. For \(0<\tau<2\), \(T_{\sigma,\tau}\) is \(\mathrm{max}\{1,\tau\}/2\)-averaged in the parameter-dependent metric \(\mathsf{G}_\tau:=\mathsf{P}+\tau^{-1}\mathsf{P}^\perp\), which is equivalent to the Frobenius metric (Theorem F.2, Appendix F.3; cf. \[KY26a\]).

### PDHG admits an endpoint chart.

Fixed-step PDHG \[CP11\] on (3.1), with state \(w=(X,\lambda)\) and steps \(\eta_x,\eta_y>0\), iterates \(X^+=\Pi_+(X-\eta_x(C-\mathcal{A}^*\lambda))\), \(\lambda^+=\lambda+\eta_y(b-\mathcal{A}(2X^+-X))\). Consider the affine change of variables \(\Phi(X,\lambda)=(Z,r)\) with \(Z:=X-\eta_x(C-\mathcal{A}^*\lambda)\) and _r_:=A_X-b_. It is a bijection sending the fixed-point set W_<sub>⋆</sub>_:=Fix_T_<sub>P</sub> of the PDHG map _T_<sub>P</sub> onto \(\mathcal{Z}_\star\times\{0\}\), with Z_<sub>⋆</sub>_ the canonical fixed-point set at parameter \(\sigma=\eta_x\). In this chart the PDHG residual _factors through the canonical one_: there is an explicit linear isomorphism \(\mathsf{L}_{\eta_x,\eta_y}:\mathcal{R}\times\mathcal{N}\times\mathbb{R}^m\rightarrow\mathbb{S}^p\times\mathbb{R}^m\) with

\(\Phi T_\mathsf{P}\Phi^{-1}(Z,r)-(Z,r)=\mathsf{L}_{\eta_x,\eta_y}\big(r^\|(Z),r_{\eta_x^\perp}^\perp(Z),r\big)\) (5.2)

(Theorem F.3). Invertibility of \(\mathsf{L}_{\eta_x,\eta_y}\) and of the chart converts (3.9) into a native setwise error bound for PDHG, and _T_<sub>P</sub> is firmly nonexpansive in the standard preconditioned metric whenever \(\eta_x\eta_y\|\mathcal{A}\|_\mathrm{op}^2<1\) \[CP11, OV20\] (Theorem F.4).

### From error bound to rates.

The passage from a setwise error bound to convergence rates is standard averaged-operator theory \[BC17\]. For an \(\alpha\)-averaged map in a metric equivalent to the Euclidean one, a setwise error bound on a neighborhood of the fixed-point set makes every orbit converge to a fixed point. The distance then contracts eventually Q-linearly in that metric, and the iterates converge R-linearly (Theorem F.1, stated and proved quantitatively in Appendix F.1).

**Corollary 5.1** (ADMM and sGS-ADMM)**.** _Under the hypotheses of Theorem 4.3 (or, abstractly, Theorem 3.1 plus any condition of Theorem 3.2), for every fixed_ \(\sigma>0\) _and_ \(0<\tau<2\)_, the shadow_<tbc>

