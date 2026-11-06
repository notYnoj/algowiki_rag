<tbc>The matrix _D_<sup>-1</sup>_CD_<sup>-1</sup> is the correlation matrix of **_Z_**, and \(\widetilde{C}_\mathbf{x}\) is the corresponding sign-flipped correlation matrix. This is exactly the construction of Mullahy (2017, Appendix B). In Mullahy’s notation, for a binary outcome he defines signs _s<sub>jp</sub>_=2_k<sub>jp</sub>_-1, forms the diagonal sign matrix _T<sub>p</sub>_=diag(_s<sub>jp</sub>_), and replaces the original correlation matrix _R_ by _Q<sub>p</sub>=T<sub>p</sub>RT<sub>p</sub>_. Here, _D_**<sub>x</sub>** plays the role of _T<sub>p</sub>_, and \(\widetilde{C}_\mathbf{x}\) plays the role of _Q<sub>p</sub>_. Now define<tbc>

\(\alpha(\mathbf{x})=\left(\alpha_1(\mathbf{x}),\dots,\alpha_U(\mathbf{x})\right)^\top\)<br>
\(\text{where}\alpha_u(\mathbf{x})=\frac{x_um_u}{\sqrt{C_{uu}}}=\frac{x_u\beta_{j_u}\left(\mu_{t-1,i_u}-\mu_{t-1,j_u}\right)}{\sqrt{C_{uu}}},u=1,\dots,U.\)

<tbc>Let **_W_**=-_D_**<sub>x</sub>**_D_<sup>-1</sup>(**_Z_**-**_m_**) so \(\mathbf{W}\sim N(\mathbf{0},\widetilde{C}_\mathbf{x})\). For each coordinate _u_,<tbc>

\(W_u\le\alpha_u(\mathbf{x})\Longleftrightarrow-\frac{x_u(Z_u-m_u)}{\sqrt{C_{uu}}}\le\frac{x_um_u}{\sqrt{C_{uu}}}\Longleftrightarrow x_uZ_u\ge 0.\)

<tbc>Therefore \(\{\mathbf{X}=\mathbf{x}\}=\{\mathbf{W}\le\alpha(\mathbf{x})\}\) almost surely. Hence

\(\mathbb{P}(\mathbf{X}=\mathbf{x}|n,p_{t-1})=\mathbb{P}\left(\mathbf{W}\le\alpha(\mathbf{x})\right)=\Phi_U\left(\alpha(\mathbf{x});\widetilde{C}_\mathbf{x}\right).\)

This proves the outcome-probability formula.

We next derive the formula for \(\lambda_\mathbf{x}\). Viewing the outcome probability above as a function of the latent mean vector **_m_**, write \(p_\mathbf{x}(\mathbf{m}):=\Phi_U\left(\alpha(\mathbf{x});\widetilde{C}_\mathbf{x}\right)\). Since _C_, and hence _D_ and \(\widetilde{C}_\mathbf{x}\), does not depend on **_m_**, the dependence on _m<sub>u</sub>_ is only through \(\alpha_u(\mathbf{x})=x_um_u/\sqrt{C_{uu}}\). Thus,<tbc>

\(\frac{\partial p_\mathbf{x}(\mathbf{m})}{\partial m_u}=\frac{\partial}{\partial\alpha_u}\Phi_U\left(\alpha(\mathbf{x});\widetilde{C}_\mathbf{x}\right)\frac{x_u}{\sqrt{C_{uu}}}.\)

<tbc>We next compute this derivative. For \(\mathbf{W}\sim N(\mathbf{0},\widetilde{C}_\mathbf{x})\),<tbc>

\(\frac{\partial}{\partial\alpha_u}\Phi_U(\alpha;\widetilde{C}_\mathbf{x})=\phi(\alpha_u)\mathbb{P}(\mathbf{W}_{-u}\le\alpha_{-u}|W_u=\alpha_u)=\phi(\alpha_u)\Phi_{U-1}\left(\alpha_{-u}-(\widetilde{C}_\mathbf{x})_{-u,u}\alpha_u;(\widetilde{C}_\mathbf{x})_{-u|u}\right),\)

<tbc>where the second equality follows from the conditional multivariate normal formula (Rao 1973, Eq. (8a.2.11), Mullahy 2017, Appendix B). Substituting this into the derivative of _p_**<sub>x</sub>**(**_m_**) gives<tbc>

\(\frac{\partial p_\mathbf{x}(\mathbf{m})}{\partial m_u}=\frac{x_u}{\sqrt{C_{uu}}}\phi(\alpha_u(\mathbf{x}))\Phi_{U-1}\left(\alpha_{-u}(\mathbf{x})-(\widetilde{C}_\mathbf{x})_{-u,u}\alpha_u(\mathbf{x});(\widetilde{C}_\mathbf{x})_{-u|u}\right).\)

<tbc>Therefore,

\(\frac{\partial}{\partial m_u}logp_\mathbf{x}(\mathbf{m})=\frac{1}{p_\mathbf{x}(\mathbf{m})}\frac{\partial p_\mathbf{x}(\mathbf{m})}{\partial m_u}\)<br>
\(=\frac{x_u}{\sqrt{C_{uu}}}\frac{\phi(\alpha_u(\mathbf{x}))\Phi_{U-1}\left(\alpha_{-u}(\mathbf{x})-(\widetilde{C}_\mathbf{x})_{-u,u}\alpha_u(\mathbf{x});(\widetilde{C}_\mathbf{x})_{-u|u}\right)}{\Phi_U\left(\alpha(\mathbf{x});\widetilde{C}_\mathbf{x}\right)}=(\lambda_\mathbf{x})_u.\)

Hence \(\lambda_\mathbf{x}=\nabla_\mathbf{m}logp_\mathbf{x}(\mathbf{m})\).

It remains to connect \(\lambda_\mathbf{x}\) to the posterior mean of \(\theta\). The pair \((\theta,\mathbf{Z})\) is jointly Gaussian. For each _u_=1_,...,U_,<tbc>

\(Cov(\theta,Z_u)=\beta_{j_u}\Sigma_{t-1}(e_{i_u}-e_{j_u}).\)

