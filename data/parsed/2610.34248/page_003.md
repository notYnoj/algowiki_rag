**Algorithm 1** SearchLayer: Greedy search in HNSW layer

Input: Query \(\vec{q}\), enter point _ep_, search width _ef_, layer \(\ell\)<br>
Output: Set W of _ef_ closest neighbors to \(\vec{q}\) in layer \(\ell\)<br>
\(V\leftarrow\{ep\}\triangleright\) Visited set<br>
\(C\leftarrow\{ep\}\triangleright\) Candidate set<br>
\(W\leftarrow\{ep\}\triangleright\) Result set<br>
while |C|\>0 do<br>
   \(c\leftarrow\) extract nearest element from C to \(\vec{q}\)<br>
   \(f\leftarrow\) furthest element from W to \(\vec{q}\)<br>
   if \(dist(c,\vec{q})>dist(f,\vec{q})\) then<br>
   break \(\triangleright\) Cannot improve W further<br>
   for each \(e\in\mathcal{N}_\ell(c)\) do<br>
   if \(e\notin V\) then<br>
   \(V\leftarrow V\cup\{e\}\)<br>
   \(f\leftarrow\) furthest element from W to \(\vec{q}\)<br>
   if \(dist(e,\vec{q})<dist(f,\vec{q})\) or |W|\<ef then<br>
   \(C\leftarrow C\cup\{e\}\)<br>
   \(W\leftarrow W\cup\{e\}\)<br>
   if |W|\>ef then<br>
remove<br>
curthest<br>
element<br>
from<br>
_W_<br>
to<br>
\(\vec{q}\)<br>
return W

## 2.1 Notation

Let \(\mathcal{D}=\{\vec{v}_0,\vec{v}_1,\dots,\vec{v}_{N-1}\}\) be a dataset of _N_ vectors in R_<sup>d</sup>_, where _d_ is the dimension. We use \(\vec{v}[j]\) to denote the _j_-th coordinate of vector \(\vec{v}\). Let \(dist:\mathbb{R}^d\times\mathbb{R}^d\rightarrow\mathbb{R}_{\ge 0}\) denote a vector distance function. The index set is \[_N_\]:={0,1_,...,N_-1}. For any set S, |S| is its cardinality. A graph G=(V,E) has vertices \(\mathcal{V}\subseteq\mathcal{D}\) and undirected edges E. For any \(\vec{v}\in\mathcal{V}\), \(\mathcal{N}(\vec{v})\) denotes its neighbor set.

## 2.2 _k_-Nearest Neighbor Search

For the _k_-nearest neighbor (_k_-NN) problem, we have a dataset D of _N_ vectors in R_<sup>d</sup>_ and a query vector \(\vec{q}\in\mathbb{R}^d\). The goal is to find the subset \(\mathcal{D}_k^*(\vec{q})\subseteq\mathcal{D}\) such that \(|\mathcal{D}_k^*(\vec{q})|=k\), and for any \(\vec{v}\in\mathcal{D}_k^*(\vec{q})\) and any \(\vec{v}'\in\mathcal{D}\backslash\mathcal{D}_k^*(\vec{q})\), it holds that \(dist(\vec{v},\vec{q})\le dist(\vec{v}',\vec{q})\). A straightforward approach is the linear scan, which computes the distance from \(\vec{q}\) to all _N_ vectors and maintains the _k_ smallest distances found so far, typically using a priority queue of size _k_. The computational cost is _O(Nd+Nlogk_), prohibitive for large-scale datasets (large _N_) or high-dimensional data (large _d_).

To address the _O(Nd+Nlogk_) cost, graph-based _k_-NN approaches have been proposed. These methods operate on a graph G=(D,E) over the dataset D, where each vector in R_<sup>d</sup>_ is represented as a vertex, and edges connect pairs of sufficiently "close" vectors. Given a query \(\vec{q}\), the search greedily traverses the graph from an initial node toward nodes closer to \(\vec{q}\). A representative example is the Delaunay graph \[13\]. In the two-dimensional case, each node in the Delaunay graph has an expected degree of _O_(1), and it guarantees that for any query \(\vec{q}\), the exact nearest neighbor can be found in expected _O_(log_N_) time \[32\]. However, moving towards the general case, the average node degree in the Delaunay graph grows exponentially in vector dimension with \(O(N^{\lceil d/2\rceil})\) \[13\], making search impractical.

