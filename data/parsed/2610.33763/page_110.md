## Chapter 8

### Structure-preserving preconditioning for variable- coefficient space-fractional diffusion equations and \(\theta\)-Method

In this chapter, based on the results presented in [73], we investigate the spectral properties and preconditioning of linear systems arising from the discretization of time-dependent space-FDEs with variable coefficient. Additional details, numerical experiments, and reformulations are included for completeness of the thesis presentation. Fractional diffusion models have become increasingly relevant in the mathematical modeling of anomalous transport processes, especially in situations where the classical diffusion equation fails to capture long-range interactions and nonlocal effects [131]. Such models are particularly valuable for describing superdiffusive behavior, where particles disperse more rapidly than predicted by classical diffusion theory.<br>
The numerical discretization of these equations leads to large linear systems that are dense, nonsymmetric, and often severely ill-conditioned. To address these challenges, we develop a preconditioning strategy based on the structural properties of the discretized operator. A detailed spectral analysis of the associated matrix sequences is carried out using the GLT theory, which provides a unified framework for describing the asymptotic singular value and spectral distributions of both the original and preconditioned matrices [41, 42]. The main novelty is that the analysis fully covers the nonconstant variable coefficient case, both in one and two spatial dimensions. Numerical experiments confirm the effectiveness of the proposed preconditioners in accelerating the convergence of GMRES.<br>
In this chapter, we consider the following class of evolutionary partial differential equations:<tbc>

\(\left\{\begin{array}{ c c }
\frac{\partial}{\partial t}u(x,y,t)=\mathcal{L}u(x,y,t)+f(x,y,t), & (x,y,t)\in\Omega\times(0,T], \\
u(x,y,t)=0, & (x,y)\in\partial\Omega,t\in[0,T], \\
u(x,y,0)=\phi(x,y), & (x,y)\in\Omega,
\end{array}\right.\) (8.1)

<tbc>where \(\Omega=(L_1,R_1)\times(L_2,R_2)\subset\mathbb{R}^2\) is open, _f(x,y,t_) is a given source term, _u(x,y,t_) denotes the unknown solution, and \(\phi(x,y)\) is the prescribed initial condition.<br>
More specifically, we consider the operator

\(\mathcal{L}=a(x,y)\left(\mathcal{D}_x^{\alpha_1}+\mathcal{D}_y^{\alpha_2}\right),\)

where _a(x,y_) is a smooth variable diffusion coefficient, \(\mathcal{D}_x^{\alpha_1}\) denotes the left-sided Riemann-Liouville fractional derivative of order \(\alpha_1\in(1,2)\) with respect to _x_, and \(\mathcal{D}_y^{\alpha_2}\) denotes the left-sided Riemann-Liouville fractional derivative of order \(\alpha_2\in(1,2)\) with respect to _y_.

