\(S_{v_{n,\lambda}}^r(i)=\left\{\begin{array}{ c c }
0, & \text{if}i\le\lambda+2\text{or}n-(\lambda+2)\le i, \\
-2T(n-7-2\lambda)(\lambda+3), & \text{if}i=\lambda+3, \\
2(\lambda+3)(n-3-\lambda-i), & \text{if}\lambda+4\le i\le n-(\lambda+3);
\end{array}\right.\)<br>
\(S_{v_{n,\lambda}}^c(j)=\left\{\begin{array}{ c c }
0, & \text{if}j\le\lambda+3\text{or}j\ge n-(\lambda+2), \\
(\lambda+3)(2j-n-1), & \text{if}\lambda+4\le j\le n-(\lambda+3);
\end{array}\right.\)<br>
\(S_{v_{n,\lambda}}^d(i-j+1)=\left\{\begin{array}{ c c }
0, & \text{if}i-j\le\lambda+2\text{or}i-j\ge n-(\lambda+3), \\
(\lambda+3)(2(i-j)+1-n), & \text{if}\lambda+3\le i-j\le n-(\lambda+4).
\end{array}\right.\) (16)

Consider the following Lemma.

**Lemma 3.10.** _For_ \(n\ge 4\) _and_ \(\lambda\in\left[-2,\lfloor\frac{n-7}{2}\rfloor\right]\), \(v_{n,\lambda}\) _in an eigenvector of_ T(_n_) _associated with_ \(\lambda\).

_Proof._ Let _A_ be the adjacency matrix of T(_n_). Consider the following equation

\(Av_{n,\lambda}(i,j)=\sum_{(p,q)\sim(i,j)}v_{n,\lambda}(p,q)\)<br>
\(=\underbrace{\sum_{q\in[i]}v_{n,\lambda}(i,q)}_{(\text{A})}+\underbrace{\sum_{p\in[j,n]}v_{n,\lambda}(p,j)}_{(B)}+\underbrace{\sum_{p-q=i-j}v_{n,\lambda}(p,q)}_{(\text{C})}-3v_{n,\lambda}(i,j)\) (17)

Taking into account (16) and (11), it follows that (A)+(B)+(C) and \((\lambda+3)(u_{n,\lambda}^1(p,q)+u_{n,\lambda}^2(p,q)+u_{n,\lambda}^3(p,q))=(\lambda+3)u_{n,\lambda}(p,q)\) are equal for each of the following conditions.

(C1) \(i\le\lambda+2\) and \(j\le\lambda+3\) and \(i-j\le\lambda+2\);<tbc>

(C2) \(i=\lambda+3\) and \(j\le\lambda+3\) and \(i-j\le\lambda+2\);<tbc>

(C3) \(\lambda+4\le i\le n-(\lambda+3)\) and \(j\le\lambda+3\) and \(i-j\le\lambda+2\);<tbc>

(C4) \(\lambda+4\le i\le n-(\lambda+3)\) and \(j\le\lambda+3\) and \(\lambda+3\le i-j\le n-(\lambda+4)\);<tbc>

(C5) \(\lambda+4\le i\le n-(\lambda+3)\) and \(\lambda+4\le j\le n-(\lambda+3)\) and \(i-j\le\lambda+2\);<tbc>

(C6) \(\lambda+4\le i\le n-(\lambda+3)\) and \(\lambda+4\le j\le n-(\lambda+3)\) and \(\lambda+3\le i-j\le n-(\lambda+4)\);<tbc>

(C7) \(n-(\lambda+2)\le i\) and \(j\le\lambda+3\) and \(\lambda+3\le i-j\le n-(\lambda+4)\);<tbc>

(C8) \(n-(\lambda+2)\le i\) and \(j\le\lambda+3\) and \(n-(\lambda+3)\le i-j\);<tbc>

(C9) \(n-(\lambda+2)\le i\) and \(\lambda+4\le j\le n-(\lambda+3)\) and \(i-j\le\lambda+2\);<tbc>

(C10) \(n-(\lambda+2)\le i\) and \(\lambda+4\le j\le n-(\lambda+3)\) and \(\lambda+3\le i-j\le n-(\lambda+4)\);<tbc>

(C11) \(n-(\lambda+2)\le i\) and \(n-(\lambda+2)\le j\) and \(i-j\le\lambda+2\).

Therefore, the proof is done.

