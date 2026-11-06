**Lemma 2.2.** _Let_ T _be a tree with weight function w, and let_ A, B _be connected subgraphs of_ T _. If_ A _and_ B _each contain a centroid of_ (T_,w), and_ \(V(\mathcal{A})\cap V(\mathcal{B})\neq\emptyset\)_, then_ \(V(\mathcal{A})\cap V(\mathcal{B})\) _contains a centroid of_ (T_,w)._

_Proof._ Let \(c_1\in\mathcal{A}\) and \(c_2\in\mathcal{B}\) be centroids. If \(c_1\in V(\mathcal{A})\cap V(\mathcal{B})\) or \(c_2\in V(\mathcal{A})\cap V(\mathcal{B})\), we are done. Otherwise, there must be a vertex _c_ on the path between _c_<sub>1</sub> and _c_<sub>2</sub> such that \(c\in V(\mathcal{A})\cap V(\mathcal{B})\). We show that _c_ is a centroid.

Let \(\mathcal{M}\in\mathbb{C}(\mathcal{T}-c)\). Note that either \(c_1\notin V(\mathcal{M})\) or \(c_2\notin V(\mathcal{M})\). Assume w.l.o.g., that \(c_1\notin V(\mathcal{M})\). Then \(V(\mathcal{M})\subseteq V(\mathcal{M}')\) for some component \(\mathcal{M}'\in\mathbb{C}(\mathcal{T}-c_1)\), and so \(w(\mathcal{M})\le w(\mathcal{M}')\le\frac{1}{2}w(\mathcal{T})\). This concludes the proof.

## Projection of a search tree.

For a rooted tree _T_ and a vertex \(v\in V(T)\), we denote by `Path`_<sub>T</sub>(v_) the set of vertices on the path in _T_ from `root`(_T_) to _v_, including both endpoints. The proofs of our upper bounds require the following notion of _projection_ of a search tree.

**Theorem 2.1.** _Let T be a search tree on_ T _and_ H _a connected subgraph of_ T _. There is a unique search tree T_|<sub>H</sub> _on_ H _such that for every_ \(v\in V(\mathcal{H})\),

\(\mathtt{Path}_{T|_\mathcal{H}}(v)=\mathtt{Path}_T(v)\cap V(\mathcal{H}).\)

**Definition 2.1** (Projection)**.** _Let T be a search tree on_ T _and_ H _a connected subgraph of_ T _. We call T_|<sub>H</sub>_, whose existence is established by Theorem 2.1, the projection of T to_ H.

An equivalent notion of projection was used by Cardinal, Langerman and Perez-Lantero \[CLP18\] without explicitly stating Theorem 2.1, and a closely related notion was used by Cicalese, Jacobs, Laber and Molinaro \[CJLM14\] in the edge-query setting. In Appendix A we prove Theorem 2.1, present the definition of a projection used by Cardinal et al. and show that the two definitions are equivalent.

## Median and centroid.

A certain concept of a _median vertex_ of a tree has been used previously in the literature. If T is a tree with positive vertex weights and positive edge weights, then the median of T is the vertex _v_ minimizing the quantity \(\sum_{u\neq v}w(u)\cdot d(u,v)\). Here _w(u_) is the weight of the vertex _u_, and _d(u,v_) is the distance from _u_ to _v_, i.e., the sum of the edge weights on the path from _u_ to _v_. We show (proof in Appendix B) that if all edge-weights are 1, then medians are precisely centroids.

**Lemma 2.3.** _Let_ T _be a graph and w be a weight function on V_(T)_. For each_ \(u\in V(\mathcal{T})\)_, define_ \(W(u)=\sum_{v\in V(\mathcal{T})}d_\mathcal{T}(u,v)\cdot w(v)\)_, where d_<sub>T</sub>(_u,v_) _denotes the number of edges on the path from u to v in_ T _. Then_ \(c\in V(\mathcal{T})\) _is a centroid of_ (T_,w_) _if and only if W(c_) _is minimal._

## Breaking ties.

Our lower bounds require the following tie-breaking procedure, with proof in Appendix C.

**Lemma 2.4.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _a weight function and let C be a centroid tree of_ (T_,w). For every_ \(\varepsilon>0\) _there exists a weight function_ \(w':V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _such that C is the unique centroid tree of_ \((\mathcal{T},w')\) _and_ \(\|w'-w\|_\infty<\varepsilon\).

## Contractions in weighted trees.

Let T be a tree, let \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) be a weight function, and let {_u,v_} be an edge of T . Then _contracting_ {_u,v_} produces a tree \(\mathcal{T}'\) and a weight function \(w'\), defined as follows. The tree \(\mathcal{T}'\) is obtained from T by removing _u_ and _v_, adding a new vertex _s_, and setting \(N_{\mathcal{T}^\prime}(s)=N_\mathcal{T}(u)\cup N_\mathcal{T}(v)-\{u,v\}\). The weight function \(w'\) is defined as \(w'(s)=w(u)+w(v)\) and \(w'(x)=w(x)\) for \(x\in V(\mathcal{T}')-\{s\}\).

The lemma below shows that contractions essentially preserve centroids.

**Lemma 2.5.** _Let_ T _be a tree and_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\) _be a weight function, and let_ \(\mathcal{T}',w'\) _be obtained from_ T_,w by contracting the edge_ {_u,v_} _into a new vertex s. Then s is a centroid of_ \((\mathcal{T}',w')\) _if and only if u or v is a centroid of_ (T_,w); and x is a centroid of_ \((\mathcal{T}',w')\) _if and only if x is a centroid of_ (T_,w), for each_ \(x\in V(\mathcal{T}')-\{s\}\).

