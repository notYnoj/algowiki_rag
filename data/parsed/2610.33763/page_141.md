## 8.4.2 GMRES performance in the _d_-dimensional space setting, _d_=1,2

We consider the one-dimensional variable-coefficient space-fractional diffusion equation (8.2):

\(\frac{\partial u(x,t)}{\partial t}=x^2D_x^\alpha u(x,t)+f(x,t),x\in(0,1),t\in(0,1],\)

with homogeneous Dirichlet boundary conditions _u_(0_,t_)=_u_(1_,t_)=0 and initial condition _u(x,_0)=0.

We choose the exact solution as

\(u(x,t)=t^2x^2(1-x)^2.\)

The corresponding source term is given by

\(f(x,t)=2tx^2(1-x)^2-x^2t^2\left[\frac{2}{\Gamma(3-\alpha)}x^{2-\alpha}-\frac{12}{\Gamma(4-\alpha)}x^{3-\alpha}+\frac{24}{\Gamma(5-\alpha)}x^{4-\alpha}\right].\)

Thus, in this section, we investigate the practical performance of the GMRES iterative solver for the all-at-once linear system arising from the one-dimensional discretization given in equation (8.15), with the time-stepping parameter set to \(\theta=0.5\) (Crank–Nicolson method). We compare the behavior of GMRES applied to both the original (non-preconditioned) system and the system preconditioned by a circulant structure-preserving preconditioners as defined in Section 8.2, to illustrate the impact of preconditioning on convergence and computational efficiency. First, the experiments are conducted for the one-dimensional constant-coefficient fractional diffusion problem (_a(x_)=1), and then for the one-dimensional variable-coefficient fractional diffusion problem with coefficient _a(x_)=_x_<sup>2</sup>+1, and _a(x_)=_x_<sup>2</sup>. The initial vector is set to zero, the tolerance is 10<sup>-8</sup>, and the maximum number of iterations equals the matrix dimension. s 8.3, 8.5, and 8.7 summarize the numerical performance of the GMRES method both for the unpreconditioned system and the preconditioned ones. Here, _N_ denotes the number of spatial grid points and _M_ the number of time levels and the average number of GMRES iterations per time step are reported in the columns. s 8.4 and 8.6 report the averaged total computational time (in seconds) for solving the entire problem 10 times.

As the discretization becomes finer, the unpreconditioned system exhibits a substantial growth in both iteration counts and CPU times, reflecting the increasing ill-conditioning of the coefficient matrix. The computational effort is mainly influenced by the spatial parameter _N_, as larger _N_ values lead to denser matrices and slower convergence, while variations in _M_ have a comparatively smaller effect.

When the preconditioners are applied, GMRES shows a significant improvement in convergence. The iteration numbers remain nearly constant for increasing _N_ and _M_, and the corresponding CPU times grow only mildly with the problem size. This behavior demonstrates the mesh-independent convergence of the preconditioned system and confirms that the preconditioners effectively captures the spectral structure of the matrix, resulting in a well-clustered spectrum and reduced computational cost.

