**Theorem 7.11.** _Let_

\(G=(V,E,c:E\rightarrow\mathbb{R}_{\ge 0},\ell:E\rightarrow\mathbb{R}_{\ge 0},s,t,B)\text{\textit{and}}\)<br>
\(G'=(V',E',c':E'\rightarrow\mathbb{R}_{\ge 0},\ell':E'\rightarrow\mathbb{R}_{\ge 0},s',t',B)\)

_be two instances of the_ Constrained Shortest Path (CSP_) problem. If_ \(G\equiv_{1\text{-WL}}G'\)_, then they have the same optimal value for_ CSP.

Before turning to the proof, let us recall how instances \(G=(V,E,c:E\rightarrow\mathbb{R}_{\ge 0},\ell:E\rightarrow\mathbb{R}_{\ge 0},s,t,B)\) of CSP are interpreted as attributed graphs. The attribute of each edge \(e\in E\) with length \(\ell(e)\) and cost _c(e_) is the vector \(\alpha_E(e)=(\ell(e),c(e))\). The vertex attributes designate the terminals: \(\alpha_V(v)=\mathsf{s}\) if _v_ is the source, \(\alpha_V(v)=\mathsf{t}\) if _v_ is the sink, and \(\alpha_V(v)=\perp\) otherwise.

_Proof._ Let _OPT(G_) and \(OPT(G')\) denote the optimal values. By symmetry, it suffices to show \(OPT(G')\le OPT(G)\). If no feasible path exists in _G_, then \(OPT(G)=\infty\) and the inequality trivially holds.

Assume a feasible optimal path exists, and let _P_=(_v_<sub>0</sub>_,e_<sub>1</sub>_,v_<sub>1</sub>_,...,e<sub>r</sub>,v<sub>r</sub>_) be an optimal directed path in _G_ from _v_<sub>0</sub>=_s_ to _v<sub>r</sub>=t_ with total cost \(C\ge 0\) and length \(L\le B\). Recall that each edge _e<sub>j</sub>_ carries the attribute \(\alpha_E(e_j)=(c(e_j),\ell(e_j))\).

Because \(G\equiv_{1\text{-WL}}G'\) and \(\alpha_V\) isolates the distinguished vertices into singleton color classes, we obtain that \(\chi_\infty^G(s)\) and \(\chi_\infty^{G^\prime}(s')\). By Lemma 7.8 (Walk Lifting), there exists a directed walk \(W'=(v'_0,e'_1,v'_1,\dots,e'_r,v'_r)\) in \(G'\) starting at \(s'\) with the exact same sequence of edge attributes \((c,\ell)\) and stable vertex colors. In particular, \(\chi_\infty^G(t)=\chi_\infty^G(v_r)=\chi_\infty^{G^\prime}(v'_r)\). Since _t_ and \(t'\) are distinguished via \(\alpha_V\) and \(\alpha'_V\), we obtain that \(v'_r=t'\) by Lemma 7.6.

The total cost and length of walk \(W'\) are identical to _P_, meaning \(W'\) is a feasible solution in \(G'\) with cost _C_. If \(W'\) contains cycles, they can be removed to form a simple directed path \(P'\). Given that the edge lengths and costs are non-negative, removing cycles cannot increase the total cost or violate the length constraint. Thus, \(OPT(G')\le C=OPT(G)\).

**Theorem 7.12.** _Let G_=(_V,E,V_<sub>1</sub>_,V_<sub>2</sub>_,w,v_<sub>0</sub>) _and_ \(G'=(V',E',V'_1,V'_2,w',v'_0)\) _be two_ Energy Game _instances. If_ \(G\equiv_{1\text{-WL}}G'\)_, then Player 1 has a winning strategy in G from v_<sub>0</sub> _with initial energy E_<sub>0</sub> _if and only if Player 1 has a winning strategy in_ \(G'\) _from_ \(v'_0\) _with initial energy E_<sub>0</sub>.

Again, let us first recall how instances _G_=(_V,E,V_<sub>1</sub>_,V_<sub>2</sub>_,w,v_<sub>0</sub>) are interpreted as attributed graphs. The attribute of each edge \(e\in E\) is \(\alpha_E(e)=w(e)\). The vertex attributes indicate the partition according to players and the initial vertex: \(\alpha_V(v)=(i,\mathsf{s})\) if _v_ is the initial vertex, and \(\alpha_V(v)=(i,\perp)\) otherwise, where in both cases \(i\in\{1,2\}\) is the unique index such that \(v\in V_i\).

_Proof._ By symmetry, it suffices to show that if Player 1 has a winning strategy \(\sigma\) in _G_ starting at _v_<sub>0</sub> with energy _E_<sub>0</sub>, they also have a winning strategy \(\sigma'\) in \(G'\) starting at \(v'_0\) with energy _E_<sub>0</sub>.

We define \(\sigma'\) dynamically by maintaining a simulated "shadow play" in _G_. Let the current finite prefix of the play in \(G'\) be \(\pi'=(v'_0,\dots,v'_k)\) and the maintained shadow play in _G_ be \(\pi=(v_0,\dots,v_k)\). We enforce the invariant that \(\chi_\infty^G(v_i)=\chi_\infty^{G^\prime}(v'_i)\) and \(w(v_{i-1},v_i)=w'(v'_{i-1},v'_i)\) for all \(i\le k\).

1. **Base Case:** For _k_=0, the play begins at \(v'_0\). We set the shadow play to _v_<sub>0</sub>. Since \(G\equiv_{1\text{-WL}}G'\), we conclude that \(\chi_\infty(v'_0)=\chi_\infty(v_0)\) using Lemma 7.6 (Refinement).<tbc>

2. **Player 1’s Turn:** Suppose the current play is at \(v'_k\in V'_1\). Because colors strictly preserve initial partitions (by Lemma 7.6, Refinement), the shadow vertex _v<sub>k</sub>_ satisfies \(v_k\in V_1\). In _G_, strategy \(\sigma\) dictates an outgoing edge (_v<sub>k</sub>,v_<sub>_k_+1</sub>) with weight _W_. By Lemma 7.6 (Neighborhood Preservation), since \(\chi_\infty^{G^\prime}(v'_k)=\chi_\infty^G(v_k)\), there exists an outgoing edge in \(G'\) to some vertex \(v'_{k+1}\) such that \(\chi_\infty^{G^\prime}(v'_{k+1})=\chi_\infty^G(v_{k+1})\) and \(w'(v'_k,v'_{k+1})=W\). Player 1’s strategy \(\sigma'\) chooses this edge, and we append _v_<sub>_k_+1</sub> to the shadow play.<tbc>

