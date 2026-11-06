where the \(\theta_j\) are the columns of _Q_<sub>-</sub> in (C.3). The identity holds since \((NI_N+\sigma S)^{-1}\) acts on _K_ as _N_<sup>-1</sup>_P<sub>K</sub>_ and on the eigenvector \(\theta_j\) of _S_ as \((N+\sigma s_j)^{-1}\). Note \(w\perp q\). The _VV_ block of (C.4) is \(Q_K\Pi_+(Q_K^\top HQ_K)Q_K^\top\), which vanishes when _K_={0}, i.e. when \(S\in\mathrm{ri}\mathcal{S}_\star\) by Theorem C.2. This proves (E.3), and (E.2) follows because at interior certificates \(X_\star-\sigma S\) is nonsingular, \(\Pi_+\) is differentiable there, and \(\delta'_\sigma=-\mathsf{P}\Pi'_+-\mathsf{P}^\perp\Pi'_-=-\big(\mathsf{P}\mathscr{J}_S+\mathsf{P}^\perp(\mathrm{Id}-\mathscr{J}_S)\big)=-\Psi_S\) by (C.6).

## E.3 Proof of the uniform modulus

_Proof of Theorem 4.2._ Suppose \(\Psi_S(H)=0\) and put _E_:=J_<sub>S</sub>(H_), _F_:=_H-E_. The two residual components vanish separately, so \(E\in\mathcal{T}_d\) and \(F\in\mathcal{R}_d\). But \(E\in\mathbb{S}(V)^\perp\) by construction, so the constant-diagonal identity (4.2) forces

\(E\in\mathcal{T}_d\cap\mathbb{S}(V)^\perp=\{0\}.\)

Multiplying _E_=0 by _q_ gives _h_<sub>00</sub>=0 and _w_=0; the inverse in (4.4) is nonsingular, so _P<sub>V</sub>Hq_=0, and with \(q^\top Hq=0\) this yields _Hq_=0, i.e. \(H\in\mathbb{S}(V)\). Then \(F=H\in\mathcal{R}_d\), so \(H\in\mathbb{S}(V)\cap\mathcal{R}_d=\mathcal{L}\). Conversely \(H\in\mathcal{L}\) gives J_<sub>S</sub>(H_)=0 and \(\mathsf{P}^\perp H=0\), so \(\Psi_S(H)=0\). This proves \(\mathrm{ker}(\Psi_S)=\mathcal{L}\); in particular \(\sigma_\mathrm{min}(\Psi_S|_{\mathcal{L}^\perp})>0\) for each _S_ by finite dimensionality. Continuity of \(S\mapsto\Psi_S\) (Appendix E.4 below) makes this least singular value continuous, and compactness of S_<sub>⋆</sub>_ gives \(\mu_\star>0\). Finally, on riS_<sub>⋆</sub>_ the extension coincides with the true derivative, which gives (4.5).

## E.4 Continuity and the compactness step

The inverse in (4.4) satisfies \(\|(NI_N+\sigma S)^{-1}\|_\mathrm{op}\le 1/N\) uniformly on S_<sub>⋆</sub>_, so the identity _B_<sup>-1</sup>-_A_<sup>-1</sup>=_B_<sup>-1</sup>(_A-B)A_<sup>-1</sup> makes \(S\mapsto\mathscr{J}_S\), hence \(S\mapsto\Psi_S\), Lipschitz on S_<sub>⋆</sub>_ in operator norm. The Lipschitz bound \(|\sigma_\mathrm{min}(B_1)-\sigma_\mathrm{min}(B_2)|\le\|B_1-B_2\|_\mathrm{op}\) (Appendix C) then makes \(S\mapsto\sigma_\mathrm{min}(\Psi_S|_{\mathcal{L}^\perp})\) continuous, which is the compactness step used in the proof of Theorem 4.2. The compactness argument applies to the continuous family \(\{\Psi_S\}_{S\in\mathcal{S}_\star}\) on the closed set S_<sub>⋆</sub>_; (E.2) identifies this family with the true derivative on riS_<sub>⋆</sub>_, which is all that (4.5) requires. In the language of Appendix C.2, \(\Psi_S\) is the primal-anchored continuous extension of the interior derivative; its dual twin, anchored at _S_<sub>sc</sub> with a varying primal optimum, is trivial here because X_<sub>⋆</sub>_ is a point.

## E.5 Tied minimizers: the error bound fails at full order

This section proves the claims of Theorem 4.4. Work at full order _d=n_, where _N_=2_<sup>n</sup>_ and the normalized evaluation vectors \(b_n(a)/\sqrt{N}\), \(a\in\{\pm 1\}^n\), form an orthonormal basis (Appendix G.1); let _Q_ be the orthogonal matrix with these columns and transform all data by _Q_. Every XOR-class matrix \(A_\Gamma\) is diagonal in this basis. Hence the feasible set becomes the diagonal matrices diag(_z_) with \(\sum_az_a=N\), and the moment matrix of a distribution \(\pi\) on the cube is \(\mathrm{diag}(N\pi)\). The objective becomes \(\sum_a\pi_af(a)\), and the data of §3 are

\(\mathcal{N}=\{\text{traceless diagonal matrices}\},\mathcal{R}=\{\text{off-diagonal symmetric matrices}\}\oplus\mathrm{span}\{I_N\},\)<br>
\(X_b=I_N,\widehat{C}=\mathrm{diag}\big(f(a)/N\big).\)

Let _f_ be nonconstant with minimizers \(a\neq b\) and a nonminimizer _c_, and write _f<sub>⋆</sub>_:=min_f_. Then X_<sub>⋆</sub>_ contains every \(\mathrm{diag}(N\pi)\) with \(\pi\) supported on the minimizers, so it is not a singleton. The matrix \(\bar{S}:=\mathrm{diag}\big((f(a')-f_\star)/N\big)_{a^\prime}\) is an optimal slack: \(\bar{S}-\widehat{C}=-(f_\star/N)I_N\in\mathcal{R}\), \(\bar{S}\unknown 0\), and \(\bar{S}\) vanishes on the minimizers. Finally, \(\big(X_\mathrm{sc},S_\mathrm{sc}\big):=\big(\mathrm{diag}(N\pi_\mathrm{u}),\bar{S}\big)\) with \(\pi_\mathrm{u}\) uniform on the minimizers is a strictly complementary pair. Thus Theorem 3.1 holds, with _U_ spanned by the minimizer coordinates and _V_ by the others.

