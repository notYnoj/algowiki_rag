<tbc>at most O(_k_), while the number of possible recursive calls produced at one call is bounded by \(k+(k+\mathbf{w}(A)+1)\cdot|\mathcal{P}|=\mathcal{O}(k^2)\). Therefore, the total number of recursive calls is \((k^2)^{\mathcal{O}(k)}=2^{k^{\mathcal{O}(1)}}\). The total running time is upper bounded with \(2^{k^{\mathcal{O}(1)}}\cdot n^{\mathcal{O}(1)}\).

The proof is complete.

## 5 XP-algorithm for rational edge weights

This section is dedicated to the proof of Theorem 2: given a graph (_G,_**w**) with rational edge weights not less than one, an acyclic subgraph of _G_ of weight at least **w**(_T_)+_k_ can be found in time \(n^{k^{\mathcal{O}(1)}}\cdot|\mathcal{I}|^{\mathcal{O}(1)}\).

We highlight that with rational edge weights, the problem becomes non-trivial even when _k_=1 and \(A=\emptyset\). In this case, we need to check whether a set \(S\subseteq E(T)\) with \(\mathbf{p}(S)\ge 1\) exists. Every such _S_ must contain an element with positive profit. Hence, for integer weights this implies that \(\mathbf{p}(s)\ge 1\) for some \(s\in S\), and we can consider only single-element sets. In contrast, when edge weights are rational, each **p**(_s_) may be arbitrarily close to zero. Thus, to reach \(\mathbf{p}(S)\ge 1\), we may now need to combine many small profits. Consequently, there are no longer any natural bounds on the size of _S_, which significantly increases the difficulty of the problem. Nevertheless, an XP algorithm must handle the case _k_=1 in polynomial time.

We overcome this obstacle in Section 5.1. Then, in Section 5.2, we address the additional challenges arising from the presence of allowed edges in _G_.

### 5.1 Maximizing profit under restrictions

A natural way to decide whether some set reaches a target profit is to find a set of maximum profit. It turns out that if the elements are restricted to not share inverse edges, this can be done efficiently. This subproblem is a key building block of our XP algorithm.

For a digraph (_G,_**w**), let _H_<sub>_G,_**w**</sub> be the undirected graph on _E(T_) where each vertex _e_ has weight **p**(_e_) and an edge connects _e_<sub>1</sub> and _e_<sub>2</sub> iff \(\mathrm{Inv}(e_1)\cap\mathrm{Inv}(e_2)\neq\emptyset\). Recall that if the sets Inv(_s_) for \(s\in S\) are pairwise disjoint, then the profit is additive. Thus, maximizing the profit of _S_ under this restriction is equivalent to finding the maximum-weight independent set in _H_<sub>_G,_**w**</sub>, which is NP-hard on general graphs. Fortunately, _H_<sub>_G,_**w**</sub> has a special structure.

**Lemma 6.** _For each edge-weighted digraph_ (_G,_**w**)_, H_<sub>_G,_**w**</sub> _is a perfect graph._

In our proof, we rely on the Strong Perfect Graph Theorem due to Chudnovsky, Robertson, Seymour and Thomas \[CRST06\]. Recall that a hole is an induced cycle of length at least five, and an antihole is a hole in the complement of a graph. A hole (or an antihole) is called odd if the corresponding cycle has an odd length. Perfect graphs are then characterized as follows.

**Proposition 3** (\[CRST06\])**.** _A graph is perfect if and only if it contains neither odd holes nor odd antiholes._

We proceed to the proof of Lemma 6.

_Proof of Lemma 6._ Let _H_:=_H_<sub>_G,_**w**</sub>. Suppose that _H_ contains an odd hole _e_<sub>1</sub>_,e_<sub>2</sub>_,...,e_<sub>2_t_+1</sub>, where \(t\ge 2\). We aim to find a triangle formed by three vertices of this hole, and thus derive a contradiction. Our crucial tool is the following claim about the structure of _H_.

