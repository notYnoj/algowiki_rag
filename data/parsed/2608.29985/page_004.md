<tbc>Building upon the HSS preconditioning framework and incorporating relaxation techniques, Shen and Shi \[31\] introduced a variant of the HSS preconditioner (VHSS), defined by

\(\mathscr{P}_\mathrm{VHSS}=\frac{1}{2\alpha}\left[\begin{array}{ c c }
\alpha I+T & 0 \\
0 & 2\alpha I
\end{array}\right]\left[\begin{array}{ c c }
\alpha I-W & W \\
W & T
\end{array}\right]=\frac{1}{2}\left[\begin{array}{ c c }
\alpha I+T & \left(I+\frac{1}{\alpha}T\right)W \\
2W & 2T
\end{array}\right].\) (4)

More recently, Balani and Hajarian \[9\] proposed a modified block product (MBP) preconditioner of the form

\(\mathscr{P}_\mathrm{MBP}=\left[\begin{array}{ c c }
T & 0 \\
W & \alpha T
\end{array}\right]\left[\begin{array}{ c c }
I & -\frac{1}{\alpha}W \\
0 & I
\end{array}\right]=\left[\begin{array}{ c c }
T & -\frac{1}{\alpha}TW \\
W & \alpha T-\frac{1}{\alpha}W^2
\end{array}\right].\) (5)

In this paper, we propose a variant of the block preconditioner for complex symmetric systems, which we refer to as the VBP preconditioner. This new preconditioner is derived from a matrix splitting approach and is designed for solving the large sparse \(2\times 2\) block complex symmetric indefinite linear system of the form (2).

Throughout this paper, \(\rho(A)\), tr(_A_), \(\|A\|_2\) and \(\|A\|_F\) denote the spectral radius, trace, the Euclidean norm and the Frobenius norm of matrix _A_, respectively. \(\lambda_\mathrm{max}(A)\) and \(\lambda_\mathrm{min}(A)\) denote the largest eigenvalue and the smallest eigenvalue of matrix _A_, respectively. For a vector \(x\in\mathbb{C}^n\), _x_<sup>∗</sup> is used for the conjugate transpose of _x_. For two vectors _x_ and _y_, the Matlab notation (_x;y_) is used for (_x<sup>T</sup>,y<sup>T</sup>)<sup>T</sup>_ (or for (_x_<sup>∗</sup>_,y_<sup>∗</sup>)<sup>∗</sup>).

The remainder of this paper is organized as follows. In Section 2, we present the detailed construction of the proposed VBP preconditioner and analyze the convergence properties of the associated iterative method. Practical implementation aspects, including computational complexity and storage requirements, are also discussed in this section. Section 3 is devoted to a thorough investigation of the spectral properties of the preconditioned matrix \(\mathscr{P}_\mathrm{VBP}^{-1}\mathcal{A}\), providing theoretical insights into the convergence behavior. The strategy for selecting the optimal preconditioner parameters \(\alpha\) and \(\gamma\) is described in Section 4. In Section 5, we conduct extensive numerical experiments to evaluate the performance, efficiency, and robustness of the proposed approach in comparison with existing preconditioners such as VHSS, BS, and MBP. Finally, Section 6 concludes the paper with some concluding remarks and discusses possible directions for future research.

## 2 The VBP preconditioner and convergence analysis

In this section, we introduce a variant of the block preconditioner (denoted as VBP) for complex symmetric systems. Let \(\alpha>0\) and \(\gamma\) be a positive real parameters. Using the \(2\times 2\) block matrix A given in (2), we construct the preconditioner block approach as follows

\(\mathscr{P}_\mathrm{VBP}=\left[\begin{array}{ c c }
T+\alpha I & -\gamma W \\
0 & I
\end{array}\right]\left[\begin{array}{ c c }
I & 0 \\
W & T
\end{array}\right]=\left[\begin{array}{ c c }
T+\alpha I-\gamma W^2 & -\gamma WT \\
W & T
\end{array}\right].\) (6)

