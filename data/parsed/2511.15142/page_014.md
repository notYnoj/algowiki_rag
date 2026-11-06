Let P be the set of characteristic vectors of perfect matchings in the complete bipartite graph _K<sub>n,n</sub>_ (with _d=n_<sup>2</sup>). Given an input weight vector _w_ for the CCO, the minimum weight perfect matching \(y_1=argmin_{y\in\mathcal{P}}\langle w,y\rangle\) can be identified in \(poly(n,\langle w\rangle)\) time using standard bipartite matching algorithms.

It remains to generate a certificate of the optimality of _y_<sub>1</sub> based solely on comparisons between perfect matchings in P. Without loss of generality, assume _y_<sub>1</sub> consists of the edges \(\{(i,i):i\in[n]\}\). Geometrically, the optimality of _y_<sub>1</sub> with respect to _w_ corresponds to the existence of a halfspace H with normal _w_ that contains P, such that _y_<sub>1</sub> lies on the boundary of H. By LP duality, such a halfspace can be represented as a conic combination of the inequalities defining the polyhedron conv(P). Our goal is to construct this certificate using a small number of comparisons. The standard LP relaxation for the bipartite perfect matching problem is:

\(min\big\{\sum_{i,j\in[n]}w_{i,j}x_{i,j}|\sum_{i\in[n]}x_{i,j}=\sum_{j\in[n]}x_{i,j}=1,x_{i,j}\ge 0\big\},\) (primal-PM)

and its dual LP is:

\(max\big\{\sum_{i\in[n]}\alpha_i+\sum_{j\in[n]}\beta_j|\alpha_i+\beta_j\le w_{i,j}\forall i,j\in[n]\big\}.\) (dual-PM)

Proving the optimality of _y_<sub>1</sub> with respect to _w_ is equivalent to demonstrating the feasibility of the following system:

\(\alpha_i+\beta_i=w_{i,i}\forall i\in[n]\) (7)

\(\alpha_i+\beta_j\le w_{i,j}\forall i,j\in[n].\) (8)

Eliminating the variables \(\beta\), this feasibility problem simplifies to:

\(\alpha_i-\alpha_j\le w_{i,j}-w_{j,j}\forall i,j\in[n].\) (9)

This condition is equivalent to requiring that the complete directed graph _D_ on vertex set \[_n_\] with edge weights _c<sub>i,j</sub>_:=_w<sub>i,j</sub>-w<sub>j,j</sub>_ contains no negative cycles. (Note that the optimality of _y_<sub>1</sub> guarantees that _D_ has no negative cycles; our task is to certify this fact.) Observe that the weight of any directed cycle _C_ (or more generally, a vertex-disjoint union of cycles, i.e., a 2-factor) in _D_ corresponds exactly to the weight difference between two perfect matchings.

Thus, the problem reduces to the following: Given a complete directed graph known to have no negative cycles, certify this property by comparing the weights of 2-factors. Note that since the empty 2-factor has weight zero, we may also check the sign of any 2-factor.

We achieve this by running the Bellman-Ford algorithm from each vertex \(s\in[n]\). Let _DP<sub>s</sub>(v,k_) denote the shortest path from _s_ to _v_ using at most _k_ edges. We initialize _DP<sub>s</sub>(s,_0) as the empty path and _DP<sub>s</sub>(u,_1) as the edge (_s,u_) for \(u\neq s\). The entry _DP<sub>s</sub>(v,k_+1) is updated by selecting the minimum weight path from the set of candidates:

\(\{DP_s(u,k)\cdot(u,v)\}_{u\in[n]}\cup\{DP_s(v,k)\}.\) (10)

Note that a candidate path \(DP_s(u,k)\cdot(u,v)\) might visit _v_ more than once. However, such walks must have weight strictly greater than _DP<sub>s</sub>(v,k_); otherwise, the graph would contain a negative cycle involving _u_ and _v_ (which we can rule out by checking the sign of this cycle). After this filtering,

