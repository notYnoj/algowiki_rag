<tbc>to its central role in modern AI systems, which often represent data using high-dimensional vector embeddings. Tasks such as semantic search, retrieval-augmented generation, recommendation, and clustering all require fast nearest-neighbor search over such vector representations \[8, 26, 30, 31, 41\].

Given the problem’s importance, many different methods have been proposed to solve approximate nearest neighbor search, including well-known and widely used methods like locality sensitive hashing \[2, 3, 20\], quantization-based inverted file indices \[17, 23, 24\], and tree-based methods \[7, 35\]. In recent years, there has been a surge of interest in a class of algorithms referred to as **_graph-based nearest neighbor search methods_**. Such methods include Hierarchical Navigable Small World (HNSW) Graphs \[33\], Vamana/DiskANN \[28, 40\], Navigating Spreading-out Graphs (NSG) \[16\], and more \[5, 6, 15, 18, 32, 34, 36, 37\]. Such methods offer state-of-the-art performance on a number of leading benchmarks and search competitions \[6, 37, 38\].

In graph-based methods, the core data structure used to support nearest neighbor search is a directed graph _G_=(_P,E_) with a node corresponding to every point in the dataset. A query _q_ is serviced by starting at some node in the graph, and greedily moving to the out-neighbor that is closest to _q_. The search continues in this way, terminating when no closer neighbor exists. Given the simplicity of this greedy search algorithm, a key differentiator between graph-based methods is how the search graph _G_ is constructed. How should the edges in _E_ be chosen to facilitate fast and accurate nearest-neighbor search?

## 1.1 \(\alpha\)-Navigable Graph Construction

While many different approaches have been employed to construct search graphs, **_navigability_** has been repeatedly identified as a desirable property for such graphs \[32, 40\]. A graph is **_navigable_** if, for every source point _s_ and distinct target point _t_ in _P_, the graph has an edge (_s,v_) where _d(v,t)\<d(s,t_), i.e. the source has an edge that leads closer to the target. On such a graph, a greedy traversal from any starting point in _P_ must converge to any query point, so long as that query is itself a member of _P_; at every step, the navigability property ensures that the traversal can make progress, until it lands on the query itself.

This basic property can be strengthened to \(\alpha\)**_-navigability_**, defined for any parameter \(\alpha\ge 1\). In this case, it is not sufficient that a source simply have an edge leading closer to each target: it must have an edge that shrinks the distance to a target by a multiplicative factor of \(\alpha\) or more. Formally, for each source-target pair _s,t_, there must be an edge (_s,v_) where \(d(v,t)<\frac{1}{\alpha}d(s,t)\).

\(\alpha\)-navigability is a powerful property. If _G_ has this property, then greedy search not only converges to any query in _P_, but it can be shown that it provides provably accurate approximate nearest neighbors for arbitrary queries. In particular, as long as the distance function _d_ is a metric, for any query _q_, greedy search will converge to a nearest neighbor whose distance from _q_ is no more than \(\frac{\alpha+1}{\alpha-1}\) times that of the query’s true nearest neighbor \[21\]. We obtain a better approximation for larger values of \(\alpha\).

Moreover, in addition to ensuring provably accurate results, \(\alpha\)-navigability ensures fast convergence. When \(\alpha>1\), we will converge to an \(\frac{\alpha+1}{\alpha-1}\)-approximate nearest neighbor in no more than

\(\lceil log_\alpha(\Delta_P)\rceil,\)

steps, where the **_aspect ratio_** \(\Delta_P\) of _P_, is the ratio between the largest and smallest pairwise distances in _P_. Moreover, search does not just converge for queries in _P_.

Fast convergence alone, however, does not govern the computation cost of graph-based nearest neighbor search. In particular, the cost of every search iteration scales with the number of out- neighbors of the current node. I.e., search is faster if _G_ is sparse. Graph sparsity also controls<tbc>

