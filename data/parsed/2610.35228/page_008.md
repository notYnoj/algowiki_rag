<tbc>Next, by the Schur product theorem \[Sch11\], the entrywise product of two positive semidefinite matrices is positive semidefinite. To see this, write two such \(m\times m\) matrices as \(P=\sum_{i=1}^mp_ip_i^\top\) and \(Q=\sum_{k=1}^mq_kq_k^\top\). Then<tbc>

\(P\circ Q=\sum_{i=1}^m\sum_{k=1}^m(p_i\circ q_k)(p_i\circ q_k)^\top\unknown 0.\)

<tbc>The first step expands the entrywise product, and the second step follows because each summand is positive semidefinite. By induction, the entrywise power \(M^{\circ\ell}\) is positive semidefinite. Taking **1** to be the all-ones vector,

\(\sum_{u\in U}\sum_{v\in U}M(u,v)^\ell=\mathbf{1}^\top M^{\circ\ell}\mathbf{1}\ge 0.\)

The first step expands the quadratic form, and the second step uses \(M^{\circ\ell}\unknown 0\).

The minimum-degree greedy algorithm returns an independent set whose size is bounded below in terms of the graph’s average degree. This will turn the sparse induced subgraphs constructed later into large independent sets.

**Lemma 3.5** (Greedy)**.** _Let H be a graph on_ \(n\ge 1\) _vertices. Repeat the following until H is empty: pick a vertex v of minimum degree, add it to I, and delete v together with its neighbors. The resulting I is an independent set with_ \(|I|\ge n/(1+2|E(H)|/n)\)_, where H in this bound denotes the original graph._

_Proof._ The set _I_ is independent because the neighbors of each chosen vertex are deleted before the next choice. Let \(\Phi(H):=\sum_{w\in V(H)}1/(deg_H(w)+1)\), and let _N<sub>H</sub>_\[_v_\] denote the closed neighborhood of _v_. Consider one round, which removes _N<sub>H</sub>_\[_v_\] for a vertex _v_ of minimum degree. Every \(w\in N_H[v]\) has \(deg_H(w)\ge deg_H(v)\), so the removed terms of \(\Phi\) sum to at most |_N<sub>H</sub>_\[_v_\]|/(deg_<sub>H</sub>(v_)+1)=1. The degrees of the remaining vertices do not increase, so their contributions do not decrease. Hence \(\Phi\) drops by at most 1 per round. It is 0 at the end, so the number of rounds is at least the initial value \(\Phi(H)\). Since \(x\mapsto 1/(x+1)\) is convex on \([0,\infty)\), Jensen’s inequality gives \(\Phi(H)\ge n/(1+D)\), where \(D:=n^{-1}\sum_{w\in V(H)}deg_H(w)=2|E(H)|/n\) is the average degree of the original graph.

## 4 Proof of the main theorem

We prove Theorem 4.6 by finding a large sparse induced subgraph and applying the greedy algorithm. Section 4.1 establishes a dyadic correlation increment that increases the marginals after conditioning on a vertex. Section 4.2 bounds the logarithmic loss in the number of retained vertices in terms of the logarithmic gain in the marginal threshold. Section 4.3 combines these estimates to obtain a large sparse set after _O(t_) conditioning steps. Section 4.4 constructs a feasible pseudo- distribution with rational entries in time _N_<sup>_O(r_)</sup>. Section 4.5 finds a sparse set deterministically by enumerating conditioning sets and thresholds. Section 4.6 chooses the parameters and applies the greedy algorithm to prove the main theorem and its approximation guarantee. Finally, Section 4.7 applies Tulsiani’s integrality gaps to bound the parameter range in which the underlying implication from the Lasserre value to the independent-set size can hold for every graph.

### 4.1 Dyadic increment

The following lemma shows that conditioning on a suitable vertex increases the marginals on a subset of a dense set. It bounds the size of this subset in terms of the correlation scale.

