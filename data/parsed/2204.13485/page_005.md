The following two versions of the stable marriage with ties problem was proven to be NP- complete by Cseh and Heeger \[8\].

A _one-sided preference model_ involves a bipartite graph _G_=(_A,B;E_) and linear orders _\><sub>a</sub>_ on _N(a_) for every \(a\in A\). A matching _M_ is _Pareto-optimal_ if there is no matching \(M'\) that is better than _M_ for some agent in _A_, and at least as good as _M_ for the other agents in _A_. Some hardness proofs in Section 5 will be based on the following NP-complete problem, introduced by Abraham et al. \[2\].

Given a bipartite graph _G_=(_A,B;E_) with preferences for each \(a\in A\) and a matching _M_, a _coalition_ is a cycle (_a_<sub>1</sub>_,b_<sub>1</sub>_,a_<sub>2</sub>_,...,b<sub>r</sub>_), such that \(a_ib_i\in M\) for each \(i\in[r]\) and each agent prefers _b_<sub>_i_+1</sub> to _b<sub>i</sub>_. The matching is _non-wasteful_ if there is no element of _B_ that is not covered by _M_, but is preferred by an agent in _A_ to his current partner. Abraham et al. verified the following.

**Theorem 3** (Abraham et al.)**.** _A matching M (in the one sided preference model) is Pareto- optimal if and only if it is maximal, non-wasteful, and coalition-free._

## 3 Vertex deletion

In this section, we study the problem of removing vertices so that the remaining graph has a stable matching. Two variants are considered: in the first one, the aim is to remove the minimum number of vertices, while in the second one, an arbitrary number of vertices can be removed, but only from a given vertex subset \(T\subseteq V\) .

Let _G_=(_V,E_) be a graph with strict preferences _\><sub>v</sub>_ for each vertex \(v\in V\) . A vertex set \(S\subseteq V\) is _removable_ if _G-S_ admits a stable matching. When vertex capacities _q(v_) are considered, a vertex set \(S\subseteq V\) is _removable_ if _G-S_ admits a stable _q_-matching.

COM-SMTI
Input: An instance (G = (A, B; E),>) of the stable marriage problem in which ties only occur at some vertices in B with exactly two neighbors.
Question: Is there a perfect weakly stable matching?

1-FORCED-SMTI
Input: An instance (G = (A, B; E),>) of the stable marriage problem with ties and a forced edge e E.
Question: Is there a weakly stable matching containing e?
1-FORBIDDEN-SMTI
Input: An instance (G = (A, B; E),>) of the stable marriage problem with ties and a forbidden edge E E.
Question: Is there a weakly stable matching not containing f?

MIN-POM
Input: A bipartite graph G = (A, B; E) with preferences for each a A and a non- negative integer k.
Question: Does there exist a Pareto-optimal matching of size at most k?

