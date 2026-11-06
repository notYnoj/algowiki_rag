The algorithm is a modification of the algorithm described in \[MV20\], and is not the main focus of our paper. We provide the details and proof in Appendix A for completeness, and will mostly use the algorithm as a black box. However we use two aspects of the algorithm explicitly:

(i) The algorithm produces an estimate _X_, and tests whether \(X\ge(1-\varepsilon)\tau\). If so, the output is _X_. Otherwise, the output is `FAIL`.<tbc>

(ii) The output _X_ satisfies \(X\le(1+\varepsilon)T+\varepsilon\tau\) with probability \(1-\delta-1/\mathrm{poly}(n)\).

From this point on, we let A be the algorithm promised by Theorem 3.1 and its space complexity \(s(m,\tau)\).

## 3.2 _O_(log_n_) pass algorithm

With a verified algorithm at hand, devising a parameter free _O_(log(_n_)) pass algorithm is simple: There are at most _m_<sup>3/2</sup> triangles in any graph, so execute A with \(\tau=m^{3/2}\). If the estimate was too large, set \(\tau_1=\frac{1}{2}m^{3/2}\) and execute A again, with \(\tau_1\) as a new guess of a lower bound. In each subsequent pass, we decrease our guess by a factor of 2, set \(\tau_j=2^{-j}m^{3/2}\) and execute A. Note that when _t_=log<sub>2</sub>(_m_<sup>3/2</sup>)=_O_(log(_n_)), \(\tau_t=1\), so there must be some _j_ where \(2\tau_j\ge T\ge\tau_j\). Therefore we terminate at pass _j=O_(log(_n_)). Formally, this is captured by the following claim.

**Claim 3.3.** _With probability_ \(1-\delta-1/\mathrm{poly}(n)\) LOGPASS _returns a_ \((1\pm\varepsilon)\) _estimate of T using O(s(m,T_)) _expected space._

_Proof._ Note that \(\tau_t=1\), so let _j_<sup>∗</sup> be the first time \(\tau_{j^*}\le T\). Then \(\mathcal{A}(\tau_{j^*})\) returns a \((1\pm\varepsilon)\) approximation of _T_. LOGPASS does not return a correct estimate if and only if at pass \(i\le j^*\), \(\mathcal{A}(\tau_i)\) did not succeed. This happens with probability at most \(\delta+1/\mathrm{poly}(n)\). So

\(\mathrm{Pr}\left[\mathrm{LOGPASS}\text{outputs a correct estimate}\right]=\mathrm{Pr}\left[\cap_{j\le j^*}\mathcal{A}\text{succeeds in pass}j\right]\)<br>
\(\ge 1-j^*\delta-j^*/\mathrm{poly}(n)\)<br>
\(\ge 1-O(\mathrm{log}(n)\delta)-1/\mathrm{poly}(n).\)

The result follows by rescaling \(\delta\).

Since \(s(m,\tau)\) is a decreasing function of \(\tau\), and \(\tau_j\) is a decreasing function of _j_, \(s(m,\tau_j)\) is an increasing function of _j_. Since the algorithm terminates at some pass _i_ with \(i\le j^*\), the expected space usage of LOGPASS is upper bounded by \(s(m,\tau_{j^*})=\widetilde{O}\left(\varepsilon^{-2}\delta^{-1}\left(\frac{m+T}{\sqrt{\tau_{j^*}}}\right)\right)=\widetilde{O}\left(\varepsilon^{-2}\delta^{-1}\left(\frac{m+T}{\sqrt{T}}\right)\right)\) where the last equality is since \(\tau_{j^*}\le T\le 2\tau_{j^*}\).

LOGPASS
Input: A random order stream S with |S|=m, a verified algorithm A.
Let t= (log(m3/2)) =O(log(n)).
At pass i [t], set = 2-i m3/2 and run A(S, T. If it returns FAIL, continue to the next pass. Otherwise, return its output as the estimate.
If all passes return FAIL, output 0.
Figure 1: An O(log(n))-pass parameter free triangle counting algorithm

