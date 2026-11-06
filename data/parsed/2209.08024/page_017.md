<tbc>_Each operation requires_ O(log_n_) _time. A forest without edges and with n arbitrarily weighted vertices can be initialized in_ O(_n_) _time._

Note that Theorem 5.1 only admits _positive_ vertex weights, whereas we allowed zero-weight vertices. We show how to handle this problem in Section 5.2.

We now show how to use Theorem 5.1 to construct a centroid tree in O(_n_log_n_) time.

**Theorem 5.2.** _Given a tree_ T _on n vertices and a positive weight function w, we can compute a centroid tree of_ (T_,w_) _in_ O(_n_log_n_) _time._

_Proof._ First build a top tree on T by adding the edges one-by-one, in O(_n_log_n_) time. Then, find the centroid _c_, and remove each incident edge. Then, recurse on each newly created tree (except for the one containing only _c_). The algorithm finds each vertex precisely once and removes each edge precisely once, for a total running time of O(_n_log_n_).

## 5.1 Output-sensitive algorithm

We now improve the algorithm given above to run in time O(_n_log_h_), where _n_ is the number of vertices in T and _h_ is the height of the computed centroid tree.

The main idea of the algorithm is inspired by the linear-time algorithm for _unweighted_ centroids by Della Giustina, Prezza, and Venturini \[GPV19\]. Instead of building a top tree on the whole tree T , we first split T into connected subgraphs of size roughly _h_, and build a top tree on each component. Contracting each component into a single vertex yields _super-vertices_ in a _super-tree_. Each search for a centroid consists of a global search and a local search: We first find the super-vertex containing the centroid, then we find the centroid within that super-vertex. After finding the centroid, we remove it, which may split up the super-vertex into multiple super-vertices with a top tree each, and also may split the super-tree into a super-forest. Finally, we recurse on each component of the super-forest.

It can be seen that the total number of top tree operations needed is O(_n_). Since the top trees each contain only _h_ vertices, a top tree operation takes O(log_h_) time, for a total of O(_n_log_h_). We now proceed with a more detailed description of the algorithm.

### Ternarization.

If the degree of a vertex of T is unbounded, then a partition into similarly sized connected subgraphs may not be possible. To fix this, we _ternarize_ T by replacing each vertex _v_ of degree _d(v_) larger than three by a path _P<sub>v</sub>_ of _d(v_)-2 vertices with degree three. Call the new vertices _virtual_ and let \(\mathcal{T}'\) denote the resulting tree. Each virtual vertex of _P<sub>v</sub>_ is incident in \(\mathcal{T}'\) to an (arbitrary) edge incident to _v_ in T except for the two endpoints of _P<sub>v</sub>_ that are incident to two such edges each. We maintain a link between each vertex in T and every associated virtual vertex in \(\mathcal{T}'\) (if any).

Let \(w'\) be a weight function on \(\mathcal{T}'\) obtained from _w_ by arbitrarily distributing weight from each deleted vertex to its associated virtual vertices. Note that T and _w_ can be obtained from \(\mathcal{T}'\) and \(w'\), respectively, by contracting every group of associated virtual vertices. Further bserve that \(|V(\mathcal{T}')|\le 2n\).

### Partition.

Fix a parameter _k_. We now compute a partition into \(\mathcal{O}(\frac{n}{k})\) connected subgraphs of size at most 3_k_ as follows. Arbitrarily root \(\mathcal{T}'\). Iteratively remove minimal rooted subtrees of size at least _k_, using a simple linear-time bottom-up traversal. Since each node has at most three children, this produces connected subgraphs of size between _k_ and 3_k_. The only exception are the nodes remaining at the end, which we put into a possibly smaller subgraph. The total number of subgraphs is at most \(\frac{2n}{k}+1\).

### Building the super-tree.

By contracting each connected subgraph of the partition into a single vertex, we obtain a tree T, the _super-tree_, and a weight function _W_. We call each vertex \(A\in V(\mathfrak{T})\) a _super-vertex_, and write \(\mathcal{T}'[A]\) for the subgraph of \(\mathcal{T}'\) contracted into _A_. We write \(V(A)=V(\mathcal{T}'[A])\) for short. By definition of _W_ via the contraction, we have \(W(A)=w'(V(A))\).

Note that each _super-edge_ in _E_(T) is associated with precisely one normal edge in \(\mathcal{T}'\); we maintain an explicit link between the super-edge and the normal edge. For each super-vertex _A_, we build a top tree on<tbc>

