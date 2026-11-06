**Algorithm 1** Finding _k_-edge-connected spanning subgraph of a given graph _G_ (from \[12\]).

1: **Input:** Graph _G_=(_V,E_)

2: **Output:** Partition _E_<sub>1</sub>_,E_<sub>2</sub>_,...,E_<sub>|_E_|</sub> of _E_

3: \(E_1:=E_2:=\cdots:=E_{|E|}:=\emptyset\);

4: Label all nodes \(v\in V\) and all edges \(e\in E\) "unscanned";

5: _r(v_):=0 for all \(v\in V\) ;

6: **while** there exist "unscanned" nodes **do**

7: Choose an "unscanned" node \(x\in V\) with the largest _r(x_);

8: **for** each "unscanned" edge _e_ incident to _x_ **do**

9: Let _y_ be the other end node \((\neq x)\) of _e_;

10: \(E_{r(y)+1}:=E_{r(y)+1}\cup\{e\}\);

11: **if** _r(x_)=_r(y_) **then**

12: _r(x_):=_r(x_)+1;

13: **end if**

14: _r(y_):=_r(y_)+1;

15: Mark _e_ "scanned";

16: **end for**

17: Mark _x_ "scanned";

18: **end while**

For dynamic maintenance of the sparse certificate we use the Link-Cut tree data structure of Sleator and Tarjan \[14\]. A Link-Cut tree maintains a forest of rooted trees. Each represented tree is partitioned into vertex-disjoint paths via a preferred-path decomposition, and each such path is stored as a splay tree \[15\] keyed by the depth of its nodes in the represented tree. The auxiliary splay trees are connected by path-parent pointers, which link the root of each auxiliary tree to the parent (in the represented tree) of the topmost node on its preferred path. We use the following operations \[14, 2\]:

• MakeTree(_v_) - creates a new singleton tree containing the vertex _v_,<tbc>

• FindRoot(_v_) - returns the root of the tree containing vertex _v_,<tbc>

• link(_v,w_) - adds an edge making _v_ a child of _w_, assuming _v_ is the root of its tree and _v_, _w_ belong to distinct trees,<tbc>

• cut(_v_) - removes the edge between vertex _v_ and its parent parent(_v_) (where _v_ is not the root), splitting the tree into two disjoint components and makes _v_ the root of a represented tree,<tbc>

• evert(_v_) - modify the tree containing vertex _v_ by making _v_ its root.

Each operation runs in _O_(log_n_) amortized time. To initialize the structure, we compute the sparse certificate using Algorithm 1 and construct _k_ Link-Cut trees _LC_<sub>1</sub>_,...,LC<sub>k</sub>_, where each _LC<sub>i</sub>_ is built by executing MakeTree(_v_) for every \(v\in V\) followed by link operations for every edge in the corresponding forest _F<sub>i</sub>_.

The core building block of the maintenance procedure is the TryAdd(_LC_, _u,v_) function (Algorithm 2), which attempts to insert an edge {_u,v_} into the forest _F<sub>i</sub>_ maintained by _LC<sub>i</sub>_ (\(1\le i\le k\)). If _u_ and _v_ lie in different components of _F<sub>i</sub>_, the edge is added via link and the function returns null. Otherwise, _u_ and _v_ are already connected in _F<sub>i</sub>_, so adding {_u,v_} would create a cycle. In this case, the function removes the edge {_u,_parent(_u_)} via cut, inserts {_u,v_} in its place via link, and returns the displaced edge {_u,_parent(_u_)} to the caller for insertion into the next forest in the sparse certificate.

The primary maintenance routine, HandleAddition(_e_) (Algorithm 3), uses TryAdd as a subroutine in a cascading fashion. Given a new edge _e_={_u,v_}, the procedure calls TryAdd on _LC_<sub>1</sub>. If the edge is absorbed (TryAdd returns null), the process terminates. Otherwise, the displaced edge is passed to TryAdd on _LC_<sub>2</sub>, and so on through the sequence of forests up to _LC<sub>k</sub>_. If an edge is displaced from the final forest _F<sub>k</sub>_, it is redundant for _k_-edge-connectivity and is discarded.

