## 3 Complexity Analysis

In this section we prove the claimed bounds of directional mergesort by analyzing the merging tree.

**Definition 1** (Merging Tree)**.** The merging tree serves as a model for the execution of the algorithm, which takes the exact shape of a segment tree over the array of _n_ elements. The root of the tree at level 0 represents the entire array of size _n_. For any internal node _v_ covering the subarray \(A[\ell,r)\) at level _i_, its children at level _i_+1 are defined by the algorithm’s recursive splitting logic: a left child _L_ covering \(A[\ell,m)\) and a right child _R_ covering _A_\[_m,r_) where \(m=\lfloor(\ell+r)/2\rfloor\). The leaves correspond to singular elements of size 1, which is the base-case of the recursive algorithm. At every internal node, a merge operation combines the sorted subarrays from its left and right children.

**Fact 2.** At any level _h_ in the merging tree, the size of nodes are either \(\lfloor n/2^h\rfloor\) or \(\lceil n/2^h\rceil\).

**Fact 3.** At any level _h_ in the merging tree, all node subarrays are contiguous and pairwise disjoint.

### 3.1 Comparison Cost Analysis

We first isolate the skip check comparisons, which are guaranteed to occur before the merge at any internal node, so that we may focus on analyzing solely the cost of merging subarrays.

**Lemma 4.** _The total cost of skip checks across the entire algorithm is exactly n_-1 _comparisons._

_Proof._ At every internal node, exactly 1 comparison is used for the skip check. Because the merging tree is a full binary tree, the number of internal nodes is exactly one less than the number of leaves. Thus, a total of _n_-1 skip checks occur, requiring a total of _n_-1 comparisons.

**Accounting Scheme:** Instead of assigning the cost of a merge to the internal node, we distribute the cost to the individual elements. For each comparison in a merge loop, the winning element is charged with the 1 comparison. After exhausting one side, no comparisons are made or charged. We now consider a pre-existing non-decreasing run of length _r_ at the bottom level of the tree, with the goal of bounding the merge charges applied specifically to the elements of this run. We categorize the internal nodes relative to this run into four cases:

1. Fully Contained (Case 1): The node’s subarray consists entirely of elements from the run. The merge is guaranteed to be skipped (costing 0).<tbc>

2. Boundary (Case 2): The node’s subarray contains run elements as either a prefix or suffix.<tbc>

3. Encapsulating (Case 3): The node’s subarray completely encapsulates the entire run, containing non-run elements on both the left and right sides.<tbc>

4. Outside (Case 4): The node’s subarray contains no elements from the run (costing 0).

To bound the total merge charges incurred by a run of length _r_, we partition the levels of the merging tree into two distinct regimes using the threshold depth \(t=\lceil lg(n/r)\rceil\): for a node at level _h_, it is in the upper levels if _h\<t_, and it is in the lower levels if \(h\ge t\).

**Lemma 5** (Comparisons at Upper Levels)**.** _For a non-decreasing run of length r, the total number of comparisons charged to its elements at levels h\<t is bounded by rt._

_Proof._ At any level _h_, the nodes form a partition of the array into disjoint contiguous subarrays (Fact 3). Consequently, each element in the array belongs to exactly one node per level.

At any upper level \(h<t=\lceil lg(n/r)\rceil\), the node size is \(\lfloor n/2^h\rfloor\ge r\) according to Fact 2. Because node size exceeds _r/_2, Case 1 nodes cannot be guaranteed to exist in this regime.

