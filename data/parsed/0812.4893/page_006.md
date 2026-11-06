## 2.4 Marriages vs. Roommates

An immediate question is whether our results apply to the stable roommates problem - the non-bipartite version of the stable marriage problem. It is easy to see that a non-bipartite graph need not have an \(\epsilon\)-stable matching for \(\epsilon<1\): consider a triangle with "rotational-symmetric" preferences - there is one unstable edge to every matching edge.

## 2.5 Bicoloured vs. Bipartite

A graph is 2-colourable if and only if it is bipartite. Given a global view of a bipartite graph, it is trivial to 2-colour the graph. In the context of distributed algorithms this relationship is more subtle, however. Linial [23] shows that there is no constant-time algorithm for finding a maximal matching in a cycle with 2_n_ with vertices. Czygrinow et al. [4] show that finding a constant-factor approximation to maximum-cardinality matching with a deterministic constant-time algorithm is not possible either. However, these negative results heavily rely on the fact that the nodes in the bipartite graph do not know their colours in a 2-colouring. Theorem 2 shows that knowledge of the colour is not only necessary but also sufficient to find a constant-factor approximation of maximum-weight matching with a deterministic distributed constant-time algorithm.

The approximation factor of \(2+\epsilon\) in Theorem 2 is almost the best possible for _any_ algorithm (distributed or centralised) that has access only to the relative order of the weights, and not their numerical values. To see that no algorithm can have the approximation factor \(2-\epsilon\) for any \(\epsilon>0\), consider the following graph with the weight \(\alpha>1\).

If \(\alpha\gg 1\), an algorithm must include the edge with weight \(\alpha\) into the output (otherwise the algorithm has no approximation guarantee at all). But then the algorithm, having access only to the relative order of the weights, must include this edge also when \(1<\alpha<2/(2-\epsilon)\), which contradicts with the approximation guarantee \(2-\epsilon\).

1
2
O
O
2
1
1
2

