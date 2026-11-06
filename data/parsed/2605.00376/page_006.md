Thus, according to (3.2), the parity-check matrix for an MDS array code C is given by

\(H=\left[\begin{array}{ c c c c c }
I_5 & I_5 & I_5 & I_5 & I_5 \\
C & C^2 & C^3 & C^4 & C^5 \\
C^2 & C^4 & C^6 & C^8 & C^{10} \\
C^3 & C^6 & C^9 & C^{12} & C^{15} \\
C^4 & C^8 & C^{12} & C^{16} & C^{20}
\end{array}\right].\)

## 4. Decoding of MDS Array s

This section presents two decoding algorithms for MDS array codes with parameters \[_n,k,n-k_+1\]=\[_m+k,k,m_+1\]: one for correcting a single symbol error over \(\mathbb{F}_2^b\) when \(m\ge 2\), and another for correcting two symbol errors over \(\mathbb{F}_2^b\) when \(m\ge 4\), where _m=n-k_, without assuming knowledge of the error locations. A simplified version of the decoding algorithm for correcting two symbol errors is presented when the superregular matrix is chosen as a Vandermonde matrix.

It is well known that linear block codes with parameters \[_N,K,D_\] can correct up to \(\left\lfloor\frac{D-1}{2}\right\rfloor\) symbol errors \[13\]. Similarly, MDS array codes with parameters \[_n,k,d_\], where _k=K/b_ and _n=N/b_, can correct up to \(\left\lfloor\frac{d-1}{2}\right\rfloor\) symbol errors over \(\mathbb{F}_2^b\). In Subsection 4.1, we present the progress made toward extending the proposed algorithms to handle three symbol errors, as well as the main obstacles encountered in this generalization. A simplified form is also presented for the case of three symbol errors when a Vandermonde matrix is used.

Let C be an MDS array code over \(\mathbb{F}_2^b\) constructed as in Section 3. If **c**=\[**c**<sub>1</sub>**c**<sub>2</sub>_..._**c**_<sub>n</sub>_\] is a transmitted codeword and **v**=\[**v**<sub>1</sub>**v**<sub>2</sub>_..._**v**_<sub>n</sub>_\] is a received vector then **e**=**v**-**c** is the error vector, where \(\mathbf{c}_j,\mathbf{v}_j,\mathbf{e}_j\in\mathbb{F}_2^b\), for _j_=1_,...,n_. The **syndrome vector s** of **v** is defined by

\(\mathbf{s}^T=H\cdot\mathbf{v}^T=[\mathbf{s}_1\mathbf{s}_2\dots\mathbf{s}_m],\) (4.1)

where \(\mathbf{s}_i\in\mathbb{F}_2^b\), for _i_=1_,...,m_, and _H_ is the parity-check matrix given in (3.2). Thus:

\(\mathbf{s}_i^T=\sum_{j=1}^kA_{ij}\mathbf{v}_j^T+\mathbf{v}_{k+i}^T=\sum_{j=1}^kA_{ij}\mathbf{e}_j^T+\mathbf{e}_{k+i}^T,\) (4.2)

for each _i_=1_,...,m_.

Next, we present Algorithm 1, which corrects a single symbol error when \(m\ge 2\).

Note that if the syndrome vector **s** is zero, then no error has occurred. In this case, the algorithm returns **c**=**v**.

**Example 4.1.** Let \(p(x)=x^3+x^2+1\in\mathbb{F}_2[x]\) be a primitive polynomial with a primitive element \(\alpha\in\mathbb{F}_{2^3}\). The superregular Vandermonde matrix and the Frobenius companion matrix are, respectively, given by

\(A=\left[\begin{array}{ c c }
1 & 1 \\
\alpha & \alpha^2
\end{array}\right]\text{and}C=\left[\begin{array}{ c c c }
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 1
\end{array}\right].\)

Thus, according to (3.2), we can construct an MDS array code C with parameters \[4,2,3\] over \(\mathbb{F}_2^3\) with parity-check matrix:

\(H=\left[\begin{array}{ c c }
I_3 & I_3 \\
C & C^2
\end{array}\right]I_6\right]\)

