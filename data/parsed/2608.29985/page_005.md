<tbc>This preconditioner, P<sub>VBP</sub>, may alternatively be formulated via the splitting approach<tbc>

\(\mathscr{A}=\mathscr{P}_\mathrm{VBP}-\mathscr{R}_\mathrm{VBP},\) (7)

<tbc>where the remainder matrix is given by

\(\mathscr{R}_\mathrm{VBP}=\mathscr{P}_\mathrm{MBP}-\mathscr{A}=\left[\begin{array}{ c c }
\alpha I-\gamma W^2 & W-\gamma WT \\
0 & 0
\end{array}\right].\) (8)

The selection strategy for these parameters will be discussed in Section 4.

Utilizing the splitting established in (7) for our coefficient matrix A , we can introduce the subsequent VBP iterative scheme to solve the \(2\times 2\) block linear system (2)

**Method 2.1 (VBP Iteration Scheme):** Given an initial vector \((u^{(0)};v^{(0)})\in\mathbb{R}^{2n}\), the proposed VBP method produces a sequence of approximate solutions {(_u_<sup>(_k_)</sup>;_v_<sup>(_k_)</sup>)} utilizing the iteration<tbc>

\(\mathscr{P}_\mathrm{VBP}\left[\begin{array}{ c }
u^{(k+1)} \\
v^{(k+1)}
\end{array}\right]=\mathscr{R}_\mathrm{VBP}\left[\begin{array}{ c }
u^{(k)} \\
v^{(k)}
\end{array}\right]+\left[\begin{array}{ c }
g \\
f
\end{array}\right].\) (9)

<tbc>We can rewrite the iteration presented in (9) into a more compact form

\(\mathbf{u}^{(k+1)}=\mathscr{L}_\mathrm{VBP}\mathbf{u}^{(k)}+c,\) (10)

in which the iteration matrix is defined as

\(\mathscr{L}_\mathrm{VBP}=\mathscr{P}_\mathrm{VBP}^{-1}\mathscr{R}_\mathrm{VBP}=\left[\begin{array}{ c c }
T+\alpha I-\gamma W^2 & -\gamma WT \\
W & T
\end{array}\right]^{-1}\left[\begin{array}{ c c }
\alpha I-\gamma W^2 & W-\gamma WT \\
0 & 0
\end{array}\right],\) (11)

and the constant vector is \(c=\mathscr{P}_\mathrm{VBP}^{-1}\mathbf{d}\).

To wrap up this section, we examine how the P<sub>VPT</sub> preconditioner is implemented within the framework of Krylov subspace techniques to solve the linear system A**x**=**d**. At each iteration of a Krylov method such as GMRES or its flexible variant FGMRES, it is necessary to evaluate the inverse action of the preconditioning matrix. This translates to finding the solution for a linear equation structured as

\(\mathscr{P}_\mathrm{VBP}z=r,\)

in which the vectors are partitioned as _z_=(_z_<sub>1</sub>;_z_<sub>2</sub>) and _r_=(_r_<sub>1</sub>;_r_<sub>2</sub>). Here, the respective block components belong to the vector spaces \(z_1,r_1\in\mathbb{R}^n\), \(z_2,r_2\in\mathbb{R}^n\). The sequential procedure for determining _z_ such that P<sub>VBP</sub>_z=r_ is outlined below.

**Algorithm 1.** _Evaluating_ \(z=\mathscr{P}_\mathrm{VBP}^{-1}r\)

1. Solve \((\alpha I+T)z_1=r_1+\gamma Wr_2\) to find _z_<sub>1</sub>;

