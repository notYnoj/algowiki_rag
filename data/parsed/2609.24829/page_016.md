**Corollary 4.6.** _Suppose that during round i,_ p-PASS _terminates and outputs_ \(t^3\widehat{T}_\mathrm{L}+\widehat{T}_\mathrm{H}\)_, and let_ \(\tau_j\) _be the guess at which_ A _returned an estimate. Then, on the success event of Lemma 4.3,_ \(\tau_j/2\le T_\mathrm{L}\le 2\tau_j\).

_Proof._ If \(T_\mathrm{L}<\tau_j\), the analysis of the second case in Lemma 4.5 shows \(\tau_j/2\le T_\mathrm{L}\le\tau_j\). Otherwise \(T_\mathrm{L}\ge\tau_j\), and _j_ is the first such index: at the first index _j_<sub>0</sub> with \(\tau_{j_0}\le T_\mathrm{L}\), the input \((1-\varepsilon)t^{-3}\tau_{j_0}\) is a lower bound on \(T_{j_0}^\mathrm{L}\), so A outputs an estimate there. We claim \(\tau_{j-1}\le 2\tau_j\): if \(\tau_j=2^{-j}m_\mathrm{L}^{3/2}\) then \(\tau_{j-1}=2\tau_j\), and if \(\tau_j=\tau^*\) then \(2^{-j}m_\mathrm{L}^{3/2}\le\tau^*\), so \(\tau_{j-1}=\mathrm{max}(2^{-(j-1)}m_\mathrm{L}^{3/2},\tau^*)\le 2\tau^*=2\tau_j\). Hence \(\tau_j\le T_\mathrm{L}<\tau_{j-1}\le 2\tau_j\).

**Corollary 4.7.** _Suppose that in round i,_ p-PASS _did not output_ \(t^3\widehat{T}_\mathrm{L}+\widehat{T}_\mathrm{H}\)_. Then with probability at least_ \(1-\delta-1/\mathrm{poly}(n)\), \(T_\mathrm{L}<\tau^*\)_. Moreover, if_ p-PASS _did not terminate,_ \(T_\mathrm{L}=\widetilde{O}(\varepsilon^{-2}n^{1/2^i})\).

_Proof._ Suppose \(T_\mathrm{L}\ge\tau^*\). By definition \(\tau_t=\tau^*\le T_\mathrm{L}\), so some executed guess satisfies \(\tau_j\le T_\mathrm{L}\). On the success event of Lemma 4.3, at the first such _j_ the input \((1-\varepsilon)t^{-3}\tau_j\) is a lower bound on \(T_j^\mathrm{L}\), so A outputs an estimate and the algorithm outputs \(t^3\widehat{T}_\mathrm{L}+\widehat{T}_\mathrm{H}\). The contrapositive implies the first part of the corollary. If p-PASS did not terminate, then in particular it did not output \(\widehat{T}_\mathrm{H}\) at the end of the stream, so \(T_\mathrm{L}<\tau^*=U_i=\widetilde{O}(\varepsilon^{-2}n^{1/2^i})\).

**Lemma 4.6** (Termination with \(\widehat{T}_\mathrm{H}\))**.** Suppose p-PASS terminates at round _i_ and outputs \(\widehat{T}_\mathrm{H}\). Then with probability \(1-\delta-1/\mathrm{poly}(n)\) it is a \((1\pm\varepsilon)\) approximation of _T_.

_Proof._ Suppose p-PASS terminates at round _i_ and outputs \(\widehat{T}_\mathrm{H}\). By the algorithm’s design, \(\tau^*=\varepsilon\widehat{T}_\mathrm{H}\), and by 4.7, \(T_\mathrm{L}<\varepsilon\widehat{T}_\mathrm{H}\). Note that by 4.4, \(\varepsilon\widehat{T}_\mathrm{H}\le\varepsilon(1+\varepsilon)T_\mathrm{H}\le 2\varepsilon T_\mathrm{H}\). Therefore<tbc>

\(T=T_\mathrm{H}+T_\mathrm{L}\le T_\mathrm{H}+2\varepsilon T_\mathrm{H}\le T_\mathrm{H}+2\varepsilon T,\)

<tbc>hence

\((1-2\varepsilon)T\le T_\mathrm{H}\le(1+2\varepsilon)T.\)

That is, the output \(\widehat{T}_\mathrm{H}\) is an approximation of _T_<sub>H</sub>, which in turn is an approximation of _T_, proving the claim. The probabilistic analysis is shown in 4.3.

We are ready to prove the correctness of p-PASS.

**Theorem 4.8** (Correctness of p-PASS.)**.** _With probability_ \(1-\delta-1/\mathrm{poly}(n)\), p-PASS _outputs a_ \((1+4\varepsilon,\widetilde{O}\left(\varepsilon^{-2}n^{1/2^p}\right))\) _one-sided approximation of T._

_Proof._ If the algorithm terminated during some round _i_, then by 4.6 and 4.5, the output is a \((1\pm\varepsilon)\) approximation of _T_, and the result follows from 4.4. Otherwise, the output is \((1-\varepsilon)^{-1}(\widehat{T}_\mathrm{H}+U_p)\). Since p-PASS did not terminate during round _p_, by 4.7 \(T_\mathrm{L}\le U_p\). Therefore<tbc>

\(\widehat{T}_\mathrm{H}+U_p\ge(1-\varepsilon)T_\mathrm{H}+(1-\varepsilon)T_\mathrm{L}\ge(1-\varepsilon)T\)

<tbc>showing the lower bound. As for the upper bound, \(\widehat{T}_\mathrm{H}\le(1+\varepsilon)T_\mathrm{H}\), therefore

\((1-\varepsilon)^{-1}(\widehat{T}_\mathrm{H}+U_p)\le\frac{1+\varepsilon}{1-\varepsilon}T_\mathrm{H}+O(U_p)\le(1+4\varepsilon)T+O(U_p).\)

The result follows by recalling that \(U_p=\widetilde{O}(\varepsilon^{-2}n^{1/2^p})\).

