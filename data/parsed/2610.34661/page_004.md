<tbc>by

\(\rho(\xi):=-\beta\sum_{i=1}^nZ_i\bar{c}_ie^{-Z_i\xi},\xi\in\mathbb{R}.\) (2)

The positive constants \(\alpha\) and \(\beta\) collect the physical constants; for _T_=298.15 K one has \(\alpha\approx 7042.94\) and \(\beta\approx 4.2413\) \[34\]. We assume throughout that the bulk solution is electrically neutral,<tbc>

\(\sum_{i=1}^nZ_i\bar{c}_i=0,\bar{c}:=\sum_{i=1}^n\bar{c}_i>0,\) (3)

<tbc>which is the standard physical assumption (the second condition merely excludes the trivial case of pure water) and implies \(\rho(0)=0\). Since

\(\rho'(\xi)=\beta\sum_{i=1}^nZ_i^2\bar{c}_ie^{-Z_i\xi}>0,\) (4)

the function \(\rho\) is strictly increasing. For a symmetric 1:1 electrolyte (_n_=2, _Z_<sub>1</sub>=-_Z_<sub>2</sub>=1, \(\bar{c}_1=\bar{c}_2=I_s\)) we have \(\rho(\xi)=\kappa^2\mathrm{sinh}\xi\) with \(\kappa^2=2\beta I_s\), and the equation in _D<sub>s</sub>_ becomes \(-\epsilon_s\Delta u+\kappa^2\mathrm{sinh}u=0\).

## 2.2 Solution decomposition

To remove the singularities caused by the Dirac distributions, Xie \[34\] decomposes the solution of (1) as<tbc>

\(u=G+\Psi+\widehat{\Phi}\text{in}\Omega,\) (5)

<tbc>where _G_ is the Coulomb potential of the solute charges,<tbc>

\(G(\mathbf{r})=\frac{\alpha}{4\pi\epsilon_p}\sum_{j=1}^{n_p}\frac{z_j}{|\mathbf{r}-\mathbf{r}_j|},\) (6)

<tbc>\(\Psi\) is the solution of the linear interface problem<tbc>

\(\left\{\begin{array}{ c c }
\Delta\Psi=0 & \text{in}D_p\cup D_s, \\
\Psi(\mathbf{s}^+)=\Psi(\mathbf{s}^-), & \epsilon_s\frac{\partial\Psi(\mathbf{s}^+)}{\partial\mathbf{n}}=\epsilon_p\frac{\partial\Psi(\mathbf{s}^-)}{\partial\mathbf{n}}+(\epsilon_p-\epsilon_s)\frac{\partial G(\mathbf{s})}{\partial\mathbf{n}} & \text{on}\Gamma, \\
\Psi=\hat{g}-G & \text{on}\partial\Omega,
\end{array}\right.\) (7)

<tbc>and \(\widehat{\Phi}\) is the solution of the semilinear interface problem<tbc>

\(\left\{\begin{array}{ c c }
\Delta\widehat{\Phi}=0 & \text{in}D_p, \\
-\epsilon_s\Delta\widehat{\Phi}+\rho(U+\widehat{\Phi})=0 & \text{in}D_s, \\
\widehat{\Phi}(\mathbf{s}^+)=\widehat{\Phi}(\mathbf{s}^-), & \epsilon_s\frac{\partial\widehat{\Phi}(\mathbf{s}^+)}{\partial\mathbf{n}}=\epsilon_p\frac{\partial\widehat{\Phi}(\mathbf{s}^-)}{\partial\mathbf{n}} & \text{on}\Gamma, \\
\widehat{\Phi}=0 & \text{on}\partial\Omega,
\end{array}\right.\) (8)

<tbc>with

\(U:=G+\Psi.\) (9)

Since \(-\Delta\big(\frac{1}{4\pi|\mathbf{r}-\mathbf{r}_j|}\big)=\delta_{\mathbf{r}_j}\), one checks directly that _u_ defined by (5) satisfies (1); see \[34\]. The functions _G_, \(\Psi\) and \(\widehat{\Phi}\) are the contributions of the solute charges, of the boundary and interface<tbc>

