### 1.4 Perspectives

Even if our algorithm produces PMCs in output-linear time, it provides no guarantee on the delay between two outputs. In fact, we are even sure that the time taken before the return of the first PMC of _G_ cannot be less than exponential in _n_, because of the recursive nature of our procedure (as for BT-enum). Hence, finding a polynomial-delay enumeration algorithm for PMCs remains an open challenge. We wonder whether the traversal of the PMC-graph - our approach introduced to improve BT-enum - could not be itself a polynomial-delay algorithm enumerating PMCs. Concretely, one could compute one arbitrary PMC of _G_, fix it as a single element in the starting queue of a BFS, and explore the PMC-graph using our neighborhood relation N. For sure, the running time between two solutions would be polynomial in _n_ as all neighbors of a PMC can be determined fast. However, the main question is whether all PMCs would be enumerated with this method. We did not identify promising directions to prove this statement so far. But this BFS did not miss any PMCs on the numerous graph classes we tested experimentally, although we are blocked computationally by the brute-force checking (at most 20 vertices).

Another natural question is whether output-linear time can be maintained while only polynomial space is used. To reach this goal, one could think of exploring the recursion tree in a DFS manner, as done in \[7\]. Perhaps such an approach stands also as another promising direction to obtain polynomial-time delay.

Fomin and Villanger \[15\] showed that, for any integer \(k\ge 1\), knowing the list \(\Pi_G^{k+1}\) of PMCs of size at most _k_+1 allows checking whether the input graph _G_ has treewidth at most _k_ in time linear in \(|\Pi_G^{k+1}|\).<sup>3</sup> As a direct consequence, the existence of an FPT-output-linear time algorithm enumerating PMCs of small size would be a significant result, _i.e._ with running time \(O(f(k)n^{O(1)}|\Pi_G^k|)\) where _f_ is an arbitrary function and \(\Pi_G^k\) is the set of PMCs of size at most _k_. Indeed, it would give an algorithm deciding whether treewidth is at most _k_ in time \(\tilde{O}(f(k)|\Pi_G^k|)\), which could be very efficient in practice.

A final perspective is simply to implement our algorithm. The experimental study produced in \[21\], which displays numerous benchmarks of algorithms/instances, could be extended with our improvement for PMC enumeration. Such an experimental contribution would allow assessing in practice the performance gain offered by output-linear time, instead of output-quadratic one.

## 2 Preliminaries

In this section, we introduce some general notation and concepts related to connectivity in graphs. We also define the notion of _Potential Maximal Clique_ (PMC) and provide some observations.

### 2.1 General graph notations

All graphs mentioned in this paper are simple, finite, undirected, unweighted and connected. Any graph _G_=(_V,E_) is given with _V_ a set of _n_ vertices and \(E\subseteq V\times V\) a set of _m_ edges. As we will sometimes handle several graphs in parallel, function \(V(\cdot)\) will provide the vertex set of a graph, and \(E(\cdot)\) its edge set: here, _V(G_)=_V_ and _E(G_)=_E_. Given a set of<tbc>

<sup>3</sup>Separators of size at most _k_ are also needed.

