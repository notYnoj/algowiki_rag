# A variant of the block preconditioner for indefinite complex symmetric linear systems

**Mehdi Makhdomi**<sup>†</sup> **and Davod Khojasteh Salkuyeh**<sup>‡∗</sup>

<sup>†</sup> _Department of Mathematics, University of Kurdistan, P.O. Box 416, Sanandaj, Iran_

<sup>‡</sup> _Faculty of Mathematical Sciences, University of Guilan, Rasht, Iran_

Emails: mehdi.ap.math@gmail.com, khojasteh@guilan.ac.ir,

**Abstract.** In this paper, we propose an efficient preconditioner for solving indefinite complex symmetric linear systems within a block preconditioning framework. We analyze the convergence of the corresponding iterative method and investigate several spectral properties of the preconditioned matrix, including eigenvalue distributions and eigenvector structures. The new preconditioner is used to accelerate the convergence of the flexible version of GMRES. Numerical experiments are presented to illustrate the effectiveness of the proposed preconditioner, and comparisons with existing block preconditioners demonstrate its superior performance.

**_Keywords:_** Complex, symmetric, linear systems, Convergence analysis, preconditioner, GMRES. _AMS Subject Classification:_ 65F10, 65F50, 65F08..

### 1 Introduction

This study is concerned with computing an approximate solution to the system of linear equations

where \(\mathcal{A}=W+iT\in\mathbb{C}^{n\times n}\) is complex symmetric (\(W,T\in\mathbb{R}^{n\times n}\) are symmetric), \(u,v,f,g\in\mathbb{R}^n\) and \(i=\sqrt{-1}\) denotes the imaginary unit. The linear system (1) appears frequently in

<sup>∗</sup>Corresponding author.

\(\mathcal{A}\mathbf{x}\equiv(W+iT)\mathbf{x}=\mathbf{d},\mathbf{x}=u+iv,\mathbf{d}=f+ig,\) (1)

