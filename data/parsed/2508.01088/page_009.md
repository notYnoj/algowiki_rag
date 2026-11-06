Thus \(\mathrm{dim}(\mathcal{E}_{\mathcal{T}(n)}(-3))\le|\mathbf{T}_n|=T(n-3)\) and so \(\mathrm{dim}(\mathcal{E}_{\mathcal{T}(n)}(-3))=T(n-3)\).

From this subsection, we conclude that -3 is the least eigenvalue of T(_n_) with multiplicity _T(n_-3) and 2_n_-2 is its largest eigenvalue which is simple.

In the next two subsections, vectors \(u_{n,\lambda},v_{n,\lambda},x_{n,\lambda}\) and \(y_{n,\lambda}\) are introduced. There will be a sequence of integer eigenvalues \(\lambda\) of T(_n_) with the eigenvectors \(u_{n,\lambda}\) and \(v_{n,\lambda}\) associated with the eigenvalues of the first part of that sequence, and \(x_{n,\lambda}\) and the eigenvectors \(y_{n,\lambda}\) associated with the eigenvalues of the second part. Separately into two parts, these vectors will be defined and investigated, in order to conclude that the integers of both sequences are eigenvalues of T(_n_).

## 3.2 First sequence of integer eigenvalues

For \(n\ge 4\) and \(\lambda\in\left[-2,\lfloor\frac{n-7}{2}\rfloor\right]\cap\mathbb{Z}\), consider the vectors \(u_{n,\lambda},u_{n,\lambda}^1,u_{n,\lambda}^2\) such that

\(u_{n,\lambda}=u_{n,\lambda}^1+u_{n,\lambda}^2,\) (5)

and

\(\left[u_{n,\lambda}^1\right]_{(i,j)}=\left\{\begin{array}{ c c }
n-6-2\lambda, & \text{if}i=\lambda+3, \\
-1, & \text{if}i\ge\lambda+3\text{and}i-j\le\lambda+2, \\
0, & \text{otherwise};
\end{array}\right.\) (6)

\(\left[u_{n,\lambda}^2\right]_{(i,j)}=\left\{\begin{array}{ c c }
-(n-6-2\lambda), & \text{if}i-j=n-\lambda-3, \\
1, & \text{if}i\ge n-\lambda-2\text{and}i-j\le n-\lambda-4, \\
0, & \text{otherwise}.
\end{array}\right.\)

A different and simple way to define these vectors is by the sum of _RCD_- vectors, and so

\(u_{n,\lambda}^1=-(D_{n,0}+\cdots+D_{n,\lambda+2})+(R_{n,1}+\cdots+R_{n,\lambda+3})+(n-6-2\lambda)R_{n,\lambda+3}\text{and}u_{n,\lambda}^2=(R_{n,n}+\cdots+R_{n,n-\lambda-2})-(D_{n,n-1}+\cdots+D_{n,n-\lambda-3})-(n-6-2\lambda)D_{n,n-\lambda-3}.\) (7)

An example of these vectors is presented in \[6, Fig. 6.8\], for _n_=10 and some values of \(\lambda\).

Note that the sum-vectors of \(u_{n,\lambda}\) are the following.

