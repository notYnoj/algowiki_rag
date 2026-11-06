**Theorem 8** (Total Comparison Complexity)**.** _An array of size n containing r_<sub>#</sub> _non-decreasing runs of lengths r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> _is sorted in at most nH_+3_n comparisons, where the run-based entropy_ \(H=\sum_{i=1}^{r_\#}(r_i/n)lg\left(n/r_i\right)\).

_Proof._ The total number of comparisons from merging is derived by summing the per run cost (Lemma 7) across all _r_<sub>#</sub> sorted runs (with lengths _r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_r_<sub>#</sub></sub> where \(\sum r_i=n\)):<tbc>

\(\left(\sum_{i=1}^{r_\#}r_ilg(n/r_i)+2r_i\right)=\left(\sum_{i=1}^{r_\#}r_ilg(n/r_i)\right)+2n=n\left(\sum_{i=1}^{r_\#}(r_i/n)lg(n/r_i)\right)+2n=nH+2n\)

<tbc>Finally, we reintroduce the cost of skip checks from Lemma 4:

\(nH+2n+(n-1)=nH+3n-1\le nH+3n\)

## 3.2 Data Movement Analysis

To analyze the data movement complexity, we apply a similar structural framework based on the merging tree established in Section 3.1.

The algorithm utilizes a half-buffered merge. In an internal node _v_, the algorithm first copies either the left child _L_ or right child _R_ into the buffer, moving at most \(max(|L|,|R|)\le\lceil|v|/2\rceil\) elements by Fact 2. It then uses at most _m_ moves to form the merged result in the original array. For \(|v|\in\mathbb{Z}\), total moves are bounded by:

\(|v|+\lceil|v|/2\rceil\le|v|+|v|/2+1/2=1.5|v|+1/2\)

Because the merging tree contains exactly _n_-1 internal nodes (see Lemma 4), the +1/2 overhead term incurred by each merge at every internal node contributes an absolute maximum of (_n_-1)/2 moves across the entire execution. We globally separate this _O(n_) overhead, leaving an aggregate move pool of exactly 1.5|_v_| for each internal node _v_.

### Amortized Accounting Method:

We distribute the 1.5|_v_| move pool evenly among the |_v_| elements in _v_, charging exactly 1.5 moves per element. The key difference from the approach for comparisons is that this 1.5 charge is a uniform mathematical abstraction over the node’s capacity rather than a physical count of whether an element was copied to the buffer or written as a residual (whereas Section 3.1 uses the actual cost of selecting the element in the merge). Hence, local deductions for uncopied residuals cannot be applied to this charge. However, if a merge is skipped entirely in Case 1, then 0 moves are made, hence the per element cost is also 0. Similarly, Case 4 nodes contain no elements from the run, thus the charge to the run is also 0.

Equipped with this charging rate, we bound the aggregate move cost for a run of length _r_, utilizing the same two regime partitioning established in Section 3.1. However, to tighten the move complexity bound, we shift the regime threshold to _t_+1.

**Lemma 9** (Moves at Upper Levels)**.** _For a non-decreasing run of length r, the total move charge incurred at upper levels (h\<t_+1_) is bounded by_ 1.5_r(t_+1).

_Proof._ Paralleling Lemma 5, each of the _r_ elements in the run belongs to exactly one node per level and is charged 1.5 moves. Across all _t_+1 levels, the total move charge is 1.5_r(t_+1).

**Lemma 10** (Moves at Lower Levels)**.** _For a non-decreasing run of length r, the total move charge incurred at lower levels (_\(h\ge t+1\)_) is bounded by_ 3(_n/_2_<sup>t</sup>)._

