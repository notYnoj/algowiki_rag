On the other hand, for non-dominating pairs that have no witness in C, we prove an interesting structural result: if _u,v_ has no "large" witness, then it must have many witnesses. More specifically, we prove that if _u,v_ is a non-dominating pair witnessed by some \(C\notin\mathcal{C}\) in **G**_<sub>x</sub>_, then there are at least \(\Omega(|V\backslash N[x]|)\) nodes \(y\in V\) such that **G**_<sub>y</sub>_ contains a component witnessing _u,v_. Assuming for simplicity that |_N[x_]|=_o(n_) for all \(x\in V\) , we can exploit this property as follows: we sample \(\Theta(logn)\) nodes and, for each sampled node _y_, find all non-dominating pairs witnessed by any component of **G**_<sub>y</sub>_. This takes O(_n_<sup>2</sup>) time per sampled node _y_, since the sizes of the components in each **G**_<sub>y</sub>_ sum to O(_n_).

In the full proof, we again provide a derandomized version of the algorithm.

## Open Problems

To conclude this section, we list some other open problems:

First, we report an open problem posed in [KS06]. It is well established that every AT-free graph contains a dominating pair [COS97], which can, in fact, be found in linear time [COS99]. However, neither AT-free graph recognition nor finding a dominating pair in a general graph can be solved in linear time unless \(\omega=2\) or some fine-grained complexity hypothesis fails. This leads to an interesting open question: is there a robust, linear-time algorithm for finding a dominating pair in an AT-free graph? Here, "robust" is used in the sense of [RS03]; a robust linear-time algorithm must take an arbitrary (i.e., not necessarily AT-free) graph as input and, in linear time, either output a dominating pair or correctly report that the graph is not AT-free.

We showed that detecting an AT-triple has the same time complexity as detecting a triangle in a graph. In time \(\mathcal{O}(n^\omega)\), however, we can solve problems stronger than triangle detection, e.g., the all-edge triangle problem, where for each edge we want to know whether it is contained in a triangle. Our approach for detecting an AT-triple does not seem to yield such an all-edge version in \(\mathcal{O}(n^\omega)\) time, and the latter seems considerably more difficult: namely, for each pair _x_, _y_ we want to know whether there is a _z_ such that {_x,y,z_} is an AT. It would be interesting to determine whether a running time of \(\mathcal{O}(n^\omega)\) is achievable, or whether some hardness result rules this out.

Generally, there is a plethora of other important structures in structural graph theory that admit polynomial-time algorithms which are nonetheless clearly far from optimal, where a fine-grained complexity lens could help uncover new structural properties; see, e.g., perfect graphs [CLV03, CKS05] or graphs with even or odd holes [CL15, CSSS20, CLL22].

## 3 Preliminaries

**Set notation.** For integers \(i,j\in\mathbb{Z}\), we write **[**_i..j_** ]** to represent the set {_i,...,j_}, and **[**_i..j_** )** to denote the set {_i,...,j_-1}. We define **(**_i..j_** ]** and **(**_i..j_** )** similarly.

Graph notation. All graphs considered in this paper are undirected. For a graph **G**=(_V,E_), we denote by _n_:=|_V_| the number of nodes and by _m_:=|_E_| the number of edges. For a node \(v\in V\) we indicate with _N(v_) its neighborhood, and with \(N[v]:=N(v)\cup\{v\}\) its _closed neighborhood_. Similarly, we define the neighborhood of a set \(S\subseteq V\) as \(N(S):=\cup_{v\in S}N(v)\backslash S\), and its closed neighborhood as \(N[S]:=N(S)\cup S\). In case of ambiguity due to the existence of multiple graphs, we write as subscript the graph which the neighborhood refers to, e.g., _N_**G**(_v_).

We indicate with **G**_<sub>v</sub>_ the graph obtained by removing from **G** the closed neighborhood, i.e., **G**_<sub>v</sub>_:=**G**[_V_\\_N[v_]]. Lastly, for a node \(u\in V\backslash N[v]\), we let _C<sub>v</sub>(u_) be the connected component of **G**_<sub>v</sub>_ that contains _u_. More specifically, _C<sub>v</sub>(u_) is the set of nodes in **G**_<sub>v</sub>_ that are in the same connected component as _u_.

Finally, we say that a (simple) _x-y_ path in **G**=(_V,E_) avoids a set \(S\subseteq V\) , if it contains no node in _S_.

