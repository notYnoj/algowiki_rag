**Lemma 3.** _The sampled matching in_ \(G'\) _has expected size at least_ \(\frac{\mathrm{OPT}'}{3\rho}\) .

_Proof._ For \(w\in W'\), let _d<sub>w</sub>_ be the number of copies of good _w_ that have been assigned in the matching _M_<sup>∗</sup>. Then \(\sum_wd_w\ge b\mathrm{OPT}'/\rho\). If \(d_w\ge 1\), then we have the following estimate for the probability that _w_ is chosen.

\(\mathrm{Pr}[w\text{is chosen}]\ge d_w\frac{1}{b}\left(1-\frac{1}{b}\right)^{d_w-1}\) (6)

\(=\frac{d_w}{b}\left(1+\frac{1}{b-1}\right)^{-(d_w-1)}\) (7)

\(\ge\frac{d_w}{b}\mathrm{exp}(-(d_w-1)/(b-1))\text{(because}1+x\le e^x\text{)}\) (8)

\(\ge\frac{d_w}{eb}.\text{(because}d_w\le b\text{)}\) (9)

Let \(M'\) be the sampled matching in \(G'\). Then by linearity of expectation:

\(\mathbb{E}[|M^*|]\ge\sum_{w\in W^\prime}\frac{d_w}{eb}\ge\frac{b\mathrm{OPT}'}{eb\rho}\ge\frac{\mathrm{OPT}'}{3\rho}.\)

This completes our proof.

## C Missing Proofs from Section 4

**Lemma 4.** _Suppose we have a dual vector_ \(\widehat{\lambda}\) _such that_ \(\|\lambda^\bullet-\widehat{\lambda}\|\le\alpha\)_. Let_ \(\widehat{x}=\mathrm{argmax}_{x\in\mathcal{F}}\mathcal{L}(x,\widehat{\lambda})\)_, then_<tbc>

\(\|\widehat{x}-x^\bullet\|\le\frac{2\sqrt{\alpha}(nk)^{1/4}}{\sqrt{\eta}}\)

<tbc>_Proof._ Fixing any _x_, the function \(\mathcal{L}(x,\lambda)\) is \(\sqrt{n}k\)-Lipschitz with respect to \(\ell_2\) norm because for any \(\lambda,\lambda'\)<tbc>

\(\|\mathcal{L}(x,\lambda)-\mathcal{L}(x,\lambda')\|=\left\|\sum_{j=1}^k(\lambda_j-\lambda'_j)\sum_{i=1}^nc_j^{(i)}\left(x^{(i)}\right)\right\|\le\|\lambda-\lambda'\|\left\|\sum_{i=1}^nc_j^{(i)}\left(x^{(i)}\right)\right\|\le\|\lambda-\lambda'\|\sqrt{nk}\)

<tbc>By the property of Lipschitz functions we know that \(g(\lambda)=\mathrm{max}_{x\in\mathcal{F}}\mathcal{L}(x,\lambda)\) is also \(\sqrt{nk}\)-Lipschitz. Since \(\|\lambda^\bullet-\widehat{\lambda}\|\le\alpha\), we can then bound<tbc>

\(\|\mathcal{L}(x^\bullet,\widehat{\lambda})-\mathcal{L}(x^\bullet,\lambda^\bullet)\|\le\alpha\sqrt{nk},\)

<tbc>and also<tbc>

\(\|\mathcal{L}(x^\bullet,\lambda^\bullet)-\mathcal{L}(\widehat{x},\widehat{\lambda})\|=\|g(\lambda^\bullet)-g(\widehat{\lambda})\|\le\alpha\sqrt{nk}.\)

<tbc>It follows that<tbc>

\(\|\mathcal{L}(x^\bullet,\widehat{\lambda})-\mathcal{L}(\widehat{x},\widehat{\lambda})\|\le 2\alpha\sqrt{nk}.\)

<tbc>Note that fixing \(\widehat{\lambda}\), the function \(\mathcal{L}(x,\widehat{\lambda})\) is \(\eta\)-strongly concave in _x_. Since \(\widehat{x}\) is a maximizer of \(\mathcal{L}(\cdot,\widehat{\lambda})\), we have

\(\|\widehat{x}-x^\bullet\|^2\le\frac{2}{\eta}\left(\mathcal{L}(\widehat{x},\widehat{\lambda})-\mathcal{L}(x^\bullet,\widehat{\lambda})\right)\le 4\alpha\sqrt{nk}/\eta\)

Therefore, we must have \(\|\widehat{x}-x^\bullet\|\le\frac{2\sqrt{\alpha}(nk)^{1/4}}{\sqrt{\eta}}\) .

