<tbc>In Eq. (64), the transposed term comes from the differential of the outer product Eq. (55), where \(\tau_{1,2}(A)_{i,j,\cdots}=A_{j,i,\cdots}\). For the differential with respect to \(\unknown\), we use the same method as in Eq. (64):

\(\frac{\partial F_\unknown}{\partial\unknown}(\theta,X)\in\mathcal{L}\left((S_d(\mathbb{R}))^K,(S_d(\mathbb{R}))^K\right)\unknown\rightarrow\mathbb{R}^{K\times d\times d\times K\times d\times d}:\) (65)

\(\left[\frac{\partial F_\unknown}{\partial\unknown}(\theta,X)\right]_{k,\cdot,\cdot,l,\cdot,\cdot}=\frac{1}{\Gamma_k}\sum_{i=1}^n(x_i-F_{m_k})(x_i-F_{m_k})^\top\otimes\left[\frac{\partial\gamma}{\partial\unknown}\right]_{i,k,l,\cdot,\cdot}\)<br>
\(-\frac{1}{\Gamma_k^2}\left(\sum_{i=1}^n\gamma_{i,k}(x_i-F_{m_k})(x_i-F_{m_k})^\top\right)\otimes\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial\unknown}\right]_{j,k,l,\cdot,\cdot}\)<br>
\(-\frac{1}{\Gamma_k}\sum_{i=1}^n\gamma_{i,k}\left\{\tau_{1,2}\left((x_i-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial\unknown}\right]_{k,\cdot,l,\cdot,\cdot}\right)+(x_i-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial\unknown}\right]_{k,\cdot,l,\cdot,\cdot}\right\}.\) (66)

Finally, for the differential with respect to _X_, the method is almost identical, with an additional term due to the presence of _x<sub>i</sub>_ in \((x_i-F_{m_k})(x_i-F_{m_k})^\top\).

\(\frac{\partial F_\unknown}{\partial X}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{n\times d},(S_d(\mathbb{R}))^K\right)\unknown\rightarrow\mathbb{R}^{K\times d\times d\times n\times d}:\) (67)

\(\left[\frac{\partial F_\unknown}{\partial X}(\theta,X)\right]_{k,\cdot,\cdot,i,\cdot}=\frac{1}{\Gamma_k}\sum_{h=1}^n(x_h-F_{m_k})(x_h-F_{m_k})^\top\otimes\left[\frac{\partial\gamma}{\partial X}\right]_{h,k,i,\cdot}\)<br>
\(-\frac{1}{\Gamma_k^2}\left(\sum_{h=1}^n\gamma_{h,k}(x_h-F_{m_k})(x_h-F_{m_k})^\top\right)\otimes\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial X}\right]_{j,k,i,\cdot}\)<br>
\(-\frac{1}{\Gamma_k}\sum_{h=1}^n\gamma_{h,k}\left\{\tau_{1,2}\left((x_h-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial X}\right]_{k,\cdot,i,\cdot}\right)+(x_h-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial X}\right]_{k,\cdot,i,\cdot}\right\}\)<br>
\(+\frac{\gamma_{i,k}}{\Gamma_k}\left\{\tau_{1,2}\big((x_i-F_{m_k})\otimes I_d\right)+(x_i-F_{m_k})\otimes I_d\right\}.\) (68)

## A.7 Local Minima in (GMM)-OT

### A.7.1 Computation of the Local Minima of the Discrete 2-Wasserstein Distance

We provide an explicit local minimum of the energy E<sub>3</sub> defined in Eq. (19). We illustrate the setup in Fig. 16.

To compute the energy \(\mathcal{E}_3(\alpha,\eta)\) at \([-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\), we must distinguish the two cases \(\alpha_1+\alpha_2\ge 0\) and \(\alpha_1+\alpha_2<0\), which yield two different OT plans between \(\mu_{\alpha,\eta}\) and \(\nu\). We will show separately that the energy E<sub>3</sub> has a strict local minimum at (0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>) in both sub-regions. To break the symmetry in \((\alpha_1,\alpha_2,\eta_1,\eta_2)\leftarrow(\alpha_2,\alpha_1,\eta_2,\eta_1)\), we will impose the constraint \(\eta_1\le\eta_2\) in the optimisation problem. To summarise, we split the optimisation problem in two as follows:

\(min_{\alpha\in[-\frac{1}{6},\frac{1}{6}]^2\eta\in(-\frac{1}{2},\frac{1}{2})^3}\mathcal{E}_3(\alpha,\eta)=min(\mathcal{E}_3^+,\mathcal{E}_3^-),\mathcal{E}_3^+:=min_{\alpha\in[-\frac{1}{6},\frac{1}{6}]^2\eta\in(-\frac{1}{2},\frac{1}{2})^3\alpha_1+\alpha_2\ge 0\eta_1\le\eta_2}\mathcal{E}_3(\alpha,\eta),\mathcal{E}_3^-:=min_{\alpha\in[-\frac{1}{6},\frac{1}{6}]^2\eta\in(-\frac{1}{2},\frac{1}{2})^3\alpha_1+\alpha_2\le 0\eta_1\le\eta_2}\mathcal{E}_3(\alpha,\eta).\) (69)

### Case

For any \((\alpha,\eta)\in[-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\) such that \(\alpha_1+\alpha_2\ge 0\) and \(\eta_1\le\eta_2\), the optimal plan between \(\mu_{\alpha,\eta}\) and \(\nu\) is given by:<tbc>

\(\pi^+(\alpha,\eta)=\left(\begin{array}{ c c c }
\frac{1}{6}+\alpha_1 & 0 & 0 \\
\frac{1}{6}-\alpha_1 & \alpha_1+\alpha_2 & 0 \\
0 & \frac{1}{3}-\alpha_1-\alpha_2 & \frac{1}{3}
\end{array}\right),\)

