it can also be used to create an _in-place_ version of _Mergesort_. Although the parallel _Merge_ algorithm and our _in-place Merge_ algorithm use this _co-ranking_, they use it for a completely different purpose.

The general idea of _co-ranking_ is visualized in Figure 2. As input, it takes two presorted arrays _A_ and _B_, as well as an arbitrary rank (index) _i_. We assume array _C_ to be the result of merging both input arrays. When _A_ contains _n<sub>A</sub>_ elements and _B_ contains _n<sub>B</sub>_ elements, this array _C_ would need to hold all these elements, i.e., _n=n<sub>A</sub>+n<sub>B</sub>_. If _i_ is a valid rank in _C_ (i.e., \(0\le i\le n\)), the _co-ranking_ functionality will determine the corresponding ranks of _i_ in the input arrays _A_ and _B_, respectively. Astonishingly, these _co-ranks j_ and _k_ are always unique, and they can be determined much faster (i.e., O(log_n_) vs. O(_n_) time) **without** actually merging the input arrays and hence without the need for the result array _C_. This is accomplished in a binary search fashion while maintaining the invariant _j+k=i_. It converges lower and upper bounds in both input arrays, where \(j_\mathrm{low}\le j\) and \(k_\mathrm{low}\le k\). The algorithm terminates when both lemma conditions (see Lemma 2.1 in [12]) are fulfilled, and thus the unique co-ranks _j_ and _k_ are found.

Previously published implementations of the _co-ranking_ functionality add some complexity caused by the nature of distributed memory systems. However, since we are only interested in a sequential implementation in this work, a simpler implementation of the _co-ranking_ functionality is possible and presented as pseudocode<sup>1</sup> in Algorithm 2. The correctness<sup>2</sup> of Algorithm 2, the two referred lemma conditions, and its run-time analysis are already proven and explained in detail in [12] and thus omitted here for brevity.

As a side note to the introducing sentences regarding the commonly known median selection, it can be revealed that the problem of selecting even an arbitrary element at position _i_ (for \(0\le i<n\)) for two sorted arrays can indeed be solved efficiently in logarithmic time. This can be achieved easily by employing _co-ranking_ for this _i_ and then returning either the minimum of _A[j_] and _B[k_] if both exist or the existing element of these. We leave

<sup>1</sup> Contrary to earlier representations of this algorithm in [11] and [12], we replace here the **smaller** / **larger than** signs (i.e., \</ \>) with **precedes** / **succeeds** symbols (i.e., \</ \>), respectively, to depict more clearly, in contrast to mere range checks, where actual element comparisons happen. <sup>2</sup> Note that the && in the **if** / **else if** statements denotes a "conditional and" as in the **C/C++** language, and means that the condition on the right is only evaluated if the condition on the left evaluates to **true** (a.k.a. "short-circuiting operator").

0 j
NA 0
k NB A
B co-ranking C
0 i
n

**Figure 2** Co-ranking idea for inputs _A_, _B_ and _i_ with results _j_ and _k_

