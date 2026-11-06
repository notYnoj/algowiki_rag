## 2.2 Algorithms via Weisfeiler-Leman (WL) Coloring (Details in Sections 7 and 8)

We sketch an elementary argument here, designed to be accessible to readers unfamiliar with WL coloring, with full details deferred to Section 7. An alternative, more concise proof based on a more general perspective is provided in Section 8.

We use Constrained Shortest Path (CSP) as our guiding example. In the preprocessing phase, we color the vertices of each prior graph _G<sub>i</sub>_ using the Weisfeiler-Leman (WL) color refinement process, which runs in time _O_((_n+m_)log_n_) \[CC82, PT87, BBG17\]. An essential property of the resulting coloring is that _every two vertices u and v that receive the same color will have identically colored neighborhoods_.

For example, in Figure 2, every pink vertex (labeled _p_) is adjacent to the target _t_ via an edge of attributes (length and cost) (5,2), to two cyan vertices (labeled _c_) via edges of attributes (2,4), and to one green vertex (labeled _g_) via an edge of attributes (3,3). Note that we initialize the process such that the source _s_ and target _t_ are assigned uniquely identifiable colors (red and blue in the example). The edge colors shown in the figure represent the edge attributes (and are not a result of the WL coloring).

Building on this property, we can easily establish the following claim (see the caption of Figure 2 for a concrete example).

**Claim 2.1** (Informal)**.** _Let G and H be two_ WL-equivalent _graphs, meaning that for every color c, both graphs contain exactly the same number of vertices assigned color c. If there exists an s-t walk (i.e., an s-t path that is not necessarily simple) W_=(_s=v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>p</sub>=t_) _in G, then there exists a corresponding walk_ \(W'=(s=v'_0,v'_1,\dots,v'_p=t)\) _in H such that, for every step_ \(i\in\{0,\dots,p-1\}\)_, the attributes (length and cost) of the edges_ (_v<sub>i</sub>,v_<sub>_i_+1</sub>) _and_ \((v'_i,v'_{i+1})\) _are identical._

_Proof Idea of Claim 2.1_ . Imagine placing a token at the source vertex _s_ in both graphs _G_ and _H_. At each step, we move the token in _G_ along the walk _W_ from a vertex of color _c_ to a neighbor of color \(c'\) via an edge with attribute \(\alpha\). The definition of WL-equivalence guarantees that the token in _H_ (which currently resides on a vertex of the exact same color _c_) has an identically attributed edge to a neighbor of color \(c'\). By matching these moves step-by-step, we successfully build the corresponding walk \(W'\) in _H_.

As an immediate consequence of the claim above, every two WL-equivalent graphs _G_ and _H_ yield the exact optimal value, i.e., _OPT(G_)=_OPT(H_).<sup>10</sup> Naturally, during the query phase, our algorithm simply computes the WL coloring of the query graph _H_, searches for a prior graph _G<sub>i</sub>_ that is WL-equivalent to _H_, and returns _OPT(G<sub>i</sub>_). This process achieves the desired near-linear query time. Additionally, if each prior graph _G<sub>i</sub>_ is equipped with its optimal path _P<sub>i</sub>_, we can efficiently reconstruct the corresponding optimal path in _H_ using the token-tracking procedure described in the proof sketch.

Other path-centric optimization problems, such as \(\ell_p\)-Shortest Path, Replacement Path, and Infinite-Duration Games, can be solved using a similar approach. Furthermore, we note that the Constrained Spanning Tree (CST) problem can be solved deterministically in _O(n_<sup>3</sup>log_n_) query time via 2-WL, a higher-dimensional variant of the WL coloring; see Section 8.

## 2.3 Lower Bounds (Details in Section 9)

### Graph Isomorphism with Promise.

Our starting point is the Graph Isomorphism (GI) problem itself, formulated within our model under a single prior instance (_k_=1). In the preprocessing phase,<tbc>

<sup>10</sup>To establish this, we rely on the standard fact that any _s-t_ walk can be transformed into a simple _s-t_ path by iteratively removing cycles, which does not increase the total cost or length of the walk since edge lengths and costs are non-negative.

