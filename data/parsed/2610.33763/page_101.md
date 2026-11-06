As in the one-dimensional case, the matrices \(A_\widetilde{\mathbf{N}}\) are non-Hermitian, and therefore the GLT symbol obtained in Theorem 7.3 directly yields the singular value distribution but does not automatically imply the eigenvalue distribution. The eigenvalue distribution in this setting follows from Theorem 7.5, where we prove that the preconditioned matrix sequence is weakly clustered at one. This clustering result is based on the low-rank perturbation structure of the preconditioned system, which is sufficient to characterize the eigenvalue behavior. For non-Hermitian matrix sequences in general, eigenvalue distributions require additional assumptions, such as Hermitian structure or suitable perturbation arguments; see \[12, 45\]. In the present work, the weak clustering result ensures fast convergence of the preconditioned GMRES method despite the non-Hermitian nature of the coefficient matrices.

**Remark 7.1** _The assumption_ \(\nu_1\neq 0\) _or_ \(\nu_2\neq 0\) _used in Corollary 7.1 and in Theorem 7.3 deserves a bit of attention and few comments since it is used also in the study of the preconditioning; see Theorem 7.4. In fact, if we assume n_<sub>1</sub>∼_n_<sub>2</sub> _i.e._ \(cn_1\le n_2\le Cn_1\) _with c,C universal constants independent of n_<sub>1</sub>_,n_<sub>2</sub>_, the we find the following cases:_

• _when_ \(\eta_1>\eta_2\)_, taking into account the expression in (7.9), (7.12), the given assumption implies_ \(\nu_1>0\) _and_ \(\nu_2=0\);<tbc>

• _when_ \(\eta_2>\eta_1\)_, taking into account the expression in (7.9), (7.12), the given assumption implies_ \(\nu_1=0\) _and_ \(\nu_2>0\);<tbc>

• _when_ \(\eta_2=\eta_1\)_, taking into account the expression in (7.9), (7.12), the given assumption implies_ \(\nu_1>0\) _and_ \(\nu_2>0\) _with_ \(\nu_1=\nu_2>0\) _if n_<sub>2</sub>=_n_<sub>1</sub>+_o(n_<sub>1</sub>);

_Finally, it is worth observing that when n_<sub>1</sub>∼_n_<sub>2</sub> _is violated, the picture becomes more complicate, but it is also a degenerate case since it implies that one space direction is approximated with much more precision than the other._

## 7.3 GLT preconditioning

The current section is divided into two parts. The first contains the proposal and the second the related spectral analysis.

### 7.3.1 Block Triangular preconditioning

In this subsection, we propose block triangular preconditioners \(P_\widetilde{\mathbf{N}}\) for the linear system (7.16), aiming to cluster the eigenvalues of \(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\) around 1. We define

\(P_\widetilde{\mathbf{N}}:=\left[\begin{array}{ c c }
U_m\otimes I_\mathbf{n}+I_m\otimes G_\mathbf{n} & \text{O}_{\mathbf{nm}\times\mathbf{n}} \\
\mathbf{e}_m^T\otimes I_\mathbf{n} & \frac{\lambda}{\alpha_m}G_\mathbf{n}
\end{array}\right].\) (7.22)

Note that both _U<sub>m</sub>_ and _G_**<sub>n</sub>** are invertible, since they are lower triangular matrices with nonzero diagonal entries. The same holds for \(U_m\otimes I_\mathbf{n}+I_m\otimes G_\mathbf{n}\), which is also block lower triangular. Moreover, due to the block triangular structure,<tbc>

