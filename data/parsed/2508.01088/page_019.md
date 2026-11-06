_Note that, as in the vector_ \(v_{n+1,n-\lambda-5}^3\)_, the non-nulls components of_ \(y_{n,\lambda}^3\) _form a hexagonal shape inside_ T(_n), where the hexagon sides are alternately_ \(\ell_1=n-\lambda-2\) _and_ \(\ell_2=-n+2\lambda+4\).

_Also note that, when n is even and_ \(\lambda=\frac{n-4}{2}\) , \(\ell_2=0\)_. Thus the vector_ \(y_{n,\lambda}^3\) _is undefined and so is_ \(y_{n,\lambda}\).

In what follows, we will compute the sum-vectors of \(y_{n,\lambda}^1\), \(y_{n,\lambda}^2\) and \(y_{n,\lambda}^3\) by row, column, and diagonal. Since these vectors have significant changes for different values of _n_ and \(\lambda\), we will divide these sums into different cases when necessary.

If \(2n-2\lambda-5<\lambda+2\), the sum-vectors of \(y_{n,\lambda}^1\) are the following.

\(S_{y_{n,\lambda}^1}^r(i)=\left\{\begin{array}{ c c }
0, & \text{if}i\le n-\lambda-3, \\
(n-2\lambda-6)(i-n+3+\lambda), & \text{if}n-\lambda-2\le i\le 2n-2\lambda-5, \\
(n-2\lambda-5)(-3n+3\lambda+2i+8)-(n-\lambda-2), & \text{if}2n-2\lambda-4\le i\le\lambda+2, \\
-2T(n-2\lambda-6), & \text{if}\lambda+3\le i;
\end{array}\right.\)<br>
\(S_{y_{n,\lambda}^1}^c(j)=\left\{\begin{array}{ c c }
0 & \text{if}j\le n-\lambda-3\text{or}j\ge\lambda+3, \\
2(n-2\lambda-5)(\lambda-j+3)-2(n-\lambda-2) & \text{if}n-\lambda-2\le j\le-n+2\lambda+4, \\
(n-2\lambda-6)(n-j+1), & \text{if}-n+2\lambda+5\le j\le\lambda+2;
\end{array}\right.\)<br>
\(S_{y_{n,\lambda}^1}^d(i-j+1)=\left\{\begin{array}{ c c }
-2T(n-2\lambda-6), & \text{if}i-j\le n-\lambda-3, \\
(n-2\lambda-5)(-n+3\lambda-2(i-j)+8)-(n-\lambda-2), & \text{if}n-\lambda-2\le i-j\le-n+2\lambda+4, \\
(n-2\lambda-6)(\lambda+3-(i-j)), & \text{if}-n+2\lambda+5\le i-j\le\lambda+2, \\
0, & \text{if}i-j\ge\lambda+3.
\end{array}\right.\) (28)

Otherwise, if \(2n-2\lambda-5\ge\lambda+2\), the sum-vectors of \(y_{n,\lambda}^1\) are the following.

\(S_{y_{n,\lambda}^1}^r(i)=\left\{\begin{array}{ c c }
0, & \text{if}i\le n-\lambda-3, \\
(n-2\lambda-6)(i-n+3+\lambda), & \text{if}n-\lambda-2\le i\le\lambda+2, \\
-2T(n-2\lambda-6), & \text{if}\lambda+3\le i;
\end{array}\right.\)<br>
\(S_{y_{n,\lambda}^1}^c(j)=\left\{\begin{array}{ c c }
0 & \text{if}j\le n-\lambda-3\text{or}j\ge\lambda+3, \\
(n-2\lambda-6)(n-j+1), & \text{if}n-\lambda-2\le j\le\lambda+2;
\end{array}\right.\)<br>
\(S_{y_{n,\lambda}^1}^d(i-j+1)=\left\{\begin{array}{ c c }
-2T(n-2\lambda-6), & \text{if}i-j\le n-\lambda-3, \\
(n-2\lambda-6)(\lambda+3-(i-j)), & \text{if}n-\lambda-2\le i-j\le\lambda+2, \\
0, & \text{if}i-j\ge\lambda+3.
\end{array}\right.\) (29)

