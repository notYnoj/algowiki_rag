## 2 Directional Mergesort

In this section, we will focus upon the elementary variant of directional mergesort. We derive DirectionalMergesort from standard top-down mergesort by making two simple adjustments: incorporating a standard skip check, and dynamically selecting the merge direction based on subarray pre-sortedness. Notably, these adjustments do not affect the boundaries of recursive calls.

**Algorithm 1** Directional Mergesort

function Sort\((A[],\ell,r)\triangleright\) _Processing Subarray_ \(A[\ell..r)\)<br>
   if \(r-\ell<2\) **then return true**<br>
   \(m\leftarrow\lfloor(\ell+r)/2\rfloor\)<br>
   \(a\leftarrow\text{Sort}(A,\ell,m)\)<br>
   \(b\leftarrow\text{Sort}(A,m,r)\)<br>
   if \(A[m-1]\le A[m]\) **then return** \(a\wedge b\triangleright\) _Skip Check_<br>
   if b then MergeBw\((A,\ell,m,r)\triangleright\) _Directional Merging_<br>
   else MergeFw\((A,\ell,m,r)\)<br>
   return false

The return value indicates whether the processed subarray is _pure_ (i.e., entirely pre-sorted). Hence, base cases return `true`, whereas any subarray requiring an explicit merge returns `false`.

### Skip Check.

Before executing a merge, the algorithm evaluates \(A[m-1]\le A[m]\). If satisfied, the adjacent subarrays are already in sorted order. The algorithm skips the merge step entirely and returns \(a\wedge b\), propagating structural purity up the call tree iff both children were pure.

### Directional Merging.

When an active merge is required, the algorithm inspects the purity flag _b_ of the right child _A_\[_m..r_\] to decide the direction of the merge.

• **Backward Merge (**_b_=**true**):** A purity flag of _b_=`true` indicates that _A_\[_m,r_\] is part of a sorted run. The directional merge optimizes for the case when \(A[\ell,m)\) contains parts from the same sorted run. Because the continuous run is non-decreasing, all run elements in the right half are greater than or equal to all run elements in the left half. When sorting \(A[\ell..m)\), larger non-run elements may move to index _m_-1, failing the skip check (_A_\[_m_-1\]_\>A_\[_m_\]). By invoking MergeBw, the merge repeatedly selects the larger element (favoring the right half on ties). This ensures the entire right half _A_\[_m,r_\] is consumed before selecting any left- half run elements. Once _A_\[_m,r_\] is exhausted, the remaining elements in \(A[\ell,m)\) are simply appended to the end of the merged result using 0 comparisons.<tbc>

• **Forward Merge (**_b_=`false**):** When _b_=`false`, the right child is not a pure run. The algorithm defaults to MergeFw, merging conventionally from left to right (smallest to largest). This offers a symmetric optimization: if the left half was pure (_a_=`true`) the trailing elements of the run in the right half would be appended using 0 comparisons.<tbc>





(a) Backward Merge (_b_=`true`)

(b) Forward Merge (_a_=`true`,_b_=`false`)

Figure 1: Subarray configurations exhibiting directional merge savings.

