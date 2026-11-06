<tbc>contained inside \(\alpha\) in the given planar drawing, ii) no shortest cycle in C fully contains another shortest cycle from C in the planar drawing, and iii) there is no cycle (different from \(\alpha\)) contained inside \(\alpha\) that fully contains a cycle from C. We make each \(\beta\in\mathscr{C}\) a child of \(\alpha\), and recursively proceed until we reach facial cycles. Roughly speaking, the above gives a clean "laminar" structure of shortest cycles in the given plane graph, and one may think of it as encountering cycles "layer- by-layer" starting from the outermost cycle.

## A simpler case of edge-disjoint cycles.

The work \[4\] uses the laminar shortest cycles tree to obtain an FPT algorithm for Edge-Disjoint Shortest Cycle Packing, running in time \(k^{O(k)}\cdot n^{O(1)}\), for the given plane graph _G_ as follows: i) if the number of leaves in the laminar shortest cycles tree T is at least 4_k_, using the Four Color Theorem, one can directly conclude that the instance is a yes-instance. ii) Else, the number of leaves in T is less than 4_k_. In this case, they show that there is a set of _O(k_<sup>2</sup>) appropriately selected "deepest" (in the layers) shortest cycles which necessarily contains a solution (if one exists). We remark that the above marking scheme relies on the "strict laminarity" property of some optimal solution; we discuss strict laminarity in more detail shortly. With these marked cycles, now one can easily obtain an FPT algorithm running in time \(k^{O(k)}\cdot n^{O(1)}\).

Before describing the challenges we face in obtaining the \(2^{O(k)}\cdot n^{O(1)}\)-time algorithm for Diverse Shortest Cycle Coverage, and the way we overcome them, we discuss how using our approach we can obtain a simpler single-exponential FPT algorithm for Edge-Disjoint Shortest Cycle Packing (which is the special case of our problem for _d_=0). Again, the non-trivial case for us is when the number of leaves in the laminar shortest cycles tree T for the given plane graph _G_ is less than 4_k_. In this case, we can obtain a family Q of shortest paths that together cover all the non-tree cycles in _G_, where: i) \(|\mathcal{Q}|\in O(k)\), and ii) for each non-tree cycle _C_ in _G_, there are two<tbc>

S
P1
P2
P3
P4
P5
P6
t

Figure 3: The figure illustrates embedding of two distinct vertices _s,t_ in a plane graph _G_, connected by exactly six internally pairwise vertex disjoint _s-t_ paths of lengths exactly _g(G)/_2, where _g(G_) is the weighted girth of given graph _G_. In the laminar shortest cycles tree, the cycle \(P_1\cup P_6\) will be a node. For each \(i\in[5]\), the cycle \(P_i\cup P_{i+1}\) will be a child of \(P_1\cup P_6\). However, the shortest cycles \(P_i\cup P_j\), where \(i,j\in[6]\), _i\<j_ and \((i,j)\notin\{(1,6)\}\cup\{(i,i+1)|i\in[5]\}\), will not be represented in the laminar shortest cycles tree. It can be shown that every shortest cycle, other than the ones obtained only using the paths _P<sub>i</sub>_, \(i\in[6]\), is embedded: i) either "inside" (including the boundary) one of the cycles \(P_i\cup P_{i+1}\), \(i\in[5]\), or ii) embedded "outside" (including the boundary) the closed curve defined by \(P_1\cup P_6\).

