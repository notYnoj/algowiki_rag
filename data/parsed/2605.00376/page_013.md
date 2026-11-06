**Proof.** Let _A_ be a Vandermonde matrix satisfying the superregularity conditions of Theorem 3.1. We will initially show that the calculation of Zech logarithms, from Equation (4.26), cancel out for all _i_=3_,...,m_, that is,

\(Z(\sigma(i,l_1)-\sigma(i,l_2)-\sigma(i-1,l_1)+\sigma(i-1,l_2))=Z(\sigma(i-1,l_1)-\sigma(i-1,l_2)-\sigma(i-2,l_1)+\sigma(i-2,l_2)).\) (4.28)

This is equivalent to showing that the arguments are equal, which implies that

\(\sigma(i,l_1)-2\sigma(i-1,l_1)+\sigma(i-2,l_1)-\sigma(i,l_2)+2\sigma(i-1,l_2)-\sigma(i-2,l_2)=0.\) (4.29)

Since _A_ is a Vandermonde matrix, then by (2.3), if _l_ is any column of _A_, considering consecutive rows _i_-2, _i_-1, and _i_, then

\(\sigma(i,l)=2\sigma(i-1,l)-\sigma(i-2,l).\) (4.30)

Replacing (4.30) into (4.29), we obtain that the Zech logarithms indeed cancels out. Therefore, Equation (4.26) can be simplified to

\(r_{i-2}=\sigma(i,l_2)-\sigma(i-1,l_2),\) (4.31)

for all _i_=3_,...,m_. Again, due to _A_ being a Vandermonde matrix, if we consider two consecutive rows _i_-1 and _i_, and a fixed column _l_<sub>2</sub>, it follows that the difference between the powers of \(\alpha\) in \(\sigma(i,l_2)\) and \(\sigma(i-1,l_2)\) is equal to _l_<sub>2</sub>, which provides us (4.27), concluding the proof. □

In the following example we show how calculations are made easier by using the Corollary 4.1.

**Example 4.4.** Consider again _C_ the MDS array code with parameters \[10,5,6\] over \(\mathbb{F}_2^5\) constructed in Example 3.1. Now, suppose that the received vector is

\(\mathbf{v}=[110011110111001111010101011010000101000011111100111].\)

The syndromes from (4.2) are given by

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
0 \\
0
\end{array}\right],\mathbf{s}_3^T=\left[\begin{array}{ c }
1 \\
0 \\
1 \\
1
\end{array}\right],\mathbf{s}_4^T=\left[\begin{array}{ c }
1 \\
1 \\
0 \\
1
\end{array}\right],\mathbf{s}_5^T=\left[\begin{array}{ c }
1 \\
1 \\
1 \\
1 \\
0
\end{array}\right].\)

Since all syndromes are nonzero, conducting the calculations in (4.3), initially with _l_<sub>1</sub>=1, we obtain

\(\mathbf{y}_1^T=\left[\begin{array}{ c }
0 \\
1 \\
1 \\
1 \\
0
\end{array}\right],\mathbf{y}_2^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
1 \\
1
\end{array}\right],\mathbf{y}_3^T=\left[\begin{array}{ c }
1 \\
0 \\
1 \\
1 \\
1
\end{array}\right],\mathbf{y}_4^T=\left[\begin{array}{ c }
0 \\
1 \\
0 \\
1 \\
0
\end{array}\right],\mathbf{y}_5^T=\left[\begin{array}{ c }
0 \\
1 \\
1 \\
1 \\
0
\end{array}\right].\)

By Corollary 4.1 all values of _r_<sub>_i_-2</sub> is equal to _l_<sub>2</sub>, that is, _r_<sub>1</sub>=_r_<sub>2</sub>=_r_<sub>3</sub>=2. Then,

\(\mathbf{y}_i^T\neq C^2\mathbf{y}_{i-1}^T,\)

for all _i_=3,4,5. As the above equalities fail, the algorithm follows for _l_<sub>2</sub>=3, where again by using Corollary 4.1, we have _r_<sub>1</sub>=_r_<sub>2</sub>=_r_<sub>3</sub>=3. Then, we check that

\(\mathbf{y}_i^T=C^3\mathbf{y}_{i-1}^T,\)

