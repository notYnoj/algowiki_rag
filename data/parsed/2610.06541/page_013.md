For regulated families, we keep the checkpoints and midpoint samples of Lemma 3.8 and truncate each sample with \(\mu\).

**Corollary 5.4.** _Let H be_ \(\sigma\)_-sparse on_ \[0_,T\], with coordinates of magnitude at most R. Let_ \(0<\varepsilon\le\sqrt{2}\sigma T\)_, let k be the least nonnegative integer with_ \(2^k\ge\sqrt{2}\sigma T/\varepsilon\)_, and let_ \(\mu\) _be a level measure with discrepancy_ \(D_R(\mu)\le 2^{-k-1}\)_. For checkpoints_ \(0=t_0\le\cdots\le t_n=T\)_, let A<sub>j</sub>=H_((_t<sub>j</sub>+t_<sub>_j_+1</sub>)/2) _and define_

\(W_\mu=e^{-i(t_n-t_{n-1})A_{n-1}^{(\mu)}}\dots e^{-i(t_1-t_0)A_0^{(\mu)}}.\)

(1) _If H is regulated, some checkpoints give_ \(\|W_\mu-U(T)\|\le\sqrt{2}\sigma 2^{-k}T\le\varepsilon\).<tbc>

(2) _For H of total variation_ \(0<\ell<\infty\)_, equal-variation checkpoints (Lemma 3.6) give this bound with_ \(n=\lceil 2^{k+1}\ell/(\sqrt{2}\sigma)\rceil\le 1+4T\ell/\varepsilon\).<tbc>

(3) _If H is L-Lipschitz with L\>_0_, uniform checkpoints t<sub>j</sub>=jT/n give the same bound with_ \(n=\lceil 2^{k+1}LT/(\sqrt{2}\sigma)\rceil\le 1+4LT^2/\varepsilon\).

_Proof._ The checkpoints and counts in Lemma 3.8 are independent of \(\mu\). For _t<sub>j</sub>\<t\<t_<sub>_j_+1</sub>, the oscillation bound in its proof gives \(\|H(t)-A_j\|\le\sqrt{2}\sigma 2^{-k-1}\), and Theorem 5.2 gives \(\|A_j-A_j^{(\mu)}\|\le\sqrt{2}\sigma D_R(\mu)\le\sqrt{2}\sigma 2^{-k-1}\). Thus, \(\|H(t)-A_j^{(\mu)}\|\le\sqrt{2}\sigma 2^{-k}\), and since the generators \(A_j^{(\mu)}\) are Hermitian, Lemma 2.4 and the choice of _k_ give the claimed error. □

We now turn to the assembly bound, which does not involve level measures. Because Duhamel’s estimate gives only an _O_(1) bound at unit steps, we compare a unitary path _U_ with a piecewise-constant evolution _V_ using corrections 1-_iY<sub>j</sub>_ on each piece.

**Theorem 5.5.** _For a partition_ \(0=a_0<\cdots<a_n=T\)_, let V_(0)=1 _evolve under constant Hermitian generators G<sub>j</sub> on_ (_a<sub>j</sub>,a_<sub>_j_+1</sub>)_. As in_ (2.2)_, V(T_)=_e_<sup>-_i(a<sub>n</sub>-a_<sub>_n_-1</sub>)_G_<sub>_n_-1</sub></sup>_...e_<sup>-_i(a_<sub>1</sub>-_a_<sub>0</sub>)_G_<sub>0</sub></sup>_. Let U be a unitary- valued function on_ \[0_,T_\] _with U_(0)=1_, and let Y_<sub>0</sub>_,...,Y_<sub>_n_-1</sub> _be matrices, with Y_<sub>-1</sub>=0_. Define M<sub>j</sub>=U_<sup>†</sup>(1-_iY<sub>j</sub>)V for_ \(j\in\{-1,0,\dots,n-1\}\)_, so M_<sub>-1</sub>=_U_<sup>†</sup>_V. If_ \(\|M_j(a_{j+1})-M_j(a_j)\|\le R_j\) _for_ \(0\le j<n\)_, then_

(5.1) \(\|V(T)-U(T)\|\le\sum_{j=0}^{n-1}(R_j+\|Y_j-Y_{j-1}\|)+\|Y_{n-1}\|.\)

_Proof._ Gluing constant evolutions gives the product, and by definition, _M_<sub>_n_-1</sub>=_U_<sup>†</sup>_V-iU_<sup>†</sup>_Y_<sub>_n_-1</sub>_V_ and _M_<sub>-1</sub>(_a_<sub>0</sub>)=1. Telescoping the corrected comparisons, with _Y_<sub>-1</sub>=0, gives

\(U(T)^\dagger V(T)-1=\sum_{j=0}^{n-1}\big[\big(U^\dagger(1-iY_j)V\big)(a_{j+1})-\big(U^\dagger(1-iY_j)V\big)(a_j)\big]\)<br>
\(-i\sum_{j=0}^{n-1}\big(U^\dagger(Y_j-Y_{j-1})V\big)(a_j)+i\big(U^\dagger Y_{n-1}V\big)(T).\)

Unitary invariance, \(\|V(T)-U(T)\|=\|U(T)^\dagger V(T)-1\|\), and the triangle inequality give (5.1). □

Thus, the piecewise-constant evolution _V_ stays close to the continuous evolution when the corrected comparison changes little across each piece and neighboring corrections nearly agree at shared endpoints. With _Y<sub>j</sub>_=0, this gives the fine-step comparison for any level measure in Corollary 5.4, and with the Hermitian frame of Section 6, it gives the unit-step comparison in Theorem 6.4.

## 6. Unit steps: from a product back to a continuous evolution

In this section, we hold the clock at finite precision using Section 5 to pass from products back to continuous evolutions. For separated samples, the comparison error is _O_(1_/T_), so continuous adiabatic bounds transfer, and we apply the transfer to quantum linear systems and to walks through their logarithms.

**Definition 6.1.** For integer \(T\ge 1\), let _H(s_) be a continuous Hamiltonian on \[0,1\]. Let _U_ evolve under _H(t/T_) on \[0_,T_\]. Set

(6.1) \(W_T=e^{-iH((T-1)/T)}\dots e^{-iH(0)}.\)

