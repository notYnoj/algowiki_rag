<tbc>and 4.2, in each row/column we can achieve work proportional to the number of tentative states. Thus the cost to put sentinels and maintain the best decision arrays is also _O(mn_log_n_). □

## 5.3 General LWS on Trees

The idea of decision monotonicity (DM) can be applied to various structures more than just 1D cases discussed in Sec. 4. The efficient parallelism on 2D grid structure is introduced in Sec. 5.2, and we now show the techniques to enable high parallelism on the tree structure. Here we refer to this problem as Tree-GLWS.

Let _T_ be a tree with _n_+1 nodes, and node 0 is the root. We use _p(v_) to denote the parent of node _v_ and _d<sub>v</sub>_ be the distance from node 0 to node _v_. Tree-GLWS takes the input tree _T_, a cost function _w_, and the boundary _D_\[0\], and computes:

\(D[v]=min\{E[u]+w(d_u,d_v)\}\) (8)

where _u_ is any ancestor of _v_, and _E_\[_u_\]=_f(D_\[_u_\]_,u_) that can be computed in constant time from _D_\[_u_\] and _u_. The cost function _w_ is decided by the depths of _u_ and _v_. Note that here sibling nodes _v_<sub>1</sub> and _v_<sub>2</sub> will have the same DP value, but _E_\[_v_<sub>1</sub>\] and _E_\[_v_<sub>2</sub>\] can be different given that _v_<sub>1</sub> and _v_<sub>2</sub> are also part of the parameter in computing the function _f_. In this section we assume _w_ is convex, but our algorithm can adapt to the concave case with some modifications.

### 5.3.1 Building Blocks.

We will first overview some basic building blocks, which are crucial subroutines used in our algorithm.

**_Persistent Data Structures._** A persistent data structure \[36\] keeps history versions when being modified. We can achieve persistence for binary search trees (BSTs) efficiently by path-copying \[14, 16, 84\], where only the affected path related to the update is copied. Hence, the BST operations can achieve persistence with the same asymptotical work and span bounds as the mutable counterpart.

**_Heavy-Light Decomposition (HLD)._** HLD \[82\] is a technique to decompose a rooted tree into a set of disjoint chains. In HLD, each non-leaf node selects one **_heavy edge_**, the edge to the child that has the largest number of nodes in its subtree. Any non-heavy edge is a **_light edge_**. If we drop all light edges, the tree is decomposed into a set of top-down chains with heavy edges. As such, HLD guarantees that the path from the root to any node _v_ contains _O_(log_n_) distinct chains plus _O_(log_n_) light edges. If we use BSTs to maintain each heavy chain in HLD, we can answer path queries (e.g., query the minimum weighted node on a tree path) in _O_(log<sup>2</sup>_n_) work.

**_Range Report Based on Tree Depth._** We now discuss a data structure that efficiently reports the set of nodes in a subtree of _T_ where the depths of the nodes are in a given range _l_ to _r_. First we build the Euler-tour (ET) sequence of _T_, so any subtree of _T_ will be a consecutive subsequence in the ET. We can map all nodes to a 2D plane each with coordinates (_f<sub>v</sub>,d<sub>v</sub>_), where _f<sub>v</sub>_ is the first index of _v_ in the ET, and the _d<sub>v</sub>_ is the tree depth of _v_. Now the original query is a 2D range report on this 2D plan. A range tree \[83\] can be built in _O(n_log_n_) work and _O_(log<sup>2</sup>_n_) span, and answer this query in _O(m_+log<sup>2</sup>_n_) work and _O_(log<sup>2</sup>_n_) span where _m_ is the output size.

### 5.3.2 Our Main Algorithm.

Here if we consider any tree path, Recurrence (8) is exactly the same as for the 1D case in Sec. 4. Hence, we can use a similar approach as in Sec. 4 by maintaining the best- decision array of (\[_l,r_\]_,j_) triples, meaning that for elements _v_ with depth \(l\le d_v\le r\), _v_’s best decision is _j_. The challenge here is the<tbc>

<tbc>branching nature of a tree--we need to handle path divergences at nodes with more than one child. The work can degenerate to \(\tilde{O}(n^2)\) if we copy the best-decision arrays at the divergences, since we can end up with _O(n_) leaves. Sequentially, we can depth-first traverse the tree and compute the "current" best-decision array, and we only need to revert the array when backtracking. However, this approach is inherently sequential. To utilize the Cordon Algorithm on a tree structure, we need to resolve the following two challenges: 1) how to efficiently identify the ready nodes; and 2) how to efficiently maintain the best decision arrays for each node.

### _Identifying the Ready States._

Similar to the 1D case Sec. 4, we maintain the best-decision array for each tree path. Then we traverse the tree top-down, and we identify the ready states _v_ that can be finalized in this round, and compute them in parallel. An illustration can be found in Fig. 5.

Our high-level idea still follows the prefix-doubling technique, similar to the 1D case. In the _t_-th doubling step we expand all nodes with \(2^{t-1}\le d_v<2^t\). These nodes can be extracted by a range report shown in Sec. 5.3.1. We use prefix doubling and the checking process in Sec. 4 to decide the boundary that forms the cordon in the next round. When checking the availability, we can use the HLD-based tree path query to find the minimum (highest) node on each path that is not available. We will put sentinels on these nodes that block their subtrees. The process stops when we find such nodes for all tree paths. In Fig. 5, these ready nodes are shown in green. In the next round we can asynchronously work on the subtrees on the cordon in parallel. We repeat this process until all nodes are finalized (correctly computed).

Here one difference to the 1D case is that the work cost of prefix doubling cannot be perfectly amortized. In the 1D GLWS, if the prefix-doubling stops at step _t_, we visit at least 2<sup>_t_-1</sup> steady states and at most 2<sup>_t_-1</sup> unready states, thus the work to visit the unready states can be amortized. However, in the tree case we are doing prefix-doubling by the depth of nodes. The number of nodes in the last prefix-doubling step can be much larger than in the previous steps, and the cost cannot be amortized. The insight is that due to the prefix-doubling, each node _v_ will be visited in at most _O_(log_n_) rounds. Plus the _O_(log<sup>2</sup>_n_) work of the range report, the work in each round can be amortized to _O(h_log<sup>3</sup>_n_), where _h_ is the frontier size.

### _Updating the Best-Decision Arrays._

The most interesting part in this algorithm is how to maintain the best-decision arrays for all tree paths while achieving work efficiency and high parallelism. Due to the tree structure, the best-decision arrays for different branches of the tree share some parts. In total, there can be _O(n_) paths with total sizes of _O(n_<sup>2</sup>). The key challenge is to save the<tbc>

Finalized
Ready
Other
Cordon

**Figure 5:** Cordon Algorithm on a tree. Note that the sibling nodes must have the same status.

