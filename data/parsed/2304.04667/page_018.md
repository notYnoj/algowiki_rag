**Lemma 2.8.** (Directed graphs with general node-capacities.) _The nondeterministic time complexity of Min-Cut data structure on directed graphs with general node-capacities is_ \(\tilde{t}_p(m)=O\left(n^{\omega(2,1,1)}\right)\) _with_ \(\tilde{t}_{mc}=O(1)\).

Assuming \(\omega=2\), the time becomes \(\tilde{t}_p(m)=O(n^3)\). With current algorithms, the time is \(\tilde{t}_p(m)=O(n^{3.252})\) using rectangular matrix multiplication \[GU18\].

_Proof of Lemma 2.8._ By combining Theorem 2.1 with the flow bound in Lemma 2.5 and the naive algorithm which has _t<sub>pq</sub>(m),t<sub>po</sub>(m_)=_O(n_<sup>2</sup>) and _t<sub>mc</sub>(m_)=_O_(1), we get a nondeterministic time of \(\tilde{t}_p(m)=O\left(n^{\omega(2,1,1)}\right)\) with \(\tilde{t}_{mc}=\tilde{O}(1)\), as required by Lemma 2.8.

**Lemma 2.9.** (Directed graphs with unit edge-capacities.) _The nondeterministic time complexity of Min-Cut data structure on directed graphs with unit edge-capacities is_ \(\tilde{t}_p(m)=O\left(n^{5/2}\sqrt{m}+n^{\omega(2,1,1)}\right)\) _with_ \(\tilde{t}_{mc}=O(1)\).

Assuming \(\omega=2\), the time becomes \(\tilde{t}_p(m)=O\left(n^{5/2}\cdot\sqrt{m}\right)\). With current algorithms, the time is \(\tilde{t}_p(m)=O\left(n^{5/2}\cdot\sqrt{m}+n^{3.252}\right)\) using an algorithm for rectangular matrix multiplication \[GU18\].

_Proof of Lemma 2.9._ According to Lemma 2.4, the flow part in the nondeterministic time \(\tilde{t}_p(m)\) in Theorem 2.1 is<tbc>

\(\sum_{(u,v)\in Q}\mathbf{volume}(f_{uv})\le\sum_{(u,v)\in Q}n\sqrt{\mathbf{value}(f_{uv})}\le\sum_{(u,v)\in Q}n\cdot\sqrt{min\{d_{out}(u),d_{in}(v)\}}.\)

<tbc>By combining Theorem 2.1 with the flow bound in Lemma 2.4 and the naive algorithm which has _t<sub>pq</sub>(m),t<sub>po</sub>(m_)=_O(n_<sup>2</sup>), we get a nondeterministic time bound of

\(\tilde{t}_p(m)=O\left(n^2\cdot n\cdot\sqrt{m/n}+n^{\omega(2,1,1)}\right)=O\left(n^{5/2}\sqrt{m}+n^{\omega(2,1,1)}\right),\)

with \(\tilde{t}_{mc}=\tilde{O}(1)\), as required by Lemma 2.9.

## 3 All-Pairs Max-Flow for Unit Node-Capacities

In this section, we prove a generalized version of Theorem 1.1 that accounts for node-capacities. We use parameter \(\alpha:V\rightarrow[n]\) to represent for a node \(v\in V\) an upper bound on the size of the minimum _uv_-separator |_C<sub>u,v</sub>_|, for all nodes \(u\in V\) .<sup>18</sup> \(\alpha\) is defined recursively, such that for any subset of nodes \(A\subseteq V\) , \(\alpha(A)\) is equal to the sum of \(\alpha(u)\) over all nodes \(u\in A\). It is important to note that in the case of unit node-capacities, we have \(\alpha(u)\le d(u)\). This implies that \(\alpha(V)\le 2m\), which concludes Theorem 1.1.

**Theorem 3.1.** _There is a randomized Las Vegas algorithm that given an undirected graph G_=(_V,E_) _with unit node-capacities, makes_ \(t_{pq}(m)=\tilde{O}(\alpha(V))\) _calls to Max-Flow in G and spends_ \(t_{po}(m)=\tilde{O}(n\alpha(V))\) _time outside of these calls, and can:_

1. _construct a data structure of size_ \(\tilde{O}\left(\alpha(V)^{3/2}\right)\) _that stores a set_ C _of_ \(\tilde{O}(\alpha(V))\) _vertex cut- separators, such that given a queried pair_ \(u,v\in V\) _outputs in_ \(t_{mc}=\tilde{O}(1)\) _time a pointer to an optimal uv-separator in_ C.<tbc>

<sup>18</sup>Via folklore reductions it captures, in particular, minimum vertex-cuts that in addition have smallest separator sizes.

