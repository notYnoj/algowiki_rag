contradiction, that there exists a source-sink pair (_s_<sub>1</sub>_,t_<sub>1</sub>) and a path \(P\in\mathcal{P}_1\) connecting them in _G_\\_g(F_) such that \(E(P)\cap g(F)=\emptyset\). Since the LP solution _x_ satisfies \(\sum_{e\in E(P)}x_e\ge 1\), the corresponding path \(P'\) in _S(G,M_) (formed by replacing each \(e\in E(P)\) with the path _P<sub>e</sub>_) has length at least 2_w_. The assumption \(E(P)\cap g(F)=\emptyset\) implies that \(E(P')\cap F=\emptyset\), and thus _s_<sub>1</sub> and _t_<sub>1</sub> remain connected in _S(G,M_)\\_F_. This contradicts the assumption that \(F\in\mathcal{F}_{2w}(S(G,M))\), as no connected component in the decomposition can have diameter \(\ge 2w\).<br>
Now, let \(B=\{g(F)|F\in\mathcal{F}_{2w}(S(G,M))\}\), and for each \(b\in B\), define<tbc>

\(y'_b=\sum_{F\in\mathcal{F}_{2w}(S(G,M))g(F)=b}y_F.\)

<tbc>Then \(y'=\{y'_b\}_{b\in B}\) is a probability distribution over multicuts in _G_. We now analyze the expected cost of a multicut drawn from this distribution. For any edge \(e\in E(G)\), if _x<sub>e</sub>_=0, then _e_ was contracted and does not appear in _S(G,M_), so:<tbc>

\(\sum_{a\unknown e,b\in B}y'_b=0.\)

<tbc>If \(e\in A\), then:<tbc>

\(\sum_{b\unknown e,b\in B}y'_b=\sum_{e^\prime\in P_e}\sum_{F\unknown e^\prime F\in\mathcal{F}_{2w}(S(G,M))}y_F\le|E(P_e)|\cdot\frac{\alpha}{2w}=\alpha x_e.\)

<tbc>Therefore, in expectation, each edge _e_ appears in a randomly sampled multicut with probability at most \(\alpha x_e\). This implies there exists a multicut \(b\in B\) such that

\(\sum_{e\in b}c_e\le\alpha\sum_{e\in E(G)}c_ex_e=\alpha\cdot OPT_{LP}(M),\)

which completes the proof. \(\blacktriangle\)

The transition to the SDD framework eliminates the dependence on the specific placement of source-sink pairs and edge costs, which could otherwise be arbitrary, and instead provides a uniform way of analyzing the integrality gap. Theorem 2 serves as the bridge between SDDs and the integrality gap. We only make use of the forward direction of Theorem 2 in the following.

## 4.1 Small Diameter Decomposition for Trees

As mentioned earlier, \(\alpha_{\mathcal{M}(\mathrm{tree})}=2\). By Theorem 2, this implies that for any tree _T_ and any integer \(w\in\mathbb{N}\), there exists

\(SDD\big(T,2w,\frac{2}{2w}=\frac{1}{w}\big).\)

In other words, the family of trees is \(SDD(2w,\frac{1}{w})\)-acceptable for any \(w\in\mathbb{N}\). Moreover, without directly appealing to Theorem 2, we can explicitly construct such an \(SDD(T,2w,\frac{1}{w})\). This explicit construction will serve as a foundation for developing intuition regarding structured small-diameter decompositions in the next Section 5.

**Theorem 3.** _Let T be a tree. Then for every integer_ \(w\in\mathbb{N}\)_, there exists_<tbc>

\(SDD\big(T,2w,\frac{1}{w}\big).\)

