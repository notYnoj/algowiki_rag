## 1.2 Related Work

The concept of _balance_ for directed graphs is introduced by Ene et al. \[EMPS16\], who show that existing techniques for undirected flow-based problems can be translated to directed graphs that are approximately balanced. For graphs that are _perfectly_ balanced, namely the Eulerian graphs, Cohen et al. \[CKK<sup>+</sup>18\] use directed graph sparsification to obtain fast algorithms for solving directed Laplacian systems. Sparsification for approximately balanced graphs is systematically studied by Cen et al. \[CCPS21\], who obtain tight upper and lower bounds for various types of sparsification. All of these results are restricted to balanced graphs, and to the best of our knowledge, our work is the first to employ techniques from balanced graphs in the context of general directed graphs.

## 1.3 Preliminaries

Throughout the paper, all graphs are uncapacitated, either weighted or unweighted, and either directed or undirected. We refer to directed edges as _arcs_ and undirected edges as _edges_. The input directed graph to maximum flow is assumed to be _G_=(_V,E_), with vertices \(s,t\in V\) . We define a _flow_ from _s_ to _t_ as a set of arc-disjoint paths from _s_ to _t_ in _G_, and the _value_ of the flow is the number of paths in the set. The _residual graph G<sub>f</sub>_ is obtained from _G_ by flipping each arc along each path in _f_. The standard augmenting paths framework attempts to find a path from _s_ to _t_ in _G<sub>f</sub>_, called an _augmenting path_. If a path is found, then each arc along the path is flipped, and the flow _f_ is updated accordingly. Otherwise, if no path exists, then _f_ is a maximum flow, and the algorithm terminates.

A _cut_ is a bipartition (_S,V_\\_S_) of the vertex set into two non-empty subsets, represented as one of the sides \(S\subseteq V\) . The _boundary_ \(\partial S\) of the cut is the set of arcs/edges with exactly one endpoint in _S_. For a directed graph, the out-boundary \(\partial^+S\) is the set of arcs with only the tail in _S_, and the in-boundary \(\partial^-S\) is the set of arcs with only the head in _S_. For a weighted graph with weight function _w_, let \(w(\partial S)\) denote the total weight of arcs/edges in \(\partial S\), and define \(w(\partial^+S)\) and \(w(\partial^-S)\) similarly. For an unweighted graph, let \(|\partial S|\) denote the number of arcs/edges in \(\partial S\), and define \(|\partial^+S|\) and \(|\partial^-S|\) similarly.

## 1.4 Preprocessing the Graph

We first preprocess the graph as follows. First, add _m_ many parallel arcs (_t,s_), which does not affect the maximum flow from _s_ to _t_. Then, compute the strongly connected components of the new graph. If _s_ and _t_ do not belong to the same strongly connected component, then the existence of arc (_t,s_) implies that there is no path from _s_ to _t_, and the algorithm concludes that the maximum flow from _s_ to _t_ has value 0. Otherwise, discard all strongly connected components except the one containing _s_ and _t_, and solve the maximum flow problem on the remaining component. This operation is safe because there is no path from _s_ to _t_ that contains vertices outside the strongly connected component containing _s_ and _t_.

Let _G_ be the resulting graph after preprocessing. The lemma below ensures that any residual graph _G<sub>f</sub>_ remains strongly connected as long as the current flow is not maximum.

**Lemma 3.** _Let f be a flow from s to t in G that does not use any arc_ (_t,s). If there is a path from s to t in G<sub>f</sub>, then G<sub>f</sub> is strongly connected._

_Proof._ It suffices to show that \(\partial_{G_f}^+S\neq\emptyset\) for any cut \(S\subseteq V\) . By assumption, all arcs (_t,s_) in _G_ remain in _G<sub>f</sub>_, and there is a path from _s_ to _t_ in _G<sub>f</sub>_. If \(t\in S\) and \(s\notin S\), then the arcs (_t,s_)<tbc>

