<tbc>BR19\], together with our algorithm for small edit distance computation with preprocessing. Even more surprisingly, by combining ideas from our algorithms with preprocessing, we design the fastest \(3+\epsilon\) approximation algorithm for edit distance without any preprocessing.

### 1.1 Open problems

We now describe a couple of exciting directions for future work

#### Preprocess one string:

An appealing variant of our preprocessing model is when only one of the string is preprocessed. (This is motivated by a scenario where a single reference string is compared to many strings that are only used once.) For sublinear algorithms, we are able to get some improvement over state of the art, but the \(\Omega(n/k)\) lower bound from communication complexity continues to hold here. With subquadratic algorithms on the other hand, our preprocessing algorithm has a natural variant that could be applied to only one string. But so far we are unable to use it to obtain significant improvement over no-preprocessing approximate edit distance algorithms.

**Open Question 1.** What is the complexity of approximate edit distance after preprocessing one of the strings?

#### Approximate edit distance in sub-linear time

A natural question is whether we can combine ideas from our exact \(\tilde{O}(k^2)\)-time algorithm for small edit distance together with the _O(n_<sup>1.5+_o_(1)</sup>)- time approximation algorithm for general edit distance to approximate small edit distance in truly sub-_k_<sup>2</sup> time. Alternatively, it may be possible to show unconditional lower bounds (e.g. via communication complexity) for approximate edit distance in this regime.

**Open Question 2.** What is the complexity of approximate edit distance with preprocessing when \(k\checkmark n\)?

#### Beyond string alignment?

As discussed before, preprocessing is particularly appealing when it runs in near-linear time and the queries run in sub-linear time. In the context of string alignment, there is a very natural notion of preprocessing where each string is preprocessed separately. An interesting, open-ended direction is to identify other problems in sub-linear algorithms where one can define preprocessing models that are both natural and allow for significant improvements.

**Open Question 3.** Define preprocessing models for other problems in sub-linear algorithms that are both natural and allow for significant improvements.

## 2 Small Ulam distance

In this section, we prove Theorem 1 where with preprocessing we can compute ulam distance (bounded by _k_) exactly in time _O(k_log(_n_)).

**Theorem 1** (Permutation-LCS)**.** _Given two permutations X,Y of_ {1_,...,n_} _with a common string of length at least n-k, we can compute their LCS exactly with O(n_log(_n_))_-time preprocessing and O(k_log(_n_))_-time joint processing._

**Claim 2** (Structure of close permutations)**.** _If two permutations X,Y of_ {1_,...,n_} _share a common string of length at least n-k, then they can be partitioned into O(k_) _contiguous blocks such that each block of Y has an identical block in Y._

