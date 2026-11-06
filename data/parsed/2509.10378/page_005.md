<tbc>they can be queried at arbitrary resolutions without retraining. This is achieved generally by learning integrating kernels that perform transformations between the function spaces \[9\], which naturally is applicable to different discretizations. Our work adopts the Fourier Neural Operator \[48\] and Fully Convolutional Network (FCN) \[49\] to capture the mapping between the space of gauge configurations to a related embedding space as part of the proposed framework to construct effective preconditioners for the Wilson-Dirac normal equations. This is the key component enabling the successful volume transfer to lattice gauge field configurations with various lattice geometries.

## 3 Methods

In this section, we formulate the learning task as an operator learning problem, employing FNO and FCN architectures to model the mapping between input and output configurations shown in Figure 1. We further introduce an efficient unsupervised loss function designed to train the networks such that the linear operator derived from the output configuration approximates the inverse of that associated with the input configuration.

### 3.1 Problem formulation

The lattice discretization of the two-flavor Schwinger model used in this study is defined by the standard plaquette gauge action and the Wilson fermion action corresponding to two degenerate fermions:<tbc>

\(S=-\beta\sum_{x\in\Lambda_L}\Re\big(P(x)\big)+\sum_{f=0}^1\sum_{x,y\in\Lambda_L}\overline{\psi_f}(x)D_{x,y}\psi_f(y),\) (2)

<tbc>where the _d=_2 spacetime lattice of finite extent _L_ in each direction is given by \(\Lambda_L=\{x=an|n\in\mathbb{Z}_L^d\}\) for lattice spacing \(a,U_\mu(x)\in\mathrm{U}(1)\) is the complex gauge field where \(\mu\in\{1,2\}\) labels the spatial and temporal components and \(\psi_f(x),\overline{\psi_f}(x)\) are two-component Wilson fermion fields with flavor indices \(f\in\{0,1\}\). The plaquette appearing in the gauge action is<tbc>

\(P(x)=U_1(x)U_2(x+\hat{1})U_1^*(x+\hat{2})U_2^*(x),\) (3)

<tbc>where \(\hat{j}\) is a unit vector in the _j_ direction, and the Wilson discretization of the Dirac operator \[67\] is

\(D_{x,y}=(m+2r)\delta_{x,y}-\frac{1}{2}\sum_{\mu=1}^2\big((1-\gamma_\mu)U_\mu(x)\delta_{x+\hat{\mu},y}+(1+\gamma_\mu)U_\mu^*(x-\hat{\mu})\delta_{x-\hat{\mu},y}\big),\) (4)

where \(\gamma_1\) and \(\gamma_2\) are Euclidean gamma matrices in two dimensions. The specific representation used in this study is provided by the Pauli matrices: \(\gamma_1=\sigma_1\) and \(\gamma_2=\sigma_2\) with \(\gamma_5=i\gamma_1\gamma_2=-\sigma_3\). Periodic spatial boundary conditions are used for all fields and the fermion(boson) fields are anti-periodic(periodic) in the temporal direction.

The Wilson-Dirac operator depends on the bare fermion mass _m_ and Wilson term _r_ and implicitly on the bare gauge coupling \(\beta\). In this work, _r=_1 throughout and _m_ is implemented through \(\kappa=(2(m+2))^{-1}\). Since _D_ itself is not Hermitian for the Wilson fermion discretization, we combine it with its conjugate transpose to produce a Hermitian system _D_<sup>†</sup>_Dx=D_<sup>†</sup>_b_ with the solution _x_ to the original system (_Dx=b_) easily constructed thereafter. Note that the _D_ operator depends on the gauge field \(U_\mu(x)\) and the hopping parameter \(\kappa\), and so we use the shorthand \(D[U_\mu(x),\kappa]\) to represent the operator defined by a particular gauge and mass. \(D^\dagger D[U_\mu(x),\kappa]\) is defined analogously. When two operators share the same mass but different gauge fields we omit the hopping parameter from their shorthands; for e.g., \(D[U_\mu(x)]\) and \(D[\tilde{U}_\mu(x)]\).

The _D_<sup>†</sup>_D_ operator is ill-conditioned for certain regions of couplings such that it requires effective preconditioning in an iterative solver to accelerate convergence. Let _M_<sup>-1</sup> be the inverse of _D_<sup>†</sup>_D_,<tbc>

