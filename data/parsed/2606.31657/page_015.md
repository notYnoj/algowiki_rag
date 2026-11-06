Pick an arbitrary \(m\in\Sigma^k\). Notice that \(\mathbf{Pr}_{m^\prime\sim\nu_m^*}\left[m'_i=m_i\right]\) is independent of _i_ because \(\nu_m^*\) depends on \(m'\) only through its Hamming distance from _m_, and every coordinate plays the same role. So we have

\(\mathbf{Pr}_{m^\prime\sim\nu_m^*}\left[m'_1\neq m_1\right]=\frac{1}{k}\sum_{i\in[k]}\mathbf{Pr}_{m^\prime\sim\nu_m^*}\left[m'_i\neq m_i\right]\)<br>
\(=\frac{1}{k}\cdot\mathbb{E}\left[d_\mathrm{H}(\sigma(\tilde{\mathcal{A}}(\mathcal{I}_C(m))),m)\right]\)<br>
\(=\frac{n}{k}\cdot\mathbb{E}\left[\delta_\mathrm{H}(\sigma(\tilde{\mathcal{A}}(\mathcal{I}_C(m))),m)\right]\)<br>
\(\le\frac{\varepsilon}{r\kappa}.\)

This means

\(\mathbf{Pr}_{m^\prime\sim\nu_m^*}\left[m'_1=m_1\right]\ge 1-\frac{\varepsilon}{r\kappa}.\) (1)

Similarly, picking a character \(a\in\Sigma\backslash\{m_1\}\), we define \(\hat{m}\) as the message \((a,m_2,\cdots,m_k)\), we have \(\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=a\right]\ge 1-\frac{\varepsilon}{r\kappa}\), which means

\(\left(|\Sigma|-1\right)\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=m_1\right]=\sum_{b\in\Sigma\backslash\{a\}}\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=b\right]=1-\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=a\right]\le\frac{\varepsilon}{r\kappa},\) (2)

and thus

\(\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=m_1\right]\le\frac{1}{|\Sigma|-1}\frac{\varepsilon}{r\kappa}.\)

Putting Equations (1) and (2) together, we have

\(L\left(\{\nu_m^*\}\right)=\mathsf{TV}(\nu_m^*,\nu_\hat{m}^*)\ge\left|\mathbf{Pr}_{m^\prime\sim\nu_m^*}\left[m'_1=m_1\right]-\mathbf{Pr}_{m^\prime\sim\nu_\hat{m}^*}\left[m'_1=m_1\right]\right|\ge 1-\frac{|\Sigma|}{|\Sigma|-1}\cdot\frac{\varepsilon}{r\kappa},\)

and the claim follows.

**Lemma 3.7.** _Let C be a systematic LTC with detection probability_ \(\kappa\) _and_ A _be a randomized_ \((1-\varepsilon)\)_-approximation algorithm for_ MaxCSP(_C). Then we have_<tbc>

\(\mathbb{E}_{m\in\Sigma^k}\left[\mathbb{E}_{m^\prime\sim m}\left[\mathsf{EMD}_{\delta_\mathrm{H}}\left(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\right)\right]\right]\ge\delta\left(1-\frac{|\Sigma|}{|\Sigma|-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}.\)

<tbc>_Proof._ By Theorem 3.6, we have<tbc>

\(\mathbb{E}_{m\in\Sigma^k}\left[\mathbb{E}_{m^\prime\sim m}\left[\mathsf{TV}\left(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\right)\right]\right]\ge 1-\frac{|\Sigma|}{|\Sigma|-1}\cdot\frac{\varepsilon}{r\kappa}.\)

<tbc>Let \(\nu_m\) and \(\nu_{m^\prime}\) denote the laws of \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\), respectively. Since total variation on \(\Sigma^k\) coincides with EMD_<sub>d<sub>c</sub></sub>_, where _d<sub>c</sub>_ is the discrete measure, every coupling \(\pi_k\in\Pi(\nu_m,\nu_{m^\prime})\) satisfies

\(\mathbb{E}_{(a,b)\sim\pi_k}\left[d_c(a,b)\right]\ge 1-\frac{|\Sigma|}{|\Sigma|-1}\frac{\varepsilon}{r\kappa}.\)

Let \(\mu_m\) and \(\mu_{m^\prime}\) be the laws of \(\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\). By conditioning on the decoded message, we extend any such \(\pi_k\) to a coupling \(\Pi\in\Pi(\mu_m,\mu_{m^\prime})\) on \(\Sigma^n\times\Sigma^n\): draw \((a,b)\sim\pi_k\) and then sample \(x\sim\mu_m\) and \(y\sim\mu_{m^\prime}\) conditioned on \(\sigma(x)=a\) and \(\sigma(y)=b\) (the conditionals exist because \(\pi_k\)<tbc>

