## 7.1 Constrained Shortest Path and Energy Game

**Definition 7.1** (Constrained Shortest Path (CSP))**.** An instance of Constrained Shortest Path is defined by a tuple \(G=(V,E,c,\ell,s,t,B)\), where:

• (_V,E_) is a finite directed graph.<tbc>

• \(c:E\rightarrow\mathbb{R}_{\ge 0}\) is a cost function assigning a non-negative cost to each edge.<tbc>

• \(\ell:E\rightarrow\mathbb{R}_{\ge 0}\) is a length (or delay) function assigning a non-negative length to each edge.<tbc>

• \(s,t\in V\) are the distinguished source and target vertices.<tbc>

• \(B\in\mathbb{R}_{\ge 0}\) is the maximum allowable path cost constraint.

For a directed path _P_=(_e_<sub>1</sub>_,...,e<sub>r</sub>_) from _s_ to _t_, the total cost is \(c(P)=\sum_{i=1}^rc(e_i)\) and the total length is \(\ell(P)=\sum_{i=1}^r\ell(e_i)\). The objective is to find a feasible path _P_<sup>∗</sup> minimizing _c(P_<sup>∗</sup>) subject to \(\ell(P^*)\le B\). The optimal value is _OPT(G_)=_c(P_<sup>∗</sup>). If no path satisfies the length constraint, \(OPT(G)=\infty\).

Two problem instances \(G=(V,E,c,\ell,s,t,B)\) and \(G'=(V',E',c',\ell',s',t',B')\) of CSP are isomorphic if \(B=B'\) and their underlying graphs are isomorphic. Note that an isomorphism has to preserve vertex attributes and edge attributes (e.g., _s_ maps \(s'\), _t_ maps \(t'\), etc.).

Naturally, CSP with isomorphic priors is formalized as follows. In the preprocessing phase, we are given a database S={_G_<sub>1</sub>_,...,G<sub>k</sub>_} of _k_ prior instances. Each instance is given as a tuple \(G_i=(V_i,E_i,c_i,\ell_i,s_i,t_i,B_i)\), provided together with its optimal value _OPT(G<sub>i</sub>_). In the query phase, we receive a query graph \(G=(V,E,c,\ell,s,t,B)\).

**Theorem 7.2** (CSP in the Isomorphic-Priors Model)**.** _There is an algorithm that solves the_ CSP _problem with k prior instances each having at most n vertices and m edges in O(k(n+m_)log_n_) _preprocesses time and O_((_n+m_)log_n_) _query time. Additionally, if each prior G<sub>i</sub> is equipped with an optimal path, then the optimal path for the query graph can be found in O_((_n+m_)log_n_) _query time._

**Definition 7.3** (Energy Game)**.** An Energy Game instance is defined by a tuple _G_=(_V,E,V_<sub>1</sub>_,V_<sub>2</sub>_,w,v_<sub>0</sub>), where:

• (_V,E_) is a finite directed graph with no terminal states.<tbc>

• _V_<sub>1</sub>_,V_<sub>2</sub> is a partition of \(V(V_1\cup V_2=V\), \(V_1\cap V_2=\emptyset)\), where Player 1 controls _V_<sub>1</sub> and Player 2 controls _V_<sub>2</sub>.<tbc>

• \(w:E\rightarrow\mathbb{Z}\) is a weight function assigning an integer energy change to each edge.<tbc>

• \(v_0\in V\) is the designated initial vertex.

A play \(\pi=v_0v_1v_2\dots\) is formed by moving a token: at step \(k\ge 0\), if \(v_k\in V_i\), Player _i_ chooses an outgoing edge \((v_k,v_{k+1})\in E\). Given an initial energy \(E_0\in\mathbb{N}\), the energy evolves via _E_<sub>_k_+1</sub>=_E<sub>k</sub>+w(v<sub>k</sub>,v_<sub>_k_+1</sub>). A strategy for Player 1 is winning from _v_<sub>0</sub> with initial energy _E_<sub>0</sub> if it ensures that \(E_k\ge 0\) for all \(k\ge 0\), regardless of the choices of Player 2. The objective is to find the minimum initial energy \(E_0^*\in\mathbb{N}\) for which Player 1 has a winning strategy from _v_<sub>0</sub>. The optimal value is \(OPT(G)=E_0^*\). If no finite initial energy allows Player 1 to win, we set \(OPT(G)=\infty\).

Two Energy Game instances _G_ and \(G'\) are isomorphic if their underlying graphs are isomorphic. Note that an isomorphism has to preserve vertex attributes and edge attributes. Therefore, Energy Game is closed under isomorphism.

