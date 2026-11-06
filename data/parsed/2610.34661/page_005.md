conditions, and of the ionic charges, respectively, and \(U=G+\Psi\) is the potential of the solute in pure water. In \[34\] the nonlinearity in (8) is written as \(-\beta\sum_iZ_i\bar{c}_iw_i(\mathbf{r})e^{-Z_i\widehat{\Phi}}\) with _w<sub>i</sub>=e_<sup>-_Z<sub>i</sub>U_</sup>; this is the same as \(\rho(U+\widehat{\Phi})\). Since all atomic centers **r**_<sub>j</sub>_ lie in _D<sub>p</sub>_ and dist(**r**_<sub>j</sub>,<o>D<sub>s</sub></o>)\>_0, the function _G_ is real-analytic in a neighborhood of <o>_D<sub>s</sub>_</o> and, in particular, \(G\in C^\infty(\overline{D_s})\) and \(\nabla G\in L^\infty(D_s)\).

## 2.3 Notation and weak formulations

We use standard notation for Lebesgue and Sobolev spaces. For a measurable set \(D\subseteq\Omega\), \(\left\|\cdot\right\|_{0,p,D}\) denotes the norm of _L<sup>p</sup>(D_), \(1\le p\le\infty\), and \((\cdot,\cdot)_D\) the _L_<sup>2</sup>(_D_) inner product; the subscript _D_ is omitted when \(D=\Omega\). For _s\>_0 we write \(H^s(D_p\cup D_s)\) for the space of functions _v_ with \(v|_{D_p}\in H^s(D_p)\) and \(v|_{D_s}\in H^s(D_s)\), normed by \(\left\|v\right\|_{H^s(D_p\cup D_s)}^2=\left\|v\right\|_{H^s(D_p)}^2+\left\|v\right\|_{H^s(D_s)}^2\). Let \(H_0^1(\Omega)=\{v\in H^1(\Omega):v=0\text{on}\partial\Omega\}\). We shall use the Poincaré and Sobolev inequalities

\(\left\|v\right\|_{0,2}\le C_P\left\|\nabla v\right\|_{0,2},\left\|v\right\|_{0,6}\le C\left\|\nabla v\right\|_{0,2},\forall v\in H_0^1(\Omega),\) (10)

and the Gagliardo-Nirenberg (Ladyzhenskaya) inequality in three dimensions \[23\]

\(\left\|v\right\|_{0,4}\le C_L\left\|v\right\|_{0,2}^{1/4}\left\|\nabla v\right\|_{0,2}^{3/4},\forall v\in H_0^1(\Omega).\) (11)

By Hölder’s inequality and (10), \(\left\|v\right\|_{0,p}\le C\left\|\nabla v\right\|_{0,2}\) for every \(p\in[1,6]\) and \(v\in H_0^1(\Omega)\).

The bilinear form associated with the dielectric operator is

\(a(v,w):=\epsilon_p\int_{D_p}\nabla v\cdot\nabla w\mathrm{d}\mathbf{r}+\epsilon_s\int_{D_s}\nabla v\cdot\nabla w\mathrm{d}\mathbf{r},v,w\in H^1(\Omega),\) (12)

and we define the energy norm |||_v_|||:=_a(v,v_)<sup>1/2</sup> on \(H_0^1(\Omega)\). Clearly

\(\epsilon_p\left\|\nabla v\right\|_{0,2}^2\le|||v|||^2\le\epsilon_s\left\|\nabla v\right\|_{0,2}^2,a(v,w)\le|||v||||||w|||.\) (13)

Using (10) we have in particular \(\left\|v\right\|_{0,p}\le C|||v|||\) for \(p\in[1,6]\) and \(v\in H_0^1(\Omega)\).

The weak form of (7) reads \[34\]: find \(\Psi\in H^1(\Omega)\) with \(\Psi=\hat{g}-G\) on \(\partial\Omega\) such that

\(a(\Psi,v)=(\epsilon_p-\epsilon_s)\int_{D_s}\nabla G\cdot\nabla v\mathrm{d}\mathbf{r}\forall v\in H_0^1(\Omega).\) (14)

Here the interface term \((\epsilon_s-\epsilon_p)\int_\Gamma\frac{\partial G}{\partial\mathbf{n}}v\mathrm{d}s\) has been converted into a volume integral by Green’s identity and the harmonicity of _G_ in _D<sub>s</sub>_, which is convenient for complex molecular surfaces. If \(\hat{g}\in H^{1/2}(\partial\Omega)\), problem (14) has a unique solution by the Lax-Milgram lemma \[34, Theorem 4.1\].

The weak form of (8) reads: find \(\widehat{\Phi}\in\mathcal{H}\) such that

\(a(\widehat{\Phi},v)+\big(\rho(U+\widehat{\Phi}),v\big)_{D_s}=0\forall v\in H_0^1(\Omega),\) (15)

where

\(\mathcal{H}:=\big\{v\in H_0^1(\Omega):e^{-Z_iv}\in L^2(D_s),i=1,\dots,n\big\}\) (16)

is a subset of \(H_0^1(\Omega)\) on which the nonlinear term is well defined whenever \(U\in L^\infty(D_s)\). It is shown in \[34, Theorem 4.2\] that (15) has a unique solution, which is the unique minimizer of a strictly convex functional on H. In Section 3 we give a different proof that also produces the a priori bound needed for the error analysis.

Throughout the paper we make the following standing assumption on the data.

