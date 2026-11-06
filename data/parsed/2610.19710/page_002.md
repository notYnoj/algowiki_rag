computing are not settled in the dynamic setting. Dynamic locality was formally defined as the dynamic-LOCAL [2] model and connected to other models of distributed computing, though implicitly variants of it were previously considered in the literature in different contexts [3,6,7,15,18].

In [2], an upper bound of _O_(log_n_) in the online-LOCAL model was established for the problem of _3-coloring bipartite graphs_, leaving open the question of whether it is possible to achieve the same in dynamic-LOCAL or not. Later, a lower bound of \(\Omega(logn)\) was proven for the problem in the online-LOCAL model [11]. As a consequence of the locality model hierarchy, this means that the problem also has at least this complexity in the dynamic- LOCAL model. However, the question of whether this bound is tight for the dynamic-LOCAL model still remained. More precisely, the question asked in [2] was the following:

Is it possible to find a 3-coloring in 2-dimensional grids in the dynamic-LOCAL model with locality _O_(log_n_)?

We answer positively to this question by Theorem 1. Our result holds not only for grids; we give an algorithm for arbitrary bipartite graphs.

\(\blacktriangleright\) **Theorem 1.** _There exists a dynamic graph algorithm which maintains a 3-coloring with a locality of O_(log_n_) _in the dynamic-LOCAL model for input sequences of node and edge insertions where the resulting graph is bipartite at every step._

Consequently, combined with the \(\Omega(logn)\) lower bound for 3-coloring grids in online- LOCAL [11], this bound is tight.

\(\blacktriangleright\) **Corollary 2.** _In the dynamic-LOCAL model, the locality of computing a proper_ 3_-coloring of a bipartite graph is_ \(\Theta(logn)\).

**Landscape of locality.**

We summarize here how dynamic locality relates to other notions of locality in graph algorithms. They are all closely connected; results in one model may have implications for other locality models.

The LOCAL model [16] is the most widely studied model of locality in distributed computing. All nodes of a graph simultaneously send messages to their neighbors, repeatedly over multiple rounds. In this model, locality refers to the number of rounds of message-passing that an algorithm has to perform to solve a problem. Message sizes and computation time are unbounded. This means an algorithm essentially produces the output label of every node independently as a function of its _T_-hop neighborhood, where _T_ is the locality. The parallel processing of nodes in the LOCAL model means that an algorithm has to break symmetries to find a consensus between nodes. However, locality is also influenced by other dependencies and uncertainties. Thus, studying different computational aspects gives a more nuanced picture of locality.

Inspired by online graph algorithms, in the online-LOCAL model [2], nodes of an initially hidden graph are revealed sequentially by an adversary. Each node is revealed together with the node’s _T_-hop neighborhood. Unlike in distributed models, the algorithm keeps a global state. When a node is revealed, the algorithm updates its global state based on the revealed _T_-hop neighborhood, and outputs the current node’s final label. The online-LOCAL model is a strong form of locality, in the sense that any lower bound in that model directly extends to many other models [1,2].

\begin{tabular}{cc}
\multicolumn{2}{c}{Is it possible to find a 3-coloring in 2-dimensional grids in the dynamic-LOCAL model with locality _O_(log_n_)?} \\ \end{tabular}

