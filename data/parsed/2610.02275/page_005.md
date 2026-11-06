In every case, _f<sub>s</sub>_ and _f_<sub>_s_+1</sub> would be compatible, contradicting their adjacency on _P_. Hence consecutive sets touch. Each _R<sub>s</sub>_ induces a connected subgraph, and therefore \(G[\bigcup_{s=0}^tR_s]\) is connected. It contains \(\ell_i\) and \(\ell_j\) and avoids \(N_G[\ell_k]\). Thus, there is an \(\ell_i\)-\(\ell_j\) path avoiding \(N_G[\ell_k]\).

The indices _i,j,k_ were arbitrary. Therefore, \(\{\ell_1,\ell_2,\ell_3\}\) is an asteroidal triple in _G_. Hence, if _A<sub>G</sub>_ contains an asteroidal triple, then so does _G_, proving the contrapositive.

### 3.3 Algorithm and running time

Given an AT-free graph _G_, construct _A<sub>G</sub>_. By Theorem 3, _A<sub>G</sub>_ is AT-free, and by Lemma 2, \(\rho_\mathrm{e}^\mathrm{o}(G)=\alpha(A_G)\). We compute a maximum independent set of _A<sub>G</sub>_ using the algorithm of Broersma et al. \[6\] and translate it back into an edge open packing of _G_ as in the proof of Lemma 2.

**Theorem 4.** _The_ Maximum Edge Open Packing _problem can be solved in O(n_<sup>2</sup>+_m_<sup>4</sup>) _time on an AT-free graph with n vertices and m edges. In particular, the running time is O(n_<sup>8</sup>) _when expressed only in terms of n._

_Proof._ The graph _A<sub>G</sub>_ has one vertex for each oriented edge of _G_, so |_V(A<sub>G</sub>_)|=2_m_. An adjacency matrix of _G_ can be constructed in _O(n_<sup>2</sup>) time, after which compatibility of two oriented edges can be tested in constant time. Thus, _A<sub>G</sub>_ can be constructed in _O(n_<sup>2</sup>+_m_<sup>2</sup>) time.

The algorithm of Broersma et al. \[6\] solves Maximum Independent Set on an _N_-vertex AT-free graph in _O(N_<sup>4</sup>) time. Applying it with _N_=2_m_ takes _O(m_<sup>4</sup>) time. Translating the independent set back into an edge open packing takes _O(m_) time. The total running time is therefore _O(n_<sup>2</sup>+_m_<sup>4</sup>), which is _O(n_<sup>8</sup>) because _m=O(n_<sup>2</sup>).

## 4 Maximum Edge Open Packing in Chordal Graphs

In this section, we give a polynomial-time algorithm for chordal graphs. Let _G_=(_V,E_) be a chordal graph on _n_ vertices. If _G_ is disconnected, we solve the problem independently on its connected components and add the optimum values. We therefore assume throughout the description that _G_ is connected.

Let T be a clique tree of _G_. From T , we construct a nice rooted tree decomposition (_T,_B) whose root and leaves have empty bags and whose nodes are leaf, introduce, forget, or join nodes. Along an edge between two maximal cliques, vertices are first forgotten down to the intersection and then introduced up to the other clique. Join nodes use copies of one maximal clique. Thus, every bag of the nice decomposition is a subset of a maximal clique and is therefore a clique. The standard transformation has _O(n_<sup>2</sup>) nodes \[16\].

For \(t\in V(T)\), let _B<sub>t</sub>_ be its bag, let _T<sub>t</sub>_ be the subtree rooted at _t_, and let _G<sub>t</sub>_ be the subgraph of _G_ induced by all vertices occurring in bags of _T<sub>t</sub>_. We use the following separation properties. If _t_ is an introduce node with child \(t'\) and \(B_t=B_{t^\prime}\cup\{v\}\), then _v_ has no neighbour in \(V(G_{t^\prime})\backslash B_{t^\prime}\). If _t_ is a forget node with child \(t'\) and \(B_t=B_{t^\prime}\backslash\{v\}\), then _v_ has no neighbour outside _V(G<sub>t</sub>_). If _t_ is a join node with children _t_<sub>1</sub>_,t_<sub>2</sub>, then \(V(G_{t_1})\cap V(G_{t_2})=B_t\), and there is no edge between _V(G_<sub>_t_<sub>1</sub></sub>)\\_B<sub>t</sub>_ and _V(G_<sub>_t_<sub>2</sub></sub>)\\_B<sub>t</sub>_.

**Observation 5.** _Let D be an edge open packing of G. Every clique of G contains at most two vertices of V(D), and every edge of G_\[_V(D_)\] _belongs to D._

Both assertions follow from Observation 1: _G_\[_V(D_)\] is a star forest, so it has no triangle, and all its edges are selected.

### 4.1 States

At every node _t_, a state records the vertices of _B<sub>t</sub>_ that are intended to be endpoints of selected edges in the final packing, together with their roles in the partial induced-star forest. We call these vertices _active_. An active vertex is either already incident with a selected edge in the processed part or is pending and must become incident with a selected edge later. Since _B<sub>t</sub>_ is a clique, Observation 5 implies that a state has at most two active vertices.

The possible states are the following.

• The empty state \(\varnothing\) means that no vertex of _B<sub>t</sub>_ is active.<tbc>

• A singleton state \((x,\lambda)\) has \(x\in B_t\) and \(\lambda\in\{P,C,L\}\). Label _P_ means that _x_ is pending and is not yet incident with a selected edge in the processed part. Label _C_ means that _x_ is the centre of a<tbc>

