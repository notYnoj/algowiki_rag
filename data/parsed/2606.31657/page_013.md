## 3.3 Total Variation Gap for Adjacent Messages

In this section, we consider symmetrizing the decoder’s output distributions for near-optimal assignments and show that the output distributions are well separated in total variation in expectation over neighboring messages.

Let

\(\mathcal{D}_\varepsilon:=\)<br>
\(\left\{(\nu_m)_{m\in\Sigma^k}\middle|\exists(1-\varepsilon)\text{-approx algorithm}\mathcal{A}\text{for MaxCSP}(C)\text{with}\nu_m=\mathrm{law}(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m)))\text{for all}m\right\}.\)

Here law(_X_) denotes the distribution of a random variable _X_ and \(\sigma\) is the nearest-message decoder.

**Lemma 3.5.** _The set_ \(\mathcal{D}_\varepsilon\) _is convex._

_Proof._ Let \((\mu_m)\) and \((\nu_m)\) lie in \(\mathcal{D}_\varepsilon\), witnessed respectively by randomized \((1-\varepsilon)\)-approximation algorithms A<sub>1</sub> and A<sub>2</sub>. For \(\lambda\in[0,1]\), define an algorithm \(\tilde{\mathcal{A}}_\lambda\) which, on input _m_, runs \(\tilde{\mathcal{A}}_1(\mathcal{I}_C(m))\) with probability \(\lambda\) and \(\tilde{\mathcal{A}}_2(\mathcal{I}_C(m))\) otherwise, and returns the resulting assignment. The expected number of satisfied constraints produced by \(\tilde{\mathcal{A}}_\lambda\) is the convex combination of those for \(\tilde{\mathcal{A}}_1\) and \(\tilde{\mathcal{A}}_2\), so \(\tilde{\mathcal{A}}_\lambda\) is again a \((1-\varepsilon)\)-approximation algorithm. Moreover, \(\mathrm{law}(\sigma\circ\tilde{\mathcal{A}}_\lambda(\mathcal{I}_C(m)))=\lambda\mu_m+(1-\lambda)\nu_m\) for every \(m\in\Sigma^k\). Hence the family \((\lambda\mu_m+(1-\lambda)\nu_m)_{m\in\Sigma^k}\) belongs to \(\mathcal{D}_\varepsilon\), establishing convexity.

**Theorem 3.6.** _Let C be a systematic LTC and_ A _be a randomized_ \((1-\varepsilon)\)_-approximation algorithm for_ MaxCSP(_C). Then we have_<tbc>

\(\mathbb{E}_{m\in\Sigma^k}\left[\mathbb{E}_{m^\prime\sim m}\left[\mathsf{TV}\left(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\right)\right]\right]\ge 1-\frac{|\Sigma|}{|\Sigma|-1}\cdot\frac{\varepsilon}{r\kappa}.\)

<tbc>_Proof._ We define _L_ as a functional on \(\mathcal{D}_\varepsilon\) by setting

\(L\left(\{\nu_m\}_{m\in\Sigma^k}\right):=\frac{1}{k(|\Sigma|-1)|\Sigma|^k}\sum_{m_1,m_2\in\Sigma^km_1\sim m_2}\mathsf{TV}\left(\nu_{m_1},\nu_{m_2}\right)\)<br>
\(=\mathbb{E}_{m\in\Sigma^k}\left[\mathbb{E}_{m^\prime\sim m}\left[\mathsf{TV}\left(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\right)\right]\right].\)

that is, the average total variation distance between the distributions associated with neighboring messages. We want to find an element in \(\mathcal{D}_\varepsilon\) that minimizes _L_.

Suppose \(\{\nu_m\}\in\mathcal{D}_\varepsilon\) is a minimizer of _L_. In the following, we construct another minimizer \(\{\nu_m^*\}\) that is symmetric in the sense that \(\nu_m^*(m')\) only depends on \(\delta_\mathrm{H}(m,m')\). To do so, we define two kinds of permutations that act on \(\mathcal{D}_\varepsilon\). For a finite set _S_ let perm(_S_) denote the collection of all permutations of _S_. We then have:

1. For any \(\pi\in\mathrm{perm}([k])\), define \(\pi(m)=(m_{\pi(1)},\dots,m_{\pi(k)})\). Then define \(\{\nu_m^\pi\}\) by<tbc>

<tbc>\(\nu_m^\pi(m'):=\nu_{\pi(m)}(\pi(m')).\)<tbc>

2. For any \(\tau=(\tau_1,\dots,\tau_k)\in\mathrm{perm}(\Sigma)^k\), define \(\tau(m)=(\tau_1(m_1),\dots,\tau_k(m_k))\). Then define \(\{\nu_m^\tau\}\) by<tbc>

<tbc>\(\nu_m^\tau(m'):=\nu_{\tau(m)}(\tau(m')).\)<tbc>

