<tbc>one of them to be alive. In fact, for every maximal block of consecutive dead integers, we only store the most recently accessed integer as a leaf in the main tree. We also store all alive integers. This ensures that, for any two integers _i,j_, the number of leaves in the main tree with integers between _i_ and _j_ is at most \(2\cdot|\{k|\text{leaf}k\text{exists}\wedge min(i,j)\le k\le max(i,j)\}|\), which then yields the stronger bound <o>_d_</o>(_i_) instead of _d(i_).

For the main tree, we use a 2-3-4 tree \[16\] instead of a complete binary tree. This will allow us to delete leaves corresponding to consecutive dead integers created by the deleteLeaf operation. The index trees remain the same, but the constants in invariant (6) need to be increased since 2-3-4 trees allow nodes to have up to four children. Similarly, some constants in the analysis need to be increased, e.g. in Lemma 17, we may get four consecutive newly created leaders of the same height, and in the proof of Lemma 21, we might need 6height(_u_) steps from _u_ to find a locked leader.

The implementations of addLeaf, access, changeKey, cleanupStep and cleanup remain largely the same. To perform deleteLeaf(_i_), we first invoke \(\text{changeKey}(i,\infty)\). Then, we mark leaf _i_ as dead and delete any adjacent dead leaves in the main tree. This might cause the 2-3-4 tree to perform some rebalancing operations, specifically _fusing_ and _borrowing_ \[16\]. Rebalancing non-leader nodes is a non-issue. For any rebalancing operation involving one or more leader nodes, we first deactivate these leader nodes and perform the operation. Then, we fix invariant (3) as in the access operation, and update the index trees. If _h_ is the height of the node involved in the rebalancing operation, then deactivating leaders creates _O_(1) bills, fixing invariant (3) takes zero amortized time, and updating the index trees takes _O(h_) time. Thus, the amortized running time of a rebalancing operation at height _h_ is _O(h_). The 2-3-4 tree analysis (Theorem 2.b in \[16\]) shows that _n_ insertions and deletions trigger at most \(n\cdot(\frac{3}{5})^{h-1}\) rebalancing operations at height _h_. Thus, the total additional running time due to rebalancing is \(n\cdot\sum_{h=1}^{log_2n}h(\frac{3}{5})^{h-1}\in O(n)\).

## 7 Open problems

### 7.1 Heaps with the Unified Bound

Both the construction and analysis of our heap with the unified bound is complicated and uses a slew of invariants and amortization potentials. It would be nice to have a simple construction, as was achieved for the working set heap \[31\]. Alternatively, it would be interesting to show that an existing self-adjusting structure, such as the smooth heap or pairing heap does the trick.

### 7.2 Chain-Antichain Partition for Points

An earlier attempt at solving sorting under partial information with merge sort (instead of heap sort) failed since we could not solve the following subproblem: You are given an integer _k\>_0 and a list _X_ of _n_ items. In _O(n_log_k_) time, partition _X_ into

• up to _k_ increasing subsequences of any length,<tbc>

• plus any number of decreasing subsequences, each of length at least _k_+1.

Such a partition always exists: While the longest decreasing subsequence of _X_ is longer than _k_, delete it. Afterwards, by Dilworth’s theorem, _X_ can be partitioned into _k_ increasing subsequences.

For our purpose, it would be enough if the decreasing subsequences had length \(\Omega(k^\varepsilon)\) for some \(\varepsilon>0\). The difficult part is that there is no wiggle room in terms of running time: it has to be _O(n_log_k_). (The chain-antichain merge sort of \[19\] solves a generalization of this problem to arbitrary partial orders in \(\tilde{O}(nk^2)\) time.)

