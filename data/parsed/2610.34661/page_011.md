**Lemma 4.3.** _For every_ \(v\in H_0^1(\Omega)\cap H^r(D_p\cup D_s)\) _with_ \(1<r\le 2\) _there exists_ \(v_h\in V_h^0\) _such that_

\(\left\|v-v_h\right\|_{0,2}+h\left\|\left\|v-v_h\right\|\right\|\le C_Ah^r\left\|v\right\|_{H^r(D_p\cup D_s)}.\) (33)

_Proof._ The estimate (33) is a standard consequence of the elementwise interpolation estimates on fitted meshes, i.e., meshes whose elements satisfy \(T\subset\overline{D_p}\) or \(T\subset\overline{D_s}\).

For _r\>_3/2, the nodal interpolant _I<sub>h</sub>v_ is well defined, since _H<sup>r</sup>(D<sub>p</sub>_) and _H<sup>r</sup>(D<sub>s</sub>_) embed into the continuous functions and _v_ is continuous across \(\Gamma\), and the usual elementwise interpolation estimates give (33) because every element lies in <o>_D<sub>p</sub>_</o> or in <o>_D<sub>s</sub>_</o>. For general \(r\in(1,2]\), the nodal interpolant need not be defined, and one instead uses a Scott-Zhang type quasi-interpolant \[31\] whose averaging patches do not cross \(\Gamma\) and which preserves homogeneous boundary values; the local estimates then yield (33) for all \(r\in(1,2]\). We refer to \[10\] and \[24, Theorem 3.5\] for the details.

## 4.2 The linear component

The finite element approximation of \(\Psi\) is defined as in \[34, Algorithm 1\]: find \(\Psi_h\in V_h\) such that \(\Psi_h=I_h^\partial(\hat{g}-G)\) on \(\partial\Omega\) and

\(a(\Psi_h,v)=(\epsilon_p-\epsilon_s)\int_{D_s}\nabla G\cdot\nabla v\mathrm{d}\mathbf{r}\forall v\in V_h^0,\) (34)

where \(I_h^\partial\) denotes nodal interpolation on the boundary mesh. Since _G_ is smooth near \(\partial\Omega\), the boundary datum \(\hat{g}-G\) is as smooth as \(\hat{g}\). From now on we assume that \(\hat{g}\) is smooth, as is the case in practice (\(\hat{g}=0\) or a smooth far-field approximation), so that nodal interpolation on \(\partial\Omega\) is defined. (If only \(\hat{g}\in H^{1/2}(\partial\Omega)\), \(I_h^\partial\) can be replaced by the trace of a Scott-Zhang quasi-interpolant \[31\].) Problem (34) is a standard discretization of a linear interface problem with piecewise constant coefficients \[3, 10, 29, 24\]. We include a short proof of the error estimate because of the nonhomogeneous Dirichlet datum.

**Lemma 4.4.** _Let Assumption 4.1 hold and let_ \(\hat{g}\) _be smooth. Then for every mesh_ T_<sub>h</sub> of the family, the solutions of_ (14) _and_ (34) _satisfy_

\(\left\|\left\|\Psi-\Psi_h\right\|\right\|\le C_\Psi h^{s-1},\left\|\Psi-\Psi_h\right\|_{0,2}\le C_\Psi h^{s+\sigma-2}\le C_\Psi h^{s-1+t},\) (35)

_with_ \(s,\sigma\) _and t as in Assumption 4.1 and_ \(C_\Psi\) _independent of h._

_Proof._ Since \(\hat{g}-G\) is smooth on \(\partial\Omega\) and \(\Gamma\cap\partial\Omega=\emptyset\), there is a lifting \(\bar{\Psi}\in C^\infty(\overline{\Omega})\) with \(\bar{\Psi}=\hat{g}-G\) on \(\partial\Omega\) and \(\bar{\Psi}=0\) in a neighborhood of \(\Gamma\). Then \(I_h\bar{\Psi}\in V_h\) has the boundary values \(I_h^\partial(\hat{g}-G)\), so that \(\Psi_h-I_h\bar{\Psi}\in V_h^0\), and

\(\left\|\left\|\bar{\Psi}-I_h\bar{\Psi}\right\|\right\|+h^{-1}\left\|\bar{\Psi}-I_h\bar{\Psi}\right\|_{0,2}+h^{-1}\left\|\bar{\Psi}-I_h\bar{\Psi}\right\|_{0,2,\partial\Omega}\le C_\bar{\Psi}h\) (36)

by the standard interpolation estimates in \(\Omega\) and on the faces of \(\partial\Omega\), with \(C_\bar{\Psi}\) depending on the _C_<sup>2</sup> norm of \(\bar{\Psi}\). Moreover \(\Psi-\bar{\Psi}\in H_0^1(\Omega)\cap H^s(D_p\cup D_s)\) by Assumption 4.1(i). Subtracting (34) from (14) gives the Galerkin orthogonality

\(a(\Psi-\Psi_h,v)=0\forall v\in V_h^0.\) (37)

_Energy estimate._ Let \(v_h\in V_h^0\) be the approximation of \(\Psi-\bar{\Psi}\) provided by Lemma 4.3 with _r=s_, and set \(\chi_h:=I_h\bar{\Psi}+v_h\in V_h\); then \(\chi_h-\Psi_h\in V_h^0\), so by (37)<tbc>

\(\left\|\left\|\Psi-\Psi_h\right\|\right\|^2=a(\Psi-\Psi_h,\Psi-\chi_h)\le\left\|\left\|\Psi-\Psi_h\right\|\right\|\left\|\Psi-\chi_h\right\|,\)

