where we used the fact that _X<sub>t</sub>_ is always an integer multiple of \(log\frac{1-p}{p}\) and hence \(X_\tau\le\left\lceil\frac{log\frac{1-\delta}{\delta}}{log\frac{1-p}{p}}\right\rceil\) . \(log\frac{1-p}{p}\) .

Thus, the algorithm stops within \(\frac{1}{1-2p}\left\lceil\frac{log\frac{1-\delta}{\delta}}{log\frac{1-p}{p}}\right\rceil\) queries in expectation.

Similarly, if the ground truth is _x\>y_, the algorithm stops within the same expected number of queries. This finishes the proof.

For simplicity, we use \(f_p(\delta)\) to denote \(\frac{1}{1-2p}\left\lceil\frac{log\frac{1-\delta}{\delta}}{log\frac{1-p}{p}}\right\rceil\) for \(0<p<\frac{1}{2}\) and \(\delta>0\), which, by Lemma 13, upper bounds the expected number of comparisons needed by Algorithm 1 to compare two elements with error probability \(\le\delta\). When clear from the context, we drop the subscript _p_.

### 2.3 Pairwise Independent Hashing

During our algorithm, we sometimes run into the following situation: we need to run a certain algorithm _n_ times, where each instance uses _m=n<sup>c</sup>_ random bits for some 0_\<c\<_1. We can only afford _o(n_log_n_) fresh random bits in total (for derandomization purpose), so the instances need to share randomness in some way. On the other hand, we want randomness between any two instances to be independent of each other, in order for concentration bounds to hold. Therefore we need the following standard result on pairwise independent hashing.

**Lemma 14** (\[CW77\])**.** _There exists a pairwise independent hash family of size_ 2_<sup>k</sup>_-1 _using k fresh random bits._

By using _m_ fully independent copies of pairwise independent hash families, we can achieve pairwise independence between instances using _O(m_log_n_) fresh random bits.

## 3 Noisy Sorting Algorithm

In this section, we will present our algorithm for noisy sorting and prove Theorem 1. We will first present the following randomized version of our algorithm, and then convert it to a deterministic one in Section 3.1.

**Theorem 15.** _There exists a randomized algorithm for_ NoisySorting(_n_) _with error probability o_(1) _which always uses at most_

\((1+o(1))\left(\frac{1}{I(p)}+\frac{1}{(1-2p)log\frac{1-p}{p}}\right)nlogn\)

_noisy comparisons, and uses O(n_) _random bits in expectation._

We start with a subroutine that sorts a list with a small number of inversion pairs.

**Lemma 16.** _Fix any parameter_ \(\sigma\in(0,1)\) _which can depend on n. Given a list of n elements with t inversion pairs, there exists a deterministic algorithm using noisy comparisons that sorts these n elements with error probability_ \(\le(n-1+t)\sigma\) _using_ \((n-1+t)f(\sigma)+(n-1+t)\sigma n^2f(\sigma)\) _noisy queries in expectation. The algorithm does not have to know t in advance._

