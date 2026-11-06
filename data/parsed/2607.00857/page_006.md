### _C._ While the matrix _D_ already satisfies

\(D[u,v]\le min_{w\in C[u,v]}D[u,w]+D[w,v],\) (1)

we would need

\(D[u,v]\le min_{w\in V}D[u,w]+D[w,v]\) (2)

to make sure that no further relaxation is possible. The verification algorithm in the second stage finds all entries that could be relaxed as well as entries for which the certificate is not sufficient to verify (2). To achieve that, we adapt the co-nondeterministic algorithm for Exact Triangle from Theorem 9.7 in [12]. Intuitively, our certificate takes the role of their nondeterministic prover. The algorithm for this stage computes a set \(U\subseteq\mathrm{U}(G,C,p)\), such that all \((u,v)\in V^2\backslash U\) are guaranteed to satisfy (2).

In the third stage, we use the set _U_ as a starting point to fix all incorrect distance entries in _D_. We face a similar problem as in Stage 1 of our algorithm: This time, we want to restrict ourselves to _O(n_) relaxations per incorrect or unverified entry in _D_ while guaranteeing that afterwards each entry satisfies (2). To solve it, we again update distance entries Dijkstra-like in the increasing order, relying on the fact that we can assume non-negative edge weights. Additionally, the algorithm works in a lazy manner and only relaxes entries _D_[_u,v_] with vertices _w_ if at least one of (_u,v_), (_u,w_), or (_w,v_) is in _U_ or has been witnessed as incorrect. Our algorithm for this section can hence be regarded as a more sophisticated implementation of the ideas already employed in the first stage.

### 1.2 Learnability

How do we argue that it is possible to efficiently learn a certificate with a small prediction error? A standard approach (see, e.g., [19, 13, 36]) would be to use the _probably approximately correct_ (PAC) learning framework. There, we assume we have sample access to an unknown distribution D over \(V\times V\) matrices of edge weights. The goal is to find a certificate that (approximately) minimizes the expected prediction error \(\mathbb{E}_{G\sim D}\eta(G,C,p)\). By a standard argument (see, e.g., [36, Section 4]), since the number of different possible certificates is upper bounded by \(\genfrac(){pt}{2}{n}{q}^{n^2}\le 2^{n^3}\), it suffices to consider _k=O(n_<sup>3</sup>) samples from D, and solve the corresponding empirical risk minimization (ERM) problem, i.e., find a certificate that minimizes the prediction error averaged over the sample:

D[a, d] = 3
D[b, d] = 2
1
1
1
a
b
C
d
C[a, d]
C[b, d]

**Figure 1** A counterexample for why the Floyd-Warshall algorithm with relaxations restricted to the certificate cannot compute _D<sub>G,C</sub>_. In the given graph _G_, with four vertices and three black edges, each of weight 1, with _C_ defined by _C_[_a,d_]={_b_} and _C_[_b,d_]={_c_} (all other certificate sets equal {_a_}), _D<sub>G,C</sub>_ should contain distances according to the colored arrows. However, when relaxing first _D_[_a,d_] with _b_ and then _D_[_b,d_] with _c_, only the latter blue distance is correct. Note that standard Floyd-Warshall corresponds to the case where _C_[_u,v_]=_V_ , for every \(u,v\in V\) , where the order of considered intermediate vertices does not matter.

