\(\blacktriangleright\) **Corollary 8.** _For s-clique listing, where every s-clique in the graph is output by at least one of its nodes, the worst case energy complexity is_ \(\Omega\big(n^{1-2/s}/logn\big)\) _rounds for algorithms that fail with some small constant probability_ \(\epsilon>0\).

**Proof.** As explained in [26], the proof is analogous to the lower bound for triangle enumeration by [34], with the crucial difference being the use of Lemma 1.3 of [26] to bound the number of _s_-cliques in any graph with a given number of edges. \(\blacktriangleleft\)

We now turn our attention to graph problems for which the existing lower bound constructions are based on reductions from the set disjointness function. By virtue of Corollary 6, we immediately obtain lower bounds on the energy complexity of several important graph problems:

\(\blacktriangleright\) **Corollary 9.** _Computing an exact minimum vertex cover, maximum independent set, or minimum dominating set has a node-averaged energy complexity of_ \(\Omega\big(\frac{n^2}{log^2n}\big)\) _in expectation._

**Proof.** In [25], it is shown that these problems admit an \(\ell\)-separated lower bound family with respect to the set disjointness function \(DISJ_{\Theta(n^2)}\), for \(\ell=\Theta(n/logn)\). The result follows from Corollary 6. \(\blacktriangleleft\)

\(\blacktriangleright\) **Corollary 10.** _Computing the exact network diameter with_ \(\epsilon\) _error, for some small constant_ \(\epsilon>0\)_, has a node-averaged energy complexity of_ \(\Omega(n/logn)\) _in expectation. The same bound holds for computing exact all-pair-shortest-paths (APSP) routing tables._

**Proof.** It is straightforward to verify that the lower bound construction of [27] has all the important properties of a 2-separated graph family with respect to \(DISJ_{\Theta(n^2)}\) and the graph predicate _P_ for deciding whether the diameter is at most 4. Since there are \(\Theta(n)\)-nodes in \(|V_1^+|\) and \(|V_2^-|\) that form a perfect matching, we know that _d<sub>cut</sub>_=1, and the maximum cut size is \(s=\Theta(n)\). Applying Corollary 6 completes the proof. \(\blacktriangleleft\)

\(\blacktriangleright\) **Corollary 11.** _In any undirected, weighted graph G, or directed, unweighted graph G, computing the exact Minimum Weight Cycle with_ \(\epsilon\) _error, for some small constant_ \(\epsilon>0\)_, has a node-averaged energy complexity of_ \(\Omega(n/logn)\) _in expectation._

**Proof.** It is straightforward to verify that the lower bound constructions of [38] both have all the important properties of a 2-separated graph family with respect to \(DISJ_{\Theta(n^2)}\) and the graph predicate _P_ for deciding, respectively, whether there exists a directed cycle of length at most 4 and a cycle of weight at most 6, whereby the cut set size (for both constructions) is \(s=\Theta(n)\). Moreover, the edges in the (only) cut form a perfect matching and hence _d<sub>cut</sub>_=1, and we can apply Corollary 6 to complete the proof. \(\blacktriangleleft\)

## 5 Conclusion

In this paper, we presented an information-theoretic framework for showing polynomial (in _n_) lower bounds for various fundamental graph problems. These energy lower bounds almost match (up to logarithmic factors) their respective round lower bounds. Hence, it is not fruitful to design distributed algorithms for these problems that achieve significantly lower energy complexity than their round complexity.

The good news is that our technique can be used to establish energy lower bounds, provided we have suitable communication-complexity lower bounds that are sufficiently large (e.g., polynomial in _n_). There are still several problems, such as minimum cut and maximum matching, where we do not have (almost) matching energy bounds, which are worth studying.

