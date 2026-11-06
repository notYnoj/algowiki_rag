## 4 Preference modifications

In this section, we consider problems where the goal is to make a given matching stable by bribing the agents to change their preferences. Each agent _v_ assigns a nonnegative real number _p<sub>v</sub>(u_) to each acceptable partner _u_. By abuse of notation, we extend this notation to edges incident to _v_ by setting _p<sub>v</sub>(uv_):=_p<sub>v</sub>(u_), and call this the _value_ of the edge _uv_ for _v_. The weak preference list of _v_ is derived from these values by declaring \(u\ge_vu'\) if and only if \(p_v(u)\ge p_v(u')\). The agents might also have positive integer capacities, denoted by _q(v_) for agent _v_.

The cost of modifying the preferences can be measured in various ways; here, we concentrate on the case of \(\ell_1\)-norm. That is, changing the value of _p<sub>v</sub>(u_) from _a_ to _b_ has cost |_a-b_|. If \(p'\) denotes the modified preference values, then the _cost of_ \(p'\) _(with respect to p)_ is \(\text{cost}(p'):=\sum_{v\in V}\sum_{u\in N(v)}|p_v(u)-p'_v(u)|\). The goal is to find a new preference matrix \(p'\) of minimum cost such that a given b-matching _M_ becomes weakly stable with respect to \(p'\).

First we show that the problem is not only NP-hard in general, but it is also hard to approximate within a factor better than 2.

**Theorem 12.** \(\ell_1\)-min-pm _is NP-hard even if each capacity is one. Furthermore, assuming the Unique Games Conjecture, it cannot be approximated within a factor of_ \(2-\varepsilon\) _for any_ \(\varepsilon>0\).

_Proof._ Observe that if each capacity is 1, then there always exists an optimal solution that changes the values only on the edges of _M_. Indeed, lowering the value of a non-matching edge _uv_ to become dominated at vertex _v_ has the same cost as increasing the value of the edge in _M(v_) for _v_ to dominate _uv_. By doing the latter, we are surely better off as other edges may become dominated too at _v_, while in the first case we do not make any progress on dominating the other edges.

The problem is clearly in NP. To show NP-hardness, we reduce from vertex-cover. Let _G_=(_V,E_) be an instance of the minimum vertex cover problem. We construct an instance \((G'=(V',E'),p,M)\) of \(\ell_1\)-min-pm. Let \(V'=\{v',v''|v\in V\}\) and \(E'=\{u'v'|uv\in E\}\cup\{v'v''|v\in V\}\). Furthermore, set \(M=\{v'v''|v\in V\}\). For each vertex \(v\in V\) , we define \(p_{v^\prime}(v'')=p_{v^{\prime\prime}}(v')=0\) and set all the other \(p_{v^\prime}(u')\) values to be 1, see Figure 2.

Let \(p'\) be a minimum cost solution of the \(\ell_1\)-min-pm instance thus obtained. By the observation above, we may assume that \(p'\) differs from _p_ only on edges of _M_. Since vertices in \(\{v''|v\in V\}\) are matched with their only partner, their preference values do not change. Clearly, for each vertex \(v'\), we have either \(p'_{v^\prime}(v'')=0\) or \(p'_{v^\prime}(v'')=1\). Furthermore, at least one of the end vertices of each original edge increases the value of the incident matching edge to 1, hence the set of such vertices forms a vertex cover. Vice versa, if we increase the values of the matching edges on the vertices of a vertex cover, then no original edge of _G_ blocks _M_.

By the above, minimum vertex cover in _G_ is equivalent to \(\ell_1\)-min-pm in \((G',p,M)\), concluding the proof of NP-hardness. Assuming the Unique Games Conjecture, vertex-cover cannot be approximated within a factor better than 2 by a result of Khoth and Regev \[19\], implying the second half of the theorem.

As a positive result, we show that \(\ell_1\)-min-pm is polynomial-time solvable in bipartite graphs. Interestingly, our solution relies on Hochbaum’s algorithm for the minimum cost vertex cover problem under bipartite-submodular functions.

\begin{tabular}{cc}
\multicolumn{2}{c}{\(\ell_1\)-min-pm} \\
\multicolumn{2}{c}{**Input:** A maximal _q_-matching _M_ and a matrix _p_ describing the preferences of the agents.} \\
\multicolumn{2}{c}{**Goal:** Preferences \(p'\) of minimum cost such that _M_ is weakly stable with respect to \(p'\).} \\
\end{tabular}

