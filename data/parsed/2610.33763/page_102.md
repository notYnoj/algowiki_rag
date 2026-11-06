the eigenvalues of \(P_\widetilde{\mathbf{N}}\) coincide with those of its diagonal blocks. Therefore, \(P_\widetilde{\mathbf{N}}\) is invertible.<br>
The linear systems with matrix \(P_\widetilde{\mathbf{N}}\) that have to be solved when applying the preconditioned GMRES to the original linear systems can be solved by standard block forward elimination. However we have to specify how the linear systems having as coefficient matrices the diagonal blocks of \(P_\widetilde{\mathbf{N}}\) are solved. Indeed the diagonal blocks have the expression \(\gamma_0I_\mathbf{n}+D_\mathbf{n}(a)B_\mathbf{n}\) and for them we can use several standard preconditioners such as \(\gamma_0I_\mathbf{n}+\hat{a}B_\mathbf{n}\) which is of Toeplitz lower triangular form, with \(\hat{a}\) being the integral average of the function _a_, or the standard circulant preconditioner constructed as \(\gamma_0I_\mathbf{n}+\hat{a}S(B_\mathbf{n})\), _S(B_**<sub>n</sub>**) being a Strang-like circulant approximation of _B_**<sub>n</sub>**, constructed by preserving the first column of _B_**<sub>n</sub>**. The computational features of these choice are discussed at the end of Section 7.4.<br>
The preconditioning strategies developed in this chapter are informed by recent advances in preconditioning for all-at-once systems arising from evolutionary PDEs. Huang, Fung, Hon, and Lin \[56\] introduced an efficient preconditioner for evolutionary PDEs discretized with the \(\theta\)-method in time, providing a comprehensive analysis of its spectral properties. Their approach, which leverages the structure of the time-stepping matrix, is complementary to the block triangular preconditioner proposed here for the ISP in a two-dimensional FDE. Additionally, the matching Schur complement preconditioning technique of Lin, Ke, Hon, and Ng \[81\] for discrete time fractional diffusion ISPs demonstrates the effectiveness of exploiting the block structure of all-at-once systems in the fractional setting.

## 7.3.2 GLT preconditioning analysis

The following theorem establishes that \(P_\widetilde{\mathbf{N}}\) has the same GLT symbol, and consequently the same singular value distribution, as the original coefficient matrix sequence.

**Theorem 7.4** _With_ \(P_\widetilde{\mathbf{N}}\) _defined in_ (7.22)_, assume that_<tbc>

\(\frac{\alpha_m}{\beta_{n_1}}\rightarrow\nu_1,\frac{\alpha_m}{\beta_{n_2}}\rightarrow\nu_2,\text{\textit{as}}m,n_1,n_2\rightarrow\infty,\)

<tbc>_with_ \(\nu_1\neq 0\) _or_ \(\nu_2\neq 0\)_. Then, it holds_

\(\{P_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_{\mathrm{GLT},\sigma} h_\xi(\theta_1)+a(x,y)\left(\nu_1g_{\eta_1}(\theta_2)+\nu_2g_{\eta_2}(\theta_3)\right),\)<br>
\((\theta_1,\theta_2,\theta_3)\in[-\pi,\pi]^3,(x,y)\in[0,1]^2,\)

_where_ \(h_\xi\) _is given in Theorems 7.1 and_ \(g_{\eta_1}\) _and_ \(g_{\eta_2}\) _are given in Theorems 7.2._

**Proof:** The result follows from the same GLT arguments used in the proof of Theorem 7.3.

The GLT symbol and the singular value distribution of the preconditioned matrix sequence follow as a corollary of Theorems 7.3 and 7.4, by exploiting the algebra properties in GLT 3. However, they can also be derived in a more general setting, without assuming specific conditions on the discretization parameters, as shown in the following theorem. Moreover, the eigenvalue distribution can be characterized.

