Next we choose maps \(f,g:[H]^s\longrightarrow[H]^s\) as in Lemma 3.1 and, for every stage index \(j\in[H]\), fix a palette family<tbc>

\(\mathcal{P}_j\subseteq\genfrac(){pt}{2}{[M_j]}{t}\)

<tbc>as given by Lemma 3.2. We write _B<sub>j</sub>_=|P_<sub>j</sub>_| and set

\(n_0=1,n_j=\prod_{h=1}^JB_h(1\le j\le H).\)

For each \(0\le j\le H\), let us fix a set _V<sub>j</sub>_ of size _n<sub>j</sub>_ which will serve as the vertex-set of the edge-colored complete graph we construct at stage _j_ of the process. We also fix, for every \(1\le j\le H\), a partition \(V_j=\sqcup_{P\in\mathcal{P}_j}V_P\), where each of the sets _V<sub>P</sub>_ has size exactly _n_<sub>_j_-1</sub> and is identified with the vertex-set of the complete graph _K_<sub>_V<sub>j</sub>_-1</sub>. We call _V<sub>P</sub>_ the _block_ associated with the palette \(P\in\mathcal{P}_j\).

For a palette \(P\in\mathcal{P}_j\) and some \(c\in[M_j]\), let us call _c active_ on _V<sub>P</sub>_ if \(c\notin P\), and _missing_ on _V<sub>P</sub>_ if \(c\in P\).

In the following, for every \(0\le j\le H\), we will construct an edge-coloring

\(\kappa_j:E(K_{V_j})\longrightarrow[M_j]\times[q],\)

and, for every \(c\in[M_j]\), a map \(L_{j,c}:V_j\rightarrow[j+1]\) (this corresponds to one of the "vertex- colorings" mentioned in the informal proof overview). These objects will satisfy the following invariants.

**Invariants.**

(i) For every \(0\le j\le H\) and distinct \(u,v\in V_j\) with \(\kappa_j(uv)=(c,b)\), we have<tbc>

<tbc>\(L_{j,c}(u)\neq L_{j,c}(v)\text{and}b=\tau\big(L_{j,c}(u)L_{j,c}(v)\big).\)<tbc>

<tbc>Hence, the second coordinate of the colorings \(\kappa_j\) corresponds to the edge-coloring \(\tau\) of the smaller complete graph _K_<sub>_H_+1</sub> lifted to _V<sub>j</sub>_ via the vertex-color maps _L<sub>j,c</sub>_.<tbc>

(ii) For every \(1\le j\le H\) and for every \(P\in\mathcal{P}_j\) there is a bijection<tbc>

<tbc>\(\phi_P:[M_{j-1}]\longrightarrow[M_j]\backslash P\)<tbc>

<tbc>such that, for every edge \(uu'\) inside _V<sub>P</sub>_, we have<tbc>

<tbc>\(\kappa_{j-1}(uu')=(d,b)\Longleftrightarrow\kappa_j(uu')=(\phi_P(d),b).\)<tbc>

<tbc>In other words, the first coordinate of the coloring \(\kappa_j\) restricted to the internal edges of any block _V<sub>P</sub>_ corresponds, after suitable color-permutation, to the first coordinate of the coloring \(\kappa_{j-1}\), while the second coordinate is inherited from \(\kappa_{j-1}\) directly. Only the colors outside _P_ are used by the first coordinate of \(\kappa_j\) on edges inside _V<sub>P</sub>_.<br>
Furthermore, for every \(u\in V_P\), we have<tbc>

<tbc>\(L_{j,\phi_P(d)}(u)=L_{j-1,d}(u)(d\in[M_{j-1}]),L_{j,c}(u)=j+1(c\in P).\)<tbc>

<tbc>In other words, for every block _V<sub>P</sub>_ and every color _c_, if _c_ is active on _V<sub>P</sub>_ then the vertex-coloring _L<sub>j,c</sub>_ on the block _V<sub>P</sub>_ is inherited from the previous stage of the process. If _c_ is missing on _V<sub>P</sub>_ then _L<sub>j,c</sub>_ is constantly equal to _j_+1 on the block _V<sub>P</sub>_.<tbc>

