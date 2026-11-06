**Definition B.14** (Independent Set (IS))**.** In the Clique problem we are given a simple graph _G_ and a value _k_. We have to decide if _G_ contains an independent set of size _k_ (i.e., a subgraph with _k_ vertices such that no vertex is connected to any other vertex)

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

**Definition B.15** (MaxCut)**.** In the MaxCut problem we are given a simple graph _G_ and a value _k_. We have to decide if there exist a subset of vertices \(S\subseteq V(G)\) such that there are at least _k_ many edges between _S_ and _V(G_)\\_S_.

Two problem instances (_G,k_) and \((G',k')\) are isomorphic if _G_ and \(G'\) are isomorphic as graphs and \(k=k'\).

**Definition B.16** (_k_-Median)**.** In the _k_-Median problem we are given a set of facilities _F_={_f_<sub>1</sub>_,...,f<sub>t</sub>_}, a set of clients _C_={_c_<sub>1</sub>_,...,c<sub>s</sub>_}, a function \(d:F\times C\rightarrow\mathbb{R}_{\ge 0}\), that satisfies the triangle inequality, a number _k_ and a number _c_. We have to decide if there are exist a set \(F'\subseteq F\) of size _k_ such that

\(\sum_{i=1}^smin_{f\in F^\prime} d(f,c_i)\le c.\)

Two problem instances (_F,C,d,k,c_) and \((F',C',d',k',c')\) are isomorphic if \(c=c'\), \(k=k'\), and there are bijections \(f:F\rightarrow F'\) and \(g:C\rightarrow C'\) such that \(d(x,y)=d'(f(x),g(y))\).

**Definition B.17** (Satisfiability (SAT))**.** In the Satisfiability problem we are given a formula \(\Phi\) in conjunctive normal form (CNF). We have to decide if \(\Phi\) is decidable.

Two CNF formulas \(\Phi\), \(\Phi'\) are isomorphic if \(\Phi'\) can be obtained from \(\Phi\) by a renaming of variables. Note that this renaming is consistent with negation (i.e., if we rename _x_ to _y_ then \(\neg x\) is mapped to \(\neg y\)).

**Definition B.18** (3-Satisfiability (3-SAT))**.** In the 3-Satisfiability problem we are given a formula \(\Phi\) in conjunctive normal form (CNF) such that each clause contains exactly three literals. We have to decide if \(\Phi\) is decidable.

Two CNF formulas \(\Phi\), \(\Phi'\) are isomorphic if \(\Phi'\) can be obtained from \(\Phi\) by a renaming of variables. Note that this renaming is consistent with negation (i.e., if we rename _x_ to _y_ then \(\neg x\) is mapped to \(\neg y\)).

**Definition B.19** (Max _k_-SAT)**.** In the Max _k_-SAT we are given a formula \(\Phi\) in conjunctive normal form (CNF) such that each clause contains exactly _k_ literals. Given an assignment _x_ of variables we write \(|\Phi(x)|\) for the number of clauses that are satisfied by _x_. We have to return \(max_x|\Phi(x)|\).

Two CNF formulas \(\Phi\), \(\Phi'\) are isomorphic if \(\Phi'\) can be obtained from \(\Phi\) by a renaming of variables. Note that this renaming is consistent with negation (i.e., if we rename _x_ to _y_ then \(\neg x\) is mapped to \(\neg y\)).

**Definition B.20** (Set Cover)**.** In the Set Cover problem we are given a number _n_, a list of subsets \(S_1,\dots,S_m\subseteq[n]\), and a number _k_. We have to decide if there are indices _j_<sub>1</sub>_,...j<sub>s</sub>_ such that \(s\le k\) and \(\bigcup_{t=1}^sS_{j_t}=\bigcup_{i=1}^mS_i\).

Two problem instances (_S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) and \((S'_1,\dots,S'_{m^\prime},n',k')\) are isomorphic if \(m=m'\), \(k=k'\), \(n=n'\) and there are bijective functions \(f:[n]\rightarrow[n']\) and \(g:[k]\rightarrow[k']\) such that for each \(i\in[m]\) we obtain \(f(S_i)=\{f(s)|s\in S_i\}=S'_{g(i)}\).

**Definition B.21** (Set Packing)**.** In the Set Packing problem we are given a family of sets S={_S_<sub>1</sub>_,...,S<sub>m</sub>_} with \(S_i\subseteq[n]\) and a number _k_. We have to decide if there exist _k_ many mutually disjoint sets in S.

