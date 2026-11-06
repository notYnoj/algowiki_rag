\(\le\frac{3}{4}\left(1+\frac{1}{2}\varepsilon\right)t^{-3}\tau_j\)

<tbc>where the last inequality holds when \(\varepsilon<1/10\). Therefore<tbc>

\((1-\varepsilon)(1-\varepsilon)t^{-3}\tau_j\le X\le\frac{3}{4}\left(1+\frac{1}{2}\varepsilon\right)t^{-3}\tau_j\)

<tbc>Contradiction when \(\varepsilon<1/10\). Therefore, \(\tau_j/2\le T\le\tau_j\), and the output _X_ satisfies

\((1-\varepsilon)^2t^{-3}T\le(1-\varepsilon)^2t^{-3}\tau_j\le X\le(1+\varepsilon)t^{-3}[T+\varepsilon max(T,\tau^*)]+2\varepsilon t^{-3}T\le(1+\varepsilon)(1+4\varepsilon)t^{-3}T.\)

Rescaling \(\varepsilon\) gets the desired result.

We now analyze the probability of success. Let R be the event that all segments are representative. By the union bound over all segments and 4.1, \(Pr\left[\mathcal{R}\right]\ge 1-t/n^4\ge 1-O(log(n)/n^4)\ge 1-1/n^3\). Let M be the event that the output of ONEPASS is a \((1\pm\varepsilon)\) approximation of _T_. For each _j_, let E<sub>A_,j_</sub> be the event that A succeeds on segment _S<sub>j</sub>_. Conditioned on R, if E<sub>A_,i_</sub> hold for all _i_, then ONEPASS succeeds. That is,<tbc>

\(Pr\left[\mathcal{M}|\mathcal{R}\right]\ge Pr\left[\cap_{i\le t}\mathcal{A}(S_i)\text{succeeds}|\mathcal{R}\right]\ge(1-t\delta-t/poly(n))\ge(1-O(log(n)\delta))-1/poly(n)).\)

<tbc>We conclude

\(Pr\left[\mathcal{M}\right]\ge Pr\left[\mathcal{M}|\mathcal{R}\right]\cdot Pr\left[\mathcal{R}\right]\ge(1-O(log(n)\delta))-1/poly(n))(1-n^{-3}).\)

Rescaling \(\delta\) provides the desired result.

**Corollary 3.6.** _If_ ONEPASS _returns FAIL, then with probability_ \(1-\delta-1/poly(n)\), \(T=\widetilde{O}(n)\).

_Proof._ Suppose \(T\ge\tau^*\). Then there exists some \(\tau_j\) such that \(T\ge\tau_j\). By 3.4, ONEPASS terminates and outputs an approximation of _T_. Equivalently, if ONEPASS did not output an estimate, then \(T<\tau^*=\widetilde{O}(n)\).

## 4 _p_ Pass Algorithm

In this section, we prove the main theorem below.

**Theorem 4.1** (_p_-pass Mixed Approximation Algorithm)**.** _Let S be a stream of edges representing a simple graph G with n vertices, m edges and T triangles. Then there exists an O(p_) _pass algorithm that uses expected_ \(\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(\frac{m+T}{\sqrt{T}}\right)\right)\) _space, and with probability_ \(1-\delta-1/poly(n)\) _outputs a mixed_ \((1+\varepsilon,\widetilde{O}(n^{1/2^p}))\) _approximation of T. The algorithm does not require any prior knowledge of T._

**Remark 4.2.** _If T\<m, the space bound simplifies to_ \(\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(m/\sqrt{T}\right)\right)\).

**Remark 4.3.** _In fact, our algorithm may terminate in fewer than O(p_) _passes, in which case we are guaranteed a_ \(1+\varepsilon\) _multiplicative approximation._

