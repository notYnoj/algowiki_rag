with \(\hat{d}=\int_\Omega a(x)\) and _d=d<sub>N</sub>_ converging to \(\hat{d}\) as _N_ tends to infinity. As a consequence

\(\{P_{N,M}^{-1}A_{\alpha,N,M}\}_{N,M}\sim_\mathrm{GLT}\frac{\gamma^*a(x)f_\alpha(\xi_1)+q_\theta(\xi_3)}{\gamma^*\hat{d}f_\alpha(\xi_1)+q_\theta(\xi_3)},\)

by using axiom GLT 3, part 4 and part 3.

Notice that this GLT symbol is equal to 1 in the constant coefficient case since \(a=\hat{d}\), so ensuring a clustering at 1 for the preconditioned matrix sequence.

## 8.3 Preconditioning strategy: 2D space setting

In the two-dimensional case, the spatial discretization yields a two-level Toeplitz structure, while the temporal discretization adds a further level so that a three-level matrix is obtained, in the all-at-once formulation. To construct an efficient preconditioner for this system, we approximate only the spatial part using a multilevel circulant matrix, while the temporal block \(Q_{\theta,M}\) remains unchanged. The spatial operator \(G_{\alpha,\mathbf{n}}\) is the diagonal sampling matrix _D_**<sub>n</sub>**(_a_) multiplied with the two-level Toeplitz matrix<tbc>

\(U_{\alpha,\mathbf{n}}=\gamma_1\overline{G_{\alpha_1,N_1}}\otimes I_{N_2}+I_{N_1}\otimes\gamma_2\overline{G_{\alpha_2,N_2}}.\)

<tbc>To form the preconditioner, we replace \(U_{\alpha,\mathbf{n}}\) with its two-level circulant approximation

\(C_{\alpha,\mathbf{n}}=\gamma_1C_{\alpha_1,N_1}\otimes I_{N_2}+I_{N_1}\otimes\gamma_2C_{\alpha_2,N_2},\)

where \(C_{\alpha_r,N_r}\), _r_=1,2 are the circulant matrices already considered in the one- dimensional case, i.e., \(C_{\alpha_r,N_r}\in\{\widetilde{C}_{\alpha_r,N_r},\widehat{C}_{\alpha_r,N_r}\}\).

Since the constants \(\gamma_1=\Delta t/(\Delta x)^{\alpha_1}\) and \(\gamma_2=\Delta t/(\Delta y)^{\alpha_2}\) are sufficiently large, the circulant approximation is applied only to the spatial blocks, while the time stepping matrix \(Q_{\theta,M}\) is left unchanged. As before, to preserve the circulant structure, the diagonal sampling matrix _D_**<sub>n</sub>**(_a_) is replaced by the spatial average of the diffusion coefficient<tbc>

\(d=\frac{1}{N_1N_2}\sum_{i_1=1}^{N_1}\sum_{i_2=1}^{N_2}a_{i_1,i_2},\)

<tbc>and the preconditioner is defined as

\(\widetilde{P}_{\alpha,\mathbf{n},M}=d\widetilde{C}_{\alpha,\mathbf{n}}\otimes I_M+I_\mathbf{n}\otimes Q_{\theta,M},\) (8.39)

or

\(\widehat{P}_{\alpha,\mathbf{n},M}=d\widehat{C}_{\alpha,\mathbf{n}}\otimes I_M+I_\mathbf{n}\otimes Q_{\theta,M},\) (8.40)

where, clearly, it holds

\(C_{\alpha,\mathbf{n}}=F_\mathbf{n}^*\Lambda_{\alpha,\mathbf{n}}F_\mathbf{n}\)

with \(C_{\alpha,\mathbf{n}}\in\{\widetilde{C}_{\alpha,\mathbf{n}},\widehat{C}_{\alpha,\mathbf{n}}\}\), \(F_\mathbf{n}=F_{N_1}\otimes F_{N_2}\) and \(\Lambda_{\alpha,\mathbf{n}}=\gamma_1\Lambda_{\alpha_1,N_1}\otimes I_{N_2}+I_{N_1}\otimes\gamma_2\Lambda_{\alpha_2,N_2}\). Now we give only the statement of results regarding the invertibility of _P_, the computation cost related to the chosen preconditioner, and the clustering results for the related preconditioned matrix sequence. The tools and the structure of the proofs follow verbatim those of Section 8.2.

