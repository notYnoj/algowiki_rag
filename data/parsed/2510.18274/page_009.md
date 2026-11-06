**Proposition 2.10.** _Let G_=(_V,E_) _be an underlying graph. Then, for any disjoint sets_ \(A,B\subseteq V\) _, we can determine_ FindEdge(_A,B_) _using either_

• _O_(1) _cut queries to G if_ FindEdge(_A,B_) _outputs_ "NONE" _(i.e._ \(E\cap\left(A\times B\right)=\emptyset\)_), or_<tbc>

• _O_(log_n_) _cut queries to G if_ FindEdge(_A,B_) _outputs an edge_ \((a,b)\in E\cap\left(A\times B\right)\).

One of its abundant benefits of the find-edge queries is that it allows us to learn the (contracted) graphs with query complexity near-linear in the representation size of the graph.

**Lemma 2.11.** _Let_ (_V_<sub>1</sub>_,...,V<sub>z</sub>_) _be a partition of a vertex set of G_=(_V,E). Then, we can learn all edges of_ \(G\langle V_1,\dots,V_z\rangle\) _using_ \(\widetilde{O}\left(z+|G\langle V_1,\dots,V_z\rangle|\right)\) _cut queries._

### 2.2 Two-Party Communication Model

In this setting, an input graph _G_=(_V,E_) is edge-partitioned across two players, namely Alice has her private graph _G<sub>A</sub>_=(_V,E<sub>A</sub>_), and Bob has his private graph _G<sub>B</sub>_=(_V,E<sub>B</sub>_), with \(E=E_A\cup E_B\). The players’ objective is to collaboratively compute a joint task (in this case, a minimum _s-t_ cut) by exchanging a sequence of messages, known as a _protocol_, while minimizing the total amount of communication. Note that the only notion of cost here is the communication; thus, Alice and Bob can be assumed to have unlimited local computation power.

Within this communication setting, the players can also "deterministically" compute a cut sparsifier and use it to approximate the max-flow/min-cut value with the same complexity.

**Lemma 2.12.** _For any_ \(\varepsilon\in(0,1)\)_, there is a deterministic protocol such that Alice and Bob jointly computes an_ \(\varepsilon\)_-cut sparsifier of G with_ \(\widetilde{O}(n/\varepsilon^2)\) _edges and maximum weight_ \(\widetilde{O}(\varepsilon^2n)\)_. The protocol communicates_ \(\widetilde{O}(n/\varepsilon^2)\) _bits and always succeeds._

**Corollary 2.13.** _For any_ \(\varepsilon\in(0,1)\)_, Alice and Bob can jointly and deterministically compute a value f such that_ \((1-\varepsilon)\nu(G)\le f\le(1+\varepsilon)\nu(G)\) _using_ \(\widetilde{O}(n/\varepsilon^2)\) _bits of communication._

## 3 Overview

The starting point of our algorithm builds on the work of \[RSW18\]. Their algorithm, in which we will call RSW algorithm, can be viewed as computing a partition of the vertex set whose contraction results in a sparse graph that preserves all _s-t_ minimum cuts. That work focuses exclusively on the cut-query model and yields a randomized algorithm with \(\widetilde{O}(n^{5/3})\) query complexity for the task. Upon closer inspection, we observe that the complexity can be parameterized in terms of \(\nu(G)\) depending on the computation models: to \(\widetilde{O}(n^{4/3}\nu(G)^{1/3})\) cut queries and to \(\widetilde{O}(n\cdot\nu(G)^{2/3})\) bits of communication. At first glance, these parameterized improvements may seem unhelpful, as \(\nu(G)\) can be as large as \(\Omega(n)\). However, to state the obvious, when \(\nu(G)\) is truly sublinear, these bounds yield a complexity of \(n^{5/3-\Omega(1)}\) in both models. This observation motivates a simple yet powerful scheme: apply a preprocessing step to _G_ that reduces the _s-t_ min-cut to \(\Delta=o(n)\) while preserving all _s-t_ min-cuts, and then apply the RSW algorithm to the post-processed graph. If this preprocessing can be implemented efficiently, it opens the possibility of achieving overall sub-_n_<sup>5/3</sup> complexity. We summarize this framework in the table below.

