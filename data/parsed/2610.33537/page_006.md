A first-order scheme can be obtained by setting all slopes **_s_**_<sub>i</sub>_ and \(d_{i,\alpha}\) to 0, while a second-order discretization is achieved by employing

\(s_i=\frac{U_{i+1}-U_{i-1}}{2\Delta x},d_{i,\alpha}=\frac{f_{i+1,\alpha}-f_{i-1,\alpha}}{2\Delta x}.\) (16)

Finally, appropriate boundary conditions are necessary to complete the discretization. The Maxwell boundary condition is employed throughout our numerical experiments. We refer to \[17, 18\] for details on such boundary conditions.

## 2.4. FIM framework

For convenience, the discretization (11) over the _i_th cell is rewritten in the residual form<tbc>

\(\mathcal{R}_i(f)=0,\) (17)

<tbc>where R_<sub>i</sub>_(**_f_**) denotes the local residual corresponding to the left-hand side of (11), and **_f_** is the global vector composed of all cell-averaged distribution functions _f<sub>i</sub>_. The above discretization results in a nonlinear system coupling all unknowns, including **_u_**_<sub>i</sub>_, \(\theta_i\), and \(f_{i,\alpha}\) for _i_=0,1_,...,N<sub>x</sub>_-1 and \(|\alpha|\le M\). A simple relaxation method for solving this nonlinear system is the Richardson iteration given by<tbc>

\(f_i^{n+1}=f_i^n+\omega\mathcal{R}_i\left(f^n\right),\) (18)

<tbc>where the superscript _n_ is the index for iteration steps. The relaxation parameter \(\omega\) is selected according to the CFL condition<tbc>

\(\omega=min_i\omega_i,\) (19)

<tbc>where the local relaxation parameter \(\omega_i\) satisfies

\(\omega_i\left(\frac{|u_{i,1}^n|+C_{M+1}\sqrt{\theta_i^n}}{\Delta x}\right)<1.\) (20)

Here, \(u_{i,1}^n\) is the first component of the vector \(u_i^n\), and _C_<sub>_M_+1</sub> is the maximal root of the Hermite polynomial of degree _M_+1. Under Grad’s expansion, the left- and right-hand sides of (18) are represented in different function spaces, namely, \(\mathcal{F}_M^{[u_i^{n+1},\theta_i^{n+1}]}\) and \(\mathcal{F}_M^{[u_i^n,\theta_i^n]}\), respectively. Therefore, the evaluated right-hand side should be projected onto \(\mathcal{F}_M^{[u_i^{n+1},\theta_i^{n+1}]}\) using the projection mentioned in the previous subsection. The Richardson iteration (18) can be interpreted as an explicit Euler scheme with the relaxation parameter \(\omega\) serving as the pseudo-time step. As _Kn_ decreases, its convergence becomes increasingly slower, resulting in poor efficiency in the near-continuum flow regime.

To accelerate the convergence, the FIM method proposed in \[23\] employs an alternating iteration framework consisting of a moment stage for the high-order moment system (9) and a hydrodynamic stage for the hydrodynamic equations (10). Specifically, in the moment stage, \(\gamma_1\) moment iterations are performed starting from the current moment solution **_f_**_<sup>n</sup>_ to obtain an intermediate approximation \(\tilde{f}\). In the hydrodynamic stage, using the macroscopic quantities \(\tilde{\rho}\), \(\tilde{u}\), and \(\tilde{\theta}\) extracted from \(\tilde{f}\) as the initial guess, at most \(\gamma_2\) hydrodynamic iterations are performed. The resulting macroscopic solution is subsequently used to update \(\tilde{f}\) and construct the new moment solution **_f_**<sup>_n_+1</sup>. The above procedure is summarized in **Algorithm 1**. In \[23\], the Richardson iteration (18) or its symmetric Gauss-Seidel (SGS) version is used in the moment stage, while a similar iterative scheme with a consistent spatial discretization is employed in the hydrodynamic stage, as described below.

Let _U<sub>i</sub>_ represent the cell average of _U_ over the _i_th grid cell R_<sub>i</sub>_. Applying the finite volume method to (10) gives<tbc>

\(\mathcal{R}_i^\mathrm{hydro}(U):=-\frac{1}{\Delta x}\left[\hat{F}_{i+1/2}\left(U_i^+,U_{i+1}^-,\sigma_i^+,\sigma_{i+1}^-,q_i^+,q_{i+1}^-\right)-\hat{F}_{i-1/2}\left(U_{i-1}^+,U_i^-,\sigma_{i-1}^+,\sigma_i^-,q_{i-1}^+,q_i^-\right)\right]=0,\) (21)

<tbc>where \(\mathcal{R}_i^\mathrm{hydro}(U)\) denotes the local hydrodynamic residual, **_U_** consists of all cell averages _U<sub>i</sub>_, and \(U_i^\pm\) are reconstructed according to (14). Similarly, the interface values of the stress tensor \(\sigma\) and heat flux **_q_** are reconstructed as<tbc>

\(\sigma_i^+=\tilde{\sigma}_i+\frac{\Delta x}{2}\tilde{s}_i,\sigma_i^-=\tilde{\sigma}_i-\frac{\Delta x}{2}\tilde{s}_i,q_i^+=\tilde{q}_i+\frac{\Delta x}{2}\tilde{s}_i,q_i^-=\tilde{q}_i-\frac{\Delta x}{2}\tilde{s}_i,\) (22)

