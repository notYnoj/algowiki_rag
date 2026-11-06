_2._ _construct a data structure of size_ \(\tilde{O}(\alpha(V))\) _that given a queried pair_ \(u,v\in V\) _outputs in_ \(t_{mf}=\tilde{O}(\text{\textit{Max-Flow}}(u,v))\) _time the value Max-Flow(u,v_) _(or simply in_ \(t_{mf}=\tilde{O}(1)\) _time in an alternative Monte Carlo version)._

For simplicity, we start with our Monte Carlo version of our algorithm, and later we discuss our Las Vegas algorithm.

## 3.1 Our Reinforced Tree-Like Data Structure: A Monte Carlo Version

In the remainder of this section, we demonstrate how to construct a data structure D that employs a tree structure to efficiently answer Max-Flow queries for an input graph _G_=(_V,E_). For a more conceptual grasp of the framework, we recommend the reader to become familiar with the original approximation algorithm designed for the edge-capacities case \[AKT20a\].

### Preprocessing

At a high level, the basic framework involves recursion. We begin by partitioning an instance \(V'\subseteq V\) using an _expansion_ operation into a few sets \(S_i\subseteq V'\), on which we will apply the operation recursively until they have a size of 1. This partition will (almost) satisfy property (\*\*) that was discussed in Section 1.3.1. To help us keep track of these partitions, we maintain a recursion-tree _T_. Each node \(t_{V^\prime}\) in the tree corresponds to an expansion operation, and stores \(V'\) along with some auxiliary information, such as a mapping from each node \(v\in V'\) to a cut (_S<sub>p,f(v)</sub>,C<sub>p,f(v)</sub>,S<sub>f(v),p</sub>_), as well as to other cuts computed directly for it. To perform a query on a pair \(u,v\in V\) we first check whether Max-Flow(_u,v_) was computed in one of the direct queries throughout the algorithm run. If not, we immediately gain information about the structure of the minimum vertex _uv_-cut. Then, we search for the recursion-node in _T_ that separated _u_ and _v_, i.e. the last \(V'\) that contains both _u_ and _v_, and output the smaller of (at most) two cuts stored in that node.

We will now shift our focus to the recursion tree and later prove that its depth is bounded by _O_(log_n_). At each depth of the tree, expansion operations are executed on disjoint subsets \(V'\). This is crucial for bounding the total number of Max-Flow queries involved in the expansion operations at that depth, which we will show is at most \(\tilde{O}(\alpha(V))\). More precisely, we run this algorithm _O_(log_n_) times on \(V'=V\) , thus constructing _O_(log_n_) recursion trees and demonstrate that with high probability, for every _u,v_ query the correct answer can be obtained from at least one of the recursion trees.

The following is the expansion operation on a subset \(V'\subseteq V\) . If \(V'=V\) (i.e., in the beginning) then repeat 4log_n_ times.

1. let \(V'_H:=\{u\in V':\alpha(u)\ge|V'|/20log_{4/3}n\}\), and compute directly Max-Flow(_u,v_) for every pair of nodes \(u,v\in V'_H\).<tbc>

2. pick a pivot node \(p\in V'\) uniformly at random.<tbc>

3. for every node \(u\in V'\backslash\{p\}\) perform a query Max-Flow(_p,u_) to get a vertex-cut (_S<sub>p,u</sub>,C<sub>p,u</sub>,S<sub>u,p</sub>_) where \(p\in S_{p,u}\), \(u\in S_{u,p}\), and the vertex-cut separating _u_ and _v_ (i.e. a _uv_-separator) is _C<sub>p,u</sub>_. Then, compute the intersection with \(V'\) of the side of _u_ in the cut, that is \(S_{u,p}\cap V'\), and denote this set by \(S'_{u,p}\), and similarly define \(S'_{p,u}\) and \(C'_{p,u}\).<tbc>

4. the following is a _reassignment_ process, which is designed for our case of vertex-cuts. We aim to satisfy three main criteria when reassigning nodes to cuts.<tbc>

(a) we may only assign a node _v_ to a cut (_S<sub>p,u</sub>,C<sub>p,u</sub>,S<sub>u,p</sub>_) with the same value as **value**(_C<sub>p,v</sub>_), which is an optimal cut for _v_. This is necessary to eventually output optimal cuts.<tbc>

