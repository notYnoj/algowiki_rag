<tbc>**Corollary A.2.** _Let O be a Hermitian involution, V an isometry, A=V_ <sup>†</sup>_OV positive definite, and_ \(\|b\|=1\)_. Assume, for some_ \(\kappa>1\)_, that every nonzero eigenvalue of H(f_) _has absolute value at least_ \(1-f+f/\kappa\) _for_ \(0\le f\le 1\) \[2, Appendix A\]_. Assume also the continuous multiplicity-one Jansen-Ruskai-Seiler theorem_ \[16, Theorem 3\]_. Use AQC_(3/2)_ with_

\(r=\sqrt{\kappa}-1,f(s)=\frac{1-(1+rs)^{-2}}{1-(1+r)^{-2}}.\)

_The walk W(s_) _of Definition A.1 uses one controlled O query per step. For the constant K\>_0 _of Lemma A.4:_

(1) _For every integer_ \(T\ge 1\),<tbc>

<tbc>\(\|(I-P(1))W((T-1)/T)\cdots W(0)P(0)\|\le\frac{K\kappa}{T},\)<tbc>

<tbc>_where P(s_) _projects onto the line through F<sub>s</sub>L_(\[(1-_f(s_))_I+f(s)A_\]<sup>-1</sup>_b,_0)_, a+i eigenvector of W(s). Thus, for_ \(0<\delta\le 1\), \(\lceil K\kappa/\delta\rceil\) _steps suffice for leakage at most_ \(\delta\).<tbc>

(2) _For_ \(0<\delta\le 1\)_, put_ \(N=\lceil 2K\kappa/\delta\rceil\)_. Starting from L(b,_0)_, apply controlled E(f_(0)) _with its control prepared in_ \((|0\rangle+i|1\rangle)/\sqrt{2}\) _and measured, succeeding on outcome_ \((|0\rangle+|1\rangle)/\sqrt{2}\)_, take N walk steps, and apply controlled E(f_(1)) _in the same way with the control prepared in_ \((|0\rangle-i|1\rangle)/\sqrt{2}\)_. The walk leakage is at most_ \(\delta/2\)_. Each endpoint succeeds with probability_ 1/2_, so joint success has probability_ 1/4_. Conditioned on success, the normalized output is within distance_ \(\delta\)_, up to a global phase, of L(A_<sup>-1</sup>_b/_\(\|A^{-1}b\|,0\))_. Each attempt uses_ \(N+2\le(2K+3)\kappa/\delta\) _controlled O queries, excluding preparing b, implementing Q<sub>b</sub>, and operations built from V ._

## A.3. Proof.

The proof cuts the walk’s logarithm in a \(\kappa\)-independent free arc, restricts it to a subspace with a rank-one solution band, and applies Theorem 6.5 and Lemmas A.3 and A.4.

_Proof._ By Lemma A.3, _E_ is a Hermitian involution with the compression stated before Corollary A.2.

For real _f_, \(\|A\|=\|V^\dagger OV\|\le 1\) gives \(\|H_0\|,\|H_1\|\le 1\) and hence \(\|H(f)\|\le|1-f|+|f|\le\sqrt{2}\alpha\) by Cauchy- Schwarz, so the compression norm is at most 1/2. For a compression eigenpair \((\lambda,v)\), \(WLv=2\lambda Lv-ELv\) and _WELv=Lv_ give the walk phases \(exp(\pm iarccos\lambda)\), \(\lambda\in spec(L^\dagger EL)\). On the complement of these invariant planes, _W_ acts as -_E_, with eigenvalues \(\pm 1\). Since \(arccos\lambda\in[\pi/3,2\pi/3]\), cutting _i_log inside the free phase arc \((0,\pi/3)\) gives, by the local inverse argument of Theorem 6.11, a _C_<sup>2</sup> Hermitian logarithm where 1+_rs\>_0, with spectrum in \([-2\pi,-\pi/3]\). The cut sends +_i_ to the logarithm eigenvalue \(-\pi/2\), and the gap bound \(1-f+f/\kappa=(1+rs)^{-2}\), by the formula for _f_, gives it gap at least \(1/[2\sqrt{2}\alpha(1+rs)^2]\) on \[0,1\]. Indeed, compression scales the gap of _H(f_) by \(1/(2\sqrt{2}\alpha)\), the phases \(e^{iarccos\lambda}\) have logarithm eigenvalues \(-arccos\lambda\) with \(|arccos\lambda-\pi/2|=|arcsin\lambda|\ge|\lambda|\), and the logarithm eigenvalues of \(e^{-iarccos\lambda}\) and \(\pm 1\) lie at least \(\pi/2\) from \(-\pi/2\).

Write \(\Lambda\) for the full logarithm, with majorants evaluated at \(w=5\pi/3\), and recall from Definition 2.8 that \(a_\Lambda(X)=i(\Lambda X-X\Lambda)\) and \(\Phi_\Lambda=\int_0^1e^{\tau a_\Lambda} d\tau\), and from Lemma 2.9(3) that \(\Phi_\Lambda^{-1}=\sum_{n\ge 0}(B_n/n!)a_\Lambda^n\). Splitting this integral at 1/2 gives \(\Phi_\Lambda=\frac{1}{2}(1+e^{a_\Lambda/2})\Phi_{\Lambda/2}\). Since these functions of \(a_\Lambda\) commute, \(2\Phi_{\Lambda/2}^{-1}=(1+e^{a_\Lambda/2})\Phi_\Lambda^{-1}\), which rearranges to the first identity below. Unitary conjugation \(e^{-a_\Lambda/2}\) preserves the norm, and the Bernoulli-series factors 2-2_<sup>n</sup>_ are 1,0 at _n_=0,1 and negative for \(n\ge 2\). Hence, using the closed form B(_x_)=2+_x/_2-(_x/_2)cot(_x/_2) (derived in the proof of Lemma A.4) and cot(_y/_2)-cot_y_=1/sin_y_,

\(\Phi_\Lambda^{-1}=\big(2\Phi_{\Lambda/2}^{-1}-\Phi_\Lambda^{-1}\big)e^{-a_\Lambda/2},\)<br>
\(2\Phi_{\Lambda/2}^{-1}-\Phi_\Lambda^{-1}=\sum_{n\ge 0}\frac{(2-2^n)B_n}{n!}(a_\Lambda/2)^n,\)<br>
\(\|\Phi_\Lambda^{-1}\|\le\mathcal{B}(w)-2\mathcal{B}(w/2)+2\)<br>
\(=\frac{w}{2}\big(cot\frac{w}{4}-cot\frac{w}{2}\big)=\frac{w/2}{sin(w/2)}.\)

Since sin(_w/_2)=1/2, the bound is \(5\pi/3\), sharper than the bound \(\mathcal{B}(5\pi/3)>9\) of Lemma 2.9. The identity \(\Lambda'=\Phi_\Lambda^{-1}(iW^\dagger W')\) (proof of Theorem 6.11) and its derivative, with \(\|(\Phi_\Lambda^{-1})'\|\le 2\mathcal{B}'\|\Lambda'\|\) (Lemma 2.9) and

