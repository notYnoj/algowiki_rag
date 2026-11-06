### 1.2.3 Directed edge-capacities.

Our last non-reducibility result is for directed graphs with unit edge-capacities. By combining Theorem 1.2 with the naive algorithm and a flow volume bound obtained by Karger and Levine \[KL98\] in the context of (single pair) Max-Flow algorithms, we show that no deterministic SETH-based reduction is likely to prove an _n_<sup>4-_o_(1)</sup> conditional lower bound for this setting.

**Theorem 1.6.** _Under NSETH, for any fixed_ \(\varepsilon,\varepsilon'>0\) _there is no deterministic fine-grained reduction proving an_ \(\Omega(n^{5/2+\varepsilon}\sqrt{m}+n^{\omega(2,1,1)+\varepsilon^\prime})\) _SETH-based lower bound for All-Pairs Max-Flow on directed graphs with unit edge-capacities._

For \(\omega=2\), the bound becomes \(\Omega(n^{5/2+\varepsilon}\sqrt{m})\). Combining our framework with Gusfield’s algorithm for Gomory-Hu trees \[Gus90\] immediately provides an _O(n_<sup>2.5</sup>) time nondeterministic algorithm for All-Pairs Max-Flow in undirected graphs with unit edge-capacities. Although this algorithm may not be competitive given the \(\tilde{O}(m)\) time nondeterministic algorithm for Gomory-Hu tree construction \[AKT20a\], we still find this observation meaningful. Relatedly, a nondeterministic algorithm was the seed of inspiration for recent breakthroughs in randomized algorithms for this problem \[AKL<sup>+</sup>22, ALPS23\] (see \[AKT21b, AKT21a\] for discussions), and we believe that the same could happen to the nondeterministic algorithms presented in this paper.

Finally, for directed graphs with general edge-capacities, we could not prove a subquartic nondeterministic algorithm. However, as a consequence of Theorem 1.5, we conclude that a hypothetical deterministic fine-grained reduction from the edge-capacities setting to the node-capacities setting would imply the non-existence of an _n_<sup>4-_o_(1)</sup> conditional lower bound for the edge-capacities setting.

**Theorem 1.7.** _Suppose there exists a deterministic fine-grained reduction proving that an_ \(O(n^{4-\varepsilon})\) _time algorithm for All-Pairs Max-Flow on graphs with node-capacities implies an_ \(O(n^{4-\varepsilon^\prime})\) _algorithm for All-Pairs Max-Flow on directed graphs with edge-capacities, for some fixed_ \(\varepsilon,\varepsilon'>0\).

_Then, under NSETH, it is not possible to have an n_<sup>4-_o_(1)</sup> _SETH-based lower bound for All-Pairs Max-Flow on directed graphs with edge-capacities._

Whether such a reduction exists is a well-known open problem in the field (see e.g. Open Problem 2 in \[AKT20b\]), and Theorem 1.7 points to a significant barrier to its positive resolution.

## 1.3 Technical Overview

Below we explain the ideas behind our randomized algorithm for undirected graphs with unit node- capacities. Then, we elaborate on our non-reducibility results.

### 1.3.1 An algorithm for undirected graph with unit node-capacities

#### High level ideas in the algorithm in \[AKT20a\]

One of the core ideas in the \((1+\varepsilon)\)- approximation algorithm for graphs with edge-capacities could be interpreted as the following: The minimum cuts between any three nodes can be captured by just two cuts. This is represented also by the following inequality for any set of nodes _u,v,w_,

\(\mathsf{Max-Flow}(u,v)\ge min\{\mathsf{Max-Flow}(u,w),\mathsf{Max-Flow}(v,w)\},\) (1.1)

which translates to the algorithmic insight that the minimum cuts between a randomly picked pivot and every other node can capture many more minimum cuts in the graph. More concretely, it was shown in \[AKT20a\] that the minimum cuts computed from a random (source) pivot _p_ to all other (sink) nodes \(u\in V\) can be used to partition _V_ as follows. Let \(S_{u,p}\subset V\) be the side of _u_ in<tbc>

