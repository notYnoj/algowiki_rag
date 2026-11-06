<tbc>with<tbc>

\(p(\theta):=\sum_{k=0}^{n-1}\omega^\frac{k}{n}a_ke^{ik\theta},\)

<tbc>and the adapted Fourier matrix containing the eigenvectors is defined as

\(F_n^\omega:=D_n^\omega F_n,D_n^\omega:=\mathrm{diag}_{k=0,\dots,n-1}\left(\omega^{-\frac{k}{n}}\right).\)

Observe that the eigenvalues of \(C_n^\omega\) are obtained by computing the matrix-vector product \(F_n^\omega\mathbf{c}\), where **c** denotes the first column of \(C_n^\omega\).<br>
Extending the computation of the matrix-vector product to \(\omega\)-circulant matrices, as well as adapting all the algorithms discussed in the previous subsection, is immediate and requires only minor modifications:

1. Compute \(\mathbf{y}=(D_n^\omega F_n)^{-1}\mathbf{x}=F_n^*(D_n^\omega)^{-1}\mathbf{x}\) using the FFT, which requires _O(n_log_n_) flops;<tbc>

2. Compute \(\mathbf{z}=\Lambda_n^\omega\mathbf{y}\), in _O(n_) flops;<tbc>

3. Compute \(D_n^\omega F_n\mathbf{z}\) via the FFT, again in _O(n_log_n_) flops.

Overall, this sequence of operations leads to a computational cost of _O(n_log_n_) in a sequential implementation, while in a parallel environment it requires _O_(log_n_) steps. Nevertheless, the presence of the parameter \(\omega\) may affect numerical stability. Since _F<sub>n</sub>_ is unitary, the conditioning of the transformation \(D_n^\omega F_n\) depends exclusively on the diagonal scaling \(D_n^\omega\). More precisely, as \(n\rightarrow+\infty\), the condition number of \(D_n^\omega\) approaches \(\mathrm{max}\{|\omega|,|\omega|^{-1}\}\), and therefore becomes unbounded whenever \(\omega\rightarrow 0\) or \(|\omega|\rightarrow\infty\).

Recent developments have extended the use of \(\omega\)-circulant preconditioners to more complex applications. For instance, Fung and Hon \[40\] introduced block \(\omega\)-circulant preconditioners for parabolic optimal control problems, demonstrating their effectiveness in accelerating the convergence of iterative solvers for large-scale all-at-once systems. More recently, Hon, Fung, and Lin \[55\] developed an optimal diagonalization- based preconditioner for parabolic optimal control problems, further showcasing the versatility of circulant-based approaches. These works highlight the continued relevance of \(\omega\)-circulant structures in modern numerical linear algebra.

**Remark 3.3** _In the standard circulant case of Theorem 3.4, the Fourier matrix F<sub>n</sub> is unitary, so_ \(F_n^*=F_n^{-1}\) _and the two notations_ \(F_n\Lambda_nF_n^*\) _and_ \(F_n\Lambda_nF_n^{-1}\) _coincide. For the_ \(\omega\)_-circulant case, the adapted Fourier matrix_ \(F_n^\omega=D_n^\omega F_n\) _is not unitary unless_ \(|\omega|=1\)_, since_ \(D_n^\omega\) _is a non-trivial diagonal scaling. Hence_ \((F_n^\omega)^*\neq(F_n^\omega)^{-1}\) _in general, and the diagonalization must be written as_

\(C_n^\omega=F_n^\omega\Lambda_n^\omega(F_n^\omega)^{-1}.\)

## 3.3.1 Block \(\omega\)-circulant matrices

To set the stage for certain practical applications to the solution of linear systems, we briefly extend the definition and diagonalization of \(\omega\)-circulant matrices to the<tbc>

