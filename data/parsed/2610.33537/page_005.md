form

\(\left\{\begin{array}{ c }
\nabla_x\cdot(\rho u)=0, \\
\nabla_x\cdot(\rho u\otimes u+p\mathbf{I}+\sigma)=0, \\
\nabla_x\cdot(\rho Eu+pu+u\cdot\sigma+q)=0,
\end{array}\right.\) (10)

where \(p=\rho\theta\) is the pressure, **I** is the identity matrix, and \(E=3\theta/2+|u|^2/2\) is the specific total energy.

## 2.3. Spatial discretization of the moment system and linear reconstruction

The hyperbolic moment system (9) of order _M_ is discretized following the unified finite volume method developed in \[7, 17, 18, 29\]. For convenience, only the one-dimensional formulation is presented here, while the extension to two-dimensional problems on rectangular grids is straightforward.

Suppose the spatial domain \(\Omega=(x_L,x_R)\) is partitioned into _N<sub>x</sub>_ uniform grid cells of size \(\Delta x\), where the _i_th cell is denoted by K_<sub>i</sub>_=\[_x_<sub>_i_-1/2</sub>_,x_<sub>_i_+1/2</sub>\]. In each cell K_<sub>i</sub>_, we use _f<sub>i</sub>_(**_v_**) and \(f_i^\pm(v)\) to denote the cell-averaged distribution function and the reconstructed interface distribution functions at \(x_{i\pm 1/2}\), respectively. Then the finite volume discretization of the Boltzmann equation (1) is given by<tbc>

\(-\frac{1}{\Delta x}\left(\bar{F}_{i+1/2}\left(f_i^+,f_{i+1}^-\right)-\bar{F}_{i-1/2}\left(f_{i-1}^+,f_i^-\right)\right)+\mathcal{Q}(f_i)=0.\) (11)

<tbc>Here, \(\bar{F}_{i\pm 1/2}\left(\cdot,\cdot\right)\) are the numerical fluxes at the boundaries of the _i_th grid cell, and Q(_f<sub>i</sub>_) denotes the collision term evaluated using the cell-averaged distribution function _f<sub>i</sub>_. Let us assume that _f<sub>i</sub>_(**_v_**) belongs to the function space \(\mathcal{F}_M^{[u_i,\theta_i]}\), i.e.,<tbc>

\(f_i(v)=\sum_{|\alpha|\le M}f_{i,\alpha}\mathcal{H}_\alpha^{[u_i,\theta_i]}(v),\) (12)

<tbc>where **_u_**_<sub>i</sub>_ and \(\theta_i\) are the local mean velocity and temperature, respectively, so that the relations (7) hold for the coefficients \(f_{i,\alpha}\). Similarly, the numerical fluxes \(\bar{F}_{i\pm 1/2}\left(\cdot,\cdot\right)\) and the collision term Q(_f<sub>i</sub>_) in (11) should be expressed as functions in the same space \(\mathcal{F}_M^{[u_i,\theta_i]}\) as follows

\(\bar{F}_{i\pm 1/2}\left(\cdot,\cdot\right)=\sum_{|\alpha|\le M}\bar{F}_{i\pm 1/2,\alpha}\left(\cdot,\cdot\right)\mathcal{H}_\alpha^{[u_i,\theta_i]}(v),\mathcal{Q}(f_i)=\sum_{|\alpha|\le M}\mathcal{Q}_{i,\alpha}\mathcal{H}_\alpha^{[u_i,\theta_i]}(v),\) (13)

where \(\bar{F}_{i\pm 1/2,\alpha}\left(\cdot,\cdot\right)\) and \(\mathcal{Q}_{i,\alpha}\) are the coefficients. Substituting the expansions (12) and (13) into the system (11) and matching the coefficients of the same basis function \(\mathcal{H}_\alpha^{[u_i,\theta_i]}(v)\), we obtain the finite volume discretization for the hyperbolic moment system (9).

In the present numerical experiments, a modified Harten, Lax and van Leer (HLL) flux, as used in \[18\], is adopted for \(\bar{F}_{i\pm 1/2}\left(\cdot,\cdot\right)\). In order to write the numerical flux in the form (13), all distribution functions involved in (11), including those in neighboring grid cells, need to be represented as members of \(\mathcal{F}_M^{[u_i,\theta_i]}\). This requires a projection onto \(\mathcal{F}_M^{[u_i,\theta_i]}\) for any function in \(\mathcal{F}_M^{[\varpi,\vartheta]}\) if \(\varpi\neq u_i\) or \(\vartheta\neq\theta_i\), regardless of the choice of the numerical flux. An efficient implementation of the required projection, which preserves all moments up to the _M_th order, can be found in \[27\].

It remains to determine the distribution functions on cell boundaries \(f_i^-\) and \(f_i^+\), which are to be constructed as functions in \(\mathcal{F}_M^{[u_i^\cdot,\theta_i^-]}\) and \(\mathcal{F}_M^{[u_i^\cdot,\theta_i^+]}\). Obviously, it is equivalent to determine the parameters \(u_i^\pm\), \(\theta_i^\pm\) and all coefficients \(f_{i,\alpha}^\pm\) with \(|\alpha|\le M\). In our method, we first calculate the reconstructed vectors of conservative variables on the cell boundaries as<tbc>

\(U_i^+=U_i+\frac{\Delta x}{2}s_i,U_i^-=U_i-\frac{\Delta x}{2}s_i,\) (14)

<tbc>where \(U_i=[\rho_i,\rho_iu_i,\rho_iE_i]^\mathsf{T}\) is the vector on the _i_th cell. The parameters \(u_i^\pm\) and \(\theta_i^\pm\) are then extracted from \(U_i^\pm\). Following \[21, 22\], the coefficients are reconstructed as<tbc>

\(f_{i,\alpha}^+=f_{i,\alpha}+\frac{\Delta x}{2}d_{i,\alpha},f_{i,\alpha}^-=f_{i,\alpha}-\frac{\Delta x}{2}d_{i,\alpha}.\) (15)

