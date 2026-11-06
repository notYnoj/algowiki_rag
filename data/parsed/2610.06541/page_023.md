\(V_1^\dagger BV_1Q_b\). Moreover, \(\Pi V_1=(V,V)/\sqrt{2}\) gives \(\mathrm{diag}(I,O)\Pi V_1=(V,OV)/\sqrt{2}\), so the first block row of _R_, _V_<sup>†</sup>_V=I_, and _V_<sup>†</sup>_OV=A_ give \(V_1^\dagger BV_1=((1-f)I+fA)/(\sqrt{2}\alpha)\). Since \(\langle 0|\Pi_1|0\rangle=1/2\) and (1-_f)I+fA_ is Hermitian,

\(L^\dagger EL=\frac{1}{2}\left(\begin{array}{ c c }
0 & V_1^\dagger BV_1Q_b \\
Q_bV_1^\dagger B^\dagger V_1 & 0
\end{array}\right)\)<br>
\(=\frac{1}{2\sqrt{2}\alpha}\left(\begin{array}{ c c }
0 & ((1-f)I+fA)Q_b \\
Q_b((1-f)I+fA) & 0
\end{array}\right)=\frac{H(f)}{2\sqrt{2}\alpha},\)

by definition of _H(f_).

The matrices _B_, \(\widetilde{B}\), \(\Sigma\), and _E_ depend linearly on _R_, giving the identity for _E_ in (2). At _f_=0,1, respectively, _E=E_<sub>1,0</sub>_,E_<sub>0,1</sub>, so both are Hermitian involutions, and they anticommute because \(E=(E_{1,0}+E_{0,1})/\sqrt{2}\) at _f_=1/2 is an involution, so \(I=E^2=I+\frac{1}{2}(E_{1,0}E_{0,1}+E_{0,1}E_{1,0})\). Put \(u=(1-f)/\alpha\), \(v=f/\alpha\), so _E=uE_<sub>1,0</sub>+_vE_<sub>0,1</sub>, and _X_=-_vE_<sub>1,0</sub>+_uE_<sub>0,1</sub>. Since _u_<sup>2</sup>+_v_<sup>2</sup>=1, _E_<sup>2</sup>=_X_<sup>2</sup>=_I_ and _EX+XE_=0. Thus, for real _x,y_, (_xE+yX_)<sup>2</sup>=(_x_<sup>2</sup>+_y_<sup>2</sup>)_I_, and \(\|M\|^2=\|M^2\|\) for Hermitian _M_ gives \(\|xE+yX\|=\sqrt{x^2+y^2}\). Differentiating in _f_ gives \(du/df=-f/\alpha^3=-v/\alpha^2\), \(dv/df=(1-f)/\alpha^3=u/\alpha^2\), and \(d\alpha^2/df=2(2f-1)\), so

\(\frac{dE}{df}=\frac{X}{\alpha^2},\frac{dX}{df}=-\frac{E}{\alpha^2},\frac{d^2E}{df^2}=-\frac{2(2f-1)}{\alpha^4}X-\frac{1}{\alpha^4}E.\)

