<tbc>convergence of our proposed preconditioner is analyzed. Numerical tests are given in Section 3 to demonstrate the matrix-size independent convergence rate of the proposed preconditioned MINRES solver.

## 2. Main results

In this section, we discuss properties of our proposed ABAC preconditioner \(\mathcal{P}_\alpha\) defined by (1.9) and the fast implementation for the proposed preconditioned method.

### 2.1. Preliminaries for convergence analysis of the preconditioned method

In this subsection, we introduce preliminaries for the linear convergence rate analysis of MINRES solver for the preconditioned system.

Denote by _GL(K_) the set of all \(K\times K\) invertible complex matrices. For a square matrix **A**, denote by \(\sigma(\mathbf{A})\), the spectrum of **A**. Define

\(\mathcal{Q}(k):=\{\mathbf{A}\in\mathbb{C}^{K\times K}|\sigma(\mathbf{A})\subset\mathbb{C}\backslash(-\infty,0]\}.\)

Clearly, \(\mathcal{Q}(K)\subset GL(K)\). For a complex number _z_, denote by \(\Re(z)\) and \(\unknown(z)\), the real part and the imaginary part of _z_, respectively.

**Lemma 1.** _For any_ \(\alpha\in[0,1)\)_, it holds_ \(\mathcal{C}_\alpha\in\mathcal{Q}(mn)\subset GL(mn)\).

**Proof:** See the proof in Appendix **A**.

**Remark 2.** _Clearly, Lemma 1 guarantees that the preconditioner_ \(\mathcal{P}_\alpha\) _is invertible. Moreover, from its proof, we see that the eigenvalues of Strang’s \[40\] block circulant preconditioner_ C<sub>1</sub> _are of form_ \(\mu=2cos(\omega_k)[\lambda cos(\omega_k)-1]+\mathbf{i}2sin(\omega_k)[\lambda cos(\omega_k)-1]\) _and some of which are equal to zero when_ \(\lambda cos(\omega_k)-1=0\)_. Therefore, such an existing block circulant preconditioner may be singular and thus not applicable in general._

Denote by UTT(**v**), the upper triangular Toeplitz matrix with **v** as its first column. Define the _i_-th order Jordan block \(J_i(\lambda)\) as<tbc>

\(J_i(\lambda):=\left\{\begin{array}{ c c c c }
\lambda, & i=1, &  &  \\
\lambda & 1 &  &  \\
 & \lambda & \ddots &  \\
 &  & \lambda & 1 \\
 &  &  & \lambda
\end{array}\right]\in\mathbb{C}^{i\times i},i>1.\)

