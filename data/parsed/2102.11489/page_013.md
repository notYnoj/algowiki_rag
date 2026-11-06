**Definition 1** (\((\eta,p)\)-orderly)**.** Let _m_ and _p_ be positive integers, and suppose that _n=mp_. Write an array _A_ of length _n_ as the concatenation of _p_ equal-sized segments: _A=A_<sub>1</sub>||_A_<sub>2</sub>||_..._||_A<sub>p</sub>_. We say that _A_ is \((\eta,p)\)-orderly iff for each \(i\in[p]\), \(\text{err}(A_i)\le\eta\cdot|A_i|\).

**Definition 2** (\((\eta,p)\)-orderly segmenter)**.** Let _n_:=_mp_. An \((\eta,p)\)-nearly orderly segmenter (for _n_) is a circuit that takes an array _A_ of length _n_, and outputs a permutation of _A_ which is \((\eta,p)\)-orderly.

## 3.3 Construction

We rely on ideas from the AKS sorting network \[AKS83\] to construct a nearly orderly segmenter.

At a very high level, the AKS algorithm proceeds in _O_(log_n_) cycles to sort a length-_n_ input array. During each cycle _t_,

1. The algorithm partitions the current array into a number of disjoint _intervals_ which are not necessarily equally sized. Henceforth the term _interval_ refers to a contiguous subarray. The number of intervals is geometrically growing with each cycle.<tbc>

2. The algorithm then partitions the intervals into groups, and each group contains a disjoint (but not necessarily contiguous) subset of the intervals. It then sorts each group and writes the sorted array back in place. Further, all the groups are sorted in parallel. The above partitioning and sorting procedure is repeated three times (and each time the partitioning may be different), and then the algorithm enters the next cycle.

At the end of log_n_ cycles, the input array is guaranteed to be sorted.

It turns out if we repeat the AKS algorithm for 6_k\<_log_n_ cycles and stop, the resulting array will satisfy (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderliness. For completeness, below we describe the algorithm where we essentially perform AKS for 6_k\<_log_n_ cycles, we then rely on a technical lemma proven in the AKS paper \[AKS83\] to prove that the resulting array is indeed (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly.

### 3.3.1 Preliminaries

Recall that we would like to partition the current array into a number of intervals in each AKS cycle _t_. To understand how the intervals a defined, we will first define a helper data structure called a _t_-AKS-tree.

even cherry
1, 22
odd cherry
2, 11
12,21
3, 6
7, 10
13,16
17,20
4
5
8
9
14
15
18
19

**Figure 2:** _t_-AKS-tree for _t_=3.

