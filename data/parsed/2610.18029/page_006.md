<tbc>colouring over the whole graph, and hence also over each vertex and its neighbours. This allows us to produce a more fine-tuned approximation of the MWC in a vertex’s neighbour without any significant processing per vertex, only a single vertex colouring at the beginning. In comparison to the MWC problem, the vertex colouring problem is more complex due to the number of colour assignments per vertex, reducing the efficacy of the greedy algorithm, suggesting the potential for improved solution quality via quantum approaches.

From there, we can remove vertices that are more straightforwardly incompatible with any MWCs: if the weight of a vertex is greater than the sum of the weights of its neighbours, we say it is "dominant", and it is always better to include the vertex rather than any subset of its neighbours. Therefore, we can store the vertex to reintroduce at the end, and discard the entire neighbourhood.

When the graph is particularly large and the previous steps have been ineffective, a more aggressive reduction is used, which checks specifically for cliques within a vertex’s neighbours. The sum of weights within a particular clique must be lower than the sum of all neighbours, and hence, at the (computational) cost of needing to find cliques, we can rule out vertices with complex neighbourhood graph structures that could not be previously ruled out. Noting that we do not need the MWC within the neighbours, just the existence of a clique with weight sum higher than the vertex weight, the algorithm in [5] simplifies this step by stopping the recursive MWC as soon as it finds a clique of an appropriate weight.

## 3 Classical Solvers

A survey of the maximum clique problem classical solvers can be found in [17] and [7].

Two performant exact clique solvers include _IncMaxCLQ_ [13] and _CliSAT_ [18]. _IncMaxCLQ_ was state of the art when published, but it has since been surpassed by _CliSAT_. We benchmark both solvers on real world graphs produced from Cherry’s phylogeny tool [5].

We also explore _FastWClq2_ [4] and _SCCWalk4L_ [21] approximate solvers, along with our own _AClique_ tool. These search a graph for a fixed amount of time, unless an exact solution is determined early, and return the best clique found. They work with approximate methods using random seeds meaning repeated runs can yield different examples of the maximum clique.

This is an important point as Cherry’s algorithm as initially written obtains all cliques with the maximum size and uses these to form a consensus tree. This is a standard method used to merge competing evidence into a single phylogenetic tree [1], [3]. However the original implementation of Cherry’s code has memory usage problems as the number of equally weighted maximum cliques grows significantly as the graph grows. Additionally even when the number of distinct cliques of maximum size is low, it may have enumerated many more maximal cliques without yet knowing they are not maximum [6]. For practicality reasons we extended Cherry’s tool to limit the number of stored cliques to a fixed size, with an eviction strategy for ensuring even distribution across the entire search run.

The best exact solvers are fast due to clever vertex ordering and branch-and-bound pruning, but they also yield the same instance of a maximum clique every time. It may be possible<tbc>

