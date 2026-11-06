The matrix \(K_{\ell\ell}\) has dimensions \(N\times N\) and is symmetric and positive semidefinite. As established in eq. 8, its entries are the analytical population limits of the corresponding finite-feature constraint Gram-matrix entries.

Let \(\alpha=(\alpha_1,\dots,\alpha_N)^\top\) denote the vector of representer coefficients and \(\mathbf{y}=(y_1,\dots,y_N)^\top\) the vector of prescribed constraint values. A regularized collocation formulation is then given by

\((K_{\ell\ell}+\lambda I)\alpha=\mathbf{y},\) (13)

where _I_ is the \(N\times N\) identity matrix and \(\lambda\ge 0\) is a prescribed regularization parameter. When \(\lambda=0\), the system corresponds to direct constraint interpolation, provided a solution exists. A positive regularization parameter improves the conditioning of the coefficient system but generally relaxes exact satisfaction of the discrete constraints. The separate enforcement of linear physical conditions through a null-space parameterization is described in the subsequent formulation.

Once the coefficient vector \(\alpha\) has been determined, the approximate solution can be evaluated at any point **z** using

\(u_h(\mathbf{z})=\mathbf{k}_{\mathbf{z}\ell}^\top\alpha,(\mathbf{k}_{\mathbf{z}\ell})_j=\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'),\) (14)

where \(\mathbf{k}_{\mathbf{z}\ell}\) is an _N_-component column vector containing the kernel interactions between the evaluation point **z** and the selected constraint functionals. Its _j_th component is obtained by applying the _j_th functional to the second argument of the continuum-feature mean kernel. The superscript \(\top\) denotes vector transposition.

Equations 7-14 define the kernel formulation without retaining the finite number of Gaussian RBF features or their individual center realizations. Because the bounded continuum-feature mean kernel is evaluated analytically, no numerical quadrature over the feature-center distribution is required. The resulting PDE approximation is determined by the prescribed kernel parameters, the selected constraint locations, and the numerical treatment of the resulting collocation system.

## 2.3 Constraint-compatible enforcement of physical conditions

When boundary or initial data are to be satisfied independently of the PDE least-squares fit, we separate the physical constraints from the interior PDE equations. Let

\(A\alpha\approx\mathbf{f},B\alpha=\mathbf{g},\) (15)

denote, respectively, the interior PDE equations and the boundary or initial constraints obtained from the CFKS representation eq. 11.

A particular coefficient vector satisfying the physical constraints is chosen as

\(\alpha_p=B^+\mathbf{g},\) (16)

where _B_<sup>+</sup> denotes the Moore-Penrose pseudoinverse. Let the columns of _Q_ span the numerical null space of _B_,

\(BQ=0.\) (17)

Every constraint-compatible solution can then be parameterized as

\(\alpha=\alpha_p+Q\eta.\) (18)

Substitution into the PDE equations gives the reduced problem

\(AQ\eta\approx\mathbf{f}-A\alpha_p.\) (19)

With Tikhonov regularization,

\(\eta=argmin_\eta\|AQ\eta-(\mathbf{f}-A\alpha_p)\|_2^2+\lambda\|\eta\|_2^2.\) (20)

This construction separates satisfaction of the linear physical constraints from fitting of the PDE residual and avoids introducing an arbitrary relative penalty between boundary and interior equations. In practice, the reduced system is solved using rank-revealing SVD-based linear algebra.

## 2.4 Nonlinear CFKS formulation

We now extend the continuum-feature kernel formulation to nonlinear differential problems. Consider

\(\mathcal{N}[u](\mathbf{z})=f(\mathbf{z}),\mathbf{z}\in\Omega,\) (21)

