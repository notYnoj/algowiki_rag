Invoking Theorem D.1, the former condition of (D.6) is satisfied whenever<tbc>

<tbc>\(\frac{b}{\left(\alpha b(1-\alpha)\right)^{3/2}}\le\frac{\beta(\alpha)}{8}\Longleftrightarrow\frac{64}{\alpha^3\beta(\alpha)^2(1-\alpha)^3}\le b.\)<tbc>

<tbc>On the other hand, since it readily follows from the Mean Value Theorem that \(\Phi\) is 1-Lipschitz, the latter condition of (D.6) is satisfied whenever<tbc>

<tbc>\(\frac{1}{b^\epsilon\sqrt{\alpha(1-\alpha)}}\le\frac{\beta(\alpha)}{8}\Longleftrightarrow\frac{8^{24}}{\alpha^{12}\beta(\alpha)^{24}(1-\alpha)^{12}}\le b.\)<tbc>

\(\bullet\) In carrying out (C.10), we assume that _b_ is large enough so that for any \(i\notin\mathcal{I}_x\), it holds that<tbc>

<tbc>\(\mathbb{P}\left(\tilde{\zeta}_1-\tilde{\zeta}_0\ge b^{1/2-\epsilon}\right)\ge\frac{1}{2}-\frac{\beta(\alpha)}{72}\)<tbc>

<tbc>where we have here that independently<tbc>

<tbc>\(\tilde{\zeta}_1,\tilde{\zeta}_0\sim\text{Bin}\left(b/2,\alpha\right).\)<tbc>

<tbc>We may express the probability of interest as<tbc>

<tbc>\(\mathbb{P}\left(\tilde{\zeta}_0-\tilde{\zeta}_1\le-b^{1/2-\epsilon}\right)=\mathbb{P}\left(\frac{\left(\tilde{\zeta}_0-\frac{\alpha b}{2}\right)-\left(\tilde{\zeta}_1-\frac{\alpha b}{2}\right)}{\sqrt{\alpha b\cdot(1-\alpha)}}\le\frac{-b^{1/2-\epsilon}}{\sqrt{\alpha b\cdot(1-\alpha)}}\right)\)<br>
\(=:\mathbb{P}\left(\tilde{S}_b\le-\frac{1}{b^\epsilon\sqrt{\alpha(1-\alpha)}}\right).\)<tbc>

<tbc>It therefore follows that<tbc>

\(\text{(D.7)}\) \(\left|\mathbb{P}\left(\tilde{\zeta}_1-\tilde{\zeta}_0\ge b^{1/2-\epsilon}\right)-\frac{1}{2}\right|\le\mathrm{sup}_x|F_{\tilde{S}_b}(x)-\Phi(x)|+\left|\Phi\left(-\frac{1}{b^\epsilon\sqrt{\alpha(1-\alpha)}}\right)-\frac{1}{2}\right|.\)

<tbc>It suffices to show that (D.7) is at most \(\beta(\alpha)/72\). In particular, this holds whenever<tbc>

\(\text{(D.8)}\) \(\mathrm{sup}_x|F_{\tilde{S}_b}(x)-\Phi(x)|\le\frac{\beta(\alpha)}{144};\left|\Phi\left(-\frac{1}{b^\epsilon\sqrt{\alpha(1-\alpha)}}\right)-\frac{1}{2}\right|\le\frac{\beta(\alpha)}{144}.\)

Invoking Theorem D.1, the former condition of (D.8) is satisfied whenever<tbc>

<tbc>\(\frac{b}{\left(\alpha b\left(1-\alpha\right)\right)^{3/2}}\le\frac{\beta(\alpha)}{144}\Longleftrightarrow\frac{20736}{\alpha^3\beta(\alpha)^2(1-\alpha)^3}\le b.\)<tbc>

<tbc>On the other hand, as \(\Phi\) is 1-Lipschitz, the latter condition of (D.8) is satisfied whenever<tbc>

<tbc>\(\frac{1}{b^\epsilon\sqrt{\alpha(1-\alpha)}}\le\frac{\beta(\alpha)}{144}\Longleftrightarrow\frac{144^{24}}{\alpha^{12}\beta(\alpha)^{24}(1-\alpha)^{12}}\le b.\)<tbc>

<tbc>Finally, we record a crude quantitative estimate for later use. We would like _b_ to be large enough so that

\(\text{(D.9)}\) \(\frac{\alpha\cdot D_\text{KL}\left(b^{-(4+8\epsilon)}\right\|2e^{-b^{1/2-6\epsilon}/2}\right)}{b^{1/2+2\epsilon}}\ge\frac{\alpha\cdot b^{-(4+8\epsilon)}\left(\frac{1}{2}b^{1/2-6\epsilon}-(4+8\epsilon)\mathrm{log}b-\mathrm{log}2\right)}{b^{1/2+2\epsilon}}\ge\frac{1}{b^5},\)

where the first inequality follows from the definition of the KL divergence of two Bernoulli distributions. The latter inequality simplifies to

\(\frac{1}{2}b^{1/3}-b^{1/12}\left(\frac{13}{3}\mathrm{log}b+\mathrm{log}2\right)\ge\frac{1}{\alpha}.\)

This condition holds whenever \(b\ge(120/\alpha)^{24}\), on which in particular \(\mathrm{log}b\le b^{1/24}\).

