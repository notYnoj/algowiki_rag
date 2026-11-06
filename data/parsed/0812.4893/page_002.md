## 1.1 Matchings

We follow the convention (see, e.g., Fleiner [7]) that an instance of the stable marriage problem is specified by a simple undirected bipartite graph \(\EuScript{G}=(R\cup B,E)\); the graph may be disconnected but there are no isolated nodes. Call the nodes in _R red_, the nodes in _B blue_, and the graph G a _bicoloured_ graph. Each node \(v\in R\cup B\) has a linear order on the adjacent nodes. The linear order constitutes the _matching preference_ for _v_; if a node _u_ is not adjacent to _v_, then neither _u_ is an acceptable partner for _v_ nor _v_ is acceptable for _u_.

A set of edges \(M\subseteq E\) is a _matching_ if every node is incident to at most one edge in _M_. Two nodes joined by an edge in _M_ are _matched_ in _M_; a node not incident to an edge in _M_ is _unmatched_ in _M_. A matching is _maximal_ if it is not a subset of a larger matching. A matching is _maximum_ if it has the maximum size among all the matchings. In an edge-weighted graph, a _maximum-weight_ matching is the one that has the maximum weight among all the matchings. A _greedy_ matching is a maximal matching obtained by adding the edges one by one, in order of decreasing weight. It is well-known that the greedy matching is a 2-approximation to the maximum-weight one.

Let _M_ be a matching. An edge \(\{u,v\}\in E\backslash M\) is _unstable_ relative to _M_ if both (i) _u_ is unmatched or prefers _v_ over its current match in _M_; and (ii) _v_ is unmatched or prefers _u_ over its current match in _M_. The matching _M_ is _stable_ if there are no unstable edges. Let \(\epsilon>0\) be some constant. This work is centred on the following notion of "almost stability".

**Definition 1.** A matching _M_ is \(\epsilon\)_-stable_ if the number of unstable edges is at most \(\epsilon|M|\).

Denote by \(\Delta\) the maximum degree of a node of G. That is, \(\Delta\) is the maximum number of acceptable partners for one participant. In a social network, the bound on the degree of a node _v_ may not necessarily be due to _v_ being particularly picky; the bound may just reflect the fact that the number of participants, information about whom is available (or comprehensible, or relevant) to _v_, is limited. Throughout this work we assume that \(\Delta\) is a constant.

## 1.2 Model of Distributed Computing

We view G as the communication graph of a distributed system: if \(\{u,v\}\in E\), then the node _u_ and the node _v_ can exchange messages.

Let _T_ be a constant that determines the trade-off between the stability and the running time. Initially, each node \(v\in R\cup B\) knows the following information: its colour (i.e., whether \(v\in R\) or \(v\in B\)), its degree _d(v_), and the constant _T_. The node _v_ has _d(v_) ports through which it can communicate with its neighbours; the ports are numbered according to _v_’s preferences.

