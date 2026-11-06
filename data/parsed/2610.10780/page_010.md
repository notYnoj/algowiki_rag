requires a compact representation of the candidate distances themselves. This section develops such a representation. The resulting theorem is the main structural result of the paper and constitutes the principal new ingredient that enables the deterministic _O(n_<sup>4/3</sup>)-time algorithm.

Given an interval _I_, our goal is to represent the distances of \(S\cap I\) by a collection of bicliques. Ideally, we would like to represent all distances of \(S\cap I\). However, it is unlikely this can be achieved in time _o(n_<sup>4/3</sup>). Instead, our strategy is to represent only a constant fraction of the distances in \(S\cap I\), which is sufficient for our prune-and-search distance selection algorithm as will be shown in Section 5.

This idea is motivated by Lemma 1. The lemma already produces a compact representation of most distance pairs while leaving a controlled collection of unresolved pairs. However, the resulting algorithm is not efficient enough for our purposes. Our new algorithm goes one step further: among the certified pairs, it records only a constant fraction of them. This additional flexibility allows us to obtain a substantially faster representation algorithm.

Like the approximate counting theorem, the distance representation theorem provides a trade-off between running time and representation error. Roughly speaking, the more unresolved pairs we allow, the more efficient the algorithm becomes. For example, if no unresolved pairs are allowed, our algorithm runs in _O(n_<sup>4/3</sup>) time. By comparison, the technique of Wang and Zhao \[28, Theorem 1\] requires \(n^{4/3}\cdot 2^{O(log^*n)}\) time for the same task.<sup>1</sup>

The following theorem summarizes the main result of this section.

**Theorem 3** (Distance Representation)**.** _Given an interval I, for every integer i with_ \(1\le i\le O(log^*n)\) _such that_

\(|S\cap I|\ge c_1\cdot n^{4/3}(log^{(i)}n)^4\)

_for a sufficiently large constant c_<sub>1</sub>_\>_0_, one can compute a collection_ \(\Gamma=\{A_t\times B_t\}\) _of edge-disjoint bicliques such that:_

1. _every pair recorded by a biclique of_ \(\Gamma\) _has distance in I;_<tbc>

2. \(\sum_t|A_t||B_t|\ge 0.4\cdot|S\cap I|\);<tbc>

_3._ \(\sum_t(|A_t|+|B_t|)\) _is O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) _for i_=1,2_, and O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) _for_ \(i\ge 3\).

_The construction time is O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) _for i_=1,2_, and O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) _for_ \(i\ge 3\).

### Remark.

The second statement implies that the bicliques of \(\Gamma\) record at least forty percent of the distances in \(S\cap I\). Although the theorem does not explicitly mention unresolved pairs, they are an essential part of the construction.

In the remainder of this section, we prove Theorem 3. The proof follows the same high-level framework as the approximate counting algorithm. However, there is a crucial difference. Theorem 1 only requires counting target distances, whereas here we must organize them into bicliques. Consequently, the representation problem is substantially more challenging.

We begin with the easier cases _i_=1,2, where the algorithm follows directly from Lemma 1. The case \(i\ge 3\) requires new ideas and constitutes the main technical contribution of this section.

## 4.1 The cases _i_=1,2

For _i_=1,2, the distance representation theorem follows directly from the recursive construction underlying Theorem 1.

<sup>1</sup>One may wonder whether the \(\Gamma\)-framework \[10\] can be used to remove the 2<sup>_O_(log<sup>∗</sup>_n_)</sup> factor. It is not clear to us whether this is possible. See the discussion in \[28\] about this challenge following Theorem 1.

