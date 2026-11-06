**Remark 6.4** _In the special case where a(x_)=_a is constant, so that D<sub>n</sub>(a_)=_aI<sub>n</sub> and G<sub>n</sub>=aB<sub>n</sub>, a more efficient preconditioner can be constructed by approximating each Toeplitz matrix appearing in P<sub>N</sub> with the corresponding Strang preconditioner, as follows:_

\(S_N:=\left[\begin{array}{ c c }
S(U_m)\otimes I_n+I_m\otimes\frac{\alpha_m}{\beta_n}aS(B_n) & \mathrm{O}_{nm\times n} \\
\mathbf{e}_m^T\otimes I_n & \frac{\lambda}{\beta_n}aS(B_n)
\end{array}\right],\)

_where S(U<sub>m</sub>), S(B<sub>n</sub>_) _are the standard Strang preconditioners of U<sub>m</sub> and B<sub>n</sub>, respectively. Since circulant matrices are uniformly diagonalizable through the Fourier matrix F<sub>m</sub>, we can write_

\(S(U_m)=F_m\Lambda_m^{(1)}F_m^*,S(B_n)=F_n\Lambda_n^{(2)}F_n^*,\)

_where_ \(\Lambda_m^{(i)}\)_, i_=1,2_, are the diagonal matrices containing the eigenvalues and can be computed starting from the coefficients of U<sub>m</sub>, B<sub>n</sub> via the FFT. Then, S<sub>N</sub> becomes_

\(S_N:=\left[\begin{array}{ c c }
(F_m\otimes F_n)\big[\Lambda_m^{(1)}\otimes I_n+I_m\otimes\frac{\alpha_m}{\beta_n}a\Lambda_n^{(2)}\big](F_m\otimes F_n)^* & \mathrm{O}_{nm\times n} \\
\mathbf{e}_m^T\otimes I_n & \frac{\lambda}{\beta_n}aF_n\Lambda_n^{(2)}F_n^*
\end{array}\right].\)

_With this approach, the computational cost of inverting S<sub>N</sub> is of_ \(O\big(nm\mathrm{log}(nm)\big)\) _arithmetic operations, since all the necessary computations can be performed via the FFT. The same reasoning can be carried out using any suitable preconditioner for Toeplitz matrices, drawn from a matrix algebra which is uniformly diagonalizable through a fast transform._

**Remark 6.5** _From an implementation viewpoint, we can define a custom function that inverts P<sub>N</sub> through a forward substitution method, thanks to the block triangular structure of the matrix and the triangular structure of the blocks themselves. The computational cost amounts to O(n_<sup>2</sup>_m_<sup>2</sup>) _arithmetic operations. However, a linear system with coefficient matrix_ \(\frac{\lambda}{\beta_n}D_n(a)B_n=\frac{\lambda}{\beta_n}G_n\) _and variable coefficient a can be still solved within_ \(O\big(n\mathrm{log}n\big)\) _arithmetic operations as in Remark 6.4, while the more difficult additive structure in the other diagonal blocks_ \(\gamma_0I_n+\frac{\alpha_m}{\beta_n}G_n\) _can be treated e.g. via preconditioned GMRES and Strang preconditioner_ \(\frac{\alpha_m}{\beta_n}\bar{a}S(B_n)\)_, with_ \(\bar{a}\) _being an average of a(x), again within_ \(O\big(n\mathrm{log}n\big)\) _arithmetic operations._

## 6.4 Numerical results

We conclude by assessing the efficiency of our preconditioning strategy in terms of iterations required by the GMRES.

Let us consider problem (6.2) in which we set<tbc>

\(T=1,a(x)=x,q(t)=t^2,\varphi(x)=0.\)

<tbc>To construct the noisy final data, we select the source function<tbc>

\(f(x)=x\mathrm{sin}(\pi x)\)

