Equation 8 establishes that the continuum-feature constraint Gram matrix is the analytical expectation of the corresponding finite-feature Gram matrix. Thus, CFKS replaces the finite feature count and individual center realization with a deterministic kernel defined by the prescribed center distribution and Gaussian widths.

For Gaussian RBF features with centers uniformly distributed over bounded intervals, the expectation defining the continuum-feature mean kernel can be evaluated analytically. In one dimension, the resulting expression consists of a Gaussian factor multiplied by error-function terms that account for the finite support of the center distribution. When the center distribution is a product of independent uniform distributions over a Cartesian box, the multidimensional mean kernel is obtained as the product of the corresponding one-dimensional kernels. The complete derivation and closed-form expressions are provided in Appendix B.

An important property of the continuum-feature mean kernel is that its derivatives can be obtained directly from the analytical kernel expression. To describe derivatives of arbitrary order, let **_p_**=(_p_<sub>1</sub>_,...,p<sub>d</sub>_) and **_q_**=(_q_<sub>1</sub>_,...,q<sub>d</sub>_) denote two multi-indices, where _p<sub>r</sub>_ and _q<sub>r</sub>_ are nonnegative integers specifying the orders of partial differentiation with respect to the _r_th coordinates of **z** and \(\mathbf{z}'\), respectively. The operators \(D_\mathbf{z}^\mathbf{p}\) and \(D_{\mathbf{z}^\prime}^\mathbf{q}\) denote the corresponding mixed partial derivatives with respect to the first and second kernel arguments.

For the smooth Gaussian features and bounded center distributions considered here, differentiation can be interchanged with expectation. Therefore,

\(D_\mathbf{z}^\mathbf{p}D_{\mathbf{z}^\prime}^\mathbf{q}k_\rho(\mathbf{z},\mathbf{z}')=\mathbb{E}_{\theta\sim\rho}\left[D_\mathbf{z}^\mathbf{p}\phi_\theta(\mathbf{z})D_{\mathbf{z}^\prime}^\mathbf{q}\phi_\theta(\mathbf{z}')\right],\) (9)

which shows that the mixed derivatives of the mean kernel are equal to the analytical averages of the corresponding products of differentiated Gaussian RBF features.

In particular, for the prescribed linear differential operator L appearing in the governing PDE,

\(\mathcal{L}_\mathbf{z}\mathcal{L}_{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}')=\mathbb{E}_{\theta\sim\rho}\left[(\mathcal{L}\phi_\theta)(\mathbf{z})(\mathcal{L}\phi_\theta)(\mathbf{z}')\right],\) (10)

where L**<sub>z</sub>** and \(\mathcal{L}_{\mathbf{z}^\prime}\) indicate application of the differential operator to the first and second kernel arguments, respectively. On the right-hand side, \((\mathcal{L}\phi_\theta)(\mathbf{z})\) denotes the operator applied to a Gaussian RBF feature and evaluated at **z**, with the analogous interpretation for the second argument.

Equation 10 establishes that the operator-applied mean kernel is exactly the population Gram kernel associated with the corresponding operator-applied Gaussian RBF features. Hence, the differential-operator kernels required by CFKS follow directly from the continuum-feature construction rather than being introduced independently.

## 2.2 Linear CFKS formulation

We now construct the CFKS approximation for the linear differential problem introduced in eq. 1. Recall that \(\ell_i\), with _i_=1_,...,N_, denotes the linear functional associated with the _i_th governing PDE, boundary, or initial constraint, and _N_ is the total number of discrete constraints. Each functional includes the appropriate differential or evaluation operation at its prescribed constraint location.

Let \(k_\rho\) denote the continuum-feature mean kernel defined in eq. 7. The CFKS approximation is expressed in the kernel representer form

\(u_h(\mathbf{z})=\sum_{j=1}^N\alpha_j\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'),\) (11)

where _u<sub>h</sub>_ is the kernel approximation to the unknown solution, **z** is an arbitrary evaluation point, \(\alpha_j\) is the coefficient associated with the _j_th constraint, and \(\mathbf{z}'\) is the second argument of the kernel. The superscript on \(\ell_j^{\mathbf{z}^\prime}\) indicates that the _j_th constraint functional acts on the second kernel argument, including evaluation at the location associated with that constraint. When the functional contains derivatives, these are applied before evaluating at the corresponding constraint location.

The representer formulation follows from the connection between finite-feature models and their continuum-kernel counterparts, as detailed in Appendix A.

Applying each constraint functional \(\ell_i\) to eq. 11 produces the linear system associated with the discrete PDE and physical conditions. Its coefficient matrix is the operator Gram matrix \(K_{\ell\ell}\), with entries

\((K_{\ell\ell})_{ij}=\ell_i^\mathbf{z}\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'),i,j=1,\dots,N,\) (12)

where \(\ell_i^\mathbf{z}\) and \(\ell_j^{\mathbf{z}^\prime}\) act on the first and second kernel arguments, respectively. Both functionals include evaluation at their prescribed constraint locations. Thus, \((K_{\ell\ell})_{ij}\) represents the interaction between the _i_th and _j_th constraint functionals through the continuum-feature mean kernel.

