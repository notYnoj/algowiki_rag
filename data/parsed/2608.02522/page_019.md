Similarly, for every \(v\in V(G_1)=V(G_2)\) we have

\(\sum_{S\in\mathcal{I}(G_1\cup G_2):v\in S}x'_S=\sum_{I\in\mathcal{I}(G_1),J\in\mathcal{I}(G_2):v\in I\cap J}x_I^{(1)}x_J^{(2)}=\sum_{I\in\mathcal{I}(G_1):v\in I}x_I^{(1)}\cdot\sum_{J\in\mathcal{I}(G_2):v\in J}x_J^{(2)}\ge 1\cdot 1=1.\)

Hence, \((x'_S)_{S\in\mathcal{I}(G_1\cup G_2)}\) is feasible for the linear program (P) for \(G_1\cup G_2\) with objective value \(\chi_f(G_1)\chi_f(G_2)\). Since \(\chi_f(G_1\cup G_2)\) is by definition the minimum of that program, it follows that \(\chi_f(G_1\cup G_2)\le\chi_f(G_1)\chi_f(G_2)\), as desired. This concludes the proof of the lemma.

Having established that the first condition of \(\chi\)-amenability is satisfied by every \(f\in\{\chi,\chi_f,\rho\}\), it remains to verify the second condition in the definition (for some suitable choice of the absolute constant \(C\ge 1\)).

For \(\chi\), the condition is trivially satisfied by taking _C_:=1. For the fractional chromatic number and the Hall ratio, the statement requires a proof, and this is supplied by our next lemma. Here, _e_ denotes Euler’s number.

**Lemma 4.2.** _Let_ \(C:=\frac{2}{1-e^{-1}}\)_. Every graph G has a subgraph_ \(G'\) _such that_<tbc>

\(\chi_f(G')\ge\chi_f(G)/C\text{\textit{and}}\chi(G')\le C\chi_f(G').\)

<tbc>_Similarly, every graph G has a subgraph_ \(G'\) _such that_<tbc>

\(\rho(G')\ge\rho(G)/C\text{\textit{and}}\chi(G')\le C\rho(G').\)

<tbc>_Proof._ We start by giving the proof for the fractional chromatic number. Let _G_ be any given graph, and set \(z:=\chi_f(G)\ge 1\). By our definition of the fractional chromatic number and strong linear programming duality, there exists a pair of optimal primal and dual solutions to the linear programs (P) and (D) for the graph _G_ with the same objective value. Let us denote such a pair of optimal solutions by \((x_I)_{I\in\mathcal{I}(G)}\) and \((y_v)_{v\in V(G)}\), such that

\(\sum_{I\in\mathcal{I}(G)}x_I=\sum_{v\in V(G)}y_v=\chi_f(G).\)

Let \(p_I:=\frac{x_I}{\chi_f(G)}\ge 0\) for every \(I\in\mathcal{I}(G)\). Then we have \(\sum_{I\in\mathcal{I}(G)}p_I=1\), and so we can define a probability distribution D on the independent sets of _G_ by including any independent set _I_ with probability exactly _p<sub>I</sub>_. Since \(\sum_{I\in\mathcal{I}(G):v\in I}p_I=\frac{\sum_{I\in\mathcal{I}(G):v\in I}x_I}{\chi_f(G)}\ge\frac{1}{\chi_f(G)}=\frac{1}{z}\), we find that a random independent set _I_ drawn according to the distribution D contains any given vertex with probability at least \(\frac{1}{z}\).

Now let \(k:=\lceil z\rceil\) and let us consider drawing _k_ independent samples _I_<sub>1</sub>_,...,I<sub>k</sub>_ from the distribution D of independent sets, and defining a subgraph \(G'\) of _G_ as \(G':=G[I_1\cup\cdots\cup I_k]\). Evidently, regardless of the outcome of the samples, we have \(\chi(G')\le k\). Furthermore, by the above, any given vertex of _G_ is contained in \(V(G')\) with probability at least \(1-(1-1/z)^k\ge 1-exp(-k/z)\ge 1-e^{-1}\). Hence, by linearity of expectation, the expectation of \(\sum_{v\in V(G^\prime)}y_v\) is at least \(\sum_{v\in V(G)}y_v\cdot(1-e^{-1})=z(1-e^{-1})\). This shows that there exists some outcome of \(G'\) for which \(\sum_{v\in V(G^\prime)}y_v\ge z(1-e^{-1})\) and \(\chi(G')\le k\). In the remainder, we fix such an induced subgraph \(G'\) of _G_ with these properties.

