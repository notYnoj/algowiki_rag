where _C_ is the constant in front of \(|||e|||^2\left\|\eta\right\|_{0,2}\) in (50). Then for \(h\le h_0\) the term \(C|||e|||^2\left\|\eta\right\|_{0,2}\) can be absorbed into the left-hand side of (50), and we obtain, using \(h^s\le h^{s-1}\) and Young’s inequality \(\delta h^{s-1}\le\frac{1}{2}(\delta^2+h^{2(s-1)})\),

\(\frac{1}{2}|||e|||^2\le C\big(h^{s-1}+\delta\big)|||e|||+C\big(h^{2(s-1)}+\delta^2\big).\)

If \(x\ge 0\) satisfies \(x^2\le bx+c\) with \(b,c\ge 0\), then \(x\le b+\sqrt{c}\). Applying this with \(x=|||e|||\) gives (45).

_Remark_ 4.7. The truncation and the bound (28) enter the proof as follows. The pointwise bound on \(U+\widehat{\Phi}\) gives the linear part of _T_<sub>1</sub> a bounded coefficient. The quadratic growth of \(\rho_\tau\) makes the rest of _T_<sub>1</sub> quadratic in _e_, so it is controlled by \(\left\|e\right\|_{0,4}^2\lesssim|||e|||^2\); this term is absorbed for small _h_ because it is multiplied by \(\left\|\eta\right\|_{0,2}=O(h^s)\). Unlike \[19, Theorem 3.5\], no pointwise bound on \(\Phi_h\) is used, and hence no condition on the mesh beyond shape regularity is needed. In return we need \(h\le h_0\), as is usual for this kind of argument (cf. \[6\]).

## 4.5 _L_<sup>2</sup> and _L_<sup>4</sup> error estimates

**Theorem 4.8** (_L_<sup>2</sup> estimate)**.** _Under the hypotheses of Theorem 4.6, let in addition Assumption 4.1(ii) hold. Then for all_ \(h\le h_0\),

\(\left\|\widehat{\Phi}-\Phi_h\right\|_{0,2}\le C\big(h^{\sigma-1}|||\widehat{\Phi}-\Phi_h|||+|||\widehat{\Phi}-\Phi_h|||^2+\delta\big),\) (51)

_with C depending on the same quantities as in Theorem 4.6 and on C<sub>R</sub>._

_Proof._ Let \(e=\widehat{\Phi}-\Phi_h\) and let \(w\in H_0^1(\Omega)\) be the solution of the dual problem (30) with _f=e_, where \(c=\rho'_\tau(U+\widehat{\Phi})\) satisfies \(0<c\le c_\mathrm{max}\) by (29). The bilinear form _B(v,w_):=_a(v,w_)+(_cv,w)<sub>D<sub>s</sub></sub>_ satisfies<tbc>

\(B(v,v)\ge|||v|||^2,B(v,w)\le\big(1+c_\mathrm{max}C_P^2\epsilon_p^{-1}\big)|||v|||w|||\forall v,w\in H_0^1(\Omega).\)

<tbc>Let \(w_h\in V_h^0\) be the Galerkin approximation of _w_, _B(v<sub>h</sub>,w<sub>h</sub>_)=(_e,v<sub>h</sub>_) for all \(v_h\in V_h^0\). By Céa’s lemma, Lemma 4.3 with \(r=\sigma\) and Assumption 4.1(ii) with \(c=\rho'_\tau(U+\widehat{\Phi})\),

\(|||w-w_h|||\le C\mathrm{inf}_{v_h\in V_h^0}|||w-v_h|||\le Ch^{\sigma-1}\left\|w\right\|_{H^\sigma(D_p\cup D_s)}\le Ch^{\sigma-1}\left\|e\right\|_{0,2},\) (52)

and, taking _v<sub>h</sub>=w<sub>h</sub>_ in the discrete dual problem,

\(|||w_h|||^2\le B(w_h,w_h)=(e,w_h)\le\left\|e\right\|_{0,2}\left\|w_h\right\|_{0,2}\le C\left\|e\right\|_{0,2}|||w_h|||,\text{so that}|||w_h|||\le C\left\|e\right\|_{0,2}.\) (53)

Taking _v=e_ in (30) (recall that _f=e_) and using the error equation (46) with \(\chi=w_h\), we get

\(\left\|e\right\|_{0,2}^2=B(e,w)=B(e,w-w_h)+a(e,w_h)+(ce,w_h)_{D_s}\)<br>
\(=B(e,w-w_h)+\big(ce-T_1,w_h\big)_{D_s}-\big(T_2,w_h\big)_{D_s}.\) (54)

For the first term, (52) gives<tbc>

\(|B(e,w-w_h)|\le C|||e||||||w-w_h|||\le Ch^{\sigma-1}|||e|||\left\|e\right\|_{0,2}.\)

<tbc>For the second term we use Taylor’s formula with integral remainder and \(\Phi_h=\widehat{\Phi}-e\): a.e. in _D<sub>s</sub>_,<tbc>

\(\rho_\tau(U+\widehat{\Phi}-e)=\rho_\tau(U+\widehat{\Phi})-\rho'_\tau(U+\widehat{\Phi})e+e^2\int_0^1(1-\vartheta)\rho''_\tau(U+\widehat{\Phi}-\vartheta e)\mathrm{d}\vartheta,\)

