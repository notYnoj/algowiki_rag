## 4.1 Graph decomposition of Q(_n_)

The graph decomposition of Q(_n_) is obtained from the vertex partition \(V(\mathcal{Q}(n))=V_1\cup V_2\) and an edge partition \(E(\mathcal{Q}(n))=E_1\cup E_2\cup E_3\), where the \(n\times n\) chessboard is divided into two right triangles, corresponding to the subgraphs _G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>) and _G_<sub>2</sub>=(_V_<sub>2</sub>_,E_<sub>2</sub>), where the first one includes the vertices corresponding to the main diagonal of the chessboard as hypotenuse. The edges of _E_<sub>1</sub> and _E_<sub>2</sub> are chosen such that _G_<sub>1</sub> is a triangular graph T(_n_) and _G_<sub>2</sub> is a triangular graph T(_n_-1), both are integral regular graphs. Then we may consider a graph _G_<sub>1,2</sub>=_G_<sub>1</sub>+_G_<sub>2</sub>, that is, a graph with two connected components _G_<sub>1</sub> and _G_<sub>2</sub>. The graph _G_<sub>3</sub>=(_V_<sub>3</sub>_,E_<sub>3</sub>) is such that _V_<sub>3</sub>=_V_(Q(_n_)) and _E_<sub>3</sub>=_E_(Q(_n_))∖_E(G_<sub>1,2</sub>).

**Theorem 4.2.** _For_ \(n\ge 4\)_, we may consider the following splitting of the adjacency matrix of the n-Queens’ graph,_ Q(_n),_

\(A(\mathcal{Q}(n))=A(G_{1,2})+A(G_3)\) (34)

\(=A(G_{1,2})+\left(A(G_3^1)+\underbrace{\left(A(G_{3,H}^2)+A(G_{3,V}^2)\right)}_{A(G_3^2)}\right)\right),\) (35)

_where each graph is obtained from the_ \(n\times n\) _chessboard as follows:_

1. _Consider the vertex partition_ \(V(\mathcal{Q}(n))=V_1\cup V_2\)_, where V_<sub>1</sub> _corresponds to the_ \(\frac{n(n+1)}{2}\) _vertices of the right triangle which includes the main diagonal as hypotenuse and V_<sub>2</sub> _corresponds to the remaining_ \(\frac{(n-1)n}{2}\) _vertices which defines the other right triangle. Choosing the edge subsets E_<sub>1</sub> _and E_<sub>2</sub> _such that G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>) _and G_<sub>2</sub>=(_V_<sub>2</sub>_,E_<sub>2</sub>) _are the triangular graphs_ T(_n_) _and_ T(_n_-1)_, respectively, we may conclude that the graph G_<sub>1,2</sub>=_G_<sub>1</sub>+_G_<sub>2</sub> _has two components_ \(G_1\cong\mathcal{T}(n)\) _and_ \(G_2\cong\mathcal{T}(n-1)\).<tbc>

_2._ _The graph G_<sub>3</sub>=(_V_<sub>3</sub>_,E_<sub>3</sub>) _is such that V_<sub>3</sub>=_V_(Q(_n_))_, E_<sub>3</sub>=_E_(Q(_n_))∖_E(G_<sub>1,2</sub>) _and_ \(A(G_3)=A(G_3^1)+A(G_3^2)\).<tbc>

(_a)_ _The connected components of the graph_ \(G_3^1\) _are the cliques formed by the edges of the diagonals parallel to the second diagonal of the_ \(n\times n\) _chessboard, that is, K_<sub>1</sub>_, K_<sub>2</sub>_, ..., K_<sub>_n_-1</sub>_, K<sub>n</sub>, K_<sub>_n_-1</sub>_, ..., K_<sub>2</sub>_, K_<sub>1</sub>.<tbc>

_(b)_ _Considering the vertices of G_<sub>1</sub> _as blue vertices and the vertices of G_<sub>2</sub> _as red vertices and partitioning the remaining edges of E_<sub>3</sub>_, that is,_ \(E(G_3^2)=E_3\unknown E(G_3^1)\)_, into the subsets of horizontal and vertical edges between blue and red vertices, we obtain the graphs_ \(G_{3,H}^2\) _and_ \(G_{3,V}^2\) _such that_ \(A(G_3^2)=A(G_{3,H}^2)+A(G_{3,V}^2)\)_. The components of_ \(G_{3,X}^2\)_, with_ \(X\in\{H,V\}\)_, are the complete bipartite graphs K_<sub>1_,n_-1</sub>_, K_<sub>2_,n_-2</sub>_, ..., K_<sub>_n_-1,1</sub>_. Additionally,_ \(G_{3,X}^2\) _also includes K_<sub>_n,_0</sub> _which are just n isolated vertices._

_Proof._ We prove this theorem by induction on _n_, taking into account that, according to Example 4.3 below, the matrix splitting (34)-(35) associated to the graph decomposition described in items (1) and (2) is true for _n_=4. Let us assume that the adjacency matrix of Q(_n_) can be split as in (34)-(35), for some \(n\ge 4\).

