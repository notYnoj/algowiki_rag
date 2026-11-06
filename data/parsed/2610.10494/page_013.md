## Appendix C. Finite separation of a shared leg

We adapt the construction of \[9, Proposition 3.1\] with an equal-sums filter, reducing the copy count from 5_M_ to 2_M_. It suffices to share leg _X_. Write<tbc>

\(T=\sum_{h=1}^M\sum_{a,b,c}\mu_{habc}x_ay_{hb}z_{hc}.\)

<tbc>Take _L_=2_M_ copies and a primitive _L_-th root of unity \(\zeta\). In copy \(\ell=0,\dots,L-1\), make the substitutions<tbc>

\(x_a^{(\ell)}\longmapsto\sum_{g=1}^M\zeta^{\ell g}X_{ag},\)<br>
\(y_{hb}^{(\ell)}\longmapsto\sum_{u=1}^M\zeta^{\ell(u-h)}Y_{hbu},\)<br>
\(z_{hc}^{(\ell)}\longmapsto\frac{1}{L}\sum_{v=1}^M\zeta^{-\ell v}Z_{hcv}.\)

<tbc>Summing the copies multiplies each coefficient by

\(\frac{1}{L}\sum_{\ell=0}^{L-1}\zeta^{\ell(g+u-h-v)}.\)

The geometric sum is one for exponent divisible by _L_ and zero otherwise. Since \(|g+u-h-v|\le 2(M-1)<L\), it retains precisely _g+u=h+v_.

Now give _X<sub>ag</sub>,Y<sub>hbu</sub>,Z<sub>hcv</sub>_ respective weights _g_<sup>2</sup>, 2_hu-h_<sup>2</sup>, and -2_hv_. On every retained term their total is<tbc>

\(g^2+2h(u-v)-h^2=(g-h)^2\ge 0.\)

<tbc>The weight-zero terms have _g=h_ and _u=v_, so the limit is

\(\sum_{h,a,b,c,u}\mu_{habc}X_{ah}Y_{hbu}Z_{hcu}=\oplus_h(T_h\otimes B_X(M)).\)

Every leg now distinguishes _h_. Although individual weights may be negative, the transformed coefficients form a polynomial of degree at most (_M_-1)<sup>2</sup>. This proves (5).

## Appendix D. Interpolation of a degeneration

For completeness, we give the standard interpolation proof \[2, Theorem 8\].

_Proof of Lemma 3.1._ Let \(P(\varepsilon)\) be the tensor obtained from _T_ by the degeneration’s substitutions. Its coefficients are polynomials in \(\varepsilon\) of degree at most _L_, and _P_(0)=_S_. Thus _L_ describes the chosen degeneration. For every \(\varepsilon\neq 0\), \(P(\varepsilon)\) is a restriction of _T_. Put \(Q(\varepsilon)=P(\varepsilon)^{\otimes N}\). Each coefficient of _Q_ is a product of _N_ coefficients of _P_, so its degree is at most _NL_, and \(Q(0)=S^{\otimes N}\).

Choose _NL_+1 distinct nonzero points \(\varepsilon_0,\dots,\varepsilon_{NL}\). Lagrange interpolation, applied to every coefficient, gives<tbc>

\(S^{\otimes N}=Q(0)=\sum_{j=0}^{NL}c_jQ(\varepsilon_j),c_j=\prod_{0\le h\le NLh\neq j}\frac{-\varepsilon_h}{\varepsilon_j-\varepsilon_h}.\)

