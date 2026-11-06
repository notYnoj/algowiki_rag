There are only finitely many such matrices. Induction on _i_ and continuity of matrix inversion therefore give an open neighborhood of (_a_<sub>1</sub>_,...,a<sub>m</sub>_) in which every displayed inverse exists and every _z<sub>i</sub>_ depends continuously on (_f_<sub>1</sub>_,...,f<sub>m</sub>_). Shrinking this neighborhood if necessary keeps every \(d\times d\) determinant formed from distinct vectors _z<sub>i</sub>_ nonzero, since there are finitely many and all are nonzero at (_a_<sub>1</sub>_,...,a<sub>m</sub>_). The resulting vectors are in general position. Moreover, _z<sub>i</sub>_ is orthogonal to each column of _B<sub>i</sub>_, so every required orthogonality relation holds exactly.

Choose all coordinates of _f_<sub>1</sub>_,...,f<sub>m</sub>_ rational within this open neighborhood. The displayed formula then produces rational coordinates for every _z<sub>i</sub>_, because it uses only rational matrix operations and inverses of invertible rational matrices. Multiply all vectors by a common positive integer that clears their denominators. This preserves orthogonality and linear independence and gives the required integral vectors _c<sub>e</sub>_.

We also use an elementary exact restriction to absorb the interpolation overhead. It extends the one-copy extraction for paths discussed in \[VC17, Section 3\] to any connected graph by selecting a spanning tree.

**Lemma B.3** (a diagonal restriction from a spanning tree)**.** _For every finite connected simple graph G on_ \(k\ge 2\) _vertices and every integer_ \(q\ge 2\)_, we have_ \(\mathsf{I}_k(q)\unknown\mathsf{GT}_q(G)\).

_Proof._ Choose a spanning tree _F_ of _G_. Every vertex is incident to at least one edge of _F_. At vertex _v_, consider the basis vector indexed by the labels on the edges incident to _v_. Send this basis vector to \(e_a^{(q)}\) if all incident edges outside _F_ have label 0 and all incident edges in _F_ have the same label \(a\in[q]_0\). Send it to zero otherwise. This specifies a linear map on every leg.

A surviving global edge labeling has label 0 on every edge outside _F_. If _a<sub>v</sub>_ is the common tree- edge label at vertex _v_, then a tree edge (_u,v_) has both labels _a<sub>u</sub>_ and _a<sub>v</sub>_, so _a<sub>u</sub>=a<sub>v</sub>_. Connectivity of _F_ forces _a<sub>v</sub>=a_ for all vertices and a single \(a\in[q]_0\). Conversely, each such _a_ gives exactly one surviving labeling. The image of the graph tensor is therefore \(\sum_{a=0}^{q-1}e_a^{(q)}\otimes_C\cdots\otimes_Ce_a^{(q)}=\mathsf{I}_k(q)\).

We now combine these two ingredients. The orthogonal representation will select a large set of edge labelings that are distinguishable at every vertex. The spanning-tree restriction will then absorb the interpolation overhead, allowing us to pass from a degeneration to ordinary asymptotic subrank.

**Theorem B.4** (Vrana-Christandl \[VC17\])**.** _For every finite simple undirected graph G with at least two vertices,_<tbc>

\(\mathrm{log}_2\widetilde{\mathsf{Q}}(\mathsf{GT}_2(G))=\mathrm{MinCut}(G).\)

<tbc>_Proof._ Let _V(G_)={1_,...,k_} and put \(\ell=\mathrm{MinCut}(G)\). For each positive integer _N_ and each nonempty proper subset \(S\subset V(G)\), Lemmas A.2 and A.3 give

\(\mathsf{Q}(\mathsf{GT}_2(G)^{\otimes_KN})\le\mathrm{FR}_S(\mathsf{GT}_2(G)^{\otimes_KN})=2^{N|\delta_G(S)|}.\)

Taking _N_-th roots, then the limit as \(N\rightarrow\infty\), and minimizing over _S_ proves \(\widetilde{\mathsf{Q}}(\mathsf{GT}_2(G))\le 2^\ell\).

If _G_ is disconnected, then \(\ell=0\). The tensor is nonzero, so its subrank is at least 1, and the upper bound proves the claim. If _G_ is connected and _k_=2, then _G=K_<sub>2</sub> and GT<sub>2</sub>(_G_)=I<sub>2</sub>(2), whose asymptotic subrank is 2. We may therefore assume that _G_ is connected and \(k\ge 3\).

Put _m_=|_E(G_)| and \(d=m-\ell\). Fix integral vectors \((c_e)_{e\in E(G)}\) as in Lemma B.2, and write _c<sub>e</sub>_=(_c_<sub>_e,_1</sub>_,...,c<sub>e,d</sub>_) for every \(e\in E(G)\). For every vertex _v_, let _E<sub>v</sub>_ be the set of edges incident to<tbc>

