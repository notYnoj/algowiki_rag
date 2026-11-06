**Theorem 3.5** _For all_ \(\mathbf{n}\in\mathbb{N}^d\) _and_ \(r\in\mathbb{N}\)_, it holds that_

\(S_{\mathbf{n},r}=Q_{\mathbf{n},r}\Lambda_{\mathbf{n},r}Q_{\mathbf{n},r},\)

_where_ \(\Lambda_{\mathbf{n},r}\) _is block diagonal and its_ \(r\times r\) _diagonal blocks are given by the d-level DST of the first block column (or, equivalently, the first block row) of S<sub>**n**,r</sub>._

All the properties established after Theorem 3.4 for block circulant matrices extend to the multi-level block \(\tau\) setting, once the necessary adaptations are made. In particular, any multi-level block \(\tau\) matrix is real and, when the generating blocks _A<sub>**k**</sub>_ are symmetric, its spectrum is the union of the spectra of the \(r\times r\) diagonal blocks of \(\Lambda_{\mathbf{n},r}\), which are obtained in explicit form by applying the DST to its first block column, while the corresponding invariant subspaces are spanned by the columns of _Q<sub>**n**,r</sub>_. Moreover, the fundamental matrix operations, including matrix-vector multiplication, inversion, the solution of linear systems, and spectral computation, can be performed with a sequential computational cost of _O(N_(**_n_**)log_N_(**_n_**)), or in _O_(log_N_(**_n_**)) steps within a parallel computational framework, with hidden constants depending on the block size _r_.

Recently, \(\tau\) preconditioners have gained renewed attention for solving FDEs. Li and Hon \[77\] developed multilevel tau preconditioners for symmetrized multilevel Toeplitz systems arising from space-FDEs, providing a comprehensive GLT-based analysis of their spectral properties. Building on this work, Hon, Li, Sormani, Krause, and Serra-Capizzano \[54\] introduced symbol-based multilevel block \(\tau\) preconditioners for general multilevel block Toeplitz systems, establishing a rigorous GLT framework for analyzing their asymptotic spectral behavior. These developments demonstrate that \(\tau\)-preconditioners remain a powerful tool for structured linear systems, particularly in the fractional diffusion setting.

## 3.5 Hankel matrices

Given \(\mathbf{n}\in\mathbb{N}^d\) and \(r\in\mathbb{N}\), a matrix of the form

\(H_\mathbf{n}:=[A_{\mathbf{i}+\mathbf{j}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r},\)

with blocks \(A_\mathbf{k}\in\mathbb{C}^{r\times r}\), where the block in position (**_i_**_,**j**_) depends only on the sum **_i_**+**_j_**, is known as a multi-level block (or _d_-level _r_-block) Hankel matrix.

In practice, it can be interpreted as a mirrored Toeplitz structure. In the one- dimensional case, i.e., for _d_=1 and **_n_**=_n_, a one-level (uni-level) _r_-block Hankel matrix is defined by the property that its blocks are constant along the block anti- diagonals:

\(H_n=\left[A_{i+j}\right]_{i,j=1}^n=\left[\begin{array}{ c c c c c c }
A_2 & A_3 & A_4 & \cdots & A_{n+1} \\
A_3 & A_4 & & \ddots & \vdots \\
A_4 & & \ddots & & A_{2n-2} \\
\vdots & \ddots & & A_{2n-2} & A_{2n-1} \\
A_{n+1} & \cdots & A_{2n-2} & A_{2n-1} & A_{2n}
\end{array}\right]\in\mathbb{C}^{nr\times nr}.\)

