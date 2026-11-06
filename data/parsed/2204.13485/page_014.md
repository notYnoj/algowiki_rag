Note that, assuming the Unique Games Conjecture, the approximation given by Theorem 15 is best possible by Theorem 12.

**Remark 16.** If an arbitrary (not necessarily maximal) _q_-matching _M_ is given and the goal is to modify the preferences in such a way that there exists a stable _q_-matching containing _M_, then the problem becomes difficult. Indeed, deciding the existence of a stable matching containing a given edge in the stable marriage problem with ties is NP-complete, as was proved by Cseh and Heeger \[8\].

**Remark 17.** If the values are not allowed to be changed on the edges of _M_, then the problem becomes very simple even for hypergraphs. Indeed, in such a case one only has to go through the hyperedges _f_ not in _M_ and decrease the value of _p<sub>v</sub>(f_) to \(min_{e\in M(v)}p_v(e)\) at a vertex _v_ where the cost of such a change is minimum, that is, \(v\in argmin_{u\in f}|p_u(f)-min_{e\in M(u)}p_u(e)|\).

The technique described in the proof of Theorem 13 can be extended to a more general setting. Assume that for each vertex-edge pair \(v\in V\) and \(e\in E(v)\), nonnegative lower and upper bounds \(\ell_v(e),u_v(e)\) are given for the target value of _e_ at _v_. We call this problem \(\ell_1\)-min- pmri (minimum preference modification with restricted intervals).

\(\ell_1\text{-min-pmri}\)

<tbc>**Input:** A maximal _q_-matching _M_, a matrix _p_ describing the preferences of the agents, and nonnegative lower and upper bounds \(\ell,u\) on the values of the modified preferences.

**Goal:** Preferences \(p'\) of minimum cost such that _M_ is weakly stable with respect to \(p'\) and \(\ell_v(e)\le p'_v(e)\le u_v(e)\) for each \(v\in V\) , \(e\in E(v)\).

Note that this extra condition does not make the problem harder. First, one can apply the following preprocessing step: if \(p_v(e)\le\ell_v(e)\) for some vertex _v_ and \(e\in E(v)\), then change the value of _p<sub>v</sub>(e_) to \(\ell_v(e)\), and if \(p_v(e)\ge u_v(e)\) for some vertex _v_ and \(e\in E(v)\), then change the value of _p<sub>v</sub>(e_) to _u<sub>v</sub>(e_). It is not difficult to see that this results in an equivalent problem. After the preprocessing step, the problem can be simply encoded into LPs as before by changing each _LP<sub>v</sub>(v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_) as follows:

\(min\sum_{e\in E(v)}|x(e)-p_v(e)|\)<br>
\(\text{s. t.}0\le x(e_{j_i}^v)\le min_{e\in M(v)}x(e)\text{for}1\le i\le k\)<br>
\(0\le x(e)\le u_v(e)\text{for}e\in M\)<br>
\(\ell_v(e)\le x(e)\text{for}e\in E\backslash M\)

As a consequence, we have the following result.

**Corollary 18.** \(\ell_1\)-min-pmri _can be solved in polynomial time in bipartite graphs, and admits a polynomial-time 2-approximation in general graphs._

**Remark 19.** The proposed framework can also be extended to more general cases, for example when the cost for each individual agent might depend not only of the \(\ell_1\) norm of the changes, but on the agent itself - e.g., it might be a lot more difficult to get some agents to cooperate than others. This can be modeled by a cost function of the form \(cost(p')=\sum_{v\in V}\sum_{u\in N(v)}\lambda_v|p_v(u)-p'_v(u)|\), where \(\lambda_v\) is a constant that depends on the agent _v_. Such a cost function can be encoded in the LP by multiplying the objective of each _LP<sub>v</sub>(v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_) by \(\lambda_v\).

