## Skip Check.

To adapt to decreasing sequences, the algorithm introduces a decreasing skip check. If both halves are strictly decreasing, the check evaluates if the two decreasing child subarrays seamlessly connect into a larger strictly decreasing run, skipping the merge step and propagating this information up the tree. This ensures that any Case 1 nodes fully contained within a decreasing run bypass the merge, costing zero comparisons. If any of the halves is not decreasing, the algorithm utilizes the standard skip check (\(A[m-1]\le A[m]\)) to evaluate non-decreasing purity instead. Because the flag conditions for executing the two skip check are mutually exclusive, at most 1 comparison is performed, hence the global overhead for skip checks remains at _n_-1 comparisons.

## Directional Merging.

The directional merging logic follows from the elementary variant. However, MergeBw is also invoked when neither the right half is purely decreasing (_b_<sub>2</sub>=`false`) nor the left half is purely non-decreasing (_a_<sub>1</sub>=`true`), utilizing the backwards merge when there are no potential forward merge savings. This leads to additional savings for decreasing runs:

• **Backward Merge:** When the left half is fully contained by a decreasing run that extends into the right half, all run elements in the right half are strictly less than the elements in the left half. In this situation, _a_<sub>2</sub>=`true`, _b_<sub>2</sub>=`false` (as it contains a boundary), and _a_<sub>2</sub>=`true` implies _a_<sub>1</sub>=`false` when |_L|\>_1 (|_L_|=1 handled in Appendix A.1), triggering MergeBw. The backwards merge then exhausts the left half before selecting any run elements from the right half. These remaining run elements are directly appended using 0 comparisons.<tbc>

• **Forward Merge:** Otherwise, when the right half is a decreasing sub-run _b_<sub>2</sub>=`true` which implies _b_<sub>1</sub>=`false` as |_R|\>_1 (when \(r-\ell\ge 3\), which holds for all non base cases), MergeFw is called. If the run begins in the left half, this gives a symmetrical saving where the right half is exhausted first, and the run elements in the left half are appended with no comparisons.

With the mechanics of directional mergesort<sup>+1</sup> established, we now prove that it achieves the same optimal comparison bounds for both non-decreasing and decreasing sequences.

**Lemma 14** (Merge Comparisons for Non-Decreasing Runs)**.** _For a non-decreasing run of length r, the total number of merge comparisons charged to its elements across all levels of the merging tree in directional mergesort_<sup>+1</sup> _is bounded by r_lg(_n/r_)+2_r._

_Proof._ Within any purely non-decreasing run, \(A[i]\le A[i+1]\) holds for all pairs of elements from the run. Hence, any size 2 base case fully contained by the run identifies the non-decreasing order and returns _x_<sub>2</sub>=0, resulting in unchanged skip check and directional merging savings upwards the merging tree (full details in Appendix A.1).

For the two elements at the ends of the run, they may be attributed as decreasing together with adjacent non-run elements if they are in Case 2 nodes. Since such a node contains non-run elements, _x_<sub>1</sub>=0 is correctly identified and the directional merge remains valid. Moreover, the worst-case accounting of Lemma 5 and Lemma 6 already assumes merges over mixed regions are never fortuitously skipped (i.e. elements from different runs happening to be in the correct order resulting in a skip), so the altered execution of the skip check does not affect the bound. Hence, the bound in Lemma 7 is retained.





(a) Backward Merge (_a_<sub>1</sub>=`false`_,b_<sub>2</sub>=`false`)

(b) Forward Merge (_b_1=`false`_,b_<sub>2</sub>=`true`)

Figure 2: Subarray configurations exhibiting directional merge savings on decreasing runs.

