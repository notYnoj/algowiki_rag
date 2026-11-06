_k_-Max-AlmostStable-sri<br>
**Input:** sri instance \(I=(A,\succ)\) and a non-negative integer _k_.<br>
**Question:** Does there exist a matching \(M\in\mathcal{M}\) such that \(max_{a_i\in A}|bp_{a_i}(M)|\le k\)?

It is easy to see that if _k_-Max-AlmostStable-sri cannot be solved in polynomial time, then Minimax-AlmostStable-sri cannot be solved in polynomial time. Notice that _I_ is a yes-instance to 0-Max-AlmostStable-sri if and only if _I_ is solvable, so this case is tractable \[34\]. Notice, furthermore, that _k_-Max-AlmostStable-sri is trivial if _k_ exceeds the maximum preference list length. In Section 4.2, we will highlight, though, that _k_-Max-AlmostStable- sri is NP-complete even in the very restricted case where _k_=1, and regardless of whether preference lists are bounded or complete. We will extend this result to any positive constant _k_ (but with weaker bounds on the preference list lengths) in Section 4.4.

We will then turn our attention to Minimax-AlmostStable-Max-smi. For our complexity analysis, we will consider a restricted decision version of this problem (where maximum- cardinality matchings are perfect), which we define as follows.

_k_-Max-AlmostStable-Perfect-smi<br>
**Input:** smi instance \(I=(A,\succ)\) and a non-negative integer _k_.<br>
**Question:** Does there exist a matching \(M\in\mathcal{M}^p\) such that \(max_{a_i\in A}|bp_{a_i}(M)|\le k\)?

It is easy to see that if _k_-Max-AlmostStable-Perfect-smi cannot be solved in polynomial time, then Minimax-AlmostStable-Max-smi cannot be solved in polynomial time. Notice that _I_ is a yes-instance to 0-Max-AlmostStable-Perfect-smi if and only if there exists a perfect stable matching of _I_. This can be decided in polynomial time by computing an arbitrary stable matching _M_ of _I_ using the classical Gale-Shapley algorithm \[20\], and checking whether _M_ is a perfect matching. It is well-known that all stable matchings of a given smi instance have the same size \[21\], so if _M_ is not perfect, then _I_ does not admit any perfect stable matching. In Section 4.3, we will highlight, though, that _k_-Max-AlmostStable-Perfect- smi is NP-complete even in the very restricted case where _k_=1 and preference lists are very short. We will extend this result to any positive constant _k_ and even to a linear dependence (within some arbitrarily small \(\varepsilon\)) on the number of agents in Section 4.4.

## 4.2 Hardness in General Bounded-Degree Graphs and Cliques

The result below states that it is impossible to distinguish in polynomial time even between instances that admit a matching in which every agent is in at most one blocking pair, and instances where every matching requires at least one agent to be in more than one blocking pair (unless P=NP), even when preference lists are of bounded length.

**Theorem 4.1.** _k_-Max-AlmostStable-sri _is_ NP-complete_, even if k_=1 _and all preference lists are of length at most 10._

_Proof._ We first note that, given a matching _M_ of an sri instance, we can verify in polynomial time whether _M_ is a solution to _k_-Max-AlmostStable-sri by iterating through the preference lists of the agents and keeping track of the maximum number of blocking pairs that any agent is contained in. Clearly, blocking pairs can be detected efficiently by comparison of preference list entries to partners in _M_. Hence, _k_-Max-AlmostStable-sri is in NP.

To show that _k_-Max-AlmostStable-sri is NP-hard, we will reduce from the previously defined NP-complete problem (2,2)-e3-sat to 1-Max-AlmostStable-sri. Suppose that _B_ is a boolean formula given as an instance of (2,2)-e3-sat, where _V_={_V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>n</sub>_} is the set of variables and _C_={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>m</sub>_} is the set of clauses. We will denote a clause by \(C_s=(C_s^1\vee C_s^2\vee C_s^3)\), where each \(C_s^l\) (for \(1\le s\le m\) and \(1\le l\le 3\)) is either an unnegated<tbc>

