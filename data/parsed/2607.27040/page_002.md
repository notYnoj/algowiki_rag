## 1 Introduction

Sorting is one of the most fundamental problems in computer science, carrying great practical and theoretical importance. For a comparison-based sort on a data set of _n_ elements, it is well known that the information-theoretic lower bound is lg(_n_!)≈_n_lg_n_-1.4427_n_ comparisons, which also holds for the average case, and at least ⌊1.5_n_⌋ moves are required to permute the input [11]. Summing gives a lower bound on total operations (i.e. sum of comparisons and moves) of ≈_n_lg_n_+0.0573_n_. Note that all logarithms throughout this paper are base 2.

In-place sorting is essential for large datasets in memory-constrained environments. A strict in-place algorithm uses only a single extra element storage location aside from the input array to permute elements and _O_(1) auxiliary words of size at least lg_n_ bits for tracking.

Simultaneously minimizing comparisons, moves, and auxiliary workspace represents a classic frontier in the complexity of sorting, dating back to foundational limits established by Munro and Raman, i.e. to achieve minimal comparisons under _O(n_) moves and in-place constraints. Currently, the tightest upper bound (for both average and worst-case behavior) is _n_lg_n+O(n_lggl_n_) comparisons and \((34+\varepsilon)n\) moves [4].

Whether the _O(n_glgl_n_) term could be reduced was left as an open problem. In this paper we resolve this open problem by presenting two variations of our in-place algorithm: a randomized and deterministic approach. Both variations are unstable. For any input, the randomized approach performs _n_lg_n+O(n_) comparisons with exponentially high probability (over the algorithm’s random choices) and always _O(n_) moves. This probabilistically achieves the ultimate goal of in-place sorting with minimal extra comparisons and moves (see [4, 10]), and matches the total operation lower bound of _n_lg_n_+0.0573_n_ up to an additive linear term. The deterministic approach makes _n_lg_n+O(n_lg<sup>(_t_)</sup>_n_) comparisons and _O(tn_) moves in the worst case, where _t_ is an integer parameter satisfying \(2\le t\le lg^*n-1\), thereby narrowing the gap to this ultimate goal: using constant _t\>_2 yields a definitive improvement over [4]. Total operations are minimized when _t_≈lg<sup>∗</sup>_n_: comparisons reach the optimal _n_lg_n+O(n_), whilst the move count degenerates slightly to _O(n_lg<sup>∗</sup>_n_).

### 1.1 Technical Overview

In Section 2, we detail the two-level structure reminiscent of y-fast tries in [12] that is used to facilitate sorting assuming the existence of additional memory:

The upper level is an ordered set containing _s<sub>#</sub> active representatives_ that supports searches in l_gs<sub>#</sub>+O_(1) comparisons and insertions in _O_(lg<sup>3</sup>_s<sub>#</sub>_) time (see Section 2.2).

Each active representative corresponds to lower-level _segment_, which is a block of size \(s=\Theta(lg^4s_#)\).

The upper level’s optimal search is used to route inserted elements towards segments. Elements are temporarily stored in a cache line (see Sections 2.4 and 2.6) within an active representative before they are flushed into segments in batches. Only when a segment becomes full and is split into two segments each containing half the elements, is a new active representative inserted for the new segment, ensuring costly upper level insertions are sparse.

Although the upper level maintains the sorted order of segments, elements in segments are kept unsorted until extraction, where they are sorted by the procedure in Section 2.3.

Lastly, in Section 3 we demonstrate a method to carve out the additional memory directly from the input array, thus achieving truly in-place sorting.

The key improvements over [4] are: the new ordered set, two optimized cache structures, and optimal segment sorting. Each change shaves off an independent _O(n_glgl_n_) term in comparisons, thus all three are required simultaneously to yield an improved bound.

