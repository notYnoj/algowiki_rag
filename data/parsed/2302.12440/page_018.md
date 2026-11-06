**Line 5.** By Chernoff bound, \(|S|\le 100n/logn\) with probability at least 1-_n_<sup>-2</sup>. In this case, SafeSimpleSort uses _O_(|_S_|log|_S_|)=_O(n_) random bits. If _S\>_100_n/logn_, SafeSimpleSort uses _O(n_log_n_) random bits, which contribute at most \(O(nlogn\cdot n^{-2})\) to the overall expectation. Thus, Line 5 uses _O(n_) random bits in expectation.

**Line 7, Line 17, Line 34.** For each of the first _n_<sup>2/3</sup> outputted random bits, we use Lemma 14 to construct a pairwise independent hash family of size _n_ using _O_(log_n_) fresh random bits. The total number of fresh random bits needed is _O(n_<sup>2/3</sup>log_n_).

Now we are ready to prove Theorem 15.

_Proof of Theorem 15._ Consider the following algorithm, which we call SafeNoisySort:

• Run NoisySort. Stop immediately if we are about to use _m_ queries, for some _m_ to be chosen later.<tbc>

• If we successfully completed NoisySort, then output the sorted array; otherwise, output any permutation.

By Lemma 23, we can choose \(m=(1+o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\) so that with proba bility 1-_o_(1), the NoisySort call completes successfully. By Lemma 21, with probability 1-_o_(1), the NoisySort call is correct. By union bound, SafeNoisySort has error probability _o_(1) and it always takes at most _m_ queries. By Lemma 24, number of random bits used is _O(n_) in expectation.

## 3.1 Trading Queries for Random Bits

In this section, we show how to use the randomized algorithm to construct a deterministic one.

**Theorem 1** (Noisy Sorting Upper Bound)**.** _There exists a deterministic algorithm for_ NoisySorting(_n_) _with error probability o_(1) _which always uses at most_

\((1+o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\)

_noisy comparisons._

_Proof._ In our model, it is possible to generate unbiased random bits using noisy comparisons. Take two arbitrary elements _x,y_, and call NoisyComparison(_x,y_) twice. If the two returned values are different, we use the result of the first returned value as our random bit; otherwise, we repeat. Clearly, this procedure generates an unbiased random bit. The probability that this procedure successfully return a random bit after each two calls of NoisyComparison is 2_p_(1-_p_), so the expected number of noisy comparisons needed to generate each random bit is \(O(\frac{1}{2p(1-p)})=O(1)\). Note that this procedure is deterministic.

Algorithm 3 uses _O(n_) random bits in expectation, so we can use the above procedure to generate random bits, and the expected number of queries needed is _O(n_). We can halt the algorithm if the number of queries used this way exceeds _O(n_loglog_n_), which only incurs an additional _o_(1) error probability.

