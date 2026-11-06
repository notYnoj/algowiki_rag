Note that the algorithm in \[DMSY23\] is randomized, thus our result is also the first deterministic algorithm to break such _O(m+n_log_n_) time bound even in undirected graphs.

### Technical Overview.

Broadly speaking, there are two traditional algorithms for solving the single-source shortest path problem:

• Dijkstra’s algorithm \[Dij59\]: via a priority queue, it each time extracts a vertex _u_ with the minimum distance from the source, and from _u_ relaxes its outgoing edges. It typically sorts vertices by their distances from the source, resulting in a time complexity of at least \(\Theta(nlogn)\).<tbc>

• Bellman-Ford algorithm \[Bel58\]: based on dynamic programming, it relaxes all edges for several steps. For finding shortest paths with at most _k_ edges, the Bellman-Ford algorithm can achieve this in _O(mk_) time without requiring sorting.

Our approach merges these two methods through a recursive partitioning technique, similar to those used in bottleneck path algorithms as described in \[GT88, CKT<sup>+</sup>16, DLWX18\].

At any point during the execution of the Dijkstra’s algorithm, the priority queue (heap) maintains a "fron tier" _S_ of vertices such that if a vertex _u_ is "incomplete" -- if the current distance estimate \(\widehat{d}[u]\) is still greater than the true distance _d(u_) -- the shortest _s-u_ path must visit some complete vertex \(v\in S\). In this case, we say _u_ is "dependent" on \(v\in S\). (However, vertices in _S_ are not guaranteed to be all complete.) The Dijkstra’s algorithm simply picks the vertex in _S_ closest to source, which must be complete, and then relaxes all edges from that vertex.

The running time bottleneck comes from the fact that sometimes the frontier may contain \(\Theta(n)\) vertices. Since we constantly need to pick the vertex closest to source, we essentially need to maintain a total order between a large number of vertices, and are thus unable to break the \(\Omega(nlogn)\) sorting barrier. Our most essential idea is a way to reduce the size of the frontier. Suppose we want to compute all distances that are less than some upper bound _B_. Let \(\widetilde{U}\) be the set of vertices _u_ with _d(u)\<B_ and the shortest _s-u_ path visits a vertex in _S_. It is possible to limit the size of our frontier |_S_| to \(|\widetilde{U}|/log^{\Omega(1)}(n)\), or \(1/log^{\Omega(1)}(n)\) of the vertices of interest. Given a parameter \(k=log^{\Omega(1)}(n)\), there are two possible cases:

• If \(|\widetilde{U}|>k|S|\), then our frontier already has size \(|\widetilde{U}|/k\);<tbc>

• Otherwise, suppose \(|\widetilde{U}|\le k|S|\). By running Bellman-Ford step _k_ times from vertices in _S_, every vertex \(u\in\widetilde{U}\) whose shortest _s-u_ path containing _\<k_ vertices in \(\widetilde{U}\) is complete. Otherwise the vertex \(v\in S\) which _u_ is dependent on must have a shortest path tree rooted at it with \(\ge k\) vertices in \(\widetilde{U}\), so we can shrink the frontier _S_ to the set of "pivots", each of which has a shortest path tree of size \(\ge k\), and the number of such pivots is bounded by \(|\widetilde{U}|/k\).

Our algorithm is based on the idea above, but instead of using a Dijkstra-like method where the frontier is dynamic and thus intractable, we use a divide-and-conquer procedure that consists of log_n/t_ levels, each containing a set of frontier vertices and an upper bound _B_, such that a naive implementation would still spend \(\Theta(t)\) time per frontier vertex and the running time would remain \(\Theta(logn)\) per vertex. We can however apply the aforementioned frontier reduction on each level so that the \(\Theta(t)\) work only applies to the pivots, about \(1/log^{\Omega(1)}(n)\) of the frontier vertices. Thus the running time per vertex gets reduced to \(logn/log^{\Omega(1)}(n)\), which is a significant speedup.

## 1.2 Related Works

For the SSSP problem, if we allow the algorithm to run in the word RAM model with integer edge weights, a sequence of improvements beyond _O(n_log_n_) \[FW93, FW94, Tho00a, Ram96, Ram97, Tho00b, Hag00\] culminated in Thorup’s linear-time algorithm for undirected graphs \[Tho99\] and _O(m+n_loglogmin{_n,C_})<tbc>

