constrained multiple selection problems have not been considered before. This could be a fruitful direction for future work.

Finally, the related _top-k sorting_ problem asks to find the smallest _k_ elements and sort them. Haeupler, Hladík, Iacono, Rozhoň, Tarjan, and Tětek \[HHI<sup>+</sup>25\] gave an optimal algorithm for poset-constrained top-_k_ sorting. Note that this problem is very close to our selection problem. Clearly, a solution to top-_k_ sorting also finds the _k_-th smallest element. Conversely, observe that finding the _k_-th smallest element also necessarily identifies all smaller elements. For top-_k_ sorting, it only remains to sort them, in at most O(_k_log_k_) time. Thus, the optimal number of comparisons for top-_k_ sorting with poset constraint _G_ is no more than O(OPT(_G,k_)+_k_log_k_), and the aforementioned algorithm achieves this bound, as it is known to be optimal.

## 2 Preliminaries

Let _G_ be a directed acyclic graph (DAG). As usual, we write _V(G_) for the set of vertices in _G_ and _E(G_) for the set of edges. For a subset \(U\subseteq V(G)\), let _G_\[_U_\] denote the subgraph of _G_ induced by _U_, and let _G-U=G_\[_V(G_)\\_U_\]. We write deg<sub>-</sub>(_G,v_) and deg<sub>+</sub>(_G,v_) for the in-degree and out-degree of a node _v_ in _G_.

A subset \(U\subseteq V(G)\) is called a _prefix_ of _G_ if for each node \(u\in U\), each in-neighbor \(v\in N_G^-(u)\) is also contained in _U_. This corresponds to a lower set in the corresponding partial order _P_. The set of sources (in-degree-zero nodes) in _G_ is denoted by Sources(_G_).

We say a node \(u\in V(G)\) is an _ancestor_ of a node \(v\in V(G)\) if there is a directed path from _u_ to _v_ in _G_. Borrowing from poset terminology, we call a set \(U\subseteq V(G)\) an _antichain_ if no \(u\in U\) is an ancestor of a different node \(v\in U\).

Let _F_ be a rooted forest. We consider _F_ to be a DAG, with each edge directed away from the root of the tree containing it. We write deg(_F,v_)=deg<sub>+</sub>(_F,v_) for each node \(v\in V(F)\). The _depth_ of a node _v_ in is the number of nodes on the path between _v_ and the root of the tree containing _v_. For a set of nodes \(U\subseteq V(F)\), we let Children(_F,U_) be the set of children of nodes in _U_ (possibly including some nodes in _U_). Finally, if _F_ is a tree, then root(_F_) denotes its unique root.

In the following, we use upper-case letters, usually _L_, to denote a total order, and write \(x\prec_Ly\) to indicate that _x_ is smaller than _y_ under _L_. The _rank_ of an element _x_ within _L_ is the number of elements smaller or equal to _x_. In particular, the rank of the minimum is 1.

Let _G_ be a DAG. A total order _L_ on _V(G_) or a superset of _V(G_) is _consistent_ with _G_ if for each edge \((u,v)\in E(G)\), we have \(u\prec_lv\). We write L(_G_) for the set of linear orders on _V(G_) that are consistent with _G_. Observe that if _P_ is the poset corresponding to the transitive closure of _G_, then L(_G_) is precisely the set of linear extensions of _P_.

In the _poset selection_ problem, we are given a DAG _G_, a number \(k\in[|V(G)|]\) and a comparison oracle for a linear order _L_ on _V(G_) that is consistent with _G_. The comparison oracle is a black-box function that answers questions \(u\prec_lv\) for \(u,v\in V(G)\) in constant time. The task is to find the the _k_-th smallest node (i.e., the node of rank _k_) according to _L_.

Let _A_ be a correct deterministic algorithm for the poset selection problem. Let T_<sub>A</sub>(G,k,L_) be the number of comparisons that _A_ performs on the input (_G,k,L_), and let T_<sub>A</sub>(G,k_)=<tbc>

