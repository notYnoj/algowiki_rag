<tbc>\(r=|\partial_w(u):u\in V|\) _is the number of distinct weighted degrees among all vertices. In the special case of degree-regular graphs, the complexity is_ (_nB_)<sup>_O_(log_B_)</sup>.

**Matroid Bases, Matroid Intersections, and Paths.** Next, we consider other basic combinatorial objects in graphs: _spanning trees_, (bipartite) _matchings_, and _s-t_ paths. Going beyond graphs, we also consider natural extensions of the first two problems to _matroid bases_ and _matroid intersections_.

**Theorem 1.9** (Matroids, Matchings, and Paths)**.** _The following combinatorial problems can be solved efficiently in the comparison oracle model:_

(_i)_ _the minimum-weight basis of a matroid on n elements can be found O(n_log_n_) _comparison queries in_ \(\widetilde{O}(n^2)\) _time,_<tbc>

(_ii)_ _the minimum-weight set in the intersection of two matroids on an n-element ground set can be found using O(n_<sup>4</sup>) _comparison queries/time, and_<tbc>

_(iii)_ _the minimum-length s-t path in a graph (or a negative cycle, if one exists) can be found using using O(n_<sup>3</sup>) _walk comparisons in O(n_<sup>3</sup>) _time._

Note that knowing the order of element weights is enough to optimize over matroids (using the greedy algorithm), but how can we compare element weights? We observe that if two elements share a circuit, then we can find two bases which differ on exactly these elements, and hence compare them. We then show that one can decompose any matroid so that we only need to compare such pairs of elements. (See Section E.1.)

For matroid intersection (and its special case, bipartite matchings), sorting the element weights is neither doable nor sufficient. Instead, we implement the shortest augmenting path algorithm (and its natural extension for matroid intersection) using only comparisons between matchings (i.e., common independent sets); see Section E.2. Finally, we show that the Bellman-Ford algorithm for shortest _s-t_ paths can be implemented using comparisons between _s-t_ walks to prove (iii).

Furthermore, by utilizing the Dual Ellipsoid reduction developed in Section 3, we obtain an efficient algorithm for finding optimal perfect matchings in complete bipartite graphs.

**Theorem 1.10** (Bipartite Perfect Matching)**.** _There is a polynomial-time algorithm to find the minimum-weight perfect matching in a complete bipartite graph K<sub>n,n</sub> using only comparisons between perfect matchings._

**Organization.** In Section 2, we present our first result on query complexity for Boolean Linear Optimization. Next, Section 3 presents our reduction from optimization to certification via the Dual Ellipsoid method. Section 4 introduces our Global Subspace Learning framework, and gives efficient algorithms for specific classes of set systems. Section 5 is dedicated to efficient algorithms for finding minimum cuts using cut comparisons. To improve flow, many technical proofs and discussions are deferred to the appendix, which includes the omitted proofs from the Dual Ellipsoid framework (see Section B), as well as our algorithms for minimum-weight matroid bases, matroid intersections, and shortest _s-t_ paths (see Section E).

## 1.2 Related Work

While our theoretical study of comparison oracles for linear discrete optimization problems is new, to the best of our knowledge, comparison oracles have been studied for submodular functions and<tbc>

