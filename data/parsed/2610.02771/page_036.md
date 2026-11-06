_Proof._ In any non-stopping round, if \(k\in\{h,\ell\}\) is sampled, the interval geometry alone gives \(B_h\le 2\beta_k\). To see this for \(k=\ell\), the sampling rule implies \(\beta_\ell\ge\beta_h\). If \(\mathrm{LCB}_\ell>\mathrm{LCB}_h\), then \(\mathrm{UCB}_\ell>\mathrm{UCB}_h\) and \(B_\ell<B_h\), contradicting the minimality of _h_. Hence \(B_h=\mathrm{UCB}_\ell-\mathrm{LCB}_h\le 2\beta_\ell\). For _k=h_, the sampling rule implies \(\beta_h\ge\beta_\ell\). If \(\mathrm{UCB}_\ell>\mathrm{UCB}_h\), then \(\mathrm{LCB}_\ell>\mathrm{LCB}_h\) and again \(B_\ell<B_h\), a contradiction. Thus \(B_h\le 2\beta_h\). Neither argument uses interval validity.

Consequently, every sampled arm has \(\beta_\varepsilon(N_k,\delta/K)>\varepsilon/2\). At the deterministic count \(n_\mathrm{fix}^\circ\), its stitched logarithm is exactly the logarithm in the proposition, and

\(2\sqrt{\frac{3\alpha_\varepsilon\sigma^2x_{n_\mathrm{fix}^\circ(\delta/K)}}{n_\mathrm{fix}^\circ}}\le\frac{\varepsilon}{8},\frac{2\alpha_\varepsilon\sigma^2x_{n_\mathrm{fix}^\circ(\delta/K)}}{n_\mathrm{fix}^\circ\varepsilon}\le\frac{\varepsilon}{384}.\)

Including the bias \(\varepsilon/4\) gives a radius strictly below \(\varepsilon/2\). Once an arm reaches this count it cannot be sampled again, since its unchanged estimate and local count retain the same radius. Including the initialization query, each arm receives at most \(n_\mathrm{fix}^\circ\) queries, proving the cap. Exponential growth of 2_<sup>m</sup>_ versus the logarithm ensures \(m_\varepsilon<\infty\). The same inversion as in Appendix B.5, with rounding to a power of two, gives the stated order.

## C.3.2 Restart phased clipping

**Proposition 33** (Pathwise phased cap)**.** _With_ \(n_j^\circ\) _and_ \(\Gamma_j\) _from Lemma 27, on every realization,_

\(\tau_\mathrm{ph}\le K\sum_{j=0}^Jn_j^\circ=O\big(K\left(1+\mathrm{log}\frac{\sigma}{\varepsilon}\right)\frac{\sigma^2}{\varepsilon^2}\Gamma_J\big).\)

_Proof._ Lemma 27 gives \(\beta_j(n_j^\circ)\le r_j\) deterministically. The sampling rule selects only an arm with radius greater than _r<sub>j</sub>_: it samples the larger-radius candidate or challenger when possible, and otherwise an active arm of maximum radius. An arm reaching \(n_j^\circ\) is therefore never sampled again in that phase. Once all active radii are at most _r<sub>j</sub>_, the algorithm returns or advances to the next phase. The active set cannot become empty, since an arm maximizing the LCB has UCB at least that LCB and survives elimination, even for invalid intervals. There are _J_+1 phases, so their caps sum to at most \(K\sum_jn_j^\circ\). Finally, \(\rho_J\in(\varepsilon/2,\varepsilon]\), \(\alpha_j\) and \(\Gamma_j\) are nondecreasing, and \(\sum_{j=0}^J4^j\le(4/3)4^J\). These facts yield the displayed order.

Combining either pathwise cap with its simultaneous confidence event proves almost-sure termination and \((\varepsilon,\delta)\)-PAC correctness. The caps are gap-independent; the high-probability theorems give sharper instance-dependent guarantees.

## C.4 Lau-Scarlett estimators with phased successive elimination

We record a batched alternative to make the scope of our rate claim explicit. Use \(\rho_j=2^{-j}\sigma\), \(J=\lceil\mathrm{log}_2(\sigma/\varepsilon)\rceil\), and \(\gamma=\delta/[K(J+1)]\). In phase _j_, invoke the finite-variance fixed-target estimator of Lau and Scarlett \[21\] separately on each active arm with accuracy \(\rho_j/8\) and failure probability \(\gamma\), using the supplied anchor. Retain arms whose estimates are within \(\rho_j/2\) of the largest completed estimate. Return a singleton immediately, or any survivor at phase _J_.

A union bound gives simultaneous accuracy of all completed arm-phase estimates with probability at least \(1-\delta\). On this event, the estimated maximum exceeds the best arm’s estimate by at most \(\rho_j/4\), so the best arm survives. A suboptimal arm with \(\Delta_k>3\rho_j/4\) has estimated deficit greater than \(\rho_j/2\) and is removed. Conversely every survivor has \(\Delta_k\le 3\rho_j/4\), so a final-phase survivor is \(\varepsilon\)-optimal.

The deterministic cost per active arm in phase _j_ is

\(m_j=O\left(\frac{\sigma^2}{\rho_j^2}\left(1+\mathrm{log}\frac{\sigma}{\rho_j}\right)\mathrm{log}\frac{K(J+1)}{\delta}\right).\)

An arm is not sampled at resolutions finer than a constant multiple of \(\overline{\Delta_k}\) on the simultaneous event; for the best arm, all challengers are removed by the corresponding scale. Summing geometrically<tbc>

