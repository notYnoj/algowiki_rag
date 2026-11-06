## 1 Introduction

One of the grand challenges in parallel computing is to overcome the _transitive closure bottleneck_ \[KK93\]: the observation that computing reachability in directed graphs apparently requires <u>either</u> superlinear work (iterated matrix squaring) to achieve polylog(_n_) depth, or \(n^{\Omega(1)}\) depth to achieve near-linear work. The problem of simultaneously achieving _m_<sup>1+_o_(1)</sup> work and _m_<sup>_o_(1)</sup> depth has remained an elusive goal for decades, for reachability and harder problems such as shortest paths and (min-cost) flows.

Naturally, researchers have tried to overcome this bottleneck in various ways. These efforts have been extremely fruitful, leading to the development of _hopsets_ \[Coh00\] for computing approximate shortest paths, _shortcuts_ \[UY91\] to achieve work-depth tradeoffs, min-sketches for estimating transitive closure size \[Coh97\], and attention to graph classes where the bottleneck does not exist, e.g., planar graphs \[KK93\]. In 1992, Thorup \[Tho92\] made a bold, purely combinatorial conjecture that was motivated by the transitive closure bottleneck.

**Conjecture 1** (Thorup’s Shortcut Conjecture \[Tho92\])**.** _Let G_<sup>∗</sup>=(_V,E_<sup>∗</sup>) _be the transitive closure of an arbitrary directed graph G_=(_V,E), with m_=|_E|. There exists a_ shortcut \(E_+\subset E^*\) _with_ \(|E_+|\le m\) _such that_ \(G_+=(V,E\cup E_+)\) _has_ polylog(_n_) _diameter, that is,_ dist<sub>_G_<sub>+</sub></sub>(_u,v_)=polylog(_n), for every_ \((u,v)\in E^*\).

In other words, once the shortcut _E_<sub>+</sub> is discovered in preprocessing, single-source reachability could be computed near-optimally, in \(\tilde{O}(m)\) work and \(\tilde{O}(1)\) depth. Conjecture 1 was known for rooted trees \[Cha87\] with a diameter<sup>1</sup> of \(O(\alpha(n,n))\) and later confirmed for planar graphs \[Tho95\] with a diameter of \(O(\alpha(n,n)log^2n)\).<sup>2</sup> Thorup \[Tho92\] insisted on \(|E_+|\le m\), but one could set any number of thresholds for the shortcut size, e.g., _O(m),m_<sup>1+_o_(1)</sup>_,n_<sup>1.5</sup>_,n_<sup>1.99</sup>, etc. In 2003 Hesse \[Hes03\] refuted Conjecture 1 and many weaker versions of it.

**Theorem 1.1** (Hesse \[Hes03\])**.** _For any_ \(\epsilon>0\) _and n sufficiently large, there exist n-vertex graphs G_=(_V,E_) _and_ \(G'=(V,E')\) _with_ \(m,m'\) _edges, respectively, such that:_

• \(m=\Theta(n^{19/17})\) _and any shortcut for G with o(n_<sup>1/17</sup>) _diameter must have_ \(\Omega(mn^{1/17})\) _edges._<tbc>

• \(m'=n^{1+\epsilon}\) _and any shortcut for_ \(G'\) _with n_<sup>_o_(1)</sup> _diameter must have_ \(\Omega(n^{2-\epsilon})\) _edges._

Theorem 1.1 precludes the most optimistic outcome, but it still leaves open many fascinating and potentially practical questions, such as: what diameter can be achieved with \(\tilde{O}(m)\)- or \(\tilde{O}(n)\)- size shortcuts? And can such shortcuts be computed efficiently? It is now known that the optimum diameters for \(\tilde{O}(n)\)- and \(\tilde{O}(m)\)-size shortcuts are in the ranges \([\tilde{\Omega}(n^{1/4}),\tilde{O}(n^{1/3})]\), and \([\tilde{\Omega}(n^{2/9}),\tilde{O}(n^{2/3}/m^{1/3})]\), respectively, and that the upper bounds can be attained in polynomial time. See  1 for details and references.

### 1.1 Reviving Conjecture 1

The shortcut problem, as Thorup \[Tho92\] originally defined it, is now well on its way to being completely solved, as we have narrowed down the correct exponent to a small range and just a couple plausible answers: 1/4 or 1/3.

However, Conjecture 1 is perhaps _too strict_ from the algorithmic perspective. This is because the final goal is to somehow replace a directed graph _G_=(_V,E_) with _any G_<sub>+</sub> of comparable size such that (1) the transitive closure of _G_ can be extracted from the transitive closure of _G_<sub>+</sub>, and (2) every \((u,v)\in E^*\) is witnessed by a "short" _u-v_ path in _G_<sub>+</sub>. We propose the following small fix to Conjecture 1 by allowing _G_<sub>+</sub> to introduce _Steiner vertices_.

<sup>1</sup>The _diameter_ of a directed graph is defined to be the largest _finite_ distance. <sup>2</sup>A corollary of Thorup’s planar reachability oracle \[Tho04\] implies a shortcut with size _O(n_log_n_) and diameter 4.

