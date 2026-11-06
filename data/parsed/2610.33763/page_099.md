Using the product property of GLT 3 applied to the sequences {_D_**<sub>n</sub>**(_a_)}**<sub>n</sub>** and \(\{B_\mathbf{n}^x+B_\mathbf{n}^y\}_\mathbf{n}\), we conclude that<tbc>

\(\{G_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}a(x,y)\left(\nu_1g_{\eta_1}(\theta_1)+\nu_2g_{\eta_2}(\theta_2)\right),(x,y)\in[0,1]^2,(\theta_1,\theta_2)\in[-\pi,\pi]^2,\)

<tbc>By GLT 1, we immediately obtain<tbc>

\(\{G_\mathbf{n}\}_\mathbf{n}\sim_\sigma a(x,y)\left(\nu_1g_{\eta_1}(\theta_1)+\nu_2g_{\eta_2}(\theta_2)\right),(x,y)\in[0,1]^2,(\theta_1,\theta_2)\in[-\pi,\pi]^2,\)

<tbc>Finally, we observe that \(B_\mathbf{n}^x\) and \(B_\mathbf{n}^y\) are lower triangular matrices. Hence \((B_\mathbf{n}^x+B_\mathbf{n}^y)\) is lower triangular, and since _D_**<sub>n</sub>**(_a_) is diagonal,<tbc>

\(G_\mathbf{n}:=D_\mathbf{n}(a)\left(B_\mathbf{n}^x+B_\mathbf{n}^y\right),\)

<tbc>is also lower diagonal. Therefore, the eigenvalues of _G_**<sub>n</sub>** coincide with its diagonal entries. Since the main diagonal entries of \(B_\mathbf{n}^x\) and \(B_\mathbf{n}^y\) are \(\delta_0\) and \(\sigma_0\), the diagonal entries of _G_**<sub>n</sub>** are \(\{a(x_i,y_j)\left(\delta_0+\sigma_0\right)\}_{i,j=1}^{n_1,n_2}\). Hence

\(\{G_\mathbf{n}\}_\mathbf{n}\sim_\lambda a(x,y)\left(\delta_0+\sigma_0\right),(x,y)\in[0,1]^2.\)

We are now in a position to compute the GLT symbol of the sequence associated with the full coefficient matrix \(A_\widetilde{\mathbf{N}}\). To ensure meaningful results, we assume a mild relation among the rates at which the discretization parameters tend to zero.

**Theorem 7.3** _With_ \(A_\widetilde{\mathbf{N}}\) _defined in_ (7.18)_, assume that_<tbc>

\(\frac{\alpha_m}{\beta_{n_1}}\rightarrow\nu_1,\frac{\alpha_m}{\beta_{n_2}}\rightarrow\nu_2,\text{\textit{as}}m,n_1,n_2\rightarrow\infty,\)

<tbc>_with_ \(\nu_1\neq 0\) _or_ \(\nu_2\neq 0\)_. Then, it holds_

\(\{A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_{\mathrm{GLT},\sigma} h_\xi(\theta_1)+a(x,y)\left(\nu_1g_{\eta_1}(\theta_2)+\nu_2g_{\eta_2}(\theta_3)\right),\)<br>
\((\theta_1,\theta_2,\theta_3)\in[-\pi,\pi]^3,(x,y)\in[0,1]^2,\)

_where_ \(h_\xi\) _is given in Theorems 7.1 and_ \(g_{\eta_1}\) _and_ \(g_{\eta_2}\) _are given in Theorems 7.2._

**Proof:** We proceed by decomposing (7.18) as follows<tbc>

\(A_\widetilde{\mathbf{N}}=\underbrace{\left[\begin{array}{ c c }
U_m\otimes I_\mathbf{n} & \mathrm{O}_{m\mathbf{n}\times\mathbf{n}} \\
\mathrm{O}_{\mathbf{n}\times m\mathbf{n}} & \mathrm{O}_\mathbf{n}
\end{array}\right]}_{=:C_\widetilde{\mathbf{N}}^{(1)}}+\underbrace{\left[\begin{array}{ c c }
I_m\otimes G_\mathbf{n} & \mathrm{O}_{m\mathbf{n}\times\mathbf{n}} \\
\mathrm{O}_{\mathbf{n}\times m\mathbf{n}} & \frac{\lambda}{\alpha_m}G_\mathbf{n}
\end{array}\right]}_{=:C_\widetilde{\mathbf{N}}^{(2)}}+\underbrace{\left[\begin{array}{ c c }
\mathrm{O}_{m\mathbf{n}} & -\alpha_m\mathbf{q}\otimes I_\mathbf{n} \\
\mathbf{e}_m^T\otimes I_\mathbf{n} & \mathrm{O}_\mathbf{n}
\end{array}\right]}_{=:C_\widetilde{\mathbf{N}}^{(3)}}.\)

<tbc>Thus, we analyze each component separately. For the first component, we have<tbc>

\(C_\widetilde{\mathbf{N}}^{(1)}=U_{m+1}\otimes I_\mathbf{n}-\underbrace{\left[\begin{array}{ c c }
\mathrm{O}_{m\mathbf{n}} & \mathrm{O}_{m\mathbf{n}\times\mathbf{n}} \\
\gamma_me^{-\rho m\Delta t}I_\mathbf{n} & \cdots \\
\gamma_1e^{-\rho\Delta t}I_\mathbf{n} & \gamma_0I_m
\end{array}\right]}_{=:R_\widetilde{\mathbf{N}}^{(1)}},\)

