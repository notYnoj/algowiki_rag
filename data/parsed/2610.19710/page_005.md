_V_ can be partitioned into two sets _V_<sub>1</sub> and _V_<sub>2</sub> such that there are no edges between nodes in the same set.

**Modulo notation.** We use the modulo operation mod(_x,m_), which is the remainder of the division of _x_ and _m_. It always satisfies \(0\le mod(x,m)<m\). The modular congruence relation is written as \(x\equiv y(modm)\).

**Graph coloring problems.** A _k_-coloring of a graph _G_ is a labeling of the nodes of _G_ with _k_ colors such that no two adjacent nodes share the same color. More formally, given \(k\in\mathbb{N}^+\), a _k_-coloring of a graph _G_ is a function \(L:V(G)\rightarrow\{0,1,\dots,k-1\}\) such that for any edge \((u,v)\in E(G)\), we have \(L(u)\neq L(v)\). A graph is _k_-colorable if there exists a _k_-coloring of the graph.

Note that a bipartite graph is always 2-colorable, since you can assign color 0 to all the nodes in _V_<sub>1</sub> and color 1 to all the nodes in _V_<sub>2</sub>, where _V_<sub>1</sub> and _V_<sub>2</sub> are the two sets of the partition of _V_ . It trivially follows that a bipartite graph is also 3-colorable. In this work we focus on the problem of finding a 3-coloring of a bipartite graph.

**The dynamic-LOCAL model.** The input sequence in dynamic-LOCAL is an adversarially chosen sequence of graphs _G_<sub>0</sub>_,...,G<sub>N</sub>_, for any \(N\in\mathbb{N}\). The initial graph _G_<sub>0</sub> is the empty graph. At each step \(i\le N\), the adversary adds either an edge or a node to _G_<sub>_i_-1</sub> to obtain _G<sub>i</sub>_:=(_V<sub>i</sub>,E<sub>i</sub>_). The _edit area R<sub>i</sub>_ is the set of nodes in _G<sub>i</sub>_ such that the modification at step _i_ is in their distance-_T_ neighborhood, where _T_ is the locality. More formally,

where _G_[N_<sub>T</sub>(v_)] refers to the induced subgraph of all nodes at distance _T_ from _v_ in _G_. If a node _v_ is added at step _i_, then this means that _R<sub>i</sub>_:={_v_}. If an edge is inserted, _R<sub>i</sub>_ contains the nodes that have distance at most _T_ from both endpoints.

At every step _i_, a dynamic-LOCAL algorithm A has to produce a new labeling _Li_ that is correct for the given problem on the graph _G<sub>i</sub>_ with the constraint that _Li(v_)=_Li_<sub>_i_-1</sub>(_v_) if \(v\notin R_i\). The algorithm A can perform any computation to obtain the new labeling _Li_ and can keep an internal state in global memory between steps.

**The online-LOCAL Model.** In this model of computation, the nodes of an input graph _G_ are revealed sequentially with respect to an adversarial input order \(\sigma=(v_1,v_2,\dots,v_n)\). An algorithm A defined on this model has a global memory. At step 0, A initializes its memory with an empty graph _G_<sub>0</sub>. At each step \(i\ge 1\), A is given the _T_-hop neighborhood of the node _v<sub>i</sub>_, assigns a label _L(v<sub>i</sub>_) and updates its memory. Note that A cannot change the label given at step _i_ on future steps: once _v<sub>i</sub>_ is labeled, its label is fixed until the end of the computation. As an equivalent characterization, the algorithm computes the label _L(v<sub>i</sub>_) of node _v<sub>i</sub>_ as a function of the revealed graph \(G_i=G_{i-1}\cup G[\mathcal{N}_T[v_i]]\). The algorithm is correct if the final labeling _L_ is a correct labeling of _G_.

In [2], the authors present an _O_(log_n_) algorithm for 3-coloring bipartite graphs in the online-LOCAL model. We summarize the algorithm here, since our work can be considered a generalization of it.

The algorithm for 3-coloring bipartite graphs in the online-LOCAL model relies on pre-committing the label of nodes that are revealed but not labeled yet. This is possible

\(R_i:=\{v\in V_i|G_i\big[\mathcal{N}_T[v]\big]\neq G_{i-1}\big[\mathcal{N}_T[v]\big]\},\)

## 3 Previous work: The online-LOCAL upper bound

