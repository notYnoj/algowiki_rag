<tbc>cations. To address these limitations, extensive research has focused on developing iterative schemes that preserve and exploit the system’s sparsity. Among these, Krylov subspace methods--most notably the generalized minimal residual (GMRES) algorithm \[28\] and its flexible variant (FGMRES) \[27\]--have proven highly effective, as they rely solely on matrix-vector multiplications, thereby preserving the original sparsity pattern.

In the following, we review some of the existing research in this area, particularly for the case where the matrix _W_ is symmetric indefinite and _T_ is SPD, for solving complex symmetric linear systems (2), numerous iterative methods have been proposed in the literature, encompassing both stationary iteration schemes and Krylov subspace methods, the latter often being equipped with preconditioners to enhance convergence. In 2017, Li and Wu \[34\] introduced the modified positive/negative stable splitting (MPNS) method. In 2021, Pourbagher and Salkuyeh \[25\] put forward the symmetric positive definite and negative stable splitting (SNSS) method. In 2022, Axelsson et al. \[3\] developed three iteration schemes for system (1) under the assumption that _W=W_<sub>1</sub>-_W_<sub>2</sub>, with both _W_<sub>1</sub> and _W_<sub>2</sub> being SPD. They also employed the resulting preconditioners to accelerate the convergence of GMRES when applied to (1). Also in 2022, Zheng et al. \[36\] proposed the VPMHSS method.

More recently, in 2025, Chen and Wu \[15\] proposed two efficient iteration methods for solving complex symmetric indefinite linear systems. In the same year, Liang and Dou \[23\] proposed modified CRI (combination of real and imaginary parts) iteration methods. Also in 2025, Salkuyeh \[29\] proposed a preconditioner for complex symmetric systems of linear equations with an indefinite Hermitian part.

Given that in this study, the matrices _T_ and _W_ are symmetric positive definite and symmetric indefinite, respectively, we introduce some effective methods that share this structure in detail.

It is well established that the convergence and performance of Krylov subspace methods depend heavily on the quality of the preconditioner. Consequently, a substantial body of literature has been dedicated to designing and analyzing efficient preconditioning techniques. Specifically, building upon the HSS iteration framework introduced by Bai et al. \[5\], various adapted HSS-based iteration schemes have been developed for the real \(2\times 2\) block system (2), formulated as follows<tbc>

\(\mathscr{P}_\mathrm{HSS}=\frac{1}{2\alpha}\left[\begin{array}{ c c }
\alpha I+T & 0 \\
0 & \alpha I+T
\end{array}\right]\left[\begin{array}{ c c }
\alpha I-W & W \\
W & \alpha I
\end{array}\right]=\frac{1}{2}\left[\begin{array}{ c c }
\alpha I+T & \left(I+\frac{1}{\alpha}T\right)W \\
\left(I+\frac{1}{\alpha}T\right)W & \alpha I+T
\end{array}\right].\) (2)

<tbc>Subsequently, Zhang and Dai \[35\] employed a relaxation strategy to construct the block splitting (BS) preconditioner, formulated as

\(\mathscr{P}_\mathrm{BS}=\left[\begin{array}{ c c }
I & -W \\
\frac{1}{\alpha}W & T
\end{array}\right]\left[\begin{array}{ c c }
\alpha I+T & 0 \\
0 & I
\end{array}\right]=\left[\begin{array}{ c c }
\alpha I+T & -W \\
W\left(I+\frac{1}{\alpha}T\right) & T
\end{array}\right].\) (3)

