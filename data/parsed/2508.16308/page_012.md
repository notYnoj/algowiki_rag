Now, we have all the tools to prove Theorem 2.

_Proof of Theorem 2._ We prove this by contradiction. Let us assume that there exists an integer \(k_0\ge 3\) and a LOCAL algorithm A which _k_<sub>0</sub>-partially colors every _n_-vertex _k_<sub>0</sub>-partially _k_<sub>0</sub>-colorable graph in _o(n/k_<sub>0</sub><sup>3</sup>) rounds. Then, there exists an integer \(\ell_0>0\) such that for each even \(\ell\ge\ell_0\), on every \(O(\ell k_0^3)\)-vertex _k_<sub>0</sub>-partially _k_<sub>0</sub>-colorable graph, the algorithm A terminates in at most \(3\big(\ell/2-1\big)\) rounds.

Now let us create indistinguishability graphs \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)for _k_<sub>0</sub> and some even arbitrary \(\ell\ge\ell_0\) as described in the section. For both \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\), the ids of the vertices are set as follows.

1. For \(a\in[k_0],i\in[\ell]\), id((_a,i_)):=(_a,i_).<tbc>

2. For \((a,b,j)\in[k_0]^3\) and \(i\in[\ell-1]\) such that \(b\neq\tau_i(a)\),<br>
id(((_a,i),(b,i_+1)_,j_)):=((_a,i),(b,i_+1)_,j_).

The ids of the vertices of \(G_1^{\{\ell,k\}}\)(and \(G_2^{\{\ell,k\}}\)) are unique and can be encoded in _O_(log_n_) bits and therefore can be mapped uniquely to the set {1,2_,...,n<sup>d</sup>_} for some constant _d_. Hence the identifiers are valid.

Let the colorings output by the algorithm A for \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)be \(\chi_1\) and \(\chi_2\), respectively. For each \(i\in[k]\), the vertex with id (_i,_1) has the same \(\big(3\ell/2-1\big)\)-radius view in \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\)(thanks to Fact 2 and the assignment of ids). The same is also true to the vertex with id \((i,\ell)\). Therefore, algorithm A at vertex with id (_i,_1) cannot distinguish between \(G_1^{\{\ell,k\}}\)or \(G_2^{\{\ell,k\}}\)after \(\big(3\ell/2-1\big)\) rounds and outputs the same color for (_i,_1) (and \((i,\ell)\)) in \(G_1^{\{\ell,k\}}\)and \(G_2^{\{\ell,k\}}\). More specifically, the following holds for vertices with ids (_i,_1) and \((i,\ell)\) for each \(i\in[k_0]\):

\(\chi_1((i,1))=\chi_2((i,1)),\)<br>
\(\chi_1((i,\ell))=\chi_2((i,\ell)).\)

Item 1 of Fact 1 implies that \(\chi_2((i,1))=\chi_2((i,\ell))\) for each \(i\in[k_0]\) in \(G_2^{\{\ell,k\}}\). However, this leads to contradiction, as due to item 2 of Fact 1, there must exist \(j\in[k_0]\) such that \(\chi_2((j,1)\neq\chi_2((j,\ell))\).

## 8 Conclusions

We systematically investigated the complexity of _k_-partial _k_-coloring in both classical and distributed settings, revealing fundamental limitations of this generalized coloring paradigm. Our results demonstrate a sharp threshold between the tractable (_k_+1)-color case and the computationally hard _k_-color variant. We proved that deciding _k_-partial _k_-colorability is NP-complete for all constants \(k\ge 3\), even for graphs where partial coloring reduces to proper coloring (as characterized by \(\Delta_E\)). This contrasts with the linear-time greedy algorithm for (_k_+1)-colorings.

In the LOCAL model, we established an \(\Omega(n)\)-round lower bound for computing _k_-partial _k_- colorings, showing an exponential separation from the \(O(log^2k\cdot logn)\)-round algorithms for (_k_+1)- colorings, using graph constructions based on _paths of cliques_ and _indistinguishability arguments_. To this end, we extend the connection of this weaker version of coloring to proper coloring for proving locality as well as classical lower bounds.

