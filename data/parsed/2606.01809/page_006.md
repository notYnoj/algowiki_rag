the online setting the sequence is revealed on-the-go. We use _G_=(_V,E,w_) to denote the input graph, where _V_ is the set of vertices with _n_=|_V_|, _E_ is the set of edges and \(w:E\rightarrow\mathbb{R}\) is the edge weight function. Assume constant time arithmetic on the weights. We let _d<sub>G</sub>(u,v_) denote the shortest path distance from _u_ to _v_ in _G_ and assume that all shortest paths at any time in _G_ are unique. This can be ensured using the deterministic perturbation technique in \[14\]).

Finally, we introduce the concept of full persistence.

**Definition 4.1** (Fully-persistent)**.** _We say a data structure undergoing an update sequence is_ fully- persistent _if every version of the data structure can be accessed and modified._

## 5 Online Incremental DDG

In this section, we show the following result which we will use in our reductions in section D and section C to get the main results of the paper.

**Theorem 5.1.** _Given input graph G, and an r-capped recursive decomposition_ R _of G with roots G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>k</sub>._

_Then, there exists a deterministic data structure that, given any G<sub>i</sub>, maintains the DDGs of all pieces in the tree rooted at G<sub>i</sub>. Its preprocessing time is_ \(\tilde{O}(n)\) _and it handles each edge weight decrease in G<sub>i</sub> in worst case update time_ \(\tilde{O}(\sqrt{r})\)_. After every update, a query for the weight of any DDG edge of any piece in the tree rooted at G<sub>i</sub> can be answered in worst-case time_ \(\tilde{O}(1)\).

_The data structure is fully-persistent._

In our construction, we focus on the first part of the theorem statement, and only at the end of this section we show how to modify our data structure to make it persistent.

### 5.1 The Data Structure

### Preliminaries.

First, we need some additional notation. To avoid clutter, let _H=G<sub>i</sub>_. We let the updates to _H_ be encoded by tuples \(\{(e^1,\omega^1),(e^2,\omega^2),\dots\}\) where _e<sup>i</sup>_ is an edge in _H_, and \(\omega^i\) its new edge weight. In this section, we also need to argue about the embedding of _G_. We assume that we are given a combinatorial planar embedding, also often called rotation system, that specifies for each vertex _v_ in _G_, a cyclic order _e_<sub>0</sub>_,e_<sub>1</sub>_,...,e_<sub>_k_-1</sub> of the edges incident to _v_, such that in the planar embedding every _e<sub>i</sub>_ is in between _e_<sub>_i_-1</sub> and _e_<sub>_i_+1</sub>. We define a sharpest right-turn (left-turn) at _v_ from an edge _e_ to be the first out-going edge \(e'\) incident to _v_ in counter-clockwise (clockwise) order starting in _e_.

We further let for each piece _P_ (where we only talk for the rest of this section about pieces _P_ in the tree rooted at _H_), _P<sup>t</sup>_ refer the version of the piece _P_ after the first _t_ updates have been applied to _H_. In particular _P_<sup>0</sup> is the initial piece.

For each piece _P_, we let _h(P_)={_h_<sub>1</sub>(_P),h_<sub>2</sub>(_P),...,h<sub>s<sub>P</sub></sub>(P_)} be the constant number of holes such that each vertex in \(\partial P\) is on some such hole. To ease indexing and avoid clutter, we allow _h<sub>i</sub>(P_) for any positive _i_, and let it refer to the \(h_{i^\prime}(P)\) such that \(i'\) is the unique integer in \[1_,s<sub>h</sub>_\] derived from subtracting a multiple of _s<sub>h</sub>_ from _i_.

Further, for each hole \(h\in h(P)\), we let _Q(h_) denote a cyclic ordering _v_<sub>1</sub>(_h),v_<sub>2</sub>(_h),...,v<sub>s<sub>h</sub></sub>(h_) of the (boundary) vertices of _h_ such that the interior of _h_ is to the right when traversing the vertices in this order. We also abuse notation slightly and denote by \[_v<sub>i</sub>(h),v<sub>j</sub>(h_)\] for \(1\le i\le j\le s_h\) the subset {_v<sub>i</sub>(h),v_<sub>_i_+1</sub>(_h),...,v<sub>j</sub>(h_)} of _Q(h_) when the context is clear. Further, we also define a _wrapped_<tbc>

