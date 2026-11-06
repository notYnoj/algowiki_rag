compilers relied on oblivious sorting which requires \(\Omega(nlogn)\) time either assuming the indivisibility model \[LSX19\] or the Li-Li network coding conjecture \[FHLS19\]; whereas more recent works \[PPRY18,AKL<sup>+</sup>20a\] observed that with with a lot more additional work, we could replace oblivious sorting with the weaker compaction primitive.

Besides Pippenger’s self-routing super-concentrator \[Pip96\], Arora, Leighton, and Maggs \[ALM90\] considered a self-routing _permutation_ network. Their construction does not accomplish sorting. Further, converting their non-blocking network to a permutation circuit would require at least \(\Omega(nlog^2n)\) gates \[bmm\]. Pippenger’s work \[Pip96\] adopted some techniques from the Arora et al. work \[ALM90\].

## 3 Nearly Orderly Segmenter

### 3.1 Notations

**Array and multiset notations.** Whenever we say an _array_, we mean an ordered array. Throughout the paper, we may assume that the array to be sorted has length _n_ that is a power of 2 -- in case not, we can always round it up to the nearest power of 2 by padding \(\infty\) elements, incurring only constant blowup in array length and consuming at most one additional bit in terms of key length.

Given an array _A_, the notation _mset(A_) denotes multiset formed by elements in _A_. Suppose that _A_ and \(A'\) are two arrays, then \(A||A'\) denotes the array formed by concatenating _A_ and \(A'\). For \(m\in\mathbb{N}\), we use the notation \[_m_\]:={1,2_,...,m_}. Suppose that \(1\le s\le t\le|A|\), we use the notation _A_\[_s:t_\] to denote the length-(_t-s_+1) segment of the array _A_ from _s_-th element to the _t_-th element. We define the short-hand notations _A_\[:_t_\]:=_A_\[1:_t_\] and _A_\[_s_:\]:=_A_\[_s_:|_A_\]]. Unless otherwise noted log means log<sub>2</sub>.

**Binary tree notations.** Given a complete binary tree with _t_ levels, the _level_ of a node is the number of edges from the root to the node. For example, the root is at _level_ 0; and the leaves are at _level t_-1.

The _tree distance_ of two nodes in a binary tree is the length of the shortest path between them.

### 3.2 Definitions

**"Misplaced" elements w.r.t. segments.** Let _A_ be an array of length _n_, and let \([s,t]\subseteq[n]\) be a contiguous sub-range of \[_n_\]. The number of _"misplaced"_ elements in the segment _A_\[_s:t_\], denoted err(_A_\[_s:t_\]), is defined as as the number of elements residing in _A_\[_s:t_\], however, if _A_ were to be sorted, ought not to be in _A_\[_s:t_\].<sup>4</sup> More formally,

\(\mathsf{err}(A[s:t])=|mset(A[s:t])-mset(B[s:t])|.\)

where _B_=sorted(_A_) denotes the sorted version of _A_, and recall that _mset(A_\[_s:t_\]) denotes the multiset formed by elements in _A_\[_s:t_\]. As a special case, if _mset(A_\[_s:t_\])=_mset(B_\[_s:t_\]), then the err(_A_\[_s:t_\])=0. (Notice that )

**Nearly orderly segmenter.** We now define \((\eta,p)\)-orderliness and an \((\eta,p)\)-orderly segmenter.

<sup>4</sup>In this section, we abuse "misplaced" and refer to the elements that are in the wrong _segments_ (instead of the wrong _position_ in the remaining of this work).

