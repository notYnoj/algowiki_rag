<tbc>becomes separable into the edge lengths. This allows the utility function to be identified using classical shortest-paths algorithms via paths that maximize the utility function.

Nikolova et al. \[106\] propose an algorithm for optimal route planning under uncertainty. They define the target as a function of both the path length and the departure time starting from the source. They indicate that path and start time are jointly optimizable due to the penalizing behavior that they exhibit for late and early arrivals. They also indicated that this joint optimization is reducible to classic shortest- path algorithms.

## 9 Parametric Shortest-Path Algorithms

Parametric shortest-paths objective is to compute the shortest-paths for all vertices based on a specific parameter. It probes for the parameter values known as _breakpoints_ where the shortest-path tends to change. The edge value varies based on a linear function of the parameter value.

Mulmuley and Shah \[102\] propose a model for lower-bound computation. It is a variant of the Parallel Random Access Machine. The proof starts with a lower-bound definition about the parametric complexity of the shortest-path problem. Plotting the weights of the shortest-path as a function results in an optimal cost graph that is piecewise-linear and concave. Breakpoints are defined as a fixed set of linear weight functions over a fixed graph.

Young et al. \[138\] propose a model where the computed edge values makes it more tractable than its predecessors. This tractability allows obtaining shortest-paths in polynomial time. They use the algorithm proposed by Karp and Orlin \[85\] and modify it to use Fibonacci heaps instead in order to improve its performance.

Erickson \[50\] proposes an algorithm for computing the maximum flow in planar graphs. The algorithm maintains three structures, namely an edge spanning tree, a predecessor dual vertex set, and the slack value of dual edge set. They compute the initial predecessor pointers and slacks in _O(nlogn_) using Dijkstra’s algorithm.

## 10 Replacement Shortest-Path Algorithms

Consider a Graph _G_=(_V,E_), where _V_ is the set of vertices and _E_ is the set of edges. For every Edge \(e\varepsilon E\) on the shortest-path from source \(s\varepsilon V\) to destination \(d\varepsilon V\) , the replacement path algorithm calculates the shortest-path from _s_ to _d_ that avoids _e_.

Emek et al. \[49\] propose an algorithm that computes the replacement path in near-linear time. The algorithm requires _O(nlog_<sup>3</sup>_n_) time during the preprocessing stage and _O(hloglogn_) time to answer the replacement path query, where _h_ is the number of hops in a weighted planar directed graph.

Roditty and Zwick \[112\] propose a Monte-Carlo randomized algorithm that computes the replacement path in an unweighted directed graph. The run-time complexity of the algorithm is \(\tilde{O}(m\sqrt{n})\). The Monte Carlo algorithm improves the run-time of the _k_-simple shortest-path and Vickrey pricing problems \[79\] by a factor of \(\sqrt{n}\).

Bernstein \[20\] proposes an approximate \((1+\epsilon)\) replacement-path algorithm that computes the paths in \(O(\epsilon^{-1}log^2n(m+nlog(nC/c)(m+nlogn))=\tilde{O}(mlog(nC/c)/\epsilon)\) time, where _C/c_ is the ratio of largest and smallest edge-weights in the graph. Bernstein’s algorithm achieves a running time of \(\tilde{O}(km\sqrt{n})\) when applied over the _k_-th simple shortest-paths problem.

