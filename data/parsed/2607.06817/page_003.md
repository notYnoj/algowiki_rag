**Proposition 2.1.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> be graphs and let_ \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) _be permutation groups on their respective vertex sets. Suppose that F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>k</sub> are graphs such that_ \(F_j\cong_{\Gamma_j}H_j\) _for each_ \(j\in\{1,2,\dots,k\}\)_. Then_ \(R(F_1^{\Gamma_1},F_2^{\Gamma_2},\dots,F_k^{\Gamma_k})=R(H_1^{\Gamma_1},H_2^{\Gamma_2},\dots,H_k^{\Gamma_k})\).

_Proof._ Let \(n\in\mathbb{N}\) and consider a _k_-edge-coloring of _K<sub>n</sub>_. For each \(j\in\{1,2,\dots,k\}\), let _G<sub>j</sub>_ denote the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color _j_. Suppose that there exists \(j\in\{1,2,\dots,k\}\) such that _H<sub>j</sub>_ is \(\Gamma_j\)-embeddable in _G<sub>j</sub>_. By symmetry, it suffices to show that _F<sub>j</sub>_ is also \(\Gamma_j\)-embeddable in _G<sub>j</sub>_. By the definition of \(\Gamma_j\)-embeddability, there exists a homomorphism from _H<sub>j</sub>_ to _G<sub>j</sub>_ of the form \(\psi\circ\varphi\), where \(\varphi\in\Gamma_j\) and \(\psi:V(H_j)\rightarrow V(G_j)\) is an increasing injection. Since \(F_j\cong_{\Gamma_j}H_j\), there exists an isomorphism \(\chi\in\Gamma_j\) from _F<sub>j</sub>_ to _H<sub>j</sub>_. Therefore, \(\psi\circ(\varphi\circ\chi)\) is a homomorphism from _F<sub>j</sub>_ to _G<sub>j</sub>_, with \(\varphi\circ\chi\in\Gamma_j\) and \(\psi\) an increasing injection. Hence, _F<sub>j</sub>_ is \(\Gamma_j\)-embeddable in _G<sub>j</sub>_.

Complementing Proposition 2.1, which treats changes of the arguments, we now consider changes in the associated permutation groups. The following observation establishes a monotonicity property with respect to these groups.

**Proposition 2.2.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> be graphs, and let_ \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) _and_ \(\Lambda_1,\Lambda_2,\dots,\Lambda_k\) _be permutation groups on their respective vertex sets. Suppose that_ \(\Gamma_j\le\Lambda_j\) _for each_ \(j\in\{1,2,\dots,k\}\)_. Then_ \(R(H_1^{\Lambda_1},H_2^{\Lambda_2},\dots,H_k^{\Lambda_k})\le R(H_1^{\Gamma_1},H_2^{\Gamma_2},\dots,H_k^{\Gamma_k})\).

**Corollary 2.3.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> be graphs and let_ \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) _be permutation groups on their respective vertex sets. Then_ \(R(H_1,H_2,\dots,H_k)\le R(H_1^{\Gamma_1},H_2^{\Gamma_2},\dots,H_k^{\Gamma_k})\le R_\mathrm{ord}(H_1,H_2,\dots,H_k)\).

Given graphs _G_ and _H_, and a permutation group \(\Gamma\) on _V(H_), it is straightforward to observe that the following two statements are equivalent.

**(1)** _H_ is \(\Gamma\)-embeddable in _G_.

**(2)** There exists a graph \(F\cong_\Gamma H\) with an increasing injective homomorphism from _F_ to _G_.

This yields the following result.

**Proposition 2.4.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> be graphs, and let_ \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) _and_ \(\Lambda_1,\Lambda_2,\dots,\Lambda_k\) _be permutation groups on their respective vertex sets. Suppose that, for each_ \(j\in\{1,2,\dots,k\}\)_, H<sub>j</sub> lies in the same equivalence class under both_ \(\cong_{\Gamma_j}\) _and_ \(\cong_{\Lambda_j}\)_. Then_ \(R(H_1^{\Lambda_1},H_2^{\Lambda_2},\dots,H_k^{\Lambda_k})=R(H_1^{\Gamma_1},H_2^{\Gamma_2},\dots,H_k^{\Gamma_k})\).

A graph _H_ is said to have _reflection symmetry_ if the mapping \(\varphi:V(H)\rightarrow V(H)\) defined by \(\varphi(x)=|H|-1-x\) is an automorphism of _H_. The following corollary of Proposition 2.4 is immediate for graphs with reflection symmetry.

**Corollary 2.5.** _For any graphs H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> with reflection symmetry, we have R_<sub>ref</sub>(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_)=_R_<sub>ord</sub>(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_) _and R_<sub>dih</sub>(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_)=_R_<sub>cyc</sub>(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>)._

The following corollary is another consequence of Proposition 2.4.

**Corollary 2.6.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> be graphs such that each graph is a start-central star or has reflection symmetry. Then_ \(R_\mathrm{dih}(H_1,H_2,\dots,H_k)=R_\mathrm{cyc}(H_1,H_2,\dots,H_k)\).

Now, we formally define each of the graph classes relevant to our work. For any \(n\in\mathbb{N}\), the _monotone path_ \(P_n^\mathrm{mon}\) is the graph of order _n_ in which any two vertices are adjacent if and only if they are consecutive integers, while the _alternating path_ \(P_n^\mathrm{alt}\) is the path graph of order _n_ with the underlying path \((0,n-1,1,n-2,2,n-3,\dots,\lfloor\frac{n}{2}\rfloor)\); see Figure 1. For any \(n\ge 3\), the _monotone cycle_ \(C_n^\mathrm{mon}\) is the graph obtained from \(P_n^\mathrm{mon}\) by adding the edge {0_,n_-1}. Also, for convenience, we let \(C_2^\mathrm{mon}:=K_2\). Furthermore, for any \(n\in\mathbb{N}\), the _start-central star_ \(S_n^\mathrm{sc}\) is the star graph of order _n_ in which vertex 0 is adjacent to all the other vertices. Finally, for any even \(n\ge 2\), the _nested matching_ \(M_n^\mathrm{nest}\) is the 1-regular graph of order _n_ in which each vertex _v_ is adjacent only to _n_-1-_v_; see Figure 2.

The choice of graph classes of interest is motivated by the computational results of \[4\]. The same graph classes are considered, with the exception of reverse alternating paths, which arise by reflecting alternating paths and are therefore equivalent to them in the context of reflective and dihedral Ramsey numbers. Furthermore, by Corollaries 2.5 and 2.6, it suffices to consider reflective Ramsey numbers in which at least one argument lacks reflection symmetry, and dihedral Ramsey numbers in which at least one argument is an alternating path. Otherwise, the problem reduces to computing an ordered or a cyclic Ramsey number, respectively, which was already investigated in \[4\]. Thus, we are interested in computing the reflective Ramsey numbers of alternating paths and start-central stars versus all the considered graph classes, together with the dihedral Ramsey numbers of alternating paths versus all the considered graph classes.

We conclude this section with the following lemma.

