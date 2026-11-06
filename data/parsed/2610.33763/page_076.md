## Chapter 6

### Krylov preconditioning for inverse problems in space-time fractional diffusion equations

Having introduced in the previous chapters the analytical foundations of fractional operators, the spectral framework of matrix sequences, and the theory of GLT sequences, we now turn to the numerical solution of an IP for a space-time FDE. This chapter is based on the work \[66\], with additional details, numerical experiments, and reformulations included for completeness of the thesis presentation. This chapter investigates the reconstruction of a space-dependent source term in a model that incorporates a tempered fractional derivative in time and a Caputo fractional derivative in space, both of order in (0,1). Such equations are particularly valuable for modeling complex transport phenomena where diffusion transitions from anomalous to normal behavior over time, a feature that cannot be captured by standard fractional or classical models \[110, 112\].<br>
The inverse problem is inherently ill-posed in the Hadamard sense, as small perturbations in the final-time data can lead to large errors in the recovered source term. To address this instability, we apply a quasi-boundary value regularization method, which reformulates the problem into a well-posed form \[29, 48\]. The finite difference discretization of the regularized system leads to a large two-by-two block linear system. We conduct a detailed spectral analysis of the associated matrix sequences using the GLT framework, which provides a rigorous description of their asymptotic spectral behavior despite the presence of the variable coefficient that spoils the pure Toeplitz structure \[41, 42\]. Based on this analysis, we design an efficient preconditioner for the GMRES method. Numerical experiments confirm the effectiveness of the proposed preconditioning strategy in reducing iteration counts and computational cost.<br>
The aim of this work is to numerically solve the IP of identifying the source term _f(x_) in the space-time FDE

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,t)+a(x)^C\mathcal{D}_x^\eta u(x,t)=q(t)f(x), & x\in(0,1),t\in(0,T), \\
u(0,t)=u(1,t)=0, & t\in(0,T), \\
u(x,0)=\varphi(x), & x\in(0,1), \\
u(x,T)=\phi(x), & x\in(0,1),
\end{array}\right.\) (6.1)

where _T\>_0 is the final time, _a(x_) is a continuous a.e. variable coefficient such that \(a(x)\neq 0\), _q(t_) is a given function, \(\varphi(x)\) is the initial condition, and \(\phi(x)\) is the final time data. Moreover, \(^T\mathcal{D}_t^{\xi,\rho}\) represents the tempered fractional derivative in the time variable of order \(\xi\in(0,1)\), defined for \(\rho>0\) as follows

\(^T\mathcal{D}_t^{\xi,\rho} u(x,t):=\frac{1}{\Gamma(1-\xi)}\int_0^te^{-\rho(t-\tau)}(t-\tau)^{-\xi}\frac{\partial}{\partial\tau}u(x,\tau)\mathrm{d}\tau,\)

while \(^C\mathcal{D}_x^\eta\) denotes the Caputo fractional derivative in the space variable of order<tbc>

