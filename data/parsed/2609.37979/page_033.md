for all \(u,v\in V_1\) with \(\chi_\infty^G(u)=\chi_\infty^G(v)\),

\(\chi_\infty^G(\sigma(u))=\chi_\infty^G(\sigma(v))\text{and}w(u,\sigma(u))=w(v,\sigma(v)).\)

The following lemma, whose proof is deferred to Appendix A.1, shows that a memoryless strategy optimal from every vertex can be made color-consistent in linear time, given the stable 1-WL coloring.

**Lemma 7.14.** _Let G_=(_V,E,V_<sub>1</sub>_,V_<sub>2</sub>_,w,v_<sub>0</sub>) _be an_ Energy Game _instance with n vertices and m edges. Suppose we are given its stable 1-WL coloring_ \(\chi_\infty^G\) _and a memoryless strategy_ \(\sigma\) _of Player 1 that wins from every vertex with the minimum possible initial energy. Then a color-consistent memoryless strategy_ \(\widehat{\sigma}\) _with the same optimality property can be computed in O(n+m_) _time._

_Proof of Theorem 7.4._ We describe the different phases of the algorithm.

**Preprocessing:** For each graph \(G_i\in\mathcal{S}\), we run the 1-WL algorithm (Theorem 7.9) and compute its complete invariant for 1-WL equivalence (Theorem 7.10). Both subroutines run in time _O_((_n+m_)log_n_) time. We insert each string \(\mathrm{WL}_1(G_i)\in\{0,1\}^*\) into a binary search tree, where the _i_-th letter determines whether we take the left/right subtree on the _i_-th level. This takes time proportional to the length of the string WL<sub>1</sub>(_G<sub>i</sub>_), i.e., it can be done in time _O_((_n+m_)log_n_). For the corresponding node where the key WL<sub>1</sub>(_G<sub>i</sub>_) is saved, we save _WIN<sub>i</sub>=OPT(G<sub>i</sub>_) and the stable coloring \(\chi^{G_i}\). If an optimal memoryless strategy \(\sigma_i\) is provided, we apply Lemma 7.14 to compute and store a color-consistent optimal memoryless strategy \(\widehat{\sigma}_i\). This additional step takes _O(m+n_) time.

Note that, if two graphs \(G_i,G_j\in\mathcal{S}\) yield the same invariant, they are 1-WL equivalent (Theorem 7.10). In particular, by Theorem 7.12, this guarantees _WIN<sub>i</sub>=WIN<sub>j</sub>_, so no conflicting values can be assigned to a single node of the search tree. Overall, processing all _k_ graphs takes _O(k(n+m_)log_n_) time.

**Query:** Given the query graph _H_, we run the 1-WL algorithm (Theorem 7.9) and compute its complete invariant for 1-WL equivalence (Theorem 7.10) in _O_((_n+m_)log_n_) time. Looking up the computed invariant in the binary search tree takes _O_((_n+m_)log_n_) time, allowing us to return _OPT(H_)=_WIN<sub>i</sub>_ (which is correct by Theorem 7.12). If the string WL<sub>1</sub>(_H_) is not contained in the search tree, then we can correctly claim that _H_ is not isomorphic to any graph in S because graphs that are not 1-WL equivalent are not isomorphic. The total query time is _O_((_n+m_)log_n_).

**Reconstruction:** Suppose \(OPT(G_i)<\infty\) and a color-consistent optimal memoryless strategy \(\widehat{\sigma}_i\) is stored. For each Player 1 color class _C_ in _G<sub>i</sub>_, choose a representative _u<sub>C</sub>_ and set \(v_C=\widehat{\sigma}_i(u_C)\). For every Player 1 vertex \(u'\in V_H\) with \(\chi_\infty^H(u')=C\), choose a successor \(v'\) satisfying

\(w_H(u',v')=w_i(u_C,v_C)\text{and}\chi_\infty^H(v')=\chi_\infty^{G_i}(v_C),\)

and define \(\sigma_H(u')=v'\). Such a successor exists by Lemma 7.6 (Neighborhood Preservation). Selecting representatives and scanning the outgoing edges of Player 1 vertices takes _O(n+m_) time, using the color identifiers computed by Theorem 7.9.

To prove correctness, consider any walk \(u'_0u'_1\dots\) consistent with \(\sigma_H\), and choose \(u_0\in V(G_i)\) with \(\chi_\infty^{G_i}(u_0)=\chi_\infty^H(u'_0)\). As in the proof of Theorem 7.12, we construct a shadow walk _u_<sub>0</sub>_u_<sub>1</sub>_..._ in _G<sub>i</sub>_ with matching vertex colors and edge weights. At Player 1 vertices, color consistency ensures that \(\widehat{\sigma}_i(u_k)\) has the same successor color and edge weight as the move chosen by \(\sigma_H\) at \(u'_k\). At Player 2 vertices, Neighborhood Preservation supplies a matching edge. Hence the shadow walk is consistent with \(\widehat{\sigma}_i\).

The shadow-play argument in both directions shows that equally colored vertices have the same minimum initial energy. Since \(\widehat{\sigma}_i\) is optimal from every starting vertex and the two walks have identical edge weights, \(\sigma_H\) is optimal from every starting vertex as well. In particular, it wins from the designated initial vertex with energy _OPT(H_)=_OPT(G<sub>i</sub>_). The total query time remains _O_((_n+m_)log_n_).

