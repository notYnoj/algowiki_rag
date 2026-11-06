_Proof._ A folklore result states that _S_ is an independent set of a graph _G_ if and only if \(\bar{S}:=V(G)\backslash S\) is a vertex cover of _G_. Thus, a function _R_ that maps (_G,k_) to (_G,|V(G_)|-_k_) is an isomorphism- preserving reduction from IS to VC.

**Lemma B.28.** MaxCut \(\le_p^\cong\) Max 2-SAT

_Proof._ Let (_G_=(_V,E),k_) be an instance of MaxCut. Let _R_ be the function that maps (_G,k_) to \(\Phi\) where \(\{x_v|v\in V\}\) are the variables of \((\Phi,|E|+k)\) and \(\bigcup_{\{v,u\}\in E}\{(x_v\vee x_u),(\neg x_v\vee\neg x_u)\}\).

If there is a set \(S\subseteq V\) that cuts at least _k_ edges, then the assignment

\(x_v=\left\{\begin{array}{ c c }
1 & ,\text{if}v\in S \\
0 & ,\text{if}v\notin S
\end{array}\right.\)

satisfies both clauses for a cut edge and one clause for every other edge. This implies that |_E_|+_k_ clauses are satisfied for this assignment.

If there is an assignment _x<sub>v</sub>_ that satisfies |_E_|+_k_ clauses, then the set \(S=\{v\in V|x_v=1\}\) cuts at least _k_ edges because there are _k_ edges for which both constraints are satisfied. These edges are cut by _S_.

Let (_G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>)_,k_<sub>1</sub>) and (_G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>)_,k_<sub>2</sub>) be isomorphic instances of MaxCut with isomorphism \(\phi:V\rightarrow V\) . Then, the formulas in _R(G_<sub>1</sub>,|_E_<sub>1</sub>|+_k_<sub>1</sub>) and _R(G_<sub>2</sub>,|_E_<sub>2</sub>|+_k_<sub>2</sub>) are isomorphic to each other due to renaming the variables using \(\phi\). Also it holds that

\(|E_1|+k_1=|E_1|+k_2=|E_2|+k_2.\)

**Lemma B.29.** Undirected Hamiltonian Cycle \(\le_p^\cong\) Metric TSP

_Proof._ Let _G_=(_V,E_) be an instance of Undirected Hamiltonian Cycle. Let _R_ be the function that maps _G_ to \((G'=(V,\genfrac(){pt}{2}{V}{2},w),|V|)\) such that

\(w(e)=\left\{\begin{array}{ c c }
1 & ,\text{if}e\in E \\
2 & ,\text{if}e\notin E
\end{array}\right.\)

for all \(e\in\genfrac(){pt}{2}{V}{2}\). Note that this weight functions satisfies the triangle inequality because it has only values from {1,2}.

If _G_ has a Hamiltonian Cycle, then it has \(G'\) has a Hamiltonian Cycle of cost at most |_V_|.

If _G_ has no Hamiltonian Cycle, then every Hamiltonian Cycle in \(G'\) uses an edge \(e\notin E\) and thus is of cost _w(e_)=2. Hence, every Hamiltonian Cycle in \(G'\) has cost at least |_V_|+1.

Let _G_<sub>1</sub> and _G_<sub>2</sub> be isomorphic instances of Undirected Hamiltonian Cycle with isomorphism \(\phi:V\rightarrow V\) . Then, \(\phi\) is also an isomorphism for _R(G_<sub>1</sub>) and _R(G_<sub>2</sub>).

This Lemma uses the reduction from \[GK99\].

**Lemma B.30.** Set Cover \(\le_p^\cong k\)-Median.

_Proof._ Let (_S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) be an instance of Set Cover. Let _R_ be the function that maps (_S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) to (\[_m_\],\[_n_\]_,d,k,n_) and<tbc>

\(d(i,j)=\left\{\begin{array}{ c c }
1 & ,\text{if}j\in S_i \\
3 & ,\text{otherwise}
\end{array}\right.\)

