a subset of _V_ of size at least _s_. In particular, applying the above lemma we can immediately obtain the following.

**Lemma 2.5.** _Let G be a graph on n vertices. There is a deterministic algorithm `Dominate` and randomized algorithm `RDominate` that computes a dominating set D of size_ \(O\left(\frac{nlogn}{s}\right)\) _of V<sub>s</sub> in time O(m+ns_) _and O(n_) _respectively._

**Lemma 2.6.** _Let G be a graph on n vertices. Given degree thresholds s_<sub>1</sub>_\>s_<sub>2</sub>_\>...\>s_<sub>_k_-1</sub>_, there is a deterministic algorithm `Decompose` and a randomized algorithm `RDecompose` that outputs edge sets_ \(\{E_i\}_{i=1}^k\)_, edge set E_<sup>∗</sup>_, and vertex sets_ \(\{D_i\}_{i=1}^k\) _satisfying,_

1. \(E_i=\{(u,v)\in E\text{\textit{s.t.}}min(deg(u),deg(v))<s_{i-1}\}\) _is the set E_<sub>_s<sub>i</sub>_-1</sub>.<tbc>

_2._ _D<sub>i</sub> dominates_ \(V_{s_i}=\{v\in V\text{\textit{s.t.}}deg(v)\ge s_i\}\) _and_ \(|D_i|=\tilde{O}\left(\frac{n}{s_i}\right)\)_. For convenience, V<sub>s<sub>i</sub></sub> may also be denoted V<sub>i</sub>._<tbc>

_3._ \(D_1\subset D_2\subset\dots\subset D_k=V\) _and_ \(E_k\subset E_{k-1}\subset\dots\subset E_1=E\).<tbc>

_4._ \(E^*=\bigcup_{i=1}^kE_i^*\) _where each_ \(E_i^*\subset E\) _has for every_ \(v\in V_i\)_, at least one edge_ \((v,w)\in E_i^*\) _for_ \(w\in D_i\).

_Furthermore, `Decompose` runs in_ \(\tilde{O}(kn^2)\) _time and `RDecompose` runs in_ \(\tilde{O}(kn)\) _time. Note that `RDecompose` satisfies the above conditions with high probability._

_For a given vertex_ \(v\in V\)_, define the_ **level of** _v, denoted_ \(\ell(v)\)_, as the integer i such that_ \(s_i\le deg(v)<s_{i-1}\)_. For a given edge_ \(e\in E\)_, define the_ **level of** _e, denoted_ \(\ell(e)\)_, as the integer i such that_ \(e\in E_i\backslash E_{i+1}\).

For sake of completeness, these proofs are given in Appendix B.

We also quote a result from Baswana and Kavitha \[BK10\] that we use crucially for our randomized algorithms (Section 3.1 and Section 4).

**Theorem 2.7** (\[BK10\])**.** _There exists a randomized algorithm `BK2apasp` that returns a_ (2,0)_- approximation of APSP on undirected unweighted graphs with an expected running time complexity_ \(\tilde{O}\left(m\sqrt{n}+n^2\right)\) _and space complexity O(n_<sup>2</sup>).

## 3 Improved (2,0)-Approximation

In this section, we provide improved running time bounds for a (2,0)-approximation of APSP on unweighted, undirected graphs. We begin with a simple randomized algorithm followed by a slightly slower deterministic algorithm.

### 3.1 A Randomized (2,0)-Approximate APSP

We prove the following theorem

**Theorem 3.1.** _Let G be an undirected, unweighted graph with n vertices. Algorithm 1 computes a_ (2,0)_-approximate APSP solution in expected time_ \(\tilde{O}\left(n^{2.03184039}\right)\).

#### High Level Overview

We begin by briefly recapping the powerful idea of degree decomposition in computing APSP approximations, first initiated by the work of Aingworth, Chekuri, Indyk, and Motwani \[ACIM99\]. The idea is roughly as follows. If we consider all vertices with degree at least _n_<sup>1/2</sup>, there will be a small set _D_ of size _n_<sup>1/2</sup>log_n_ such that every vertex of high degree has a neighbor<tbc>

