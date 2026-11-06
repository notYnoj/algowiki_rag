<tbc>by compactness, (D.7), and (D.9). The fixed anchors now give \(a_S\|(E_k)_{VV}\|_F\le\langle(E_k)_{VV},S_\mathrm{sc}|_V\rangle=\langle E_k,S_\mathrm{sc}\rangle\rightarrow 0\) and \(a_X\|(F_k)_{UU}\|_F\le-\langle(F_k)_{UU},X_\mathrm{sc}|_U\rangle=-\langle F_k,X_\mathrm{sc}\rangle\rightarrow 0\), using \(\mathrm{tr}A\ge\|A\|_F\) for PSD _A_; hence

\((E_k)_{VV}\rightarrow 0,(F_k)_{UU}\rightarrow 0,E_{VV}=0,F_{UU}=0.\) (D.10)

_Step 2: annihilation without spectral gaps._ All of \(X_k,S_k,\bar{X}_k,\bar{S}_k\) are bounded. Theorem C.6 and (D.9) give \(\|X_k\bar{S}_k\|_F^2=o(t_k^2)\) and \(\|\bar{X}_kS_k\|_F^2=o(t_k^2)\), and \(\bar{X}_k\bar{S}_k=0\) turns these into \(E_k\bar{S}_k=X_k\bar{S}_k/t_k\rightarrow 0\) and \(\bar{X}_kF_k=-\sigma\bar{X}_kS_k/t_k\rightarrow 0\). In the limit,

\(E\bar{S}=0,\bar{X}F=0.\) (D.11)

No lower bound on the positive eigenvalues of \(\bar{X}_k\) or \(\bar{S}_k\) has been used.

_Step 3: the limits lie in the direction spaces._ By (D.7), (D.10), and (D.11), \(E\in\mathcal{N}\) with _E<sub>VV</sub>_=0 and \(E\bar{S}=0\), and \(F\in\mathcal{R}\) with _F<sub>UU</sub>_=0 and \(\bar{X}F=0\). The identities (3.8) at \(\bar{S}\) and \(\bar{X}\) give \(E\in\mathcal{M}\), \(F\in\mathcal{L}\), hence \(H=E+F\in\mathcal{D}\).

_Step 4: normality contradicts the secant signs._ Choose any decomposition _H<sub>k</sub>=Y<sub>k</sub>-W<sub>U,k</sub>+W<sub>V,k</sub>_ as in (C.10); all three sequences are bounded by Theorem D.2. Since \(H_k\rightarrow H\in\mathcal{D}\) and \(Y_k\perp\mathcal{D}\), \(\langle H_k,Y_k\rangle=\langle H_k-H,Y_k\rangle\rightarrow 0\). The kernel supports give \(\bar{X}_kW_{U,k}=0\) and \(\bar{S}_kW_{V,k}=0\). By (D.6) and positivity,<tbc>

\(\langle E_k,W_{U,k}\rangle=t_k^{-1}\langle X_k,W_{U,k}\rangle\ge 0,\langle F_k,W_{V,k}\rangle=-\sigma t_k^{-1}\langle S_k,W_{V,k}\rangle\le 0.\)

<tbc>The cross pairings vanish by (D.10): \(|\langle F_k,W_{U,k}\rangle|=|\langle(F_k)_{UU},(W_{U,k})_{UU}\rangle|\rightarrow 0\) and \(|\langle E_k,W_{V,k}\rangle|=|\langle(E_k)_{VV},(W_{V,k})_{VV}\rangle|\rightarrow 0\). Therefore

\(1=\|H_k\|_F^2=\langle H_k,Y_k\rangle-\langle H_k,W_{U,k}\rangle+\langle H_k,W_{V,k}\rangle\le\langle H_k,Y_k\rangle-\langle F_k,W_{U,k}\rangle+\langle E_k,W_{V,k}\rangle\longrightarrow 0,\)

a contradiction.

## D.5 Normal modulus and exact linearization: (iii)\(\Rightarrow\)(iv)\(\Rightarrow\)(i) and (iii)\(\Rightarrow\)(v)\(\Rightarrow\)(ii)

