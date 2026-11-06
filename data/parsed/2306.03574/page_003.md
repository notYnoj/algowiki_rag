<tbc>all-at-once linear system from wave equation when \(\alpha\) is properly chosen. Numerical results in Section 3 also show that the ABAC preconditioner outperforms the ABC preconditioner.

More importantly, to the best of our knowledge, our proposed preconditioning method is the first work to show that a nontrivial symmetric positive definite version of block \(\alpha\)-circularant matrix can be constructed for the symmetrized the all-at-once system arising from wave equations, providing a positive answer to the open question discussed in \[32, Section 3\] that the construction and analysis of such a preconditioner is possible. We emphasize that the construction of our proposed preconditioner, involving the use of matrix square root on \(\alpha\)-circularant matrices, has rarely been seen in the relevant literature. Through this novel preconditioning idea, we hope to inspire and stimulate a new line of efficient algorithms for solving other more challenging PDEs, further enriching the PinT solver community.

It is worth noting that the use of ABAC preconditioners has recently been applied to dense block lower triangular Toeplitz systems \[27\]. However, we must emphasize that the theoretical results presented in \[27\] are not applicable to the wave equation considered in this work. This inapplicability arises because \[27, Assumption 1 (ii)\] is not satisfied by the matrix T to be defined in (1.2).

In this work, we are interested in solving the following linear wave equation as a model problem

\(\left\{\begin{array}{ c c }
u_{tt}(x,t)=\Delta u(x,t)+f(x,t), & (x,t)\in\Omega\times(0,T], \\
u=0, & (x,t)\in\partial\Omega\times(0,T], \\
u(x,0)=\psi_0,u_t(x,0)=\psi_1, & x\in\Omega.
\end{array}\right.\) (1.1)

For instance, a direct PinT solver was proposed in \[13\] for (1.1), where the so-called diagonalization technique \[33\] was used. For more about the existing solvers based on this diagonalization technique for solving the wave equation, we refer to the recent review paper \[15\].

Unlike a direct solver, we focus on a preconditioned iterative method for the equation in what follows. For solving (1.1), we adopt here the implicit leap-frog finite difference scheme used in \[32, 43\], which was established and shown in \[31\] to be unconditionally stable without the requirement of the restrictive Courant-Friedrichs-Lewy (CFL) condition on the mesh step sizes. Specifically, given a positive integer _n_, we let \(\tau=\frac{T}{n}\) be the time step size. Let _h_ denote the step size along each spatial direction and let _m_ denote the number of spatial grid points. For _k_=1_,...,n_-1, we have<tbc>

\(\frac{\mathbf{u}_m^{(k+1)}-2\mathbf{u}_m^{(k)}+\mathbf{u}_m^{(k-1)}}{\tau^2}=\Delta_h\frac{\mathbf{u}_m^{(k+1)}+\mathbf{u}_m^{(k-1)}}{2}+\mathbf{f}^{(k)},\)

<tbc>where \(\Delta_h\in\mathbb{R}^{m\times m}\) is the second-order discrete matrix approximating the Laplacian operator \(\Delta\) in (1.1), \(\mathbf{u}_m^{(k)}\in\mathbb{R}^{m\times 1}\) is an approximation to \(u(\mathcal{G}_h,k\tau)\), \(\mathbf{f}^{(k)}=f(\mathcal{G}_h,k\tau)\), G_<sub>h</sub>_ denoting the<tbc>

