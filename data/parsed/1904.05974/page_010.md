## 3 Our Algorithm

We prove Theorem 2 in this section. Our input instance is \(G=(A\cup B,E)\) and without loss of generality, assume \(|A|\ge|B|\). The first step in our algorithm is an _augmentation_ of the graph _G_ into \(G^*=(A\cup B,E^*)\), with \(E^*\supseteq E\). The new edges in _E_<sup>∗</sup> are obtained by introducing edges between certain pairs of _unstable_ vertices and each new edge has cost 0. Given a popular matching _M_ in _G_, we will use these new edges to obtain an extension _M_<sup>∗</sup> in _G_<sup>∗</sup> such that _M_<sup>∗</sup> is a _dominant_ matching in _G_<sup>∗</sup>, see Lemma 2.

Moreover, _M_<sup>∗</sup> satisfies some stronger condition on witnesses than a dominant matching (as given in Theorem 7). Hence, we will call _M_<sup>∗</sup> _extra-dominant_, see Definition 3. The second step of the algorithm proves that every extra-dominant matching in _G_<sup>∗</sup> projects to a quasi-popular matching in _G_, see Lemma 3.

The first two steps imply that in order to prove Theorem 2, it suffices to efficiently find a min-cost extra-dominant matching (in _G_<sup>∗</sup>). We show how to do this by providing a compact extended formulation of the extra-dominant matching polytope. In fact, we first describe an extension of the dominant matching polytope of _G_<sup>∗</sup>, and then show that one of its faces is an extension of the extra-dominant matching polytope of _G_<sup>∗</sup>.

Lemma 2 and Lemma 3 are our technical lemmas here and their proofs are given in Section 3.3. The proofs of correctness of our extended formulations are given in Section 3.4.

### 3.1 The Popular Subgraph

The augmentation of _G_ into _G_<sup>∗</sup> is based on a certain subgraph of _G_ called its _popular subgraph_. Call an edge _e_ in \(G=(A\cup B,E)\) _popular_ if there is some popular matching in _G_ that contains _e_. Let \(E_0\subseteq E\) be the set of popular edges in _G_. The set _E_<sub>0</sub> can be computed in linear time, see \[11\]. Call \(G_0=(A\cup B,E_0)\) the _popular subgraph_ of _G_.

The subgraph _G_<sub>0</sub> need not be connected: let _C_<sub>1</sub>_,...,C<sub>h</sub>_ be the set of connected components in _G_<sub>0</sub>. Call a component _C<sub>i</sub> non-trivial_ if \(|C_i|\ge 2\). The following observation will be useful.

**Observation 1** _For any non-trivial connected component C<sub>i</sub> in the popular subgraph G_<sub>0</sub>_, the number of unstable vertices in_ \(A\cap C_i\) _equals the number of unstable vertices in_ \(B\cap C_i\).

Indeed, every max-size popular matching _M_ restricted to _C<sub>i</sub>_ is a perfect matching, since all max-size popular matchings match the same set of vertices, while vertices left unmatched in any max-size popular matching are left unmatched in all popular matchings (see the discussion in Section 2.2). Thus \(|A\cap C_i|=|B\cap C_i|\). The number of stable vertices in \(A\cap C_i\) equals the number of stable vertices in \(B\cap C_i\), since every stable matching matches stable vertices in _C<sub>i</sub>_ among themselves. Hence Observation 1 follows.

**Lemma 1.** _Let C<sub>i</sub> be any connected component in the popular subgraph G_<sub>0</sub>_, M a popular matching in G, and_ \(\alpha\in\{0,\pm 1\}^n\) _a witness for M. Then one of the following two statements has to hold:_

- \(\alpha_u=0\) _for all vertices u of C<sub>i</sub> and no unstable vertex of C<sub>i</sub> is matched in M._<tbc>

**-** \(\alpha_u\in\{\pm 1\}\) _for all vertices u of C<sub>i</sub> and every unstable vertex of C<sub>i</sub> is matched in M._

_Proof._ Let _M_ be a popular matching in _G_. Consider the max-weight perfect matching LP (this is (LP1) given below) in \(\tilde{G}=(A\cup B,\tilde{E})\) with edge weight function wt_<sub>M</sub>_ described in Section 2. For any \(u\in A\cup B\), let \(\tilde{\delta}(u)=\delta(u)\cup\{(u,u)\}\). The linear program (LP2) is the dual LP.

\(\text{maximize}\sum_{e\in\tilde{E}}\text{wt}_M(e)\cdot x_e\) (LP1)

subject to<tbc>

