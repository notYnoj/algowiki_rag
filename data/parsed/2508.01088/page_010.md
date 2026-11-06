\(S_{u_{n,\lambda}}^c(i)=\left\{\begin{array}{ c c }
0, & \text{if}i\le\lambda+2\text{or}i\ge n-\lambda-2, \\
(\lambda+3)(n-6-2\lambda), & \text{if}i=\lambda+3, \\
-(\lambda+3), & \text{if}\lambda+4\le i\le n-\lambda-3;
\end{array}\right.S_{u_{n,\lambda}}^c(j)=0,\forall j\in[n];S_{u_{n,\lambda}}^d(i-j+1)=\left\{\begin{array}{ c c }
0, & \text{if}i-j\le\lambda+2\text{or}i-j\ge n-\lambda-2, \\
\lambda+3, & \text{if}\lambda+3\le i-j\le n-\lambda-4, \\
-(\lambda+3)(n-6-2\lambda), & \text{if}i-j=n-\lambda-3.
\end{array}\right.\) (8)

Consider the following lemma.

**Lemma 3.8.** _For_ \(n\ge 4\) _and_ \(\lambda\in\left[-2,\lfloor\frac{n-7}{2}\rfloor\right]\cap\mathbb{Z}\), \(u_{n,\lambda}\) _is an eigenvector of_ T(_n_) _associated with_ \(\lambda\).

_Proof._ Let _A_ be the adjacency matrix of T(_n_). Consider the following equation

\(Au_{n,\lambda}(i,j)=\sum_{(p,q)\sim(i,j)}u_{n,\lambda}(p,q)=\underbrace{\sum_{q\in[i]}u_{n,\lambda}(i,q)}_{(\text{A})}+\underbrace{\sum_{p\in[j,n]}u_{n,\lambda}(p,j)}_0+\underbrace{\sum_{p-q=i-j}u_{n,\lambda}(p,q)}_{(\text{B})}-3u_{n,\lambda}(i,j)\) (9)

In \[6,  6.2\], some parts of Equation (9) are presented. The columns (A)+(B) and \((\lambda+3)u_{n,\lambda}(i,j)\) are complemented with the respective values of Equations (8) and (5), respectively. Since they are equal for each condition, the proof is done.

Now consider the vectors \(v_{n,\lambda},v_{n,\lambda}^1,v_{n,\lambda}^2,v_{n,\lambda}^3,v_{n,\lambda}^{3,k}\in\mathbb{R}^{T(n)}\) for some \(n\in\mathbb{N}\) and for all \(k\in[min\{\lambda+3,n-7-2\lambda\}]\) such that

\(v_{n,\lambda}=v_{n,\lambda}^1+v_{n,\lambda}^2+v_{n,\lambda}^3,v_{n,\lambda}^3=\sum_{k=1}^{min\{\lambda+3,n-2\lambda-7\}}v_{n,\lambda}^{3,k}\) (10)

and

\(\left[v_{n,\lambda}^1\right]_{(i,j)}=\left\{\begin{array}{ c c }
-T(n-7-2\lambda), & \text{if}i=\lambda+3, \\
n-7-2\lambda, & \text{if}i\ge\lambda+4\text{and}j\le\lambda+3\text{and}i-j\le n-(\lambda+4), \\
0, & \text{otherwise;}
\end{array}\right.\left[v_{n,\lambda}^2\right]_{(i,j)}=\left\{\begin{array}{ c c }
-T(n-7-2\lambda), & \text{if}i=\lambda+3, \\
n-7-2\lambda, & \text{if}i\ge\lambda+4\text{and}j\le n-(\lambda+3)\text{and}i-j\le\lambda+2, \\
0, & \text{otherwise;}
\end{array}\right.\left[v_{n,\lambda}^{3,k}\right]_{(i,j)}=\left\{\begin{array}{ c c }
-2, & \text{if}\lambda+4+k\le i\le n-k\text{and} \\
k+1\le j\le n-(\lambda+3+k)\text{and} & \text{if}k\le i-j\le n-(\lambda+4+k), \\
0, & \text{otherwise.}
\end{array}\right.\) (11)

