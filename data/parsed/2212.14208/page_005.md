One can work with \(\sigma I+SH^{-1}\) rather than with \(i\sigma I+BH^{-1}\) in Algorithm 3.1, adapting the matrix vector multiplication in line 4 and changing the last summand \(-\beta_{k-1}v_{k-1}\) to \(+\beta_{k-1}v_{k-1}\) in line 6. The reason for the latter is that due to the fact that _SH_<sup>-1</sup> is _H_<sup>-1</sup>-anti selfadjoint we now have \(\langle w,\widetilde{v}_{k-1}\rangle=-\langle H^{-1}v_k,\beta_{k-1}v_k\rangle\). This observation represents the general transition rule from formulations for the systems with \(i\sigma I+BH^{-1},i\sigma I+H^{-1}B\) or \(i\sigma H+B\) to systems with \(\sigma I+SH^{-1},\sigma I+H^{-1}S\) or \(\sigma H+S\). Our presentation will continue to be based on the systems using _B_ rather than _S_.

Right preconditioning is the key to develop flexible variants of the GAL, MR and ME methods. The term "flexible" includes "inexact" methods in which \(\widetilde{w}=H^{-1}w\) is replaced by \(\widehat{w}=\widehat{H}^{-1}w\) with a fixed matrix \(\widehat{H}\). For example, \(\widehat{H}\) may result from an incomplete Cholesky factorization. "Flexible" also includes the more general possibility to approximate _H_<sup>-1</sup>_w_ via a non-stationary iteration such as (possibly preconditioned) CG which, formally, means that \(\widehat{H}\) changes from one approximate solve to the next.

**3.2. Flexible methods.** Using exact multiplications with _H_<sup>-1</sup>, the Lanczos algorithm given in Algorithm 3.1 for the right preconditioned matrix \(i\sigma I+BH^{-1}\) produces the relation

(3.2) \((i\sigma I+BH^{-1})V_m=V_{m+1}T_{m+1,m},\)

with<tbc>

\(T_{m+1,m}=\left[\begin{array}{ c c c c c c c c c }
\alpha_1 & \beta_1 &  &  &  &  &  &  &  \\
\beta_1 & \alpha_2 & \beta_2 &  &  &  &  &  &  \\
 & \beta_2 & \ddots &  & \ddots &  &  &  &  \\
 &  & \ddots &  & \ddots &  & \beta_{m-1} &  \\
 &  &  &  & \beta_{m-1} &  & \alpha_m &  \\
 &  &  &  &  &  & \beta_m &  \\
\end{array}\right],\)

<tbc>where now _V<sub>m</sub>_ has _H_<sup>-1</sup>-orthonormal columns. The transformation of an iterate<tbc>

\(\widetilde{x}_m=x_0+V_m\zeta_m\)

<tbc>for the right preconditioned system back to the iterate \(x_m=H^{-1}\widetilde{x}_m=H^{-1}x_0+H^{-1}V_m\zeta_m\) of the original system is most easily done via a short recurrence update using the preconditioned Lanczos vectors \(\widetilde{v}_m=H^{-1}v_m\) which we compute anyways. The relation (3.2) can then be stated as

(3.3) \((i\sigma H+B)\underbrace{\widetilde{V}_m}_{=H^{-1}V_m}=V_{m+1}T_{m+1,m}.\)

We can now divise a flexible method in a manner similar to what has been done for FGMRES, the flexible GMRES method \[26\] and, with regard to short recurrences, in flexible QMR \[24\], e.g. Assume that _z<sub>k</sub>_ is only an approximation to _H_<sup>-1</sup>_v<sub>k</sub>_ and proceed as follows:

1. Compute \(w=(i\sigma H+B)z_k\)<tbc>

2. _H_<sup>-1</sup>-orthogonalize _w_ against _v<sub>k</sub>_ and _v_<sub>_k_-1</sub> _approximately_. This means that the inner products \(\langle w,v_k\rangle_{H^{-1}}\) and \(\langle w,v_{k-1}\rangle_{H^{-1}}\) are obtained as standard inner products with \(\widehat{w}\) where \(\widehat{w}\) is an approximation to _H_<sup>-1</sup>_w_.<tbc>

