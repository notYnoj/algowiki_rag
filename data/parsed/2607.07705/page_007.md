## 3.1 Maximum spanning tree, allowed and blocked edges

We start with properly defining the "guaranteed" subgraph of _G_. We informally refer to it as a maximum spanning tree, or MaxST for short.

**Definition 1** (Maximum spanning tree)**.** Let _G_ be a weakly-connected _n_-vertex digraph with an edge set {_e_<sub>1</sub>_,...,e<sub>m</sub>_} and edge weights **w**. By MaxST(_G,_**w**) we denote a subgraph _T_ of _G_, such that:

• |_V(T_)|=_n_ and |_E(T_)|=_n_-1;<tbc>

• _T_ is weakly-connected;<tbc>

• **w**(_E(T_)) is maximum possible;<tbc>

• a sorted sequence of indices of edges from the set _E(T_) is lexicographically smallest possible among all subgraphs satisfying the previous constraints.

Throughout the paper, we use _T_ as a shortcut for MaxST(_G,_**w**).

Note that in the definition above, we put the last property in order that _T_ is defined unambiguously. Moreover, _T_ can still be found in polynomial time via the standard argument: we first find the maximum weight _w_ of a spanning tree of _G_. Then we construct _T_ iteratively, starting with the empty subgraph. In each iteration, we find an edge _e<sub>i</sub>_ of minimum index such that _T+e<sub>i</sub>_ can be extended to a spanning tree of _G_ of weight _w_, and add this _e<sub>i</sub>_ to _T_.

Naturally, some edges outside _E(T_) do not form a cycle, if added to _T_. For example, if _T+e_ is acyclic for \(e\in E(G)\backslash E(T)\), then (_G,_**w**_,k_) is a yes-instance of MAS/MaxST for any \(k\le\mathbf{w}(e)\). We proceed with a proper formal definition that includes the concept of such edges.

**Definition 2** (Classification of graph edges relative to MaxST)**.** For a weakly-connected digraph _G_ with edge weights **w**, we say that

• Each edge \(e\in E(T)\) is a _tree_ edge.<tbc>

• Each edge \(e\in E(G)\backslash E(T)\) such that _T+e_ has no directed cycles is an **_allowed_** edge.<tbc>

• Each edge \(e\in E(G)\backslash E(T)\) such that _T+e_ has a directed cycle is a **_blocked_** edge.

By _A(G,_**w**) we denote the set of all _allowed_ edges of _G_ and by _B(G,_**w**) we denote the set of all _blocked_ edges of _G_. We shorten this notation to just _A_ and _B_, unless the arguments are different from (_G,_**w**).

The main challenge in our two algorithms is to handle both edge types simultaneously. In the rest of this section, we focus on blocked edges.

## 3.2 Inverse edges and their properties

Note that removing an edge from _T_ can "unblock" some edges in _B_. That is, if _b_ is blocked, and \(e\in E(T)\) belongs to a directed cycle in _T+b_, then (_T-e_)+_b_ is acyclic. In this situation, we say that _b_ is an _inverse edge_ of _e_. We give a formal definition below.

