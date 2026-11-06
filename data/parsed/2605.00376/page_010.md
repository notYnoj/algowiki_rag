Using the Zech logarithm defined in (2.5) and the property (2.7), we have<tbc>

\(\mathbf{y}_2^T=C^{\sigma(2,l_2)+Z(\sigma(2,l_1)-\sigma(1,l_1)+\sigma(1,l_2)-\sigma(2,l_2))}\mathbf{e}_{l_2}^T,\) (4.20)

<tbc>that is<tbc>

\(\mathbf{e}_{l_2}^T=C^{-\sigma(2,l_2)-Z(\sigma(2,l_1)-\sigma(1,l_1)+\sigma(1,l_2)-\sigma(2,l_2))}\mathbf{y}_2^T.\) (4.21)

<tbc>In the same way<tbc>

\(\mathbf{y}_3^T=C^{\sigma(3,l_2)+Z(\sigma(3,l_1)-\sigma(2,l_1)+\sigma(2,l_2)-\sigma(3,l_2))}\mathbf{e}_{l_2}^T.\) (4.22)

<tbc>Replacing (4.21) into (4.22), we have<tbc>

\(\mathbf{y}_3^T=C^{r_1}\mathbf{y}_2^T,\) (4.23)

<tbc>where<tbc>

\(r_1=\sigma(3,l_2)-\sigma(2,l_2)+Z(\sigma(3,l_1)-\sigma(3,l_2)-\sigma(2,l_1)+\sigma(2,l_2))-Z(\sigma(2,l_1)-\sigma(2,l_2)-\sigma(1,l_1)+\sigma(1,l_2)).\) (4.24)

<tbc>Similarly,<tbc>

\(\mathbf{y}_i^T=C^{r_{i-2}}\mathbf{y}_{i-1}^T,\) (4.25)

<tbc>for all _i_=3_,...,m_, where

\(r_{i-2}=\sigma(i,l_2)-\sigma(i-1,l_2)+Z(\sigma(i,l_1)-\sigma(i,l_2)-\sigma(i-1,l_1)+\sigma(i-1,l_2))-Z(\sigma(i-1,l_1)-\sigma(i-1,l_2)-\sigma(i-2,l_1)+\sigma(i-2,l_2)).\) (4.26)

By ensuring that Equation (4.25) hold for all _i_=3_,...,m_, it follows that the expressions **s**_<sub>i</sub>_ are valid, that is, the symbol errors indeed occurred at positions _l_<sub>1</sub> and _l_<sub>2</sub>. To determine the magnitudes of the errors, solve the linear system given in Equation (4.10) using any two syndrome equations. To determine the magnitudes of the errors, solve the linear system given in Equation (4.10) using any two syndrome equations. Its coefficient matrix is a \(2b\times 2b\) block submatrix of \(\psi(A)\) and is nonsingular due to the block-superregularity induced by the superregularity of _A_. Consequently, the error magnitudes _e_<sub>_l_<sub>1</sub></sub> and _e_<sub>_l_<sub>2</sub></sub> are uniquely determined. □

Below, we present examples illustrating Cases 3 and 4 of Algorithm 2, in order to better elucidate the behavior of the algorithm using MDS array codes constructed from superregular Vandermonde and Cauchy matrices.

**Example 4.2.** Consider C the MDS array code with parameters \[10,5,6\] over \(\mathbb{F}_2^5\) constructed in Example 3.1. Assume that the received vector is<tbc>

\(\mathbf{v}=[011011110101101110101010110101000001010100001111100111].\)

<tbc>The syndromes from (4.2) are given by<tbc>

\(\mathbf{s}_1^T=\left[\begin{array}{ c }
0 \\
0 \\
1 \\
1 \\
0
\end{array}\right],\mathbf{s}_2^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
0
\end{array}\right],\mathbf{s}_3^T=\left[\begin{array}{ c }
0 \\
0 \\
1 \\
0
\end{array}\right],\mathbf{s}_4^T=\left[\begin{array}{ c }
0 \\
0 \\
0 \\
1 \\
0
\end{array}\right],\mathbf{s}_5^T=\left[\begin{array}{ c }
1 \\
1 \\
1 \\
1 \\
1
\end{array}\right].\)

<tbc>Since all the syndromes are nonzero, we start by calculating the equations in (4.3) with _l_<sub>1</sub>=1, yielding the following results:

\(\mathbf{y}_1^T=\left[\begin{array}{ c }
1 \\
1 \\
1 \\
0
\end{array}\right],\mathbf{y}_2^T=\left[\begin{array}{ c }
0 \\
1 \\
1 \\
1 \\
1
\end{array}\right],\mathbf{y}_3^T=\left[\begin{array}{ c }
0 \\
0 \\
0 \\
0 \\
0
\end{array}\right],\mathbf{y}_4^T=\left[\begin{array}{ c }
0 \\
0 \\
0 \\
0 \\
0
\end{array}\right],\mathbf{y}_5^T=\left[\begin{array}{ c }
0 \\
0 \\
0 \\
0 \\
0
\end{array}\right].\)

Note that in this case, we have three zero vectors, confirming an error at position _l_<sub>1</sub>=1. The two nonzero vectors share the syndrome **s**<sub>1</sub>. Therefore, the second error occurred in the position corresponding to the<tbc>

