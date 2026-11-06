<tbc>_partially dynamic._ The following section illustrates the algorithms that demonstrate the aforementioned differences.

## 6.1 All-Pairs Shortest-Path (APSP)

The all-pairs shortest-paths algorithms reports the distances between any two vertices in a graph. The algorithms attempt to answer distance queries between any two vertices while dynamically maintaining changes that can occur to the graph such as inserts, deletes, and updates.

Demetrescu and Italiano [38] propose a fully dynamic algorithm over directed graphs for all-pairs shortest-paths with real-valued edge weights. Every edge can have a predefined number of values. Their algorithm achieves an amortized time complexity of _O(Sn_<sup>2.5</sup>_log_<sup>3</sup>_n_) for update operations while achieving an optimal worst-case for query processing time. The proposed algorithm for the update operation inserts or deletes a vertex in addition to all its possible edges. The algorithm also maintains a complete distance matrix between updates.

Thorup [131] improves over Demetrescu and Italiano [38] by reducing the fully-dynamic graph problem to a smaller set of decremental problems. Thorup adopts the idea of a fully-dynamic minimum spanning tree by utilizing the efficiency of the decremental algorithm to solve the fully-dynamic all-pairs shortest- paths problem.

Bernstein [19] presents a \((2+\epsilon)\)-approximation algorithm for APSP over an undirected graph with positive edge weights. Bernstein’s algorithm achieves an update time that is almost linear and a query time of _O(loglogn_). The proposed query algorithm is deterministic while the update procedure is randomized. The algorithm run-time behavior depends on the distance from the source vertex to the destination vertex. Since _d(x,y_) is not known beforehand, the algorithm relies on guessing several different values for _d(x,y_).

Roditty and Zwick [111] propose a fully dynamic APSP algorithm for unweighted directed graphs. The algorithm is randomized and the correctness of the returned results are claimed to be high. The proposed algorithm passes through a set of phases that rely on the ideas of a decremental algorithm [77]. They demonstrate how the incremental and decremental versions of the SSSP problems are similar in terms of complexity to the the static all-pairs shortest-paths problem over directed or undirected graphs

Bernstein [21] proposes an \((1+\epsilon)\) approximate algorithm that improves over existing studies with respect to the delete operation and edge weight increase. The algorithm computes the decremental all-pairs shortest-paths on weighted graphs. The approach achieves an update time of _o(mn_<sup>2</sup>) using a randomized algorithm.

Henzinger et al. [75] enhances over the fastest deterministic algorithm by Shiloach and Even [122] by achieving an update time of _O(n_<sup>5/2</sup>). It also achieves a constant query time. Also, they propose a deterministic algorithm with with an update time of _O(mn_) and a query time of _O(loglogn_). They introduce two techniques, namely a lazy Even-Shiloach tree algorithm. The proposed approach maintains a shortest-paths tree that is bounded by distance with a Even-Shiloach tree based de-randomization technique.

## 6.2 Single-Source Shortest-Path

The single-source shortest-paths algorithm reports the distances from a given source vertex. The dynamic algorithm computes the update and query operations in an online fashion. The update operation inserts, deletes, or modify the edge’s weight. The query operation probes for the distance from the source vertex to a given target vertex.

Fakcharoenphol and Rao [51] propose an algorithm for planar graphs with real-valued edge weights.

