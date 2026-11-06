<tbc>we construct a matching _N_<sub>2</sub> in the extended bipartite graph by adding \(v_e^uu_j\) to _N_<sub>2</sub> for each \(v_eu_j\in N_1\).

_Phase 3:_ Starting from the matching _N_<sub>2</sub>, we check whether there exists a matching that covers all vertices of _U_ using the Hungarian method \[21\]. If no such matching exists, then the preferences cannot be extended in such a way that _M_ is a stable _q_-matching and the lower bounds are met, and the algorithm stops with the answer ‘NO’. If there exists such a matching, then a nice feature of the algorithm is that once a vertex becomes covered, it remains so throughout. Hence, for each edge _e=xy_, one of the vertices \(v_e^x\) and \(v_e^y\) is covered. We denote the resulting matching by _N_<sub>3</sub>.

_Phase 4:_ We further extend _H_ by adding all the copies of each vertex \(u\in V\) to _U_ that have not been added in Phase 1. Also, we extend the set of edges such that there is an edge \(u_jv_e^u\) for each \(u\in V\) , \(e\in E(u)\backslash M(u)\) and \(j\ge\ell_u(e)\). Consider the vertices corresponding to edges _e_ that were isolated until the addition of the new edges, that is, satisfied \(\ell_u(e)\ge min\{p_u(f)|f\in M(u)\}\). We check if these vertices can all be matched to vertices not covered by _N_<sub>3</sub> by running the Hungarian algorithm. If no such matching exists, then there is no preference extension satisfying the lower bounds at all, and the algorithm outputs ‘NO’.

Otherwise, let _N_<sub>4</sub> denote the matching obtained. We claim that the matching \(N_3\cup N_4\) can be extended to a matching in such a way that it covers all vertices in _H_. To see this, observe that only lower bounds are given and for each remaining copy \(v_e^u\) of an edge, the lower bound \(\ell_u(e)\) is smaller than the indices of the uncovered copies of _u_. Indeed, all \(v_e^u\) vertices with \(l_u(e)\ge min\{p_u(f)|f\in M(u)\}\) are matched by _N_<sub>4</sub>, and for each \(u\in V\) the copies _u<sub>j</sub>_ with \(j\le min\{p_u(f)|f\in M(u)\}\) are matched by _N_<sub>3</sub>. Therefore, the graph induced by the unmatched vertices consists of a union of complete bipartite graphs with equal sized color classes, so it admits a perfect matching _N_<sub>5</sub>.

Setting the preferences according to \(N_3\cup N_4\cup N_5\) gives a preference extension that satisfies all conditions.

**Remark 31.** Theorems 29 and 30 can be straightforwardly extended to hypergraphs. That is, given a hypergraph _H_=(_V,_E), vertex capacities \(q\in\mathbb{Z}_+^V\), a feasible _q_-matching \(M\subseteq\mathcal{E}\), preference values _p<sub>v</sub>(f_) for \(v\in V\) and \(f\in M(v)\), preference values for some other vertex- hyperedge pairs, and lower bounds \(\ell_v(f)\) for \(v\in V\) , \(f\in E(v)\), one can decide in polynomial time if there exists a preference extension for which _M_ is stable.

A further extension would be to consider _q_-matchings _M_ that are not necessarily inclusion- wise maximal. Let _M_ be an arbitrary _q_-matching and suppose that the places in the preference lists of the agents are fixed for the edges of _M_ for each saturated vertex and maybe on some other vertex-edge pairs, too. The goal is to set the remaining preferences in such a way that there exists a stable _q_-matching \(M'\) containing _M_.

Forced-SPE

**Input:** A graph _G_=(_V,E_), vertex capacities \(q\in\mathbb{Z}_+^V\), a feasible _q_-matching \(\mu\subseteq E\), preference values _p<sub>v</sub>(e_) for each saturated vertex \(v\in V\) and \(e\in\mu(v)\), and preference values for some other vertex-edge pairs.

**Question:** Does there exist a preference extension together with a stable _q_-matching _M_ for which \(\mu\subseteq M\)?

Surprisingly, this problem becomes NP-complete even for the stable marriage case.

**Theorem 32.** forced-spe _is NP complete even for bipartite graphs with capacity one on each vertex._

