the largest integer such that \(g_{t^\prime}<\mathrm{lg}m\). To account for any remaining space, we define the final term (overrides _g_<sub>1</sub> base case when \(t'=0\)):

\(g=g_{t^\prime+1}=g_{t^\prime}\lceil\mathrm{lg}m/g_{t^\prime}\rceil\le g_{t^\prime} 2^{g_{t^\prime}/2^{t^\prime-1}}\)

This ensures \(\mathrm{lg}m\le g\le 2\mathrm{lg}m\) as in (4), and that cache lines take up no more than 2_g_ spaces [App. C]. The recurrence makes _g<sub>i</sub>_ grow as a tower of exponentials, so the number of levels is proportional to _t_. It can be shown \(t'\le t-1\) by induction [App. C]. This growth also guarantees that the amortized comparison cost at levels \(i\ge 2\) form a convergent geometric series, shown shortly.

The procedure for insert(_x_) iterates through levels \(i=1\dots t'+1\). At every level:

**1.** Binary search in _G<sub>i</sub>_ for the next available sub cache block _B_<sub>_j_+1</sub> of buffer elements.

**2.** Swap the entire contents of the lower leveled cache block _G_<sub>_i_-1</sub> (or simply _x_ when _i_=1) into the found buffer block.

**3.** If this fills _G<sub>i</sub>_ (i.e. the last buffer block _B_<sub>_g<sub>i</sub>/g_<sub>_i_-1</sub> was used), we continue to level _i_+1, otherwise insertion completes returning 0.

If the loop ends without insert terminating, the last block \(G_{t^\prime+1}\) has been filled, and the cache line is full thus the procedure returns 1.

At level _i_, the lg(_g<sub>i</sub>/g_<sub>_i_-1</sub>) comparisons to locate a buffer block by binary search is spread among _g_<sub>_i_-1</sub> elements to lg(_g<sub>i</sub>/g_<sub>_i_-1</sub>)/_g_<sub>_i_-1</sub> comparisons per element. For \(i\ge 2\), the recurrence yields \(\mathrm{lg}\left(g_i/g_{i-1}\right)/g_{i-1}\le 1/2^{i-1}\). Summing over all levels, the total comparisons per element are \(\mathrm{lg}g_1+\sum_{i=2}^{t^\prime+1}1/2^{i-1}<\mathrm{lg}^{(t)}m+2\). Each element passes through every level once by a single swap costing 3 moves, which over all levels is \(3\left(t'+1\right)\le 3t\) moves.

The operation _G<sub>i</sub>_.flush(_x_) iterates through all cache blocks \(G_{t^\prime+1}\dots G_1\) in descending order of level, where for each cache block a binary search locates last sub cache block containing active elements _A<sub>j</sub>_, swapping all active elements in the cache block in _A_<sub>1</sub>_...A<sub>j</sub>_ to the next available buffer spaces after _x_. Because each level has _O_(lg_m_) sub cache blocks, each binary search costs _O_(lglg_m_) comparisons. With \(t'=O(\mathrm{lg}^*m)\) levels, the total comparisons are \(O(\mathrm{lg}\mathrm{lg}m\cdot\mathrm{lg}^*m)\). Each active element is swapped exactly once, totaling 3_g_ moves.

\(\blacktriangleright\) **Theorem 2.7.** _A sequence A of m active elements can be sorted using no more than_ \(m\mathrm{lg}m+O(m\mathrm{lg}^{(t)}m)\) _comparisons and O(tm_) _movies if given a buffer memory B containing_ 3_m_-1 _buffer elements and bit vector V of size m/_lg<sup>2</sup>_m._

**Proof.** The result follows by a parallel derivation to Theorem 2.6, substituting the deterministic cache operation costs (shown just above) into the bounds of Lemmas 2.4 and 2.5. \(\blacktriangleleft\)

\(\blacktriangleright\) Remark 2.8. The deterministic additional memory algorithm is stable on the active elements, i.e. the relative order of equal active elements in the output is identical to the input. This does not apply to the randomized variant as active elements are placed arbitrarily in randomized cache lines. However, any in-place adaptation is unstable as the buffer memory is simulated by elements in the array, which are scrambled arbitrarily. If the buffer memory does not contain any equal array elements (e.g. if it is external or an explicitly collected distinct buffer), global stability holds. A full proof of this claim is in [App. C].

## 2.7 Handling Short Blocks

During the analysis, we have assumed _m_ is sufficiently large. When _m\<_2<sup>19</sup>=524288, we use table sort from [9] applying merge sort on pointers as a fallback. This uses _O_(1) words as _m_ is constant, albeit large, and works within the bounds of Theorems 2.6 and 2.7.

