candidates and do not address layout generation, the most computationally demanding stage.

A distinctive characteristic of quantum layout selection is that the pattern graphs (circuits) are relatively large, typically on the order of dozens to around one hundred vertices in state- of-the-art workloads. This contrasts with many traditional subgraph matching workloads that emphasize small pattern graphs (with 10 or fewer vertices) within very large data graphs. While much of the existing methods focus on scaling to larger data graphs, scaling pattern graph size introduces its own challenges, as larger patterns induce substantial search spaces and many valid embeddings. As quantum devices continue to scale, even larger interaction patterns are expected to become relevant, motivating algorithms capable of efficiently handling larger pattern graphs while exploiting the structured connectivity commonly observed in quantum hardware topologies.

Moreover, data graphs representing the physical qubit connectivity in quantum hardware typically remain static over time, meaning a significant portion of the pipeline can be precomputed and cached. This use-case-specific feature enables the reuse of intermediate results across multiple compilation runs, delivering further speedups in practice when precomputation costs are excluded.

## III. DATA-CENTRIC SUBGRAPH ISOMORPHISM ALGORITHM

In this section, we introduce a data-science-inspired method for the subgraph isomorphism problem. Instead of exhaustively matching full patterns in the data graph via node-by-node traversal, we adopt a modular strategy based on motif decomposition, which we call \(\Delta\)_-Motif_, reflecting the decomposition of pattern graphs into smaller components. In Section IV, we draw an analogy between \(\Delta\)_-Motif_ and the \(\Delta\)_-Stepping_ algorithm for single-source shortest path (SSSP) problems \[59\], which shares a similar trade-off between additional work and improved parallelism. The details of this analogy become clearer after introducing the algorithm and its performance characteristics.

### A. Preliminaries

**Subgraph Isomorphism:** We formally define a graph as a tuple _G_=(_V,E_), where _V_ is a finite set of vertices and \(E\subseteq V\times V\) is the set of undirected edges. Let the data graph be denoted as _G<sub>d</sub>_=(_V<sub>d</sub>,E<sub>d</sub>_) and the pattern graph as _G<sub>p</sub>_=(_V<sub>p</sub>,E<sub>p</sub>_). We say that _G<sub>p</sub>_ is isomorphic to a subgraph of _G<sub>d</sub>_ if there exists an injective mapping _f:V<sub>p</sub>-V<sub>d</sub>_ such that \((u,v)\in E_p\Longleftrightarrow(f(u),f(v))\in E_d\). The subgraph isomorphism enumeration problem is to find all such mappings _f_ from _G<sub>p</sub>_ into vertex-induced subgraphs of _G<sub>d</sub>_ that preserve adjacency as defined above. Throughout this work, we assume all graphs are unlabeled, undirected and connected.

**Motifs:** Motifs are size-limited, well-defined subgraphs that capture local structural patterns within a graph. Common examples include linear paths (e.g., _a-b-c_), triangles (_a-b-c-a_), and other frequent occurring configurations such as squares, stars, or short cycles. In this work, we pre-define a<tbc>

<tbc>set of motifs {_M_<sub>0</sub>_,M_<sub>1</sub>_,...,M<sub>k</sub>_}, where each _M<sub>i</sub>_=(_V<sub>i</sub>,E<sub>i</sub>_) is a small, connected subgraph of the data graph. Fig. 1 illustrates the lattice structures used as data graphs in our benchmarks, together with the representative motifs derived from them. We have attempted to keep the naming of the motifs fairly simple: _M<sub>i</sub>_ denotes a path of _i_ vertices, while additional suffixes (e.g., "-O" for cycles or "-1" for one branch) indicate common variations.

These motifs serve as the building blocks for decomposing both data and pattern graphs into sequences of motif instances, which can then be incrementally joined to reconstruct larger subgraph matches. As we show in Section VI-B, the choice and ordering of motif set directly influence performance. Selecting motifs requires balancing expressiveness with computational cost, and is informed by the structural characteristics of both the data and pattern graphs.

We denote the set of all embeddings of a motif _M<sub>i</sub>_ in the data graph by _Res(M<sub>i</sub>_). Each element in _Res(M<sub>i</sub>_) is a tuple of vertex indices that together form a subgraph isomorphic to _M<sub>i</sub>_. These embeddings are stored in tabular form, where each row corresponds to a single match and each column to a vertex position in the motif template. This tabular format allows subsequent processing, such as joining embeddings and enforcing constraints, to be performed using scalable dataframe operations.

### B. The \(\Delta\)_-Motif Approach_

To motivate our approach, we begin with a simple example. Consider a data graph _G<sub>d</sub>_ with 7 nodes, shown in Fig. 2(a), and a pattern graph _G<sub>p</sub>_ defined as a 6-node undirected cycle shown in Fig. 2(b). Rather than trying to match the entire cycle directly in the _G<sub>d</sub>_, we firstly decompose _G<sub>p</sub>_ into a set of smaller, overlapping motifs, M={_M_<sub>0</sub>_,...,M<sub>i</sub>_}. Each motif captures a localized structure that can be matched independently. For<tbc>

(a)
(b)
(c)
M2
M3
M6
M3-0
M4-1
M4-0
M6-20
M12-0
M18-0-6

Fig. 1. (a) Heavy-hex and (b) 2D square grid lattice structures used as data graphs in our benchmark tests. These lattices represent common qubit connectivity topologies in quantum hardware and serve as the input data graphs for quantum layout selection. The corresponding set of representative motifs is shown in (c).

