**Algorithm 1** Naive Pauli decomposition algorithm.

**Require:** Square matrix _A_, tolerance \(\epsilon\).<br>
**Ensure:** List of Pauli terms _P_ and coefficients _C_.

1: \(N\leftarrow\text{dimension}(A)\)

2: \(n\leftarrow\lceil\mathrm{log}_2(N)\rceil\)

3: **if** \(N\neq 2^n\) **then**

4: Pad _A_ with zeros to size \(2^n\times 2^n\).

5: **end if**

6: Empty array of P, C

7: **for** each \(\sigma\in\{I,X,Y,Z\}^{\otimes n}\) **do**

8: \(P_\text{curr}\leftarrow\sigma_1\otimes\sigma_2\otimes\cdots\otimes\sigma_n\)

9: \(c\leftarrow\frac{1}{2^n}\mathrm{Tr}(P_\text{curr}\cdot A)\)

10: **if** \(|c|\ge\epsilon\) **then**

11: Append _c_ to _C_

12: Append _P_curr to _P_

13: **end if**

14: **end for**

15: **return** _P,C_

\(\alpha_{r,s}=\frac{i^{-|r\wedge s|}}{2^n}\sum_{q=0}^{2^n-1}a_{q\oplus r,q}(H^{\otimes n})_{q,s}.\) (5)

where \(a_{q\oplus r,q}\) denotes the XOR column permutation of the element _a<sub>r,q</sub>_ in the input matrix _A_, and _H_ is the standard Hadamard gate with matrix expression \(H=\left[\begin{array}{ c }
1 \\
1
\end{array}\right]\).

To further improve scalability, we implemented shared memory for multiple workers so that the system stores the input matrix once while all cores compute Pauli terms and coefficients in an embarrassingly parallel manner.

By adopting FWHT, the computational complexity is reduced to O(_n_<sup>2</sup>log_n_) with fixed auxiliary memory for the decomposition. This algorithm scales better than the naive approach and reduces the matrix-initialization bottleneck that often dominates practical QLSA workflows. We evaluate its performance in Section IV. The detailed algorithm is shown in Algorithm 2.

## C. Minimization of decomposition terms

Even though the Pauli strings and coefficients can be generated efficiently through the improved algorithm, the number of Pauli terms increases the total number of circuits executed on the quantum computer, leading to inefficiency in VQLS. Therefore, a decomposition method with fewer terms is desirable for better scalability. In this paper, we use a decomposition that requires at most two terms for an arbitrary square matrix of size \(2^n\times 2^n\). This decomposition is based on the singular value decomposition (SVD) and expresses _A_ as the sum of two unitaries with equal weights, as derived below.

For an arbitrary square real matrix _A_, we apply a single SVD,

\(A=U\Sigma V^T,\) (6)

where _U_ and _V_ are orthogonal (and hence unitary over the reals), and \(\Sigma\) is a diagonal matrix of non-negative singular<tbc>

<tbc>**Algorithm 2** Fast Walsh-Hadamard transform-based Pauli Decomposition

**Require:** \(A=(a_{p,q})\in\mathbb{C}^{2^n\times 2^n}\)

**Ensure:** Pauli coefficients \(\alpha_{r,s}\) (stored in-place)

1: **for** _q_=0 to 2_<sup>n</sup>_-1 **do**

2: **XOR permutation:**

3: **for** _r_=0 to 2_<sup>n</sup>_-1 **do**

4: \(a_{r,q}\leftarrow a_{r\oplus q,q}\)

5: **end for**

6: **end for**

7: **for** _r_=0 to 2_<sup>n</sup>_-1 **do**

8: **Walsh-Hadamard transform on row** _r_**:**

9: \(a_{r,*}\leftarrow H^{\otimes n}a_{r,*}\)

10: **end for**

11: **for** _r,s_=0 to 2_<sup>n</sup>_-1 **do**

12: **Phase and normalization:**

13: \(a_{r,s}\leftarrow\frac{i^{-|r\wedge s|}}{2^n}a_{r,s}\)

14: **end for**

values \(\sigma_j\). To map these singular values onto the complex unit circle, we first normalize by the spectral norm \(\|A\|_2\),

\(\tilde{\Sigma}=\frac{\Sigma}{\|A\|_2},\) (7)

so that all entries of \(\tilde{\Sigma}\) are bounded by 1. We then construct two diagonal matrices by introducing an imaginary phase,

\(D_\pm=\tilde{\Sigma}\pm i\sqrt{I-\tilde{\Sigma}^2}.\) (8)

Since \(\tilde{\sigma}_j^2+(1-\tilde{\sigma}_j^2)=1\), every diagonal element of \(D_\pm\) has magnitude 1, so _D_<sub>+</sub> and _D_<sub>-</sub> are unitary. Defining \(U_\pm=UD_\pm V^T\), each \(U_\pm\) is unitary as a product of three unitaries. Summing cancels the imaginary part,

\(U_++U_-=U(2\tilde{\Sigma})V^T=\frac{2A}{\|A\|_2},\) (9)

and isolating _A_ yields the exact two-term LCU,

\(A=\frac{\|A\|_2}{2}U_++\frac{\|A\|_2}{2}U_-.\) (10)

With this decomposition, we only need one extra preparation qubit along with the encoding qubits of the two unitaries for the computation and lead to the minimal number of LCU terms. A thorough analysis is described in Section IV.

## D. Quantum Ansatz Selection

The form of the particular ansatz circuit is also the key to capturing the essential physics of the state vector. There have been several works in the literature providing guidance on the choice of the ansatz for variational circuits. The work by \[26\] elaborates the choice based on quantitative metrics for expressibility and entangling capability of the ansatz. For the current implementation, we use amplitude encoding for representing \(|b\rangle\).

In this work, we analyze several quantum ansatz families with different expressibility to study the trade-offs between<tbc>

