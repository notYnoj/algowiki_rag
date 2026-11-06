the coefficient \(g_0^{(\alpha)}\), which is nonnegligible while \(g_N^{(\alpha)}\) tends to zero as _N_ tends to infinity; see also the Riemann-Lebesgue lemma \[141\].<br>
It is well known that any circulant matrix _C<sub>N</sub>_ can be diagonalized by the Fourier matrix, i.e.,

\(C_N=F_N\Lambda_NF_N^*,\)

where _F<sub>N</sub>_ is the unitary matrix given by (3.3) and \(\Lambda_N\) is a diagonal matrix containing the eigenvalues of _C<sub>N</sub>_.

**Theorem 8.5** _Let_ \(P\in\{\widetilde{P}_{\alpha,N,M},\widehat{P}_{\alpha,N,M}\}\) _as defined in_ (8.35) _and in_ (8.36)_, respectively. Set_ \(U=F_N\otimes I_M\)_. Then P is unitarily similar to a block diagonal matrix, namely_

\(U^*PU=\mathrm{blkdiag}\big(\gamma d\lambda_jI_M+Q_{\theta,M}\big)_{j=1}^N,\) (8.37)

_where_ \(\lambda_j\)_, j_=1_,...,N, denote the eigenvalues of the circulant block_ \(\tilde{C}_{\alpha,N}\) _or_ \(\hat{C}_{\alpha,N}\)_, respectively. Moreover, each diagonal block_

\(D_j=\gamma d\lambda_jI_M+Q_{\theta,M},j=1,\dots,N,\) (8.38)

_is an invertible lower triangular Toeplitz matrix (ILTT)._

**Proof:** Substituting the diagonalization of the circulant matrix into (8.35) (or into (8.36) equivalently) gives<tbc>

\(P=\gamma dF_N\Lambda_{\alpha,N}F_N^*\otimes I_M+I_N\otimes Q_{\theta,M}.\)

<tbc>Then, using the mixed-product property \((A\otimes B)(C\otimes D)=AC\otimes BD\), it holds that

\(U^*PU=\left(F_N^*\otimes I_M\right)\left(\gamma dF_N\Lambda_{\alpha,N}F_N^*\otimes I_M+I_N\otimes Q_{\theta,M}\right)\left(F_N\otimes I_M\right)\)<br>
\(=\gamma dF_N^*F_N\Lambda_{\alpha,N}F_N^*F_N\otimes I_M+F_N^*F_N\otimes Q_{\theta,M}\)<br>
\(=\gamma d\Lambda_{\alpha,N}\otimes I_M+I_N\otimes Q_{\theta,M}.\)

Since \(\Lambda_{\alpha,N}=\mathrm{diag}(\lambda_1,\dots,\lambda_N)\), it follows that<tbc>

\(\Lambda_{\alpha,N}\otimes I_M=\mathrm{blkdiag}(\lambda_1I_M,\dots,\lambda_NI_M),I_N\otimes Q_{\theta,M}=\mathrm{blkdiag}(Q_{\theta,M},\dots,Q_{\theta,M}).\)

<tbc>Hence their sum is block diagonal with blocks \(\gamma d\lambda_jI_M+Q_{\theta,M}\), _j_=1_,...,N_. Finally, note that \(Q_{\theta,M}\) is a lower triangular Toeplitz matrix, and adding a scalar multiple of the identity preserves both the Toeplitz and lower triangular structure. Thus, taking into account that \(H_{\theta,M}\) is invertible, each block

\(D_j=\gamma d\lambda_jI_M+Q_{\theta,M}=H_{\theta,M}^{-1}\left(\gamma d\lambda_jH_{\theta,M}+H_M\right)\)

is lower triangular Toeplitz. Now we can conclude that _D<sub>j</sub>_ is nonsingular because \(\gamma d\lambda_jH_{\theta,M}+H_M\) is lower bidiagonal and its invertibility is decided by the diagonal elements, which are of the form \(1-\gamma d\lambda_j\theta\) which can not vanish since the eigenvalues \(\lambda_j\) have all nonzero imaginary part. With the latter the proof is concluded.

**Remark 8.3** _The block diagonalization in Theorem 8.5 shows that applying P_<sup>-1</sup> _to a given vector v can be performed through the following three steps._

1. _Step 1: compute_ \(\dot{v}=(F_N^*\otimes I_M)v\).<tbc>

