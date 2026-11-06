<tbc>For the fine-step comparison and its adiabatic consequences, we use two standard facts. First, if _U_ and _V_ are the evolutions of _H_ and _G_ starting at the identity, differentiation gives<tbc>

\(\frac{d}{dt}(U^\dagger V)=iU^\dagger(H-G)V.\)

<tbc>Integrating gives, in the operator norm used throughout, the Duhamel estimate (Lemma 2.4, \[4\])

\(\|U(T)-V(T)\|\le\int_0^T\|H(t)-G(t)\|dt\le Tsup_t\|H(t)-G(t)\|.\)

Our second tool is the Davis-Kahan \(sin\Theta\) theorem \[10\]. A continuous adiabatic theorem bounds the leakage between spectral subspaces of _H_(0) and _H(T_), the largest norm, over unit vectors in the initial subspace, of the evolved vector’s component outside the final subspace (Definition 2.6). If these endpoint subspaces are instead taken from the truncated matrices, Davis-Kahan bounds their change by the Hamiltonian error divided by the spectral gap (Theorem 2.7), and this change adds to the leakage bound.

## 1.1. Main results.

We summarize the comparisons informally, calling a matrix \(\sigma\)-sparse when each row has at most \(\sigma\) nonzero entries (Definition 2.2).

**"Theorem" A.** _Let H be a regulated,_ \(\sigma\)_-sparse Hermitian family on_ \[0_,T_\]_, with evolution U starting at the identity. If its entrywise k-bit truncation H_<sup>(_k_)</sup> _is piecewise constant, the induced product W, one exponential per constant piece, satisfies_

\(\|W-U(T)\|\le\sqrt{2}\sigma 2^{-k}T.\)

Otherwise, we use truncated midpoint samples (Lemma 3.8).

**"Theorem" B.** _For a regulated,_ \(\sigma\)_-sparse Hermitian family H on_ \[0_,T_\] _with total variation_ \(0<\ell<\infty\)_, holding truncated midpoint samples between equal-variation checkpoints gives a product within_ \(\varepsilon\) _of U(T), with_ \(O(T\ell/\varepsilon)\) _factors and_ \(O(log_2(\sigma T/\varepsilon))\) _bits as_ \(\varepsilon\rightarrow 0\).

To apply this comparison, traverse a fixed path over time _T_, preserving its variation \(\ell\). If a continuous theorem bounds leakage between its endpoint subspaces by _C/T_, with _C\>_0 depending on the path, choosing _T_ proportional to \(C/\delta\) and evolution error proportional to \(\delta\) gives leakage \(O(\delta)\). The standard fine-step count is \(O(\ell C/\delta^2)\), with about \(2log_2(1/\delta)\) bits for fixed \(\sigma\), _C_, and \(\ell\) (Corollary 3.15).

Bit precision is one choice of levels for holding values fixed, and the layer-cake construction, which allows other levels and also applies to time, starts from the identity \[20\]

\(x=\int_{(0,\infty)}\mathbf{1}_{\{\lambda\le x\}}d\lambda(x\ge 0).\)

Replacing \(d\lambda\) by positive point masses, finitely many in each bounded range, gives a step function _F(x_). Applied to magnitudes of entries’ real and imaginary parts, with signs restored, its discrepancy |_F(x_)-_x_| controls Hamiltonian error. Equal masses 2<sup>-_k_</sup> at positive multiples of 2<sup>-_k_</sup> recover bit truncation (Section 5).

Holding the clock, rather than the entries, at finite precision gives the converse comparison, in which a product of unit-step samples approximates the path’s own continuous evolution, up to two half-step phases and _O_(1_/T_) under the hypotheses below. Take a Hermitian family _H_ on \[0,1\], with _U_ evolving under _H(t/T_) for \(0\le t\le T\), and for integer \(T\ge 1\) put

\(W_T=e^{-iH((T-1)/T)}\cdots e^{-iH(1/T)}e^{-iH(0)}.\)

Unit masses at the positive half-integers give the rounded clock \(q(t)=\lfloor t+1/2\rfloor\), so _H(q(t)/T_) holds each sample on a centered unit interval, with half intervals at 0 and _T_. Its evolution is exactly \(e^{-iH(1)/2}W_Te^{iH(0)/2}\) at time _T_.

Direct Duhamel comparison integrates an _O_(1_/T_) Hamiltonian error over time _T_ and gives only an _O_(1) bound, so instead a Hermitian correction, the frame, cancels first-order changes within each centered interval and takes equal values at its ends. The second-order remainder and neighboring-frame differences contribute _O_(1_/T_<sup>2</sup>) per interval, and the ends contribute _O_(1_/T_) (Lemma 6.2 and Theorem 5.5). Separation of the samples’ eigenvalue differences from nonzero multiples of \(2\pi\) bounds the frame (Lemma 2.9 and Remark 2.10).

