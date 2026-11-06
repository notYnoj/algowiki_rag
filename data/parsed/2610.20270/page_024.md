by (C.7) solves \(X_\mathrm{sc}|_UY_\varepsilon+\sigma Y_\varepsilon(\bar{S}_\varepsilon)_{VV}=X_\mathrm{sc}|_UB\). Subtracting the same expression evaluated at _B_ and using \(B\bar{S}_{VV}=0\) gives the exact identity

\(X_\mathrm{sc}|_U\left(Y_\varepsilon-B\right)+\sigma(Y_\varepsilon-B)(\bar{S}_\varepsilon)_{VV}=-\sigma\varepsilon BS_\mathrm{sc}|_V.\) (D.5)

Pairing with \(Y_\varepsilon-B\) and using \((\bar{S}_\varepsilon)_{VV}\unknown 0\) yields \(a_X\|Y_\varepsilon-B\|_F^2\le\sigma\varepsilon\|Y_\varepsilon-B\|_F\|BS_\mathrm{sc}|_V\|_F\), so \(\|Y_\varepsilon-B\|_F\le(\sigma\varepsilon/a_X)\|BS_\mathrm{sc}|_V\|_F\rightarrow 0\) and \(J_{X_\mathrm{sc},\bar{S}_\varepsilon}(E)\rightarrow E\) (its _UU_ block is _E<sub>UU</sub>_ and its _VV_ block is zero, as is _E<sub>VV</sub>_). Since P_E_=0, (C.6) becomes \(\delta'_\sigma(Z_\varepsilon;E)=(\mathsf{P}^\perp-\mathsf{P})\big(J_{X_\mathrm{sc},\bar{S}_\varepsilon}(E)-E\big)\), and \(\mathsf{P}^\perp-\mathsf{P}\) is an orthogonal reflection, so \(\|\delta'_\sigma(Z_\varepsilon;E)\|_F=\|J_{X_\mathrm{sc},\bar{S}_\varepsilon}(E)-E\|_F\rightarrow 0\). The quotient bound (D.3) forces dist_<sub>F</sub>(E,_D)=0. Writing \(E=M+\Lambda\) with \(M\in\mathcal{M}\), \(\Lambda\in\mathcal{L}\), the condition _E<sub>VV</sub>_=0 gives \(\Lambda=0\), so \(E\in\mathcal{M}\).

