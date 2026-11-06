Consequently, \(S^*\subseteq S\cup C(a,S)\). Since _C(b,S_) induces a connected subgraph of _G_ and \(S^*\cap C(b,S)=\emptyset\), then \(C(b,S)\subseteq C(b,S^*)\). As _S_<sup>∗</sup> and _S_ are both minimal (_a,b_)-separators, one cannot be included into the other. As _S_\\_S_<sup>∗</sup> is nonempty, it contains a vertex of _C(b,S_<sup>∗</sup>). Hence, \(C(b,S)\unknown C(b,S^*)\) and \(C(a,S^*)\unknown C(a,S)\) as announced.

**Definition 11.** _Let G be a graph with two vertices a,b such that_ \((a,b)\notin E(G)\)_, and_ \(S\subseteq V(G)\backslash\{a,b\}\)_. We say that S_ separates closely _the pair_ (_a,b_) _if S is either the_ (_a,b)-close separator or the_ (_b,a)-close separator in G._

Directly inspired by the close separators defined by Takata in \[28\], we define here a generalization of these separators.

**Definition 12** (_X_-Close (_a,b_)-separator)**.** _Consider a graph G, a pair_ \(a,b\in V(G)\) _and a set_ \(X\subseteq V(G)\) _such that_ \(a\in X\)_, and X_\\{_a_} _is an_ (_a,b)-separator. Set_ \(S\subseteq X\backslash\{a\}\) _is the X-close_ (_a,b)-separator if:_

\(S=\mathcal{S}_G(A,b)\text{\textit{with}}A=C_G(a,X\backslash\{a\}).\)

_By Lemma 4, the X-close_ (_a,b)-separator is a minimal_ (_a,b)-separator, is unique and can be computed in O(m_) _as A can be deducted in O(m). Moreover,_ \(S\unknown N(A)=R_G(a,X)\backslash\{a\}\).

Concretely, the _X_-close (_a,b_)-separator is the unique minimal (_a,b_)-separator included into _X_ which is "as close as possible" from _a_, or said differently with the smallest connected component containing _a_ in _G_\\_S_. The close (_a,b_)-separator - without any mention of _X_ - is the minimal (_a,b_)-separator of the entire graph as close as possible from _a_. Indeed, it is also the _X_<sup>∗</sup>-close (_a,b_)-separator, with _X_<sup>∗</sup>=_V(G_). In other words, the _X_-close (_a,b_)-separator can be seen as the extension of the close (_a,b_)-separator to a more restricted area of the graph.

As for Lemma 5, the _X_-close (_a,b_)-separator is parallel to any minimal (_a,b_)-separator included into _X_.

**Lemma 6** (_X_-Close (_a,b_)-separators and parallelism)**.** _Let_ \(X\subseteq V(G)\), \((a,b)\notin E(G)\), \(a\in X\)_, and S_<sup>∗</sup> _be the X-close_ (_a,b)-separator. Consider any other minimal_ (_a,b)-separator S included into X:_ \(S\subseteq X\) _and_ \(S\neq S^*\)_. Then, S_<sup>∗</sup> _and S are parallel and_ \(C_G(a,S^*)\unknown C_G(a,S)\).

_Proof._ The arguments are very similar to the ones used for Lemma 5. Assume by way of contradiction that some \(v\in S^*\) belongs to _C<sub>G</sub>(b,S_). As _S_<sup>∗</sup> is _X_-close for (_a,b_), we have \(S^*\subseteq R_G(a,X)\). Vertex _a_ must be separated from \(v\in C_G(b,S)\) by _S_, but \(v\in R_G(a,X)\): _v_ is reachable from _a_ despite _X_. This contradicts the fact that \(S\subseteq X\) separates pair (_a,v_). Therefore, \(S^*\subseteq S\cup C_G(a,S)\) and we conclude as in the proof of Lemma 5.

More generally, we say that an _X_-close separator is the _X_-close (_a,b_)-separator for some pair (_a,b_). In the remainder, _X_-close separators stand as a key tool to characterize PMC supersets (subsection 3.3).

## 2.3 A story of potential maximal cliques

Initially, PMCs were defined as a key tool for designing a divide-and-conquer algorithm computing the treewidth of an input graph \[3\]. Their original definition comes with the notion of _triangulation_. A graph _G_ is _chordal_ if every cycle of length at least 4 has a chord. A<tbc>

