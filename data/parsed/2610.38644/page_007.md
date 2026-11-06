where N is a prescribed nonlinear differential operator, _u_ is the unknown solution, _f_ is a known source function, and \(\Omega\) is the computational domain. The operator may depend nonlinearly on the solution, its derivatives, or both. Appropriate boundary and, when applicable, initial conditions complete the problem.

Unlike the linear formulation, a nonlinear differential operator does not generally produce a fixed operator Gram matrix. Instead, CFKS constructs a deterministic kernel trial representation and determines its coefficients by minimizing the nonlinear PDE residual.

Let \(k_\rho\) be the continuum-feature mean kernel defined in eq. 7. We consider the trial representation

\(u_h(\mathbf{z};\unknown)=u_\mathrm{base}(\mathbf{z})+w(\mathbf{z})\sum_{j=1}^{N_r}\alpha_jk_\rho(\mathbf{z},\unknown_j),\) (22)

where _u<sub>h</sub>_ denotes the approximate solution, \(\unknown=(\alpha_1,\dots,\alpha_{N_r})^\top\) is the unknown coefficient vector, _N<sub>r</sub>_ is the number of kernel representer sites, and \(\unknown_j\) is the location of the _j_th representer site. The prescribed functions _u_<sub>base</sub> and _w_ define an additive component and a multiplicative factor, respectively.

When a suitable analytical constraint embedding is available, these functions can be selected so that the trial solution satisfies the prescribed boundary or initial conditions independently of the coefficient values. An unconstrained representation is recovered by setting _u_<sub>base</sub>=0 and _w_=1.

The trial representation is linear in \(\unknown\), although the governing PDE residual is generally nonlinear in these coefficients. Importantly, _N<sub>r</sub>_ determines the dimension of the discrete kernel representation and does not represent the number of Gaussian RBF features. Each kernel section is already obtained by analytically averaging a continuum of Gaussian RBF features over the prescribed center distribution.

Let \(\{\mathbf{z}_i\}_{i=1}^{N_p}\) denote the interior PDE collocation locations, where _N<sub>p</sub>_ is the number of discrete PDE constraints. The residual at the _i_th collocation point is defined as

\(r_i(\unknown)=\mathcal{N}\left[u_h(\cdot;\unknown)\right](\mathbf{z}_i)-f(\mathbf{z}_i),i=1,\dots,N_p,\) (23)

where the nonlinear operator acts on the trial solution before evaluation at **z**_<sub>i</sub>_.

Collecting the residuals into the vector \(\mathbf{r}(\unknown)=(r_1,\dots,r_{N_p})^\top\), the kernel coefficients are determined through

\(\unknown^*=\mathrm{arg}\mathrm{min}_\unknown\frac{1}{2}\left\|\mathbf{r}(\unknown)\right\|_2^2,\) (24)

where \(\unknown^*\) denotes the optimized coefficient vector and \(\|\cdot\|_2\) is the Euclidean norm. Thus, the nonlinear PDE is enforced through least-squares minimization of its discrete residual.

The analytical continuum-feature kernel also permits direct construction of the residual Jacobian. Define the coefficient- independent trial functions

\(\psi_j(\mathbf{z})=w(\mathbf{z})k_\rho(\mathbf{z},\unknown_j),j=1,\dots,N_r.\) (25)

Since the derivative of the trial solution with respect to \(\alpha_j\) is \(\psi_j\), the Jacobian entries are

\(J_{ij}(\unknown)=\frac{\partial r_i}{\partial\alpha_j}=(\mathcal{N}'[u_h]\psi_j)(\mathbf{z}_i),\) (26)

provided the nonlinear operator is Fréchet differentiable. Here, \(\mathcal{N}'[u_h]\) denotes the linearization of N about the current trial solution, acting on the function \(\psi_j\). The Jacobian \(J(\unknown)\) has dimensions \(N_p\times N_r\).

Because the mean kernel and its derivatives are available analytically, the residual and Jacobian can be evaluated without generating finite random-feature realizations. The nonlinear optimization therefore determines only the coefficients of the prescribed continuum-feature kernel representation.

## Linearized initialization

The nonlinear least-squares problem generally requires an initial coefficient vector. A suitable initialization can be obtained by linearizing the governing equation about an available approximation.

Let _u_<sup>(_k_)</sup> denote the current approximation at iteration _k_, and let \(\delta u\) be a correction. A first-order expansion gives

\(\mathcal{N}[u^{(k)}+\delta u]\approx\mathcal{N}[u^{(k)}]+\mathcal{N}'[u^{(k)}]\delta u,\) (27)

where \(\mathcal{N}'[u^{(k)}]\) is the Fréchet derivative of the nonlinear operator evaluated at _u_<sup>(_k_)</sup>. The corresponding linearized equation is

\(\mathcal{N}'[u^{(k)}]\delta u\approx f-\mathcal{N}[u^{(k)}].\) (28)

