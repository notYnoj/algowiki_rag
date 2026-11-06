### Low Degree Vertices.

Consider the graph _G<sub>x</sub>_=(_V,E<sub>n<sup>x</sup></sub>_) where _E<sub>n<sup>x</sup></sub>_={(_u,v_)_s.t. deg(u)\<n<sup>x</sup>_ or _deg(v)\<n<sup>x</sup>_}. Then |_E<sub>n<sup>x</sup></sub>|=O(n_<sup>1+_x_</sup>). We simply run an algorithm by Baswana and Kavitha that satisfies Theorem 2.7 \[BK10\]. This computes a (2,0)-approximation of paths contained in _G<sub>x</sub>_ with an expected time of \(\tilde{O}\left(n^{1.5+x}+n^2\right)\).

### Time Complexity

Balancing _n_<sup>1.5+_x_</sup> with \(\omega(1,1-x,1)\), we get _x_=0.53184039, and an overall running time of \(\tilde{O}\left(n^{2.03184}\right)\). Note that the running time bound holds on expectation.

### Algorithm

Algorithm 1 begins by initializing the distance matrix with adjacency matrix and setting parameters _x,C_ which will be chosen to optimize the running time.

Phase 1 (Lines 4-6), uses `boundedMinPlus` on matrix _M<sub>t</sub>_ to estimate distances for paths of length at most _C_ containing at least one vertex of degree \(\ge n^x\). To do so, Line 4 considers log_n_ degree thresholds, each of the form \(t=\frac{n}{2j}\). Within each threshold, a dominating set _C<sub>t</sub>_ is computed (Line 5) and a edge set _E_<sub>2_n/t_</sub> such that the degree of each vertex does not exceed \(\frac{2n}{t}\) . Line 12 of `dominatingSetAPASP` computes a `BFS` within the sub-graph _G<sub>t</sub>_=(_V,E_<sub>2_n/t_</sub>) from each node in the dominating set _C<sub>t</sub>_, keeping only distances up to _C_+1. Then, for each pair of vertices, _u,v_, a bounded (min,+) product is computed in Line 15 of `dominatingSetAPASP` to compute the shortest path between _u,v_ passing through a vertex \(w\in C_t\). We repeat this computation for all _t_, balancing the thresholds so that each `BFS` search can be computed efficiently. We repeat for all _t_ large enough such that the dominating set _C<sub>t</sub>_ is small.

Phase 2 uses `BK2APASP` to compute (2,0) approximations for paths with maximum degree _n<sup>x</sup>_.

Phase 3 uses `DenseAPASP` to compute a +_C_ approximation, which implies a (2,0) approximation for all paths of length at least _C_.

Next, we give the pseudocode of `Random2ApproxAPSP` and its correctness proof along with a time complexity analysis.

## Correctness

_Proof._ First, \(\delta(u,v)\le\hat{\delta}(u,v)\) for all _u,v_. For each call to `dominatingSetAPASP`, this follows from Lemma C.1 as \(\hat{\delta}(u,v)\ge\delta(G_t,u,v)\ge\delta(u,v)\) as \(G_t\subset G\). The claim then follows from the correctness of `BK2APASP` and `DenseAPASP`.

We now show that \(\hat{\delta}(u,v)\le 2\delta(u,v)\) for all _u,v_. Let _P_ be a shortest path and \(deg(P)=max_{v\in V}deg(v)\) be the maximum degree of a vertex in path _P_.

