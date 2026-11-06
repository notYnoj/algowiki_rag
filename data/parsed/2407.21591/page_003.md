<tbc>remove an _arbitrary_ source _x<sub>i</sub>_ from _H<sub>i</sub>_ to get _H_<sub>_i_+1</sub>. Insert _x<sub>i</sub>_ into \(\pi\) using _finger search_ where the finger _p<sub>i</sub>_ is the farthest in-neighbour of _x<sub>i</sub>_ in _G_ along \(\pi\) (we find _p<sub>i</sub>_ by simply iterating over all in-neighbours of _x<sub>i</sub>_). We use \(\Theta(n+m+loge(P_G))\) time and \(\Theta(loge(P_G))\) queries. We consider this algorithm to be simpler. Our proof of correctness is considerably simpler, as it relies upon only one counting argument and one geometric observation.

## 2 Algorithm

The input is a directed acyclic graph _G_ with vertex set _X_=(_x_<sub>1</sub>_,...,x<sub>n</sub>_). This graph induces a partial order _P<sub>G</sub>_ where \(x_i\prec x_j\) if and only if there exists a directed path from _x<sub>i</sub>_ to _x<sub>j</sub>_ in _G_. The input also contains an oracle _O<sub>L</sub>_ that specifies a linear order _L_ over _X_. For any distinct _x<sub>i</sub>,x<sub>j</sub>_, an (oracle) query answers whether _x<sub>i</sub>\<<sub>L</sub>x<sub>j</sub>_. The goal is to output _X_ in its sorted order _L_.

We describe our algorithm. Our key observation is that the problem becomes significantly easier when we first extract a maximum-length directed path \(\pi\) from _G_. We iteratively remove an _arbitrary_ source _x<sub>i</sub>_ from \(H=G-\pi\) and insert it into \(\pi\). Once _H_ is empty, we return \(\pi\).

In our analysis, our logarithms are base 2 and _d_<sup>∗</sup>(_x<sub>i</sub>_) denotes the sum of the out-degree and the in-degree of a vertex _x<sub>i</sub>_ in _G_.

### Data structures.

We maintain a path \(\pi\) where for all vertices \(p,q\in\pi\): _p\<<sub>L</sub>q_ if and only if _p_ precedes _q_ in \(\pi\). We store the path \(\pi\) in a dynamic list order structure \(T_\pi\) which is a data structure that supports the following operations:

FingerInsert(_q<sub>i</sub>,x<sub>i</sub>_). Given vertices \(x_i\unknown\in\pi\) and \(q_i\in\pi\), insert _x<sub>i</sub>_ into \(\pi\) succeeding _q<sub>i</sub>_.

Search(_x<sub>i</sub>,p<sub>i</sub>,O<sub>L</sub>_). Given a vertex \(x_i\unknown\in\pi\) and a vertex \(p_i\in\pi\) with _p<sub>i</sub>\<<sub>L</sub>x<sub>i</sub>_. Return the farthest vertex _q<sub>i</sub>_ along \(\pi\) where _q<sub>i</sub>\<<sub>L</sub>x<sub>i</sub>_. Let _d<sub>i</sub>_ denote the number of vertices on the subpath from _p<sub>i</sub>_ to _q<sub>i</sub>_ along \(\pi\). We want to use _O_(1+log_d<sub>i</sub>_) time and queries to _O<sub>L</sub>_.

Compare(_p,q_). Given \(p,q\in\pi\), return _q_ if it succeeds _p_ in \(\pi\) in _O_(1) time (return _p_ otherwise). To achieve this, we store \(\pi\) in leaf-linked a balanced finger search tree \(T_\pi\). Many implementations exist \[2\]. We choose the level-linked (2-4)-tree by Huddleston and Mehlhorn \[6\], which supports FingerInsert in amortised _O_(1)-time, and Search in _O_(1+log_d<sub>i</sub>_) time. For Compare, we store the linked leaves in the simple dynamic list ordering structure by Bender et al. \[1\] whose simplest implementation supports Compare in _O_(1) time, and FingerInsert in amortised _O_(1) time.

### Algorithm and runtime analysis.

Our algorithm is straightforward. The pseudo code is given by Algorithm 1 where each algorithmic step also indicates the running time. We require linear space. We first extract a longest directed path \(\pi\) from _G_, which we store in our two data structures. This takes _O(n+m_) total time. If \(\pi\) has _n-k_ vertices, this leaves us with a graph _H_ with _k_ vertices.

We then iteratively remove an arbitrary source _x<sub>i</sub>_ from _H_. Since _x<sub>i</sub>_ is a source in _H_, all vertices \(p\in X\) that have a directed path to _x<sub>i</sub>_ in _G_ must be present in \(\pi\). We iterate over all in-neighbours of _x<sub>i</sub>_ in _G_, and use our Compare operation to find the in-neighbour _p<sub>i</sub>_ that is furthest along \(\pi\). If _x<sub>i</sub>_ has no in-neighbours, _p<sub>i</sub>_ is a dummy vertex that precedes the head of \(\pi\) instead. Finally, we proceed in a way that is very similar to the algorithm for topological sorting by Knuth \[10\]: We remove _x<sub>i</sub>_ from _H_, iterate over all out-neighbours of _x<sub>i</sub>_ in _H_ and decrement their in-degree, and update the linked list of sources to include the newly found ones. Since we inspect each in- and out-edge of _x<sub>i</sub>_ only once, this takes _O(m_) total time.

We then want to find the farthest _q<sub>i</sub>_ along \(\pi\) that precedes _x<sub>i</sub>_ in _L_. In the special case where _p<sub>i</sub>_ is the dummy vertex preceding the head _h_ of \(\pi\), we use a query to _O<sub>L</sub>_ to check whether _x<sub>i</sub>\<sub>L</sub>h_. If<tbc>

