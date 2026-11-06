<tbc>sets of vertices visited by the forward contraction hierarchy from _s_ and the reverse contraction hierarchy of _t_. The contraction hierarchies algorithm computes for the shortest-path the intersection of the forward and reverse sets that contain the maximum-rank vertex.

Babenko et al. [9] propose an approximation algorithm for producing small labels. Their main target is to reduce the size of the maximum hub-label. This reduction process leads to unbalanced solutions as vertices will have a skewed label sizes. They propose an approximation algorithm for the maximum label size that runs in _O(logn_). The proposed approach reduces the the hub-labeling problem to a set-covering problem.

Cohen et al. [31] propose a data structure for storing the reachability label using a 2-hops cover of all the paths in a graph. Each vertex \(v\epsilon V\) precomputes the Label _L<sub>in</sub>_ and \(L_{out}\subseteq V\) such that, for any pair _s_ and _t_, at least one vertex is in \(L_{out}(s)\cap L_{in}(t)\). The distance labeling query finds the shortest-path from source _s_ to destination _t_ by finding the minimum distance from (_L<sub>out</sub>(s),x_) to (_x,L<sub>in</sub>(t_)) for each label \(x\epsilon(L_{out}(s)\cap L_{in}(t))\). The size of a label _L_ is not guaranteed and the polynomial preprocessing time is approximately _O(logn_) for finding a 2-hop cover of the invariant paths whose size is larger than the set of all shortest-paths.

Chang et al. [29] propose a multi-hop distance labeling with a size smaller than another 2-hop labeling approach [31]. In the preprocessing phase, the algorithm stores a parent function _P_ that assigns the parent vertex to each vertex by avoiding the preprocessing of the all-pairs shortest-path. The proposed approach performs vertex separation on the graph _G_ that divides _G_ into multiple connected subgraphs. The graph is further decomposed into a minimal tree _T(I,F_), where \(I\subset V\) represents the set of vertices and _F_ is the set of edges. The approach uses the distance query to compute the minimum distance. The time complexity of query processing is _O(tw∗h_), where _tw_ represents the width and _h_ represents the height of the decomposed tree _T_.

#### 5.5.6 Highway Node Routing

The motivation behind using highway node routing is that prominent vertices that overlap various shortest-paths will generate sparse overlay graphs. The result would be faster query processing and lower space overhead.

Schultes and Sanders [118] proposes a dynamic algorithm that is space-efficient and allows query time to be thousand times faster when compared to Dijkstra’s algorithm. The choice of vertices is achieved by capitalizing on previous results in addition to using the required vertex sets defined by highway hierarchies algorithms. They simplify the complications of computation into the preprocessing step. This also leads to simplification of the query processing algorithm, especially the dynamic variants.

Abraham [3] suggests that road networks do not necessarily have a significant highway dimension. The proposed algorithm relies on realizing balls of a specific radius _r_. For every _r\>_0, there exits a sparse set _S<sub>r</sub>_ where shortest-path of length more than _r_ will have a vertex from the set _S<sub>r</sub>_. If every ball having radius _O(r_) contains less number of vertices than _S<sub>r</sub>_, then the set _S<sub>r</sub>_ is sparse.

## 6 Dynamic Shortest-Path Algorithms

The main requirement of dynamic shortest-path algorithms is to process updates and query operations efficiently in an online fashion. In the update operation, edges are inserted or deleted from the graph. In the query operation, the distance between vertices is computed.

_Fully dynamic algorithms_ are those that can process insertions and deletions. _Incremental algorithms_ can process insert operations, but not delete operations. _Decremental algorithms_ can process delete operations, but not insert operations. This implies that incremental and decremental algorithms are<tbc>

