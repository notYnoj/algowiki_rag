<tbc>with the _H_-inner product and associated norm. When translating back to our original matrix _H+S_, we have \(\sigma=1\), and _H_-norms for the residual w.r.t. _iI+H_<sup>-1</sup>_B_ turn into _H_<sup>-1</sup>-norms for the residuals w.r.t. _H+S_. This gives us the following theorem.

Theorem 4.2. _Let_ \(\mathrm{spec}(H^{-1}S)\subseteq i[\alpha,\beta]\) _with_ \(\alpha<\beta\) _and let R be the unique solution of_

(4.1) \(\frac{1}{2}\left(R+\frac{1}{R}\right)=\frac{\sqrt{\beta^2+1}+\sqrt{\alpha^2+1}}{\beta-\alpha},R>1.\)

_Then the residuals of the_ \(\ell\)_MR iterates x<sub>m</sub> from_ (2.2) _satisfy_

\(\|b-Ax_m\|_{H^{-1}}\le\|b-Ax_0\|_{H^{-1}}\cdot\frac{2}{R^k+R^{-k}}.\)

Compared to Theorem 4.1 this theorem allows for a more narrow interval to contain the spectrum of _H_<sup>-1</sup>_S_ as it does not need to be symmetric with respect to the real axis. Note, however, that for real matrices spec(_H_<sup>-1</sup>_S_) is always symmetric with respect to the real axis, so that optimal bounds on the spectrum are of the form \(i[-\lambda,\lambda]\) as in Theorem 4.1. But even with symmetric bounds for the spectrum, the bound of Theorem 4.2 is always better than that of Theorem 4.1 as we will explain now. In order to not unnecessarily burden our discussion, we will omit details of somewhat longish but elementary algebraic manipulations in the paragraph to follow.

We first note that the expression \((\sqrt{\beta^2+1}+\sqrt{\alpha^2+1})/(\beta-\alpha)\) increases mono tonically in \(\beta\) and decreases monotonically in \(\alpha\). Thus, for \(\lambda\ge\mathrm{max}\{\beta,-\alpha\}\), we have

\(\frac{\sqrt{\beta^2+1}+\sqrt{\alpha^2+1}}{\beta-\alpha}\le\frac{\sqrt{\lambda^2+1}}{\lambda}.\)

The solution _R\>_1 of the equation _R_+1_/R=c_ with \(c\ge 1\) increases monotonically with _c_. Consequently, when \(\lambda\ge\mathrm{max}\{\beta,-\alpha\}\), the solution _R_ of (4.1) is larger or equal than the solution \(\widehat{R}=\left(\sqrt{1+\lambda^2}+1\right)/\lambda\) of \(R+1/R=\sqrt{\lambda^2+1}/\lambda\). Now, the factor \(\left(\lambda/(\sqrt{1+\lambda^2}+1)\right)^m\) in the bound of Theorem 4.1(ii) is precisely \(1/\widehat{R}^m\). The quantity 1/(_R<sup>m</sup>+R_<sup>-_m_</sup>) in the bound of Theorem 4.2 is thus smaller for two reasons: Because of the presence of _R_<sup>-_m_</sup>_\>_0 and because \(\widehat{R}>R\) as soon as \(\beta\neq-\alpha\), i.e., \(\lambda>\beta\) or \(\lambda>-\alpha\).

We now turn to the flexible methods. Conceivably, a detailed convergence analysis, depending on the "degree of inexactness" of the preconditioner could be based on prior work for flexible CG [16], flexible GMRES [19, 26] and, in particular, flexible QMR [24]. We anticipate this to be quite involved and also quite technical, so that we do not address this in the context of the present paper. We rather state and prove two basic properties which are essential for the algorithmic aspects.

The first property is that in typical situations we cannot encounter unlucky breakdowns in the flexible Lanczos process, Algorithm 3.2. An unlucky breakdown at step _m_ means that we get \(\beta_m=\langle w,\widehat{w}\rangle=0\) although \(w\neq 0\). If there is no unlucky breakdown, the FMR iterates all exist up to the step where we obtain the solution, as in that case the matrix _T_<sub>_m_+1_,m_</sub> of (3.5) has full rank for all relevant _m_. Though, its square part _T<sub>m,m</sub>_ need not be non-singular, which means that the FGAL iterate does not necessarily exist. However, as is done in the SYMMLQ-algorithm (see [12, 17]), the _QR_-factorization of _T<sub>m,m</sub>_ can still be updated from that of _T_<sub>_m_-1_,m_-1</sub>, which allows to efficiently update the next FGAL iterate from the previous existing one using the _QR_-factorization.

