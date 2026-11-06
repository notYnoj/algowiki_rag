<tbc>**Corollary 1.** For every \(v_h\in S_h\),

\(\|v_h\|_{H^1(\Omega_h)}^2\le C\big(\|\nabla v_h\|_{L^2(\Omega)}^2+\|v_h\|_{L^2(\Gamma)}^2+h^2j_h(v_h,v_h)\big),\) (3.7)

where _C_ is independent of _h_.

_Proof._ Repeating the path argument in Lemma 3.3 for derivatives of order at most one gives<tbc>

\(\|v_h\|_{H^1(\Omega_h)}^2\le C\big(\|v_h\|_{H^1(\Omega)}^2+h^2j_h(v_h,v_h)\big).\)

<tbc>The generalized Poincaré-Friedrichs inequality on the fixed domain \(\Omega\) yields

\(\|v_h\|_{H^1(\Omega)}^2\le C\big(\|\nabla v_h\|_{L^2(\Omega)}^2+\|v_h\|_{L^2(\Gamma)}^2\big).\)

Combining these two estimates proves the result. □

**Lemma 3.4** (Interpolation with geometric error)**.** _Under Assumption 2.1, for any_ \(v\in H^{k+1}(\widetilde{\Omega}_h)\) _with_ \(v|_\Omega\in H_0^1(\Omega)\)_, let_ \(z:=v/\phi\) _be the corresponding scaled function. Let_ I_<sub>h</sub> be the standard spline interpolation operator. We define the modified interpolant_ \(\widetilde{\mathcal{I}}_hv\in S_h\) _as_

\(\widetilde{\mathcal{I}}_hv:=\phi_h(\mathcal{I}_hz).\) (3.8)

_Then, the following error estimate holds for_ \(m\in\{1,2\}\):

\(\|v-\widetilde{\mathcal{I}}_hv\|_{H^m(\Omega_h)}\le Ch^{k+1-m}\|v\|_{H^{k+1}(\widetilde{\Omega}_h)},\) (3.9)

_where C may depend on higher-order Sobolev norms of the level set function_ \(\phi\).

_Proof._ Denote _z<sub>h</sub>_=I_<sub>h</sub>z_ as the spline interpolant of _z_. We decompose the interpolation error as

\(\phi z-\phi_hz_h=\underbrace{(\phi-\phi_h)z_h}_{T_1}+\underbrace{\phi(z-z_h)}_{T_2}\) (3.10)

and estimate _T_<sub>1</sub> and _T_<sub>2</sub> in the \(H^1(\Omega_h)\)- and \(H^2(\Omega_h)\)-norms, respectively.

**Estimate for** _T_<sub>1</sub>**:** Using the Sobolev embeddings \(H^2(\Omega_h)\unknown\rightarrow L^\infty(\Omega_h)\) and \(H^1(\Omega_h)\unknown\rightarrow L^6(\Omega_h)\unknown\rightarrow L^3(\Omega_h)\), we obtain

\(\|T_1\|_{H^1(\Omega_h)}\le C\big(\|(\phi-\phi_h)z_h\|_{L^2(\Omega_h)}+\|(\nabla(\phi-\phi_h))z_h\|_{L^2(\Omega_h)}+\|(\phi-\phi_h)\nabla z_h\|_{L^2(\Omega_h)}\big)\)<br>
\(\le C\big(\|\phi-\phi_h\|_{L^2(\Omega_h)}\|z_h\|_{L^\infty(\Omega_h)}+\|\nabla(\phi-\phi_h)\|_{L^2(\Omega_h)}\|z_h\|_{L^\infty(\Omega_h)}\)<br>
\(+\|\phi-\phi_h\|_{L^3(\Omega_h)}\|\nabla z_h\|_{L^6(\Omega_h)}\big)\)<br>
\(\le C\|\phi-\phi_h\|_{H^1(\Omega_h)}\|z_h\|_{H^2(\Omega_h)}\le Ch^k\|z\|_{H^2(\widetilde{\Omega}_h)},\) (3.11)

where the last inequality follows from the _H_<sup>2</sup>-stability of the spline interpolation operator and the approximation property (2.4). By the Hardy-type result \[19, Lemma 3.1\], we have \(z\in H^k(\widetilde{\Omega}_h)\) and

\(\|z\|_{H^k(\widetilde{\Omega}_h)}\le C\|v\|_{H^{k+1}(\widetilde{\Omega}_h)}.\) (3.12)

Therefore, substituting the Hardy-type inequality (3.12) into (3.11), we obtain

\(\|T_1\|_{H^1(\Omega_h)}\le Ch^k\|v\|_{H^3(\widetilde{\Omega}_h)}.\) (3.13)

Similarly, the _H_<sup>2</sup>-norm admits the estimate

\(\|T_1\|_{H^2(\Omega_h)}\le C\big(\|\phi-\phi_h\|_{H^2(\Omega_h)}\|z_h\|_{L^\infty(\Omega_h)}+\|\nabla(\phi-\phi_h)\|_{L^3(\Omega_h)}\|\nabla z_h\|_{L^6(\Omega_h)}\)<br>
\(+\|\phi-\phi_h\|_{L^\infty(\Omega_h)}\|z_h\|_{H^2(\Omega_h)}\big)\)<br>
\(\le C\|\phi-\phi_h\|_{H^2(\Omega_h)}\|z_h\|_{H^2(\Omega_h)}\text{(using Sobolev embedding)}\)<br>
\(\le C\|\phi-\phi_h\|_{H^2(\Omega_h)}\|v\|_{H^3(\widetilde{\Omega}_h)},\) (3.14)

