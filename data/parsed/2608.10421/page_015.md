**Theorem 21.** _Directional Mergesort_<sup>+2</sup> _sorts an array of size n with run-based entropy H (defined for exclusively non-decreasing runs) using no more than nH_+3_n comparisons and_ 1.5_nH_+5_n element moves. Excluding the merge buffer of size_ \(\lceil n/2\rceil\)_, the algorithm uses O_(1) _auxiliary words._

_Proof._ The optimized version processes all subproblems in postorder identically to the base variant, maintaining the correct return flags, resulting in identical behavior to the base variant (making the same comparisons and moves). Hence, the comparison and move bounds in Corollary 12 is retained.

However, the total auxiliary space usage, excluding the merge buffers, is reduced to _O_(1) words: the algorithm utilizes a fixed number of single word variables alongside the two bit stacks A and D. Because the height of the merge tree is bounded by \(\lceil lgn\rceil\), D and A contain at most \(\lceil lgn\rceil\) single-bit entries. According to the standard assumption that words are at least l_gn_ bits wide, each bit stack can fit within a single word.

The arithmetic operations for managing the tree traversal is _O(n_). This is because an iterative postorder traversal in a tree of 2_n_-1 nodes calls the move primitives no more than 2((2_n_-1)-1) times, as each edge is walked at most twice. Each move primitive makes _O_(1) arithmetic operations, totaling _O(n_) arithmetic operations across the algorithm’s execution. Consequently, the overall time complexity of the algorithm remains bounded by _O(nH+n_).

### 4.3 Summary

**Corollary 22.** _Directional Mergesort_<sup>++</sup> _sorts an array of size n with run-based entropy H (defined for both non-decreasing and decreasing runs) using no more than nH_+3_n comparisons and_ 1.5_nH_+6.5_n moves. Excluding the merge buffer of size_ \(\lceil n/2\rceil\)_, the algorithm uses O_(1) _auxiliary words._

_Proof._ By a parallel application of stack space reduction optimization to Directional Mergesort<sup>+1</sup>, the resulting algorithm operating within _O_(1) words inherits the bounds in Theorem 17 and Theorem 20. The bit stack A and variable _b_ is expanded to accommodate two-bit entries, requiring twice the space, but this does not violate _O_(1) word space constraints.

**Remark 23.** Whilst Corollary 22 establishes an upper bound of _nH_+3_n_ comparisons for simplicity, a tighter analysis of the right boundary accounting for the size 2 base case yields a stronger bound of _nH_+3_n-r_<sub>#</sub>. The full proof is deferred to Appendix A.2.

## 5 Concluding Remarks

In this paper, we introduced directional mergesort, a minimalistic adaptive sorting algorithm that matches the optimal _nH_+3_n_ comparisons bound set by state-of-the-art natural mergesorts Powersort and Peeksort. Unlike predecessors that rely on dynamic run-scanning and variable merge tree geometries, our approach operates strictly over static index partitions using localized skip checks and dynamic merge-direction choices. This ensures the merging tree structure remains completely static, simplifying the underlying element-charging analysis across tree levels.

Furthermore, directional mergesort<sup>++</sup> then leverages this data oblivious merge tree geometry to compress both child-size differences and purity return flags into single word bit stacks, reducing auxiliary space usage (aside from the merge buffer) to _O_(1) words. This demonstrates that optimally run-adaptive sorting does not require _O_(l_n_) words for boundary tracking or intrusion into the data itself to simulate this space. Furthermore, by tracking non-decreasing and strictly decreasing runs using two flags, the algorithm adapts to both orientations of runs without incurring any additional overhead in comparisons, matching the decreasing run adaptivity of natural mergesorts.

