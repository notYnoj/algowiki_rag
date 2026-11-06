## 3 The Framework

In this section we describe the input/output guarantees of all the subroutines used in our algorithm, as well as some of the algorithms themselves.

### 3.1 Basic Subroutines

**Lemma 3.1** (Dijkstra)**.** _There exists an algorithm_ Dijkstra(_G,s_) _that takes as input a graph G with non-negative edge weights and a vertex_ \(s\in V\) _and outputs a shortest path tree from s in G. The running time is O(m+n_log(_n_)).

It is easy to see that if _G_ is a DAG (Directed Acyclic Graph), computing a price function \(\phi\) such that \(G_\phi\) has non-negative edge weights is straightforward: simply loop over the topological order _v_<sub>1</sub>_,...,v<sub>n</sub>_ and set \(\phi(v_i)\) so that all incoming edges have non-negative weight. The lemma below generalizes this approach to graphs where only the "DAG part" has negative edges.

**Lemma 3.2** (FixDAGEdges)**.** _There exists an algorithm_ FixDAGEdges(_G,_P) _that takes as input a graph G and a partition_ P:={_V_<sub>1</sub>_,V_<sub>2</sub>_,..._} _of vertices of G such that_

1. _for every i, the induced subgraph G_\[_V<sub>i</sub>_\] _contains no negative-weight edges, and_

_2. when we contract every V<sub>i</sub> into a node, the resulting graph is a DAG (i.e. contains no cycle). The algorithm outputs a price function_ \(\phi:V\rightarrow\mathbb{Z}\) _such that_ \(w_\phi(u,v)\ge 0\) _for all_ \((u,v)\in E\)_. The running time is O(m+n)._

_Proof sketch._ The algorithm is extremely simple: it loops over the SCCs _V<sub>i</sub>_ in topological order, and when it reaches _V<sub>i</sub>_ it sets the same price \(\phi(v)\) for every \(v\in V_i\) that ensures there are no non-negative edges entering _V<sub>i</sub>_; since all \(\phi(v)\) are the same, this does not affect edge-weights inside _V<sub>i</sub>_. We leave the pseudocode and analysis for Section B in the appendix.

The next subroutine shows that computing shortest paths in a graph _G_ can be done efficiently as long as \(\eta(v)\) is small on average (see Definition 2.4 for \(\eta(v)\)). Note that this subroutine is the reason we use the assumption that every vertex has constant out-degree (Assumption 2.1).

**Lemma 3.3.** (ElimNeg) _There exists an algorithm_ ElimNeg(_G,s_) _that takes as input a graph G_=(_V,E,w_) _in which all vertices_ \(v\neq s\) _have constant out-degree and a source_ \(s\in V\) _that can reach all vertices in V. The algorithm outputs a price function_ \(\phi\) _such that_ \(w_\phi(e)\ge 0\) _for all_ \(e\in E\) _and has running time_ \(O(log(n)\cdot(n+\sum_{v\in V}\eta_G(v;s)))\) _(Definition 2.4); note that if G contains a negative-weight cycle then_ \(\sum_{v\in V}\eta_G(v;s)=\infty\) _so the algorithm will never terminate and hence not produce any output._

_Proof sketch._ By Lemma 2.7, in order to compute the desire price function, it suffices to describe how ElimNeg(_G_) computes dist_<sub>G</sub>(s,v_) for all \(v\in V\) , where _s_ is the input source to ElimNeg(_G,s_).

The algorithm is a straightforward combination of Dijkstra’s and Bellman-Ford’s algorithms. The algorithm maintains distance estimates _d(v_) for each vertex _v_. It then proceeds in multiple iterations, where each iteration first runs a Dijkstra Phase that ensures that all non-negative edges are relaxed and then a Bellman-Ford Phase ensuring that all negative edges are relaxed. Consider a vertex _v_ and let _P_ be a shortest path from _s_ to _v_ in _G_ with \(\eta_G(v;s)\) edges of _E<sup>neg</sup>(G_). It is easy to see that \(\eta_G(v;s)+1\) iterations suffice to ensure that _d(v_)=dist_<sub>G</sub>(s,v_). In each of these iterations, _v_ is extracted from and added to the priority queue of the Dijkstra Phase only _O_(1) times. Furthermore, after the \(\eta_G(v;s)+1\) iterations, _v_ will not be involved in any priority queue operations. Since the bottleneck in the running time is the queue updates, we get the desired time bound of \(O(log(n)\cdot\sum_{v\in V}(\eta_G(v;s)+1))=O(log(n)\cdot(n+\sum_{v\in V}\eta_G(v;s)))\).

This completes the proof sketch. The full proof can be found in Appendix A.

