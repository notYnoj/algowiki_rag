Listing or finding the _extremities_ of **G**: These are vertices \(v\in V\) such that **G**[_V_\\_N[v_]] is connected. This can be derived directly from the previous problem.

Determining whether **G** has a _star-cutset_ or a _clique-cutset_: A _cutset_ is a set of nodes \(S\subseteq V\) such that **G**[_V_\\_S_] is disconnected; it is a _star-cutset_ if there is a central node in _S_ connected to all other nodes in _S_, and a _clique-cutset_ if **G**[_S_] is a clique.

Recognizing _AT-free graphs_: This involves verifying whether **G** contains an _asteroidal triple_--an independent set of three vertices \(x,y,z\in V\) such that, between any two vertices in the triple, there exists a path avoiding the neighborhood of the third vertex.

Listing or finding _dominating pairs_: These are distinct nodes \(u,v\in V\) such that for every _u-v_ path \(\pi\) and every node \(w\in V\) , the path \(\pi\) contains at least one neighbor of _w_ or contains _w_ itself. (In other words, the vertex set of any path between these two vertices is a dominating set of the graph.)

Listing or finding _two-pairs_: These are distinct nodes \(u,v\in V\) such that all induced (or equivalently, chordless) paths between _u_ and _v_ have length two.

For all of these problems, the authors present algorithms with running times strictly _between_ O(_n_<sup>3</sup>) _and_ \(\mathcal{O}(n^\omega)\). Specifically, as mentioned earlier, an O(_n_<sup>2.79</sup>)-time algorithm is provided for all problems, except for recognizing AT-free graphs, which is solved in \(\mathcal{O}(n^{4\omega/(\omega+1)})=\mathcal{O}(n^{2.81})\) time. As mentioned earlier, the O(_n_<sup>2.79</sup>) time can be replaced by O(_n_<sup>2.69</sup>) by slightly modifying the algorithms. Prior to [KS06], only O(_nm_)-time algorithms were known for some of these problems, which still take \(\Omega(n^3)\) time on dense graphs.

## 1.2 Why \(n^\omega\) seems needed for all the problems

Spinrad and Kratsch provide evidence that solving the problems listed above requires at least \(n^{\omega-o(1)}\) time. To support this, they identify three problems for which no algorithms faster than \(\mathcal{O}(n^\omega)\) are currently known (see Figure 1 for the hardness proven by [KS06] from these problems). For each of the three problems one hypothesizes that in the word-RAM model with _O_(log_n_) bit words, the problem requires \(n^{\omega-o(1)}\) time.

**Determining whether a graph contains a triangle:** The corresponding Triangle Detection Hypothesis that the problem requires \(n^{\omega-o(1)}\) time has been repeatedly used within fine-grained complexity (e.g., [Vas18, VW18, AV14]). It is also supported by the subcubic equivalence [WW10, VW18] between triangle detection and Boolean matrix multiplication.

**Determining whether a graph contains a dominated vertex:** A _dominated vertex_ is a node _x_ such that \(N(x)\subseteq N[y]\) for some \(y\neq x\). This problem turns out to be exactly equivalent to the Orthogonal Vectors (OV) problem in _n_ dimensions (see Section B in the appendix for a proof). Whether this high-dimensional OV problem requires fast matrix multiplication was first asked<sup>3</sup> almost 3 decades ago by Aingworth, Chekuri, Indyk and Motwani [ACIM99]. The hypothesis that OV in _n_ dimensions requires \(n^{\omega-o(1)}\) time has been used in fine-grained complexity in recent years (see e.g., [DK21]).

**Determining whether a graph contains a simplicial vertex:** A node _v_ is _simplicial_ if **G**[_N(v_)] is a clique. The hypothesis that Simplicial Vertex requires \(n^{\omega-o(1)}\) time has also been used in recent years for hardness results in fine-grained complexity (see e.g., [DJVW22]).

<sup>3</sup> They actually asked whether distinguishing between diameter 2 and 3 in an undirected graph in subcubic time without matrix multiplication, but this problem is easily seen to be equivalent to OV in _n_ dimensions, e.g., via a reduction as in [RV13, Vas18].

