The two orthogonal equations \(r^\|=r_\sigma^\perp=0\) are equivalent to A_X=b_ and \(C-S\in\mathrm{ran}(\mathcal{A}^*)\), hence to KKT feasibility plus complementarity; surjectivity of A makes the multiplier unique. Conversely any KKT pair (_X,S_) gives the fixed point \(Z=X-\sigma S\).

**Lemma C.2** (Optimal product geometry)**.** _Under Theorem 3.1,_

\(\mathcal{X}_\star=(X_\mathrm{sc}+\mathcal{M})\cap\mathbb{S}_+(U),\mathcal{S}_\star=(S_\mathrm{sc}+\mathcal{L})\cap\mathbb{S}_+(V),\mathcal{Z}_\star=\mathrm{Fix}T_{\sigma,1}=\mathcal{X}_\star-\sigma\mathcal{S}_\star.\) (C.1)

_Each_ \(\bar{Z}\in\mathcal{Z}_\star\) _has a unique representation_ \(\bar{X}-\sigma\bar{S}\) _with_ \((\bar{X},\bar{S})\in\mathcal{X}_\star\times\mathcal{S}_\star\)_. Moreover_ span(X_<sub>⋆</sub>_-X_<sub>⋆</sub>_)=M, span(S_<sub>⋆</sub>_-S_<sub>⋆</sub>_)=L, aff \(\mathcal{Z}_\star=X_\mathrm{sc}-\sigma S_\mathrm{sc}+\mathcal{D}\)_, and_

\(\mathrm{ri}\mathcal{X}_\star=\{X\in\mathcal{X}_\star:X_{UU}\succ 0\},\mathrm{ri}\mathcal{S}_\star=\{S\in\mathcal{S}_\star:S_{VV}\succ 0\},\) (C.2)

_with the relative boundaries the complementary sets;_ \(\bar{X}-\sigma\bar{S}\in\mathrm{ri}\mathcal{Z}_\star\) _if and only if_ \(\bar{X}\in\mathrm{ri}\mathcal{X}_\star\) _and_ \(\bar{S}\in\mathrm{ri}\mathcal{S}_\star\)_. Finally,_ Z_<sub>⋆</sub> is compact and convex._

_Proof of Theorem C.2._ For any primal optimizer _X_ and optimal slack _S_, equality of the optimal values gives \(\langle X,S\rangle=0\), hence _XS=SX_=0 since both are PSD. Taking _S=S_<sub>sc</sub> shows \(\mathrm{ran}X\subseteq\mathrm{ker}S_\mathrm{sc}=U\), and taking _X=X_<sub>sc</sub> shows \(\mathrm{ran}S\subseteq\mathrm{ker}X_\mathrm{sc}=V\) . Primal feasibility gives \(X-X_\mathrm{sc}\in\mathcal{N}\) and dual feasibility gives \(S-S_\mathrm{sc}\in\mathcal{R}\), which proves the inclusions "\(\subseteq\)" in the first two identities of (C.1). Conversely, \(X\in(X_\mathrm{sc}+\mathcal{M})\cap\mathbb{S}_+(U)\) is feasible and complementary to _S_<sub>sc</sub>, hence optimal; symmetrically for _S_. Since _X_<sub>sc</sub> is positive definite on _U_, \(X_\mathrm{sc}\pm\varepsilon M\) is PSD for every \(M\in\mathcal{M}\) and small \(\varepsilon>0\), so span(X_<sub>⋆</sub>_-X_<sub>⋆</sub>_)=M; likewise for L.

Every pair \((X,S)\in\mathcal{X}_\star\times\mathcal{S}_\star\) has disjoint supports, so _XS_=0, \(\Pi_+(X-\sigma S)=X\), \(\Pi_-(X-\sigma S)=-\sigma S\), and \(\delta_\sigma(X-\sigma S)=0\) by Theorem C.1; conversely a fixed point decodes to a KKT pair, which is optimal. This proves the third identity. Compressing \(\bar{Z}\) to _U_ and _V_ recovers \(\bar{X}\) and \(-\sigma\bar{S}\), so the representation is unique. The map \((X,S)\mapsto X-\sigma S\) is a linear isomorphism from \(\mathbb{S}(U)\times\mathbb{S}(V)\) onto \(\mathbb{S}(U)\oplus\mathbb{S}(V)\). This gives the affine hull and reduces the relative-interior statement to the factors. A point of X_<sub>⋆</sub>_ positive definite on _U_ has a relative neighborhood inside X_<sub>⋆</sub>_. A point \(\bar{X}\) with singular \(\bar{X}_{UU}\) is not relatively interior: the line through \(\bar{X}\) and _X_<sub>sc</sub>, continued past \(\bar{X}\), leaves the PSD cone immediately. The same argument applies to S_<sub>⋆</sub>_ inside S<sub>+</sub>(_V_), which proves (C.2). Compactness and convexity of Z_<sub>⋆</sub>_ follow from those of the factors.

## C.2 The endpoint derivative formula

Fix an endpoint \(\bar{Z}=\bar{X}-\sigma\bar{S}\). Choose orthonormal eigenvector matrices _Q_<sub>+</sub> of \(\bar{X}\) on \(\mathrm{ran}\bar{X}\) (eigenvalues \(\xi_i>0\)) and _Q_<sub>-</sub> of \(\bar{S}\) on \(\mathrm{ran}\bar{S}\) (eigenvalues _s<sub>j</sub>\>_0). Choose also an orthonormal basis _Q<sub>K</sub>_ of the zero eigenspace \(K:=K_\bar{X}\oplus K_\bar{S}\) of \(\bar{Z}\). The frame \(Q:=[Q_+Q_KQ_-]\) is orthogonal, and

\(Q^\top\bar{Z}Q=\mathrm{diag}(\Lambda_+,0,-\sigma\Lambda_-),\widetilde{H}:=Q^\top HQ,\Lambda_+=\mathrm{diag}(\xi_i)\succ 0,\Lambda_-=\mathrm{diag}(s_j)\succ 0.\) (C.3)

In this chart the directional derivative of the PSD projection takes the classical form \[SS02\]

\(Q^\top\Pi'_+(\bar{Z};H)Q=\left[\begin{array}{ c c c }
\widetilde{H}_{++} & \widetilde{H}_{+K} & \Omega\circ\widetilde{H}_{+-} \\
\widetilde{H}_{K+} & \Pi_+(\widetilde{H}_{KK}) & 0 \\
(\Omega\circ\widetilde{H}_{+-})^\top & 0 & 0
\end{array}\right],\Omega_{ij}:=\frac{\xi_i}{\xi_i+\sigma s_j}\in(0,1).\) (C.4)

Here \(\Pi'_-(\bar{Z};H)=H-\Pi'_+(\bar{Z};H)\) and \(\circ\) is the entrywise product. The entries of \(\Omega\) are the divided differences of \(t\mapsto\mathrm{max}\{t,0\}\) across the nonzero spectral blocks. The +_K_ block carries the divided difference \(\xi_i/(\xi_i-0)=1\), and the _K_- block carries \(0/(0+\sigma s_j)=0\). The zero block contributes its<tbc>

