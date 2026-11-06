**Remark 6.1** _We remark that the tempered fractional derivative is discretized by the L_1 _finite difference scheme. Under the regularity assumption_ \(u(\cdot,t)\in C^2(0,T)\)_, the L_1 _approximation satisfies an error estimate of order_ \(O(\Delta t^{2-\xi})\)_, while the spatial L_1_- type discretization of the CFD yields an error of order_ \(O(\Delta x^{2-\eta})\)_. These estimates are standard and well documented for FDEs. However, due to the weak initial- time singularity typically exhibited by solutions of time-FDEs, the effective temporal convergence rate on uniform grids is often reduced to first order. Since the IP is regularized through the quasi-boundary value method, the resulting formulation is well posed. Consequently, the consistency of the space-time discretization, together with stability of the discrete scheme, ensures convergence of the numerical solution of the linear system_ (6.9) _to the solution of the regularized problem_ (6.2) _as_ \(\Delta x,\Delta t\rightarrow 0\)_, despite the first-order accuracy in time._

**Remark 6.2** _The structure of the matrix A<sub>N</sub> is very interesting because, up to a rank m correction, it is a block lower triangular matrix. This suggests two things: the first is either an easy to invert preconditioner or a plain Sherman-Morrison-Woodbury (SMW) direct solver plus possibly iterative refinement, the second is a technique for checking the invertibility of the matrix A<sub>N</sub>. As reported in the conclusions, the first item represents an additional research line which we leave for a future work, while the second is treated in detail here._

_We start from the expression of A<sub>N</sub> in (6.11). Let us consider the symmetric permutation matrix_<tbc>

\(\Pi_N:=\left[\begin{array}{ c c }
 & I_n \\
 & \ddots \\
I_n & 
\end{array}\right]\)

<tbc>_Hence A<sub>N</sub> is invertible if and only if_<tbc>

\(\Pi_NA_N\Pi_N=\left[\begin{array}{ c c }
Q_N & -\alpha_m\tilde{\mathbf{q}}\otimes I_n \\
\mathbf{e}_1^T\otimes I_n & \frac{\lambda}{\beta_n}G_n
\end{array}\right]\)

<tbc>_is invertible with_ \(\tilde{\mathbf{q}}:=\left[q^{(m)},\dots,q^{(1)}\right]^T\) _and_<tbc>

\(Q_N:=\left[\begin{array}{ c c c c c c }
Q_{m,m} & Q_{m,m-1} & \cdots & \cdots & Q_{m,1} \\
\mathrm{O}_n & Q_{m-1,m-1} & Q_{m-1,m-2} & \cdots & Q_{m-1,1} \\
\mathrm{O}_n & \mathrm{O}_n & Q_{m-2,m-2} & \cdots & Q_{m-2,1} \\
\vdots &  &  & \ddots & \ddots & \vdots \\
\mathrm{O}_n & \cdots & \cdots & \mathrm{O}_n & Q_{1,1}
\end{array}\right],\)

\(Q_{j,k}:=\left\{\begin{array}{ c c }
u_{j,k}I_n & \text{\textit{for}}j<k, \\
u_{j,j}I_n+\frac{\alpha_m}{\beta_n}G_n & \text{\textit{for}}j=k, \\
0 & \text{\textit{elsewhere}},
\end{array}\right.\)

<tbc>_in which u<sub>j,k</sub>_=\[_U<sub>n</sub>_\]_<sub>j,k</sub> are the entries of the matrix U<sub>n</sub> appearing in_ (6.11)_. For the first step of the block Gaussian elimination, let us define_<tbc>

\(P_N^{(1)}:=\left[\begin{array}{ c c c }
I_n &  &  \\
 & \ddots &  \\
-Q_{m,m}^{-1} &  & I_n
\end{array}\right].\)

