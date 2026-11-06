<tbc>is to design a search strategy that locates the target node and minimizes the search time in the worst case.

The vertex search problem is more general than its ‘edge variant’ that has been more extensively studied. In the latter problem one selects an edge _e_ of an edge-weighted tree _T_=(_V,E,w_) in a query and learns in which of the two components of _T-e_ the target node is located. Indeed, this edge variant can be reduced to our problem as follows: first assign a ‘large’ weight to each node of _T_ (for example, one plus the sum of the weights of all edges in the graph) and then subdivide each edge _e_ of _T_ giving to the new node the weight of the original edge, _w(e_). It is apparent that an optimal search strategy for the new node-weighted tree should never query the nodes with large weights, thus immediately providing a search strategy for the edge variant of _T_.

We also point out that the considered problem, as well as the edge variant, being quite fundamental, were historically introduced several times under different names: minimum height elimination trees \[31\], ordered colourings \[19\], node and edge rankings \[16\], tree-depth \[29\] or LIFO-search \[14\].

1.1 summarizes the complexity status of the node-query model (in case of unweighted paths in both cases the solution is the classical binary search algorithm) and places our result in the general context.

## 1.1 State-of-the-Art

In this work we focus on the worst case search time for a given input graph and we only remark that other optimization criteria has been also considered \[5, 20, 21, 35\]. For other closely related models and corresponding results see e.g. \[1, 15, 23, 25, 34\].

**The node-query model.** An optimal search strategy can be computed in linear-time for an unweighted tree \[30, 33\]. The number of queries performed in the worst case may vary from being constant (for a star one query is enough) to being at most log<sub>2</sub>_n_ for any tree \[30\] (by always querying a node that halves the search space). Several following results have been obtained in \[12\]. First, it turns out that log<sub>2</sub>_n_ queries are always sufficient for general simple graphs and this implies a _O(m_<sup>log<sub>2</sub>_n_</sup>_n_<sup>2</sup>log_n_)-time optimal algorithm for arbitrary unweighted graphs. The algorithm which performs log<sub>2</sub>_n_ queries also serves as a _O_(log_n_)-approximation algorithm, also for the weighted version of the problem. (We remark that in the weighted case, the algorithms<tbc>

\begin{tabular}{ccc}
_Graph class_ & _Unweighted_ & _Weighted_ \\
\multirow{2}{*}{Paths:} & exact in _O(n_) time & exact in _O(n_<sup>2</sup>) time \[6\] \\
 & & strongly NP-complete \[11\] \\
\multirow{2}{*}{Trees:} & exact in _O(n_) time \[30, 33\] & \((1+\varepsilon)\)-approx. in \(n^{O(logn/\varepsilon)}\) time (Thm. 3.3) \\
 & & \(O(\sqrt{logn})\)-approx. in poly-time (Thm. 3.4) \\
\multirow{2}{*}{Undirected:} & exact in _n_<sup>_O_(log_n_)</sup> time \[12\] & PSPACE-complete \[12\] \\
 & _O_(log_n_)-approx. in poly-time \[12\] & _O_(log_n_)-approx. in poly-time \[12\] \\
Directed: & PSPACE-complete \[12\] & PSPACE-complete \[12\] \\
\end{tabular}

1.1: Computational complexity of the search problem in different graph classes, including our results for weighted trees. Completeness results refer to the decision version of the problem.

