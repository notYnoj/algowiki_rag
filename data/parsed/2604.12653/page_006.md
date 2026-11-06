## 2.1 Existing Machinery for Sorting under Partial Information

The interval lemma is a powerful tool for analysing fast algorithms that use adaptive data structures. It was originally introduced in \[4\] and has been extensively used \[4,13,14,19,30\]. Here, we consider a lopsided version where the number of intervals may be different from the range of the intervals. For example, for the analysis in Section 3, it is convenient to consider _n_ intervals in \[1,2_n_\].

**Lemma 6** (A generalization of Lemma 3.2 in \[4\])**.** _Let_ \(\{[a_i,b_i]\}_{i=1}^k\) _be a family of k subintervals of_ \[0_,m_\] _that each have size at least_ 1_. Let Z be the set of linear orders realizable by real numbers_ \(z_i\in[a_i,b_i]\)_. Then_ \(\sum_{i\in[k]}log(b_i-a_i)\in O(klog(\frac{em}{k})+log|Z|)\).

_Proof._ Many existing proofs of Lemma 3.2 in \[4\] can be adapted to work in the lopsided setting. For example, we tweak the proof of \[14\]: For each _i_ between 1 and _k_ inclusive, choose a real number _z<sub>i</sub>_ uniformly at random from the real interval \[0_,m_\], independently for each _i_. With probability 1, the _z<sub>i</sub>_ are distinct. Let _L_ be the permutation of \[_k_\] obtained by sorting \[_k_\] by _z<sub>i</sub>_. Each possible permutation is equally likely. If each \(z_i\in[a_i,b_i]\) then _L_ is in _Z_. The probability of this happening is \(\prod_{i=1}^k\frac{b_i-a_i}{m}\) . It follows that \(|Z|\ge k!\cdot\prod_{i=1}^k\frac{b_i-a_i}{m}\) . Taking logarithms gives \(log|Z|\ge\sum_{i=1}^klog(b_i-a_i)+logk!-klogm\). By Stirling’s approximation of the factorial, \(logk!\ge klogk-kloge\). Thus,

\(\sum_{i=1}^klog(b_i-a_i)\le log|Z|+klogm-logk!\le log|Z|+klog\left(\frac{em}{k}\right).\square\)

In the introduction, we present two algorithms for sorting under partial information with different running times: Theorem 4 and Theorem 5. The main difference between these is the additional _O(n_) term in the sorting time of Theorem 4. This term is only relevant if \(loge(G)\in o(n)\), and there is existing machinery \[4,19,30\] for dealing with this case: Roughly speaking, this can only happen if there is a very long path in _G_. We can find this path during the preprocessing phase, and not waste any comparisons on it during the sorting phase. Formally:

**Lemma 7** (Lemma 1 in \[30\] + Lemma 8 of \[19\])**.** _Let P be a longest path in G. Then,_ \(n-|P|\in O(loge(G))\)_. Moreover, after performing O(n+m_) _preprocessing on G, we can, given the sorted order of X-P, sort all of X in O_(log_e(G_)) _time during the sorting phase._

In Section 4 we use this lemma to derive Theorem 5 from Theorem 4.

## 2.2 Existing Results on Adaptive Data Structures

In this paper, we mainly focus on adaptive heap data structures. However, there is a standard way of using a binary search tree as a heap: sort the items by the order in which they were inserted, and maintain the subtree minimum at each node. Thus, we will also mention some results on binary search trees, as these results have implications for adaptive heaps.

### Existing notions of unified bounds.

Unified bounds were first defined for binary search trees. For splay trees, Sleator and Tarjan \[26\] use the term "unified bound" for the minimum of three other bounds, the so-called static optimality, static finger, and working set bound. However, Elmasry, Farzan and Iacono \[10\] show that this "unified bound" is equivalent to the working set bound. Hence, this definition has been obsoleted.

Iacono \[18\] introduces the unified bound for binary search trees, which is strictly stronger than the working set bound for binary search trees. He conjectures that the splay tree also satisfies this<tbc>

