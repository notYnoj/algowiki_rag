## 4 A polynomial-space algorithm

We now consider poly(_n_)-space algorithms for Pigeonhole Equal Sums. The straightforward binary search approach (described at the end of Section 2) can be adapted to run in _O_<sup>∗</sup>(2_<sup>n</sup>_) time and poly(_n_) space: instead of using meet-in-middle (Lemma 3, which requires large space), we count the number of valid subsets \(S\subseteq[n]\) by brute force in _O_<sup>∗</sup>(2_<sup>n</sup>_) time and only poly(_n_) space.

We improve this _O_<sup>∗</sup>(2_<sup>n</sup>_) running time using the ideas from earlier sections. Again, consider two cases depending on whether parameter _d_ from Equation (3) is small or large.

\(\blacktriangleright\) **Lemma 11.** _Given parameter_ \(\Delta\le 2^n/(3n^2)\)_, Pigeonhole Equal Sums with_ \(d\le\Delta\) _can be solved deterministically in_ poly(_n_) _space and_ \(O^*(\Delta)\) _time._

**Proof Sketch.** The proof is almost the same as Lemma 4 (see Section 3.1), with the only difference in Case 3 from the proof of Lemma 7: instead of using meet-in-middle, here we count the valid subsets \(A'\subseteq A\) by brute force in \(O^*(2^{|A|})=O^*(2^{i^*})=O^*(\Delta)\) time and only poly(_n_) space. \(\blacktriangleleft\)

To solve the large _d_ case, we need the low-space element distinctness algorithm by Beame, Clifford, and Machmouchi [7] (generalized in [6], and with a non-standard assumption removed by [11, 16]). This algorithm was also previously used for Subset Sum [6] and Equal Sums [17]. The following statement can be inferred from [11, Section 4.2 (proof of Theorem 1.1)].

\(\blacktriangleright\) **Theorem 12** (Low-space Element Distinctness, [7, 6, 11])**.** _Given random access to an integer list a_<sub>1</sub>_,...,a<sub>N</sub> (where_ \(a_i\in[\mathrm{poly}(N)]\)_) that contains at least one pair_ \((i,j)\in[N]\times[N]\) _with_ \(a_i=a_j,i\neq j\)_, there is a randomized algorithm that reports such a pair using_ polylog_N working memory and_

\(O\left(\frac{N\sqrt{F_2}}{F_2-N}\cdot\mathrm{polylog}N\right)\)

