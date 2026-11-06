The next algorithm relies on the existence of the map _f_ as above, but does not require to compute it explicitly.

**Lemma 26.** _Fix real numbers_ \(c,\rho\ge 1\) _and_ \(\delta>0\)_, and let_ \(\alpha:=1-1/\rho\)_. There is a Las Vegas randomized algorithm that, given an n-vertex graph G with_ \((c,\rho)\)_-polynomial neighborhood complexity and a set_ \(U\subseteq V(G)\) _with_ \(|U|\ge max(\delta n,2)\)_, outputs in expected time_

\(\mathcal{O}_{c,\rho,\delta}\left(n+\sum_{u\in U}deg_G(u)\right)\)

_a set of_ \(\Omega_{c,\rho,\delta}(|U|)\) _disjoint pairs of_ \(\mathcal{O}_{c,\rho,\delta}(n^\alpha)\)_-near-twins contained in U._

_Proof._ We may assume that \(\delta\le 1\). If \(|U|<2^{\rho+1}c\), then \(n\le|U|/\delta=\mathcal{O}_{c,\rho,\delta}(1)\). An arbitrary maximal pairing of _U_ has size at least |_U|/_4, and every pair has symmetric difference at most \(n=\mathcal{O}_{c,\rho,\delta}(n^\alpha)\), so we are done. Henceforth assume that \(|U|\ge 2^{\rho+1}c\).

We first consider the case when _U_ contains no pair of vertices which are twins in _G_. Let<tbc>

\(\mathcal{F}:=\{N_G(u)|u\in U\}\)

<tbc>be the set system with domain _V(G_) of neighborhoods of vertices of _U_. The members of F are distinct, and, since _G_ has \((c,\rho)\)-polynomial neighborhood complexity,<tbc>

\(\pi_\mathcal{F}(m)\le\pi_G(m)\le c\cdot m^\rho\)

<tbc>for every positive integer _m_. Let _d_<sub>0</sub> be the VC dimension of F. Since \(|\mathcal{F}|=|U|\ge 2\), we have \(d_0\ge 1\), and

\(2^{d_0}\le\pi_\mathcal{F}(d_0)\le c\cdot d_0^\rho.\)

Consequently, there is an integer \(d:=d(c,\rho)\), fixed independently of the input, such that \(d_0\le d\).

Let<tbc>

\(s:=\left[\left(\frac{|U|}{2c}\right)^{1/\rho}\right],\varepsilon:=\frac{1}{16},k:=\left\lceil\frac{2dn}{\varepsilon s}\right\rceil.\)

<tbc>Our lower bound on |_U_| ensures that<tbc>

\(s\ge\frac{1}{2}\left(\frac{|U|}{2c}\right)^{1/\rho}\text{and}cs^\rho\le\frac{|U|}{2}.\)

<tbc>Moreover,<tbc>

\(k\le 1+\frac{4dn(2c)^{1/\rho}}{\varepsilon|U|^{1/\rho}}\le\mathcal{O}_{c,\rho,\delta}\left(n^{1-\frac{1}{\rho}}\right).\)

<tbc>Fix a map _f_ as in Lemma 25, using the upper bound _d_ on the VC dimension. For an _s_-sample _S_, we call an element \(F\in\mathcal{F}\) _bad_ (with respect to _S_) if<tbc>

\(|F\triangle f(S,F\cap S)|\ge\frac{k}{2}.\)

<tbc>By Lemma 25, for any fixed \(F\in\mathcal{F}\), the probability over the random choice of _S_ that _F_ is bad is at most \(\varepsilon\). Thus, the expected number of bad elements of F is at most \(\varepsilon|U|\). By Markov’s inequality,<tbc>

\(\mathbb{P}_{S\sim V(G)^s}\left(|\{F\in\mathcal{F}|F\text{is bad with respect to}S\}|>|U|/8\right)\le\frac{\varepsilon|U|}{|U|/8}=8\varepsilon=\frac{1}{2}.\)

