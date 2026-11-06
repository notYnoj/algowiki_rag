For more general self-adjoint boundary value problems, in particular for Sturm-Liouville and Dirac systems, the analogue of Krylov’s correction polynomial is no longer a Bernoulli polynomial but a combination of derivatives of the Green’s function of the underlying operator. The basic algebraic identity behind the method, an integration-by-parts decomposition of _c<sub>n</sub>_ into a boundary part _P<sub>n</sub>_ and a smoother interior part _F<sub>n</sub>_, was extended by J. Shaw, L. Johnson and R. Riess \[24\] and, in the form most relevant here, by A. Nersessian and A. Poghosyan \[18, 20, 19\]. The Gibbs phenomenon in eigenfunction expansions of the one-dimensional Dirac system was studied in \[4\]. For the same system, by R. Barkhudaryan obtained in \[2, 3\] a generalization of the Eckhoff method under the assumption that the boundary values of _f_ and of its successive Dirac iterates are known _exactly_, and computed the asymptotic _L_<sub>2</sub> constant of the resulting approximation.

In the current paper we consider the case when these boundary values are not known in advance and have to be _computed_ from the Fourier coefficients \(\{c_n\}_{|n|\le N}\) themselves, exactly as Eckhoff proposed in the trigonometric case. The boundary conditions on the eigenfunctions reduce the 4_q_ scalar boundary values of _f_ to 2_q reduced boundary values_ \(g_k^\pm\), and Eckhoff’s recipe, applied at 2_q_ selected indices _n<sub>s</sub>_, leads to a linear system for their approximations \(\widetilde{g}_k^\pm\) -- the KEG-D system -- whose coefficient matrix is a \(2q\times 2q\) _block Vandermonde matrix_, the natural generalization of the \(q\times q\) Vandermonde matrix of the original Eckhoff method. Accordingly, in Section 1 we recall the Dirac boundary value problem and the exact-jumps form of the convergence acceleration of \[2\]; in Section 2 we prove a closed-form expression for the determinant of the block Vandermonde matrix and describe its inverse; in Section 3 we set up the KEG-D system and estimate the errors \(\widetilde{g}_k^\pm-g_k^\pm\), showing in particular that strict parity balance is necessary and sufficient for the leading-order coefficient matrix to be nonsingular; and in Section 4 we prove the main result of the paper (Theorem 4.1), an explicit formula for the limit of \(N^{2q+1}\|\widetilde{R}_{q,N}(f)\|^2\) in terms of the Dirac jump constants.

## 1 The Dirac system and exact-jumps method

We work with the canonical Dirac system on \[-1,1\]<tbc>

\(\left(\begin{array}{ c c }
0 & 1 \\
-1 & 0
\end{array}\right)\frac{dy}{dx}-\left(\begin{array}{ c c }
p(x) & 0 \\
0 & r(x)
\end{array}\right)y=\lambda y,\) (1)

<tbc>with separated self-adjoint boundary conditions

\(y_2(-1)cos\alpha+y_1(-1)sin\alpha=0,y_2(1)cos\beta+y_1(1)sin\beta=0,\) (2)

where \(p,r\in C^1[-1,1]\) are real-valued and \(\alpha,\beta\in[0,\pi]\). We assume that \(\lambda=0\) is not an eigenvalue. This entails no loss of generality, since the spectrum is discrete and a constant spectral shift may always be made so that zero does not belong to the spectrum.

Let \(\{\lambda_n\}_{n\in\mathbb{Z}}\) be the eigenvalues, indexed in increasing order, with the origin of the indexing chosen consistently with the asymptotic formula below, so that \(\lambda_n\rightarrow\pm\infty\) as \(n\rightarrow\pm\infty\). Let {_v<sub>n</sub>_} be the corresponding real orthonormal eigenfunctions in _L_<sub>2</sub>(\[-1,1\];R<sup>2</sup>). The asymptotic results of Levitan-Sargsyan \[16\] give

\(v_{n,1}(x)=K_0cos(\xi_n(x)-\alpha)+O(1/n),v_{n,2}(x)=K_0sin(\xi_n(x)-\alpha)+O(1/n),\) (3)

as \(n\rightarrow\pm\infty\), uniformly for \(x\in[-1,1]\), where

\(\xi_n(x):=\lambda_n(x+1)+\frac{1}{2}\int_{-1}^x\left(p(\tau)+r(\tau)\right)d\tau.\) (4)

