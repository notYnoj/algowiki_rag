# CFKS: CONTINUUM-FEATURE KERNEL PDE SOLVERS

**ABSTRACT**

Neural-network-based PDE solvers require architectural choices, particularly the number of layers and neurons per layer. Fixing a single Gaussian radial basis function (RBF) feature layer and taking the number of features to the continuum limit removes the need to prescribe a finite feature count or select individual feature centers, thereby reducing representation arbitrariness. Motivated by this principle, we introduce Continuum-Feature Kernel Solver (CFKS), a deterministic framework for PDEs obtained by analytically marginalizing a bounded continuum of Gaussian RBF features. CFKS works directly with the resulting continuum-feature mean kernel and its operator-applied counterparts, parameterized by prescribed Gaussian widths and bounded center distributions. For linear PDEs, CFKS leads to symmetric operator-kernel collocation systems with null-space enforcement of physical constraints. Nonlinear PDEs are addressed through linearized initialization and nonlinear least-squares residual minimization using analytical kernel derivatives and Jacobians. Residual-guided collocation enrichment and sequential space--time-slab marching provide additional resolution strategies, while prescribed multiscale kernel refinement helps resolve localized nonlinear structures. Finite-feature experiments confirm convergence of empirical value and operator Gram matrices toward their continuum counterparts. Numerical studies include oscillatory and multiscale ODEs, irregular- domain Poisson and biharmonic problems, singular perturbations, transient transport equations, and viscous Burgers’ equation. The results establish CFKS as a direct computational connection between finite Gaussian-RBF representations and continuum-feature kernel PDE solvers. s: `https://github.com/vikas-dwivedi-2022/CFKS\_s`

### 1 Introduction

Physics-informed neural networks (PINNs) are increasingly used for forward and inverse partial differential equation (PDE) problems [1]. However, their practical performance depends on architectural choices, particularly the number of layers and neurons per layer, as well as optimization and collocation-point placement. A natural way to reduce this architectural arbitrariness is to consider a single-layer Gaussian radial basis function (RBF) representation and take the number of features to the continuum limit. When the corresponding feature expectation is available analytically, the resulting kernel eliminates the need to prescribe a finite feature count or select individual feature centers. The representation nevertheless remains parameterized by prescribed Gaussian widths and center distributions, which influence approximation accuracy and numerical conditioning. This motivates the development of meshfree PDE solvers that work directly with continuum-feature kernels rather than finite feature realizations.

<sup>∗</sup>Corresponding Author

**Vikas Dwivedi**<sup>∗</sup><br> CREATIS Biomedical Imaging Laboratory<br> INSA, CNRS UMR 5220, Inserm, Universit ́e Lyon 1<br> Lyon 69621, France<br> **vikas.dwivedi@creatis.insa-lyon.fr**

**Monica Sigovan**<br> CREATIS Biomedical Imaging Laboratory<br> INSA, CNRS UMR 5220, Inserm, Universit ́e Lyon 1<br> Lyon 69621, France<br> **monica.sigovan@insa-lyon.fr**

**Balaji Srinivasan**<br> Wadhwani School of Data Science and AI<br> IIT Madras, India<br> **sbalaji@dsai.iitm.ac.in**

**Bruno Sixou**<br> CREATIS Biomedical Imaging Laboratory<br> INSA, CNRS UMR 5220, Inserm, Universit ́e Lyon 1<br> Lyon 69621, France<br> **bruno.sixou@insa-lyon.fr**

