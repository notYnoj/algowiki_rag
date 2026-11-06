# A block \(\alpha\)-circulant based preconditioned MINRES method for wave equations

Xue-lei Lin<sup>1</sup> and Sean Hon<sup>2</sup>

**Abstract**

In this work, we propose an absolute value block \(\alpha\)-circulant preconditioner for the minimal residual (MINRES) method to solve an all-at-once system arising from the discretization of wave equations. Motivated by the absolute value block circulant preconditioner proposed in [E. McDonald, J. Pestana, and A. Wathen. SIAM J. Sci. Comput., 40(2):A1012-A1033, 2018], we propose an absolute value version of the block \(\alpha\)-circulant preconditioner. Since the original block \(\alpha\)-circulant preconditioner is non-Hermitian in general, it cannot be directly used as a preconditioner for MINRES. Our proposed preconditioner is the first Hermitian positive definite variant of the block \(\alpha\)-circulant preconditioner for the concerned wave equations, which fills the gap between block \(\alpha\)-circulant preconditioning and the field of preconditioned MINRES solver. The matrix-vector multiplication of the preconditioner can be fast implemented via fast Fourier transforms. Theoretically, we show that for a properly chosen \(\alpha\) the MINRES solver with the proposed preconditioner achieves a linear convergence rate independent of the matrix size. To the best of our knowledge, this is the first attempt to generalize the original absolute value block circulant preconditioner in the aspects of both theory and performance the concerned problem. Numerical experiments are given to support the effectiveness of our preconditioner, showing that the expected optimal convergence can be achieved.

_Keywords:_ Block Toeplitz matrix; convergence of MINRES solver; wave equations; absolute value block \(\alpha\)-circulant preconditioners

**Mathematics Subject Classification:** 15B05; 65F08; 65F10; 65M22

### 1. Introduction

Over the past few decades, the development of parallel-in-time (PinT) solvers for evolutionary partial differential equations (PDEs) has been an active research area. Various PinT methods have been proposed and, among these, two types of solvers are particularly of interest<tbc>

<sup>1</sup>School of Science, Harbin Institute of Technology, Shenzhen 518055, China. E-mail: linzuelei@hit.edu.cn <sup>2</sup>The Corresponding Author. Department of Mathematics, Hong Kong Baptist University, Kowloon Tong, Hong Kong SAR. E-mail: seanyshon@hkbu.edu.hk

