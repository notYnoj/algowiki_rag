<tbc>is not the chosen satisfying literal in _C<sub>j</sub>_, then \(c_j^s\) is matched to their first choice \((p_j^s)\) in _M_, so they cannot block with \(x(c_j^s)\).

For the other direction, suppose that _M_ is a perfect matching in _I_ such that no agent in _D_ is in a blocking pair. As _M_ is perfect, either \(M_{V_i}^1\subseteq M\) or \(M_{V_i}^2\subseteq M\) for every variable gadget _G<sub>V<sub>i</sub></sub>_ (\(1\le i\le n\)), and either \(M_{C_j}^1\subseteq M\), \(M_{C_j}^2\subseteq M\) or \(M_{C_j}^3\subseteq M\) for the clause gadget _G<sub>C<sub>j</sub></sub>_ (\(1\le j\le m\)). We define a truth assignment _f_ of _B_ as follows. For each variable \(V_i\in V\) , if \(M_i^1\subseteq M\) then set _f(V<sub>i</sub>_) to true, otherwise (it must be true that \(M_{V_i}^2\subseteq M\)) set _f(V<sub>i</sub>_) to false. Naturally, this yields a valid truth assignment. We now show that it satisfies _B_. Suppose for the sake of contradiction that there exists a clause \(C_j\in C\) such that no literal in _C<sub>j</sub>_ is satisfied. Consider the matching \(M_{C_j}^s\subseteq M\) corresponding to the clause gadget _G<sub>C<sub>j</sub></sub>_. By construction, it must be the case that \(\{c_j^s,q_j\}\in M_j^s\) and agent \(c_j^s\) prefers \(x(c_j^s)\) to their partner in _M_. However, because \(c_j^s\in D\) and we assume that no agent in _D_ is in a blocking pair, we know that \(x(c_j^s)\) has a partner better than \(c_j^s\). Hence, by construction, either \(C_j^s\) is an unnegated literal, and we have already set the corresponding variable to true, or \(C_j^s\) is a negated literal and we have already set the corresponding variable to false. In both cases, _f_ satisfies \(C_j^s\), which is a contradiction.

Our claim above immediately establishes that 0-Deviator-Perfect-smi-Dec is NP-hard. Notice that every agent in our construction has a preference list of length at most 3, and that all agents in _D_ are on the same side of the bipartition where the _c,y_ and _z_ agents are on one side, and the _p,q_ and _x_ agents are on the other side. This also completes the proof that 0-Deviator-Perfect-smi-Dec is NP-complete.

We can immediately conclude the following intractability result for our original optimisation problem.

**Corollary 3.2.** _k_-Deviator-Max-smi _is_ para-NP-hard _with respect to k and, in particular, is_ NP-complete _even when k_=0 _and all preference lists are of length at most 3 and all deviators are on the same side. Thus,_ Deviator-Max-smi _is_ NP-hard _in equally restricted settings, and cannot be in_ XP _with respect to the optimum parameter value, unless_ P=NP.

Note that these hardness results no longer apply when preference lists are complete, since then every stable matching is a maximum-cardinality matching \[43\].

**Remark 3.3.** _A reviewer of a preliminary version of this paper pointed out that a new analysis of the reduction in the proof of Theorem 3 of \[28\] can also establish that_ 0-Deviator-Max-smi _(which we newly introduced in this paper) is_ NP-hard_, although not for preference lists of length at most 3. However, given that we establish in Section 6 that k_-Deviator-Max-smi _is in_ P _for instances with lists of length at most 2, there is direct merit in our reduction, as it establishes a tight complexity frontier with respect to the preference list length._

## 3.2 Deviator-Stable Matchings in General Acceptability Graphs

We now turn to the general case, where matchings may have arbitrary size, and the acceptability graph need not be bipartite. We start by defining a restricted version of Deviator-sri as follows.

_k_-Deviator-sri<br>
**Input:** sri instance \(I=(A,\succ)\) and a subset \(D\subseteq A\).<br>
**Output:** A matching \(M\in\mathcal{M}\) such that \(|\bigcup_{a_i\in D}bp_{a_i}(M)|\le k\), if one exists.

Again, we will focus on the very restricted case of _k_=0, where we require a matching in which no agent in _D_ is in a blocking pair, and denote the problem of deciding whether 0-Deviator-sri admits a solution by 0-Deviator-sri-Dec.

We start with the following observation about a special class of 0-Deviator-sri instances.

