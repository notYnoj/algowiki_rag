<tbc>complementary: bipartite permutation graphs are AT-free and biconvex, but biconvex graphs need not be AT-free. Section 2 gives the inclusion relations and a small example separating the two classes.

## 2 Preliminaries

All graphs are finite, simple, and undirected. For a graph _G_, write _n_=|_V(G_)| and _m_=|_E(G_)|. The open and closed neighbourhoods of a vertex _v_ are _N<sub>G</sub>(v_) and _N<sub>G</sub>_\[_v_\], respectively. For \(U\subseteq V(G)\), _G_\[_U_\] denotes the subgraph induced by _U_. An independent set consists of pairwise nonadjacent vertices, and \(\alpha(G)\) is its maximum size. For \(D\subseteq E(G)\), let _V(D_) be the set of endpoints of its edges. Throughout the paper, a _star_ means _K_<sub>1_,t_</sub> with \(t\ge 1\). In particular, _K_<sub>2</sub> is a star, and either endpoint may be chosen as its centre. A star with at least two edges has a unique centre.

We use the edge open packing definition from the introduction. The following characterisation also specifies exactly which edges are selected.

**Observation 1.** _An edge set_ \(D\subseteq E(G)\) _is an edge open packing if and only if every connected component of G_\[_V(D_)\] _is a star. In this case, E(G_\[_V(D_)\])=_D._

_Proof._ If _D_ is an edge open packing, an edge in _E(G_\[_V(D_)\])\\_D_ would join two distinct selected edges incident with its endpoints. Hence _E(G_\[_V(D_)\])=_D_. This graph contains neither a triangle nor a path with three edges as a subgraph: in either case one edge is common to two others. A connected graph with an edge and neither of these subgraphs is a star. Conversely, if every component of _G_\[_V(D_)\] is a star, each leaf belongs to _V(D_), so its unique incident edge must belong to _D_. Thus all star edges are selected, and no third edge joins two of them in the forbidden way.

A graph is _chordal_ if it has no induced cycle of length at least four. Its maximal cliques admit a _clique tree_: for each vertex _v_, the maximal cliques containing _v_ induce a connected subtree \[14, 15\]. An _asteroidal triple_ is an independent set {_u,v,w_} such that each pair is joined by a path avoiding the closed neighbourhood of the third vertex. A graph is _AT-free_ if it contains no asteroidal triple.

A bipartite graph \(G=(X\cup Y,E)\) is _convex bipartite_ if one part, say _X_, admits an ordering _x_<sub>1</sub>_,...,x<sub>p</sub>_ in which every neighbourhood _N(y_), \(y\in Y\) , is consecutive. After deleting isolated vertices, write \(N(y)=\{x_{\ell(y)},\dots,x_{r(y)}\}\) with \(1\le\ell(y)\le r(y)\le p\). A convex ordering can be found by testing the consecutive- ones property of the bipartite adjacency matrix \[2\]. A graph is _biconvex bipartite_ if both parts admit such orderings. A _bipartite permutation graph_ is a bipartite graph whose vertices can be represented by line segments between two parallel lines, with adjacency corresponding to intersection. A bipartite graph is _chordal bipartite_ if it has no induced cycle of length at least six.

The standard strict inclusion chain is bipartite permutation graphs \(\unknown\) biconvex bipartite graphs \(\unknown\) convex bipartite graphs \(\unknown\) chordal bipartite graphs \[3\]. Bipartite permutation graphs are AT-free, but biconvex graphs need not be. For example, take a cycle _abcda_ and add pendant vertices \(a',b',c',d'\) at the corresponding cycle vertices. The two part orders \((b',a,c,d')\) and \((a',b,d,c')\) show that this graph is biconvex, whereas \(\{a',b',c'\}\) is an asteroidal triple. Consequently, our AT-free result does not subsume the earlier biconvex result. A claw with each edge subdivided once is convex but not biconvex: order its three subdivision vertices on one side to obtain convexity; on the other side, making each pair consisting of the original centre and an original leaf consecutive would require the centre to be consecutive with three different vertices.

## 3 Maximum Edge Open Packing in AT-Free Graphs

We use the oriented star-conflict graph of Das and Santra \[13\] to reduce Maximum Edge Open Packing on an AT-free graph to Maximum Independent Set on another AT-free graph.

### 3.1 The oriented star-conflict graph

We recall the construction from \[13\]. An _oriented edge_ of _G_ is an ordered pair \((c,\ell)\) such that \(c\ell\in E(G)\). The _oriented star-conflict graph A<sub>G</sub>_ has all oriented edges of _G_ as its vertices. Two distinct oriented edges \((c,\ell)\) and (_d,r_) are _compatible_ if one of the following conditions holds.

(i) They have the same centre: _c=d_, \(\ell\neq r\), and \(\ell r\notin E(G)\).<tbc>

(ii) The vertices \(c,\ell,d,r\) are all distinct, and none of the four pairs \(cd,cr,\ell d,\ell r\) is an edge of _G_.<tbc>

