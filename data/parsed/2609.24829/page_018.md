We conclude

\(\mathcal{S}_\text{oracle}(i)+\mathcal{S}_\mathcal{A}(i,j^*)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-2.5}\left(\frac{m+T}{\sqrt{T}}\right)\right)+\widetilde{O}\left(\varepsilon^{-3.5}\left(\frac{m}{\sqrt{T}}\right)\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(\frac{m+T}{\sqrt{T}}\right)\right).\)

**Lemma 4.9** (Space Complexity)**.** The expected space usage of P-PASS is \(\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(\frac{m+T}{\sqrt{T}}\right)\right)\).

_Proof._ If the algorithm terminates at the first pass, the result follows from 3.4.

Otherwise, note that \(s(m,\tau)=\widetilde{O}(\delta^{-1}\varepsilon^{-2}(m+T)/\sqrt{\tau})\) is a decreasing function of \(\tau\). Consequently, for each _i_ S<sub>A</sub>(_i,j_) is an increasing function of _j_ and \(\mathcal{S}_\mathcal{A}(i+1,\cdot)\le\mathcal{S}_\mathcal{A}(i,\cdot)\). That is, with each round we increase the space complexity used by the algorithm, so the total space complexity is dominated by the point in which P-PASS terminated.<br>
If P-PASS terminates at round _i_, then the claim follows from 4.8. If P-PASS did not terminate in all rounds \(i\in[p]\), then by 4.7 \(T=\widetilde{O}(\varepsilon^{-3}n^{1/2^p})\). The peak space usage therefore was at round _p_, where, by the same analysis as in 4.8, the space complexity is

\(\widetilde{O}\left(\delta^{-1}\varepsilon^{-2}\frac{m+T}{\sqrt{(1-\varepsilon)\varepsilon^{-2}n^{1/2^p}}}\right)=\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\frac{m+T}{\sqrt{T}}\right).\)

_Proof of Theorem 4.1._ Correctness follows from 4.8. The space complexity follows from 4.9

### 4.3 A multiplicative approximation algorithm

We designed a family of algorithms that allow for a tradeoff between the accuracy of approximation and the number of passes over the stream: _p_ passes guarantee a \((1+\varepsilon,\widetilde{O}(\varepsilon^{-2}n^{1/2^p}))\) approximation of _T_. Setting _p_=loglog(_n_), we can modify P-PASS slightly and strengthen the guarantees. Let LOGLOGPASS be the following algorithm: Run P-PASS with \(p=\lceil loglog(n)\rceil\) where the last pass simply keeps all edges of _S_ and counts triangles exactly.

**Theorem 4.9** (loglog(_n_) Pass Multiplicative Error)**.** LOGLOGPASS _returns a_ \((1+\varepsilon,0)\) _mixed approximation of T with probability at least_ \(1-\delta-1/poly(n)\)_, using_ \(\widetilde{O}(\delta^{-1}\varepsilon^{-3.5}(m+T)/\sqrt{T})\) _expected space._

_Proof._ By 4.6 and 4.5, if LOGLOGPASS terminates before the last pass, the output is a \((1+\varepsilon,0)\) approximation of _T_. In the last pass, we count exactly the number of triangles, so it’s clearly the desired approximation. We only need to justify the space usage of the last pass: Since round _p_=loglog(_n_) did not end in termination, by 4.7, \(T=O(\varepsilon^{-1}U_p)=\widetilde{O}(\varepsilon^{-3})\). Therefore

\(m=\widetilde{O}\left(\frac{m}{\sqrt{\varepsilon^{-3}polylog(n)}}\right)=\widetilde{O}\left(\varepsilon^{-3.5}\frac{m}{\sqrt{T}}\right).\)

## 5 Lower Bound on Parameter Free Triangle Estimation

In this section, we prove a space lower bound for our problem using the following formulation of the Random Partition Model. To prove our lower bound, we first consider a special case of the _robust communication model_ introduced by Chakrabarti, Cormode, and McGregor \[CCM16\].

