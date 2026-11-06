Therefore, the total communication is bounded by \(\widetilde{O}\left(\frac{n}{\varepsilon^2}+\varepsilon n^{3/2}\nu(G)^{1/2}\right)\). By setting \(\varepsilon=(n\cdot\nu(\mathcal{G}))^{-1/6}\), the number of cut queries become \(\widetilde{O}\left(n^{4/3}\nu(\mathcal{G})^{1/3}\right)\) as wished.

As a final piece, observe that we cannot set \(\varepsilon=(n\cdot\nu(\mathcal{G}))^{-1/6}\) exactly, as we do not know the true value of \(\nu(\mathcal{G})\) at the onset of our algorithm. To fix this, we can w.h.p. compute a constant- approximation of \(\nu(\mathcal{G})\) within \(\widetilde{O}(n)\) cut queries<sup>6</sup>, and use it as a proxy to \(\nu(\mathcal{G})\). This does not affect the integrity of our proofs, nor the asymptotic number of queries.

## 4.2 Implementation in Two-Player Communication

We describe the implementation of Algorithm 1 in the two-player communication model. As a reminder, in this setting, Alice holds a subgraph _G<sub>A</sub>_=(_V,E<sub>A</sub>_) and Bob holds _G<sub>B</sub>_=(_V,E<sub>B</sub>_), where the true input graph is the union \(G=G_A\cup G_B\). The complexity of the algorithm is measured by the total number of bits communicated between the two players throughout the execution.

We begin by studying a useful combinatorial structure: a _forest packing_. Let _G_ be an undirected, unweighted graph. For any integer \(k\ge 1\), we define a _k-forest packing_ of _G_ to be \(P=F_1\cup\dots\cup F_k\) where, for each \(i\in[k]\), the subgraph _F<sub>i</sub>_ is a spanning forest of the graph \(G\backslash(F_1\cup\dots\cup F_{i-1})\). A crucial insight is that any _k_-forest packing yields a relatively sparse subgraph of _G_ that simultaneously preserves all small cuts and ensures that large cuts remain large. These properties are formally captured in the following lemma.

**Lemma 4.2.** _Let P be k-forest packing of a graph G. Then, the following statements are true._

1. _For a cut_ (_S,T), if_ \(|E_G(S,T)|\le k\)_, then E<sub>P</sub>(S,T_)=_E<sub>G</sub>(S,T)._<tbc>

_2._ _For a cut_ (_S,T), if_ \(|E_G(S,T)|\ge k+1\)_, then_ \(|E_P(S,T)|\ge k\).<tbc>

_3._ _P has average degree O(k)._

_Proof._ We first prove (1). Let \(P=F_1\cup\dots\cup F_k\) be a forest packing of _G_. Let (_S,T_) be a cut such that \(|E_G(S,T)|\le k\). Consider any \(i\le k\). If there is an edge among _E<sub>G</sub>(S,T_) remained in \(G\backslash(F_1\cup\dots\cup F_{i-1})\), the spanning forest _F<sub>i</sub>_ must include at least one of those remaining edges. In other words, upon packing \(k\ge|E_G(S,T)|\) spanning forest into _P_, all edges of _E<sub>G</sub>(S,T_) must be included. This means _E<sub>P</sub>(S,T_)=_E<sub>G</sub>(S,T_).

For (2), we have two cases. First, if \(E_{F_i}(S,T)=\emptyset\) for some \(i\in[k]\), it means all edges in _E<sub>G</sub>(S,T_) must have already been included in \(F_1\cup\dots\cup F_{i-1}\). This then implies \(|E_P(S,T)|=|E_G(S,T)|\ge k+1\). The other case is \(|E_{F_i}(S,T)|\ge 1\) for each \(i\in[k]\). In this case, we can write \(|E_P(S,T)|=\sum_{i\in[k]}|E_{F_i}(S,T)|\ge k\) as wished.

Finally, we prove (3). Notice that each _F<sub>i</sub>_ has at most _n_-1 edges. Thus, the number of edges in _P_ is at most _k(n_-1), implying that the average degree is at most \(\frac{2k(n-1)}{n}=O(k)\).

As an implication, we obtain the following lemma.

**Lemma 4.3.** _Let_ \(\mathcal{G}=(G_A\cup G_B,F)\) _be a mixed graph in two-player communication setting, and let k be a parameter such that_ \(k\ge\nu(\mathcal{G})+1\)_. Let P<sub>A</sub> and P<sub>B</sub> be a k-forest packing of G<sub>A</sub> and G<sub>B</sub> respectively, and denote a mixed graph_ \(\mathcal{P}=(P_A\cup P_B,F)\)_. Then, we have:_

1. _Both P<sub>A</sub> and P<sub>B</sub> have average degree O(k)._<tbc>

<sup>6</sup>To do this, we first compute an _G_<sup>∗</sup> to be a \(\frac{1}{100}\)-cut sparsifier of _G_ via Corollary 2.8, and use \(\nu(G^*\cup F)\) as a proxy to \(\nu(\mathcal{G})\).

