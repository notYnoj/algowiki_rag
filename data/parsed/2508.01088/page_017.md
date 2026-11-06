\(S_{x_{n,\lambda}}^r(i)=0S_{x_{n,\lambda}}^c(j)=\left\{\begin{array}{ c c }
0, & \text{if}j\le n-\lambda-3\text{or}j\ge\lambda+3, \\
-(2\lambda-n+5)\times & \text{if}j=n-\lambda-2, \\
\times((2\lambda-n-6)+(n-\lambda-3)), & \text{if}n-\lambda-1\le j\le\lambda+2; \\
(2\lambda-n+6)+(n-\lambda-3), & \text{if}i-j\le n-\lambda-5\text{or}i-j\ge\lambda+3, \\
0, & \text{if}i-j=n-\lambda-4, \\
\times((2\lambda-n-6)+(n-\lambda-3)), & \text{if}i-j=n-\lambda-4, \\
-(2\lambda-n+6)-(n-\lambda-3), & \text{if}n-\lambda-3\le i-j\le<\lambda+2.
\end{array}\right.\) (22)

Consider the following Lemma.

**Lemma 3.13.** _For_ \(n\ge 4\) _and_ \(\lambda\in\left[\lceil\frac{n-4}{2}\rceil,n-3\right]\cap\mathbb{Z}\), \(x_{n,\lambda}\) _is an eigenvector of_ T(_n_) _associated with_ \(\lambda\).

_Proof._ Let _A_ be the adjacency matrix of T(_n_). Consider the following equation

\(Ax_{n,\lambda}(i,j)=\sum_{(p,q)\sim(i,j)}x_{n,\lambda}(p,q)=\underbrace{\sum_{q\in[i]}x_{n,\lambda}(i,q)}_{=0}+\underbrace{\sum_{p\in[j,n]}x_{n,\lambda}(p,j)}_{(\text{A})}+\underbrace{\sum_{p-q=i-j}x_{n,\lambda}(p,q)-3x_{n,\lambda}(i,j)}_{(\text{B})}\) (23)

In \[6,  6.4\], some parts of Equation (23) are presented. The columns (_A_)+(_B_) and \((\lambda+3)x_{n,\lambda}(i,j)\) are complemented with the values of (22) and (19), respectively. Since they are equal for each condition, the proof is done.

Now consider the vectors \(y_{n,\lambda},y_{n,\lambda}^1,y_{n,\lambda}^2,y_{n,\lambda}^{2,1},y_{n,\lambda}^{2,2},y_{n,\lambda}^{2,3},y_{n,\lambda}^{2,4},y_{n,\lambda}^3,y_{n,\lambda}^{3,k}\in\mathbb{R}^{T(n)}\) for some \(n\in\mathbb{N}\) and for all \(k\in[\mathrm{min}\{n-\lambda-2,-n+2\lambda+4\}]\) such that<tbc>

\(y_{n,\lambda}=y_{n,\lambda}^1+y_{n,\lambda}^2+y_{n,\lambda}^3,y_{n,\lambda}^2=y_{n,\lambda}^{2,1}+y_{n,\lambda}^{2,2}+y_{n,\lambda}^{2,3}+y_{n,\lambda}^{2,4}\text{and}y_{n,\lambda}^3=\sum_{k=1}^{\mathrm{min}\{n-\lambda-2,-n+2\lambda+4\}}y_{n,\lambda}^{3,k}\text{(24)}\)

<tbc>with

\(\left[y_{n,\lambda}^1\right]_{(i,j)}=\left\{\begin{array}{ c c }
0, & \text{if}j\le n-\lambda-3\text{or}j\ge\lambda+3, \\
n-2\lambda-6, & \text{if}(-n+2\lambda+5\le j\le\lambda+2)\text{or} \\
\left(\left(n-\lambda-2\le j\le-n+2\lambda+4\right)\text{and} & \text{if}i\ge\lambda+3\text{or}i-j\le n-\lambda-3\right)\right), \\
2\left(n-2\lambda-5\right), & \text{if}i\le\lambda+2\text{and}j\ge n-\lambda-2\text{and}i-j\ge n-\lambda-2;
\end{array}\right.\) (25)

