# Block preconditioning for all-at-once variable-coefficient fractional evolution equations via the GLT analysis

**Abstract**

We study a class of nonlocal evolutionary partial differential equations with weakly singular temporal kernel and spatially variable diffusion coefficient. The model is posed on \(\Omega\subset\mathbb{R}\), and involves a left- sided Riemann–Liouville fractional derivative in space multiplied by a variable coefficient _a(x_). The temporal derivative is approximated by an _L_1 type scheme, while the spatial operator is discretized by finite difference techniques, resulting in large scale all at once linear systems with a twolevel Toeplitz like structure. We develop and analyze a block lower triangular strategy that mimics the structure of the coefficient matrix while simplifying its components for computational efficiency. The analysis is carried out at the level of matrix sequences by means of generalized locally Toeplitz (GLT) theory. Within this framework, we characterize the asymptotic spectral distribution of the discretized operators and use the associated GLT symbol to guide the construction of the structured approximation. Numerical experiments using the GMRES solver demonstrate that the proposed preconditioning strategy significantly improves convergence rates, robustness, and scalability for large-scale problems. Open problems and possible extensions are briefly discussed at the end of the present work.

_Keywords:_ Fractional evolution equations, Riemann-Liouville fractional derivative, spectral analysis, generalized locally Toeplitz, GMRES, preconditioning

### 1. Introduction

Consider the following nonlocal evolutionary fractional differential equation (FDE) with a weakly singular temporal kernel

\(\left\{\begin{array}{ c } \frac{1}{\Gamma(1-\beta)}\int_0^t\frac{\partial u(x,s)}{\partial s}(t-s)^{-\beta} ds=\mathcal{L}u(x,t)+f(x,t),x\in\Omega\subset\mathbb{R}^d,t\in(0,T], \\ u(x,t)=0,x\in\partial\Omega,t\in(0,T], \\ u(x,0)=\psi(x),x\in\Omega, \end{array}\right.\) (1)

where \(\Gamma(\cdot)\) denotes the Gamma function, \(0<\beta<1\), the boundary of \(\Omega\) is \(\partial\Omega\); \(\Omega=\prod_{i=1}^d(\tilde{a}_i,\hat{a}_i)\); \(x=(x_1,x_2,\dots,x_d)\in\mathbb{R}^d\); for _i_=1_,...,d_ and \(f,\psi\) are given functions. The operator L represents the spatial differential operator acting on _u(x,t_), which can take several representative forms such as

_Email addresses:_ `mfkhan@uninsubria.it` (Muhammad Faisal Khan<sup>∗</sup>), `s.serracapizzano@uninsubria.it` (Stefano Serra-Capizzano)

Muhammad Faisal Khan<sup>∗</sup><sup>a</sup>, Stefano Serra-Capizzano<sup>a,b</sup>

<sup>_a_</sup>_Department of Science and High Technology, University of Insubria, Como, Italy_

<sup>_b_</sup>_Department of Information Technology, Uppsala University, Uppsala, Sweden_

