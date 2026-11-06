Just like Toeplitz matrices, _H<sub>n</sub>_ is completely determined by its 2_n_-1 blocks _A<sub>k</sub>_ for _k_=2_,...,_2_n_, or, equivalently, by its first block row and last block column. For _d_=2 and **_n_**=(_n_<sub>1</sub>_,n_<sub>2</sub>), a 2-level _r_-block Hankel matrix takes the form

\(H_n=\left[A_{i+j}\right]_{i,j=1}^n=\left[\left[A_{(i_1+j_1,i_2+j_2)}\right]_{i_2,j_2=1}^{n_2}\right]_{i_1,j_1=1}^{n_1}=\left[\mathcal{A}_{i_1+j_1}\right]_{i_1,j_1=1}^{n_1}\)<br>
\(=\left[\begin{array}{ c c c c c }
\mathcal{A}_2 & \mathcal{A}_3 & \mathcal{A}_4 & \cdots & \mathcal{A}_{n_1+1} \\
\mathcal{A}_3 & \mathcal{A}_4 & & \ddots & \vdots \\
\mathcal{A}_4 & & \ddots & & \mathcal{A}_{2n_1-2} \\
\vdots & \ddots & & \mathcal{A}_{2n_1-2} & \mathcal{A}_{2n_1-1} \\
\mathcal{A}_{n_1+1} & \cdots & \mathcal{A}_{2n_1-2} & \mathcal{A}_{2n_1-1} & \mathcal{A}_{2n_1}
\end{array}\right]\in\mathbb{C}^{n_1n_2r\times n_1n_2r},\)

where each block A_<sub>k</sub>_ is itself a 1-level _r_-block Hankel matrix,

\(\mathcal{A}_k=\left[A_{(k,i_2+j_2)}\right]_{i_2,j_2=1}^{n_2}\)<br>
\(=\left[\begin{array}{ c c c c c }
A_{(k,2)} & A_{(k,3)} & A_{(k,4)} & \cdots & A_{(k,n_2+1)} \\
A_{(k,3)} & A_{(k,4)} & & \ddots & \vdots \\
A_{(k,4)} & & \ddots & & A_{(k,2n_2-2)} \\
\vdots & \ddots & & & A_{(k,2n_2-2)} & A_{(k,2n_2-1)} \\
A_{(k,n_2+1)} & \cdots & A_{(k,2n_2-2)} & A_{(k,2n_2-1)} & A_{(k,2n_2)}
\end{array}\right]\in\mathbb{C}^{n_2r\times n_2r}.\)

In the multi-level setting, a _d_-level _r_-block Hankel matrix admits a recursive block structure, in the sense that it can be interpreted as a block Hankel matrix whose blocks are (_d_-1)-level _r_-block Hankel matrices. As in the one-level case, the entire matrix is uniquely specified by the blocks in its first block row and last block column. To obtain a compact representation of _H<sub>n</sub>_, we introduce, for \(n\in\mathbb{N}\) and \(k\in\mathbb{Z}\), the matrix<tbc>

\(\left[K_n^{(k)}\right]_{i,j}:=\delta_{i+j-k}=\left\{\begin{array}{ c c }
1 & \text{if}i+j=k, \\
0 & \text{otherwise,}
\end{array}\right.i,j=1,\dots,n,\)

<tbc>which places ones on the (_k_-1)-th anti-diagonal and zeros elsewhere. The multi-level generalization for \(n\in\mathbb{N}^d\) and \(k\in\mathbb{Z}^d\) is given by<tbc>

\(K_n^{(k)}:=K_{n_1}^{(k_1)}\otimes K_{n_2}^{(k_2)}\otimes\cdots\otimes K_{n_d}^{(k_d)}.\)

<tbc>This leads to the following compact expression for _H<sub>n</sub>_:

\(H_n=\left[A_{i+j}\right]_{i,j=1}^n=\sum_{k=2}^{2n}K_n^{(k)}\otimes A_k.\) (3.6)

In analogy with the Toeplitz and circulant cases, the above representation follows from a direct verification of the individual matrix blocks.

Block Hankel matrices are closely related to block Toeplitz matrices through the anti-identity matrix; see \[37\] for spectral properties and applications.

