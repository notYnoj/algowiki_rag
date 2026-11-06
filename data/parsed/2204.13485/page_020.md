does not get a selector. If _x<sub>j</sub>_ was matched to \(c_j^2\) or \(c_j^3\), then \(x_jc_j^1\) would block, so it is matched to \(c_j^1\).

In summary, for each set gadget, we must match either at least one selector agent or all three element agents to it in any stable matching. Therefore, if there is a stable matching _M_, then all set gadgets in _M_ must get either a selector or three element agents. But there are 2_n_ selectors only, so there must be at least _n_ set gadgets that can only get element agents. By the above observation, each must get exactly three of those, so these _n_ sets must form an exact cover.

The following corollary provides a different interpretation of Theorem 26.

**Corollary 27.** srt _is NP complete even if the graph is complete and each preference list is either strict or a single tie._

As a positive result, we show that the problem becomes tractable when the preferences are fixed for agents forming an independent set in the graph.

**Theorem 28.** _If the preferences are only fixed on an independent set, then_ sr-strat _is polynomial-time solvable._

_Proof._ Let the agents with fixed preference lists be _v_<sub>1</sub>_,...,v<sub>k</sub>_. For \(i\in[k]\), we do the following. Let _v<sub>i</sub>_ choose its best available partner _u<sub>i</sub>_ if there is any, add _u<sub>i</sub>v<sub>i</sub>_ to _M_, and set _u<sub>i</sub>_’s preference such that _v<sub>i</sub>_ is the best. Then find an inclusionwise maximal matching among the rest of the vertices, add it to _M_, and set the preference of each remaining vertex in a way that it prefers its partner the most. It follows from the construction that the matching thus obtained is stable.

## 5.2 Fixed entries in the preference lists

We move on to problems where the preference lists of the agents have some fixed places that cannot be modified. The setting we concentrate on is the following. We are given a graph _G_=(_V,E_) with vertex capacities _q(v_) for \(v\in V\) and an inclusionwise maximal feasible _q_- matching \(M\subseteq E\). For a saturated vertex _v_ and edge \(e\in M(v)\), we have a fixed number _p<sub>v</sub>(e_) denoting that _e_ is the _p<sub>v</sub>(e_)-th worst edge in _v_’s ranking on the incident edges. Furthermore, a similar _p<sub>v</sub>(e_) value might be given for other vertex-edge pairs as well. Note that the _p<sub>v</sub>(e_) values for \(e\in M(v)\) where _v_ is non-saturated are not interesting in the sense that no edge can be dominated at such a vertex. The task is to determine whether there exists an extension of these partial preference lists such that the given _q_-matching _M_ is stable. Such an extension is called a _stable preference extension_. In a sense, this problem is the inverse of the stable _q_-matching problem, where the preferences are set in advance and the task is to find a stable _q_-matching _M_.

INC-MAX-SPE

Input: A graph _G_=(_V,E_), vertex capacities \(q\in\mathbb{Z}_+^V\), an inclusionwise maximal feasible _q_-matching \(M\subseteq E\), preference values _p<sub>v</sub>(e_) for each saturated vertex \(v\in V\) and \(e\in M(v)\), and preference values for some other vertex-edge pairs.

Question: Does there exist a preference extension for which _M_ is stable?

We show that the problem of finding a stable preference extension can be reduced to computing a maximum stable matching in a bipartite graph.

**Theorem 29.** _For any graph G_=(_V,E), q-matching M and partial preference p which fixes p<sub>v</sub>(e_) _for each saturated vertex v and each edge_ \(e\in M\) _containing v,_ inc-max-spe _an be solved in polynomial time._

