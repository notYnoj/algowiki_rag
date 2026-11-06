We conclude by GLT 3 that

\(\big\{C_N^{(2)}\big\}_N\sim_\mathrm{GLT}\nu a(x)g_\eta(\theta_2).\) (6.13)

Finally, we have

\(C_N^{(3)}=\left[\begin{array}{ c c }
\mathrm{O}_{mn} & -\alpha_m\mathbf{q}\otimes I_n \\
\mathrm{O}_{n\times mn} & \mathrm{O}_n
\end{array}\right]+\left[\begin{array}{ c c }
\mathrm{O}_{mn} & \mathrm{O}_{mn\times n} \\
\mathbf{e}_m^T\otimes I_n & \mathrm{O}_n
\end{array}\right],\)

where each of these components has rank at most _m=o(N_). Therefore,

\(\big\{C_N^{(3)}\big\}_N\sim_\mathrm{GLT}0.\) (6.14)

By summing the contributions in (6.12), (6.13) and (6.14), we find the GLT symbol of the overall coefficient matrix sequence {_A<sub>N</sub>}<sub>N</sub>_ via GLT 3, and then the singular value distribution via GLT 1.

Since the matrices _A<sub>N</sub>_ are non-Hermitian, the GLT symbol obtained in Theorem 6.3 directly implies the singular value distribution via GLT 1. However, the GLT theory alone does not guarantee the eigenvalue distribution. In the present setting, the eigenvalue distribution can be established because the preconditioned matrix sequence is weakly clustered at one, as shown in Theorem 6.5. This clustering result relies on the fact that the perturbation between the preconditioner and the coefficient matrix is of low rank relative to the matrix size, which is sufficient to characterize the eigenvalue behavior in the sense of weak clustering. In general, for non-Hermitian matrix sequences, eigenvalue distributions require additional assumptions, such as Hermitian structure, normality, or suitable perturbation arguments; see \[12, 45\] and references therein.

## 6.3 GLT preconditioning

In the present section, we propose preconditioners _P<sub>N</sub>_ for the linear system (6.9), with the aim of clustering at 1 the eigenvalues of \(\{P_N^{-1}A_N\}_N\). Let us define

\(P_N:=\left[\begin{array}{ c c }
U_m\otimes I_n+I_m\otimes\frac{\alpha_m}{\beta_n}G_n & \mathrm{O}_{nm\times n} \\
\mathbf{e}_m^T\otimes I_n & \frac{\lambda}{\beta_n}G_n
\end{array}\right].\) (6.15)

Note that both _U<sub>m</sub>_ and _G<sub>n</sub>_ are invertible, in consequence of their lower triangular structure with non-zero diagonal elements, and the same is true for \(U_m\otimes I_n+I_m\otimes\frac{\alpha_m}{\beta_n}G_n\), which is also lower triangular. Because of the block triangular structure, the eigenvalues of _P<sub>N</sub>_ are the eigenvalues of the diagonal blocks, therefore _P<sub>N</sub>_ is invertible.

The following theorem proves that {_P<sub>N</sub>}<sub>N</sub>_ has the same GLT symbol, and hence the same singular value distribution, as the coefficient matrix sequence.

**Theorem 6.4** _With P<sub>N</sub> defined in_ (6.15)_, assume that_

\(\frac{\alpha_m}{\beta_n}\rightarrow\nu,\text{\textit{as}}m,n\rightarrow\infty,\)

