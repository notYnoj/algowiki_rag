<tbc>for any \(d\ge 16\). Thus, the number of pebble sets is upper bounded by

\(2^{40\alpha\sqrt{d}}(60\alpha d\mathrm{log}(d))^{20\alpha\sqrt{d}\mathrm{log}(d)}\le 2^{40\alpha\sqrt{d}+20\alpha\sqrt{d}\mathrm{log}(d)\mathrm{log}(d^2)}\le 2^{80\alpha\sqrt{d}\mathrm{log}^2(d)}.\)

We can compute all such sets by iterating over all subsets _S_<sub>1</sub> of _C_<sub>he</sub> and all subsets _S_<sub>2</sub> of _C_<sub>li</sub> of size at most \(60\alpha d\mathrm{log}(d)\) in \(\mathcal{O}(2^{|C_\mathrm{he}|}\genfrac(){pt}{2}{|C_\mathrm{li}|}{20\alpha\sqrt{d}\mathrm{log}(d)}))\subseteq\mathcal{O}(2^{80\alpha\sqrt{d}\mathrm{log}^2(d)})\) time and computing \(S_1\cup S_2\) in O(_d_) time.

We are finally in a position to prove our result for _k_-Subgraph Scoring. To this end, recall that a request variant \(\pi\)-Request of locality \(\alpha_\pi\) takes a tuple \((d,G,B,x,S_\pi)\) as input where _B_=(_B_<sub>he</sub>_,B_<sub>li</sub>_,B_<sub>di</sub>) is partitioned into heavy, light, and discarded vertices, _G_ is a \(\alpha_\pi d\)- outerplanar graph, and (_B,x_) is almost measured with respect to _d_ and \(\alpha_\pi\). The output is a lookup table with an entry for each request \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\), where M is a pebble set for \((B,d,\alpha_\pi,x)\) and the output represents some solution where the vertices in the solution contained in \(B_\mathrm{he}\cup B_\mathrm{li}\cup B_\mathrm{di}\) is exactly M.

**Theorem 4.** _k_-Subgraph Scoring _can be solved in_ \(2^{\tilde{\mathcal{O}}(\sqrt{k})}n^{2.49}\) _time for planar input graphs._

_Proof._ We follow the recipe from above and first choose \(\gamma(d)=2^{240\sqrt{d}\mathrm{log}^2(d)}d^2\), \(\rho=2\), and \(\alpha_\pi=3\). The set \(S_\pi\) will contain the weight function _w_ and the cost function _c_ for all edges and vertices in the currently considered graph as well as the values \(\alpha_1,\alpha_2,\alpha_3\), and \(\beta\). A request \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) will be a pair \((\mathcal{M},\ell)\) where \(\ell\le d\). The answer for such a request should correspond to the maximum score achieved by a set of vertices intersecting _B_ in exactly M and of cost exactly \(\ell\). It is easy to verify that \(S_\pi\) can be maintained in O(_n_<sup>2</sup>) time and \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) can be computed in O(_nk_) time by iterating over all \(\ell\le d\) and copying the vertices in M. For the third step of our recipe, we define _k_-Subgraph Scoring Request as follows.

_k_-Subgraph Scoring Request

**Input:** An integer _d_, a directed 3_d_-outerplanar graph _G_=(_V,A_), a portal set _B_=(_B_<sub>he</sub>_,B_<sub>li</sub>_,B_<sub>di</sub>), an integer _x_, a vertex-cost function \(c:V\rightarrow\mathbb{N}\), an arc-weight function \(w:A\rightarrow\mathbb{R}\), and values \(\alpha_1,\alpha_2,\alpha_3,\beta\in\mathbb{R}\) such that (_B,x_) is almost measured with respect to _d_ and 3.<br>
**Task:** Output a lookup table that returns for each request \(r=(\mathcal{M},\ell)\) for each pebble set M for (_B,d,_3_,x_) and each \(\ell\le d\), the maximum value<tbc>

\(\alpha_1\big(\sum_{(u,v)\in Au,v\in S}w((u,v))\big)+\alpha_2\big(\sum_{(u,v)\in Au\in S,v\notin S}w((u,v))\big)+\alpha_3\big(\sum_{(u,v)\in Au\notin S,v\in S}w((u,v))\big)+\beta\big(\sum_{v\in S}w(S)\big)\)

<tbc>of any set _S_ of cost exactly \(\ell\) and where \(S\cap(B_\mathrm{he}\cup B_\mathrm{li}\cup B_\mathrm{di})=\mathcal{M}\) (or \(-\infty\) if no such set exists).

Next, we show that Requirement R1 of Theorem 3 holds, that is, there is an index _i_ such that we can remove the vertices from each layer \(i+j\cdot(3k+1)\) for any _j_ of any given BFS layering of the underlying undirected graph \(G_\downarrow\). To this end, note that the score of a set _S_ only depends on the vertices in _S_ and the arcs incident to _S_. For each vertex \(v\in S\) and any BFS-layering of \(G_\downarrow\), it holds that all arcs incident to _v_ have all their endpoints in at most 3 (consecutive) layers: the layer of _u_, the one before, and the one after. Thus, all arcs relevant for a set _S_ of size at most _k_ are incident to at most 3_k_ layers and if there are more than 3_k_ layers, then there is an index _i_ such that removing all layers _i+j_(3_k_+1) for any _j_ does not invalidate _S_. Moreover, no new solutions are<tbc>

