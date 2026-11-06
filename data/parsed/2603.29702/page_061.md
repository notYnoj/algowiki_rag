**Claim 7.13** (Restated)**.** _Assume that the length of the longest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path is at least n/_2<sup>_o_\(\big(\)log<sup>0.02</sup>(_n_)\(\big)\)</sup>_. Let_ \(\widetilde{S}\subset[S]\) _be such that each scale that is a multiple of_ 3 _is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path be_ \(\widehat{p}\) _with_ \(w(\widehat{p})=\Omega(w(p))\)_. Recall that_ \(W(\widehat{p})\) _is the sequence of length n/_B_<sub>x</sub> whose i-th entry is:_

\(W(\widehat{p})_i:=w(\widehat{p}(i\mathcal{B}_x,(i+1)\mathcal{B}_x]),\) (32)

_which captures the "weight distribution" of_ \(\widehat{p}\).

_With probability at least_ 4/5_, we have_ \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

_Proof._ We first show that \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))=o(w(p)/M)\). Then we argue that the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) is also _o(w(p)/M_).

**Part I:** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) **is small** Using the bound on tree total deviation in Lemma 4.1 we know that,

\(\unknown\mathrm{TD}_{M,S}(W(p))=O\left(w(p)\cdot S^{0.51}+\underbrace{\mathcal{B}_x}_{\mathrm{maxlengthof}p\text{overscale}0\text{interval}}\cdot\underbrace{(n/\mathcal{B}_x)}_{\mathrm{numberofscale}0\text{intervals}}/2^{\mathrm{log}_M^{0.015}(n)}\right)\)<br>
\(=O\left(w(p)\cdot S^{0.51}+n/2^{\mathrm{log}_M^{0.015}(n)}\right)\)

Since each scale that is a multiple of 3 is in \(\widetilde{S}\) u.a.r with probability 1_/S_<sup>0.98</sup>, and _p_ does not depend on \(\widetilde{S}\), we have that with probability at least 9/10,

\(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))=O\left(\left(w(p)\cdot S^{0.51}+n/2^{\mathrm{log}_M^{0.015}(n)}\right)/S^{0.98}\right)\)<br>
\(=\left(O\left(\left(w(p)\cdot S^{0.51}\right)+o\left(\frac{w(p)}{M}\right)\right)\right)/S^{0.98}\text{since}w(p)=n/2^{o\big(\mathrm{log}^{0.01}(n)\big)}\)<br>
\(=w(p)/S^{0.47}+o\left(\frac{w(p)}{M}\right)\)<br>
\(=o\left(\frac{w(p)}{M}\right).\text{since}M=\Theta\left(\mathrm{log}^{0.109}(n)\right)\)

**Part II:** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) **is not too different from** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) From Lemma 7.3, with probability at least 19/20. We can round _p_ to an \(\widetilde{S}\)-regular path \(\widehat{p}\) such that there are at most \(o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) columns _x_ before which their weights differ. Each of these columns contributes at most \(O(\left|\widetilde{S}\right|)\) to the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\). Since the size of \(\widetilde{S}\) is \(O(S^{0.02})=o\left(\mathrm{log}^{0.02}(n)\right)\) with probability 1-_o_(1)_\>_19/20, by the union bound, with probability at least 9/10, the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) is at most \(o\left(\frac{w(p)}{M}\right)\).

Combining the two parts, with probability at least 4/5, we have \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

## 7.3.3 Our Estimate Is Sound

Now we show that our estimate is sound:

