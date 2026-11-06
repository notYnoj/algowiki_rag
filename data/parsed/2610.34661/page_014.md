_Proof._ Set \(e:=\widehat{\Phi}-\Phi_h\). Subtracting (41) from (23) (recall \(\widehat{\Phi}=\Phi_\tau\) by Theorem 3.6) gives the error equation<tbc>

\(a(e,\chi)+(T_1+T_2,\chi)_{D_s}=0\forall\chi\in V_h^0,\) (46)

<tbc>where<tbc>

\(T_1:=\rho_\tau(U+\widehat{\Phi})-\rho_\tau(U+\Phi_h),T_2:=\rho_\tau(U+\Phi_h)-\rho_\tau(U^*+\Phi_h).\)

<tbc>Let \(v_h\in V_h^0\) be arbitrary and \(\eta:=\widehat{\Phi}-v_h\). Then \(v_h-\Phi_h=e-\eta\in V_h^0\), and by (46),

\(|||e|||^2=a(e,\eta)+a(e,e-\eta)=a(e,\eta)-(T_1,e)_{D_s}-(T_2,e)_{D_s}+(T_1,\eta)_{D_s}+(T_2,\eta)_{D_s}.\text{(47)}\)

Since \(\rho_\tau\) is increasing,

\(T_1e=\big(\rho_\tau(U+\widehat{\Phi})-\rho_\tau(U+\widehat{\Phi}-e)\big)e\ge 0\text{a.e. in}D_s,\)

so \(-(T_1,e)_{D_s}\le 0\). We bound the remaining terms.

_The term T_<sub>1</sub>. Applying (44) with \(\xi_1=U+\widehat{\Phi}\) and \(\xi_2=U+\Phi_h\), so that \(\xi_1-\xi_2=e\), and using (28),<tbc>

\(|T_1|\le C_1(1+2M_U+|e|)|e|\text{a.e. in}D_s.\)

<tbc>Hence, by Hölder’s inequality and (10)-(13),

\(|(T_1,\eta)_{D_s}|\le C_1(1+2M_U)\left\|e\right\|_{0,2,D_s}\left\|\eta\right\|_{0,2,D_s}+C_1\left\|e\right\|_{0,4,D_s}^2\left\|\eta\right\|_{0,2,D_s}\le C\big(|||e|||+|||e|||^2\big)\left\|\eta\right\|_{0,2}.\text{(48)}\)

_The term T_<sub>2</sub>. Applying (44) with \(\xi_1=U+\Phi_h\) and \(\xi_2=U^*+\Phi_h\), so that \(\xi_1-\xi_2=U-U^*=\Psi-\Psi^*\),<tbc>

\(|T_2|\le C_1\big(1+M_U+|\Phi_h|+|\Psi-\Psi^*|\big)|\Psi-\Psi^*|\text{a.e. in}D_s.\)

<tbc>For any \(w\in H_0^1(\Omega)\), Hölder’s inequality with exponents (3,2,6) gives

\(|(T_2,w)_{D_s}|\le C_1\left\|1+M_U+|\Phi_h|+|\Psi-\Psi^*|\right\|_{0,3,D_s}\left\|\Psi-\Psi^*\right\|_{0,2,D_s}\left\|w\right\|_{0,6}\le C\delta|||w|||,\text{(49)}\)

where we used

\(\left\|\Phi_h\right\|_{0,3}\le C|||\Phi_h|||\le CC_\Lambda,\left\|\Psi-\Psi^*\right\|_{0,3,D_s}\le C\big(\left\|\Psi\right\|_{H^1(\Omega)}+\Lambda\big),\left\|w\right\|_{0,6}\le C|||w|||,\)

by Lemma 4.5, the Sobolev embedding \(H^1(\Omega)\unknown\rightarrow L^3(\Omega)\), and (10)-(13), respectively.

_Conclusion._ Inserting (48) and (49) (with _w=e_ and \(w=\eta\)) into (47) and using \(a(e,\eta)\le|||e|||\eta|||\) yields

\(|||e|||^2\le|||e|||\big(|||\eta|||+C\left\|\eta\right\|_{0,2}+C\delta\big)+C|||e|||^2\left\|\eta\right\|_{0,2}+C\delta|||\eta|||.\) (50)

Now choose _v<sub>h</sub>_ according to Lemma 4.3 with _r=s_ and \(v=\widehat{\Phi}\in H_0^1(\Omega)\cap H^s(D_p\cup D_s)\), so that<tbc>

\(|||\eta|||\le C_Ah^{s-1}\left\|\widehat{\Phi}\right\|_{H^s(D_p\cup D_s)},\left\|\eta\right\|_{0,2}\le C_Ah^s\left\|\widehat{\Phi}\right\|_{H^s(D_p\cup D_s)},\)

<tbc>and let _h_<sub>0</sub>_\>_0 be such that<tbc>

\(CC_Ah_0^s\left\|\widehat{\Phi}\right\|_{H^s(D_p\cup D_s)}\le\frac{1}{2},\)

