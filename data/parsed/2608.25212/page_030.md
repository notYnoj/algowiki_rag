## A Neighborhood complexity and versatile symmetric difference

We give a shorter (albeit non-algorithmic) proof for the inclusion of class families that can already be deduced in Lemma 26. In Theorem 33, we derive versatile symmetric difference from VC density thanks to the following fundamental result of Haussler.

**Theorem 32** (Haussler’s packing lemma \[32\])**.** _Let_ F _be a set system of VC dimension d_<sub>0</sub> _with_ |F|_\>_1 _on a finite domain D, and let_ \(c,\rho\ge 1\) _be real numbers such that_ \(\pi_\mathcal{F}(m)\le c\cdot m^\rho\) _for every positive integer m. Then_ \(d_0\le\mathcal{O}(\mathrm{log}c+\rho\mathrm{log}\rho)\)_, and there are distinct_ \(F,F'\in\mathcal{F}\) _such that_<tbc>

\(|F\triangle F'|\le d_0\cdot c^{1/\rho}\cdot\frac{|D|}{|\mathcal{F}|^{1/\rho}}=\mathcal{O}_{c,\rho}\left(\frac{|D|}{|\mathcal{F}|^{1/\rho}}\right).\)

<tbc>_Proof._ Since |F|_\>_1, we have \(d_0\ge 1\). Hence,

\(2^{d_0}\le\pi_\mathcal{F}(d_0)\le c\cdot d_0^\rho,\)

which implies that \(d_0\le\mathcal{O}(\mathrm{log}c+\rho\mathrm{log}\rho)\).

Let<tbc>

\(\delta:=\mathrm{min}\{|F\triangle F'|:F,F'\in\mathcal{F},F\neq F'\}.\)

<tbc>By Theorem 1 of \[32\], more precisely by the proof<sup>2</sup> of \[42, Lemma 5.14\],<tbc>

\(|\mathcal{F}|\le c\cdot\left(\frac{d_0|D|}{\delta}\right)^\rho.\)

<tbc>Rearranging gives

\(\delta\le d_0\cdot c^{1/\rho}\cdot\frac{|D|}{|\mathcal{F}|^{1/\rho}},\)

as required.

We can now prove the main result of this section. Note that a stronger algorithmic result is proved in Lemma 26.

**Theorem 33.** _For every fixed pair of real numbers_ \(c,\rho\ge 1\)_, there is a constant_ \(d:=d(c,\rho)\) _such that every n-vertex graph G with_ \((c,\rho)\)_-polynomial neighborhood complexity contains at least_ \(\lfloor n/8\rfloor\) _disjoint pairs of vertices u,v satisfying_ \(sd_G(u,v)\le dn^{1-1/\rho}\).

_Consequently, every hereditary graph class of VC density_ \(\rho\) _has versatile symmetric difference of exponent_ \(1-1/\rho\)_. In particular, every class of linear neighborhood complexity has bounded versatile symmetric difference._

_Proof._ Fix an _n_-vertex graph _G_ with \((c,\rho)\)-polynomial neighborhood complexity. Let \(U\subseteq V(G)\) be a largest subset of vertices without twins in _G_, that is, \(N_G(u)\neq N_G(u')\) for any distinct \(u,u'\in U\). For each \(u\in U\), let _C(u_) be the set of vertices in _V(G_) that are twins of _u_. Then \(\{C(u):u\in U\}\) forms a partition of _V(G_). We split the argument depending on whether \(|U|\le n/2\).

**Case** \(|U|\le n/2\)**:** For every \(u\in U\), pairing vertices arbitrarily inside _C(u_) gives \(\lfloor|C(u)|/2\rfloor\) disjoint pairs of twins. Thus, the total number of pairs is at least<tbc>

\(\sum_{u\in U}\left\lfloor\frac{|C(u)|}{2}\right\rfloor\ge\frac{1}{2}\sum_{u\in U}(|C(u)|-1)=\frac{n-|U|}{2}\ge\frac{n}{4}.\)

<sup>2</sup>The constant _C_<sub>2</sub> on page 158 of \[42\] is \(c\cdot d_0^\rho\) in our notation, and the last inequality on page 159, for P=F, gives \(|\mathcal{F}|=|\mathcal{P}|\le c\cdot(d_0|D|/\delta)^\rho\).

