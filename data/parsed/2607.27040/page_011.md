Let _C_ext(_m_) and _M_ext(_m_) denote the comparisons and moves respectively made during extraction. As \(s_i\le s\) and \(\sum_{i=0}^{s_\#}s_i\le m\), summing over all segments gives

\(C_\mathrm{ext}(m)=8s'_\#+\sum_{i=0}^{s_\#}(s_ilgs_i+O(s_i))\le 8s'_\#+\sum_{i=0}^{s_\#}(s_i(lgs+O(1))\le mlgs+O(m)M_\mathrm{ext}(m)=\sum_{i=0}^{s_\#}O(s_i)=O(m)\blacktriangleleft\)

## 2.6 Structure of Cache Lines

We now specify the two different designs for cache lines (defined in Section 2.1).

First, consider the _randomized cache line_ used in the **randomized approach**. We choose _g_=2<sup>⌊lglg_m_⌉</sup>, which satisfies (4). Let us denote: the cache line as the block of elements _g_<sub>1</sub>_...g_<sub>2_g_</sub>, and the corresponding cache integer as _d_, with bits _d_<sub>0</sub>_...d_lg_g_, where bit _d<sub>i</sub>_ has weight 2_<sup>i</sup>_. This is well defined as _g_ is a power of 2.

The process of insert(_x_) in a randomized cache line works as follows:

**1.** Probe for a buffer slot. Repeatedly select a uniformly random index \(j\in[1\dots 2g]\), check whether _g<sub>j</sub>_ is a buffer element, and retry if it is active until a buffer position _g<sub>j</sub>_ is found.

**2.** Swap the active element _x_ with _g<sub>j</sub>_, placing _x_ in the cache line.

**3.** Increment _d_ to reflect the new active element.

**4.** Return the state of the cache line (full or not), given by the value of the bit _d_lg_g_ with priority _g_.

Randomized cache lines store data sparsely like hash tables for constant-time insertions: at most _g_ active elements are spread among 2_g_ slots, capping the load factor at 1/2, so the expected number of probes is 1/(1-1/2)=2, each requiring one comparison. Then, the swap requires 3 moves. The increment of _d_ is _O_(1) amortized by aggregate analysis. Finally, checking for fullness requires reading the bit _d_lg_g_ using one comparison. In total, each insertion requires _O_(1) comparisons expected and _O_(1) moves amortized (see [App. C] for a more comprehensive analysis).

The operation _G<sub>i</sub>_.flush(_x_) is a simple linear scan with swaps. Iterating through _g_<sub>1</sub>_...g_<sub>2_g_</sub>, identify every active element _g<sub>j</sub>_, and swap _g<sub>j</sub>_ with the next available buffer space after _x_. Lastly, reset the cache integer by _d_:=0. This process uses 2_g_ comparisons and \(\le 3g+3\) moves.

**Theorem 2.6.** _A sequence A of m active elements can be sorted using m_lg_m+O(m_) _comparisons with exponentially high probability and always O(m_) _moves if given a buffer memory B containing_ 3_m_-1 _buffer elements and bit vector V of size m/_lg<sup>2</sup>_m._

**Proof.** By instating the randomized cache line design, cache insertions cost _O_(1) comparisons expected and _O_(1) moves amortized and cache flushes cost _O(g_) comparisons and _O(g_) moves (shown directly above). Substituting these costs into Lemmas 2.4 and 2.5 then summing them gives _m_lg_m+O(m_) comparisons expected and _O(m_) moves deterministically. Over _m_ cache insertions, the probability of large deviations (i.e. _\>m_ comparisons above the expected amount) is bounded by (27/32)_<sup>m</sup>_ (see the Chernoff tail bound in [App. C]). \(\blacktriangleleft\)

Next, we detail the mechanics of _deterministic cache lines_ for the **deterministic approach**. Deterministic cache lines consist of \(t'\) _cache blocks_ \(G_{t^\prime+1}\dots G_1\) from left to right, where _g<sub>i</sub>_=|_G<sub>i</sub>_| (we locally redefine _G<sub>i</sub>_ and _g<sub>i</sub>_ here). The block _G<sub>i</sub>_ consists of _g<sub>i</sub>/g_<sub>_i_-1</sub> _sub cache blocks A_<sub>1</sub>_...A<sub>j</sub>B_<sub>_j_+1</sub>_...B_<sub>_g<sub>i</sub>/g_<sub>_i_-1</sub> each of size _g_<sub>_i_-1</sub>, where _A_<sub>1</sub>_...A<sub>j</sub>_ contain only active elements and _B_<sub>_j_+1</sub>_...B_<sub>_g<sub>i</sub>/g_<sub>_i_-1</sub> contain only buffer elements.

The sizes are controlled by a parameter _t_ that satisfies \(2\le\left\lceil lg^{(t)}m\right\rceil\le lggm+1\). They are defined as _g_<sub>0</sub>=1, \(g_1=2^{\left\lceil lg^{(t)}m\right\rceil}\), and _g<sub>i</sub>=g_<sub>_i_-1</sub>2<sup>_g_<sub>_i_-1</sub>/2<sup>_i_-1</sup></sup> for all \(2\le i\le t'\), where \(t'\) is

