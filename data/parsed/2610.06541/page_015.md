Hence, \(c_0(w),c_2(w)\le\frac{1}{4}+4/(\pi\gamma)\) and \(c_1(w)\le\frac{1}{64}+1/(2\pi\gamma)+4/(\pi\gamma^2)\). Eigenvalue differences near nonzero multiples of \(2\pi\) therefore give large constants, because errors whose phase advances by \(\gamma\) per step can add for about \(1/\gamma\) steps before cancelling.

Rescaling cannot remove separation, a condition on step length times eigenvalue differences (Remark 2.10), because scaling _H_ by _c_ changes each factor to _e_<sup>-_icH(j/T_)</sup> and hence the product itself.

**Theorem 6.4.** _Let T, H, U, and W<sub>T</sub> be as in Definition 6.1. Suppose that H is differentiable,_ \(\left\|H'\right\|\le L\), \(\left\|H'(s)-H'(s')\right\|\le 2\nu|s-s'|\)_, and each sample H(j/T),_ 0_\<j\<T, is_ \(\gamma\)_-separated of width at most_ \(\bar{w}\) _(Definition 2.8). Then_

\(\left\|W_T-e^{iH(1)/2}U(T)e^{-iH(0)/2}\right\|\le\frac{c_0L+c_1L^2+c_2\nu}{T},\)

_with c<sub>i</sub> from Definition 6.3, or c<sub>i</sub>(w_) _for width at most_ \(w<2\pi\).

_Proof._ For each full piece, set _h<sub>j</sub>=H(j/T_), \(D_j=H'(j/T)/T\), \(\Delta_j(\tau)=H((j+\tau)/T)-h_j\), and \(Y_j=\Theta_{h_j}(D_j)\), and let _R<sub>j</sub>_ be the integral in Lemma 6.2(2) with \(N_\gamma\) for _N_. By Lemma 6.2(1), the varying correction equals _Y<sub>j</sub>_ at both endpoints, so _R<sub>j</sub>_ bounds the increment with constant _Y<sub>j</sub>_ in (5.1). With _Y_<sub>-1</sub>=_Y_<sub>0</sub>=_Y<sub>T</sub>_=0 and _M<sub>j</sub>=U_<sup>†</sup>(1-_iY<sub>j</sub>)V_ as in Theorem 5.5, Lemma 2.4 bounds the two half-piece increments by _B<sub>T</sub>_. In (5.1) over _T_+1 pieces, the last jump is \(\left\|Y_{T-1}\right\|\) and the final correction vanishes, giving, by (6.2), the error bound

\(B_T=\int_0^{1/2}\left\|H(t/T)-H(0)\right\|dt+\int_{T-1/2}^T\left\|H(t/T)-H(1)\right\|dt,\)<br>
\(E_T=B_T+\sum_{j=1}^{T-1}(R_j+\left\|Y_j-Y_{j-1}\right\|)+\left\|Y_{T-1}\right\|.\)

Since \(\Delta_j(\tau)-\tau D_j=\int_0^\tau\left(H'((j+s)/T)-H'(j/T)\right)ds/T\), integrating the derivative bounds gives \(\left\|\Delta_j\right\|\le L|\tau|/T\), \(\left\|D_j\right\|\le L/T\), and \(\left\|\Delta_j-\tau D_j\right\|\le\nu\tau^2/T^2\), so \(B_T\le L/(4T)\) and

\(R_j\le\int_{-1/2}^{1/2}\big[\frac{\nu\tau^2}{T^2}+\omega(\tau)\frac{L^2|\tau|}{T^2}\big]d\tau=\frac{\nu/12+(N_\gamma/4+1/64)L^2}{T^2},\)

by \(\int_{-1/2}^{1/2}\tau^2d\tau=1/12\) and \(\int_{-1/2}^{1/2}|\tau|\omega(\tau)d\tau=N_\gamma/4+1/64\). The derivative hypotheses give \(\left\|D_j-D_{j-1}\right\|\le 2\nu/T^2\) and \(\left\|h_j-h_{j-1}\right\|\le L/T\). Hence, Lemma 2.9 bounds the end frames by \(N_\gamma L/T\) and each internal jump by \(N_\gamma\left\|D_j-D_{j-1}\right\|+N'_\gamma\left\|h_j-h_{j-1}\right\|\left\|D_{j-1}\right\|\le(2N_\gamma\nu+N'_\gamma L^2)/T^2\). For \(T\ge 2\), adding _B<sub>T</sub>_, the _T_-1 pieces, the two end frames, and the _T_-2 internal jumps gives

\(E_T\le\frac{L}{4T}+(T-1)\frac{\nu/12+(N_\gamma/4+1/64)L^2}{T^2}+\frac{2N_\gamma L}{T}+(T-2)\frac{2N_\gamma\nu+N'_\gamma L^2}{T^2}\)<br>
\(\le\frac{c_0L+c_1L^2+c_2\nu}{T}\text{by (6.3)}.\)

For _T_=1, \(E_T=B_T\le L/4\), and the width specialization follows from Lemma 2.9(2). □

Thus, a product of steps of length one agrees with the path’s own evolution, up to two half-step phases and _O_(1_/T_) error. Since these phases preserve the endpoint spectral subspaces, we can transfer continuous adiabatic bounds to the product.

**Theorem 6.5.** _With the hypotheses and constants of Theorem 6.4, let P,Q be orthogonal projectors commuting with H_(0)_,H_(1)_, respectively, for example their spectral projectors. Then_

\(\left|\left\|(1-Q)W_TP\right\|-\left\|(1-Q)U(T)P\right\|\right|\le\frac{c_0L+c_1L^2+c_2\nu}{T}.\)

_In particular, if a continuous adiabatic theorem bounds by_ \(\varepsilon\) _the leakage_ \(\left\|(1-Q)U(T)P\right\|\) _of H over the time T, then_ \(\left\|(1-Q)W_TP\right\|\le\varepsilon+(c_0L+c_1L^2+c_2\nu)/T\).

_Proof._ The endpoint commutations and unitary invariance give<tbc>

\(\left\|(1-Q)e^{iH(1)/2}U(T)e^{-iH(0)/2}P\right\|=\left\|(1-Q)U(T)P\right\|.\)

