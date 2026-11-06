_Additionally, if each prior instance G<sub>i</sub> is equipped with a multiset of cost-distance pairs_ \(W_i:=\{w_1^{(i)},\dots w_{n-1}^{(i)}\}\)_, we can explicitly output the corresponding spanning tree in H in_ \(\widetilde{O}(n^\omega)\) _time with high probability._

## 6.1 Negative Triangle

**Definition 6.4** (Negative Triangle)**.** An instance is defined by an undirected, edge-weighted graph _G_=(_V,E,w_), where \(w:E\rightarrow\mathbb{R}\) assigns a real weight to each edge. The objective is to determine whether there exist three vertices \(u,v,x\in V\) forming a triangle such that the sum of their edge weights is strictly negative: _w(u,v_)+_w(v,x_)+_w(x,u)\<_0.

Two problem instances _G_ and _H_ of Negative Triangle are isomorphic if their underlying graphs are isomorphic. Note that an isomorphism has to preserve edge weights. Therefore, Negative Triangle is closed under isomorphism.

In order to use Lemma 6.1, we have to find a way how to detect (or count) negative triangles via polynomial. To this end, we associate a formal variable _x<sub>w</sub>_ with every distinct edge weight _w_. The _triangle polynomial_ of _G_ is defined as:

\(P_\Delta(G):=\sum_{w_1\le w_2\le w_3}c_{w_1,w_2,w_3}(G)x_{w_1}x_{w_2}x_{w_3}\)

where _c_<sub>_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub></sub>(_G_) is the exact number of triangles in _G_ whose edges possess the weight multiset {_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub>}. See Figure 1. We now, obtain that \(P_\Delta(G)\) encodes all different kinds of triangles inside of _G_ and thus especially the negative triangles.

**Lemma 6.5.** _If G and H are two graphs such that_ \(P_\Delta(G)\equiv P_\Delta(H)\)_, then G contains a negative triangle if and only if H contains a negative triangle._

_Proof._ If \(P_\Delta(G)\equiv P_\Delta(H)\) then the coefficients of every corresponding monomial match exactly, i.e. _c_<sub>_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub></sub>(_G_)=_c_<sub>_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub></sub>(_H_) for all combinations of weights. Consequently, _G_ contains a weight combination with _c_<sub>_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub></sub>(_G)\>_0 and _w_<sub>1</sub>+_w_<sub>2</sub>+_w_<sub>3</sub>_\<_0 if and only if _H_ contains the exact same number of such negative triangles.

_Proof of Theorem 6.2._ Let S:={_G<sub>i</sub>_=(_V<sub>i</sub>,E<sub>i</sub>,w<sub>i</sub>_)}<sub>_i_=1_...k_</sub> be a database of prior instances and assume that for each \(i\in[k]\) we are given _OPT(G<sub>i</sub>_) that indicates whether _G<sub>i</sub>_ contains a negative triangle.

**Preprocessing:** Given S, we first compute a prime number \(p\ge 3k^2n^{log(n)}\) and construct a finite field F_<sub>p</sub>_. Note that all basic operations in F_<sub>p</sub>_ can be performed in time \(O(logp)=\widetilde{O}(1)\). Next, we assign arbitrarily a unique non-zero element in F_<sub>p</sub>_ to each edge-weight of the graphs _G<sub>i</sub>_ and store the edge-weights together with the corresponding field elements in a binary search tree. Formally, we construct a function \(\text{enc}_\mathcal{S}:\mathbb{R}\rightarrow\mathbb{F}_p\cup\{\perp\}\) that, on input _x_, either outputs an unique element in F_<sub>p</sub>_ if _x_ is the weight of some graph in S, or returns \(\perp\) otherwise. Note that enc<sub>S</sub> can be computed in time \(O(k\cdot n^2\cdot logp)\), and evaluating enc<sub>S</sub> on some _x_ takes time \(O(log(kn^2)\cdot logp)=\widetilde{O}(1)\).

Given a graph _G<sub>i</sub>_, we write enc<sub>S</sub>(_G<sub>i</sub>_) for graph where each edge weight _w_ was replaced with enc<sub>S</sub>(_w_). This can be done in time \(\widetilde{O}(kn^2)\).

We construct a \((k\cdot n^2)\)-wise independent family of hash functions \(h:\mathbb{F}_p\rightarrow\mathbb{F}_p\) using \[Vad12, Construction 3.32\]. Concretely, we sample a random polynomial over F_<sub>p</sub>_ of degree at most \(k\cdot n^2-1\). Note that such a hash function can be constructed in time \(O(k\cdot n^2)\). Give an edge-weight _w_, we define _r(w_):=_h_(enc<sub>S</sub>(_w_)). For a graph _G<sub>i</sub>_, we write _r(G<sub>i</sub>_) for the graph obtained by replacing each edge weight _w_ with _r(w_).

Let \(x_1,\dots,x_m\in\mathbb{F}_p\), where \(m\le k\cdot n^2\), be a sequence of values. Using the Fast Fourier Transformation, we can evaluate _h(x<sub>i</sub>_) for all _i_ in time \(\widetilde{O}(k\cdot n^2)\). Thus, we can compute \(\widetilde{G}_1:=\)<tbc>

