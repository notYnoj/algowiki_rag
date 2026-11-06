Essentially, all entries above and on the main diagonal are multiplied by the factor \(\omega\), resulting in the following structure:<tbc>

\(C_n^\omega=\left[\begin{array}{ c c c c c c c c }
a_0 & \omega a_{n-1} & \omega a_{n-2} & \cdots & \cdots & \omega a_1 \\
a_1 & a_0 & \omega a_{n-1} & \omega a_{n-2} &  &  & \vdots \\
a_2 & a_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & a_2 & \ddots & \ddots & \ddots &  &  \\
\vdots &  & \ddots & \ddots & \ddots & \omega a_{n-2} \\
a_{n-1} & \cdots & \cdots & a_2 & a_1 & a_0
\end{array}\right]\in\mathbb{C}^{n\times n}.\)

<tbc>Note that \(C_n^\omega\) still retains a Toeplitz structure, and that for \(\omega=1\) it reduces to the standard circulant matrix. To generalize equation (3.2), we define the \(\omega\)-circulant generator as<tbc>

\([Z_n^\omega]_{i,j}:=\left\{\begin{array}{ c c }
\delta_{(i-j-1)modn} & \text{if}i>j, \\
\omega\delta_{(i-j-1)modn} & \text{if}i\le j,
\end{array}\right.i,j=1,\dots,n.\)

<tbc>Equivalently,<tbc>

\([Z_n^\omega]_{i,j}=\left\{\begin{array}{ c c }
1 & \text{if}i-j=1, \\
\omega & \text{if}i=1\wedge j=n, \\
0 & \text{otherwise,}
\end{array}\right.i,j=1,\dots,n.\)

<tbc>In other words, \(Z_n^\omega\) has all ones on the first superdiagonal and \(\omega\) in the top-right corner:<tbc>

\(Z_n^\omega=\left[\begin{array}{ c c c c c c c }
0 &  &  &  &  & \omega \\
1 & \ddots &  &  &  &  &  \\
\ddots &  & \ddots &  &  &  &  \\
 &  & \ddots & \ddots &  &  &  \\
 &  &  & \ddots & \ddots &  &  \\
 &  &  &  & 1 & 0
\end{array}\right]\in\mathbb{C}^{n\times n}.\)

<tbc>In this framework, \(C_n^\omega\) can be expressed as a linear combination of powers of \(Z_n^\omega\):<tbc>

\(C_n^\omega=\sum_{k=0}^{n-1}a_k(Z_n^\omega)^k.\)

<tbc>A diagonalization formula, paralleling equation (3.4), naturally extends to the case of \(\omega\)-circulant matrices:<tbc>

\(C_n^\omega=F_n^\omega\Lambda_n^\omega(F_n^\omega)^{-1},\)

<tbc>where the diagonal matrix containing the eigenvalues of \(C_n^\omega\) is given by<tbc>

\(\Lambda_n^\omega:=\mathrm{diag}_{j=0,\dots,n-1}\left(p\left(\frac{2\pi j}{n}\right)\right)\)

