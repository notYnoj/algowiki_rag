Partial order production for a given _\<_slot naturally decomposes into the same problem for each of the connected components of the undirected graph underlying _\<_slot. In the case of a single connected component, an elementary adversary argument shows that \(\mathsf{Q}(\Pi)\ge n-1\): Any combination of less than _n_-1 queries to \(\rho\) leaves some pair of slots in _\<_slot undetermined with respect to \(\rho\). Another lower bound is the information-theoretic limit. For each way of putting items into slots, the number of input rankings \(\rho\) for which that way is a correct answer is bounded by _e(\<_slot), the number of ways to extend _\<_slot to a total order. Therefore, there must be at least _n!/e(\<_slot) distinct execution traces. Since each execution trace is determined by the outcomes of its queries, and each query has only two outcomes, we conclude that \(\lambda(<_\mathsf{slot})\doteq log_2(n!/e(\text{\textit{\<}}_\mathsf{slot}))\) queries are necessary to solve partial order production. Complementing these lower bounds there exists an upper bound of \((1+o(1))\cdot\lambda(\text{\textit{\<}}_\mathsf{slot})+c\cdot(n-1)\) queries for some universal constant _c_ \[CFJ<sup>+</sup>10\]. For a generic instance \(\Pi\) with partial order _\<_slot it follows that \(\mathsf{Q}(\Pi)=\Theta(\lambda(\text{\textit{\<}}_\mathsf{slot})+n-\gamma(\text{\textit{\<}}_\mathsf{slot}))\), where \(\gamma(\text{\textit{\<}}_\mathsf{slot})\) denotes the number of connected components of the undirected graph underlying _\<_slot.

Not every problem of interest in the comparison model is an instance of partial order production. Here are a few examples.

\(\circ\) In _rank finding_ there is a designated item _x_<sup>∗</sup>, and we have to compute its rank. The rank can be computed by comparing _x_<sup>∗</sup> with each of the _n_-1 other items. A similar elementary adversary argument as above shows that the query complexity is at least _n_-1.<tbc>

\(\circ\) In _counting inversions_ the items are arranged in some known order \(\sigma\) and the objective is to count the number of inversions of \(\sigma\) with respect to \(\rho\). As we reviewed in Section 1, counting inversions has exactly the same query complexity as sorting.<tbc>

\(\circ\) The problem of _inversion parity_ is the same as counting inversions except that one need only count the number of inversions modulo 2. This problem, as well as counting inversions modulo _m_ for any integer _m\>_1, also has exactly the same complexity as sorting.

For each of the three problems above, information theory does not provide a satisfactory lower bound. For example, in the inversion parity problem there are only two possible outputs, which yields a lower bound of log<sub>2</sub>(2)=1. It so happens that for each of the preceding three examples, the query complexity is known quite precisely; however, the known arguments are rather problem- specific.

_Inversion minimization on trees_ is another example that does not fit the framework of partial order generation, and for which information theory only yields a weak lower bound: \(log_2\genfrac(){pt}{2}{n}{2}=2log_2(n)-\Theta(1)\). In contrast to the above examples, a strong lower bound does not seem to follow from a simple ad-hoc argument nor from a literal equivalence to sorting.

## 3 Sensitivity Lemma

In this section we develop Lemma 14. We actually prove a somewhat stronger version.

**Lemma 17 (Strong Sensitivity Lemma).** _Consider an algorithm A in the comparison-based model with n items, color each vertex of the permutahedron with its execution trace under A, and let <o>H</o> denote the subgraph with the same vertex set but only containing the bichromatic edges. The number of distinct execution traces of A is at least g_(deg<sub>avg</sub>(<o>_H_</o>)+1)_/n, where_ \(g:[1,\infty)\rightarrow\mathbb{R}\) _is any convex function with g(x_)=_x! for_ \(x\in[n]\).

