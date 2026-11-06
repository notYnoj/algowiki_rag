from [12]. However, in [12] they only mention the application of DFS. We elaborate on the above other applications in Section 6.

Our algorithm works with vertex-weighted graphs, where previous works [9, 12] focused on the unweighted case (i.e., the unit-weight case. In particular, note that no vertex weighs more than 1_/n_ fraction of the total weight). Finally, it is often useful for applications to compute a separator in multiple vertex-disjoint subgraphs of _G_ simultaneously. Our algorithm can be easily extended to support this as we show in Section 5.

**Roadmap.** In Section 2 we give the necessary preliminaries. In Section 3 we overview related work and our technical contribution. Our deterministic separator algorithm is presented in Section 4, and its distributed implementation in Section 5. The applications are discussed in Section 6. Finally, Appendix A includes some deferred details from Section 5.

## 2 Preliminaries

**The CONGEST model.** We work in the standard distributed CONGEST model [17]. Initially, each vertex knows only its unique _O_(log_n_)-bit ID and the IDs of its neighbors. Communication occurs in synchronous rounds. In each round, each vertex can send each neighbor a distinct _O_(log_n_)-bit message. When the vertices of _G_ are weighted, we assume that the weights are polynomially bounded integers. Thus, the weight of a vertex can be transmitted in _O_(1) rounds. This is a standard assumption in the CONGEST model. Input and output are local, e.g. when rooting a spanning tree, we assume that all vertices know (as an input) the ID of the root _r_, and their incident edges in the tree. When the algorithm halts, each vertex knows the ID of its parent in the tree.

**Basic notation and graph theory.** We denote by _G_=(_V,E_) the vertex-weighted or face-weighted simple (connected) planar graph of communication. We denote by _D_ the hop-diameter of _G_ and by _F_ the set of faces of _G_ in a given planar embedding (defined next). When the weights are assigned to vertices (resp. faces), we denote the weight function by \(w_\nu(\cdot)\) (resp. \(w_F(\cdot)\)). We denote by _w<sub>A</sub>(G_) the total weight of _G_ w.r.t. \(w_A(\cdot)\) where \(A\in\{V,F\}\). When _A_ is clear from context we may omit it from the subscript and write \(w(\cdot)\).

**Planar embedding.** The _geometric_ planar embedding of a planar graph _G_ is a drawing of _G_ on a plane so that edges intersect only in vertices. In such embedding, there is a distinguished face \(f_\infty\) (called the infinite face) surrounding the graph. When we consider a cycle _C_ in _G_, we refer to _C_’s _exterior_ (resp. _interior_) as the side of _C_ that contains (resp. does not contain) \(f_\infty\). We denote by _C<sub>in</sub>_ (resp. _C<sub>out</sub>_) the interior (resp. exterior) of _C_, including _C_ itself. We denote the _strict_ interior (resp. exterior) of _C_ (i.e., excluding _C_) by \(C_{in}^-\) (resp. \(C_{out}^-\)).

A _combinatorial_ planar embedding of _G_ provides for each vertex \(v\in G\), the local clockwise ordering of its incident edges, such that the ordering is consistent with some geometric planar embedding of _G_. See Chapter 3.4 of [13] for more information. Throughout, we assume that a combinatorial embedding of _G_ is known locally for each vertex. This is achieved in \(\tilde{O}(D)\) rounds using the _deterministic_ distributed planar embedding algorithm of Ghaffari and Haeupler [6].

**Planar duality.** The _dual_ of a _primal_ embedded planar graph _G_ is a planar graph _G_<sup>∗</sup> whose nodes <sup>2</sup> correspond to the faces of _G_. For each edge \(e\in G\) that belongs to two faces in _G_, there is an edge _e_<sup>∗</sup> in _G_<sup>∗</sup> between the faces’ corresponding nodes (and a self-loop when the same face appears on both sides of an edge). We sometimes abuse notations and denote both _e_ and _e_<sup>∗</sup> as _e_. See the figure for an illustration (the primal graph _G_ in blue and its dual graph _G_<sup>∗</sup> in red).

<sup>2</sup>For clarity, we will refer to faces of the primal graph _G_ as _nodes_ (rather than vertices) of the dual graph _G_<sup>∗</sup>.



