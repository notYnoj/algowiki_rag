### Concurrent work of Koucký and Král [KK21].

<sup>2</sup> In the independent and concurrent work, Koucký and Král construct a sorting circuit of size \(O(nk(w+k)\cdot(1+log^*n-log^*(w+k)))\) and depth _O_(log<sup>3</sup>_n_) for \(k\le(logn)/11\) bits. Compared to our result, their circuit depth is still polylogarithmic, since they directly adopt the two-parameter recursion trick by Lin et al. [LSX19] to upgrade from 1-bit sorting to _k_-bit sorting. As mentioned, this framework inherently suffers from at least poly-logarithmic depth. We got around this issue by proposing a brand new framework for this 1-bit to _k_-bit upgrade. On the other hand, Koucký and Král tightened the polylog<sup>∗</sup> factor to log<sup>∗</sup>. In addition, Koucký and Král consider another variant of sorting circuit that sorts _n_ integers each of _k_ bits _without payload_, commonly referred to as _integer sorting_. For integer sorting, they claim circuit size _O(nk_<sup>2</sup>) and depth _O_(log_n+k_log_k_). Our paper mainly focuses on sorting with payload.

## 2 Technical Roadmap

We give an informal technical overview of our ideas in this section.

### 2.1 Sorting Short Keys on an Oblivious PRAM (a.k.a. 1-bit to _k_-bit Upgrade)

As an intermediate stepping stone, we first consider how to sort _k_-bit keys on an Oblivious PRAM in \(O(n)\cdot min(k,logn)\) total work and _O_(log_n_) depth. Without loss of generality, we assume that \(k<\frac{1}{8}logn\) in the following exposition where _n_ denotes the length of the array to be sorted; since if \(k\ge\frac{1}{8}logn\), we can simply run AKS [AKS83] to sort the array. We also assume that _n_ is a power of 2; if not, we can pad it with elements with \(\infty\) keys to the next power of 2. We assume that each element can be stored in _O_(1) memory words.

In the Oblivious PRAM model, Asharov et al. [AKL<sup>+</sup>20b] showed how to get an optimal compaction algorithm that is linear in total work and logarithmic in depth (even though the optimal counterpart in the circuit model is not known prior to our work). Our goal is to upgrade the 1-bit sorting (i.e., compaction) to _k_-bit sorting. As mentioned, we cannot build upon existing approaches for this upgrade since they incur polylogarithmic depth [LSX19,ALS21]. We therefore suggest a brand new approach.

#### 2.1.1 New Abstraction: Nearly Orderly Segmenter

We propose a new abstraction called an \((\eta,p)\)_-orderly segmenter_, where \(\eta\in(0,1)\) indicates how sorted the resulting array is, and _p_ denotes the number of segments. An array _A_:=_A_<sub>1</sub>||_A_<sub>2</sub>||_..._||_A<sub>p</sub>_, represented as the concatenation of _p_ equally sized partitions denoted _A_<sub>1</sub>_,A_<sub>2</sub>_,...,A<sub>p</sub>_, is said to be \((\eta,p)\)-orderly iff in each of the _p_ segments, at most \(\eta\) fraction of the elements belong to the _wrong segment_ if the array were to be fully sorted. An \((\eta,p)\)-orderly segmenter receives an input array whose length is divisible by _p_, and outputs a permutation of the input array that is \((\eta,p)\)-orderly.

We then show how to construct a deterministic, oblivious (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly segmenter that requires _O(nk_) total work and _O(k_) depth. The construction involves partially executing the AKS algorithm [AKS83]. Recall that the full AKS algorithm would execute for a total of log_n_ cycles. In each cycle, the following is repeated for _O_(1) number of times: partition the array into disjoint partitions where each partition may not be a contiguous region in the original array, and apply an<tbc>

<sup>2</sup>This manuscript was written in 2020, and then we posted it in February 20201 (arXiv:2102.11489), four days after Koucký and Král.

