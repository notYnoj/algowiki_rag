a value of \(\mu\) falling into a wide range. Then, our final proofs pick an appropriate value of \(\mu\) that falls into that range while having small bit-complexity.

## 2 Preliminaries

We will now define the main convex relaxation we will work with. Let \(\xi:=\frac{9}{4}c^2\), let \(\mathcal{S}:=\{S\subseteq V:|S|\ge\left(1-\frac{c}{4}\right)n\}\), and let P be the set of sequences \(p=(p_0,\dots,p_{\ell(p)})\) of distinct nodes in _G_. We use the notation \(p=(p_0,\dots,p_{\ell(p)})\) for the sequence of vertices along a path \(p\in\mathcal{P}\). We use nonnegative scalar deletion variables _x<sub>z</sub>_ for all elements \(z\in V\cup E\); in particular, _x<sub>ij</sub>_ is the variable for edge _ij_, distinct from the Gram-matrix entry _X<sub>ij</sub>_. (We write _ij_ for an undirected edge with endpoints _i,j_.) We consider the following relaxation of the _c_-balanced element cut problem:

\(min\sum_{z\in V\cup E}w(z)x_z\) (1a)

\(x_i+x_j+x_{ij}\ge\|v_i-v_j\|^2x_i+x_j+x_{ij}-L_{ij}\bullet X\ge 0\forall ij\in E\) (1b)

\(\|v_i\|^2=1X_{ii}=1\forall i\in V\) (1c)

\(\sum_{j=1}^{\ell(p)}\|v_{p_j}-v_{p_{j-1}}\|^2\ge\|v_{p_{\ell(p)}}-v_{p_0}\|^2T_p\bullet X\ge 0\forall p\in\mathcal{P}\) (1d)

\(\sum_{i,j\in S:i<j}\|v_i-v_j\|^2\ge\xi n^2K_S\bullet X\ge\xi n^2\forall S\in\mathcal{S}\) (1e)

\(x\ge 0X\unknown 0,x\ge 0\) (1f)

Variables for elements of infinite cost are fixed to zero and their objective terms are omitted. In particular, at the optimum we have _x<sub>i</sub>_=0, \(x_{ij}=\|v_i-v_j\|^2\) in the case of edge separators and _x<sub>ij</sub>_=0 in the case of vertex separators. The left and right sides here both denote the same optimization problem. The difference is notational. The matrix _X_ is defined as _X_:=_V<sup>T</sup>V_ , where _V_ is the \(n\times n\) matrix with columns _v_<sub>1</sub>_,...,v<sub>n</sub>_. We have _L<sub>ij</sub>_=L(_G_<sub>(_i,j_)</sub>) and _T<sub>p</sub>_=L(_G<sub>p</sub>_)-L(\(G_{(p_0,p_{\ell(p)})}\)) where \(\mathcal{L}(\cdot)\) is the Laplacian of the corresponding graph (the diagonal degree matrix minus the adjacency matrix) and _G<sub>q</sub>_ for a path _q_ is the undirected unweighted graph containing all edges of _q_. Finally, we define _K<sub>S</sub>(i,i_)=|_S_|-1 for \(i\in S\), _K<sub>S</sub>(i,j_)=-1 for distinct \(i,j\in S\), and _K<sub>S</sub>(i,j_)=0 in all other cases.

**Proposition 6.** _The optimal value of problem (1) divided by 4 is a lower bound on the minimum c_-Balanced Element Cut _problem._

_Proof._ Let (_A,B),C_ be an optimal _c_-balanced element cut, so \(max\{|A|,|B|\}\le(1-c)n\). We need to construct a feasible solution of problem (1) of value at most 4(_w(C_)+_w(E(A,B_))). In the construction below, the last _n_-1 coordinates of vectors _v<sub>i</sub>_ will be set to 0; we can thus assume for brevity of notation that \(v_i\in\mathbb{R}\) rather than \(v_i\in\mathbb{R}^n\).

Let us choose a partition \((\hat{A},\hat{B})\) of _V_ with \(A\subseteq\hat{A}\), \(B\subseteq\hat{B}\) which is the "most balanced", i.e. it minimizes the absolute value of \(|\hat{A}|-|\hat{B}|\). In particular, if \(max\{|A|,|B|\}\le n/2\) then \(min\{|\hat{A}|,|\hat{B}|\}\ge\lfloor n/2\rfloor\), otherwise either \((\hat{A},\hat{B})=(A,V-A)\) (if |_A|\>n/_2) or \((\hat{A},\hat{B})=(V-B,B)\) (if |_B|\>n/_2). In all three cases we have \(|\hat{A}|\ge cn\) and \(|\hat{B}|\ge cn\), since _c\<_1/2. Set \(x_i=\left\{\begin{array}{ c c }
0 & \text{if}i\in A\cup B \\
4 & \text{if}i\in C
\end{array}\right.\) and \(v_i=\left\{\begin{array}{ c c }
-1 & \text{if}i\in\hat{A} \\
+1 & \text{if}i\in\hat{B}
\end{array}\right.\). Set _x<sub>ij</sub>_=4 for \(ij\in E(A,B)\) and _x<sub>ij</sub>_=0 otherwise. Checking conditions (1b), (1c), (1d), (1f) is straightforward. (For each edge _ij_ with \(v_i\neq v_j\), either an endpoint lies in _C_, or \(ij\in E(A,B)\), so \(x_i+x_j+x_{ij}\ge 4\).) Let us show (1e). Consider a set<tbc>

