<tbc>this can be done efficiently.

We first show that (_x,S_)-activeness of edges from \(B'_0\) does not actually depend on _S_ and is determined by the set _R_<sub>0</sub>.

**Claim 16.** _Consider a vertex x lying on P. For each x-active edge_ \(e\in B'_0\) _and each subgraph X=T-S_+Inv(_S_) _satisfying_ \((F_0,R_0,B'_0)\)_, e is_ (_x,S)-active if and only if T-R_<sub>0</sub>+_e contains a path from x to_ \(x'(e)\).

_Proof of Claim 16._ Since _X_ satisfies \((F_0,R_0,B'_0)\), we have \(e\in B'_0\subseteq\mathrm{Inv}(R_0)\) and \(R_0\subseteq S\), which implies that \(e\in\mathrm{Inv}(S)\). Therefore, it remains to check that there is a path from _x_ to \(x'(e)\) in _T-S+e_ if and only if the same path is present in _T-R_<sub>0</sub>+_e_. One implication is trivial: if such a path exists in _T-S+e_, then _T-R_<sub>0</sub>+_e_ also contains this path because \(R_0\subseteq S\) and hence \(T-S+e\subseteq T-R_0+e\). We now show the converse implication.

Suppose that there is a path from _x_ to \(x'(e)\) in _T-R_<sub>0</sub>+_e_. Since _e_ is _x_-active, \(x'(e)\) is lower than _x_ on _P_, and hence _x_ is reachable from \(x'(e)\) in _T_. Then the path from _x_ to \(x'(e)\) must use the edge _e_. Let _a_ and _b_ be the starting and ending vertices of _e_, respectively. It follows that _T-R_<sub>0</sub> contains paths from _x_ to _a_ and from _b_ to \(x'(e)\).

Since \((F_0,R_0,B'_0)\) is a strict restriction triple and \(e\in B'_0\), the path in _T_ from _b_ to _a_ contains edges \(e_1,e_2\in R_0\). Moreover, it is guaranteed that all edges on the paths from _b_ to the start of _e_<sub>1</sub> and from the end of _e_<sub>2</sub> to _a_ belong to _F_<sub>0</sub>.

Since _e_ is _x_-active, _x_ lies on the path from _b_ to _a_. Then _x_ appears later than _e_<sub>2</sub> on this path because there is a path from _x_ to _a_ in _T-R_<sub>0</sub>. Consequently, all edges of the path from _x_ to _a_ are in _F_<sub>0</sub>. Since _X_ satisfies \((F_0,R_0,B'_0)\), \(S\cap F_0=\emptyset\), and therefore the path from _x_ to _a_ is present in _T-S_. Symmetrically, we can show that the path from _b_ to \(x'(e)\) is also present in _T-S_. Then these paths together with _e_ form a path from _x_ to \(x'(e)\) in _T-S+e_. \(\lrcorner\)

It follows that for each _x_-active edge \(e\in B'_0\) such that _T-R_<sub>0</sub>+_e_ contains a path from _x_ to \(x'(e)\), we must forbid a path from \(x'(e)\) to _v_.

For the edges from \(B\backslash B'_0\), we use a different idea. We first characterize their (_x,S_)-activeness using only the interaction between _P_ and _S_.

**Claim 17.** _Let X=T-S_+Inv(_S_) _with_ \(S\subseteq E(T)\) _be a subgraph that satisfies_ \((F_0,R_0,B'_0)\)_. Consider a vertex x lying on P. An x-active edge_ \(e\in B\backslash B'_0\) _is_ (_x,S)-active if and only if the subpath of P from_ \(x'(e)\) _to x contains an edge from S._

_Proof of Claim 17._ Let _a_ and _b_ be the starting and ending vertices of _e_, respectively. Since _e_ is _x_-active, the path from _b_ to _a_ in _T_ consists of paths from _b_ to \(x'(e)\), from \(x'(e)\) to _x_, and from _x_ to _a_.

Suppose that _e_ is (_x,S_)-active. Then \(e\in\mathrm{Inv}(s)\) for some \(s\in S\). By Observation 1, all such _s_ lie on the path from _b_ to _a_ in _T_. On the other hand, there must be a path in _T-S+e_ from _x_ to \(x'(e)\). Since \(x'(e)\) is lower than _x_, this path must use the edge _e_. Consequently, the paths in _T_ from _x_ to _a_ and from _b_ to \(x'(e)\) do not contain edges from _S_. Then _s_ must lie on the path from \(x'(e)\) to _x_.

Conversely, assume that there is an edge \(s\in S\) on the path from \(x'(e)\) to _x_. Then this edge also lies on the path from _b_ to _a_ in _T_. By Observation 1, it follows that \(e\in\mathrm{Inv}(s)\). Since _X_ satisfies \((F_0,R_0,B'_0)\) and \(e\in B\backslash B'_0\), _e_ cannot be an inverse edge to multiple elements of _S_, and hence _s_ is the only edge on the path from _b_ to _a_ that lies in _S_. Then _T-S_ contains the paths from _x_ to _a_<tbc>

