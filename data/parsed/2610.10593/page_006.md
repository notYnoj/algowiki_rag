At the canonical root, use _D_={_s:s<sub>X</sub>+s<sub>Y</sub>+s<sub>Z</sub>_=16} in (5). If \(\overline{\beta^w}=\sum_s\alpha^*(s)\beta_s^w\), the analogous root totals are

\(R_{0,X}=H(\alpha_X^*)-\widehat{P}_D(\alpha^*;f^*),R_{0,Y}=H(\overline{\beta^Y})-\eta_Y(\alpha^*,\beta;\{s:s_Z=0\}),R_{0,Z}=H(\overline{\beta^Z})-\eta_Z(\alpha^*,\beta;\{s:s_X=0\text{or}s_Y=0\}).\text{(10)}\)

## 2.3 Six-copy symmetrization and the exponent objective

The complete construction consists of six globally coordinate-permuted copies of the canonical parameter tree, each assigned weight 1/6. This symmetrization is performed in addition to the six local extraction regions. We write \(\widehat{E}\) for the conservative retained exponent obtained after inserting the entropy upper bounds (4); it need not equal the exponent obtained with exact maximum-entropy penalties. The six-copy symmetry yields the following exact reduction of the stage formula for this \(\widehat{E}\):

\(\widehat{E}=min_kR_{0,k}+min_kR_{4,k}+min_kR_{3,k}+E_2.\) (11)

To see why the minima have this form, let _K<sub>r,w</sub>_ be the canonical contribution in physical coordinate _w_ from local region _r_, including all occurrence masses and region weights. For a fixed physical orientation _h_ and a local permutation _p<sub>r</sub>_, precisely one global copy contributes, namely \(g=h\circ p_r^{-1}\). Its contribution in physical coordinate _h(k_) is _K<sub>r,p<sub>r</sub>(k_)</sub>/6. Thus the three totals at orientation _h_ are \(R_{\ell,k}/6\), and summing the minimum over the six physical orientations gives \(min_kR_{\ell,k}\). This argument uses the particular six-copy symmetry; it does not interchange a minimum and a sum for arbitrary inputs.

The same symmetry makes the three terminal dimension exponents equal. The contribution of a positive level-2 occurrence with parameter \(\mu_v\) is

\(E_{2,v}=\frac{m_v}{3}\big(2+H(\mu_v,1-2\mu_v,\mu_v)\big),M_v=\frac{m_v}{3}(2-2\mu_v)log_2q.\) (12)

A zero-coordinate occurrence contributes no term to _E_<sub>2</sub> and contributes

\(M_v=\frac{m_v}{3}\left(H(\beta_v^w)+\sum_L\beta_v^w(L)\#_1(L)log_2q\right)\) (13)

to _M_, where _w_ is any nonzero coordinate and #<sub>1</sub>(_L_) counts the entries equal to 1. Complementation shows that either nonzero coordinate gives the same expression. If two coordinates vanish, all distributions are point masses and the matrix-size contribution is zero. Summing these terms gives _E_<sub>2</sub> and the common matrix-size exponent _M\>_0.

The degeneration theorem and asymptotic sum inequality imply

\(\omega\le\widehat{\Omega}(x):=\frac{C-\widehat{E}(x)}{M(x)}.\) (14)

Equivalently, to prove \(\omega<\tau\), it suffices to exhibit admissible parameters for which

\(\widehat{E}(x)+\tau M(x)-C>0.\) (15)

All three minima in (11) are retained in the certified evaluation.