## 2.3 Approximate _k_-NN and Hierarchical Navigable Small World

Given that existing _k_-NN search algorithms are infeasible for large- scale, high-dimensional data, where both linear scan and ideal graph-based methods are prohibitively expensive, a practical trade- off between accuracy and efficiency is necessary. Consequently, people have proposed the _Approximate k-NN (ANN)_. In ANN, instead of returning the exact nearest set \(\mathcal{D}_k^*(\vec{q})\), the goal is to find an approximate set S that meets a target Recall \(R\in(0,1]\), defined as \(\text{Recall}(\mathcal{S})=|\mathcal{S}\cap\mathcal{D}_k^*(\vec{q})|/k\ge R\). Over the years, various families of ANN methods have been developed, including hashing-based, tree- based, and quantization-based approaches. Among them, Hierarchical Navigable Small World (HNSW) \[32\], achieves state-of-the-art query performance for high-dimensional data \[32\].

The core of HNSW is a multi-layered graph structure G={G<sub>0</sub>,G<sub>1</sub>_,...,_G<sub>_L_-1</sub>}, where each layer \(\mathcal{G}_\ell=(\mathcal{V}_\ell,\mathcal{E}_\ell)\) denotes a graph whose nodes correspond to vectors in the dataset D. The layers form a sequence of nested subsets of D: \(\mathcal{V}_{L-1}\subset\mathcal{V}_{L-2}\subset\cdots\subset\mathcal{V}_1\subset\mathcal{V}_0=\mathcal{D}\). The number of nodes decreases geometrically from bottom to top, resulting in _L=O_(log_N_) layers. The edges are constructed from the nodes’ underlying vector representations, and each \(\mathcal{G}_\ell\) serves as an out-degree bound _M=O_(1) approximation of a Delaunay graph. This hierarchical graph G is an efficient index for the vector database D. Its design enables a two-phase search strategy: upper, sparser layers support coarse-grained navigation, ensuring high search efficiency, while lower, denser layers provide fine-grained refinement, ensuring high search accuracy.

For query \(\vec{q}\in\mathbb{R}^d\), HNSW starts at a random entry point in the top layer G<sub>_L_-1</sub>. Each layer search locates the locally closest node to \(\vec{q}\), which becomes the entry point for the next lower layer. After searching the base layer G<sub>0</sub>, the algorithm returns the _k_ nearest neighbors of \(\vec{q}\) from all visited nodes. To implement this idea, at each layer the search maintains three data structures: a candidate set _C_, which stores potential nodes for further exploration; a result set _W_, which stores the closest nodes found so far, where |_W_|=_ef_ with _ef_=1 for non-base layers and _ef=O(k_) for the base layer; and a visited set _V_ , which records all visited nodes to prevent revisits.

All these data structures are initialized with the entry point _ep_, and the search then proceeds iteratively. At each iteration, we extract the nearest candidate _c_ from _C_, explore each unvisited neighbor _e_ of _c_, and add them to _V_ . If _e_ is closer to \(\vec{q}\) than the farthest node in _W_, it is inserted into both _C_ and _W_, and _W_ is kept at size at most _ef_. The search terminates when no candidate in _C_ is closer to \(\vec{q}\) than the farthest node in _W_, or when _C_ becomes empty. Algorithm 1 gives the detailed procedure.

We abstract HNSW into three key components: the **search logic flow**, the **data structures**, and the **graph and vector access**. The logic flow specifies how the search proceeds within each layer. In each step, it moves to the nearest candidate node and then explores all its neighbors. The search stops when no candidate is closer to the query than the current results. The data structures support this process. At each layer, the algorithm maintains three sets: a candidate set _C_, a result set _W_, and a visited set _V_ . Finally, the logic flow interacts with the underlying graph index and vector database. For each candidate _c_, the search first accesses the graph index to<tbc>

