Data-driven accelerated multigrid method for Riesz space fractional diffusion equations

**Abstract**

The multigrid method is one of the most efficient iterative methods for solving large structured linear systems, and its efficiency stems from the complementarity between the smoother and the coarse grid correction. In this paper, we consider the block Toeplitz linear system obtained by discretizing time dependent Riesz space fractional diffusion equations, and employ the weighted Jacobi iterative method as a smoother. The weighted Jacobi smoother features a simple structure and low computational cost, yet its smoothing property is highly dependent on the relaxation parameter. We adopt Gaussian process regression to select the relaxation parameter to accelerate the convergence of the multigrid method. Numerical experiments confirm the theoretical analysis, which simultaneously verifies the effectiveness and superiority of the data-driven parameter selection strategy.

**Keywords:** Multigrid methods, Fractional differential equations, Gaussian process regression

## 1. Introduction

Fractional differential equations are powerful mathematical tools that can accurately describe certain complex phenomena, such as pricing options [1, 17], control problems [10, 23], image processing [4, 2]. Consider a two-dimensional Riesz space fractional diffusion equation as follows:

\(\left\{\begin{array}{ c c } d(x,y,t)\frac{\partial u(x,y,t)}{\partial t}-\frac{\partial^{\gamma_1}u(x,y,t)}{\partial|x|^{\gamma_1}}-\frac{\partial^{\gamma_2}u(x,y,t)}{\partial|y|^{\gamma_2}}=f(x,y,t), & (x,y,t)\in\Omega\times(0,T), \\ u(x,y,t)=0, & (x,y,t)\in\partial\Omega\times(0,T), \\ u(x,y,0)=u_0(x,y), & (x,y)\in\bar{\Omega},
\end{array}\right.\) (1.1)

where \(\Omega=(x_L,x_R)\times(y_L,y_R)\), \(\partial\Omega\) denotes the boundary of \(\Omega\), _f(x,y,t_) is the source term, \(d(x,y,t)\ge 0\) is the coefficient function. _u_<sub>0</sub>(_x,y_) is the initial condition, \(\gamma_1,\gamma_2\in(1,2)\). Specifically, Riesz fractional derivatives are defined as follows:

\(\frac{\partial^{\gamma_1}u(x,y,t)}{\partial|x|^{\gamma_1}}=\sigma_{\gamma_1}\left(x_LD_x^{\gamma_1}+_xD_{x_R}^{\gamma_1}\right)u(x,y,t),\)<br> \(\frac{\partial^{\gamma_2}u(x,y,t)}{\partial|y|^{\gamma_2}}=\sigma_{\gamma_2}\left(y_LD_y^{\gamma_2}+_yD_{y_R}^{\gamma_2}\right)u(x,y,t),\)

_Email address:_ `zhangjuan@xtu.edu.cn` ( Juan Zhang<sup>∗</sup>1,2)

Yang Hu<sup>1</sup>, Juan Zhang<sup>∗</sup>1,2

1 School of Mathematics and Computational Science, Xiangtan University, Xiangtan, 411105, Hunan, People’s Republic of China

2 Hunan Key Laboratory for Computation and Simulation in Science and Engineering, Xiangtan University, Xiangtan, People’s Republic of China

