• \((u,v)\in\mathrm{Inv}(e_1)\cap\mathrm{Inv}(e_2)\);<tbc>

• every edge of the path in _T_ from _v_ to the start of _e_<sub>1</sub> belongs to _F_;<tbc>

• every edge of the path in _T_ from the end of _e_<sub>2</sub> to _u_ belongs to _F_.

If a subgraph _X=T-S_+Inv(_S_) satisfies such a strict triple, then \(e_1,e_2\in R\subseteq S\), so these two edges are absent from _X_. Conversely, edges of the path before _e_<sub>1</sub> and after _e_<sub>2</sub> must belong to _X_ because they are present in _F_ and \(S\cap F=\emptyset\).

Given a strict restriction triple, we can filter the family of subgraphs _T-S_+Inv(_S_) satisfying it: a constraint set, constructed in the next lemma, keeps exactly those subgraphs that avoid the forbidden path. This is by far the most difficult part of our XP-algorithm.

**Lemma 9.** _Let_ (_G,_**w**) _be a digraph with edge weights. For every_ \(u,v\in V(G)\) _and every strict restriction triple_ \((F_0,R_0,B'_0)\)_, there exists a constraint set_ C _such that:_

• _For every_ \(S\subseteq E(T)\)_, let X=T-S_+Inv(_S). If X satisfies_ C_, then X contains no directed path from u to v. Conversely, if X satisfies_ \((F_0,R_0,B'_0)\) _and contains no directed path from u to v, then X satisfies_ C.<tbc>

• _For each_ \((F,R,B')\in\mathcal{C}\)_, it holds that_ \(B'=B'_0\), \(F_0\subseteq F\), \(R_0\subseteq R\)_, and each of the sets F_\\_F_<sub>0</sub> _and R_\\_R_<sub>0</sub> _can be represented as a union of at most_ \(|B'_0|+1\) _directed paths in T._

_Proof._ We first show how to construct a constraint set with the needed properties if _T_ contains a directed path _P_ from _v_ to _u_. This case is essential for the general construction. For two vertices on _P_, we say that the higher of them is the one that appears later on _P_ (i.e., closer to _u_). The second vertex is then lower.

Let \(x\neq v\) be a vertex lying on _P_. Our approach is based on the fact that if a subgraph of the form _T-S_+Inv(_S_) contains a path from _x_ to _v_, then there always exists such a path of the specific structure: it has a prefix that leads to some vertex \(x'\) on _P_ that is lower than _x_ and consists of tree edges and _exactly one blocked edge_. Moreover, given a blocked edge on this prefix, we can identify the corresponding \(x'\).

For a blocked edge _e_=(_a,b_), let \(x'(e)\) be the first vertex on the path in _T_ from _b_ to _a_ that belongs to _P_. If this path does not contain vertices from _P_, we leave \(x'(e)\) undefined. We say that _e_ is _x_-active if _a_ is reachable from _x_ in _T_, \(x'(e)\) is defined and lower than _x_. Intuitively, an _x_-active edge is a candidate for the unique blocked edge in the path prefix described above. Note that if _e_ is _x_-active, then the path in _T_ from _b_ to _a_ consists of paths from _b_ to \(x'(e)\), from \(x'(e)\) to _x_ (such a path exists because \(x'(e)\) is lower than _x_ on _P_), and from _x_ to _a_.

When we consider a specific subgraph _T-S_+Inv(_S_), not every _x_-active edge can be used in the path prefix: indeed, some _x_-active edges may be not present in the subgraph. Even if an edge is present, some needed tree edges may be outside _T-S_. We say that _e_ is (_x,S_)-active if _e_ is _x_-active, \(e\in\mathrm{Inv}(S)\), and _T-S+e_ contains a directed path from _x_ to \(x'(e)\).

We then formalize the discussion above as follows.

**Claim 15.** _Consider a vertex_ \(x\neq v\) _lying on P and a subgraph X=T-S_+Inv(_S_) _with_ \(S\subseteq E(T)\)_. X contains a directed path from x to v if and only if there exists_ \(e\in B\) _such that:_

• _e is_ (_x,S)-active;_<tbc>

• _X contains a directed path from_ \(x'(e)\) _to v._<tbc>