_Proof of_ (iii)\(\Rightarrow\)(iv)\(\Rightarrow\)(i). For \(\bar{Z}\in\mathcal{Z}_\star\) and a unit \(H\in N_{\mathcal{Z}_\star}(\bar{Z})\), the projection characterization of closed convex sets gives \(\mathrm{dist}_F(\bar{Z}+tH,\mathcal{Z}_\star)=t\) for \(t\ge 0\). For \(0<t\le t_\sigma\), (3.9) and \(\delta_\sigma(\bar{Z})=0\) give \(\|\delta_\sigma(\bar{Z}+tH)\|_F/t\ge c_\sigma\), and directional differentiability lets \(t\downarrow 0\): \(\|\delta'_\sigma(\bar{Z};H)\|_F\ge c_\sigma\), so \(\mu_\mathrm{nor}\ge c_\sigma>0\). On ri Z_<sub>⋆</sub>_ the normal cone is \(\mathcal{D}^\perp\) (Theorem C.4), so \(\mu_\mathrm{ri}\ge\mu_\mathrm{nor}>0\).

_Proof of_ (iii)\(\Rightarrow\)(v). We prove \(\mathcal{C}(\bar{Z})=T_{\mathcal{Z}_\star}(\bar{Z})\) at _every_ \(\bar{Z}\in\mathcal{Z}_\star\). The inclusion \(T_{\mathcal{Z}_\star}(\bar{Z})\subseteq\mathcal{C}(\bar{Z})\) needs no hypothesis. Let \(t_k\downarrow 0\) and \(H_k\rightarrow H\) with \(\bar{Z}+t_kH_k\in\mathcal{Z}_\star\). Since \(\delta_\sigma\) is Lipschitz with some constant \(L_\sigma\) and vanishes on Z_<sub>⋆</sub>_, \(\|\delta_\sigma(\bar{Z}+t_kH)\|_F\le L_\sigma t_k\|H-H_k\|_F=o(t_k)\). The directional derivative exists, so it must be zero. Conversely, if \(\delta'_\sigma(\bar{Z};H)=0\) then \(\|\delta_\sigma(\bar{Z}+tH)\|_F=o(t)\). For small _t_, \(\mathrm{dist}_F(\bar{Z}+tH,\mathcal{Z}_\star)\le t\|H\|_F\le t_\sigma\), so (3.9) applies and gives \(\mathrm{dist}_F(\bar{Z}+tH,\mathcal{Z}_\star)\le c_\sigma^{-1}\|\delta_\sigma(\bar{Z}+tH)\|_F=o(t)\). With _Z<sub>t</sub>_ a nearest point, \((Z_t-\bar{Z})/t\rightarrow H\), so \(H\in T_{\mathcal{Z}_\star}(\bar{Z})\).

_Proof of_ (v)\(\Rightarrow\)(ii). By Theorem D.1 the identities hold at interior factors, so fix \(\bar{S}\in\mathrm{rb}\mathcal{S}_\star\) and \(E\in\mathcal{N}\) with _E<sub>VV</sub>_=0 and \(E\bar{S}=0\). The primal-anchored endpoint \(\bar{Z}:=X_\mathrm{sc}-\sigma\bar{S}\) lies in robZ_<sub>⋆</sub>_ (Theorem C.2). Apply the coarse form (C.7) in case (b). The _UU_ block of \(\Pi'_+(\bar{Z};E)\) is _E<sub>UU</sub>_. The _VV_ block is the positive part of the \(K_\bar{S}K_\bar{S}\) block of _E<sub>VV</sub>_=0, hence zero. The cross block _Y_ solves \(X_\mathrm{sc}|_UY+\sigma Y\bar{S}_{VV}=X_\mathrm{sc}|_UE_{UV}\); since \(E_{UV}\bar{S}_{VV}=0\), the unique solution is _Y=E<sub>UV</sub>_. Thus \(\Pi'_+(\bar{Z};E)=E\), and \(\delta'_\sigma(\bar{Z};E)=-\mathsf{P}E=0\) because \(E\in\mathcal{N}\). Hence \(E\in\mathcal{C}(\bar{Z})=T_{\mathcal{Z}_\star}(\bar{Z})\subseteq\mathcal{D}\), and _E<sub>VV</sub>_=0 gives \(E\in\mathcal{M}\).

