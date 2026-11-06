in which each block A_<sub>k</sub>_ is itself a 1-level _r_-block circulant matrix:<tbc>

\(\mathcal{A}_k=\left[A_{(k,(i_2-j_2)modn_2)}\right]_{i_2,j_2=1}^{n_2}\)<br>
\(=\left[\begin{array}{ c c c c c c c c }
A_{(k,0)} & A_{(k,n_2-1)} & A_{(k,n_2-2)} & \cdots & \cdots & A_{(k,1)} \\
A_{(k,1)} & A_{(k,0)} & A_{(k,n_2-1)} & A_{(k,n_2-2)} &  & \vdots \\
A_{(k,2)} & A_{(k,1)} & \ddots & \ddots & \ddots & \vdots \\
\vdots & A_{(k,2)} & \ddots & \ddots & \ddots & A_{(k,n_2-2)} \\
\vdots &  & \ddots & \ddots & \ddots & A_{(k,n_2-1)} \\
A_{(k,n_2-1)} & \cdots & \cdots & A_{(k,2)} & A_{(k,1)} & A_{(k,0)}
\end{array}\right]\in\mathbb{C}^{n_2r\times n_2r}.\)

<tbc>For _r_=1 this structure is often called a _block circulant matrix with circulant blocks (BCCB)._<br>
For _d_=3, a 3-level _r_-block circulant matrix is constructed as a block circulant matrix, where each block is itself a 2-level _r_-block circulant matrix. More generally, a _d_-level _r_-block circulant matrix can be defined recursively as a block circulant matrix whose blocks have (_d_-1)-level _r_-block circulant structure. Just as in the classic (uni-level) case, the entire matrix is fully specified by the blocks in its first block column, or, equivalently, by those in its first block row.<br>
A compact expression for a uni-level _r_-block circulant matrix _C<sub>n,r</sub>_ can be derived by using<tbc>

\([Z_n]_{i,j}:=\delta_{(i-j-1)modn}=\left\{\begin{array}{ c c c }
1 & \text{if}i-j=1modn, \\
0 & \text{otherwise,}
\end{array}\right.i,j=1,\dots,n,\)

<tbc>where \(n\in\mathbb{N}\) and \(\delta\) is the Dirac delta function. More explicitly, _Z<sub>n</sub>_ is the matrix that has all ones on the first and (1-_n_)-th diagonals, with zeros elsewhere:<tbc>

\(Z_n=\left[\begin{array}{ c c c c c c }
0 &  &  &  &  & 1 \\
1 & \ddots &  &  &  &  \\
\ddots &  & \ddots &  &  &  \\
 &  & \ddots & \ddots &  &  \\
 &  &  & \ddots & \ddots &  \\
 &  &  &  & 1 & 0
\end{array}\right]\in\mathbb{C}^{n\times n}.\)

<tbc>Raising _Z<sub>n</sub>_ to the power _k_, for _k_=1_,...,n_-1, cyclically shifts the diagonals by _k_ positions, with entries given by<tbc>

\([Z_n^k]_{i,j}:=\delta_{(i-j-k)modn}=\left\{\begin{array}{ c c c c }
1 & \text{if}i-j=kmodn, &  & i,j=1,\dots,n. \\
0 & \text{otherwise,}
\end{array}\right.\)

