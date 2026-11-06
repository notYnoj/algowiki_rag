# Maximum Common Subgraphs

3<tbc>

### 2 Finding maximum common subgraphs

We consider simple undirected graphs _G_=(_V,E_) with a finite vertex set _V(G_):=_V_ and an edge set _E(G_):=_E_. We write \(G\simeq H\) if the graphs _G_ and _H_ are isomorphic. A _"pure" subgraph_ of a graph _G_ is a graph _H_ satisfying \(V(H)\subseteq V(G)\) and \(E(H)\subseteq E(G)\). Moreover, _H_ is a _subgraph_ of _G_ if _G_ contains a pure subgraph \(H'\) such that \(H\simeq H'\). If _H_ is a subgraph of both _G_<sub>1</sub> and _G_<sub>2</sub>, then it is called a _common subgraph_. A common subgraph is a _maximum-vertex common subgraph (MVCS)_ of _G_<sub>1</sub> and _G_<sub>2</sub> if |_V(H_)| is maximized among all common subgraphs of _G_<sub>1</sub> and _G_<sub>2</sub>. Similarly, a _maximum-edge common subgraph (MECS) H_ is a common subgraph that maximizes |_E(H_)|. The latter definition naturally generalizes to common subgraphs of more than two graphs.

A classical method to find an MVCS of two graphs _G_<sub>1</sub> and _G_<sub>2</sub> is as follows \[11\]. First, compute the modular product _G_<sub>1</sub>⋆_G_<sub>2</sub> with vertex set \(V(G_1\star G_2):=V(G_1)\times V(G_2)\), where the edge set _E(G_<sub>1</sub>⋆_G_<sub>2</sub>) includes all pairs \(\{(u,v),(u',v')\}\) for which either \(\{u,u'\}\in E(G_1)\) and \(\{v,v'\}\in E(G_2)\) or \(\{u,u'\}\notin E(G_1)\) and \(\{v,v'\}\notin E(G_2)\). Each vertex (_u,v_) in a clique corresponds to vertex _u_ in _G_<sub>1</sub> and vertex _v_ in _G_<sub>2</sub>, and an edge \(\{(u,v),(u',v')\}\) in the clique implies that either both \(\{u,u'\}\) and \(\{v,v'\}\) are edges or both are non-edges in _G_<sub>1</sub> and _G_<sub>2</sub>, respectively. Therefore, we can find all maximal common induced subgraphs between two graphs by finding all maximal cliques in their modular product \[12\].

The modular product can naturally be generalized to more than two factors. However, the product is not associative in general, i.e. \((G_1\star G_2)\star G_3\unknown\unknown G_1\star(G_2\star G_3)\) may happen. To simplify notation, we use the convention that \(\star_{i=1}^nG_i:=(((G_1\star G_2)\star G_3)\cdots\star G_n)\) and that _v_=(_v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,...,v<sub>i</sub>,...,v<sub>n</sub>_):=(((_v_<sub>1</sub>_,v_<sub>2</sub>)_,v_<sub>3</sub>)_...,v<sub>i</sub>),...,v<sub>n</sub>_)\(\in V(\star_{i=1}^nG_i)\). Given \(G=\star_{i=1}^nG_i\), the _projection onto the i-th factor_ is the map \(p_i:V(G)\rightarrow V(G_i)\), defined by _p<sub>i</sub>_((_v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,...,v<sub>i</sub>,...,v<sub>n</sub>_))=_v<sub>i</sub>_. For a given subgraph \(H\subseteq G\), we often write _p<sub>i</sub>(H_) for the subgraph of _G<sub>i</sub>_ induced by the vertices _p<sub>i</sub>(v_) with \(v\in V(H)\).

As outlined above, an MVCS of _G_<sub>1</sub> and _G_<sub>2</sub> can be found by filtering all inclusion-maximal cliques in _G_<sub>1</sub>⋆_G_<sub>2</sub>. We aim to extend this idea to establish methods for:

(1) Finding an MVCS for more than two graphs.<tbc>

(2) Finding a _connected_ MVCS for more than two graphs.<tbc>

(3) Finding a (connected) MECS for two or more graphs.<tbc>

(4) Handling the MVCS and MECS problems for edge-labeled and vertex-labeled graphs, where common subgraphs are determined by retaining the respective labels.

For Task (1), assume that we want to compute an MVCS of the graphs _G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>n</sub>_. We first compute all inclusion-maximal cliques in _G_<sub>1</sub>⋆_G_<sub>2</sub> and store them in the set K. Then, for each \(K\in\mathcal{K}\), we consider the subgraphs \(H_K^i=p_i(K)\) in _G<sub>i</sub>_, \(1\le i\le 2\). By definition of the modular product, we have \(H_K^1\simeq H_K^2\) for each \(K\in\mathcal{K}\). We then collect a representative for each \(K\in\mathcal{K}\), defined as \(H_K:=H_K^2\), and store all representatives in the set H<sub>1,2</sub>. For each

