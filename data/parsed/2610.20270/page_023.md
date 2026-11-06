_Proof._ Let \(\bar{S}\in\mathrm{ri}\mathcal{S}_\star\), so \(\bar{S}_{VV}\succ 0\) by (C.2). If \(E\in\mathcal{N}\) satisfies _E<sub>VV</sub>_=0 and \(E\bar{S}=0\), write its blocks as \(\left[\begin{array}{ c }
A \\
B^\top \\
0
\end{array}\right]\); the _UV_ block of \(E\bar{S}=0\) reads \(B\bar{S}_{VV}=0\), so _B_=0 and \(E\in\mathbb{S}(U)\cap\mathcal{N}=\mathcal{M}\). The inclusion of M in the left side is immediate, since elements of M are supported on _U_ and annihilate every matrix supported on _V_ . The dual statement is symmetric, with \(\bar{X}_{UU}\succ 0\).

Now let \(\bar{Z}=\bar{X}-\sigma\bar{S}\in\mathrm{ri}\mathcal{Z}_\star\) and \(H\in\mathcal{C}(\bar{Z})\). Put \(E:=J_{\bar{X},\bar{S}}(H)\) and _F_:=_H-E_. The two terms of (C.6) lie in the orthogonal spaces R and N, so \(\delta'_\sigma(\bar{Z};H)=0\) gives P_E_=0 and \(\mathsf{P}^\perp F=0\), hence \(E\in\mathcal{N}\), \(F\in\mathcal{R}\), and \(\langle E,F\rangle=0\). By (C.5) at an interior endpoint, where every weight \(\Omega_{ij}\) lies strictly between 0 and 1, this forces _H<sub>UV</sub>_=0; then \(E=P_UHP_U\in\mathcal{M}\) and \(F=P_VHP_V\in\mathcal{L}\) by the coarse form (C.7), so \(H\in\mathcal{D}\). Conversely, for \(M\in\mathcal{M}\) and \(\Lambda\in\mathcal{L}\) one has \(J_{\bar{X},\bar{S}}(M+\Lambda)=M\) (the cross block is zero and the _VV_ block is killed), so \(\delta'_\sigma(\bar{Z};M+\Lambda)=-\mathsf{P}M-\mathsf{P}^\perp\Lambda=0\). Finally, at a relative-interior point of the convex set Z_<sub>⋆</sub>_ the tangent cone is the direction space D (Theorem C.2).

Because \(\delta'_\sigma(\bar{Z};\cdot)\) is linear at interior endpoints and vanishes on D, condition (i) implies the quotient bound

\(\|\delta'_\sigma(\bar{Z};H)\|_F\ge\mu_\mathrm{ri}\mathrm{dist}_F(H,\mathcal{D})(\bar{Z}\in\mathrm{ri}\mathcal{Z}_\star,H\in\mathbb{S}^p),\) (D.3)

obtained by applying the definition of \(\mu_\mathrm{ri}\) to the component of _H_ orthogonal to D.

## D.2 Uniformly bounded normal decompositions

**Lemma D.2** (Uniformly bounded normal decompositions)**.** _For every endpoint_ \(\bar{Z}=\bar{X}-\sigma\bar{S}\)_, every_ \(H\in N_{\mathcal{Z}_\star}(\bar{Z})\)_, and every decomposition H=Y-W<sub>U</sub>+W<sub>V</sub> with_ \(Y\in\mathcal{D}^\perp\), \(W_U\in\mathcal{K}(\bar{X})\), \(W_V\in\mathcal{K}(\bar{S})\) _as in_ (C.10),

\(\|W_U\|_F\le\frac{R_X}{a_X}\|H\|_F,\|W_V\|_F\le\frac{R_S}{a_S}\|H\|_F,\|Y\|_F\le\big(1+\frac{R_X}{a_X}+\frac{R_S}{a_S}\big)\|H\|_F.\) (D.4)

_The three summands need not be orthogonal, and the decomposition need not be unique; the bounds hold for every choice._

_Proof._ Since \(W_U\unknown 0\), \(\mathrm{tr}W_U\ge\|W_U\|_F\). We claim

\(a_X\|W_U\|_F\le a_X\mathrm{tr}W_U\le\langle W_U,X_\mathrm{sc}\rangle=\langle W_U,X_\mathrm{sc}-\bar{X}\rangle\)<br>
\(=-\langle H,X_\mathrm{sc}-\bar{X}\rangle\le\|H\|_F\|X_\mathrm{sc}-\bar{X}\|_F\le R_X\|H\|_F.\)

The second inequality holds because _W<sub>U</sub>_ is supported on _U_ and \(X_\mathrm{sc}\unknown a_XP_U\) (Theorem C.7, as ran_X_<sub>sc</sub>=_U_). The first equality uses \(\bar{X}W_U=0\). The second equality uses \(Y\perp\mathcal{D}\unknown X_\mathrm{sc}-\bar{X}\), and that _W<sub>V</sub>_ is supported on _V_ while \(X_\mathrm{sc}-\bar{X}\) is supported on _U_. Symmetrically, \(S_\mathrm{sc}\unknown a_SP_V\), \(\bar{S}W_V=0\), and \(S_\mathrm{sc}-\bar{S}\in\mathcal{L}\subseteq\mathcal{D}\) give \(a_S\|W_V\|_F\le\langle W_V,S_\mathrm{sc}-\bar{S}\rangle=\langle H,S_\mathrm{sc}-\bar{S}\rangle\le R_S\|H\|_F\); the sign differs because the fixed-point variable carries \(-\sigma S\). The bound on _Y=H+W<sub>U</sub>-W<sub>V</sub>_ follows by the triangle inequality.

## D.3 The interior modulus forces the kernel identities: (i)\(\Rightarrow\)(ii)

_Proof of_ (i)\(\Rightarrow\)(ii). We prove both identities at _every_ optimal factor, which is stronger than required. The inclusions "\(\supseteq\)" are immediate as in Theorem D.1.

_Primal identity._ Fix \(\bar{S}\in\mathcal{S}_\star\) and take \(E\in\mathcal{N}\) with _E<sub>VV</sub>_=0 and \(E\bar{S}=0\); write _B_:=_E<sub>UV</sub>_, so \(B\bar{S}_{VV}=0\). For \(0<\varepsilon\le 1\) set \(\bar{S}_\varepsilon:=(1-\varepsilon)\bar{S}+\varepsilon S_\mathrm{sc}\) and \(Z_\varepsilon:=X_\mathrm{sc}-\sigma\bar{S}_\varepsilon\). Then \(\bar{S}_\varepsilon\unknown\varepsilon a_SP_V\) is positive definite on _V_ , so \(Z_\varepsilon\in\mathrm{ri}\mathcal{Z}_\star\) by Theorem C.2. Let \(Y_\varepsilon\) be the cross block of \(J_{X_\mathrm{sc},\bar{S}_\varepsilon}(E)\), which<tbc>

