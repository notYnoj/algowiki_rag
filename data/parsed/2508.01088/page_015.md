**Lemma 3.11.** \(u_{n,\lambda},u_{n,\lambda}^-\) _and_ \(v_{n,\lambda}\) _are linearly independent._

_Proof._ Let \(\alpha,\beta,\gamma\in\mathbb{R}\) and **0** the null-vector with _T(n_) components such that

\(\alpha u_{n,\lambda}+\beta u_{n,\lambda}^-+\gamma v_{n,\lambda}=\mathbf{0}.\) (18)

Considering the Equation (18) and since, for \(i-j=n-\lambda-3\), \(u_{n,\lambda}(i,j)\neq 0\) and \(u_{n,\lambda}^-(i,j)=v_{n,\lambda}(i,j)=0\), then \(\alpha=0\). On the other hand, since \(u_{n,\lambda}^-(\lfloor\frac{n}{2}\rfloor,\lfloor\frac{n}{2}\rfloor)=0\) and \(v_{n,\lambda}(\lfloor\frac{n}{2}\rfloor,\lfloor\frac{n}{2}\rfloor)\neq 0\), then \(\gamma=0\). Finally \(\beta\) has to be zero and so these vectors are linearly independent.

**Remark 3.12.** _Note that the vectors_ \(u_{n,\lambda}\), \(u_{n,\lambda}^-\) _and_ \(u_{n,\lambda}^+\) _are not linearly independent, since the sum of them is the null vector. However, if we consider just two of them, like in the previous Lemma, they are._

In this section, we proved that \(\lambda\in\{-2,\dots,\lfloor\frac{n-7}{2}\rfloor\}\) are eigenvalues of T(_n_). Three linearly independent eigenvectors associated with \(\lambda\) were introduced, \(u_{n,\lambda},u_{n,\lambda}^-\) and \(v_{n,\lambda}\), and so its multiplicity is at least 3, except for \(\lambda=\frac{n-7}{2}\) , when _n_ is odd, whose multiplicity is at least 2.

## 3.3 Second sequence of integer eigenvalues

For \(n\ge 4\) and \(\lambda\in\left[\lceil\frac{n-4}{2}\rceil,n-3\right]\cap\mathbb{Z}\), consider the vectors \(x_{n,\lambda},x_{n,\lambda}^1,x_{n,\lambda}^2\) such that

\(x_{n,\lambda}=x_{n,\lambda}^1+x_{n,\lambda}^2\) (19)

with

\(\left[x_{n,\lambda}^1\right]_{(i,j)}=\left\{\begin{array}{ c c }
2\lambda-n+6, & \text{if}i-j=1-(n-\lambda-2) \\
1, & \text{if}i-j<1-(n-\lambda-2)\text{and}j\le n-\lambda+1 \\
0, & \text{otherwise;}
\end{array}\right.\) (20)

\(\left[x_{n,\lambda}^2\right]_{(i,j)}=\left\{\begin{array}{ c c }
-(2\lambda-n+6), & \text{if}j=n-\lambda-2 \\
-1, & \text{if}j<n-\lambda-2\text{and}i-j\le\lambda+2 \\
0, & \text{otherwise;}
\end{array}\right.\)

A different and simple way to define these vectors is by the sum of _RCD-_ vectors, and so

\(x_{n,\lambda}^1=(D_{n,n-\lambda-4}+\dots+D_{n,0})-(C_{n,n}+\dots+C_{n,\lambda+3})+(2\lambda-n+6)D_{n,n-\lambda-3}\text{and}x_{n,\lambda}^2=-(C_{n,n-\lambda-3}+\dots+C_{n,1})+(D_{n,n-1}+\dots+D_{n,\lambda+3})-(2\lambda-n+6)C_{n,n-\lambda-2}.\) (21)

An example of these vectors is presented in Figure 9, for _n_=10 and some values of \(\lambda\). Other examples of these vectors are presented in \[6, Appendix B\].

