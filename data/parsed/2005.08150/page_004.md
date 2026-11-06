<tbc>Unsurprisingly perhaps, the existence of a stable matching in the proximity of which we wish to find a solution, does not readily mitigate the computational hardness of the problem, as evidenced by Theorem 2, which is implied by the construction of an instance in the proof of Theorem 1 itself.

**Theorem 2.** LS-ASM _is_ W\[1\]_-hard with respect to k+t, even when maximum degree is at most four._

In our quest for a parameterization that makes the problem tractable, we investigate LS-ASM with respect to _k+q+t_.

**Theorem 3.** LS-ASM _is_ W\[1\]_-hard with respect to k+q+t._

To prove Theorem 3, we again give a polynomial-time many-to-one parameter preserving reduction from the MCQ problem to LS-ASM. We wish to point out here that in the instance which was constructed to prove Theorem 1, _q_ is not a function of _k_. Thus, we mimic the idea of gadget construction in the proof of Theorem 1 and reduces _q_ to a function of _k_. However, in this effort, degree of the graph increases. Therefore, the result in Theorem 3 does not hold for constant degree graph or even when the degree is a function of _k_. This tradeoff between _q_ and the degree of the graph in the construction of instances to prove intractability results is not a coincidence as implied by our next result.

**Theorem 4.** _There exists an algorithm that given an instance of_ LS-ASM_, solves the instance in_ 2<sup>O(_q_log_d_)+_o(dq_)</sup>_n_<sup>O(1)</sup> _time, where n is the number of vertices in the given graph, and d is the maximum degree of the given graph._

To prove Theorem 4, we use the technique of _random separation_ based on color coding, in which the underlying idea is to highlight the solution that we are looking for with good probability. Suppose that \(\eta\) is a hypothetical solution to the given instance of LS-ASM. Note that to find the matching \(\eta\), it is enough to find the edges that are in the symmetric difference of \(\mu\) and \(\eta\) (\(\mu\triangle\eta\)). Thus, using the technique of random separation, we wish to highlight the edges in \(\mu\triangle\eta\). We achieve this goal using two layers of randomization. The first one separates vertices that appear in \(\mu\triangle\eta\), denoted by the set \(V(\mu\triangle\eta)\), from its neighbors, by independently coloring vertices 1 or 2. Let the vertices appearing in \(V(\mu\triangle\eta)\) be colored 1 and its neighbors that are not in \(V(\mu\triangle\eta)\) be colored 2. Observe that the matching partner of the vertices which are not in \(V(\mu\triangle\eta)\) is same in both \(\mu\) and \(\eta\). Therefore, we search for a solution locally in vertices that are colored 1. Let _G_<sub>1</sub> be the graph induced on the vertices that are colored 1. At this stage

\begin{tabular}{cc}
\multicolumn{2}{c}{Local Search-ASM (LS-ASM)} \\
\multicolumn{2}{c}{**Input:** A bipartite graph \(G=(A\cup B,E)\), a set L containing the preference list of every vertex, a stable matching \(\mu\), and non-negative integers _k_, _q_, and _t_.} \\
\multicolumn{2}{c}{**Question:** Does there exist a matching \(\eta\) of size at least \(|\mu|+t\) with at most _k_ blocking edges such that the symmetric difference between \(\mu\) and \(\eta\) is at most _q_?} \\
\end{tabular}

