<tbc>**Theorem 2** (Noisy Sorting Lower Bound)**.** _Any (deterministic or randomized) algorithm for_ NoisySorting(_n_) _with error probability o_(1) _must make at least_

\((1-o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\)

_noisy comparisons in expectation, even if the input is a uniformly random permutation._

To compare with previous works more quantitatively, our constant is roughly 2.27755 for _p_=0.1. When _p_ approaches 0, i.e., when the noisy comparisons are almost errorless, our bounds approach \((1\pm o(1))nlogn\), matching the bounds of classical sorting.

## Noisy Binary Search.

We also study the closely related Noisy Binary Search problem. In NoisyBinarySearch(_n_), we are given a sorted list of _n_ elements and an element _x_, and the goal is to find the predecessor of _x_ in the sorted list. Noisy Binary Search is well-studied \[Hor63, BZ74, FRPU94, BH08, Pel89, DLU21\] in the noisy model we consider, as well as in some other models \[AD91, BK93, DGW92, Mut94, RMK<sup>+</sup>80\].

Both previous algorithms \[FRPU94, WGW22\] for NoisySorting(_n_) use binary insertion sort at the high level. More specifically, the algorithms keep a sorted array of the first _i_ elements for _i_ from 1 to _n_. When the _i_-th element needs to be inserted for _i\>_1, the algorithms use some implementations of NoisyBinarySearch(_i_-1) to find the correct position to insert it, with error probability _o_(1_/n_) (it also suffices to have average error probability _o_(1_/n_)). A simple union bound then implies that the error probability of the sorting algorithm is _o_(1). The difference between the two algorithms is that \[FRPU94\] uses an algorithm for Noisy Binary Search based on random walk, while \[WGW22\] builds on Burnashev and Zigangirov’s algorithm \[BZ74\].

In fact, a variable-length version of Burnashev and Zigangirov’s algorithm \[BZ74\] achieves optimal query complexity for the Noisy Binary Search problem.<sup>3</sup> They proved that NoisyBinarySearch(_n_) with error probability \(\delta\) can be solved using at most \(\frac{logn+log(1/\delta)+log((1-p)/p)}{I(p)}\) noisy comparisons in expectation (we remark that their algorithm is randomized and assumes uniform prior). Information theoretical lower bound (e.g., \[BH08, Theorem B.1\]) shows that \((1-\delta-o(1))\frac{logn}{I(p)}\) noisy comparisons are necessary. These bounds essentially match when \(1/n^{o(1)}\le\delta\le o(1)\). However, for the application of Noisy Sorting, we must have \(\delta=o(1/n)\) on average. In this case, the lower and upper bounds do not match.

Dereniowski, Łukasiewicz, and Uznański \[DLU21\] designed alternative algorithms Noisy Binary Search in various settings. They also considered a more general problem called Graph Search.

We remark that Ben-Or and Hassidim \[BH08\], likely unaware of \[BZ74\], claims an algorithm for solving NoisyBinarySearch(_n_) with error probability \(\delta\) using at most \((1-\delta-o(1))\frac{logn+O(log(1/\delta))}{I(p)}\) noisy comparisons in expectation. However, as pointed out by \[DLU21\], there are potential issues in \[BH08\]’s proof.

By using a similar technique as our lower bound for Noisy Sorting, we are also able to improve the lower bound for Noisy Binary Search for \(\delta=1/n^{\Omega(1)}\).

<sup>3</sup>The original paper is in Russian. See \[WGZW23, Theorem 5\] for an English version.

