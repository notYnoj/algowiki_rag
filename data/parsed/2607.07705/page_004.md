<tbc>subgraph with at least _m/_2+_k_ edges in an arbitrary digraph can be simply reduced to the same problem on an oriented graph.

There is one particular lower bound for MAS that has been overlooked in this line of research. This lower bound is the _spanning tree_ guarantee, and it speaks for itself: any weakly-connected digraph admits an acyclic graph with at least _n_-1 edges. The spanning tree bound is also (algorithmically) inferior to the Poljak-Turzík bound.

The situation with these three guarantees changes slightly when we introduce edge weights in _G_. The algorithm of \[GKSY11\] for MAS above random ordering works in the multigraph setting when we are allowed to have several copies of the same edge in _G_. This can alternatively be seen as a weighted scenario. Instead of having several copies of the same edge, we keep _G_ a simple digraph, and we assign a positive integer weight **w**(_e_) to each edge \(e\in E(G)\). Then the random ordering guarantee is at least the half of the total edge weight, **w**(_E(G_))/2. Within this context, the mentioned algorithm of \[GKSY11\] finds an acyclic subgraph of total edge weight at least **w**(_E(G_))/2+_k_ in \(2^{\mathcal{O}(k\mathrm{log}k)}\cdot n^{\mathcal{O}(1)}\) running time.

The Poljak-Turzík lower bound was originally formulated in \[PT86\] for the weighted case, and it essentially guarantees that an edge-weighted _oriented_ graph _G_ contains an acyclic subgraph of weight at least **w**(_E(G_))/2+**w**(MinST(_G,_**w**))/4, where MinST(_G,_**w**) is the _minimum_ spanning tree of the underlying undirected graph of _G_ (or its minimum spanning forest, if _G_ is not weakly- connected). In \[EM18\], the authors posed an open question on whether the efficient FPT-algorithms above Poljak-Turzík can be generalized to the weighted case.

But are these two lower bounds that good when the edge weights are not evenly distributed? If, for example, the graph has just one heavy edge, whose weight is greater than the sum of all other weights, then this edge alone is better than any of the two guarantees can provide.

The spanning tree guarantee becomes the _maximum_ spanning tree (MaxST) guarantee in the weighted setting. Clearly, _G_ admits an acyclic subgraph of weight at least MaxST(_G,_**w**), a weight of the maximum spanning tree of the underlying undirected graph of _G_. This lower bound captures the case in the paragraph above and is better on instances where edge weights are concentrated around a sparse structure. For instance, it dominates both the random ordering and the Poljak-Turzík guarantees on instances where MaxST(_G,_**w**) is at least \(\frac{3}{4}\cdot\mathbf{w}(E(G))\). The MaxST lower bound is the central guarantee for MAS in our work. We give a formal definition to the corresponding parameterized problem below.

Maximum Weight Acyclic Subgraph Above MaxST (MAS/MaxST)

_Input:_ Weakly-connected _n_-vertex digraph _G_ with integer weight function \(\mathbf{w}:E(G)\rightarrow\mathbb{Z}_{\ge 1}\) assigned to its edges, and integer \(k\ge 0\).

_Task:_ Find an acyclic subgraph \(G'\) of _G_ such that \(\mathbf{w}(E(G'))\) is at least **w**(MaxST(_G,_**w**))+_k_, or report that \(G'\) does not exist.

This parameterization differs significantly from the Poljak-Turzík one. First, we do not have to enforce that _G_ is oriented for our guarantee to work. The restriction on the weak connectivity of _G_ can also be lifted, because _G_ can always be made weakly-connected by adding bridges between connected components of _G_. Second, these bounds are generally incomparable since they behave differently on sparse and dense graphs.

## Our contribution.

Our first main result is an FPT-algorithm for MAS/MaxST. It is obtained by a novel approach that combines several constructive ideas and precise analysis of the edges outside<tbc>

