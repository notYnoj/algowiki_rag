This gives iterates \(x_m=x_0+V_m\zeta_m\) with

\(\ell\text{GAL:}T_m\zeta_m=\|r_0\|_He_1,\) (2.3)

\(\ell\text{MR:}\zeta_m=\mathrm{argmin}\big\{\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|\big|_2\big\}.\) (2.4)

Note that in the formula for the _m_-th iterate of the \(\ell\)MR variant we find the standard 2-norm in the least squares problem for \(\zeta_m\).

The short recurrences for computing the iterates of \(\ell\)GAL and \(\ell\)MR with the _H_-inner product arise using an _LU_ or a _QR_ factorization of _T<sub>m</sub>_ or _T_<sub>_m_+1_,m_</sub> which is updated from one iteration to the next. All eigenvalues of _T<sub>m</sub>_ are of the form \(1+i\mu\) with \(\mu\in\mathbb{R}\) so that _T<sub>m</sub>_ as well as all its principal minors cannot become singular, which guarantees that a non-pivoted LU-factorization always exists. For the \(\ell\)MR variant one typically uses a _QR_ factorization of _T_<sub>_m_+1_,m_</sub> with an implicit representation of _Q_ as a sequence of Givens rotations and _R_ having three non-zero diagonals (the diagonal and two superdiagonals). Overall this process is analogous to the implementations proposed for SYMMLQ and MINRES in \[17\], to the implementation of the GAL, MR and ME methods in \[5\], to the implementation of \(\ell\)GAL in \[3\], \[27\] and of \(\ell\)MR in \[18\] and to the implementation of QMR as described in \[6\]. We therefore spare ourselves from reproducing technical details, the principles of which can also be found, e.g., in the textbooks \[12\], \[20\] and in \[23\].

**3. Right preconditioned and flexible methods.** If we multiply the original equation _Ax_=(_H+S)x=b_ with the imaginary unit _i_ we obtain

(3.1) \((iH+iS)x=ib.\)

In here _iS_=: _B_ is now Hermitian, and preconditioning with _H_<sup>-1</sup> yields a shifted _H_-selfadjoint matrix _H_<sup>-1</sup>(_iH+B_)=_iI+H_<sup>-1</sup>_B_.

In his 1990 paper, Freund \[5\] considers CG type methods for matrices of the form

\(i\sigma I+W,W^*=W,\sigma\in\mathbb{R}.\)

There, three short recurrence Krylov subspace methods, all within the framework of the standard \(\ell_2\) inner product are developed: GAL, MR and ME. GAL is variationally characterized by a Galerkin condition, MR by a minimal residual condition, and ME ("minimal error") minimizes the error in 2-norm over the subspace \(x_0+(i\sigma I+W)^*K_m(i\sigma I+W,r_0)\). The ME approach dates back to \[7\] for the case \(\sigma=0\) and is less commonly used today. In our numerical experiments it behaved quite similarly as the other methods, but with slightly larger errors and residuals than GAL, so we do not consider this variant any further in this paper.

The methods in \[5\] can be easily adapted to work with the _H_-inner product rather than with the standard inner product. The requirement is that _W_ is then an _H_-selfadjoint matrix, which is exactly the situation that arises when we precondition (3.1) with _H_<sup>-1</sup>, yielding _W=H_<sup>-1</sup>_B_ (and \(\sigma=1\)). For any vector _r_, the Krylov subspaces \(\mathcal{K}(i\sigma I+H^{-1}B,ir)\) and \(\mathcal{K}(\sigma I+H^{-1}S,r)\) are identical. This means that for a given initial guess _x_<sub>0</sub>, the defining Galerkin conditions produce identical iterates, independently of whether we consider \((\sigma I+H^{-1}S)x=b\) with initial residual \(r=b-(\sigma I+H^{-1}S)x_0\) or \((i\sigma I+B)x=ib\) with initial residual \(ib-(i\sigma I+B)x_0=ir\). The same holds for the minimal residual based methods. We emphasize this relation in the following proposition for the case \(\sigma=1\).

Proposition 3.1. _Freund’s GAL method with the H-inner product for_ (_iI+H_<sup>-1</sup>_B)x=ib is identical to the Concus and Golub / Widlund method for_ (_I_+<tbc>

