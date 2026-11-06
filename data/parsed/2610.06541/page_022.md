\(\|(iW^\dagger W')'\|\le\|W''\|+\|W'\|^2\), give

\(\|\Lambda'\|\le\frac{5\pi}{3}\|W'\|,\|\Lambda''\|\le\frac{5\pi}{3}\|W''\|+\frac{5\pi}{3}(1+2\mathcal{B}')\|W'\|^2.\)

The fixed orthogonal projector _Z_ commutes with _E_ and every step, hence with _F<sub>s</sub>_ and the logarithm, and satisfies _ZL=L_diag(_I,Q<sub>b</sub>_) (Lemma A.3). The invariant planes give the phase \(\pi/2\) only at \(\lambda=0\), so the +_i_ eigenspace of _W(s_) is _F<sub>s</sub>L_ker_H(f(s_)), and _ZF<sub>s</sub>L=F<sub>s</sub>L_diag(_I,Q<sub>b</sub>_). Since ker_H(f_)={(_z_\[(1-_f)I+fA_\]<sup>-1</sup>_b,z'b_):_z,z_\('\in\mathbb{C}\}\) meets randiag(_I,Q<sub>b</sub>_) in the line through (\[(1-_f)I+fA_\]<sup>-1</sup>_b,_0), the +_i_ eigenspace of _W(s_) on ran_Z_ is ran_P(s_).

Define \(\widehat{\Lambda}=Z\Lambda Z-(7\pi/6)(I-Z)\). It agrees with \(\Lambda\) on the invariant subspace ran_Z_, so \(e^{-i\widehat{\Lambda}(s)}Z=W(s)Z\), and equals \(-7\pi/6\), the midpoint of \([-2\pi,-\pi/3]\), on its orthogonal complement, so its spectrum stays in that interval and its \(-\pi/2\) band is ran_P(s_). The added eigenvalue is \(2\pi/3\) from the band, preserving the gap bound \(1/[2\sqrt{2}\alpha(1+rs)^2]\le 1/2\), since \(\alpha\ge 1/\sqrt{2}\) and \(s\ge 0\). Since _Z_ is fixed, \(\widehat{\Lambda}'=Z\Lambda'Z\) and \(\widehat{\Lambda}''=Z\Lambda''Z\), so projector contraction preserves both derivative bounds. Since _W(s_) and \(e^{-i\widehat{\Lambda}(s)}\) commute with _Z_ and agree on ran_Z_, and _ZP_(0)=_P_(0), their products agree on ran_P_(0). Thus, substituting Lemma A.3(2) into the derivative bounds lets us apply Lemma A.4 to \(\widehat{\Lambda}\). With _J_<sub>1</sub>, _g_, \(\rho_1\), \(\rho_2\), and _c<sub>i</sub>_ from Lemma A.4, every integer \(T\ge 1\) satisfies

\(\|(I-P(1))W((T-1)/T)\cdots W(0)P(0)\|\le\frac{J_1+(4c_0\rho_1+16c_1\rho_1^2+6c_2\rho_2)(1+r)^2}{T}\)<br>
\(\le\frac{K(1+r)^2}{T}=\frac{K\kappa}{T}.\)

The first uses Jansen-Ruskai-Seiler, monotonicity in derivative norms, and Theorem 6.5 with Lemma A.4(3). Part (2) and _K_’s definition give the second, and \(1+r=\sqrt{\kappa}\) gives equality. Taking \(T=\lceil K\kappa/\delta\rceil\) or \(\lceil 2K\kappa/\delta\rceil\) bounds leakage by \(\delta\) or \(\delta/2\), respectively.

Finally, control preparation and postselection give \((I+iE(f(0)))/2=F_0/\sqrt{2}\) and \((I-iE(f(1)))/2=F_1^\dagger/\sqrt{2}\). Since _F<sub>s</sub>_ is unitary, each succeeds with probability 1/2, hence 1/4 jointly. By the definition of _P(s_), _f_(0)=0, and _f_(1)=1, _F_<sub>0</sub>_L(b,_0) spans ran_P_(0) and, with _x=A_<sup>-1</sup>_b/_\[_A_<sup>-1</sup>_b_\], _F_<sub>1</sub>_L(x,_0) spans ran_P_(1). Let \(\psi\) be the walk product applied to _F_<sub>0</sub>_L(b,_0), so the normalized successful joint output is \(F_1^\dagger\psi\), and put \(\chi=F_1^\dagger P(1)\psi\). Since _F_<sub>1</sub> is unitary and \(\delta\le 1\), the leakage bound \(\delta/2\) of \(\lceil 2K\kappa/\delta\rceil\) steps gives \(\|F_1^\dagger\psi-\chi\|=\|(I-P(1))\psi\|\le\delta/2<1\). The reverse triangle inequality gives \(\chi\neq 0\) and \(|1-\|\chi\|\le\|F_1^\dagger\psi-\chi\|\), so homogeneity and the triangle inequality give

\(\left\|F_1^\dagger\psi-\frac{\chi}{\|\chi\|}\right\|\le\|F_1^\dagger\psi-\chi\|+|1-\|\chi\|\le\delta.\)

Since \(P(1)\psi\) lies in the line through _F_<sub>1</sub>_L(x,_0), \(\chi/\|\chi\|\) is _L(x,_0) up to phase. Using \(\lceil y\rceil\le y+1\) and \(\kappa/\delta\ge 1\) gives \(\lceil 2K\kappa/\delta\rceil+2\le 2K\kappa/\delta+3\le(2K+3)\kappa/\delta\). □

We now verify the three circuit facts the proof used.

**Lemma A.3.** _Let O, V , A, and b be as in Corollary A.2, and use the walk construction of Definition A.1. Write E_<sub>1,0</sub>_,E_<sub>0,1</sub> _for E with R replaced by R_<sub>1,0</sub>_,R_<sub>0,1</sub>_, respectively. Then, for every real f and, along the schedule, every s at which_ \(s\mapsto f(s)\) _is twice differentiable:_

(1) _E is a Hermitian involution and_ \(L^\dagger EL=H(f)/(2\sqrt{2}\alpha(f))\).<tbc>

(2) \(E=((1-f)E_{1,0}+fE_{0,1})/\alpha\) _with E_<sub>1,0</sub> _and E_<sub>0,1</sub> _Hermitian involutions, and, with_ \(\alpha=\alpha(f(s))\), \(\|W'(s)\|\le|f'(s)|/\alpha^2\) _and_ \(\|W''(s)\|\le(|f''(s)|+\frac{4}{\sqrt{3}}|f'(s)|^2)/\alpha^2\).<tbc>

(3) _ZL=L_diag(_I,Q<sub>b</sub>), and Z commutes with E and with W(s_).

_Proof._ Put \(B=R\mathrm{diag}(I,O)\Pi\) and \(\widetilde{B}=\mathrm{diag}(B,B)\Pi_Q\), with \(\Sigma=\left(\begin{array}{ c }
0 \\
\widetilde{B}^\dagger \\
0
\end{array}\right)\). Since \(\Pi\), \(\Pi_Q\), and diag(_I,O_) are Hermitian, block multiplication gives \(E=\Pi_1\otimes\Sigma\).

The matrices _R_, diag(_I,O_), \(\Pi\), \(\Pi_1\), and \(\Pi_Q\) are Hermitian involutions. For _R_, this follows from _R_<sub>1,0</sub>_R_<sub>0,1</sub>+_R_<sub>0,1</sub>_R_<sub>1,0</sub>=0 and \(((1-f)/\alpha)^2+(f/\alpha)^2=1\), and for \(\Pi_Q\), from _Q_<sub>0</sub> being an orthogonal projector. Hence, _B_ and \(\widetilde{B}\) are unitary, and \(\Sigma\) and _E_ are Hermitian involutions. Put \(V_1=|0\rangle\otimes V\) and \(V_2=|0\rangle\otimes V_1\), so that \(L=|0\rangle\otimes I_2\otimes V_2\), \(V_1^\dagger V_1=I\), and \(V_1Q_bV_1^\dagger=Q_0\). Since \(\Pi_QV_2=(Q_0V_1,(I-Q_0)V_1)\), \(V_2^\dagger\widetilde{B}V_2=V_1^\dagger BQ_0V_1=\)<tbc>

