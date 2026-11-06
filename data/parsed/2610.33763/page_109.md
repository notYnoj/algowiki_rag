Define the unitary transformation<tbc>

\(Q:=\left[\begin{array}{ c c }
F_m\otimes F_\mathbf{n} & \text{O}_{\mathbf{n}m\times\mathbf{n}} \\
\text{O}_{\mathbf{n}\times\mathbf{n}m} & F_\mathbf{n}
\end{array}\right],\)

<tbc>Then

\(Q^*S_\widetilde{\mathbf{N}}Q:=\left[\begin{array}{ c c }
\Lambda_m^{(1)}\otimes I_\mathbf{n}+I_m\otimes\hat{a}\Lambda_\mathbf{n}^{(2)} & \text{O}_{\mathbf{n}m\times\mathbf{n}} \\
\mathbf{e}_m^TF_m^*\otimes I_\mathbf{n} & \frac{\lambda}{\alpha_m}\hat{a}\Lambda_\mathbf{n}^{(2)}
\end{array}\right].\) (7.24)

The preconditioner \(S_\widetilde{\mathbf{N}}\) is cheaper than \(P_\widetilde{\mathbf{N}}\), but it cannot ensure the clustering at 1 due to GLT arguments since

\(\{S_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_{\mathrm{GLT},\sigma}\frac{h_\xi(\theta_1)+a(x,y)\left(\nu_1g_{\eta_1}(\theta_2)+\nu_2g_{\eta_2}(\theta_3)\right)}{h_\xi(\theta_1)+\hat{a}\left(\nu_1g_{\eta_1}(\theta_2)+\nu_2g_{\eta_2}(\theta_3)\right)}\)

and hence it is less effective that \(P_\widetilde{\mathbf{N}}\) in terms of iteration count, also because the asymptotic behavior of the eigenvalues is not favourable.

