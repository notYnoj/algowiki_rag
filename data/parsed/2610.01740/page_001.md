# TOEPLITZ INFINITE GMRES FOR PARAMETERIZED LINEAR SYSTEMS

**Abstract.** We develop Toeplitz infinite GMRES for solving large sparse analytic parameterized systems _A(s)x(s_)=_z_ at many parameter values. Our method exploits a block upper triangular Toeplitz structure in the companion Krylov sequence to construct the Arnoldi process and recover solution approximations without storing full Arnoldi vectors. We derive incremental recurrences requiring O(_np_<sup>2</sup>+_p_<sup>3</sup>) arithmetic and O(_np+p_<sup>2</sup>) storage for _p_ Arnoldi steps, excluding factorization setup and assuming linear-cost coefficient actions and triangular solves. A dynamic generator-refreshing strategy addresses cancellation in this basic recurrence. Moreover, we show that the Arnoldi basis can be simply represented using one block row and a nilpotent matrix. For _A(s_) admitting a split form, we further use this structure to develop an implicitly rebased method. A residual lower bound for square-summable Taylor coefficients explains the effect of scaling outside the unit disk. Theoretical analysis and numerical experiments illustrate the computational efficiency of the proposed methods.

**Key words.** parameterized linear systems, Krylov methods, infinite Arnoldi, Toeplitz matrices, companion linearization

**MSC codes.** 65F10, 65F15, 65F50, 65H17

### 1. Introduction.

We consider the repeated solution of

\(A(s)x(s)=z,s\in\mathbb{C},\)

where \(A(s)\in\mathbb{C}^{n\times n}\) is large, sparse, and analytic, and \(z\in\mathbb{C}^n\) is fixed. Such systems arise in parameter-dependent partial differential equations, transfer-function evaluation, and contour-integral methods for nonlinear eigenvalue problems. When many parameter values are required, factoring each matrix _A(s_) separately is often too expensive.

GMRES [19] methods for shifted linear systems exploit Krylov shift invariance to reuse a common search space [7]. Infinite GMRES (infGMRES) [10] applies this principle to analytic parameterized systems through a Taylor companion linearization. It constructs one Arnoldi factorization for all parameter values and solves only a small parameter-dependent least-squares problem for each _s_. Extensions include inexact preconditioning [6] and a two-level orthogonal Arnoldi (TOAR) implementation for contour-integral nonlinear eigensolvers [16]. Related compact representations appear in infinite and tensor infinite Arnoldi methods [11-13,18,20] and in TOAR methods [17,22] for polynomial linearizations [15], as well as in the compact rational Krylov (CORK) framework [21].

Constructing this Arnoldi basis is still expensive. Suppose that coefficient-matrix products and triangular solves using one stored LU factorization require O(_n_) arithmetic. For _p_ steps, direct infGMRES then has O(_np_<sup>3</sup>) arithmetic and O(_np_<sup>2</sup>) storage complexity. With TOAR techniques, TOAR infGMRES reduces storage complexity to O(_np+p_<sup>3</sup>), but still needs O(_np_<sup>3</sup>+_p_<sup>4</sup>) arithmetic complexity due to the construction of full Arnoldi vectors.

Our approach exploits the Toeplitz structure in the companion Krylov sequence and updates only the QR data needed for solution recovery. Fast QR methods for

<sup>∗</sup>School of Mathematical Sciences, Fudan University, Shanghai 200433, China & Shanghai Key Laboratory of Contemporary Applied Mathematics, Shanghai, China, 200433 (wggao@fudan.edu.cn). <sup>†</sup>School of Mathematical Sciences, Fudan University, Shanghai 200433, China (fyjiang26@m.fudan.edu.cn).

WEIGUO GAO<sup>∗</sup> AND FEIYANG JIANG<sup>†</sup>

arXiv:2610.01740v2 [math.NA] 26 Oct 2026

