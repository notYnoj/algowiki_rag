_Proof._ The closed forms are proved in Appendix A. With _u_=1_/n_, \(nQ_1(n,1)=(3-3u+\sqrt{13-18u+9u^2})/2\). Its derivative in _u_ is \(-3/2+(9u-9)/(2\sqrt{13-18u+9u^2})<0\) for \(0<u\le 1/2\), so the size increases with _n_, and its value at _u_=0 is \((3+\sqrt{13})/2\). For the comparison with _C_<sub>2</sub>(_n,_1)=3_/n_ from Theorem 1, \(3(n-1)+\sqrt{13n^2-18n+9}>6n\) is equivalent to 13_n_<sup>2</sup>-18_n_+9_\>_9(_n_+1)<sup>2</sup>, that is to 4_n(n_-9)_\>_0.

The classical value with one comparison is _C_<sub>1</sub>(_n,r_)=_r/n+r(n-r)/(n(n_-1)) by Theorem 1. It is (10) with \(\zeta\) replaced by 1. Since \(\zeta\ge 1\), with equality only at _r=n_-1, one quantum comparison is strictly better than one classical comparison for \(1\le r\le n-2\).

The same formula gives the limiting alignment probability when the good-enough set occupies a fixed fraction of the designs.

**Corollary 3.** _Fix_ \(0<\varrho<1\) _and put_ \(r_n=\lfloor\varrho n\rfloor\)_. Then_<tbc>

\(lim_{n\rightarrow\infty} Q_1(n,r_n)=F_1(\varrho)=\varrho+\varrho(1-\varrho)\zeta(\varrho),\)

<tbc>_where_ \(\zeta(\varrho)\) _is the smallest positive root of_

\(H_\varrho(z)=2(1-2\varrho)z^3+12\varrho(1-\varrho)z^2-8(1-2\varrho)z-6=0.\) (11)

_In particular,_ \(F_1(1/2)=1/2+\sqrt{2}/4\) _and_ \(lim_{\varrho\downarrow 0}F_1(\varrho)/\varrho=(3+\sqrt{13})/2\).

_Proof._ Write \(r_n=\varrho n+e_n\), where \(-1<e_n\le 0\). Dividing _F<sub>n,r<sub>n</sub></sub>_ in (9) by _n_<sup>2</sup> gives coefficientwise convergence to \(H_\varrho\), since every remaining term has a bounded coefficient times 1_/n_ or 1_/n_<sup>2</sup>. Let \(\zeta_n\) be the root selected in Theorem 3. If \(\varrho<1/2\), then \(1<\zeta_n<3\) for all sufficiently large _n_. The signs of the coefficients of \(H_\varrho\) are +,+,-,-, so it has exactly one positive root. Every subsequential limit of \(\zeta_n\) is a root of \(H_\varrho\) in \[1,3\], and thus the whole sequence converges to that positive root. At \(\varrho=1/2\), the same boundedness holds for both parities of _n_, and the limiting polynomial is 3_z_<sup>2</sup>-6. Its only root in \[1,3\] is \(\sqrt{2}\).

For \(\varrho>1/2\), put \(a=2\varrho-1\in(0,1)\). Theorem 3 gives \(1<\zeta_n<(n-2)/(2r_n-n)\) for all sufficiently large _n_. The upper endpoint tends to 1_/a_. Moreover, \(H_\varrho(1)=-12(1-\varrho)^2<0\) and \(H_\varrho(1/a)=a^{-2}-1>0\). The negative leading coefficient gives a second positive root above 1_/a_, and Descartes’ rule permits at most two. There is therefore exactly one root in \[1,1_/a_\], and it is the smallest positive root. Boundedness and coefficient convergence again give \(\zeta_n\rightarrow\zeta(\varrho)\). Substitution in (10) proves the asserted limit for every \(0<\varrho<1\).

The value at 1/2 follows from \(\zeta(1/2)=\sqrt{2}\). As \(\varrho\downarrow 0\), the selected root remains in \[1,3\], and _H_<sub>0</sub>(_z_)=2(_z_+1)(_z_<sup>2</sup>-_z_-3) has only one root in this interval. Consequently \(\zeta(\varrho)\rightarrow(1+\sqrt{13})/2\), which gives the stated small-fraction limit.

The proof of Theorem 3 in Appendix A uses the same moment matrices for the upper bound and the attaining construction. The state after one call is a linear image of the feature vector \(\phi_x=|0\rangle+\sum_{i<j}\mathrm{sgn}(x_i-x_j)e_i\wedge e_j\), so the success of any algorithm is \(\sum_i\mathrm{tr}(M_iB_i)\) for target-conditioned moment matrices _M<sub>i</sub>_ and positive semidefinite matrices _B<sub>i</sub>_ whose sum is a nonnegative diagonal matrix of trace one. This is the one-query case of the semidefinite characterization of quantum query algorithms \[31\], reduced by label symmetry. The moment matrices _M<sub>i</sub>_ decompose into explicit \(2\times 2\) blocks under label permutations. A dual matrix \(\mathcal{L}\unknown M_i\) with constant diagonal then gives an upper bound for every algorithm, and an explicit covariant state and measurement attain the bound. The value \(\zeta\) is the root at which the diagonal of L becomes constant.

