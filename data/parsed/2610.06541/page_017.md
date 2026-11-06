**Corollary 6.9.** _Assume the continuous multiplicity-one Jansen-Ruskai-Seiler theorem_ \[16, Theorem 3\]_. Let A be Hermitian positive definite with_ \(\|A\|=1\) _and condition number_ \(\kappa\ge 1\)_, and let_ \(\|b\|=1\)_. With_ \(Q_b=1-|b\rangle\langle b|\)_, let H_=(1-_f)H_<sub>0</sub>+_fH_<sub>1</sub> _be the An-Lin path with the AQC_(3/2) _schedule of Definition 6.8 and P(s_) _the projector onto_ (\[(1-_f(s_))+_f(s)A_\]<sup>-1</sup>_b,_0)_, where_<tbc>

\(H_0=\left(\begin{array}{ c c }
0 & Q_b \\
Q_b & 0
\end{array}\right),H_1=\left(\begin{array}{ c c }
0 & AQ_b \\
Q_bA & 0
\end{array}\right).\)

<tbc>_Assume An and Lin’s gap bound_ \[2, Appendix A\]_: the nonzero eigenvalues of H(s_) _are at distance at least_ \(g(s)=1-f(s)+f(s)/\kappa\) _from_ 0_. If_ \(\kappa>1\)_, then, for every integer_ \(T\ge 1\)_, the product_ (6.1) _satisfies_

\(\|(1-P(1))W_TP(0)\|\le\frac{5J_1(|f'|,|f''|,g)}{4T}\le\frac{45\kappa}{T},\)

_with the Jansen-Ruskai-Seiler coefficient J_<sub>1</sub> _of Definition 3.14. If_ \(\kappa=1\)_, then_ (1-_P_(1))_W<sub>T</sub>P_(0)=0_. Thus, for_ \(\delta>0\), \(\lceil 45\kappa/\delta\rceil\) _unit steps give leakage at most_ \(\delta\).

_Proof._ The block norm bound \(\big\|\big(_{B^\dagger}^0B_0^B\big)\big\|\le\|B\|\) and \(\|Q_b\|,\|A\|,\|1-A\|\le 1\) give \(\|H_0\|,\|H_1\|,\|H_1-H_0\|\le 1\). Since \(0\le f\le 1\), convexity gives \(\|H\|\le 1\), hence width at most 2. In block form, _H_ has off-diagonal blocks \[(1-_f_)+_fA_\]_Q<sub>b</sub>_ and its adjoint, with (1-_f_)+_fA_ positive, so the range of _P(s_) and (0_,b_) span the kernel of _H(s_), and _HP=PH_=0. If \(\kappa=1\), positivity and \(\|A\|=\|A^{-1}\|=1\) give _A_=1, so the path is constant and every step acts as the identity on its kernel.

Assume \(\kappa>1\), and put \(J=J_1(|f'|,|f''|,g)\) and \(S=|(0,b)\rangle\langle(0,b)|\). Since _HS=SH_=0 and _SP(s_)=0, the operator _H+S_ has derivatives \(f'(H_1-H_0)\) and \(f''(H_1-H_0)\), of norms at most \(|f'|\) and \(|f''|\), the simple eigenvalue 0 with projector _P(s_), and gap at least _g_, since _S_ moves (0_,b_) to eigenvalue \(1\ge g\). Its evolution _U(t)e_<sup>-_itS_</sup> agrees with _U(t_) on ran_P_(0), so Jansen-Ruskai-Seiler, whose coefficient increases with the derivative norms, gives leakage at most _J/T_.

With _L_=2(1+_r_)<sup>2</sup>/(_r_+2), differentiation, 1-(1+_r_)<sup>-2</sup>=_r(r_+2)/(1+_r_)<sup>2</sup>, and \(\kappa=(1+r)^2\) give _g_=(1+_rs_)<sup>-2</sup>, \(f'=L(1+rs)^{-3}\), and \(f''=-3rL(1+rs)^{-4}\), hence the bounds \(\|H'\|\le L\) and \(\|H''\|\le 3rL\). The width-2 specialization in Theorem 6.4, with _c<sub>i</sub>=c<sub>i</sub>_(2) and \(\nu=\frac{3}{2}rL\), gives comparison error at most \(E=(c_0L+c_1L^2+\frac{3}{2}c_2rL)/T\). By Theorem 6.5, leakage is at most _J/T+E_. Evaluating (3.1) at _m_=1, the endpoint terms \(f'(0)/g(0)^2=L\) and \(f'(1)/g(1)^2=L(1+r)\) and constant integrands \(|f''|/g^2=3rL\) and \(7f'^2/g^3=7L^2\) give

\(J=L+L(1+r)+3rL+7L^2=(4r+2)L+7L^2\le 36\kappa,\)

using \(L\le 2(1+r)\) and \(4r+2\le 4(1+r)\).

Since \(\pi>3\), the bounds (6.4) give \(\mathcal{N}(2)\le 1/8\) and \(\mathcal{N}'(2)\le 1/64\), so (6.3) gives \(c_0,c_2\le 1/2\) and \(c_1\le 1/64+1/32+1/32=5/64\). Since _r,L\>_0, these bounds give \(TE\le J/4\) term by term:

\(c_0L\le\frac{L+L(1+r)}{4},c_1L^2\le\frac{5L^2}{64}\le\frac{7L^2}{4},c_2\frac{3rL}{2}\le\frac{3rL}{4}.\)

Adding gives leakage at most \(5J/(4T)\le 45\kappa/T\le\delta\) when \(T\ge 45\kappa/\delta\). □

## 6.3. Walks.

We extend the comparison to walks through their logarithms. Since a unitary determines its eigenphases only modulo \(2\pi\) (Remark 2.10), we choose a logarithm with a branch cut in a common open arc free of spectrum.

**Definition 6.10.** A _walk_ is an ordered sequence of unitaries. The walk is _compatible_ with a differentiable unitary-valued family _W_ on \[0,1\] when its _T_ steps are _W(j/T_), with product<tbc>

\(W_T=W((T-1)/T)\cdots W(0).\)

<tbc>**Theorem 6.11.** _Let_ \(T\ge 1\) _be an integer, let_ \(w<2\pi\)_, and let W be differentiable and unitary on_ \[0,1\]_, with_ \(\|W'\|\le L\) _and_ \(\|W'(s)-W'(s')\|\le 2\nu|s-s'|\)_. Suppose that some open arc of length_ \(2\pi-w\) _meets the spectrum of no W(s). Then there is a differentiable Hermitian path_ \(\Lambda\) _on_ \[0,1\] _with_ \(e^{-i\Lambda}=W\) _such that, for the product W<sub>T</sub> of the compatible walk and evolution_ \(U_\Lambda\) _of_ \(\Lambda(t/T)\),<tbc>

\(\big\|W_T-e^{i\Lambda(1)/2}U_\Lambda(T)e^{-i\Lambda(0)/2}\big\|\le\frac{c_0L_\Lambda+c_1L_\Lambda^2+c_2\nu_\Lambda}{T},\)

