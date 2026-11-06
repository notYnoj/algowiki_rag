## 2 Notations and Preliminaries

In this section, we introduce the terminologies and computation models that will be used throughout the paper. Due to brevity, some of the proofs are deferred to Section A.

### Graph.

Let _G_=(_V,E_) denote a graph with a designated terminals _s_ and _t_. Unless stated otherwise, a graph is assumed to be undirected and unweighted. For two graphs _G_=(_V,E_) and \(G'=(V,E')\) on the same vertex set, we denote \(G\cup G'=(V,E\cup E')\) as the graph obtained by combining the edges of _G_ and \(G'\). We also write \(G\cup e\) for the addition of a single edge _e_ to _G_.

In this work, we also study graphs whose edge sets comprise both undirected unweighted edge (i.e. unit-weight) and directed weighted edges. We call a graph of this type a _mixed graph_, denoted by G=(_G,F_) where _G_ is undirected unweighted graph, and _F_ is a directed graph with bounded weights. For a directed edge, we write (_a,b_) to represent an edge from _a_ to _b_. For an undirected edge, we may write it as either (_a,b_) or (_b,a_) interchangeably, with no implied direction.

For a weighted graph _G_=(_V,E_), we denote \(w_G:E\rightarrow\mathbb{Z}_{\ge 0}\) as the weight function that maps an edge of _G_ to its positive integral weight. The total weight of any edge set \(E'\subseteq E\) is given by \(w_G(E'):=\sum_{e\in E^\prime} w_G(e)\). Also denote _w(G_) or |_G_| to be the total weight of edges in the graph.

Let _G_=(_V,E<sub>G</sub>_) and _H_=(_V,E<sub>H</sub>_) be two graphs on the same set of vertices which may be directed or weighted. We say _H_ is a _subgraph_ of _G_, denoted \(H\unknown G\), iff \(E_H\subseteq E_G\), and \(w_H(e)\le w_G(e)\) for any edge \(e\in E_H\). When both _G_ and _H_ are undirected unweighted, the second condition is not necessary.

For any graph _G_=(_V,E_) and \(U\subseteq V\) , denote _G_\[_U_\] to be an induced subgraph of _G_ on vertex set _U_. For a partition (_V_<sub>1</sub>_,...,V<sub>z</sub>_) of _V_ , denote \(G\langle V_1,..,V_z\rangle\) to be a (weighted) graph over _z_ super- vertices resulted from contracting each vertex set _V<sub>i</sub>_ into one super-vertex. Equivalently, we can view \(G\langle V_1,..,V_z\rangle\) as _G_ with all edges within each _G_\[_V<sub>i</sub>_\] removed.

### Flow and Maximum Flow.

Let _G_=(_V,E_) be a (possibly directed weighted) graph with a designated source _s_ and sink _t_. A _unit of s-t flow_ (or simply a _unit flow_) is a directed path from _s_ to _t_. We say a directed graph _F_ is a _flow graph of value f_ if and only if _F_ can be exactly partitioned into _f_ unit flows. We denote MaxFlow(_G_) as the value of _G_’s largest flow subgraph. When _G_ is undirected unweighted, MaxFlow(_G_) corresponds to the maximum number of edge-disjoint _s-t_ paths that can be packed into _G_.

**Lemma 2.1** (Lemma 5.4 of \[RSW18\])**.** _Let F_=(_V,E_) _be a non-circular flow graph of value f with n vertices. Let W be the maximum weight of edges in F. Then, we have_ \(w(F)\le O(n\sqrt{fW})\).

The following lemma bounds the number of edges in a flow graph.

**Lemma 2.2.** _Let F_=(_V,E_) _be a non-circular flow graph of value f with n vertices. Then, F contains_ \(|E|\le O(n\sqrt{f})\) _edges._

### Residual Graph.

Given an undirected unweighted graph _G_ and a flow subgraph \(F\unknown G\), the _residual graph_ of _G_ induced by _F_, denoted _G<sub>F</sub>_, is obtained by replacing each edge in _F_ with its reverse edge, assigned a weight of 2. Notably, _G<sub>F</sub>_ is a mixed graph consisting of the undirected unweighted part _G_\\_F_, and a directed weighted part which is a reversal of _F_ with weight 2 on each edge (see Figure 1 for an illustration).

**Proposition 2.3.** _For any graph G and a flow subgraph_ \(F\unknown G\)_, we have:_<tbc>

\(MaxFlow(F)+MaxFlow(G_F)=MaxFlow(G).\)

