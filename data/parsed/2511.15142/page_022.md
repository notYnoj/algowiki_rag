Given this efficient edge-extraction claim, we now prove the claimed bounds for graph recovery.

_Proof of Theorem 1.7._ When \(n\ge 4\), using Lemma 5.3, we can discover all the neighbors of _u_ using \(|\partial(u)|\cdot O(logn)\) queries and \(\widetilde{O}(n)\) time. Summing over all _u_ gives a total of at most _O_((_m+n_)log_n_) queries and \(\widetilde{O}(n^2)\) time. Hence, we start by running this procedure until the number of edges discovered is at least _n_<sup>2</sup>/log_n_. At this point, we switch to the algorithm using Theorem 5.1(i) to discover the remaining edges using at most _O(n_<sup>2</sup>) queries. This guarantees that we use at most _O_(min((_m+n_)log_n,n_<sup>2</sup>)) queries and \(\widetilde{O}(n^2)\) time.

When \(n\le 3\) and \(G\notin\{K_2,\bar{K}_2,K_3,\bar{K}_3\}\), sorting the degrees of the vertices reveals the graph.

## 5.2 Finding Minimum Cuts

We now turn to finding minimum cuts. We start off by observing that when \(n\le 4\), we can bruteforce the minimum cut and otherwise, use Theorem 1.7 to optimize over min-cuts: we reconstruct the graph using _O_(min((_m+n_)log_n,n_<sup>2</sup>)) queries and \(\widetilde{O}(n^2)\) time; we can then optimize over it in \(\widetilde{O}(n^2)\) time. However, the number of cut queries incurred this way is quadratic and not near-linear, as promised in Theorem 1.6.

However, we can use ideas from \[RSW18\] to do better. Suppose \(G'\) is a contracted graph (i.e., where some nodes in _G_ have been contracted into each other), and \(G'(p)\) is the "edge-percolation" graph obtained by sub-sampling each edge of \(G'\) independently with probability _p_. Distilling the results of \[RSW18\] shows that if, for any contraction \(G'\) of _G_, we can obtain a sample from \(G'(p)\) using \(\alpha\cdot p\cdot|E(G')|\) queries, then we can compute the min-cut of _G_ using \(\alpha\cdot\widetilde{O}(n)\) queries and in \(\widetilde{O}(n^2)\) expected runtime. (A proof appears in Section D.2.)

To use this result, we show how to sample percolations of contractions with \(\alpha=\widetilde{O}(1)\).

**Lemma 5.4** (Contracted Graphs)**.** _When_ \(n\ge 4\)_, for any contraction_ \(G'=(U',E')\) _of G, with its vertex set_ \(U'\) _represented as a partition of the original vertex set U, we can sample a subgraph_ \(G'(p)\) _where each edge in_ \(G'\) _is sampled independently with probability p using_ \(|E'|\cdot O(plogn)+\widetilde{O}(n)\) _queries and_ \(\widetilde{O}(n^2)\) _time in expectation._

_The sampling can be done more generally for any induced subgraph_ \(G''=G'[S]\) _for some_ \(S\subseteq U'\) _with_ \(|E'(S)|\cdot O(plogn)+\widetilde{O}(n)\) _queries and_ \(\widetilde{O}(n^2)\) _time._

_Proof._ For any regular vertex _u_, if _V<sub>u</sub>_ is the super vertex that contains it, we will show how to sample edges from \(\partial(u,U-V_u)\) with each edge sampled independently with bias \(q\in[0,1]\). Call this random subgraph \(\partial_{G^\prime}(u,q)\). Given the primitive to sample \(\partial_{G^\prime}(u,q)\), taking the union \(\cup_{u\in U}\partial_{G^\prime}(u,q)\) of such samples for each vertex \(u\in U\) with \(q=1-\sqrt{1-p}\) (so that 1-(1-_q_)<sup>2</sup>=_p_) gives \(G'(p)\). Because, the probability of any edge \(e\in E'\) to be selected is 1-(1-_q_)<sup>2</sup>=_p_ and the independence is trivial.

To sample \(\partial_{G^\prime}(u,q)\), let _T_ be a random subset of _U-V<sub>u</sub>_ with each element sampled independently with probability _q_. Reveal all the edges of _u_ going into _T_ using Lemma 5.3. This takes \(|\partial(u,T)|\cdot O(logn)\) queries which is \(q\cdot|\partial(u,U-V_u)|\cdot O(logn)\) in expectation and \(\widetilde{O}(n)\) time. Summing over all \(u\in U\) gives a total of \(|E'|\cdot O(plogn)+\widetilde{O}(n)\) queries and \(\widetilde{O}(n^2)\) time in expectation. An edge {_u,v_} for \(v\in U\backslash V_u\) is sampled iff \(v\in T\). This implies that each edge is sampled independently with probability _q_. Simply replacing _U_ with _S_ gives the extension to induced subgraphs.

Combining Lemma 5.4 with the abstraction of \[RSW18\] discussed above completes our algorithm for min-cuts (Theorem 1.6).

