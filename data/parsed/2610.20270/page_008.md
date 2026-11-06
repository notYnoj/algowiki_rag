properties of the residual field equivalent, among them a setwise error bound. §4 verifies one of them and inherits the other four.

## 3.1 The canonical residual and the two-sided geometry

Consider the primal-dual pair

\((\mathsf{P})\mathrm{min}_{X\unknown 0}\langle C,X\rangle\mathrm{s}.\mathrm{t}.\mathcal{A}X=b,\)<br>
\((\mathsf{D})\mathrm{max}_{\lambda\in\mathbb{R}^m,S\unknown 0}b^\top\lambda\mathrm{s}.\mathrm{t}.\mathcal{A}^*\lambda+S=C,\) (3.1)

with \(\mathcal{A}:\mathbb{S}^p\rightarrow\mathbb{R}^m\) surjective; in the dual, only the slack _S_ is constrained to be PSD. Set R:=ran(A<sup>∗</sup>), \(\mathcal{N}:=\mathrm{ker}(\mathcal{A})=\mathcal{R}^\perp\), and A<sup>†</sup>:=A<sup>∗</sup>(AA<sup>∗</sup>)<sup>-1</sup>, and let P:=A<sup>†</sup>A and \(\mathsf{P}^\perp:=\mathrm{Id}-\mathsf{P}\) be the orthogonal projectors onto R and N on the _matrix_ space S_<sup>p</sup>_; put _X<sub>b</sub>_:=A<sup>†</sup>_b_. For fixed \(\sigma>0\), define the two orthogonal residual components and the canonical Douglas-Rachford (DR) map

\(r^\|(Z):=\mathsf{P}\big(\Pi_+(Z)-X_b\big),r_\sigma^\perp(Z):=\mathsf{P}^\perp\big(\Pi_-(Z)+\sigma C\big),\delta_\sigma:=-r^\|-r_\sigma^\perp,T_{\sigma,1}:=\mathrm{Id}+\delta_\sigma.\) (3.2)

This is the DR map (with \(\Pi_+\) applied before the affine step) for \(F(X)=\langle C,X\rangle+\iota_{\{\mathcal{A}X=b\}}(X)\) and \(G=\iota_{\mathbb{S}_+^p}\); its fixed points are \(X-\sigma S\) over all KKT pairs, with \(X=\Pi_+(Z)\) and \(S=-\sigma^{-1}\Pi_-(Z)\) (Theorem C.1, Appendix C.1).

**Assumption 3.1** (Two-sided optimal geometry)**.** _The primal optimal set_ X_<sub>⋆</sub> and the optimal slack set_ S_<sub>⋆</sub> are nonempty and compact, and there is an optimal pair_ (_X_<sub>sc</sub>_,S_<sub>sc</sub>) _with X_<sub>sc</sub>_S_<sub>sc</sub>=0, \(X_\mathrm{sc}+S_\mathrm{sc}\succ 0\)_, and_ \(1\le\mathrm{rank}X_\mathrm{sc}<p\).

We call (_X_<sub>sc</sub>_,S_<sub>sc</sub>) the _anchor pair_, fixed once and for all; the uniform spectral estimates below rest on it, never on the moving optima. Set _U_:=ran_X_<sub>sc</sub> and _V_:=ran_S_<sub>sc</sub>=_U_<sup>\`</sup>, let _P<sub>U</sub>_, _P<sub>V</sub>_ be the orthogonal projectors onto them, write S(_U_), S(_V_) for the symmetric matrices supported on _U_, _V_ , and define the primal and dual direction spaces and their sum

\(\mathcal{M}:=\mathcal{N}\cap\mathbb{S}(U),\mathcal{L}:=\mathcal{R}\cap\mathbb{S}(V),\mathcal{D}:=\mathcal{M}\oplus\mathcal{L}.\) (3.3)

Every optimal _X_ is supported on _U_ and every optimal _S_ on _V_ , so (Theorem C.2, Appendix C.1)

\(\mathcal{X}_\star=(X_\mathrm{sc}+\mathcal{M})\cap\mathbb{S}_+(U),\mathcal{S}_\star=(S_\mathrm{sc}+\mathcal{L})\cap\mathbb{S}_+(V),\mathcal{Z}_\star=\mathrm{Fix}T_{\sigma,1}=\mathcal{X}_\star-\sigma\mathcal{S}_\star.\) (3.4)

We call the points of Z_<sub>⋆</sub> endpoints_, where convergent runs end. Each endpoint \(\bar{Z}\) has a unique representation \(\bar{X}-\sigma\bar{S}\), and we call \(\bar{X}\) and \(\bar{S}\) its two _factors_. Also aff \(\mathcal{Z}_\star=X_\mathrm{sc}-\sigma S_\mathrm{sc}+\mathcal{D}\), and \(\bar{Z}\in\mathrm{ri}\mathcal{Z}_\star\) exactly when \(\bar{X}\) is positive definite on _U_ and \(\bar{S}\) on _V_ . In words, Z_<sub>⋆</sub>_ is a product of two PSD slices, and its relative boundary consists of the endpoints at which a factor loses rank. When X_<sub>⋆</sub>_={_X<sub>⋆</sub>_} is a singleton, M={0} and D=L, which is the Boolean situation of §2.

## 3.2 Endpoints, derivatives, and the stall cone

Fix an endpoint \(\bar{Z}=\bar{X}-\sigma\bar{S}\) and set \(K_\bar{X}:=\mathrm{ker}\bar{X}\cap U\) and \(K_\bar{S}:=\mathrm{ker}\bar{S}\cap V\) , the subspaces on which the two factors have lost rank; both are {0} exactly on riZ_<sub>⋆</sub>_. Only these kernels move with the endpoint; _U_ and _V_ stay fixed, and no continuity of eigenbases in the endpoint is ever assumed. At an interior endpoint the PSD projection is differentiable, and in the fixed \(U\oplus V\) blocks its derivative \(J_{\bar{X},\bar{S}}(H):=\Pi'_+(\bar{Z};H)\) keeps the _UU_ block, kills the _VV_ block, and replaces the cross block by the solution _Y_ of the Sylvester equation

\(\bar{X}Y+\sigma Y\bar{S}Y=\bar{X}H_{UV}\) (3.5)

