Asymptotic behavior of Eckhoff’s method for convergence acceleration of Dirac eigenfunction expansions

**Abstract**

The current paper considers the problem of recovering a vector-function on [-1,1] from a limited number of coefficients of its expansion into a series of eigenfunctions of a one- dimensional Dirac system. The Krylov-Lanczos-Eckhoff-Gottlieb acceleration method is examined in the situation when the boundary values it requires have to be computed from the generalized Fourier coefficients themselves. This leads to a \(2q\times 2q\) linear system whose matrix is a block Vandermonde matrix; its determinant and inverse are computed explicitly, and the asymptotic _L_<sub>2</sub>-error constant of the method is found, paralleling the classical trigonometric case.

## Introduction

Let \(\{\lambda_n\}_{n\in\mathbb{Z}}\), \(\{v_n\}_{n\in\mathbb{Z}}\) be the eigenvalues and _L_<sub>2</sub>-orthonormal eigenfunctions of a self-adjoint boundary value problem on a finite interval, and let _f_ be a square-integrable function on that interval. It is well known that the expansion

\(f(x)=\sum_{n=-\infty}^\infty c_nv_n(x),c_n=\langle f,v_n\rangle,\)

converges to _f_ in _L_<sub>2</sub>. For practical purposes one approximates _f_ by the truncated series \(S_N(f)=\sum_{|n|\le N}c_nv_n\), and the involved error is strongly dependent on the smoothness of _f_. If _f_ belongs to the domain of the underlying differential operator, this approximation converges uniformly. If, however, _f_ or its derivatives do not satisfy the boundary conditions, the convergence becomes slow, its rate reflects only the smoothness of _f_, and the Gibbs phenomenon appears at the endpoints.

For the classical Fourier series \((v_n=e^{i\pi nx}/\sqrt{2}\) on [-1,1], the eigenfunctions of _id/dx_ with periodic boundary conditions), increasing the convergence rate by subtracting a polynomial that carries the discontinuities of the function and of its first few derivatives was suggested by A. Krylov as early as 1906 [13] and later, in 1964, by C. Lanczos [14, 15]. More detailed investigation of this approach, together with practical algorithms for computing the "jumps" of _f_ and its derivatives from the Fourier coefficients alone, was performed by K. S. Eckhoff and D. Gottlieb [6, 7, 8, 9, 11, 12]. The method is now usually called the Krylov-Lanczos- Eckhoff-Gottlieb, or simply Eckhoff, method. Its asymptotic _L_<sub>2</sub> error constants were computed by A. Barkhudaryan, R. Barkhudaryan and A. Poghosyan in [1]. An alternative acceleration technique for nonperiodic functions, based on quasi-periodic approximations and interpolations, was developed in [22, 23, 21].

R. H. Barkhudaryan<sup>1,2</sup>, G. G. Gevorkyan<sup>1</sup>, and L. D. Poghosyan<sup>1,2,3</sup>

<sup>1</sup>Yerevan State University, Yerevan, Armenia

<sup>2</sup>Institute of Mathematics of NAS RA, Yerevan, Armenia

<sup>3</sup>DiGREA lab, Center for Scientific Innovation and Education, Yerevan, Armenia

September 2, 2026

arXiv:2609.00895v1 [math.NA] 1 Sep 2026

