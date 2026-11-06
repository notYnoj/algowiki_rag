<tbc>numerous scientific and engineering contexts, such as molecular scattering \[24\], structural dynamics \[17\]. Additional examples may be found in \[12, 33\] and the references cited therein.

Assuming that the matrix A is large and sparse, iterative techniques are generally preferred over direct solvers, such as Gaussian elimination, for solving systems of the form (1). When the matrices _W_ and _T_ are positive semidefinite, with at least one of them being positive definite, several iterative methods and preconditioning techniques have been developed for systems such as (1).

In 2000, Axelsson and Kucherov proposed the C-to-R method \[1\]. In 2008, Bai \[8\] introduced several splitting for non-Hermitian linear systems. Bai et al. \[6\] in 2010, proposed the modified Hermitian and skew-Hermitian splitting (MHSS) iteration method, which bypasses the need to solve a shifted skew-Hermitian linear system at each iteration. Following this, in 2011, a preconditioned variant of MHSS, known as the PMHSS method, was introduced by Bai et al. \[7\]. This variant has been demonstrated to achieve remarkably superior computational efficiency compared to its predecessor. In 2015, Wu \[33\] proposed several variants of the HSS method for solving a class of complex symmetric linear systems. In 2015, Salkuyeh et al. \[30\] proposed the generalized SOR iterative method for solving a class of complex symmetric linear systems, while in the same year, Hezari et al. \[18\] developed the preconditioned GSOR iterative method. To enhance the convergence rate of the GSOR method, Edalatpour et al. \[16\] proposed an accelerated variant, termed AGSOR, which incorporates two acceleration parameters. In 2016, Hezari et al. \[19\] proposed a new iterative method for solving a class of complex symmetric linear systems. In 2017, Wang et al. \[32\] proposed the combination method of real and imaginary parts (CRI) for solving complex symmetric linear systems. In 2018, Li et al. \[22\] constructed a symmetric block triangular splitting (SBTS) iteration method based on two distinct splittings. Later, in 2018, Axelsson and Salkuyeh \[2\] presented the transformed matrix preconditioner (TMP) approach.

In order to circumvent the need for complex arithmetic, a widely adopted technique is to transform the original complex linear system (1) into an equivalent real block system of dimension \(2\times 2\). By employing the real-equivalent reformulation described in \[11\], we decompose the complex solution and right-hand side vectors as **x**=_u+iv_ and **d**=_f+ig_, respectively. Consequently, the system can be expressed in the following real block form

\(\mathscr{A}\mathbf{x}\equiv\left[\begin{array}{ c c }
T & -W \\
W & T
\end{array}\right]\left[\begin{array}{ c }
u \\
-v
\end{array}\right]=\left[\begin{array}{ c }
g \\
f
\end{array}\right]\equiv\mathbf{d},\) (2)

From now on, we assume that \(W\in\mathbb{R}^{n\times n}\) is symmetric indefinite and \(T\in\mathbb{R}^{n\times n}\) is symmetric positive definite.

Due to the high dimensionality and sparse nature of the coefficient matrix A in the \(2\times 2\) block linear system (2), applying direct factorization methods typically incurs severe fill- in. This not only imposes prohibitive memory requirements but also significantly degrades computational efficiency, rendering direct solvers impractical for large-scale, real-world appli<tbc>

