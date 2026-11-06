**GLT 7** _Let_ \(\{A_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa\) _and_ \(\{B_\mathbf{m}\}_\mathbf{m}\sim_\mathrm{GLT}\xi\) _with_

\(\kappa(x_1,\theta_1):[0,1]^{d_1}\times[-\pi,\pi]^{d_1}\rightarrow\mathbb{C},\)<br>
\(\xi(x_2,\theta_2):[0,1]^{d_2}\times[-\pi,\pi]^{d_2}\rightarrow\mathbb{C}.\)

_Then, it holds_

\(\{A_\mathbf{n}\}_\mathbf{n}\otimes\{B_\mathbf{m}\}_\mathbf{m}=\{A_\mathbf{n}\otimes B_\mathbf{m}\}_\mathbf{nm}\sim_\mathrm{GLT}\kappa\otimes\xi,\)

_where_ \((\kappa\otimes\xi):[0,1]^{d_1+d_2}\times[-\pi,\pi]^{d_1+d_2}\rightarrow\mathbb{C}\) _is given by_

\((\kappa\otimes\xi)(x_1,x_2,\theta_1,\theta_2):=\kappa(x_1,\theta_1)\xi(x_2,\theta_2),\)

_i.e., the tensor product is a_ (_d_<sub>1</sub>+_d_<sub>2</sub>)_-level GLT matrix sequence with scalar symbol. In particular, when d_<sub>1</sub>=_d_<sub>2</sub>=1_, the tensor product is a two-level GLT matrix sequence._

Note that, by **GLT 1**, it is always possible to obtain the singular value distribution from the GLT symbol, while the eigenvalue distribution can only be deduced either if the involved matrices are Hermitian or the related matrix-sequence is quasi- Hermitian in the sense of **GLT 5**.

## 4.6.1 GLT theory and preconditioning: a practical perspective

Before proceeding to the numerical applications in Part II, it is useful to clarify how the abstract GLT framework directly informs preconditioner design. The central idea is as follows: if a preconditioned matrix sequence has GLT symbol equal to the constant function 1, then, by GLT 1, its singular values are asymptotically distributed as 1. In other words, the singular values cluster at 1 in the weak sense. If, in addition, the matrices are Hermitian, the eigenvalues also cluster at 1. For non- Hermitian matrices, eigenvalue clustering at 1 may still be obtained under suitable additional assumptions, such as normality or the existence of a low-rank perturbation structure that allows the application of perturbation arguments \[12, 45\]. Such clustering is of significant practical importance: when the eigenvalues or singular values of the preconditioned matrix are clustered around 1, Krylov subspace methods such as GMRES or MINRES typically exhibit fast convergence. Thus, the GLT symbol serves as a powerful predictive tool: it not only describes the asymptotic spectral behavior of the coefficient matrices but also guides the construction of preconditioners whose symbols match those of the original matrices, thereby ensuring favorable convergence properties. Throughout the following chapters, this principle will be applied systematically to design and analyze preconditioners for ISPs of the FDEs.

