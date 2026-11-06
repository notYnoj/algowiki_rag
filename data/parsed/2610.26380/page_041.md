<tbc>By the conditional multivariate normal formula (Rao 1973, Eq. (8a.2.11)),

\(\mathbb{E}[\theta|\mathbf{Z}]=\mu_{t-1}+Cov(\theta,\mathbf{Z})C^{-1}(\mathbf{Z}-\mathbf{m}).\)

Since **_X_** is determined by **_Z_**, the tower property gives

\(\mathbb{E}[\theta|\mathbf{X}=\mathbf{x},n,p_{t-1}]=\mu_{t-1}+Cov(\theta,\mathbf{Z})C^{-1}\left(\mathbb{E}[\mathbf{Z}|\mathbf{X}=\mathbf{x},n,p_{t-1}]-\mathbf{m}\right).\)

We will show \(C^{-1}\left(\mathbb{E}[\mathbf{Z}|\mathbf{X}=\mathbf{x},n,p_{t-1}]-\mathbf{m}\right)=\lambda_\mathbf{x}\). Define \(A_\mathbf{x}:=\{z\in\mathbb{R}^U:x_uz_u\ge 0,u=1,\dots,U\}\). Since \(\{\mathbf{X}=\mathbf{x}\}=\{\mathbf{Z}\in A_\mathbf{x}\}\) almost surely, we have

\(p_\mathbf{x}(\mathbf{m})=\int_{A_\mathbf{x}}\phi_C(z-\mathbf{m})dz,\)

where \(\phi_C\) is the _N_(**0**_,C_) density. Differentiating gives

\(\nabla_\mathbf{m}\phi_C(z-\mathbf{m})=C^{-1}(z-\mathbf{m})\phi_C(z-\mathbf{m})\)

which is locally dominated by some integrable function of **_z_**. Therefore, by the dominated convergence theorem,

\(\nabla_\mathbf{m}p_\mathbf{x}(\mathbf{m})=\int_{A_\mathbf{x}}C^{-1}(z-\mathbf{m})\phi_C(z-\mathbf{m})dz\)<br>
\(=C^{-1}\left[\int_{A_\mathbf{x}}z\phi_C(z-\mathbf{m})dz-\mathbf{m}\int_{A_\mathbf{x}}\phi_C(z-\mathbf{m})dz\right]\)<br>
\(=C^{-1}\left[p_\mathbf{x}(\mathbf{m})\mathbb{E}[\mathbf{Z}|\mathbf{X}=\mathbf{x},n,p_{t-1}]-p_\mathbf{x}(\mathbf{m})\mathbf{m}\right]\)<br>
\(=p_\mathbf{x}(\mathbf{m})C^{-1}\left(\mathbb{E}[\mathbf{Z}|\mathbf{X}=\mathbf{x},n,p_{t-1}]-\mathbf{m}\right).\)

Therefore,

\(C^{-1}\left(\mathbb{E}[\mathbf{Z}|\mathbf{X}=\mathbf{x},n,p_{t-1}]-\mathbf{m}\right)=\nabla_\mathbf{m}logp_\mathbf{x}(\mathbf{m})=\lambda_\mathbf{x}.\)

Substituting this into the expression above gives \(\mu_t(\mathbf{x}|n,p_{t-1})=\mu_{t-1}+Cov(\theta,\mathbf{Z})\lambda_\mathbf{x}\), and

\(Cov(\theta,\mathbf{Z})\lambda_\mathbf{x}=\sum_{u=1}^U\beta_{j_u}(\lambda_\mathbf{x})_u\Sigma_{t-1}(e_{i_u}-e_{j_u}).\)

Hence

\(\mu_t(\mathbf{x}|n,p_{t-1})=\mu_{t-1}+\sum_{u=1}^U\beta_{j_u}(\lambda_\mathbf{x})_u\Sigma_{t-1}(e_{i_u}-e_{j_u}).\)

This also proves Lemma 3 which is the special case _U=_1. □

## Appendix B: Supplements to §2

### B.1. Derivations of calibration formulas

_Calibrating the pairwise accuracy factor_ \(\beta_1\). We calibrate \(\beta_1\) from the probability that a comparison of two randomly chosen items agrees with their true ordering. Let

_P<sub>P</sub>_:=P(a comparison of two randomly chosen items agrees with the true ordering).

