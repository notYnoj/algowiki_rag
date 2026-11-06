<tbc>runtime, though motif selection, ordering, and decomposition strategy remain promising avenues for future optimization.

### D. From a Single Motif to Computing Embeddings of Motif Sequences

In the above, we decomposed the pattern graphs into a sequence of motifs. In this subsection, we show how we can extract the embeddings of those motifs from the data graph and how we connect the results of multiple motif searches. As a simple case, searching for motif _M_<sub>2</sub> is equivalent to returning all edges of _G<sub>d</sub>_ excluding self-loops _a-a_. Formally, _Res(M_<sub>2</sub>)=_E<sub>d</sub>_\\_E<sub>self</sub>_, where _E<sub>self</sub>_ is the set of self-loops.

To compute embeddings of larger motifs, we apply a sequence of _join_-and-_filter_ operations using an algorithm described in Algorithm 1. For example, consider the motif _M_<sub>3</sub>, defined as a simple path: _a-b-c_ where \(a\neq b\neq c\). Its embeddings, denoted _Res(M_<sub>3</sub>), can be computed by inner- joining two instances of _Res(M_<sub>2</sub>) on the shared node _b_. This can be written as: \(Res(M_3)=\text{L}\bowtie_{\text{L}[1]==\text{R}[0]}\text{R}\), where both L and R refer to the same table _Res(M_<sub>2</sub>). The _join_ captures all three-node paths, and is followed by a filtering step to eliminate invalid embeddings. For example, since both edges _a-b_ and _b-a_ exist in the undirected data graph, the resulting table may incorrectly include the cyclic pattern _a-b-a_. The _filter_ removes such entries and ensures that all three vertices in each triplet are distinct. This entire process can be carried out in a single call to our motif solver. The resulting set _Res(M_<sub>3</sub>) is stored in a dataframe format.

Similarly, embeddings of larger motifs can be computed recursively. For example, _Res(M_<sub>4</sub>) can be built by joining _Res(M_<sub>3</sub>) with _Res(M_<sub>2</sub>) on the last and first vertex: \(Res(M_4)=\text{L}\bowtie_{\text{L}[2]==\text{R}[0]}\text{R}\), where L=_Res(M_<sub>3</sub>) and R=_Res(M_<sub>2</sub>), followed by filtering. This pattern generalizes to arbitrary motif sizes (e.g. _Res(M_<sub>5</sub>) from (_M_<sub>3</sub>_,M_<sub>3</sub>) or (_M_<sub>4</sub>_,M_<sub>2</sub>)), as shown in _Algorithm 2_.

### E. Performance Increase from Larger Motifs

The use of larger motifs for decomposing the pattern graph has several benefits: 1) fewer motifs are needed for the decomposition, hence fewer _join_-and-_filter_ , which can be substantially fewer than the branching levels explored in a VF2 tree search, 2) larger motifs can increase parallelism in the data pre-processing phase, and 3) larger motifs enable early-stage pruning of invalid solutions, which also takes place during the pre-processing phase.

**Algorithm 2** Build Motif Database Recursively

function BUILDDATABASE(_G<sub>d</sub>,_M)<br>
   \(DB\leftarrow\{(u,v):(u,v)\in E_d\}\triangleright\text{DB is}Res(M_2)\)<br>
   for all \(M_i\in\mathcal{M}\) do<br>
   \(Res(M_i)\leftarrow\text{DELTA-MOTIF}(M_i,DB)\)<br>
   \(DB\leftarrow DB\cup Res(M_i)\)<br>
   end for<br>
   return DB<br>
end function

## IV. ANALOG TO TREE SEARCH AND PRUNE

Having presented our join-based algorithm for subgraph isomorphism, we now draw a parallel to traditional tree- search-and-prune approaches. Although not obvious at first, these algorithms share many features while trading off others.

### A. Parallelism Vs. Storage

Most tree-search-and-prune solutions rely on recursion. Some parallelism is possible--typically by enumerating an ordered set of vertices for the first few levels of the tree (e.g., one to three) and parallelizing across them, i.e., an initial BFS to generate starting conditions followed by DFS to find the remaining pattern. Extending parallelism beyond these levels raises several challenges: workload imbalance, a larger memory footprint for storing starting points (similar to generating _Res(M_<sub>3</sub>)), and, most critically, synchronization overhead as threads coordinate access to shared data structures. These limits on achievable parallelism also explain why some algorithms handle only patterns with fewer than 10 vertices and edges.

In contrast, most phases of \(\Delta\)-_Motif_ are inherently parallel: each row in our dataframe is an independent candidate, and the same operations apply uniformly across all rows, letting thousands of candidate mappings be processed simultaneously, similar to BFS. This parallelism comes at a cost: our new algorithm has an increased memory footprint. The increased memory requirements stem from two main factors: 1) holding intermediate data generated during join operations before key constraints are applied to prune invalid matches and 2) storing complete tables of intermediate solutions after each join-and- filter iteration.

### B. M<sub>2</sub> and Its Analogy to Parallel Tree-Search

Consider the case where the pattern graph is decomposed only with the M<sub>2</sub> motif. In this setup, the number of steps in \(\Delta\)-_Motif_ matches the branching levels explored in a VF2 tree search: the first M<sub>2</sub> expansion enumerates all edges, the next expands them into all possible 3-hop paths, then into 4-hop paths, and so on.The key difference is that VF2 moves forward one branch at a time, while \(\Delta\)-_Motif_ processes all branches at a given depth in parallel (similar to a BFS traversal) through joins and filters that run simultaneously across all candidates.

However, the M<sub>2</sub>-only case shares a limitation with VF2: the same path may be traversed multiple times from different starting points, incurring redundant work. In contrast, using larger motif choices allows \(\Delta\)-_Motif_ to operate on larger structural units, avoiding repeated traversal; invalid candidates are discarded during filtering rather than through recursive backtracking.

### C. \(\Delta\)-_Motif_ and \(\Delta\)-_Stepping_

We now return to the analogy with the \(\Delta\)-_Stepping_ algorithm for solving the SSSP problem. Although SSSP and subgraph isomorphism address different problems, both approaches expose additional parallelism by allowing extra work during execution. In \(\Delta\)-_Stepping_, the parameter \(\Delta\) trades computational<tbc>

