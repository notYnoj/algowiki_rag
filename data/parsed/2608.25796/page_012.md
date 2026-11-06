or \(P_{\omega,\alpha,\beta,MN}=C_{\omega,\alpha,\beta,MN}\) corresponding \(\omega-\)circulant matrix of \(C_{\alpha,\beta,NM}\).<br>
The principal part of the related computational cost is given by direct applications of preconditioned GMRES, where the preconditioner solution cost via FFT is given by \(\sharp\tilde{it}O(MNlogNM)\) and \(\sharp\tilde{it}\) is the number of required iterations.

In all the cases it is worth noticing that the cardinality of iterations is the critical parameter. When the quantity \(\sharp it\) is constant with respect to _N_ and the quantity \(\sharp\tilde{it}\) is constant with respect to _N_ and _M_ then we end up fast methods, with optimal cost of _O(MN_log_NM_) arithmetic operations for the second proposal.

Now these quantities \(\sharp it\) and \(\sharp\tilde{it}\) depend on a favourable spectral distribution of the corresponding matrix sequences. In the subsequent part of the section, we study the singular value and eigenvalue distributions of the indicated preconditioned matrix sequences.

## 5.1. GLT analysis of the preconditioning proposals

We study the quality of the approximation resulting from the replacement of the Toeplitz structures by the considered circulant and \(\omega-\)circulant counterparts.

### 5.1.1. GLT analysis of the preconditioning for Technique 1

We first remind that \(\overline{G_{\alpha,N}}=T_N(f_\alpha)\) with \(f_\alpha\) belonging to the Wiener class; see e.g. \[14\]. Now by classical results on Toeplitz preconditioning \[11, 39\], we know that the natural circulant and the natural \(\omega\)-circulant approximations _P<sub>N</sub>_ ensure a strong singular value clustering at zero for \(\{\overline{G_{\alpha,N}}-P_N\}_N\) in the sense of Definition 2.3. Hence, taking into account Remark 2.4, \(\{\overline{G_{\alpha,N}}-P_N\}_N\sim_\sigma 0\) and the latter is equivalent to

\(\{\overline{G_{\alpha,N}}-P_N\}_N\sim_\mathrm{GLT}0,\) (13)

by Axiom **GLT1**.

Relation (13) is the basis for proving the following result.

**Theorem 5.1.** _Let_ \(\alpha\in(1,2)\) _and let_ \(P_N\in\left\{\widehat{C}_{\alpha,N},\widehat{C}_{\omega,\alpha,N}\right\}\)_. Then_

• \(\{P_N\}_N\sim_{\mathrm{GLT},\sigma} f_\alpha(\theta)\);<tbc>

• \(\{P_N^{-1}A_N\}_N\sim_{\mathrm{GLT},\sigma} 1\) _when a is a constant;_<tbc>

• \(\{P_N^{-1}A_N\}_N\sim_{\mathrm{GLT},\sigma}\frac{\ell_0-\gamma a(x)f_\alpha(\theta)}{\ell_0-\gamma df_\alpha(\theta)}\)<tbc>

_for a general Riemann integrable coefficient a(x)._

_Proof._ By Axiom **GLT2**, part 1, we have \(\{\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}f_\alpha(\theta)\) since \(\overline{G_{\alpha,N}}=T_N(f_\alpha)\). Then \(\{D_N(a)\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}a(x)f_\alpha(\theta)\) because of Axiom **GLT2**, part 2, and **GLT3**, part 3. As a consequence, since {_A<sub>N</sub>}<sub>N</sub>_ is linear combination of the GLT sequences {_I<sub>N</sub>}<sub>N</sub>_ and {_D<sub>N</sub>(a_)\(\overline{G_{\alpha,N}}\}_N\) with coefficients \(\ell_0\) and \(\gamma\), we deduce that

\(\{A_N=\ell_0I_N-\gamma\mathcal{D}_N(a)\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}\ell_0-\gamma a(x)f_\alpha(\theta).\) (14)

Now relation (13), \(\{\overline{G_{\alpha,N}}\}_N\sim_\mathrm{GLT}f_\alpha(\theta)\), and Axiom **GLT3**, part 2, imply \(\{P_N\}_N\sim_\mathrm{GLT}f_\alpha(\theta)\). Since \(f_\alpha\) has a unique zero at \(\theta=0\), it is obvious that it is invertible a.e. and hence Axiom **GLT3**, part 4, leads to the conclusion

\(\{P_N^{-1}\}_N\sim_\mathrm{GLT}\frac{1}{f_\alpha(\theta)}\)

