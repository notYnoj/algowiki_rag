sive parallelism and memory bandwidth required by APSP.

To break through the fundamental memory and power walls that create critical performance bottlenecks in exact APSP computation, we introduce RAPID-Graph, a novel software- hardware co-designed PIM system. Our approach overcomes the communication limits of multi-GPU clusters and the dense- workload constraints of prior PIM architectures. Our core contributions are as follows:

\(\bullet\) Recursive in-memory APSP dataflow. We design an algorithm that recursively decomposes the graph into subproblems sized for a single PIM tile, enabling massively parallel FW execution entirely in PCM arrays and eliminating off-chip data movement.<tbc>

\(\bullet\) Heterogeneous 2.5D PIM architecture. We build a tailored architecture for this dataflow, integrating PCM compute dies with a logic die via UCIe, supported by an on-package HBM3 for hot submatrices and external FeNAND for bulk storage, forming a balanced memory hierarchy.<tbc>

\(\bullet\) SOTA performance and efficiency. RAPID-Graph delivers up to 1061\(\times\) speedup and 7208\(\times\) energy efficiency over CPU. On the OGBN-Products dataset (2.5M nodes), it outperforms GPU clusters by 5.8\(\times\) in runtime and 1186\(\times\) in energy efficiency.

## II. BACKGROUND

### A. Graphs

A graph _G_=(_V,E,w_) can be stored as an adjacency matrix or CSR. Computation is most convenient on its dense adjacency matrix _A_, defined by _A<sub>ij</sub>=w(i,j_) for \((i,j)\in E\) and \(+\infty\) otherwise, enabling regular dataflow for FW and MP kernels. For storage, we adopt CSR, which records only the nonzero weights together with row boundaries, reducing space from _n_<sup>2</sup> to |_E_|. Fig. 1 illustrates an 8-vertex toy graph in three views: (a) the original topology, (b) the dense matrix with finite weights marked, and (c) the compressed CSR `rowptr,col,val`, demonstrating space savings when \(|E|\checkmark n^2\).

### B. APSP Algorithms

#### 1) Classic FW DP:

The FW algorithm \[6\] solves the APSP problem on a weighted graph _G_=(_V,E,w_) via an in-place dynamic program over an \(n\times n\) distance matrix _D_. _D_\[_i_\]\[_j_\] is set to the weight of edge (_i,j_), or \(\infty\) if no edge exists. The algorithm updates all entries by checking whether paths through vertex _k_ yield shorter distances by:

\(D[i][j]=min\left(D[i][j],D[i][k]+D[k][j]\right),k\in[1,n].\)

**Algorithm 1** Partition APSP Pseudocode

1: Partition _G_ into _k_ components _C_<sub>1</sub>_,...,C<sub>k</sub>_ via METIS \[24\]<br>
2: for i=1 to k do \(\triangleright\) Step 1<br>
3: FW(_C<sub>i</sub>_)<br>
4: \(G_B\leftarrow\) EXTRACTBOUNDARYGRAPH(_G_) \(\triangleright\) Step 2<br>
5: FW(_G<sub>B</sub>_)<br>
6: for i=1 to k do \(\triangleright\) Step 3 with injected d<sub>B</sub><br>
7: FW(_C<sub>i</sub>_)<br>
8: for i=1 to k do \(\triangleright\) Step 4<br>
9: for j=1 to k do<br>
10: MINPLUSMERGE(_C<sub>i</sub>,C<sub>j</sub>_)<br>
11: return global distance matrix

After _n_ iterations, _D_ contains the exact shortest path lengths between all vertex pairs. The algorithm runs in _O(n_<sup>3</sup>) time and _O(n_<sup>2</sup>) space, following a computation pattern equal to a dense outer product of row _i_ and column _k_ against column _j_.

#### 2) Partitioned APSP:

Our recursive partition APSP extends the four-stage scheme by \[10\], which reshapes FW into tile- local semiring operations, aligning with PIM’s in-place parallelism. The algorithm is illustrated in Fig.2 and summarized in Algorithm 1. Graph preprocessing runs on host CPU, where a weighted graph _G_ is partitioned into components _C_<sub>1</sub>_,...,C<sub>k</sub>_ and their boundary set _B_ via a _k_-way METIS \[24\]. Within each component, a boundary vertex has an edge connecting to another component, while an internal vertex only has edges to vertices within its own component. For computational efficiency, boundary vertices are reordered before internal vertices.

**Step 1: Local APSP.** Each component independently runs FW to fill its intra-component distance matrix _d_<sub>intra</sub>; all passes execute in parallel and scale linearly.

**Step 2: Boundary-graph APSP.** All boundary vertices form a reduced graph _G<sub>B</sub>_, with edges comprising: (i) cross- component edges from _G_, and (ii) virtual edges within components weighted by _d_<sub>intra</sub>. A single FW run computes the boundary distance matrix _d<sub>B</sub>_. As this step involves dense _O_(|_B_|<sup>3</sup>) work, it becomes the primary bottleneck when |_B_| nears hardware limits. Section III-A addresses this bottleneck through recursive partitioning.

**Step 3: Boundary injection.** Each component copies the relevant rows and columns of _d<sub>B</sub>_ into its local matrix and reruns FW once, propagating inter-component shortcuts.

**Step 4: Cross-component merge.** An MP merge combines (i) source to boundary, (ii) boundary to boundary, and (iii) boundary to destination paths, producing the final cross- component distances _d_<sub>cross</sub> and thus completing global APSP.

