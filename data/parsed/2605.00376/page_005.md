## 3. Constructions of MDS Array s

In this section we will present the encoding of MDS array codes based on \[5,7\]. We start by defining an isomorphism that takes a primitive element of a finite field into a Frobenius companion matrix.

Let us consider \(M_{m\times n}(\mathbb{F}_q)\) and \(\alpha\in\mathbb{F}_{q^b}\), with _b_ a positive integer. There is a field isomorphism \(\phi:\mathbb{F}_{q^b}\longrightarrow\mathbb{F}_q[C]\) defined by \(\phi(\alpha)=C\), where \(C\in M_{b\times b}(\mathbb{F}_q)\) is a Frobenius companion matrix. We can extend to a ring isomorphism defined by

\(\begin{array}{ c c c }
\psi:M_{m\times n}(\mathbb{F}_{q^b})\longrightarrow & M_{mb\times nb}(\mathbb{F}_q) \\
A=[a_{ij}] & \longmapsto\psi(A)=[\phi(a_{ij})]=[C^{\sigma(i,j)}],
\end{array}\) (3.1)

where \(\sigma(i,j)\) is the power of \(\alpha\) in each element _a<sub>ij</sub>_ of _A_.

Let C be a linear array code over \(\mathbb{F}_q^b\) with parameters \[_n,k,d_\]. If _d_ satisfies the equality in (2.2), then C is an MDS array code. The following result provides a condition for C to be MDS and presents a parity-check matrix for C.

**Theorem 3.1.** _\[19,7\] If_ \(A=[a_{ij}]\in M_{(n-k)\times k}(\mathbb{F}_{q^b})\) _is a superregular b-block matrix, then_ \(H=\left[\psi(A)|I_{(n-k)b}\right]\) _is a parity-check matrix of a_ \[_n,k,n-k_+1\] _MDS linear array code_ C_, where_ \(\psi\) _is the isomorphism given in (3.1)._

Henceforth we assume _q_=2, that is, binary codes and linear codes. Then, C is an MDS array code over \(\mathbb{F}_2^b\). The code parameters become \[_n,k,n-k_+1\]=\[_m+k,k,m_+1\], where _m=n-k_. The parity-check matrix is given by

\(H=\left[\psi(A)|I_{mb}\right]=\left[\begin{array}{ c c c }
A_{11} & A_{12} & \dots & A_{1k} \\
A_{21} & A_{22} & \dots & A_{2k} \\
\vdots & \vdots & \ddots & \vdots \\
A_{m1} & A_{m2} & \dots & A_{mk}
\end{array}\right],\) (3.2)

with \(A_{ij}=C^{\sigma(i,j)}\), where \(C\in M_{b\times b}(\mathbb{F}_2)\) is a Frobenius companion matrix, \(\sigma(i,j)\) is the power \(\alpha\) of each element _a<sub>ij</sub>_ of a superregular matrix _A_ of dimension \(m\times k\) and _I<sub>mb</sub>_ is the identity matrix of dimension _mb_.

**Example 3.1.** Let \(p(x)=x^5+x^3+x^2+x+1\in\mathbb{F}_2[x]\) be a primitive polynomial with primitive element \(\alpha\in\mathbb{F}_{25}\) and let us construct an MDS array code C with parameters \[10,5,6\] over \(\mathbb{F}_2^5\), that is, with _m=k=b_=5. The superregular Vandermonde matrix and the Frobenius companion matrix associated to _p(x_) are, respectively, given by<tbc>

\(A=\left[\begin{array}{ c c c c }
1 & 1 & 1 & 1 & 1 \\
\alpha & \alpha^2 & \alpha^3 & \alpha^4 & \alpha^5 \\
\alpha^2 & \alpha^4 & \alpha^6 & \alpha^8 & \alpha^{10} \\
\alpha^3 & \alpha^6 & \alpha^9 & \alpha^{12} & \alpha^{15} \\
\alpha^4 & \alpha^8 & \alpha^{12} & \alpha^{16} & \alpha^{20}
\end{array}\right]\text{and}C=\left[\begin{array}{ c c c c }
0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 0
\end{array}\right].\)

<tbc>Applying the isomorphism (3.1) we have that<tbc>

\(\psi(A)=\left[\begin{array}{ c c c c }
I_5 & I_5 & I_5 & I_5 & I_5 \\
C & C^2 & C^3 & C^4 & C^5 \\
C^2 & C^4 & C^6 & C^8 & C^{10} \\
C^3 & C^6 & C^9 & C^{12} & C^{15} \\
C^4 & C^8 & C^{12} & C^{16} & C^{20}
\end{array}\right].\)

