for all \(i\in[m]\) and \(j\in[n]\). In \[GK99\], they show that _R(S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) is a YES-Instance of _k_-Median if and only if (_S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) is a YES-Instance of Set Cover.

It remains to show that the reduction _R_ is isomorphism-preserving. To this end, we start by considering two isomorphic instances (_S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_) and \((S'_1,\dots,S'_{m^\prime},n',k')\). By definition, there are two bijective functions \(f:[n]\rightarrow[n']\) and \(g:[m]\rightarrow[m']\) with \(S'_{g(i)}=f(S_i)\). Then _R(S_<sub>1</sub>_,...,S<sub>m</sub>,n,k_)=(\[_m_\],\[_n_\]_,d,k,n_) and \(R(S'_1,\dots,S'_{m^\prime},n',k')=([m'],[n'],d',k',n')\) are isomorphic due to the same bijective functions _f_ and _g_ because for all \(i\in[m]\) and \(j\in[n]\) it holds that,

\(d(i,j)=1\Leftrightarrow j\in S_i\Leftrightarrow f(j)\in S'_{g(i)}\Leftrightarrow d(f(j),g(i))=1.\)

**Lemma B.31.** \(\mathsf{VC}\le_p^\cong\mathsf{Gap}\)-k-Center<sub>1,2</sub>

_Proof._ Let ((_V,E),k_) be an instance of VC. Let _R_ be the function that maps ((_V,E),k_) to ((_V,E,w),k_) such that _w(e_)=1 for all \(e\in E\).

If there is a vertex cover _X_ of size _k_ in _V_ , then it holds that<tbc>

\(max_{v\in V}d_{(V,E),w}(v,X)\le 1.\)

<tbc>If (_V,E_) does not contain a vertex cover of size _k_, then for all subsets \(X\subseteq V\) of size _k_ it holds that

\(max_{v\in V}d_{(V,E),w}(v,X)\ge 2.\)

This is an isomorphism-preserving reduction because the graph is not changed when _R_ is applied.

**Lemma B.32.** Undirected Hamiltonian Cycle \(\le_p^\cong\mathsf{Gap}\)-TSP<sub>1_,c_</sub> _For all c\>_1.

_Proof._ Let _G_=(_V,E_) be an instance of Undirected Hamiltonian Cycle. Let _R_ be the function that maps _G_ to \(G'=(V,\genfrac(){pt}{2}{V}{2},w)\) such that

\(w(e)=\left\{\begin{array}{ c c }
1/|V| & ,\text{if}e\in E \\
C & ,\text{if}e\notin E
\end{array}\right.\)

for all \(e\in\genfrac(){pt}{2}{V}{2}\).

If _G_ has a Hamiltonian Cycle, then it has \(G'\) has a Hamiltonian Cycle of cost at most 1.

If _G_ has no Hamiltonian Cycle, then every Hamiltonian Cycle in \(G'\) uses an edge \(e\notin E\) and thus is of cost _w(e_)=_C_. Hence, every Hamiltonian Cycle in \(G'\) has cost at least _C_.

Let _G_<sub>1</sub> and _G_<sub>2</sub> be isomorphic instances of Undirected Hamiltonian Cycle with isomorphism \(\phi:V\rightarrow V\) . Then, \(\phi\) is also an isomorphism for _R(G_<sub>1</sub>) and _R(G_<sub>2</sub>).

