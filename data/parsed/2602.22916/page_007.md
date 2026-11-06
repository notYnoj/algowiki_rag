<tbc>to exactly one face this overcomes the issue of overcounting (Challenge I). It extremely simplifies upon the approach of [12] for computing face-weights. Both [9] and [12] design other solutions that lead to either complicated or random algorithms to deal with the two challenges above.

We achieve the best of both worlds. Our algorithm is a combination of Lipton-Tarjan [15] and Ghaffari-Parter [9], that allows us to exploit the power of planar duality, which significantly simplifies the algorithm and its correctness compared to [12]. Concretely, we deal with Challenge I exactly like Lipton-Tarjan (i.e. every vertex transfers its weight to an arbitrary face it lies on), and we deal with Challenge II exactly like Ghaffari-Parter (i.e. using the fact that if there is no balanced node then there must be a critical node). Our contribution is in showing that this simple approach works, and can be implemented distributively.

Our correctness proof is inspired by the proofs of Lipton-Tarjan and Ghaffari-Parter. However, as we cannot triangulate the graph, we need to carefully handle the case of a critical node. In addition, we handle vertex-weighted graphs and adapt the proof to our weight assignment to faces. Finally, the distributed implementation is similar to both [9, 12] and uses very standard tools in distributed computing such as low-congestion shortcuts and part-wise aggregation.

## 4 A Deterministic Separator Algorithm

Our algorithm begins by transferring weights from vertices to faces using a simple procedure: Each vertex transfers its weight to one arbitrary face it belongs to. The weight of the face is then the total weight of vertices that transferred their weight to this face. Then, we find a node _f_ in the dual tree _T_<sup>∗</sup> that is either a balanced node or a critical node (where the weights are now on nodes of _T_<sup>∗</sup>). We prove that the fundamental cycle separator defined by _f_ is also a separator w.r.t. the original vertex-weights. A pseudocode of the algorithm is given in Algorithm 1. The algorithm mostly follows the (distributed) algorithm of [9]. The highlighted steps are the steps where we differ from [9]. For each such step we provide a proof of correctness. We assume that the input graph is _bi-connected_. This assumption can be removed as in [14]. We discuss this in more detail in the next section.

**Observation 1.** Let _G_ be a planar graph with vertex-weights \(w_\nu(\cdot)\), and _S_ a cycle in _G_. Then, the weight assignment where each vertex transfers its weight to an arbitrary face it belongs to satisfies<tbc>

\begin{tabular}{cc}
\multicolumn{2}{c}{**Algorithm 1:** Separator} \\
**Input:** & A bi-connected _D_-diameter graph _G_, a spanning tree tree _T_ of _G_, and a \(\frac{1}{12}\)-proper weight assignment \(w_\nu(\cdot)\) to the vertices of _G_. \\
**Output:** & A 3/4-balanced path separator _P_ of _G_ and an edge \(e\notin T\) s.t. \(P\cup\{e\}=C(T,e)\). (If \(e\notin G\), then, adding _e_ to _G_ preserves planarity). \\
1. & Compute the cotree _T_<sup>∗</sup>; \\
2. & Transfer vertex-weights to face-weights. I.e., to nodes of _T_<sup>∗</sup> (Observation 1); \\
3. & Detect a \((\frac{1}{4},\frac{3}{4})\)-balanced dual node or a \((\frac{1}{4},\frac{3}{4})\)-critical dual node (Lemma 4); \\
4. & Mark the separator path _P_ in _T_, and learn vertices \(u,v\in G\) s.t. \(S=P\cup\{e\}\), where _e_=(_u,v_) is possibly not in _G_ (Lemma 5) : \\
(a) & If a balanced dual node _f_ was found, mark _P_ and _e_=(_u,v_) where _P_ is the _u_- to-_v_ path in _T_ and _e_<sup>∗</sup>=(_f,_parent(_f_)) in _T_<sup>∗</sup> ; \\
(b) & If a critical dual node _f_ was found, find vertices _u,v_ on the face _f_ s.t. if _e_=(_u,v_) is added to _f_ it creates a balanced node in _T_<sup>∗</sup>. Mark the _u_-to-_v_ path _P_ in _T_ as before. \\
\end{tabular}

