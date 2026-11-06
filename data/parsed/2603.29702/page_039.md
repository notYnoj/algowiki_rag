_Proof._ For each active scale _s_, we consider the following question: how much would we overestimate if there were no subsampling on active scales larger than _s_? We can see that the final estimate is at most:

\(\mathcal{P}_s:=\sum_{i=1}^{n/I_s}\mathrm{est}[(i-1)\cdot I_s,\widehat{p}((i-1)\cdot I_s),i\cdot I_s,\widehat{p}(i\cdot I_s)].\)

We can see that \(\mathcal{P}_0=w(\widehat{p})\), and that \(\mathcal{P}_S=\mathrm{est}[0,n_X,n_X+n_Y,n_Y]\), namely our final estimate for \(w(\widehat{p})\). To see how much larger P_<sub>S</sub>_ can be compared to P<sub>0</sub>, we go through each scale _s_ and examine the difference between P<sub>_s_-1</sub> and P_<sub>s</sub>_.

If scale-_s_ is passive, then since we compute every \(\mathrm{est}[l,\widehat{p}(l),r,\widehat{p}(r)]\) to be the length of the shortest \(\widetilde{S}\)-regular \(\langle l,\widehat{p}(l)\rangle\)-\(\langle r,\widehat{p}(r)\rangle\) path in the Scale-(_s_-1) Sparsified Grid Graph, \(\mathcal{P}_s\le\mathcal{P}_{s-1}\).

If scale-_s_ is active, fix a scale-_s_ interval (_l,r_\]. From Claim 6.7, the magnitude of overestimation is bounded by the sum of the following:

• Type I: If \(\mathrm{TD}_M(W(\widehat{p}(l,r]))=\omega\left(\frac{w(\widehat{p}(l,r])}{M}\right)\), an additive error of \(O(w(\widehat{p}(l,r]))\);<tbc>

• Type II: An additive error of \(o\left(\frac{w(\widehat{p}(l,r])}{\mathrm{log}^{0.02}(n)}\right)\));<tbc>

• Type III: With probability \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\), an additive error of \(O(w(\widehat{p}(l,r]))\).

The total sum of type III error is at most \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\) times the total sum of \(\widehat{p}(l,r]\) on every interval (_l,r_\] on an active scale. The total sum of \(\widehat{p}(l,r]\) is at most \(O(w(\widehat{p})\left|\widetilde{S}\right|)\) and the total total sum of type III error is at most \(w(\widehat{p})\left|\widetilde{S}\right|\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)=o(w(\widehat{p}))\).

By summing over every interval in each of the \(\left|\widetilde{S}\right|\) active scales (which is \(O(S^{0.02})=o\left(\mathrm{log}^{0.02}(n)\right)\) with probability 1-_o_(1)), the total sum of type II error is \(o(w(\widehat{p}))\).

Finally, since \(O(w(\widehat{p}(l,r]))=o(M)\cdot\omega\left(\frac{w(\widehat{p}(l,r])}{M}\right)\), the total sum of type I error is _o(M_) times the total sum of \(\mathrm{TD}_M(W(\widehat{p}(l,r]))\) over interval (_l,r_\] on an active scale, namely \(o(M\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p)))\), which from Claim 6.12 is \(o(w(\widehat{p}))\) with probability at least 4/5.

Combining all three types, with probability 4/5-_o_(1)_\>_19/25, the total overestimation is bounded by _o(w(p_)).

We now prove the auxiliary claim from before:

**Claim 6.12** (Restated)**.** _Assume that the length of the shortest_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path p is at least n/_2<sup>_o_\(\left(\mathrm{log}^{0.02}(n)\right)\)</sup>_. Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path be_ \(\widehat{p}\)_. With probability at least_ 4/5_, we have_ \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

_Proof._ We show a stronger result: with probability at least 4/5, we have \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(p)}{M}\right)\) (which is stronger since \(w(p)\le w(\widehat{p})\)).

We first show that \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))=o\left(\frac{w(p)}{M}\right)\). Then we argue that the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) is also \(o\left(\frac{w(p)}{M}\right)\).

