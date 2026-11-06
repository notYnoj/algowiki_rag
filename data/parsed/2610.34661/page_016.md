so that<tbc>

\(ce-T_1=\rho'_\tau(U+\widehat{\Phi})e-\big(\rho_\tau(U+\widehat{\Phi})-\rho_\tau(U+\widehat{\Phi}-e)\big)=e^2\int_0^1(1-\vartheta)\rho''_\tau(U+\widehat{\Phi}-\vartheta e)\mathrm{d}\vartheta.\)

<tbc>Since \(|\rho''_\tau|\le C_2\) by (21), we get \(|ce-T_1|\le\frac{1}{2}C_2e^2\), and Hölder’s inequality, (10) and (53) yield<tbc>

\(|(ce-T_1,w_h)_{D_s}|\le\frac{1}{2}C_2\left\|e\right\|_{0,4}^2\left\|w_h\right\|_{0,2}\le C\left\|e\right\|^2\left\|w_h\right\|\le C\left\|e\right\|^2\left\|e\right\|_{0,2}.\)

<tbc>For the third term, (49) and (53) give

\(|(T_2,w_h)_{D_s}|\le C\delta\left\|w_h\right\|\le C\delta\left\|e\right\|_{0,2}.\)

Collecting the three bounds in (54) and dividing by ∥_e_∥<sub>0,2</sub> proves (51).

The quadratic term in (51) is the place where the bounded second derivative of the truncated nonlinearity is used; with the exponential itself this step would need pointwise bounds on \(\Phi_h\), as in \[19, Theorem 3.7\].

**Corollary 4.9** (_L_<sup>2</sup> and _L_<sup>4</sup> estimates)**.** _Under the hypotheses of Theorem 4.8, suppose in addition that_ \(\delta\le C_\delta h^{s-1+t}\)_. Then for all_ \(h\le h_0\)_, with C depending additionally on_ \(C_\delta\),

\(\left\|\widehat{\Phi}-\Phi_h\right\|\le Ch^{s-1},\left\|\widehat{\Phi}-\Phi_h\right\|_{0,2}\le Ch^{s-1+t},\left\|\widehat{\Phi}-\Phi_h\right\|_{0,4}\le Ch^{s-1+t/4},\) (55)

_where t is given by_ (32).

_Proof._ The first estimate follows from (45) since \(\delta\le C_\delta h^{s-1+t}\le C_\delta h^{s-1}\). Inserting it into (51) gives<tbc>

\(\left\|\widehat{\Phi}-\Phi_h\right\|_{0,2}\le C\big(h^{\sigma-1+s-1}+h^{2(s-1)}+h^{s-1+t}\big)\le Ch^{s-1+t},\)

<tbc>since \(t\le\sigma-1\) and \(t\le s-1\). Finally, (11) and (13) give

\(\left\|\widehat{\Phi}-\Phi_h\right\|_{0,4}\le C_L\left\|\widehat{\Phi}-\Phi_h\right\|_{0,2}^{1/4}\left\|\nabla(\widehat{\Phi}-\Phi_h)\right\|_{0,2}^{3/4}\le C\big(h^{s-1+t}\big)^{1/4}\big(h^{s-1}\big)^{3/4}=Ch^{s-1+t/4}.\)

Applying Corollary 4.9 with \(\Psi^*=\Psi_h\) and Lemma 4.4, so that \(\delta=\left\|\Psi-\Psi_h\right\|_{0,2,D_s}\le C_\Psi h^{s-1+t}\), we obtain the error estimates for the finite element solution decomposition scheme of \[34, Algorithm 1\].

**Corollary 4.10** (error of the fine-mesh solution)**.** _Let Assumptions 2.1 and 4.1 hold, let_ \(\hat{g}\) _be smooth, let_ (3) _and_ (27) _hold, and let_ \(\Phi_h\) _be the solution of_ (41) _with_ \(U^*=U_h=G+\Psi_h\)_. Then for_ \(h\le h_0\) _the finite element solution_ \(u_h:=G+\Psi_h+\Phi_h\) _satisfies_

\(\left\|u-u_h\right\|\le Ch^{s-1},\left\|u-u_h\right\|_{0,2}\le Ch^{s-1+t}.\) (56)

_Proof._ Since \(u-u_h=(\Psi-\Psi_h)+(\widehat{\Phi}-\Phi_h)\), the claim follows from (35) and (55); note that \(\Psi-\Psi_h\notin H_0^1(\Omega)\) in general, but \(\left\|\cdot\right\|\) is still defined on \(H^1(\Omega)\) by (12).

_Remark_ 4.11. If _V<sub>h</sub>_ consists of continuous piecewise polynomials of degree \(k\ge 1\) and the solutions have piecewise _H<sup>s</sup>_ regularity with \(1<s\le k+1\), then Lemma 4.3 holds with _r=s_ \[24\], and all the results of this section and of Section 5 hold with the same proofs. For molecular surfaces, however, the regularity of \(\widehat{\Phi}\) is limited, and higher-order elements pay off only if the interface is also approximated to higher order \[34\].

