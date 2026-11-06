<tbc>and by (36) and (33),

\(\left|\left|\Psi-\chi_h\right|\right|\le\left|\left|\bar{\Psi}-I_h\bar{\Psi}\right|\right|+\left|\left|\Psi-\bar{\Psi}\right|\right|-v_h\right|\right|\le C_\bar{\Psi}h+C_Ah^{s-1}\left|\left|\Psi-\bar{\Psi}\right|\right|_{H^s(D_p\cup D_s)}\le Ch^{s-1}.\)

_L_<sup>2</sup> _estimate._ Write \(e:=\Psi-\Psi_h=(\bar{\Psi}-I_h\bar{\Psi})+e^0\) with \(e^0:=(\Psi-\bar{\Psi})-(\Psi_h-I_h\bar{\Psi})\in H_0^1(\Omega)\). By (36), \(\left|\left|\bar{\Psi}-I_h\bar{\Psi}\right|\right|_{0,2}\le Ch^2\), so it suffices to bound \(\left|\left|\left|e^0\right|\right|\right|_{0,2}\). Let \(w\in H_0^1(\Omega)\) solve the dual problem (30) with _c_=0 and _f=e_<sup>0</sup>, and let \(w_h\in V_h^0\) be its Galerkin approximation, so that \(\left|\left|\left|w-w_h\right|\right|\right|\le Ch^{\sigma-1}\left|\left|e^0\right|\right|\right|_{0,2}\) by Lemma 4.3 and Assumption 4.1(ii). Using (37) in the form \(a(e^0,w_h)=a(e,w_h)-a(\bar{\Psi}-I_h\bar{\Psi},w_h)=-a(\bar{\Psi}-I_h\bar{\Psi},w_h)\), we obtain<tbc>

\(\left|\left|\left|e^0\right|\right|\right|_{0,2}^2=a(e^0,w)=a(e^0,w-w_h)-a(\bar{\Psi}-I_h\bar{\Psi},w_h-w)-a(\bar{\Psi}-I_h\bar{\Psi},w).\) (38)

<tbc>The first two terms are bounded by \(C\big(\left|\left|\left|e^0\right|\right|\right|+\left|\left|\bar{\Psi}-I_h\bar{\Psi}\right|\right|\right)\left|\left|\left|\Psi w-w_h\right|\right|\right|\le Ch^{s-1}h^{\sigma-1}\left|\left|\left|e^0\right|\right|\right|_{0,2}\), where \(\left|\left|\left|e^0\right|\right|\right|\le\left|\left|\left|\Psi e\right|\right|+\left|\left|\bar{\Psi}-I_h\bar{\Psi}\right|\right|\le Ch^{s-1}\) by the energy estimate. For the last term we integrate by parts in _D<sub>p</sub>_ and _D<sub>s</sub>_: since \(-\nabla\cdot(\epsilon\nabla w)=e^0\) in \(D_p\cup D_s\) and the flux \(\epsilon\partial w/\partial\mathbf{n}\) is continuous across \(\Gamma\), while \(\bar{\Psi}-I_h\bar{\Psi}\) vanishes near \(\Gamma\),

\(a(\bar{\Psi}-I_h\bar{\Psi},w)=\big(\bar{\Psi}-I_h\bar{\Psi},e^0\big)+\epsilon_s\int_{\partial\Omega}(\bar{\Psi}-I_h\bar{\Psi})\frac{\partial w}{\partial\mathbf{n}}\mathrm{d}s.\)

The volume term is bounded by \(Ch^2\left|\left|\left|e^0\right|\right|\right|_{0,2}\) by (36). For the boundary term, if \(\sigma>3/2\) the trace \(\partial w/\partial\mathbf{n}\in L^2(\partial\Omega)\) satisfies \(\left|\left|\left|\partial w/\partial\mathbf{n}\right|\right|\right|_{0,2,\partial\Omega}\le C\left|\left|\left|w\right|\right|\right|_{H^\sigma(D_s)}\le C\left|\left|\left|\left|e^0\right|\right|\right|\right|_{0,2}\), and (36) bounds the term by \(Ch^2\left|\left|\left|e^0\right|\right|\right|_{0,2}\). If \(1<\sigma\le 3/2\), the conormal derivative is defined by Green’s formula as an element of \(H^{\sigma-3/2}(\partial\Omega)\) with norm bounded by \(C\left|\left|\left|e^0\right|\right|\right|_{0,2}\), and interpolating the \(L^2(\partial\Omega)\) and \(H^{1/2}(\partial\Omega)\) interpolation estimates for \(\bar{\Psi}-I_h\bar{\Psi}\) on the faces of \(\partial\Omega\) gives \(\left|\left|\left|\bar{\Psi}-I_h\bar{\Psi}\right|\right|\right|_{H^{3/2-\sigma}(\partial\Omega)}\le Ch^{\sigma+1/2}\), so that the term is bounded by \(Ch^{\sigma+1/2}\left|\left|\left|e^0\right|\right|\right|_{0,2}\). Since \(s+\sigma-2\le\mathrm{min}\{\sigma+1/2,2\}\) for \(s,\sigma\in(1,2]\), all contributions in (38) are bounded by \(Ch^{s+\sigma-2}\left|\left|\left|e^0\right|\right|\right|_{0,2}\), which proves the _L_<sup>2</sup> estimate; the last inequality in (35) uses \(h\le 1\) and \(\sigma-1\ge t\).

Since \(h\le 1\) and \(s,\sigma>1\), Lemma 4.4 and (13) give, for every mesh of the family,

\(\left|\left|\Psi_h\right|\right|_{H^1(\Omega)}\le\left|\left|\Psi\right|\right|_{H^1(\Omega)}+\left|\left|\Psi-\Psi_h\right|\right|_{0,2}+\epsilon_p^{-1/2}\left|\left|\left|\Psi-\Psi_h\right|\right|\right|\le\left|\left|\Psi\right|\right|_{H^1(\Omega)}+\big(1+\epsilon_p^{-1/2}\big)C_\Psi=:\Lambda.\) (39)

The constant \(\Lambda\) does not depend on the mesh; in Section 5 it is used for both the fine mesh T_<sub>h</sub>_ and the coarse mesh T_<sub>H</sub>_. We set \(U_h:=G+\Psi_h\).

## 4.3 The nonlinear component: discrete problem and stability

In the discrete problem for \(\widehat{\Phi}\), the function _U_ is not available and is replaced by an approximation. To treat the fine and coarse meshes of the two-grid method simultaneously, we consider a generic mesh T_<sub>h</sub>_ and a generic datum<tbc>

\(U^*:=G+\Psi^*,\Psi^*\in H^1(\Omega),\left|\left|\Psi^*\right|\right|_{H^1(\Omega)}\le\Lambda,\) (40)

<tbc>where \(\Lambda>0\) is a fixed constant. With \(\Lambda\) as in (39), both \(\Psi^*=\Psi_h\) and \(\Psi^*=\Psi_H\) are admissible. The discrete nonlinear problem reads: find \(\Phi_h\in V_h^0\) such that<tbc>

\(a(\Phi_h,v)+\big(\rho_\tau(U^*+\Phi_h),v\big)_{D_s}=0\forall v\in V_h^0;\) (41)

