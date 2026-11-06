operator kernels, together with analytical constraint embeddings for nonlinear problems, provides a unified approach for separating the enforcement of physical conditions from the approximation of the governing PDE.

### Contributions

The main contributions of this work are:

• We develop CFKS by analytically replacing a finite Gaussian-RBF feature representation with its exact bounded continuum-feature mean kernel. This removes the need to prescribe a finite feature count or select individual feature centers, while retaining Gaussian widths and center distributions as prescribed parameters.<tbc>

• We derive the corresponding differential-operator kernels and employ them in symmetric strong-form collocation for linear PDEs. Boundary and initial conditions are enforced through a null-space parameterization, allowing the governing equations to be solved within a constraint-compatible subspace.<tbc>

• We extend CFKS to nonlinear PDEs through linearized initialization and nonlinear least-squares residual minimization, using analytical kernel derivatives and Jacobians. Analytical constraint embeddings and multiscale continuum-feature kernels further accommodate prescribed physical conditions and localized solution structures.<tbc>

• We integrate optional residual-adaptive collocation and sequential space-time-slab marching into the CFKS framework. Residual-guided enrichment concentrates computational resolution in regions of under-resolution, while prescribed multiscale kernel refinement provides additional flexibility for resolving localized structures.

Residual-based adaptive sampling is already well established in meshfree and physics-informed methods \[19, 20\]. In CFKS, it is incorporated as an optional refinement strategy in which independently evaluated PDE residuals guide the allocation of additional collocation points. When the mean kernel is fixed, this refinement changes the collocation and represententer sites without altering the underlying continuum-feature kernel or prescribed physical conditions. For nonlinear problems, collocation enrichment can additionally be combined with prescribed changes in kernel scales. Sequential space-time-slab marching extends this strategy to time-dependent problems, consistent with earlier time-marching and causality-aware formulations \[21, 22\].

### Organization of the paper

The remainder of this paper is organized as follows. Section 2 presents the mathematical formulation of CFKS, including the continuum-feature mean kernel, operator-based collocation, constraint enforcement, and extensions to nonlinear PDEs, residual-adaptive collocation, and sequential space-time slabs. Section 3 introduces the numerical benchmark problems. Section 4 presents and discusses the numerical results, including finite-feature convergence and conditioning studies. Section 5 summarizes the main findings and outlines directions for future research. The appendices provide the connection between finite-feature models and the CFKS representer formulation, together with the analytical derivation of the bounded Gaussian continuum-feature kernel.

## 2 Mathematical tion

We first develop CFKS for linear differential problems and subsequently describe its extension to nonlinear PDEs. Let \(\Omega\) denote the computational domain and **z** the vector of independent variables. For time-dependent problems, **z**=(**x**_,t_), where **x** represents the spatial coordinates and _t_ denotes time. We consider the linear differential problem

\(\mathcal{L}u(\mathbf{z})=f(\mathbf{z}),\mathbf{z}\in\Omega,\) (1)

where L is a prescribed linear differential operator, _u_ is the unknown solution, and _f_ is a known source function. The problem is supplemented by boundary conditions and, for time-dependent equations, appropriate initial conditions.

To formulate the numerical problem, the governing PDE and its physical conditions are expressed through a collection of linear constraint functionals,

\(\ell_i[u]=y_i,i=1,\dots,N,\) (2)

where _N_ is the total number of discrete constraints, \(\ell_i\) denotes the linear functional associated with constraint _i_, and _y<sub>i</sub>_ is its prescribed value. For an interior PDE constraint imposed at a collocation point **z**_<sub>i</sub>_, the functional \(\ell_i\) applies the differential operator L to the solution at that point, with _y<sub>i</sub>=f_(**z**_<sub>i</sub>_). Boundary and initial conditions are represented by the corresponding evaluation or differential functionals at the selected physical constraint locations.

### 2.1 From finite RBF features to the continuum-feature mean kernel

We begin with a finite representation of the unknown solution using Gaussian radial basis function (RBF) features. Let **z**=(_z_<sub>1</sub>_,...,z<sub>d</sub>_) denote a point in the computational domain, where _d_ is the number of independent variables. For time-dependent problems, these variables include both spatial coordinates and time.

