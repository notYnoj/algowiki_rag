## 1 Introduction

In the planar, dynamic All-Pairs Shortest Paths (APSP) problem, one is given a planar, directed and weighted graph _G_=(_V,E,w_) undergoing edge updates, i.e. edge insertions and deletions and the goal is to maintain a data structure that processes edge updates and can return for any pair of vertices \(x,y\in V\) , the distance _d<sub>G</sub>(x,y_) from _x_ to _y_ in the current version of _G_. In this work we use a somewhat restricted setting where the embedding is preserved throughout. Thus the allowed updates are edge weight increases and decreases.

This problem is maybe the most notorious open problem in planar dynamic graph algorithms: while a data structure exists \[16, 25\] that achieves worst-case update and query time \(\tilde{O}(n^{2/3})\) and a conditional lower bound \[1\] indicates that \(\tilde{\Omega}(\sqrt{n})\) update and query time is essentially necessary, progress to close this gap has proven elusive.

**Research Question 1.** _Can we close the gap between_ \(\tilde{O}(n^{2/3})\) _and_ \(\tilde{\Omega}(\sqrt{n})\) _update and query time for planar, dynamic APSP?_

Currently all approaches to achieve fast update and query times boil down to rather straightforward extensions of static algorithms combined with the simple fact that there exists an _r_-division for any planar graph. Our approach involves a recursive decomposition into _r_-divisions.

**Definition 1.1** (r-division)**.** _Given planar embedded graph G and_ \(r\ge 1\)_, an r-division is a set of O(n/r_) _edge-induced subgraphs G_<sub>1</sub>=_G_\[_E_<sub>1</sub>\]_,G_<sub>2</sub>=_G_\[_E_<sub>2</sub>\]_,...,G<sub>k</sub>=G_\[_E<sub>k</sub>_\]_, called_ pieces_, each of vertex size at most r where E_<sub>1</sub>_,E_<sub>2</sub>_,...,E<sub>k</sub> partition the edge set E, such that each piece G<sub>i</sub> shares at most_ \(O(\sqrt{r})\) _vertices_ \(\partial G_i\) _with any of the other pieces. Further all vertices_ \(\partial G_i\) _are on a constant number of holes of G<sub>i</sub> (where a_ hole _of G<sub>i</sub> is a face in the induced graph G<sub>i</sub> that is not a face of G)._

For convenience, we will assume the vertices of the _O_(1) holes of a piece _P_ are exactly the boundary vertices of _P_. This can always be ensured by adding, for each hole _h_, infinite-weight dummy edges between boundary vertices of _h_ that are consecutive in the cyclic ordering of the vertices of _h_.

**Definition 1.2** (Capped Recursive decomposition)**.** _Given graph G and_ \(r\ge 1\)_, an r_-capped recursive decomposition _of G is a forest_ R _with_ \(\lfloor lrr\rfloor\) _levels where each node is associated with a subgraph of G. In particular, each child node is associated with a subgraph of the graph associated with its parent node. Further, the nodes in_ R _that are at distance i from the root, form an r/_2_<sup>i</sup>-division of G (and an r/_2_<sup>i</sup>-division of their parent’s graph) and leaf nodes consist of a single edge only. We often do not distinguish between a node and its associated subgraph of G._

It is well-known that such an _r_-capped recursive decomposition can be found for any _r_ and planar _G_ in linear time \[26\]. The approach of \[16, 25\] is to initially construct an _n_<sup>2/3</sup>-capped recursive decomposition R, where for each subgraph _H_ in R, it computes the distances \(\partial H\times\partial H\) which are stored as a complete graph over \(\partial H\) (so-called _dense distance graph (DDG)_ of _H_), and finally exploit a clever modification of Dijkstra’s algorithm (see the Theorem below) to implement queries in \(\tilde{O}(n^{2/3})\) time by leveraging the DDGs.

**Theorem 1.3** (FR-Dijkstra, see \[16, 21\])**.** _Given a graph G, and r-capped recursive decomposition_ R _and dense distance graphs for every graph in_ R_. Then, there exists an algorithm that for any_ \(x,y\in V\)_, computes the distance d<sub>G</sub>(x,y_) _in time_ \(\tilde{O}(n/\sqrt{r})\).

