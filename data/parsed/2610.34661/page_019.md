**Theorem 5.2.** _Let Assumptions 2.1 and 4.1 hold, let_ \(\hat{g}\) _be smooth, let_ (3) _and_ (27) _hold, and assume that the coarse datum in Algorithm 1 satisfies_<tbc>

\(\left\|\Psi^\sharp\right\|_{H^1(\Omega)}\le\Lambda,\left\|\Psi-\Psi^\sharp\right\|_{0,2,D_s}\le C_\Psi H^{s-1+t},\) (64)

<tbc>_which holds for_ \(\Psi^\sharp=\Psi_h\) _and for_ \(\Psi^\sharp=\Psi_H\) _by_ (39) _and Lemma 4.4. Then there are constants h_<sub>0</sub>_\>_0 _and C\>_0_, independent of h and H, such that for all_ \(h<H\le h_0\) _the two-grid solution_ \(u_h^\mathrm{tg}\) _of Algorithm 1 satisfies_<tbc>

\(|||u-u_h^\mathrm{tg}|||\le C\big(h^{s-1}+H^{2(s-1)+t/2}\big),t=\mathrm{min}\{s,\sigma\}-1.\) (65)

<tbc>_Proof._ By the triangle inequality and Corollary 4.10,<tbc>

\(|||u-u_h^\mathrm{tg}|||\le|||u-u_h|||+|||\Phi_h-\Phi_h^\mathrm{tg}|||\le Ch^{s-1}+|||\Phi_h-\Phi_h^\mathrm{tg}|||.\) (66)

<tbc>By Lemma 5.1 and the triangle inequality in \(L^4(\Omega)\),<tbc>

\(|||\Phi_h-\Phi_h^\mathrm{tg}|||\le C\left\|\Phi_h-\Phi_H\right\|_{0,4}^2\le 2C\big(\left\|\widehat{\Phi}-\Phi_h\right\|_{0,4}^2+\left\|\widehat{\Phi}-\Phi_H\right\|_{0,4}^2\big),\) (67)

<tbc>where we used \((x+y)^2\le 2(x^2+y^2)\). The function \(\Phi_h\) is the solution of (41) on T_<sub>h</sub>_ with \(\Psi^*=\Psi_h\), for which \(\delta\le C_\Psi h^{s-1+t}\) by Lemma 4.4; the function \(\Phi_H\) is the solution of (41) on T_<sub>H</sub>_ with \(\Psi^*=\Psi^\sharp\), for which \(\delta\le C_\Psi H^{s-1+t}\) by (64). Since \(h<H\le h_0\), Corollary 4.9 applies on both meshes and gives

\(\left\|\widehat{\Phi}-\Phi_h\right\|_{0,4}\le Ch^{s-1+t/4},\left\|\widehat{\Phi}-\Phi_H\right\|_{0,4}\le CH^{s-1+t/4}.\)

The constants in Corollary 4.9 depend on the datum only through \(\Lambda\) and \(C_\Psi\), and are therefore the same for both meshes. Inserting these bounds into (67) and then into (66), and using _h\<H_, yields (65).

**Corollary 5.3.** _Under the hypotheses of Theorem 5.2, if the coarse mesh size satisfies_

\(H\le Ch^\gamma,\gamma:=\frac{s-1}{2(s-1)+t/2},\) (68)

_then_ \(|||u-u_h^\mathrm{tg}|||\le Ch^{s-1}\)_, i.e., the two-grid solution has the same asymptotic accuracy as the fine-mesh solution u<sub>h</sub>. If_ \(\sigma\ge s\)_, then t=s_-1 _and_ \(\gamma=2/5\) _for every_ \(s\in(1,2]\)_; in particular H∼h_<sup>2/5</sup> _suffices when_ \(s=\sigma\)_, which includes the case of full regularity_ \(s=\sigma=2\).

_Remark_ 5.4. If \(\sigma<s\), then \(t=\sigma-1<s-1\) and \(2/5<\gamma<1/2\), with \(\gamma\rightarrow 1/2\) as \(\sigma\rightarrow 1\); the coarse mesh then has to be somewhat finer relative to the fine mesh. The exponent \(\gamma\) is the same as in \[19, Remark 4.5\], where it was obtained under a discrete maximum principle; here no angle condition on T_<sub>h</sub>_ and T_<sub>H</sub>_ is needed, and the nonlinearity contains the discrete datum _U<sub>h</sub>_. For quasi-uniform meshes and \(\gamma=2/5\), the numbers of unknowns satisfy \(N_H\sim H^{-3}\sim h^{-6/5}\sim N_h^{2/5}\); for example, _N<sub>h</sub>_≈10<sup>6</sup> corresponds to _N<sub>H</sub>_ of a few hundred. In practice the coarse mesh still has to resolve the molecular surface, and the constants in (65) depend on the geometry, so a somewhat finer coarse mesh may be preferable.

_Remark_ 5.5 (the two variants of Step 3). Theorem 5.2 covers both \(\Psi^\sharp=\Psi_h\) and \(\Psi^\sharp=\Psi_H\), because the proof compares \(\Phi_H\) directly with \(\widehat{\Phi}\) and only needs the perturbation of the datum in the coarse problem to be of the order _H_<sup>_s_-1+_t_</sup> of the coarse _L_<sup>2</sup> error. The fine Newton correction (58) always<tbc>

