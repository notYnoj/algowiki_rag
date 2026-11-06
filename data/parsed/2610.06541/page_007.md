_Remark_ 2.10. Separation is a sampling condition on step length times eigenvalue differences. At an eigenvalue difference \(x=2\pi n\neq 0\), the averaging multiplier (_e<sup>ix</sup>_-1)/(_ix_) vanishes, so the exponential derivative is not invertible. In (2.5), the left multiplier _e<sup>ix</sup>_-1 vanishes, while integration by parts gives \(1/(2\pi in)\) on the right, so a nonzero entry of _D_ at that difference prevents a solution. A walk must choose its logarithm (Section 6.3), since for an orthogonal projector _P_ commuting with _H_, \(e^{-i(H+2\pi P)}=e^{-iH}e^{-2\pi iP}=e^{-iH}\) by \(e^{-2\pi iP}=1+(e^{-2\pi i}-1)P=1\).

## 3. Fine steps

In this section, we use Duhamel to match products at finite precision to continuous evolution, then Davis-Kahan to transfer leakage bounds. We start with bit truncation because it is concrete, and piecewise- constant truncations generate products directly. For other regulated paths, we hold truncated midpoint samples constant on chosen intervals, which gives the standard fine-step count.

### 3.1. Bit truncation.

**Definition 3.1** (Bit truncation)**.** Let _k_ be any integer. The _truncation at scale_ 2<sup>-_k_</sup> of a real number _x_ rounds its magnitude down to a multiple of 2<sup>-_k_</sup> and restores its sign:

\([x]_k=2^{-k}\text{trunc}(2^kx),\)

where trunc(_y_) removes the fractional part of _y_, rounding toward zero. A complex number is truncated in its real and imaginary parts, \([z]_k=[\Re z]_k+i[\text{Im}z]_k\). A matrix _H_ is truncated entry by entry, \(H_{pq}^{(k)}=[H_{pq}]_k\), and a family pointwise, _H_<sup>(_k_)</sup>(_t_)=_H(t_)<sup>(_k_)</sup>. For nonnegative _k_, this is _k_-bit truncation.

Binary precision is relative to a unit of energy, and changing the unit by a power of two moves the binary point and rescales time, preserving the evolution.

**Lemma 3.2.** _Let j be a nonnegative integer. The family_ \(t\mapsto 2^jH(2^jt)\) _on_ \[0,2<sup>-_j_</sup>_T_\] _has evolution_ \(t\mapsto U(2^jt)\)_, which equals U(T_) _at time_ 2<sup>-_j_</sup>_T. Moreover,_ \[2_<sup>j</sup>x_\]_<sub>k</sub>_=2_<sup>j</sup>_\[_x_\]<sub>_k+j_</sub> _for every real x and nonnegative integer k._

_Proof._ By the chain rule, \(i\frac{d}{dt}U(2^jt)=2^jH(2^jt)U(2^jt)\) wherever _U_ is differentiable at 2_<sup>j</sup>t_, which is at all but countably many _t_. The initial value is _U_(0)=1, so Lemma 2.4 with identical generators gives uniqueness. For the second claim, the definition of truncation gives \[2_<sup>j</sup>x_\]_<sub>k</sub>_=2<sup>-_k_</sup>trunc(2<sup>_k+j_</sup>_x_)=2_<sup>j</sup>_\[_x_\]<sub>_k+j_</sub>. □

We fix the energy unit henceforth (Lemma 3.2). Truncation preserves Hermiticity because \[-_x_\]_<sub>k</sub>_=-\[_x_\]_<sub>k</sub>_ and \([\bar{z}]_k=\overline{[z]_k}\), and its entrywise errors give the following norm bound.

**Lemma 3.3.** _For nonnegative k, if H is_ \(\sigma\)_-sparse, then_ \(\|H(t)-H^{(k)}(t)\|\le\sqrt{2}\sigma 2^{-k}\) _for every t._

_Proof._ Fix _t_ and suppress it. Truncation preserves Hermiticity and zeros, so _H-H_<sup>(_k_)</sup> is Hermitian with at most \(\sigma\) nonzero entries in each row. The real and imaginary parts of each entry have truncation errors below 2<sup>-_k_</sup>, so each entry has modulus less than \(\sqrt{2}2^{-k}\). The row-sum bound for Hermitian matrices therefore gives

\(\big\|H-H^{(k)}\big\|\le max_p\sum_q\big|H_{pq}-[H_{pq}]_k\big|\le\sqrt{2}\sigma 2^{-k}.\)

□

For piecewise-constant truncation, this bounds the induced product’s error.

**Lemma 3.4.** _Let H be regulated and_ \(\sigma\)_-sparse, with evolution U, and let k be a nonnegative integer. If H_<sup>(_k_)</sup> _is regulated, its evolution V satisfies_

\(\|V(t)-U(t)\|\le\sqrt{2}\sigma 2^{-k}t(0\le t\le T).\)

_In particular, whenever H_<sup>(_k_)</sup> _is piecewise constant, its induced product W=V(T_) _(Definition 2.1) satisfies_ \(\|W-U(T)\|\le\sqrt{2}\sigma 2^{-k}T\).

_Proof._ Truncation preserves Hermiticity, so Proposition 2.5 gives both evolutions, with _U_(0)=_V_(0)=1. By Lemma 3.3, \(\|H(s)-H^{(k)}(s)\|\le\sqrt{2}\sigma 2^{-k}\) for \(s\in[0,T]\). Applying Lemma 2.4 outside both countable exceptional sets and the endpoints and integrating over \[0_,t_\] gives \(\sqrt{2}\sigma 2^{-k}t\). For piecewise-constant truncation, gluing constant-generator evolutions gives _V(T_)=_W_, one exponential per piece (Definition 2.1), and we take _t=T_. □

