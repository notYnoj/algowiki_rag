## 6 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

We find this problem interesting from a fine-grained complexity viewpoint because it appears closely related to another area whose fine-grained landscape still has many open problems: the detection of induced patterns (see \[FKLL12, VWWY15, BKS18, DVV21, DV22\]), where also runtimes of \(\mathcal{O}(n^{2\omega})\) are common, e.g., for detecting a six-clique or other patterns.

Finally, we mention that algorithms for detecting _uv_-trails have been used to improve the runtime for recognizing graphs in which all holes have the same length. This was first achieved by Cook et al. \[CHP<sup>+</sup>24\] in time O(_n_<sup>21</sup>) and subsequently improved by Chiu and Lu \[CL24\] to \(\mathcal{O}(n^{2\omega+3})\).

### Recognition of Quasi-Triangulated Graphs and Decremental Simplicial Vertex.

The second problem is the recognition of another generalization of triangulated graphs, called _quasi-triangulated_ graphs. A graph **G** is _quasi-triangulated_ if and only if every induced subgraph of **G** contains a simplicial vertex or a _cosimplicial vertex_ (i.e., a simplicial vertex in the complement). Just as triangulated graphs can be recognized by iteratively removing a simplicial vertex from the resulting graph, quasi-triangulated graphs can be recognized similarly by iteratively removing a simplicial or cosimplicial vertex. Thus both classes can be recognized using the following subroutine.

**Decremental Simplicial Vertex**

**Input:** An unweighted graph **G**=(_V,E_).

**Update:** Delete a given vertex _v_ together with all its incident edges.

**Query:** Does the current graph **G** contain a simplicial vertex? If so, return one.

Hence, to recognize whether a graph **G** is quasi-triangulated, it suffices to maintain a decremental simplicial vertex subroutine for both **G** and its complement \(\tilde{\mathbf{G}}\), proceeding iteratively as follows: In each iteration, check whether **G** or \(\tilde{\mathbf{G}}\) contains a simplicial vertex. If such a vertex _v_ exists in either graph, remove _v_ from both **G** and \(\tilde{\mathbf{G}}\). If this elimination process continues until the graph is empty, **G** is quasi-triangulated. Otherwise, if the process halts because neither **G** nor \(\tilde{\mathbf{G}}\) contains a simplicial vertex, the algorithm terminates and rejects **G**.

In reality, triangulated graphs can be recognized faster, in linear time \[RTL76\], using another simple algorithm. However, the fastest algorithm for quasi-triangulated graphs runs in time O(min(_n_<sup>2.77</sup>,_nm_)) \[Spi04, Hoà03\], where the recognition algorithm relies on the decremental simplicial vertex subroutine. We find this last problem especially interesting from a fine-grained point of view because edge- decremental triangle detection has recently been shown to admit a \(\tilde{\mathcal{O}}(n^\omega)\)-time algorithm \[BBF<sup>+</sup>26\]. In this light, it would be interesting to see whether Triangle Detection, Simplicial Vertex, or High- dimensional OV all retain a \(\tilde{\mathcal{O}}(n^\omega)\)-time algorithm, or whether some interesting difference emerges.

Our partial progress here is an improvement of the algorithm for Decremental Simplicial Vertex to O(_n_<sup>2.5275</sup>), which on sparse graphs can be balanced to be something slightly better.

**Theorem 4.14.** _There is an algorithm for Decremental Simplicial Vertex that on an n-node graph runs in time_

\(\mathcal{O}\left(min_{\Delta\in[1..n]}\left\{n/\Delta\cdot MM(n,\Delta,n)+m\cdot\Delta\right\}\right).\)

_In particular, with the current bounds on rectangular matrix multiplication_<sup>6</sup> _this gives a running time of_ O(_n_<sup>2.5275</sup>) _on dense graphs. For sparse graphs, bounding the rectangular product naively by dividing it into_ \(\Delta\times\Delta\) _blocks yields a running time of_ \(\mathcal{O}\left(m^{(3-\omega)/(4-\omega)}n^{3/(4-\omega)}\right)\).

Notably, the running time we obtain is the same as the best known running times for both directed unweighted APSP \[Zwi02\] and Min Witness Product \[CKL07\].

<sup>6</sup> We used the bounds from \[ADV<sup>+</sup>25\] plugged into van den Brand’s optimization tool \[Bra\].

