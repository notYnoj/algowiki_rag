with blocks \(A_\mathbf{k}\in\mathbb{C}^{r\times r}\), \(\mathbf{k}\in\{-(\mathbf{n}-\mathbf{1}),\dots,\mathbf{n}-\mathbf{1}\}\), where the block in position (**_i_**_,**j**_) depends only on the difference **_i_**-**_j_**, is called a multi-level block Toeplitz matrix, or, more precisely, a _d_-level _r_-block Toeplitz matrix. For _r_=1 the blocks are scalars and one recovers the classical _d_-level (scalar) Toeplitz matrices.<br>
In the simplest case where _d_=1 and **_n_**=_n_, a 1-level _r_-block Toeplitz matrix is just a classical block Toeplitz matrix, whose blocks remain constant along the block diagonals:<tbc>

\(T_n=[A_{i-j}]_{i,j=1}^n=\left[\begin{array}{ c c c c c c c }
A_0 & A_{-1} & A_{-2} & \cdots & \cdots & A_{1-n} \\
A_1 & A_0 & A_{-1} & A_{-2} &  & \vdots \\
A_2 & A_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & A_2 & \ddots & \ddots & \ddots & A_{-2} \\
\vdots &  & \ddots & \ddots & \ddots & A_{-1} \\
A_{n-1} & \cdots & \cdots & A_2 & A_1 & A_0
\end{array}\right]\in\mathbb{C}^{nr\times nr}.\)

<tbc>Note that _T<sub>n</sub>_ is completely specified by its 2_n_-1 blocks \(A_k\in\mathbb{C}^{r\times r}\), _k_=-(_n_-1)_,...,n_-1, or equivalently by its first block row and first block column.<br>
For _d_=2 and **_n_**=(_n_<sub>1</sub>_,n_<sub>2</sub>), we have a 2-level _r_-block Toeplitz matrix:<tbc>

\(T_\mathbf{n}=\left[\left[A_{(i_1-j_1,i_2-j_2)}\right]_{i_2,j_2=1}^{n_2}\right]_{i_1,j_1=1}^{n_1}=[\mathcal{A}_{i_1-j_1}]_{i_1,j_1=1}^{n_1}\)<br>
\(=\left[\begin{array}{ c c c c c c c c }
\mathcal{A}_0 & \mathcal{A}_{-1} & \mathcal{A}_{-2} & \cdots & \cdots & \mathcal{A}_{1-n_1} \\
\mathcal{A}_1 & \mathcal{A}_0 & \mathcal{A}_{-1} & \mathcal{A}_{-2} &  & \vdots \\
\mathcal{A}_2 & \mathcal{A}_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & \mathcal{A}_2 & \ddots & \ddots & \ddots & \mathcal{A}_{-2} \\
\vdots &  & \ddots & \ddots & \ddots & \mathcal{A}_{-1} \\
\mathcal{A}_{n_1-1} & \cdots & \cdots & \mathcal{A}_2 & \mathcal{A}_1 & \mathcal{A}_0
\end{array}\right]\in\mathbb{C}^{n_1n_2r\times n_1n_2r},\)

<tbc>where each block A_<sub>k</sub>_ is itself a 1-level _r_-block Toeplitz matrix:<br>
\(\mathcal{A}_k=\left[A_{(k,i_2-j_2)}\right]_{i_2,j_2=1}^{n_2}\)<br>
\(=\left[\begin{array}{ c c c c c c c c }
A_{(k,0)} & A_{(k,-1)} & A_{(k,-2)} & \cdots & \cdots & A_{(k,1-n_2)} \\
A_{(k,1)} & A_{(k,0)} & A_{(k,-1)} & A_{(k,-2)} &  & \vdots \\
A_{(k,2)} & A_{(k,1)} & \ddots & \ddots & \ddots & \vdots \\
\vdots & A_{(k,2)} & \ddots & \ddots & \ddots & A_{(k,-2)} \\
\vdots &  & \ddots & \ddots & \ddots & A_{(k,-1)} \\
A_{(k,n_2-1)} & \cdots & \cdots & A_{(k,2)} & A_{(k,1)} & A_{(k,0)}
\end{array}\right]\in\mathbb{C}^{n_2r\times n_2r}.\)

For _r_=1, this type of matrix is also known as a _block Toeplitz matrix with Toeplitz blocks_ or BTTB matrix; for a general _r_ it is a BTTB matrix whose innermost entries are \(r\times r\) matrices.

In the case where _d_=3, a 3-level _r_-block Toeplitz matrix is made up of blocks, and each block has its own 2-level _r_-block Toeplitz structure. A more general way to describe a _d_-level _r_-block Toeplitz matrix is as a block Toeplitz matrix whose blocks<tbc>

