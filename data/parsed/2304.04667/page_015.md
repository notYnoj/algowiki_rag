**Algorithm: Cuts Verification**

1. perform the multiplication \(P'=PM_G\).<tbc>

2. for every pair \((u,v)\in Q\) verify that \(\sum_{z\in T_{uv}}P'[g_{uv},z]\le p_{uv}\).<tbc>

3. if at least one verification step returned "no", reject, otherwise accept.

### Correctness.

Observe that for every node _z_, \(P'[g_{uv},z]\) is precisely \(\sum_{w\in S_{uv}}c(w,z)\), and thus for each pair \((u,v)\in Q\), the verified values are precisely what we are looking for:

\(\sum_{z\in T_{uv}}P'[g_{uv},z]=\sum_{w\in S_{uv},z\in T_{uv}}c(w,z)=\mathbf{value}(S_{uv},T_{uv}).\)

### Running time.

The total size of |_Q_| cut guesses (by their nodes) is \(O(|Q|\cdot n)\). Multiplying an \(|Q|\times n\) matrix with an \(n\times n\) matrix takes \(n^{\omega(\mathrm{log}_n(|Q|),1,1)}\) time, and counting _O(n_) entries per pair of nodes in _Q_ takes \(O(|Q|\cdot n)\) time, which brings the total verification time to \(O\left(n^{\omega(\mathrm{log}_n(|Q|),1,1)}+|Q|\cdot n\right)\le O\left(n^{\omega(\mathrm{log}_n(|Q|),1,1)}\right)\), concluding Lemma 2.2.

## 2.1 Succinct _st_-flows in Various Settings

In this section, we detail the volume upper bounds for flows in various settings, that we either prove or reference.

### 2.1.1 Unit node-capacities

**Lemma 2.3.** _Let G_=(_V,E_) _be an undirected graph with unit node capacities,_ \(s,t\in V\) _a pair of nodes, and f<sub>st</sub> an st-flow in G. Then_ \(\mathbf{volume}(f_{st})\le 2n\).

_Proof._ Observe that _f<sub>st</sub>_ consists of internally node-disjoint paths. Therefore, each node in _V(f<sub>st</sub>_) except for _s_ and _t_, has degree 2 in _f<sub>st</sub>_, and consequently we have \(\mathbf{volume}(f_{st})\le 2n\), as required.

### 2.1.2 Unit edge-Capacities

In contrast to the case of unit node-capacities, here, nodes in _V(f<sub>st</sub>_) can have arbitrarily high degrees in _f<sub>st</sub>_, and it is not immediately evident that the total volume of _f<sub>st</sub>_ is bounded by anything significantly smaller than _m_. We use a general lemma from \[KL98\] that works even for arbitrary integer capacities, in our context of (multi-)graphs with unit edge-capacities:

**Lemma 2.4** (Theorem 7.1 in \[KL98\], rephrased)**.** _Let G_=(_V,E_) _be a directed graph with integer edge-capacities,_ \(s,t\in V\) _a pair of nodes, and f<sub>st</sub> an st-flow in G. Then_ \(\mathbf{volume}(f_{st})\le\tilde{O}\left(n\sqrt{\mathbf{value}(f_{st})}\right)\).

### 2.1.3 General node-capacities

We will now prove that the total volume necessary to ship any flow value in a node-capacitated network never exceeds 2_n_.

**Lemma 2.5.** _Let G_=(_V,E_) _be a directed graph with node-capacities,_ \(s,t\in V\) _be a pair of nodes, and f<sub>st</sub> be an st-flow in G. Then there exists an st-flow_ \(f'_{st}\) _in G of the same value_ \(\mathbf{value}(f'_{st})=\mathbf{value}(f_{st})\) _such that_ \(\mathbf{volume}(f'_{st})\le 2n\).

