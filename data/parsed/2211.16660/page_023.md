## A Proof of Lemma 4.4

Lemma 4.4 is essentially a corollary of the stronger combinatorial structure lemma \[GHL22, Lemma 4.1\], except that the constant dependences are superior and we make the additional assumption that the lengths involved are all powers of two. For completeness, we include a proof here which is significantly simpler than the proof of \[GHL22, Lemma 4.1\].

**Lemma** (Lemma 4.4, restated)**.** _For_ \(\varepsilon=10^{-5}\) _and w sufficiently large, at least one of the following two conditions holds for every string_ \(x\in\{0,1\}^w\).

1. _There exists_ \(\ell\in[\varepsilon^2w,w]\) _equal to a power of two and an_ 0.1_-imbalanced interval I in x of length_ \(\ell\).<tbc>

_2._ _There exists_ \(\ell\in[1,\varepsilon^2w)\) _equal to a power of two such that the number of_ \(\ell^+\)_-flags in x is at least_ \(\varepsilon w\)_, and x contains_ \((0^\ell 1^\ell)^{\varepsilon w/\ell}\) _as a subsequence._

_Proof._ We first reduce to the case that _w_ is a power of two. Indeed, suppose we show the statement for all lengths \(w'\) equal to sufficiently large powers of 2, with a stronger \(\varepsilon'=10^{-4}\) in place of \(\varepsilon\). Then, let \(w'\) be the largest power of two at most _w_, and let \(x'=x_{[w^\prime]}\) be the prefix of _x_ of length \(w'>w/2\). Applying our assumption to \(x'\), the lemma statement holds for \(x'\) with stronger \(\varepsilon'=10^{-4}\). If \(x'\) falls into the first case of the lemma, then \(x'\) contains a 0.1-imbalanced interval _I_ of length \(\ell\in[(\varepsilon')^2w',w']\subseteq[\varepsilon^2w,w]\), so _x_ must fall into the first case as well.

Otherwise, there exists \(\ell\in[1,(\varepsilon')^2w')\) equal to a power of two such that the number of \(\ell^+\)-flags in \(x'\) is at least \((\varepsilon')^2w'\ge\varepsilon w\), and \(x'\) contains \((0^\ell 1^\ell)^{(\varepsilon^\prime)^2w^\prime/\ell}\supseteq(0^\ell 1^\ell)^{\varepsilon^2w/\ell}\). If \(\ell\ge\varepsilon^2w\), then the existence of an \(\ell^+\)-flag implies that there is a 0.1-imbalanced interval of length at least \(\ell\) in \(x'\), so _x_ again falls into the first case of the lemma. On the other hand, if \(\ell<\varepsilon^2w\) then _x_ falls into the second case of the lemma, as desired.

Thus, we assume _w_ is a power of two and prove this special case with the stronger constant \(\varepsilon=10^{-4}\). Let _w_=2_<sup>K</sup>_, and for any \(0\le k\le K\) and \(1\le i\le 2^{K-k}\), define \(I_{k,i}:=[(i-1)\cdot 2^k+1,i\cdot 2^k]\) to be an aligned dyadic interval of length 2_<sup>k</sup>_. Observe that for each _k_, the intervals _I<sub>k,i</sub>_ form a partition of \[_w_\]. If _I<sub>k,i</sub>_ is 0.1-imbalanced for some _k_ satisfying \(2^k\ge\varepsilon^2w\), case 1 holds and we are done. Thus, we may assume _I<sub>k,i</sub>_ is 0.1-balanced whenever \(2^k\ge\varepsilon^2w\). We would like to show that case 2 above always holds.

Call an interval _I_ is _sparse_ if _d(x<sub>I</sub>)\<_0.01, and _dense_ otherwise. Let S_<sub>k</sub>_ denote the collection of all maximal sparse dyadic intervals _I<sub>k,i</sub>_ of length 2_<sup>k</sup>_, i.e. all sparse dyadic intervals _I<sub>k,i</sub>_ that are not proper subintervals of other sparse \(I_{k^\prime,i^\prime}\). Let \(\mathcal{S}=\bigcup_{k=0}^K\mathcal{S}_k\), so that S is the collection of all maximal sparse dyadic intervals in _x_, and the elements of S are pairwise disjoint.

Observe that sparse intervals are certainly 0.1-imbalanced, so by our previous assumption, S_<sub>k</sub>_ is empty if \(2^k\ge\varepsilon w\). On the other hand, we also assumed that _I_<sub>_K,_1</sub>=\[_w_\] is 0.1-balanced, so the number of zeros in _x_ is at least 0.4_w_. Every zero-bit in _x_ constitutes a sparse dyadic interval _I_<sub>0_,i_</sub> of length 1 by itself, and every sparse dyadic interval lies inside some element of S. Thus, intervals in S cover all zero-bits in _x_ and have total length at least 0.4_w_.

Let if _I=I<sub>k,i</sub>_ and _i\>_1, define the _predecessor_ of _I_ to be pred(_I_):=_I_<sub>_k,i_-1</sub>.

