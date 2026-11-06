## 5. Numerical experiments

In Section 3, we discuss the convergence of the TGM. The TGM contains only one coarse level. When the size of the original matrix is too large, the order of the coarse matrix obtained by projection may still be high, and it remains difficult to solve the coarse-grid equation exactly. A natural approach to resolve this difficulty is to recursively apply the TGM on this coarse level to generate coarser levels successively, until the order of the coarsest level is sufficiently small. Except for the coarsest level, each of the remaining grid levels performs only one such recursive procedure, which yields the V-cycle of the multigrid method\[24, 27, 32\].

In this section, we present several numerical experiments to demonstrate the computational efficiency of the multigrid method and verify the acceleration effect of using GPR-predicted parameters on the multigrid solver. Specifically, we set the order of the matrix on the coarsest level of the multigrid method to be no more than 1000. Except for the coarsest level, one weighted Jacobi iteration is applied for pre-smoothing and post- smoothing on all remaining grid levels, and the same input relaxation parameter is used for all weighted Jacobi iterations. In the experiments, we consider three test cases for comparison: the multigrid method with \(\omega=1\) as the relaxation parameter, the multigrid method using GPR-predicted values as the relaxation parameter, and the unpreconditioned conjugate gradient method.

The training strategy of GPR is as follows: starting from _N_=5 with a step size of 5 up to _N_=50, we construct a training set consisting of 10 samples. For each problem size, the quasi-optimal parameter \(\omega\) is obtained via grid search over the interval \[0.001,1\] with a step size of 0.001.For all algorithms, the zero vector is used as the initial iterate, with the stopping criterion

\(\mathrm{RRES}=\frac{\|Au-b\|_\infty}{\|b\|_\infty}\le 10^{-7}.\)

All experiments are carried out using MATLAB (version R2025b) on a laptop equipped with an Intel Core i5-9300H CPU (4 cores, 2.40 GHz) and 8 GB of memory.

**Example 5.1.** Consider the two-dimensional Riesz space fractional diffusion equation (1.1) defined on the domain \((0,1)\times(0,1)\times(0,1)\). The exact solution is given by _u(x,y,t_)=2(_t_<sup>3</sup>+0.01)_xy_(1-_x_)(1-_y_), and the initial condition is _u_<sub>0</sub>(_x,y_)=0.02_xy_(1-_x_)(1-_y_). We take _d(x,y,t_)=ln(1+_x_)(_y_+1)<sup>2</sup>. The source term _f_ is derived from the exact solution.

Weighted Jacobi Smoother
Weighted Jacobi Smoother
Weighted Jacobi Smoother
Weighted Jacobi Smoother
Exact Solve
Restriction
Prolongation

Figure 4: V-cycle sketch map

