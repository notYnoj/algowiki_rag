**Theorem 3** (Noisy Binary Search Lower Bound)**.** _Any (deterministic or randomized) algorithm for_ NoisyBinarySearch(_n_) _with error probability_ \(\le\delta\) _must make at least_

\((1-o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right)\)

_noisy comparisons in expectation, even if the position of the element to search for is uniformly random._

This lower bound indicates that, any algorithm for NoisySorting(_n_) purely based on binary insertion sort, which requires _n_-1 executions of Noisy Binary Search with average error probability _o_(1_/n_), needs at least \((1-o(1))\left(\frac{1}{I(p)}+\frac{2}{(1-2p)log\frac{1-p}{p}}\right)nlogn\) noisy comparisons in expectation to achieve error probability _o_(1). In light of Theorem 1, we see that any algorithm for Noisy Sorting purely based on binary insertion sort cannot be optimal.

We also show an algorithm for NoisyBinarySearch(_n_) that matches with the lower bound in Theorem 3:

**Theorem 4** (Noisy Binary Search Upper Bound)**.** _There exists a randomized algorithm for_ NoisyBinarySearch(_n_) _with error probability_ \(\le\delta\) _that makes at most_

\((1+o(1))\left((1-\delta)\frac{logn}{I(p)}+\frac{2log\frac{1}{\delta}}{(1-2p)log\frac{1-p}{p}}\right)\)

_noisy comparisons in expectation._

### Concurrent Work.

Concurrent work \[WGZW23\] also improves over \[WGW22\] in many aspects. Our results are stronger than their main results. Our algorithm in Theorem 1 uses fewer noisy comparisons than their algorithms in expectation \[WGZW23, Theorem 1 and 2\]. Our Theorem 2 is strictly stronger than \[WGZW23, Theorem 3\]. Our lower bound for insertion-based sorting algorithms (see discussion after Theorem 3) is strictly stronger than \[WGZW23, Theorem 4\].

### Other Related Works.

People have also considered Noisy Sorting in a slightly different noisy model, where every pair of elements is allowed to be compared at most once \[BM08, KPSW11, GLLP17, GLLP20, GLLP19\]. Sorting is harder in this model than the model we consider, as it is information-theoretically impossible to correctly sort all the elements with 1-_o_(1) probability for _p\>_0 \[GLLP17\]. For _p\<_1/16, Geissmann, Leucci, Liu, Penna \[GLLP19\] achieved an _O(n_log_n_) time algorithm that guarantees _O_(log_n_) maximum dislocation and _O(n_) total dislocation with high probability, matching the lower bound given in \[GLLP17\].

### Acknowledgements.

We thank Przemysław Uznański for telling us about the issue of \[BH08\].

## 1.1 Technical Overview

Before we give the overview of our techniques, let us first give some intuitions about the constant, \(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\) , in our bound. _I(p_) is essentially the amount of information in bits each noisy<tbc>

