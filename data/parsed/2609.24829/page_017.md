## 4.2 Space complexity

The space complexity of P-PASS is shown in two steps. First, we show that if P-PASS finished round _i_ with no output, then _T_ must be bounded from above, and these bounds are decreasing with _i_. We then use this bound to show that if the algorithm terminated at round _i_, then space used during the round does not exceed \(\widetilde{O}(\varepsilon^{-3.5}m/\sqrt{T})\). Our analysis implies that the space complexity must increase with each round. Since we execute passes sequentially, the maximum space complexity is bounded by the maximum space complexity of all iterations.

**Lemma 4.7** (Non-termination)**.** At the end of round _i_, if P-PASS did not terminate, then \(T=\widetilde{O}(\varepsilon^{-3}n^{1/2^i})\) with probability \(1-\delta-1/\mathrm{poly}(n)\).

_Proof._ Suppose P-PASS did not terminate at round _i_, then by 4.7, \(T_\mathrm{L},\varepsilon\widehat{T}_\mathrm{H}<\tau^*=U_i\). Since \(T_\mathrm{H}/2\le(1-\varepsilon)T_\mathrm{H}\le\widehat{T}_\mathrm{H}\), we conclude

\(T=T_\mathrm{L}+T_\mathrm{H}\le\widetilde{O}(\varepsilon^{-2}n^{1/2^i})+\widetilde{O}(\varepsilon^{-3}n^{1/2^i})=\widetilde{O}(\varepsilon^{-3}n^{1/2^i}).\)

The probability guarantees follow from 4.7

**Lemma 4.8** (Space Complexity of Round _i_)**.** Suppose the algorithm terminates during round _i_, then the expected space used is \(\widetilde{O}(\delta^{-1}\varepsilon^{-3.5}(m+T)/\sqrt{T})\).

_Proof._ Let S<sub>oracle</sub>(_i_) be the space used by the oracle in round _i_, and S<sub>A</sub>(_i,j_) be the space complexity used by A with guess \(\tau_j\) in round _i_. The expected space complexity of round _i_ is therefore S<sub>oracle</sub>(_i_)+S<sub>A</sub>(_i,j_<sup>∗</sup>) where _j_<sup>∗</sup> is the point where A terminates. Recall that \(s(m,\tau)=\widetilde{O}(\delta^{-1}\varepsilon^{-2}(m+T)/\sqrt{\tau})\), which is a decreasing function of \(\tau\). Since the guesses \(\tau_j\) are decreasing with _j_, \(s(m,\tau)\) is an increasing function of _j_, so the space complexity of round _i_ is dominated by the point in which the round terminates.

Suppose first that A outputs an estimate, and that \(\tau_j\) is the guess when the algorithm terminated. By Corollary 4.6, \(T_\mathrm{L}=\Theta(\tau_j)\). Moreover, this implies \(T_\mathrm{L}=\Omega(\tau_j)=\Omega(\tau^*)=\Omega(\varepsilon\widehat{T}_\mathrm{H})=\Omega(\varepsilon T_\mathrm{H})\) and therefore \(\varepsilon T=\varepsilon T_\mathrm{L}+\varepsilon T_\mathrm{H}=O(T_\mathrm{L})\), and as always \(T=\Omega(T_\mathrm{L})\). Consequently,

\(\mathcal{S}_\mathcal{A}(i,j)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\left(\frac{m_\mathrm{L}+T_\mathrm{L}}{\sqrt{(1-\varepsilon)\tau_jt^{-3}}}\right)\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\left(\frac{m+T}{\sqrt{T_\mathrm{L}}}\right)\right)\)<br>
\(=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\left(\frac{m+T}{\sqrt{\varepsilon T}}\right)\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2.5}\frac{m+T}{\sqrt{T}}\right).\)

Suppose now that the algorithm terminated and outputs \(\widehat{T}_\mathrm{H}\). By the analysis in Lemma 4.6, \(T_\mathrm{L}\le 2\varepsilon T_\mathrm{H}\), and consequently \(T=\Theta(T_\mathrm{H})\). Every execution of A in this round uses a guess \(\tau_j\ge\tau^*=\varepsilon\widehat{T}_\mathrm{H}\), so the space of each is at most

\(\mathcal{S}_\mathcal{A}(i,t)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\left(\frac{m_\mathrm{L}+T_\mathrm{L}}{\sqrt{(1-\varepsilon)\tau^*t^{-3}}}\right)\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\left(\frac{m+T}{\sqrt{\varepsilon\widehat{T}_\mathrm{H}}}\right)\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2.5}\left(\frac{m+T}{\sqrt{T}}\right)\right).\)

That is, \(\mathcal{S}_\mathcal{A}(i,j^*)=\widetilde{O}\left(\varepsilon^{-2.5}\delta^{-1}\left(\frac{m+T}{\sqrt{T}}\right)\right)\). For S<sub>oracle</sub>(_i_), we only need to maintain |_O_|. Since the algorithm arrived at round _i_, it did not terminate at round _i_-1. By Lemma 4.7 \(\varepsilon T=\widetilde{O}(\varepsilon^{-2}n^{1/2^{i-1}})\), that is \(\varepsilon^{3.5}\sqrt{T}=\widetilde{O}(\varepsilon^{-2}n^{1/2^i})\). We compute

\(\mathbb{E}\left[|O|\right]=\sum_{v\in V}p_id\mathrm{deg}(v)=\widetilde{O}\left(\frac{m}{\varepsilon^2n^{1/2^i}}\right)=\widetilde{O}\left(\frac{\varepsilon^{-3.5}m}{\sqrt{T}}\right).\)

