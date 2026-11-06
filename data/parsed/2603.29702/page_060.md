The most technically involved part of this proof is the analysis of the type II error. Since our estimate \(\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\) can be different from \(w(\widehat{p}(m_{i-1},m_i])\), the errors can have a cascading effect. We say an interval is "imbalanced" if \(\mathrm{max}_iw(\widehat{p}(m_{i-1},m_i])>\frac{2w(\widehat{p}(l,r])}{M}\) and "balanced" otherwise. Suppose (_l,r_\] is "balanced." Namely the weight distribution of \(\widehat{p}\) inside (_l,r_\] is balanced. We now argue that the cascading effect is insignificant for "balanced" interval. We now show that in order for there to be a type II error on "balanced" (_l,r_\], namely for the distribution of \(\mathrm{est}'\) to be imbalanced despite the actual answer distribution being balanced, the \(\mathrm{est}'\) values must have decayed so much that they are small enough to be ignored. Formally, notice that every \(\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\le w(\widehat{p}(m_{i-1},m_i])\). Thus type II error only exists if<tbc>

\(\mathrm{max}_iw(\widehat{p}(m_{i-1},m_i])=\Omega\left(\frac{\mathrm{log}^{0.02}(n)}{M}\sum_i\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\right).\)

<tbc>Since we assume (_l,r_\] is "balanced," we have \(\mathrm{max}_iw(\widehat{p}(m_{i-1},m_i])\le\frac{2w(\widehat{p}(l,r])}{M}\) . This means that

\(\sum_i\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]=O\left(\frac{w(\widehat{p}(l,r])}{\mathrm{log}^{0.02}(n)}\right).\)

The worst total extra additive error incurred this way inside a "balanced" (_l,r_\] on scale _s_ is not worse than if the estimation simply decays to 0 completely, but even then the error is only \(O\left(\frac{w(\widehat{p}(l,r])}{\mathrm{log}^{0.02}(n)}\right)\).

Therefore, the total magnitude of type II error on scale _s_ is at most the sum of:

**Type II(a) - "imbalanced" intervals** the sum of \(w(\widehat{p}(l,r])\) over "imbalanced" interval (_l,r_\] on scale _s_;

**Type II(b) - "balanced" intervals** the sum of \(w(\widehat{p}(l,r])\) over "balanced" interval on scale _s_, which we now know is at most \(O\left(\frac{w(\widehat{p})}{\mathrm{log}^{0.02}(n)}\right)\).

Summing over active scales, we can see that with probability 1-_o_(1), the total type II(b) error is at most \(O\left(\frac{w(\widehat{p})}{\mathrm{log}^{0.02}(n)}\cdot\left|\widetilde{S}\right|\right)=o(w(\widehat{p}))\).

We now bound the sum of type II(a) error on active scales, namely the sum of \(w(\widehat{p}(l,r])\) over "imbalanced" interval (_l,r_\] on active scales. If an interval (_l,r_\] is "imbalanced," namely \(\mathrm{max}_iw(\widehat{p}(m_{i-1},m_i])>\frac{2w(\widehat{p}(l,r])}{M}\) , then

\(\mathrm{TD}_M(W(\widehat{p}(l,r]))=\sum_i\left|w(\widehat{p}(m_{i-1},m_i])-\frac{w(\widehat{p}(l,r])}{M}\right|=\Omega\left(\frac{w(\widehat{p}(l,r])}{M}\right).\)

Thus \(w(\widehat{p}(l,r])=O(MT\mathrm{TD}_M(W(\widehat{p}(l,r])))\), which means that the sum of \(w(\widehat{p}(l,r])\) over "imbalanced" interval (_l,r_\] on active scales is \(O(M\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p})))\), which is \(o(w(\widehat{p}))\) from Claim 7.13 with probability 4/5.

Summing up all errors and taking the union bound over the probability that \(\left|\widetilde{S}\right|=O(S^{0.02})\), we can see that the lemma indeed holds with probability 4/5-_o_(1)_\>_19/25.

We now prove the auxiliary claim from before:

