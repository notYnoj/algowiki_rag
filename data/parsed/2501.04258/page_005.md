<tbc>with vertices _V_<sup>∗</sup>={_v_<sub>1</sub>_,v_<sub>2</sub>_,...,v<sub>n</sub>_} and edges _E_<sup>∗</sup>={_e_<sub>1</sub>_,e_<sub>2</sub>_,...,e<sub>m</sub>_}. Here _n_ is the number of vertices (or nodes), and _m_ is the number of edges. The adjacency matrix of dual graph _G_<sup>∗</sup> is defined as:

\(A=\left\{\begin{array}{ c c }
2, & \text{if}i=j\text{and}v_i\text{has a self-loop} \\
0, & \text{if}i=j\text{and}v_i\text{does not have a self-loop} \\
N_{ij}, & \text{if}i\neq j,
\end{array}\right.\) (1)

where _N<sub>ij</sub>_ represents the number of edges between _v<sub>i</sub>_ and _v<sub>j</sub>_. Since multiple edges between two vertices are allowed. Hence, the minimal value of _N<sub>ij</sub>_ is 0, and the maximum is 3. In Figure 1, stem 1 has a self-loop; therefore, the entry _A_<sub>11</sub>=2. Additionally, there are two edges between stem 1 and stem 2, so the entry _A_<sub>12</sub>=2.

To uniquely identify each graph topology, we assign a unique graph ID _a-k_, where _a_ denotes the number of vertices and _k_ indicates the descending rank based on the Fiedler number of the graph Laplacian within all graph topologies with _a_ vertices. For example, graph ID 4.1 refers to the graph topology with 4 vertices that has the smallest Fiedler number among all 4 vertices graph topologies.

1 lists the numbers of all possible 2D graphs and all graphs corresponding to existing RNA molecules in the Prior Existing and Current Existing. Notably, only a small portion of these graph topologies match known RNA structures, and the remaining motifs are called "hypothetical". This suggests that many graph<tbc>

\begin{tabular}{cccc}
Vertex & Possible Graphs & Exist Graphs in 2021 Dataset & Existing in 2022 Dataset \\
2 & 3 & 3 & 3 \\
3 & 8 & 7 & 8 \\
4 & 29 & 17 & 22 \\
5 & 110 & 20 & 29 \\
6 & 508 & 22 & 37 \\
7 & 2,551 & 21 & 34 \\
8 & 14,670 & 14 & 20 \\
9 & 92,788 & 17 & 28 \\
Total & 110,667 & 121 & 181 \\
\end{tabular}

PDB ID: 1A9L
A
G
Dual Graph ID: 3_4
G
A
C
G
Stem 1
U
A
G
A
G
C
A
C
G
A
C
G
Stem 2
C
G
A
A
C
G
A
A
U
G
U
A
G
C
Stem 3
U
A
2
2
0
G
C
Adjacency matrix:
2
0
2
0
2
0
C
C

Figure 1: The secondary structural of 1A9L with its corresponding dual graph representations under "RNA-As-Graphs" (RAG) framework. The adjacency matrix describes the connectivity between nodes and edges.

1: Enumeration of all possible non-isomorphic graph topologies and corresponding RNA molecules in Prior Existing and Current Existing. The number of all possible graphs, graphs with a match to existing RNA molecules in the Prior Existing and Current Existing corresponding to a specific vertex number is listed.

