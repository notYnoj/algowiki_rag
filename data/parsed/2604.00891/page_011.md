Maximum-Weight Rooted Parallel Induced Minor

**Input:** A graph _G_=(_V,E_), an edge-weight function \(w:E\rightarrow\PazoBB{R}^+\), a multigraph _H_=(_U,F_), a function \(\eta:U\rightarrow 2^V\), an integer _k_, and a value \(W\in\PazoBB{R}\).

**Question:** Is there an induced subgraph \(G'\) of _G_ with at most _k_ vertices and of total weight at least _W_ such that \(G'\) contains all vertices in \(\bigcup_{u\in U}\eta(u)\) and _H_ is a rooted parallel induced minor of \(G'\)?

The next problem we study is Maximum-Weight Induced Forest.

Maximum-Weight Induced Forest

**Input:** A graph _G_=(_V,E_), a vertex-weight function \(w:V\rightarrow\PazoBB{R}\), an integer _k_, and a value \(W\in\PazoBB{R}\).

**Question:** Is there a set \(S\subseteq V\) of at most _k_ vertices of total weight at least _W_ such that _G_\[_S_\] is a forest?

The definition of _k_-Subgraph Scoring was already shown in the introduction. We repeat it here to have all problem definitions in one place.

_k_-Subgraph Scoring

**Input:** A directed graph _G_=(_V,A_), a vertex-cost function \(c:V\rightarrow\PazoBB{N}\), a weight function \(w:V\cup A\rightarrow\PazoBB{R}\), an integer _k_, and values \(\alpha_1,\alpha_2,\alpha_3,\beta,W\in\PazoBB{R}\).

**Question:** Is there a set _S_ of cost exactly _k_, that is, \(\sum_{v\in S}c(v)=k\) and

\(\alpha_1\big(\sum_{(u,v)\in Au,v\in S}w((u,v))\big)+\alpha_2\big(\sum_{(u,v)\in Au\in S,v\notin S}w((u,v))\big)+\alpha_3\big(\sum_{(u,v)\in Au\notin S,v\in S}w((u,v))\big)+\beta\big(\sum_{v\in S}w(S)\big)\ge W?\)

When the parameters \(\alpha_1,\alpha_2,\alpha_3\) and \(\beta\) are clear from the context, then we call the value for a particular set _S_ the **_score_** of _S_. All other problems we study are simple corollaries of the above problems. We hence only give informal problem statements for these. In Weighted Partial Vertex Cover, the input consists of a graph _G_ with positive integer costs and real-valued edge weights, an integer _k_, and a real value _W_. The question is whether there is a set of vertices of cost at most _k_ such that the weight of covered edges is at least _W_. An edge is covered if at least one of its endpoints is contained in the solution. Note that we require all costs to be integers as otherwise the problem is para-NP-hard when parameterized by _k_ (start with an instance (_G,k,W_) of unweighted Partial Vertex Cover and set the weight of each vertex to \(\frac{1}{k}\)). In Maximum- Weight Independent Set, we are given a graph _G_ with real-valued vertex weights, an integer _k_, and a real value _W_. The questions is whether an independent set of size at most _k_ and weight at least _W_ exists.

In Densest _k_-Subgraph, we are given an undirected graph _G_ and two integers _k_ and _W_. The question is whether there is a set of exactly _k_ vertices such that there are at least _W_ edges with both endpoints in that set. Maximum (_k,n-k_)-Cut can be defined on both undirected and directed graphs together with two integers _k_ and _W_. In the undirected setting, the question is whether there is a set _S_ of exactly _k_ vertices such that there are at least _W_ edges with exactly one endpoint in _S_. In the directed setting, the question is whether there is a set _S_ of exactly _k_ vertices such that there are at least _W_ edges (_u,v_) with \(u\in S\) and \(v\notin S\).

In Minimum-Weight Subgraph Isomorphism, the task is to find a subgraph of minimum weight that is isomorphic to a given pattern graph _H_. In Maximum-Weight Induced Subgraph Isomorphism, the task is to find an induced subgraph of maximum weight that is isomorphic to a<tbc>

