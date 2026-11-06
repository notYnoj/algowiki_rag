## 11 Alternative Shortest-Path Algorithms

The alternative shortest-path problem reports paths that avoid a given vertex or edge, termed the unwanted vertex or the unwanted edge. The key difference between the replacement-path and the alternative shortest-path is that the user is not required to specify the unwanted vertex or edge for replacement paths. The goal of the alternative path problem is reusing the previously computed results of the unwanted vertex or edge. In turn, this achieves better performance. Existing algorithms, e.g., all-pairs dynamic shortest-paths, do not solve the alternative shortest-path problem because of the high complexity of the update operation.

Xie et al. [136] propose a storage schemed, termed iSPQF. It is an extension of the shortest-path quad-tree [115] that further reduces the number of quad-trees at each vertex. The space complexity of the shortest-path quad-tree into forest (SPQF) is _O(n_<sup>1.5</sup>). The SPQF algorithm can find the alternative shortest-path over a single source (from source _s_ to destination _d_ that avoids Vertex _v_) as well as all pairs (from set of sources _X_ to set of destinations _Y_ that avoid Vertex _v_) in _O(n_) time-complexity.

## 12 Weighted Region Shortest-Path Algorithms

Mitchell and Papadimitriou [97] define the Weighted Region Problem (WRP) as a generalization of the two-dimensional shortest path problem with obstacles. The problem assumes that the plane is subdivided into weighted polygonal regions. The objective is to minimize the cost according to a weighted Euclidean metric. The study by Mitchell and Papadimitriou sheds light on the discriminating properties of the weighted region problem over planar divisions and proposes an algorithm that runs in _O(n_<sup>8</sup>_L_), where _n_ is the number of vertices and _L_ is the number of bits required to encode the problem instance. In specific, \(L=O(log(nNW/\epsilon W))\), where _N_ is the maximum integer representing vertices of the triangulation, and \(\epsilon>0\) is a user-specified error value that can be tolerated.

Mata and Mitchell [94] propose an algorithm to compute the approximate optimal-path for the weighted planar subdivision problem by constructing a sparse graph, termed the _path-net_. The approach uses Snell’s law of Refraction [133] to divide the vertices into cones that bound the path of a vertex. The worst-case complexity to build the path-net graph with _O(kn_) vertices is _O(kn_<sup>3</sup>), where _k_ is the number of cones. After being scanned, it produces the paths that are within a factor of \((1+\epsilon)\) from the optimal solution.

## 13 Conclusion

In this paper, we devise a taxonomy for the shortest-path problem. For each branch of the taxonomy, we illustrate the discriminating features and highlight the state-of-the-art research. The taxonomy provides investigators of the shortest-path problem with a guideline on where a required problem definition maps within the current related work.

## Acknowledgements

Walid G. Aref’s research has been supported in part by the National Science Foundation under Grant IIS 1117766.

