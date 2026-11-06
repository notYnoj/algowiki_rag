several devices.

## 4. Benchmarks

In this section, we benchmark `diff-soup` against widely used scientific computing frameworks for stiff dynamical systems, including the CPU libraries SUNDIALS [31], PETSc [33], `DifferentialEquations.jl` [34], and MATLAB `ode15s` [35], and the GPU-based `JAX` library `diffrax` [49]. We use three problems of increasing complexity: the heat equation, which admits a closed-form solution in both the continuous and the discrete setting, the Brusselator system, which is a model benchmark problem for stiff PDEs [65], and a challenging coupled chemo-mechanical Cahn-Hilliard problem inspired by PFHub benchmark problem 4 [94].

### 4.1. Comparing time integrators with the heat equation

The heat equation on the unit interval with homogeneous Dirichlet boundaries takes the following form:

\(\frac{\partial u}{\partial t}=\frac{\partial^2u}{\partial x^2},x\in(0,1),t\in(0,T],u(0,t)=u(1,t)=0,u(x,0)=x(1-x),\) (16)

which is discretized with second-order central differences on _N_ interior nodes \(x_i=i\Delta x\) with spacing \(\Delta x=1/(N+1)\) as

\(u'_i=\frac{u_{i-1}-2u_i+u_{i+1}}{\Delta x^2},i=1,\dots,N,u_0=u_{N+1}=0,\) (17)

and integrated to _T_=0.2. Both the continuous problem and the semidiscrete system admit closed-form solutions,

\(u(x,t)=\sum_{k=1}^\infty\frac{4\left(1-\left(-1\right)^k\right)}{k^3\pi^3}sin(k\pi x)e^{-k^2\pi^2t},u_i(t)=\sum_{k=1}^N\hat{u}_ksin(k\pi x_i)e^{-\lambda_kt},\lambda_k=\frac{4}{\Delta x^2}sin^2\left(\frac{k\pi\Delta x}{2}\right),\) (18)

where \(\hat{u}_k\) are the discrete sine coefficients of the initial condition and \(\lambda_k\) are the eigenvalues of the negative discrete Laplacian. Figure 4 shows the decay of the solution over the benchmark window.