_Dual identity._ Fix \(\bar{X}\in\mathcal{X}_\star\) and take \(F\in\mathcal{R}\) with _F<sub>UU</sub>_=0 and \(\bar{X}F=0\); write _B_:=_F<sub>UV</sub>_, so \(\bar{X}_{UU}B=0\). Set \(X_\varepsilon:=(1-\varepsilon)\bar{X}+\varepsilon X_\mathrm{sc}\) and \(Z_\varepsilon:=X_\varepsilon-\sigma S_\mathrm{sc}\in\mathrm{ri}\mathcal{Z}_\star\). The cross block \(Y_\varepsilon\) of \(J_{X_\varepsilon,S_\mathrm{sc}}(F)\) solves \((X_\varepsilon)_{UU}Y_\varepsilon+\sigma Y_\varepsilon S_\mathrm{sc}|_V=(X_\varepsilon)_{UU}B=\varepsilon X_\mathrm{sc}|_UB\), so Theorem C.3(b) gives \(\|Y_\varepsilon\|_F\le\varepsilon\|X_\mathrm{sc}|_UB\|_F/(\sigma a_S)\rightarrow 0\), and \(J_{X_\varepsilon,S_\mathrm{sc}}(F)\rightarrow 0\) because its _UU_ block _F<sub>UU</sub>_ and its _VV_ block vanish identically. Since \(\mathsf{P}^\perp F=0\), \(\delta'_\sigma(Z_\varepsilon;F)=-(\mathsf{P}-\mathsf{P}^\perp)J_{X_\varepsilon,S_\mathrm{sc}}(F)\rightarrow 0\), and (D.3) gives \(F\in\mathcal{D}\); the condition _F<sub>UU</sub>_=0 kills the M component, so \(F\in\mathcal{L}\).

## D.4 The kernel identities force the error bound: (ii)\(\Rightarrow\)(iii)

_Proof of_ (ii)\(\Rightarrow\)(iii). By Theorem D.1, (ii) gives both identities at every optimal factor. Suppose (3.9) fails. Since \(\delta_\sigma\) vanishes on Z_<sub>⋆</sub>_, there are \(Z_k\notin\mathcal{Z}_\star\) with \(0<t_k:=\mathrm{dist}_F(Z_k,\mathcal{Z}_\star)\le 1/k\) and \(\|\delta_\sigma(Z_k)\|_F/t_k<1/k\). Let \(\bar{Z}_k=\bar{X}_k-\sigma\bar{S}_k\) be the point of the compact convex set Z_<sub>⋆</sub>_ nearest to _Z<sub>k</sub>_, and put \(H_k:=(Z_k-\bar{Z}_k)/t_k\), so that \(\|H_k\|_F=1\), \(H_k\in N_{\mathcal{Z}_\star}(\bar{Z}_k)\), and \(Z_k=\bar{Z}_k+t_kH_k\). Define the _exact_ projections and secants

\(X_k:=\Pi_+(Z_k),S_k:=-\sigma^{-1}\Pi_-(Z_k),E_k:=\frac{X_k-\bar{X}_k}{t_k},F_k:=-\sigma\frac{S_k-\bar{S}_k}{t_k}.\) (D.6)

The Moreau decomposition gives _E<sub>k</sub>+F<sub>k</sub>=H<sub>k</sub>_, and nonexpansiveness of \(\Pi_\pm\) gives \(\|E_k\|_F,\|F_k\|_F\le 1\). After a subsequence, \((\bar{X}_k,\bar{S}_k,E_k,F_k,H_k)\rightarrow(\bar{X},\bar{S},E,F,H)\) with _E+F=H_ and \(\|H\|_F=1\). These are moving-base secants; no derivative at a limiting endpoint is used anywhere below.

_Residual components and the energy identity._ Since \(\delta_\sigma(\bar{Z}_k)=0\), (3.2) gives \(\delta_\sigma(Z_k)/t_k=-\mathsf{P}E_k-\mathsf{P}^\perp F_k\), whose two terms are orthogonal; hence<tbc>

\(\mathsf{P}E_k\rightarrow 0,\mathsf{P}^\perp F_k\rightarrow 0,E\in\mathcal{N},F\in\mathcal{R},\) (D.7)

<tbc>and \(\langle E_k,F_k\rangle=\langle\mathsf{P}E_k,F_k\rangle+\langle E_k,\mathsf{P}^\perp F_k\rangle\rightarrow 0\). Exact complementarity _X<sub>k</sub>S<sub>k</sub>_=0 and \(\bar{X}_k\bar{S}_k=0\), expanded through (D.6), yields the energy identity<tbc>

\(\langle E_k,F_k\rangle=\frac{\sigma}{t_k^2}\big(\langle X_k,\bar{S}_k\rangle+\langle\bar{X}_k,S_k\rangle\big)\ge 0;\) (D.8)

<tbc>both of its terms are nonnegative, so<tbc>

\(\langle X_k,\bar{S}_k\rangle=o(t_k^2),\langle\bar{X}_k,S_k\rangle=o(t_k^2).\) (D.9)

<tbc>_Step 1: the wrong-face diagonal blocks vanish._ Optimal primal matrices are supported on _U_ and optimal slacks on _V_ , so \((E_k)_{VV}=(X_k)_{VV}/t_k\unknown 0\) and \((F_k)_{UU}=-\sigma(S_k)_{UU}/t_k\unknown 0\). Since \(S_\mathrm{sc}-\bar{S}_k\in\mathcal{L}\subseteq\mathcal{R}\) and \(X_\mathrm{sc}-\bar{X}_k\in\mathcal{M}\subseteq\mathcal{N}\),<tbc>

\(\langle E_k,S_\mathrm{sc}\rangle=\langle\mathsf{P}E_k,S_\mathrm{sc}-\bar{S}_k\rangle+\frac{\langle X_k,\bar{S}_k\rangle}{t_k}\rightarrow 0,\langle F_k,X_\mathrm{sc}\rangle=\langle\mathsf{P}^\perp F_k,X_\mathrm{sc}-\bar{X}_k\rangle-\frac{\sigma\langle\bar{X}_k,S_k\rangle}{t_k}\rightarrow 0,\)

