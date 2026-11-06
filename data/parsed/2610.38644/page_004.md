The _m_th Gaussian RBF feature is defined as

\(\phi_{\theta_m}(\mathbf{z})=\mathrm{exp}\left(-\frac{1}{2}\sum_{r=1}^d\frac{(z_r-\theta_{m,r})^2}{\sigma_r^2}\right),\) (3)

where \(\theta_m=(\theta_{m,1},\dots,\theta_{m,d})\) denotes the center of the _m_th feature, \(\theta_{m,r}\) is its center coordinate in the _r_th direction, and \(\sigma_r>0\) is the prescribed Gaussian width associated with that direction. The index _r_ runs over the _d_ independent variables. Equal widths in all directions give the isotropic Gaussian RBF, whereas different widths allow coordinate-dependent scaling. In space-time problems, separate spatial and temporal widths can therefore be prescribed.

Using _M_ such features, where _M_ is the total number of Gaussian RBF features, the finite-feature approximation is expressed as

\(u_M(\mathbf{z})=\frac{1}{\sqrt{M}}\sum_{m=1}^M\beta_m\phi_{\theta_m}(\mathbf{z}),\) (4)

where _u<sub>M</sub>_ denotes the approximate solution, _m_ indexes the individual features, and \(\beta_m\) is the output coefficient associated with the _m_th feature. The feature centers and Gaussian widths are fixed when determining the coefficients from the governing constraints. The normalization factor \(1/\sqrt{M}\) ensures that the associated feature Gram matrix has a nontrivial finite limit as the number of features increases.

Recall that the governing PDE and physical conditions are represented by _N_ linear constraint functionals, denoted by \(\ell_i\), with _i_=1_,...,N_. Applying these functionals to the finite-feature representation gives the constraint matrix _Z_, whose entries are

\(Z_{im}=\frac{1}{\sqrt{M}}\ell_i[\phi_{\theta_m}],\) (5)

where _Z<sub>im</sub>_ is the entry associated with constraint _i_ and feature _m_. Thus, _Z_ is an \(N\times M\) matrix, and \(\ell_i[\phi_{\theta_m}]\) denotes the result of applying the _i_th linear constraint functional to the _m_th Gaussian RBF feature.

The corresponding constraint Gram matrix is obtained by multiplying _Z_ by its transpose:

\((ZZ^\top)_{ij}=\frac{1}{M}\sum_{m=1}^M\ell_i[\phi_{\theta_m}]\ell_j[\phi_{\theta_m}],\) (6)

where \(Z^\top\) denotes the transpose of _Z_, and _i,j_=1_,...,N_ index pairs of constraint functionals. The matrix \(ZZ^\top\) is symmetric and positive semidefinite, with each entry representing the inner product of two constraint-applied finite-feature vectors.

To obtain the continuum-feature formulation, suppose that the Gaussian RBF centers are independently sampled from a prescribed probability distribution with density \(\rho(\theta)\), where \(\theta\) represents a generic feature-center vector. The distribution specifies the region and relative weighting of admissible feature centers. In the present work, bounded uniform center distributions are used.

Rather than retaining an explicit finite realization of these centers, we consider the analytical mean of the products of Gaussian RBF features. This defines the _continuum-feature mean kernel_

\(k_\rho(\mathbf{z},\mathbf{z}')=\mathbb{E}_{\theta\sim\rho}\left[\phi_\theta(\mathbf{z})\phi_\theta(\mathbf{z}')\right],\) (7)

where \(k_\rho\) denotes the mean kernel associated with the center distribution \(\rho\), and **z** and \(\mathbf{z}'\) are its first and second arguments, respectively. The notation \(\mathbb{E}_{\theta\sim\rho}\) denotes expectation with respect to the prescribed probability distribution of the feature-center vector \(\theta\). The function \(\phi_\theta\) is the Gaussian RBF defined in eq. 3, with the generic center \(\theta\) replacing the individual center \(\theta_m\).

For independently sampled feature centers, the law of large numbers implies that, as the number of features _M_ tends to infinity, each entry of the empirical constraint Gram matrix converges to its corresponding population value, provided the relevant feature moments are finite. For the bounded Gaussian-feature construction considered here, these conditions are satisfied. Consequently,

\((ZZ^\top)_{ij}\longrightarrow\mathbb{E}_{\theta\sim\rho}\left[\ell_i[\phi_\theta]\ell_j[\phi_\theta]\right]\)<br>
\(=\ell_i^\mathbf{z}\ell_j^{\mathbf{z}^\prime} k_\rho(\mathbf{z},\mathbf{z}'),\) (8)

where the superscripts on the constraint functionals identify the kernel argument on which each functional acts. Specifically, \(\ell_i^\mathbf{z}\) acts on the first argument of the kernel, while \(\ell_j^{\mathbf{z}^\prime}\) acts on the second. Each functional includes the appropriate differential or evaluation operation at the location associated with its constraint.

