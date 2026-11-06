The \((n+1)\times(n+1)\) chessboard associated to Q(_n_+1) is obtained from the \(n\times n\) chessboard associated to Q(_n_) adding a row of _n_ squares at the bottom, a column of _n_ squares at the right and a square to the right bottom position of its main diagonal. Coloring the vertices corresponding to the new bottom row with _n_+1 squares by the colour blue and colouring the vertices associated to the remaining new _n_ squares (column on the right) by the colour red, we obtain the graph _G_<sub>1,2</sub>=_G_<sub>1</sub>+_G_<sub>2</sub> with two components \(G_1\cong\mathcal{T}(n+1)\) and \(G_2\cong\mathcal{T}(n)\) as in item-1.

The graph decomposition described in item (2) is easily extended from Q(_n_) to Q(_n_+1).

**Example 4.3.** _Let us consider the graph_ Q(4) _associated to the chessboard presented in  2_

_Considering the vertex partition and edge partition referred in Theorem 4.2, it follows that_ \(G_1\cong\mathcal{T}(4)\) _and_ \(G_2\cong\mathcal{T}(3)\)_. From Theorem 3.6 it follows that the largest eigenvalues of_ T(4) _(and_ T(3)_) is simple and equal to_ \(2\times 4-2=6\) _(is simple and equal to_ \(2\times 3-2=4\)_, respectively). Furthermore, from Theorem 3.7, we know that the least eigenvalue of_ T(4) _has multiplicity_ \(\frac{(4-3)(4-2))}{2}=1\) _and is equal to_ -3_. Additionally, as it easy to conclude,_ \(\sigma(\mathcal{T}(3))=\{4,0^{[3]},-2^{[2]}\}\)_. On the other hand,_ \(\sigma(\mathcal{T}(4))=\{6,1^{[3]},0^{[2]},-2^{[3]},-3\}\)_. Therefore,_

\(\sigma(G_{1,2})=\{6,1^{[3]},0^{[2]},-2^{[3]},-3\}\bigcup_{withrepetitions}\{4,0^{[3]},-2^{[2]}\}\)<br>
\(=\{6,4,1^{[3]},0^{[5]},-2^{[5]},-3\}.\)

_Analyzing the  2 and the possible edge partitions we conclude following._

1. _The connected components of the graph_ \(G_3^1\) _are the cliques C_<sub>1</sub>={_a}, C_<sub>2</sub>={_e,b}, C_<sub>3</sub>={_i,f,c}, C_<sub>4</sub>={_m,j,g,d}, C_<sub>5</sub>={_n,k,h}, C_<sub>6</sub>={_o,l_} _and C_<sub>7</sub>={_p}, formed by the edges of the diagonals parallel to the second diagonal in  2. So, the components of_ \(G_3^1\) _are the subgraphs K_<sub>1</sub>=_G_<sub>3</sub>\[_C_<sub>1</sub>\]_, K_<sub>2</sub>=_G_<sub>3</sub>\[_C_<sub>2</sub>\]_, K_<sub>3</sub>=_G_<sub>3</sub>\[_C_<sub>3</sub>\]_, K_<sub>4</sub>=_G_<sub>3</sub>\[_C_<sub>4</sub>\]_, K_<sub>3</sub>=_G_<sub>3</sub>\[_C_<sub>5</sub>\]_, K_<sub>2</sub>=_G_<sub>3</sub>\[_C_<sub>6</sub>\] _and K_<sub>1</sub>=_G_<sub>3</sub>\[_C_<sub>7</sub>\]_, where the adjacency matrix of each clique appears as a diagonal square submatrix of_ \(A(G_3^1)\)_. Therefore,_<tbc>

<tbc>\(\sigma(G_3^1)=\{3,2^{[2]},1^{[2]},0^{[2]},-1^{[9]}\}.\) \(\text{(36)}\)

_2._ _The remaining edges can be partitioned into the horizontal (H) and vertical (V) edges (relatively to -2), defining two graphs,_ \(G_{3,H}^2\) _and_ \(G_{3,V}^2\)_, whose componentes are the following complete bipartite subgraphs:_<tbc>

\begin{tabular}{ccccc}
a & b & c & d & \\
e & f & g & h & \\
i & j & k & l & \\
m & n & o & p & \\
\end{tabular}

2: \(4\times 4\) chessboard divided into two triangles

