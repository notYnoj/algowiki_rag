where I(_i_) is the set of the indices for the cells related to the computation of the local residual \(\mathcal{R}_i^\mathrm{hydro}\left(\mathbf{U}^m\right)\). Once the Newton correction \(\delta U_i^m\) is obtained, the solution is updated by<tbc>

\(U_i^{m+1}=U_i^m+\tau\delta U_i^m,\) (51)

<tbc>where \(\tau\) is a relaxation parameter often set as 1. The closed-form expression of the Jacobian \(\partial\mathcal{R}_i^\mathrm{hydro}/\partial U_j\) can be obtained by the chain rule, but the result is usually complicated and depends on the choice of the numerical flux and the implementation of boundary conditions. Therefore, instead of deriving the Jacobian analytically, a numerical differentiation method is applied to evaluate the entries of the Jacobian matrix as

\(\frac{\partial\mathcal{R}_{i,l}^\mathrm{hydro}\left(\mathbf{U}^m\right)}{\partial U_{j,k}}\approx\frac{1}{\epsilon}\left(\mathcal{R}_{i,l}^\mathrm{hydro}\left(\mathbf{U}^m+\epsilon\mathbf{e}\right)-\mathcal{R}_{i,l}^\mathrm{hydro}\left(\mathbf{U}^m\right)\right),\) (52)

where \(\partial\mathcal{R}_{i,l}^\mathrm{hydro}/\partial U_{j,k}\) denotes the derivative of the _l_th component of the vector \(\mathcal{R}_i^\mathrm{hydro}\) with respect to the _k_th component of the vector _U<sub>j</sub>_. The unit vector **_e_** is of the same length as **_U_**, with its only non-zero entry positioned where _U<sub>j,k</sub>_ appears in **_U_**. The parameter \(\epsilon\) is given by \(\epsilon=\epsilon_1U_{j,k}^m+\epsilon_2\), where the scale factor \(\epsilon_1=10^{-6}\) and the small perturbation \(\epsilon_2=10^{-8}\).

Since the Jacobian matrix may be singular, a suitable regularization is necessary to improve the robustness of the linear solver. Unlike the problems considered in \[31-33\], the hydrodynamic system (10) is not closed by itself but relies on the constitutive variables \(\sigma\) and **_q_** provided by the high-order moment solution. These variables depend implicitly on the Knudsen number _Kn_, and the resulting hydrodynamic system therefore inherits this dependence. Accordingly, in addition to the regularization based on the \(\ell^2\) norm of the local residual, _Kn_ is also incorporated into the regularization, leading to the following modified Newton iteration

\(\eta\left(Kn+\|\mathcal{R}_i^\mathrm{hydro}\left(\mathbf{U}^m\right)\|_\ell^2\right)\delta U_i^m+\sum_{j\in\mathcal{I}\left(i\right)}\frac{\partial\mathcal{R}_i^\mathrm{hydro}\left(\mathbf{U}^m\right)}{\partial U_j}\delta U_j^m=-\mathcal{R}_i^\mathrm{hydro}\left(\mathbf{U}^m\right),\) (53)

where \(\eta\) is a positive constant parameter and is set to 4 in the numerical tests unless otherwise specified.

Combining (53) on all cells, a linear system for all the unknowns over the computational domain can be rewritten as

\(\mathbf{J}\delta\mathbf{U}^m=-\mathbf{R}^m,\) (54)

where **_J_** is the regularized Jacobian matrix, and \(\delta\mathbf{U}^m\) and **_R_**_<sup>m</sup>_ are vectors of \(\delta U_i^m\) and \(\mathcal{R}_i^\mathrm{hydro}\left(\mathbf{U}^m\right)\), respectively. To solve the linear system (54) efficiently, the geometric multigrid method \[31, 34\] is adopted, with the block LU-SGS method \[35\] employed as the smoother on each grid level to damp high-frequency errors. A _V_ -cycle iteration with two pre- and post-smoothing steps is used in the implementation. The total number of grid levels is chosen such that the coarsest grid consists of 8 cells in the one-dimensional case and \(8\times 8\) cells in the two-dimensional case \[21\]. With such a coarsest grid, the substantially reduced number of degrees of freedom (DOF) allows the problem to be solved accurately at a relatively low computational cost.

One step of the Newton-multigrid method is summarized in **Algorithm 3**. The geometric multigrid method is employed as the inner linear solver in Step 2, where only a few multigrid iterations are performed. In the present work, two multigrid iterations per Newton iteration are used to balance computational cost and convergence efficiency.

**Algorithm 3** One step of the Newton-multigrid iteration for the hydrodynamic equations

**Input:** Grid, **_U_**_<sup>m</sup>_<br>
**Output:** The new approximation **_U_**<sup>_m_+1</sup> denoted by **_U_**<sup>_m_+1</sup>=Newton (**_U_**_<sup>m</sup>_)

1: Construct the regularized Jacobian matrix **_J_** using (52) and (53);

2: Solve the linear system (54) using the geometric multigrid method to obtain \(\delta\mathbf{U}^m\);

3: Update \(U_i^{m+1}\) using \(U_i^{m+1}=U_i^m+\tau\delta U_i^m\) on every cell;

