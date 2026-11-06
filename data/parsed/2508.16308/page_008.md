<tbc>**Edge Gadget.** The edge gadget _e_<sub>{_u,v_}</sub> is constructed by adding additional vertices {(_u,v,_1),(_u,v,_2)_,...,(u,v,k_)} and edges between them such that these vertices form a _k_-clique. Moreover, the vertex _u_ is made adjacent to (_u,v,_1),(_u,v,_2)_,...,_ and (_u,v,k_-1) and the vertex _v_ is adjacent to (_u,v,k_). See Figure 2 for an example.

The transformation trivially runs in polynomial time. We now prove the following property of the graph \(G'\).

**Lemma 2.** _Any k-partial k-coloring_ \(\gamma\) _of_ \(G'\) _satisfies that_ \(\gamma(u)\neq\gamma(v)\) _for each edge_ \(\{u,v\}\in E(G)\).

_Proof._ By the construction of the edge gadget _e_<sub>{_u,v_}</sub>, for each \(i\in[k]\), \(deg_{G^\prime}((u,v,i))=k\), therefore by the definition of _k_-partial coloring, the vertex (_u,v,i_) must be properly colored with respect to all its neighbors. By the fact that the set {(_u,v,_1)_,...,(u,v,k_)} forms a _k_-clique and that the vertex _u_ is adjacent to all vertices of the _k_-clique except (_u,v,k_), the only possibility is that \(\gamma(u)=\gamma((u,v,k))\). Since (_u,v,k_) is adjacent to _v_ and has to be properly colored with respect to it, the claim immediately follows.

The next claim proves the correctness of the reduction.

**Lemma 3.** _The graph G is properly k-colorable if and only if the graph_ \(G'\) _is k-partially k-colorable._

_Proof._ Let us assume that _G_ is properly _k_-colorable and let \(\gamma\) be such a coloring of _G_. We define a coloring \(\gamma'\) on \(G'\) by extending the coloring of \(\gamma\) on the vertices of _e_<sub>{_u,v_}</sub> for each edge {_u,v_} of _G_ as follows. Assign \(\gamma'((u,v,k)):=\gamma(u)\). For the rest of the vertices, assign each vertex with a unique color from the palette \([k]\backslash\{\gamma(u)\}\). The resultant coloring \(\gamma'\) is a proper coloring and therefore, a _k_-partial _k_-coloring of \(G'\).

V

E {u,v}
u
v

Figure 1: A nontrivial obstruction for 3-partial 3-coloring, showing an example of a graph with \(\Delta_E=3\) which does not admit a proper 3-coloring, and therefore, a 3-partial 3-coloring. Also, observe that for this instance, \(\Delta=4\) and therefore, \(\Delta_E<\Delta\).

Figure 2: The edge gadget _e_<sub>{_u,v_}</sub> with _k_=5 (in red circle, connected with gray edges to the vertices _u_ and _v_). Vertices _u_ and _v_ are forced to take different colors.

