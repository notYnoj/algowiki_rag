we cannot compute _r_<sub>min</sub> efficiently,<sup>9</sup> if we were given this parameter, we could replace the 2/|_e_| scaling factor with _r_<sub>min</sub>/|_e_|. This would improve our query complexity to \(O(n\frac{r}{r_\mathrm{min}}\mathrm{log}n/\varepsilon^2)\), and in particular, obtain a bound of \(\widetilde{O}_\varepsilon(n)\) queries for _r_-uniform hypergraphs.

## 4 Barriers for Densest Subhypergraph Problems

In this section, we first show that cut algorithms cannot achieve \(o(\sqrt{n})\)-approximations to DSH with constant probability. We then rule out all approximations to D_k_SH for algorithms restricted to only cut or only edge queries.

### 4.1 Hardness of Approximating DSH and D_k_SH with cut queries

We build off an observation of Chakrabarty and Liao \[11\] to show that cut queries do not suffice to approximate DSH well or D_k_SH at all. They note that the simple graph _K_<sub>3</sub> shares the same cut structure as the multiplicity-2 hyperedge on three vertices,<sup>10</sup> which we will denote by \(2K_3^3\). By the additivity of the cut function over partitions of hyperedges, these ‘triangles’ can be overlaid arbitrarily to create families of hypergraphs with the same cut profiles; we use this insight to construct hard Densest (_k_-)Subhypergraph instances for cut algorithms.

Given an edge (_u,v_) and a set _L_ of \(\ell\) leaves, we construct the multihypergraphs _F_<sup>2</sup> and _F_<sup>3</sup> by overlapping \(\ell\) triangles (one for each vertex of _L_) along the shared edge (_u,v_), as seen in Figure 1. The hypergraph _F_<sup>2</sup> is composed of rank-2 triangles _K_<sub>3</sub> and thus \(\rho(F^2)=\rho(\{u,v\})=n/2\), while _F_<sup>3</sup> has all rank-3 triangles \(2K_3^3\) and so \(\rho(F^3)=\rho(V)=2n/(n+2)\le 2\). A uniform distribution over these two hypergraphs suffices for \(\Omega(\sqrt{n})\) hardness of approximation for cut algorithms in the _value estimation_ setting,<sup>11</sup> where one only has to estimate the objective’s value; however, this distribution admits a deterministic _O_(1)-approximation to DSH by simply returning the vertices of a single triangle. To prove our lower bound in the _subgraph finding_ setting, we hide a single copy of _F_<sup>2</sup> among \(\sqrt{n}\) copies of _F_<sup>3</sup>. As a result of Theorem 4.1, we show that cut algorithms cannot achieve an \(o(\sqrt{n})\)-approximation to DSH with constant probability.

**Theorem 4.1.** With only cut access to a hypergraph, it is impossible to obtain an \(o(\sqrt{n}/(1+p^{-1}))\)-approximation for DSH with probability at least _p_.

<sup>9</sup>To see this, consider a construction akin to Theorem 4.3, with a single cardinality _r_<sub>min</sub> hyperedge hidden among exponentially-many larger hyperedges. <sup>10</sup>\[14, Example 16\] implicitly uses this fact in noting that the graph _K_<sub>4</sub> and the complete 3-uniform hypergraph on four vertices, say \(K_4^3\), have the same cut profile. This already shows that determining the maximum density of a hypergraph within a 1.5-factor is impossible, as _K_<sub>4</sub> has density 1.5 and \(K_4^3\) has density 1. The elegance of this example is that both hypergraphs are unweighted. <sup>11</sup>See \[33\] for further discussion of the difference of these two settings in the cut query model.

cut = 2
cut = 2
x2
x2

W2
W3
W1
W4
u
v

W2
W3
x2
x2
W1
W4
x2
x2
u
v

(a) _K_<sub>3</sub> and \(2K_3^3\) have equal cut profiles.

(b) The construction _F_<sup>2</sup> has \(\rho(F^2)=\rho(\{u,v\})=N/2\).

(c) The construction _F_<sup>3</sup> has \(\rho(F^3)=\rho(V)=\frac{2\ell}{\ell+2}\le 2\).

Figure 1: The construction in Section 4.1 for \(\ell=4\). _F_<sup>2</sup> and _F_<sup>3</sup> have equal cut profiles, but density differing by a factor \(\Theta(N)\). Dashed regions mark the densest subhypergraph.

