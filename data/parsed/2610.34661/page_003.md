The main results are as follows. Under piecewise _H<sup>s</sup>_ regularity of \(\Psi\) and \(\widehat{\Phi}\) and \(H^\sigma\) regularity of a linear dual problem, \(1<s,\sigma\le 2\), we prove that the finite element approximation \(\Phi_h\) of \(\widehat{\Phi}\) computed with the perturbed datum _U<sub>h</sub>_ satisfies energy-norm, _L_<sup>2</sup> and _L_<sup>4</sup> error estimates, in which the perturbation enters only through \(\|\Psi-\Psi_h\|_{L^2(D_s)}\) (Theorems 4.6 and 4.8, Corollary 4.9). For the two-grid solution \(u_h^\mathrm{tg}=G+\Psi_h+\Phi_h^\mathrm{tg}\) we prove

\(|||u-u_h^\mathrm{tg}|||\le C\big(h^{s-1}+H^{2(s-1)+t/2}\big),t=\mathrm{min}\{s,\sigma\}-1,\)

in three dimensions (Theorem 5.2), so that the choice \(H\sim h^{(s-1)/(2(s-1)+t/2)}\) keeps the accuracy of the nonlinear fine-mesh solution. If \(\sigma\ge s\), in particular if \(s=\sigma\), this is _H∼h_<sup>2/5</sup>. The estimate holds whether the coarse nonlinear problem uses the fine-mesh datum _U<sub>h</sub>_ or the coarse-mesh datum \(U_H=G+\Psi_H\); with the second choice the whole nonlinear computation stays on the coarse mesh. On the fine mesh the scheme needs only two linear solves with symmetric positive definite matrices, one for \(\Psi_h\) and one for the Newton correction, and both can be done by conjugate gradients with multilevel preconditioners that are robust with respect to the dielectric jump \[40\]. For a symmetric 1:1 electrolyte the truncated nonlinearity is \(\kappa^2\mathrm{sinh}_\tau\), a _C_<sup>2</sup> version of the modified hyperbolic sine of \[34\].

The remainder of the paper is organized as follows. Section 2 recalls the dimensionless PBE model, the solution decomposition of \[34\], and the weak formulations. Section 3 introduces the truncated nonlinearity and proves the a priori bounds and the equivalence of the truncated and the original problems. Section 4 contains the finite element discretization and the error estimates for \(\Phi_h\), including the effect of the perturbed datum. Section 5 presents the two-grid algorithm, its error analysis and the choice of the coarse mesh size. Section 6 reports a three-dimensional test with a manufactured solution, and Section 7 contains concluding remarks.

## 2 The Poisson-Boltzmann model and its solution decomposition

### 2.1 The dimensionless PBE model

Let \(\Omega\subset\mathbb{R}^3\) be a bounded Lipschitz domain that is partitioned as \(\overline{\Omega}=\overline{D_p}\cup\overline{D_s}\), where _D<sub>p</sub>_ is the solute region hosting a biomolecule with _n<sub>p</sub>_ atoms, \(D_s=\Omega\backslash\overline{D_p}\) is the solvent region, and \(\Gamma=\partial D_p\) is the interface between them. We assume that \(\overline{D_p}\subset\Omega\), so that \(\Gamma\cap\partial\Omega=\emptyset\), and that both _D<sub>p</sub>_ and _D<sub>s</sub>_ are Lipschitz domains. The _j_th atom has position \(\mathbf{r}_j\in D_p\) and charge number _z<sub>j</sub>_, and the solvent contains _n_ ionic species with charge numbers \(Z_i\neq 0\) and bulk concentrations \(\bar{c}_i\ge 0\) (in mol/L), _i_=1_,...,n_. The two regions are treated as homogeneous dielectric media with relative permittivities \(\epsilon_p\) and \(\epsilon_s\); throughout we only use \(0<\epsilon_p\le\epsilon_s\), and we write \(\epsilon\) for the piecewise constant function with \(\epsilon|_{D_p}=\epsilon_p\) and \(\epsilon|_{D_s}=\epsilon_s\). Following \[34\], when the length is measured in Ångströms and the potential in units of _k<sub>B</sub>T/e<sub>c</sub>_, the PBE model takes the dimensionless form

\(\left\{\begin{array}{ c c }
-\epsilon_p\Delta u(\mathbf{r})=\alpha\sum_{j=1}^{n_p}z_j\delta_{\mathbf{r}_j}, & \mathbf{r}\in D_p, \\
-\epsilon_s\Delta u(\mathbf{r})+\rho(u(\mathbf{r}))=0, & \mathbf{r}\in D_s, \\
u(\mathbf{s}^+)=u(\mathbf{s}^-), & \epsilon_s\frac{\partial u(\mathbf{s}^+)}{\partial\mathbf{n}(\mathbf{s})}=\epsilon_p\frac{\partial u(\mathbf{s}^-)}{\partial\mathbf{n}(\mathbf{s})}, & \mathbf{s}\in\Gamma, \\
u(\mathbf{s})=\hat{g}(\mathbf{s}), & \mathbf{s}\in\partial\Omega,
\end{array}\right.\) (1)

where \(\delta_{\mathbf{r}_j}\) is the Dirac distribution at **r**_<sub>j</sub>_, **n** is the unit outward normal of _D<sub>p</sub>_, \(u(\mathbf{s}^\pm)=\mathrm{lim}_{t\rightarrow 0^+}u(\mathbf{s}\pm t\mathbf{n}(\mathbf{s}))\), \(\hat{g}\) is a given boundary function (commonly \(\hat{g}=0\)), and the ionic charge density is described<tbc>

