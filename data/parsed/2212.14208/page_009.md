Proposition 4.3. _Assume that the inexact solves_ \(\widehat{w}\approx H^{-1}w\) _in Algorithm 3.2 are done in one of the following ways_

(_i)_ _by performing k steps of the CG method with initial guess 0,_<tbc>

_(ii)_ _by performing k steps of the preconditioned CG method with initial guess 0 and a Hermitian positive definite preconditioner K,_<tbc>

_(iii)_ _as_ \(\widehat{w}=Gw\) _with_ \(G\in\mathbb{C}^{n\times n}\) _Hermitian and positive definite. Then, if_ \(w\neq 0\)_, we have_ \(\beta=\langle w,\widehat{w}\rangle>0\).

_Proof._ In case (i), the initial residual for the CG method is _w_, and with the columns of \(W\in\mathbb{C}^{n\times k}\) being the Lanczos vectors which form an orthonormal basis of the Krylov subspace K_<sub>k</sub>(H,w_), we know that \(\widehat{w}=V_k(V_k^*HV_k)^{-1}V_k^*w\); see e.g. \[12\] or \[20\]. Thus, \(\beta_m=\langle w,\widehat{w}\rangle=\langle V_k^*w,(V_k^*HV_k)^{-1}V_k^*w\rangle\), and this quantity is positive as \(V_k^*HV_k\) is Hermitian positive definite and \(V_k^*w=\|w\|_2e_1\), _e_<sub>1</sub> the first canonical unit vector in C_<sup>k</sup>_, is non-zero.

Case (ii) follows in a similar manner as (i), replacing _V<sub>k</sub>_ by the matrix of _K_- orthonormal Lanczos vectors for K_<sub>k</sub>(K_<sup>-1</sup>_H,K_<sup>-1</sup>_w_).

In case (iii), as _G_ is Hermitian positive definite and \(w\neq 0\), we immediately have \(\beta=\langle w,\widehat{w}\rangle=\langle w,Gw\rangle>0\). □

An important example for case (iii) above is when _G=L_<sup>-1</sup>_L_<sup>-∗</sup> with _L_ a sparse lower triangular matrix arising from an incomplete Cholesky factorization of _H_, _H=L_<sup>∗</sup>_L-R_. Such _G_ is also a typical preconditioner _K_<sup>-1</sup> for case (ii). Another important example for (iii) are Galerkin based multigrid methods for Hermitian positive definite systems with symmetric pre- and post-smoothing and exact coarsest level solves.

The second property we want to stress deals with \(\|b-Ax_m\|_{H^{-1}}\) as a measure of the error of iterate _x<sub>m</sub>_. Using _b-Ax<sub>m</sub>=A(x_<sub>∗</sub>-_x<sub>m</sub>_), we have

\(\|b-Ax_m\|_{H^{-1}}^2=\langle A(x_*-x_m),A(x_*-x_m)\rangle_{H^{-1}}\)<br>
\(=\langle x_*-x_m,x_*-x_m\rangle_{A^*H^{-1}A}=\|x_*-x_m\|_{A^*H^{-1}A}^2\)

with

\(A^*H^{-1}A=(-i\sigma H+B)H^{-1}(i\sigma H+B)=\sigma^2H+BH^{-1}B.\)

Thus, if _H_ dominates _S_, i.e., if _H_<sup>-1</sup>_B_ is small, the matrix _AH_<sup>-1</sup>_A_ is close to \(\sigma^2H\) (and we have equality if _B_=0). Consequently, when _H_ dominates _B_, up to the trivial factor \(\sigma^2\), the norm \(\|b-Ax_m\|_{H^{-1}}\) is a good approximation to the _H_-norm of the error. There are multiple reasons why in the case _B_=0 the _H_-norm of the error--and not its \(\ell_2\)-norm nor the \(\ell_2\)-norm of the residual, e.g.--should be considered the most adequate measure for the error, in particular when the linear systems arise from a discretization of an underlying continuous, infinite-dimensional equation; see \[1, 13\], e.g. Even if \(B\neq 0\), the _H_-norm can still be regarded as the canonical measure for the error. By the following proposition, an approximate bound for this norm is available at almost no cost for the FMR iterates.

Proposition 4.4. _Let v<sub>k</sub>,k_=1_,...,m, denote the vectors produced by the flexible Lanczos algorithm, Algorithm 3.2, and let_ \(\varrho_m\) _be the value of the minimum in the defining equation_ (3.8) _of the FMR iterate x<sub>m</sub>, i.e._<tbc>

\(\varrho_m:=min_{\zeta\in\mathbb{C}^m}\{\|\beta_0e_1-T_{m+1,m}\zeta\|_2\}.\)

<tbc>_Then_

(4.2) \(\|b-Ax_m\|_{H^{-1}}\le\|V_{m+1}\|_{H^{-1}}\cdot\varrho_m,\)

