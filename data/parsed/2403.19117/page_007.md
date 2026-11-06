## Success probability

We study how the frequent subset sums, \(X=\{t:f_t\ge h\}\), are distributed to the bins modulo a random prime _p_, using an argument similar to \[3\]. Setting

\(k:=\big\lceil\frac{m}{4P}\big\rceil,\) (12)

the following lemma shows that the bin _B_<sub>_r_<sup>∗</sup></sub> receives at least _k_ frequent subset sums, with \(\Omega^*(1)\) probability.

\(\blacktriangleright\) **Lemma 9.** _With at least_ \(\Omega(1/n)\) _probability over the choice of prime_ \(p\in[P,2P]\) _and_ \(r^*\in\mathbb{Z}_p\)_, there are at least k integers_ \(t\in\mathbb{N}\) _such that_ \(\#\{S\in B_{r^*}:w(S)=t\}\ge h\).

**Proof.** Since \(|X|\ge m\) by Equation (11), we arbitrarily pick \(X'\subseteq X\) with \(|X'|=m\) for the sake of analysis. Let \(c_{r,p}:=\{t\in X':t\equiv r(modp)\}\). Then,

\(\mathbf{E}_{p\in[P,2P]}\big[\sum_{r\in\mathbb{Z}_p}c_{r,p}^2\big]=\sum_{x\in X^\prime,y\in X^\prime}\mathbf{Pr}_{p\in[P,2P]}[p|x-y]\)<br> \(\le m+m^2\cdot\frac{log_P2^n}{\Omega(P/lnP)}\text{(by}|x-y|\le 2^n\text{and the density of primes)}\)<br> \(\le O(n\cdot m^2/P).\text{(by the assumption that}P\le 2m\)

Then by Markov’s inequality, with 0.9 success probability over the choice of _p_, we have \(\sum_{r\in\mathbb{Z}_p}c_{r,p}^2\le O(n\cdot m^2/P)\). Conditioned on this happening, by Cauchy-Schwarz inequality we have

\(\sum_{r\in\mathbb{Z}_p}\mathbf{1}[c_{r,p}\ge\frac{m}{2p}]\ge\frac{\big(\sum_{r\in\mathbb{Z}_p}\mathbf{1}[c_{r,p}\ge\frac{m}{2p}]\cdot c_{r,p}\big)^2}{\sum_{r\in\mathbb{Z}_p}c_{r,p}^2}\)<br> \(\ge\frac{\big((\sum_{r\in\mathbb{Z}_p}c_{r,p})-p\cdot\frac{m}{2p}\big)^2}{O(n\cdot m^2/P)}=\frac{(|X'|-m/2)^2}{O(n\cdot m^2/P)}=\frac{(m/2)^2}{O(n\cdot m^2/P)}=\Omega(P/n),\)

and hence, by our choice of \(k=\big\lceil\frac{m}{4P}\big\rceil\le\big\lceil\frac{m}{2p}\big\rceil\),

\(\mathbf{Pr}_{r^*\in\mathbb{Z}_p}[c_{r^*,p}\ge k]\ge\mathbf{Pr}_{r^*\in\mathbb{Z}_p}[c_{r^*,p}\ge\frac{m}{2p}]\ge\frac{\Omega(P/n)}{p}=\Omega(1/n).\)

Conditioned on \(c_{r^*,p}\ge k\) happening, we have at least _k_ integers \(t\in X'\subseteq X\) such that \(t\equiv r^*(modp)\). By definitions of _B_<sub>_r_<sup>∗</sup></sub> and _X_, this implies that there are at least _k_ integers \(t\in\mathbb{N}\) such that \(\#\{S\in B_{r^*}:w(S)=t\}\ge h\), with overall success probability at least \(0.9\cdot\Omega(1/n)=\Omega(1/n)\) over the choice of _p_ and _r_<sup>∗</sup>. \(\blacktriangleleft\)

Recall our algorithm subsamples \(C\subseteq B_{r^*}\) at rate \(\alpha\in(0,\frac{1}{2h}]\), and fails iff _w(S_) are distinct for all \(S\in C\). The failure probability of this step can be derived from the following lemma:

\(\blacktriangleright\) **Lemma 10.** _Let_ \(B'\) _be a collection of kh colored balls_ \((h\ge 2,k\ge 1)\)_, with exactly h balls of color i for each color_ \(i\in[k]\)_. Let_ \(C'\subseteq B'\) _be an i.i.d. subsample at rate_ \(\alpha\in[0,\frac{1}{2h}]\)_. Then_ \(C'\) _contains distinct colors with at most_ \(exp(-kh(h-1)\alpha^2/4)\) _probability._

**Proof.** For each color \(i\in[k]\), by Bernoulli’s inequality, the probability that \(C'\) includes exactly two balls of color _i_ is \(\genfrac(){pt}{2}{h}{2}\alpha^2(1-\alpha)^{h-2}\ge\genfrac(){pt}{2}{h}{2}\alpha^2\big(1-(h-2)\alpha\big)\ge\genfrac(){pt}{2}{h}{2}\alpha^2/2\). Hence, the probability that \(C'\) includes at most one ball of every color \(i\in[k]\) is at most \(\big(1-\genfrac(){pt}{2}{h}{2}\alpha^2/2\big)^k\le exp\big(-k\genfrac(){pt}{2}{h}{2}\alpha^2/2\big)=exp(-kh(h-1)\alpha^2/4)\). \(\blacktriangleleft\)

