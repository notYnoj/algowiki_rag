For a fixed approximation _u_<sup>(_k_)</sup>, this is a linear differential problem for the correction \(\delta u\). Its discretization can use the analytical kernel derivatives developed for linear CFKS.

Alternatively, a Picard-type approximation may be used when the nonlinear operator admits an appropriate coefficient- freezing formulation. The resulting linearized solution supplies initial coefficients for the nonlinear least-squares problem eq. 24.

This initialization procedure does not replace the nonlinear coefficient solve. Rather, it provides a starting approximation for minimizing the full nonlinear PDE residual.

## Multiscale continuum-feature kernels

For problems with localized gradients or multiple characteristic scales, the trial representation can combine continuum-feature mean kernels with different prescribed Gaussian widths and center distributions.

We consider an additive global-local kernel of the form

\(k_\mathrm{ms}^{(s)}(\mathbf{z},\mathbf{z}')=\widehat{k}_g^{(s)}(\mathbf{z},\mathbf{z}')+\eta\widehat{k}_\ell^{(s)}(\mathbf{z},\mathbf{z}'),\eta>0,\) (29)

where \(k_\mathrm{ms}^{(s)}\) is the multiscale kernel at refinement stage _s_, and \(\eta\) is a prescribed positive mixing weight. The subscripts _g_ and \(\ell\) identify the global and local components, respectively.

The global kernel is constructed from a bounded distribution of Gaussian centers covering the spatial domain, whereas the local kernel uses a center distribution concentrated around a prescribed region of interest. Each component is an analytically marginalized Gaussian-RBF mean kernel of the form defined in eq. 7.

To balance their contributions, the components are normalized according to

\(\widehat{k}_q^{(s)}(\mathbf{z},\mathbf{z}')=\frac{k_q^{(s)}(\mathbf{z},\mathbf{z}')}{k_q^{(s)}(\mathbf{z}_\mathrm{ref},\mathbf{z}_\mathrm{ref})},q\in\{g,\ell\},\) (30)

where _q_ identifies the kernel component and **z**<sub>ref</sub> is a prescribed reference point at which the diagonal kernel value is positive.

Positive normalization factors preserve positive semidefiniteness, and the positive weighted sum in eq. 29 remains a symmetric positive-semidefinite kernel. Its derivatives are obtained by differentiating the analytical component kernels.

The center distributions, Gaussian widths, normalization point, and mixing weight remain prescribed parameters. The multiscale construction therefore increases representation flexibility without introducing finite Gaussian-feature center sampling.

## Illustration using viscous Burgers’ equation

As a nonlinear example, consider the one-dimensional viscous Burgers equation

\(u_t+uu_x-\nu u_{xx}=0,(x,t)\in[-1,1]\times(0,T],\) (31)

where _x_ denotes the spatial coordinate, _t_ is time, _T_ is the final simulation time, and \(\nu>0\) is the viscosity. The subscripts _t_, _x_, and _xx_ denote the corresponding first time, first spatial, and second spatial derivatives.

For the homogeneous Dirichlet boundary conditions and prescribed initial profile used in this benchmark, analytical constraint embedding is applied on successive space-time slabs.

Let _n_ index the time slabs, with \(\tau=t-t_n\) denoting the local time measured from the beginning _t<sub>n</sub>_ of the current slab. At refinement stage _s_, the trial solution is

\(u_{h,n}^{(s)}(x,\tau)=u_{\mathrm{in},n}^{(s)}(x)+\tau(1-x^2)v_{h,n}^{(s)}(x,\tau),\) (32)

where \(u_{\mathrm{in},n}^{(s)}\) is the incoming solution profile and \(v_{h,n}^{(s)}\) is an unknown correction field.

The factors \(\tau\) and 1-_x_<sup>2</sup> make the correction vanish at the beginning of each slab and at the spatial boundaries, respectively. Hence, the trial solution preserves the incoming profile and satisfies the homogeneous boundary conditions, provided the incoming profile is boundary-compatible.

The correction field is represented by

\(v_{h,n}^{(s)}(\mathbf{z})=\sum_{j=1}^{N_{p,n}^{(s)}}\alpha_{j,n}^{(s)}k_\mathrm{ms}^{(s)}(\mathbf{z},\mathbf{z}_{j,n}^{(s)}),\) (33)

