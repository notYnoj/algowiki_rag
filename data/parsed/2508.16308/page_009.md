Now, let us assume that \(G'\) is _k_-partially _k_-colorable. Let \(\gamma'\) be such a coloring of \(G'\). We can deduce a proper _k_-coloring \(\gamma\) of _G_ from \(\gamma'\) by simply assigning \(\gamma(v):=\gamma'(v)\) for all \(v\in V\) . The fact that \(\gamma\) is a proper coloring of _G_ follows from Lemma 2.

Before we complete the proof of Theorem 1, we make this simple observation.

**Observation 1.** _The graph_ \(G'\) _satisfies that_ \(\Delta_{E(G^\prime)}=k\) _and therefore, any k-partial k-coloring is also a proper k-coloring of_ \(G'\).

If there exists a polynomial time algorithm for deciding _k_-partial _k_-colorability we can construct a polynomial time algorithm for _k_-colorability, which is a contradiction. Given an instance _G_ of proper _k_-colorability, we use the transformation described above to create an instance \(G'\) in polynomial time. Then we can use the _k_-partial _k_-colorability decision algorithm on \(G'\). By Lemma 3, this gives the answer whether _G_ is properly _k_-colorable or not.

## 7 Distributed Complexity

In this section, we prove that the problem of _k_-partial _k_-coloring is "global". More precisely, we prove the following theorem.

**Theorem 2.** _For every fixed integer_ \(k\ge 3\) _and for any k-partial k-coloring LOCAL algorithm_ A _for k-partially k-colorable graphs, there exists an n-node k-partially k-colorable graph G such that_ A _requires_ \(\Omega(n/k^3)\) _rounds to color G._

To prove Theorem 2, we first present the following graph gadget which has also been used in \[17\] and \[5\] in the context of distributed certification.

### Path of Cliques.

For integers \(k\ge 3\) and \(\ell\ge 2\), the graph \(\ell\)-path of _k_-cliques is defined on the vertex set \(V=[k]\times[\ell]\) with respect to \(\ell-1\) permutations \(\tau_1\), \(\tau_2\), _..._, \(\tau_{\ell-1}:[k]\rightarrow[k]\). Let the set of vertices {(1_,i),...,(k,i_)} be denoted by _V<sub>i</sub>_ for each \(i\in\ell\). The graph induced on _V<sub>i</sub>_ is a _k_-clique, denoted by \(K_k^i\). For each \(i\in[\ell-1]\), each vertex of _V<sub>i</sub>_ is adjacent to every vertex of _V_<sub>_i_+1</sub> except the perfect matching specified by the permutation \(\tau_i\), i.e. for vertices _a_ and _b_ from _V<sub>i</sub>_ and _V_<sub>_i_+1</sub> respectively, \(\{(a,i),(b,i+1)\}\in E\) if and only if \(b\neq\tau_i(a)\). We call the set of such edges between _V<sub>i</sub>_ and _V_<sub>_i_+1</sub> as _anti-matching_ specified by \(\tau_i\). See Figure 3 for an example. Also observe that \(\ell\)-path of _k_-cliques is uniquely determined by the permutations \(\tau_1,\dots,\tau_{\ell-1}\).

**Lemma 4.** _For every integer_ \(k\ge 3\) _and_ \(\ell\ge 2\)_, every_ \(\ell\)-path of _k_-cliques _is properly k-colorable._

a)
b)

Figure 3: Two 4-path of 3-cliques which differ only on the permutation \(\tau_2\) and the effect of this difference on the coloring of the two graphs. Anti-matchings induced by \(\tau_1,\tau_2,\tau_3\) are depicted with dashed lines, and the one induced by \(\tau_2\) being in violet color.

