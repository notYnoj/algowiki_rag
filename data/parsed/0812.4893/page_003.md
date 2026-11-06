We assume synchronous communication. On each time step, every node can (i) receive messages from its neighbours, (ii) perform deterministic local computations, and (iii) send a message to each of its neighbours. The algorithm runs for _T_ synchronous time steps, after which each node needs to produce the output: which of the neighbours, if any, is its partner in the matching. We also require that the output is consistent: if _u_ announces that _v_ is its partner, then _v_ must announce that _u_ is its partner.

## 1.3 Statement of Results

Our main contribution lies in an analysis of the "transient phase" of the Gale-Shapley algorithm for the stable marriage problem. We truncate the algorithm to a specified number of proposal rounds and investigate the resulting matching for stability. We find that a constant number of rounds suffice to obtain a constant ratio of unstable edges to matching edges. We obtain the following result.

**Theorem 1.** _There exists a deterministic distributed algorithm that finds an_ \(\epsilon\)_-stable matching in a bicoloured graph in time_ \(T\le 4+2\Delta^2/\epsilon\).

The algorithm works even in the case when ties in the preference lists are allowed.

We also consider the case where G is an edge-weighted graph, and the preferences are determined by the edge weights: each node prefers its incident edges in order of their weight, with the heaviest edge being the most preferred. If all weights are distinct, the unique _stable_ matching in G is the greedy one, and its weight is at least 1/2 of that of the maximum-weight matching. In general, an _almost_ stable matching can be a poor approximation to the maximum-weight one; say, a super-heavy edge may be missing from the almost stable matching. Fortunately, the particular almost stable matching from Theorem 1 is much better in this sense.

**Theorem 2.** _There exists a deterministic distributed algorithm that finds a_ \((2+\epsilon)\)_-approximation for maximum-weight matching in bicoloured graphs in time_ \(T\le 4+2\Delta/\epsilon\).

Given access to a bicoloured graph via a _preference oracle_ (queried with a node, the oracle replies with the colour of the node and the adjacent nodes listed in order of preference), the algorithm in Theorem 1 enables estimation of the size of a stable matching using a constant number of queries to the oracle. We analyse the non-degenerate case \(\Delta\ge 3\).

**Theorem 3.** _For any_ \(0<\delta\le 1/2\), \(0<\epsilon\le 1\)_, and_ \(\Delta\ge 3\)_, there exists a randomised algorithm that, given access to a preference oracle for a bicoloured graph_ G _without isolated nodes, makes at most_ \(25000\epsilon^{-2}(\Delta-1)^{3+4\Delta/\epsilon} ln\delta^{-1}\) _queries to the oracle and outputs with probability at least_ \(1-\delta\) _an estimate_ \(\hat{m}\) _such that_ \(\left|\hat{m}-\left|M\right|\right|\le\epsilon|M|\) _where M is a stable matching in_ G.

