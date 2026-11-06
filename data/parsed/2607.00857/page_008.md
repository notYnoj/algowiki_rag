polylogarithmic approximations are ruled out under the Exponential Time Hypothesis [33], and there are strong reasons to believe that the upper bound could be optimal [28].

However, there are several distinguishing details that make our problem different. First, we are interested in hypergraphs, which are generally harder but also less understood [6, 15, 14]. Second, in contrast to D_k_S, we want to approximately minimize the number of edges that are _not_ in the induced subgraph. This coincides for exact computation but could be very different for multiplicative approximation. Third, due to the large verification running time, the certificate optimally has size \(p=\Theta(n^{0.83})\), which corresponds to the number of vertices in the subgraph; however, the hardness hypotheses used for D_k_S only apply to the regime \(k\le\sqrt{n}\) [15, 9]. Finally, it is not clear how bicriteria approximation could help and only little is known for standard D_k_S [29]. Understanding what can be done and what cannot for our learning problem is hence an interesting challenge.

## 1.4 Notation and preliminaries

We only work with directed weighted graphs _G_=(_V,E,w<sub>G</sub>_) with _n_=|_V_| vertices. For \((u,v)\in E\), we use _w<sub>G</sub>(u,v_) to denote the weight of the edge (_u,v_). For \((u,v)\in V^2\backslash E\) with \(u\neq v\), we let \(w_G(u,v):=\infty\), and for _u=v_ we set _w<sub>G</sub>(u,v_):=0. We write _d<sub>G</sub>(u,v_) (or just _d(u,v_) when _G_ is clear from context) to denote the length of a shortest path from _u_ to _v_. For \(u,v,w\in V\) , we say that an algorithm **_relaxes_** a matrix entry _D[u,v_] with _D[u,w_]+_D[w,v_] to refer to setting _D[u,v_] to the minimum of the two values.

All our algorithms only add, subtract, and compare edge weights, so they work equally well in the word RAM model with polynomially-bounded integer edge weights and in the real RAM model with real edge weights.

## 1.5 Organization

We discuss Stages 1, 2, and 3 of the algorithm in Sections 2, 3, and 4, respectively. See Section 5 for a discussion on how to handle negative edge weights. In Section 6, we prove that the learning problem is NP-hard to solve exactly. Section 7 presents some empirical evidence that one can hope for small prediction error in practice.

## 2 Stage 1: Computing distance estimates

In the first stage of the algorithm, we compute the initial distance estimates from the certificate. The distance estimate matrix can also be defined by specific properties, as given in Lemma 3. Intuitively, we use the certificate to restrict the set of possible relaxations. The distance estimates are then the smallest matrix that can be obtained by using only these relaxations. To avoid having to do a relaxation multiple times, we compute distance estimates in increasing order.

\(\blacktriangleright\) **Lemma 3.** _There is an algorithm that, given a graph G and a certificate C with_ |_C[u,v_]|=_q for all_ \(u,v\in V\) _, computes the element-wise maximum matrix D that satisfies, for all_ \(u,v\in V\) ,

1. \(d(u,v)\le D[u,v]\)_, and_

2. \(D[u,v]=min\{w_G(u,v),min_{w\in C[u,v]}D[u,w]+D[w,v]\}\).

_The algorithm runs in time_ O(_n_<sup>2</sup>(_q_+log_n_)).

**Proof.** Our algorithm (see Algorithm 2) works in a Dijkstra-like manner by computing estimates in increasing order and relaxing other entries with just computed ones. The

