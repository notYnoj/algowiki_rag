holds for minimum fill-in, lis-(\(\text{tw}\le t\)) and max-(\(\text{tw}\le t,\varphi\)). Combining Theorem 1 with contributions in \[12, 14, 16\], we obtain the following corollary.

**Corollary 1.** _Given a graph G, an integer_ \(t\ge 0\) _and a CMS formula_ \(\varphi\)_, we have:_

• treewidth _and_ minimum fill-in _can be solved in_ \(\tilde{O}(|\Pi_G|)\),<tbc>

• lis-\((\text{\textit{tw}}\le t)\) _can be solved in_ \(O(n^{O(t)}|\Pi_G|)\),<tbc>

• max-\((\text{\textit{tw}}\le t,\varphi)\) _can be solved in_ \(O(n^{O(t)}\cdot f(t,\varphi)\cdot|\Pi_G|)\),

_without the need to possess initially the list of PMCs._

Let us describe briefly our approach for Theorem 1. Our algorithm, called PMC-Traversal, reuses some principles of BT-enum while developing a new technique which allows to decrease the overall running time. It is also recursive: it enumerates all PMCs by launching first a recursive call on a subgraph _G_\\{_a_} with an arbitrary vertex \(a\in V\) . The PMCs of _G_ containing _a_ - formed like \(S\cup\{a\}\) or \(\Omega'\cup\{a\}\) - are listed as in BT-enum. Also, as in BT-enum, all PMCs of _G_ which were PMCs of _G_\\{_a_} are enumerated easily thanks to the recursive call. The major difference between both algorithms lies in the way to enumerate PMCs of _G_ which are neither PMCs of _G_\\{_a_} nor containing _a_. Instead of listing brute-forcely all pairs of minimal separators of _G_, we introduce a novel and completely different technique to achieve this task: we execute a traversal of some "PMC-graph", whose nodes are PMCs and edges define a notion of neighborhood between PMCs. This approach was inspired by the _Proximity Search_ framework \[10\].

More concretely, we define a neighborhood relation \(\mathcal{N}\in\Pi_G\times\Pi_G\) which associates any PMC with a collection of neighbors. Relation N is fast to handle, since any PMC admits at most _n_<sup>2</sup> neighbors and, moreover, these neighbors can be computed in time polynomial in _n_. The PMC-graph mentioned above is then the graph \((\Pi_G,\mathcal{N})\). Naturally, this graph is partially known even after exploiting the recursive call, since otherwise all PMCs would have already been listed. Our idea consists of traversing the PMC-graph, starting from the PMCs already enumerated (PMCs containing _a_ or PMCs of _G_\\{_a_}), exploring their neighbors through N and so on. Said differently, we launch a _Breadth-First Search_ (BFS) whose initial queue contains the PMCs already enumerated, and the edges visited are given by relation N. We show that this procedure allows us to attain any PMC of _G_.

By the way, a large part of the paper is dedicated to the proof of this latter statement. An essential tool to complete this proof consists, at some moment, in deciding whether some given set _X_ contains (or not) a PMC \(\Omega\subseteq X\), and, if yes, producing such \(\Omega\). We call this problem PMC Superset. Observe that PMC Superset is a special case of PMC Extension defined above, fixing \(M=\emptyset\). We show that PMC Superset is polynomial-time solvable.

**Theorem 2.** _There is an algorithm deciding_ PMC Superset _in time O(n_<sup>3</sup>_m). Furthermore, for a yes-instance, it produces a solution PMC._

One may wonder what is the computational complexity of the more general PMC Extension problem, since a polynomial-time algorithm for it would imply polynomial delay for PMC enumeration, which is stronger than Theorem 1. We provide a NP-hardness proof, using a 3-SAT reduction. This proof is preceded by another NP-hardness reduction for Minimal (_a,b_)-separator Extension which stands as an intermediary step.

**Theorem 3.** PMC Extension _is NP-complete._

