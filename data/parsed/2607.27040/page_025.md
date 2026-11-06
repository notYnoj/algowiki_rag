require only \(\left\lceil lgk'\right\rceil\) comparisons. For \(m'\) elements, this is \(m'\left\lceil lgk'\right\rceil+O(m')\) comparisons. Applying the naive bound for the first _k_<sub>#</sub>-1 passes, and the tighter bound for the final pass, we have the total number of comparisons \(C''(m')\) to sort a sequence of \(m'\) elements using the algorithm

\(C^{^{^\prime}}\left(m'\right)=m'lgk-m'+(k_\#-1)\left(m'lgk+O(m')\right)+m'\left\lceil lgk'\right\rceil+O(m')\)<br> \(\le m'lgk_\#+m'\left\lceil lg\left\lceil m'/k_\#\right\rceil\right\rceil-m'+o(m')\)<br> \(\le m'lgk_\#+m'lg(m/k_\#)+m'-m'+o(m')\)<br> \(\le m'lgm'+o(m')\)

The number of moves made by the final merge pass is still \(3m'\). As a result, the naive bound is tight, which counts \(3m'\) moves for the initial run sorting, and \(3m'\) moves for each of the _k_<sub>#</sub> subsequent merge passes. By (B.1), (B.2) and (B.3), \(k_\#=\left\lceil lgm'/lgk\right\rceil-1=O(1)\) when \(m'=O(lg^cm)\) and word width \(w\ge lgm\) bits, giving the final bounded moves \(M''\left(m'\right)=3\left(k_\#+1\right)m'=O(m')\).

\(\blacktriangleright\) **Lemma B.1.** _For any constant c, a sequence of_ \(m'=O(lg^cm)\) _active elements can be sorted using no more than_ \(m'lgm'+o(m')\) _comparisons and_ \(O(m')\) _movies if given a merge buffer of_ \(m'\) _buffer elements._

## C Analysis of Cache Lines

Recall that we have two designs of cache lines, the randomized and deterministic design.

## C.1 Randomized Cache Lines

First, we analyze randomized cache lines. We have

\(g=2^{\left\lceil lglgm\right\rceil}\) (C.1)

A randomized cache line contains at most _g_ active elements spread in 2_g_ spaces, then the probability of any uniformly random _g<sub>i</sub>_ being active is at most 1/2. Thus, from uniformly randomly probing in step 1 of insertion, the expected number of probes is bounded by 1/(1-1/2)=2. This is averaged over all possible streams of random bits ("coin flips") used to choose random _g<sub>i</sub>_. Each probe uses a single comparison to check if _g<sub>i</sub>_ is buffer, giving 2 comparisons on average for probing in step 1. Then, swapping _x_ with the found buffer space _g<sub>i</sub>_ in step 2 requires 3 data moves. Incrementing _d_ in step 3 is implemented as a binary increment over its \(\left\lfloor lgg\right\rfloor+1\) bits. A single increment may read and flip all bits, but over a sequence of an arbitrary number of increments from 0, the amortized cost of each increment is _O_(1). This is because the _j_th bit is read then flipped every 2_<sup>j</sup>_ increments, and by aggregate analysis over an arbitrary number _k_ increments from 0, we have the amortized number of read and write operations per increment

\(\left(\sum_{i=0}^k\left\lfloor 1/2^i\right\rfloor\right)/k<2\)

This bound holds for any positive integer _k_. As every read operation requires 1 comparison and every write 3 moves, this is 2 comparisons and 6 moves amortized. The final step, checking if the cache line is full requires a read operation of the bit _d_lg_g_. This is because if bit _d_lg_g_ (this is well defined as _g_ is a power of 2 by (C.1)) with priority 2lg_g_=_g_ by is 1, \(d\ge g\),

