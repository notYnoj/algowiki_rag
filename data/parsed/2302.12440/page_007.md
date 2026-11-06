<tbc>algorithm \(\mathcal{A}'\). This way, to the view of the algorithm, the elements are ordered by (_a<sub>i</sub>,i_). It is easy to see that \(\mathcal{A}'\) has the same distribution of number of queries, and error probability is no larger than error probability of A. Thus, we get an algorithm which works for the case where elements are not necessarily distinct.

Similarly, by our definition of the Noisy Binary Search Problem, we can WLOG assume that all elements \((a_i)_{i\in[n]}\) and _x_ are distinct.

## 2.2 Known and Folklore Algorithms

**Theorem 10** (\[DLU21, Corollary 1.6\])**.** _There exists a randomized algorithm for_ NoisyBinarySearch(_n_) _with error probability at most_ \(\delta\) _using_

\((1+o(1))\left(\frac{logn+O(log(1/\delta))}{I(p)}\right)\)

_noisy comparisons in expectation, and using O_(log_n_) _random bits always._

**Remark 11.** \[DLU21\] stated their problem as finding an element in a sorted array, but their algorithm can also find the predecessor. The only place their algorithm uses randomness is to shift the initial array randomly, which requires _O_(log_n_) random bits (as we can WLOG assume _n_ is a power of two in NoisyBinarySearch(_n_), it always takes _O_(log_n_) random bits to sample a random shift, instead of _O_(log_n_) random bits in expectation).

We could also use the noisy binary search algorithm in \[BZ74\] (see also \[WGZW23, Theorem 5\]), which achieves a slightly better bound on the number of noisy comparisons. However, the number of random bits used in Burnashev-Zigangirov’s algorithm is _O_(log_n_) in expectation, not always. This would make our control of number of random bits used slightly more complicated.

**Corollary 12.** _There exists a randomized algorithm for_ NoisySorting(_n_) _with failure probability_ \(\delta\) _using_ \(O(nlog(n/\delta))\) _noisy comparisons in expectation, and using O(n_log_n_) _random bits always._

_Proof._ The algorithm keeps a sorted array of the first _i_ elements for _i_ from 1 to _n_. Each time a new element needs to be inserted, the algorithm uses Theorem 10 to find its correct position, with error probability \(\delta/n\). By union bound, the overall error probability is bounded by \(\delta/n\cdot n=\delta\), the expected number of queries is \(n\cdot(1+o(1))\left(\frac{logn+log(n/\delta)}{I(p)}\right)=O(\frac{nlog(n/\delta)}{I(p)})\), and the number of random bits used is _O(n_log_n_).

We show how to use repeated queries to boost the correctness probability of pairwise comparisons. This is a folklore result, but we present a full proof here for completeness.

**Lemma 13.** _There exists a deterministic algorithm which compares two (unequal) elements using noisy comparisons with error probability_ \(\le\delta\) _using_

\(\frac{1}{1-2p}\left[\frac{log\frac{1-\delta}{\delta}}{log\frac{1-p}{p}}\right]=(1+o_{1/\delta}(1))\frac{log(1/\delta)}{(1-2p)log((1-p)/p)}\)

_noisy queries in expectation._

