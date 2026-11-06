**Theorem 3.3** _With reference to Definition 2.1, if_ \(f\in L^1([-\pi,\pi]^d,\mathbb{C}^{r\times r})\)_, then_<tbc>

\(\{T_\mathbf{n}(f)\}_\mathbf{n}\sim_\sigma f.\)

<tbc>_If, moreover, f is Hermitian a.e., then_

\(\{T_\mathbf{n}(f)\}_\mathbf{n}\sim_\lambda f.\)

_Here the singular values and the eigenvalues of the matrix-valued symbol_ \(f(\unknown)\) _play the role of the values of the scalar symbol._

## 3.2 Circulant matrices

Given \(\mathbf{n}\in\mathbb{N}^d\) and \(r\in\mathbb{N}\), a matrix of the form

\(C_\mathbf{n}:=[A_{(\mathbf{i}-\mathbf{j})\mathrm{mod}\mathbf{n}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r},\)

with blocks \(A_\mathbf{k}\in\mathbb{C}^{r\times r}\), \(\mathbf{k}\in\{\mathbf{0},\dots,\mathbf{n}-\mathbf{1}\}\), where the block in position (**_i_**_,**j**_) depends only on the difference (**_i_**-**_j_**)mod**_n_**, is called a _multi-level block_ or _d-level r-block circulant matrix_. In particular, since the (**_i_**_,**j**_)-th block depends only on **_i_**-**_j_**, circulant matrices can be regarded as a special subclass of Toeplitz matrices.

When _d_=1 and **_n_**=_n_, this reduces to a classic _r_-block circulant matrix, where each block column is a one-position downward shift of the previous one:

\(C_n=\big[A_{(i-j)\mathrm{mod}n}\big]_{i,j=1}^n=\left[\begin{array}{ c c c c c c c c c }
A_0 & A_{n-1} & A_{n-2} & \cdots & \cdots & A_1 \\
A_1 & A_0 & A_{n-1} & A_{n-2} &  & \vdots \\
A_2 & A_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & A_2 & \ddots & \ddots & \ddots & A_{n-2} \\
\vdots &  & \ddots & \ddots & \ddots & A_{n-1} \\
A_{n-1} & \cdots & \cdots & A_2 & A_1 & A_0
\end{array}\right]\in\mathbb{C}^{nr\times nr}.\)

_C<sub>n</sub>_ is entirely determined by the _n_ blocks in its first block column, \(\{A_k\}_{k=0}^{n-1}\). Similarly, each block row is a one-element rightward shift of the previous block row, so that the matrix is fully specified by its first block row.

For _d_=2 and **_n_**=(_n_<sub>1</sub>_,n_<sub>2</sub>), we obtain a 2-level _r_-block circulant matrix:

\(C_\mathbf{n}=\big[\big[A_{((i_1-j_1)\mathrm{mod}n_1,(i_2-j_2)\mathrm{mod}n_2)}\big]_{i_2,j_2=1}^{n_2}\big]_{i_1,j_1=1}^{n_1}=\big[\mathcal{A}_{(i_1-j_1)\mathrm{mod}n_1}\big]_{i_1,j_1=1}^{n_1}\)<br>
\(=\left[\begin{array}{ c c c c c c c c }
\mathcal{A}_0 & \mathcal{A}_{n_1-1} & \mathcal{A}_{n_1-2} & \cdots & \cdots & \mathcal{A}_1 \\
\mathcal{A}_1 & \mathcal{A}_0 & \mathcal{A}_{n_1-1} & \mathcal{A}_{n_1-2} &  & \vdots \\
\mathcal{A}_2 & \mathcal{A}_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & \mathcal{A}_2 & \ddots & \ddots & \ddots & \mathcal{A}_{n_1-2} \\
\vdots &  & \ddots & \ddots & \ddots & \mathcal{A}_{n_1-1} \\
\mathcal{A}_{n_1-1} & \cdots & \cdots & \mathcal{A}_2 & \mathcal{A}_1 & \mathcal{A}_0
\end{array}\right]\in\mathbb{C}^{n_1n_2r\times n_1n_2r},\)