By the norm identity, \(\|dE/df\|=\alpha^{-2}\) and, with \((2f-1)^2=2\alpha^2-1\), \(\|d^2E/df^2\|^2=(8\alpha^2-3)/\alpha^8\le 16/(3\alpha^4)\), because \(16\alpha^4-24\alpha^2+9=(4\alpha^2-3)^2\). Since 2_LL_<sup>†</sup>-_I_ is a reflection, \(\|\frac{d}{df}W\|\le\alpha^{-2}\) and \(\|\frac{d^2}{df^2}W\|\le\frac{4}{\sqrt{3}}\alpha^{-2}\), and the chain rule \(W'=f'\frac{dW}{df}\) and \(W''=f''\frac{dW}{df}+f'^2\frac{d^2W}{df^2}\) gives the second claim.

Finally, put _Z_<sub>1</sub>=diag(_I,_0) and _Z_<sub>2</sub>=diag(_Q_<sub>0</sub>_,I-Q_<sub>0</sub>), so \(I_2\otimes\mathrm{diag}(Z_1,Z_2)\) is _Z_ in the block order of \(\Sigma\). Since _Q_<sub>0</sub>(_I-Q_<sub>0</sub>)=0,

\(Z_1\widetilde{B}=\left(\begin{array}{ c c }
BQ_0 & B(I-Q_0) \\
0 & 0
\end{array}\right)=\widetilde{B}Z_2,\)

and taking adjoints gives \(Z_2\widetilde{B}^\dagger=\widetilde{B}^\dagger Z_1\), so diag(_Z_<sub>1</sub>_,Z_<sub>2</sub>) commutes with \(\Sigma\) and _Z_ commutes with \(E=\Pi_1\otimes\Sigma\). Since _Z_<sub>1</sub>_V_<sub>2</sub>=_V_<sub>2</sub> and _Z_<sub>2</sub>_V_<sub>2</sub>=(_Q_<sub>0</sub>_V_<sub>1</sub>,0)=(_V_<sub>1</sub>_Q<sub>b</sub>,_0)=_V_<sub>2</sub>_Q<sub>b</sub>_, _ZL=L_diag(_I,Q<sub>b</sub>_). Since diag(_I,Q<sub>b</sub>_) is Hermitian, _ZLL_<sup>†</sup>=_L_diag(_I,Q<sub>b</sub>)L_<sup>†</sup>=(_ZLL_<sup>†</sup>)<sup>†</sup>=_LL_<sup>†</sup>_Z_, so _Z_ commutes with 2_LL_<sup>†</sup>-_I_, hence with _W(s_). □

Finally, we bound the constants using AQC(3/2), which makes the integrands of _J_<sub>1</sub> constant up to \(1/\alpha\le\sqrt{2}\), as in Section 6.2.

**Lemma A.4.** _Let_ \(\kappa>1\)_, let r, f, and_ \(\alpha=\alpha(f(s))\) _be as in Corollary A.2 and Definition A.1, and, with_ \(a=1+r=\sqrt{\kappa}\) _and_ \(\omega=2(1+r)^2/(r+2)\)_, put_<tbc>

\(p(s)=\frac{3a\omega}{(1+rs)^4},g(s)=\frac{\beta}{\alpha(1+rs)^2},\beta=\frac{1}{2\sqrt{2}}.\)

<tbc>_Evaluate the Bernoulli majorant derivative_ \(\mathcal{B}'\) _(Definition 2.8) and unit-step coefficients c_<sub>0</sub>_, c_<sub>1</sub>_, and c_<sub>2</sub> _(Definition 6.3) at_ \(5\pi/3\)_, and set_<tbc>

\(\rho_1=\frac{5\pi}{3},\rho_2=\frac{5\pi}{9}\left(7+\frac{8}{\sqrt{3}}+8\mathcal{B}'\right),K=\frac{4\rho_1+6\rho_2}{\beta^2}+\frac{28\sqrt{2}\rho_1^2}{\beta^3}+4c_0\rho_1+16c_1\rho_1^2+6c_2\rho_2.\)

<tbc>_Let_ \(\Lambda\) _be a C_<sup>2</sup> _Hermitian path on an open interval containing_ \[0,1\] _with_

\(\|\Lambda'\|\le\frac{\rho_1|f'|}{\alpha^2},\|\Lambda''\|\le\frac{\rho_1(|f''|+\frac{4}{\sqrt{3}}|f'|^2)}{\alpha^2}+\frac{\rho_1(1+2\mathcal{B}')|f'|^2}{\alpha^4}.\)

(1) _On_ \[0,1\], \(\|\Lambda'\|\le\rho_1f'/\alpha^2\le 4\rho_1a\) _and_ \(\|\Lambda''\|\le\rho_2p/\alpha^2\le 12\rho_2a^2\).<tbc>

(2) _The Jansen-Ruskai-Seiler coefficient J_<sub>1</sub> (3.1) _of the envelopes_ \(\rho_1f'/\alpha^2\), \(\rho_2p/\alpha^2\)_, and the gap g is at most_ \(\left((4\rho_1+6\rho_2)/\beta^2+28\sqrt{2}\rho_1^2/\beta^3\right)a^2\).<tbc>

