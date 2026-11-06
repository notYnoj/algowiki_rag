Geisberger et al. [63] devise an algorithm based on contraction hierarchies to calculate continent-based shortest-paths. The preprocessing step relies on the hierarchical properties of road networks in order to add shortcut edges. They use a modified version of Dijkstra’s algorithm that visits only a few hundred vertices that in turn makes it suitable to implement on mobile devices.

## 5.5.3 Multi-Level Graphs

In a multi-level overlay graph, if a set of vertices lie at a specific level, then the shortest-paths in that level do not use vertex from the upper levels. In turn, this method depends on the correct selection of vertices to act as landmarks on the higher levels.

Schulz et al. [120] propose a multi-level graph-based decomposition method that targets space reduction. This method precomputed the shortest-paths and replaces the weights of single edges with a weight equal to the shortest-path length. The result is a subgraph that is smaller in size when compared with the original graph. The subgraph distances between a set of vertices is the same as the shortest-path graph distance between the same set of vertices in the original graph.

Holzer et al. [80] introduce several vertex selection criteria on overlay graphs. These include criteria to determine a representative subset of the original graph. They investigate the criteria’s effectiveness over multilevel overlay graphs and the speed-up achieved for shortest-path computation.

## 5.5.4 Transit vertex Routing

Transit vertex routing precomputed the shortest paths to and from all landmarks identified in a graph. The algorithm requires extensive preprocessing but exhibits very fast query time as it requires a limited number of look-ups between landmarks located in different locations.

Bast et al. [12] propose transit vertex routing. They suggest that a vertical and horizontal sweep are sufficient to compute the set of transit vertices. They also illustrate some techniques to make the approach more space-efficient.

Arz et al. [8] propose a variant of contraction hierarchies that achieves an order of magnitude speeds up , similar to the time needed to find contraction hierarchies. They propose a graph-theoretical locality filter that does not affect the query time.

## 5.5.5 Hub Labeling

Modeling road networks as a low-dimensional graph is a method used for computing the shortest paths. One method used for such modeling is the process of _labeling_. Algorithms for labeling have been introduced in the distributed computing field [61, 132]. In the labeling preprocessing stage, each vertex _v_ is computed and assigned a _forward label_ and a _reverse label_. The forward label encompasses a set of vertices _w_, where each vertex contains a computed distance _dist(v,w_) from _v_. The reverse label consists of a set of vertices _u_, where each vertex contains a computed distance _dist(u,v_) to _v_. These labels are later used in the query stage to determine the vertices that minimize the distance from source to destination. A label can be perceived as a set of _hubs_ that a vertex _v_ has a direct connection to. The labeling algorithm ensures that any two vertices have one hub in common when computing the shortest path.

Hub labeling starts by preprocessing the vertices, where, for each vertex _v_, it precomputes the distance to a set of landmarks _L(v_) in the vertex label. The query algorithm is fast as long as the number of landmarks of the source and destination vertices is small. Storing the labels in a consecutive manner allows the algorithm to exhibit good locality.

Abraham and Delling [1, 2] propose a labeling scheme that, given a vertex _s_ and _t_, it considers the

