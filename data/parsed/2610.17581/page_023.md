## A Heavy Subgraph Problems

We begin by formally defining the other problems in Proposition 3. The Densest Bipartite Subgraph problem is to find a bipartite subgraph of a graph maximizing the density as defined for DSG. The solutions to this problem can be defined by a subset of vertices _S_ and an accompanying bipartition \(S=L\cup R\), containing only the induced edges _E(L,R_). The _d_-Max Cut problem is to color the vertices of graph with (exactly) _d_ colors and maximize the weight of edges with differently-colored endpoints, and the _d_-Sum-Max Clustering problem is to maximize the weight of that set’s complement, being the edges with same-colored endpoints. The ‘exactly’ is needed for _d_-Sum-Max Clustering, where the objective is _decreasing_ in number of colors. We also note that the work of \[16\] implicitly places the restriction that _d\<n/_2 so that \(\gamma>0\); this assumption is removable by a better lower bound on \(m(1-\frac{d}{n})^2\) for _f_(S<sup>∗</sup>), but outside of the scope of this work.

**Proposition 3** (\[16, Theorem 1.4\])**.** The following statements hold.

• Densest Sub(hyper)graph is a \((\frac{1}{logn},n)\)-heavy subgraph problem.<tbc>

• Densest Bipartite Subgraph is a \((\frac{1}{2log2n},n)\)-heavy subgraph problem.<tbc>

• _d_-Max Cut is a \((\frac{1}{2logd},1)\)-heavy subgraph problem.<tbc>

• _d_-Sum-Max Clustering is an \((\frac{n-2d}{nlogd},1)\)-heavy subgraph problem.<tbc>

