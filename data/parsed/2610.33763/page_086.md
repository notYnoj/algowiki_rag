We are now ready to compute the GLT symbol of the sequence associated with the full coefficient matrix. To provide meaningful results, we introduce a mild assumption regarding the rate at which the discretization parameters tend to zero with respect to one another.

**Theorem 6.3** _With A<sub>N</sub> defined in_ (6.11)_, assume that_<tbc>

\(\frac{\alpha_m}{\beta_n}\rightarrow\nu,\text{\textit{as}}m,n\rightarrow\infty,\)

<tbc>_with_ \(\nu\neq 0\)_. Then, it holds_

\(\{A_N\}_N\sim_{\mathrm{GLT},\sigma} h_\xi(\theta_1)+\nu a(x)g_\eta(\theta_2),(\theta_1,\theta_2)\in[-\pi,\pi]^2,x\in[0,1],\)

_where_ \(h_\xi\) _and_ \(g_\eta\) _are given in Theorems 6.1-6.2._

**Proof:** We begin by decomposing (6.11) as<tbc>

\(A_N=\underbrace{\left[\begin{array}{ c c }
U_m\otimes I_n & \mathrm{O}_{mn\times n} \\
\mathrm{O}_{n\times mn} & \mathrm{O}_n
\end{array}\right]}_{=:C_N^{(1)}}+\underbrace{\left[\begin{array}{ c c }
I_m\otimes\frac{\alpha_m}{\beta_n}G_n & \mathrm{O}_{mn\times n} \\
\mathrm{O}_{n\times mn} & \frac{\lambda}{\beta_n}G_n
\end{array}\right]}_{=:C_N^{(2)}}+\underbrace{\left[\begin{array}{ c c }
\mathrm{O}_{mn} & -\alpha_m\mathbf{q}\otimes I_n \\
\mathbf{e}_m^T\otimes I_n & \mathrm{O}_n
\end{array}\right]}_{=:C_N^{(3)}},\)

<tbc>so we can focus on each component individually. For the first one, we have<tbc>

\(C_N^{(1)}=U_{m+1}\otimes I_n-\underbrace{\left[\begin{array}{ c c }
\mathrm{O}_{mn} & \mathrm{O}_{mn\times n} \\
\gamma_me^{-\rho m\Delta t}I_n & \cdots \\
\gamma_1e^{-\rho\Delta t}I_n & \gamma_0I_n
\end{array}\right]}_{=:R_N^{(1)}},\)

<tbc>where \(\mathrm{rank}R_N^{(1)}\le n=o(N)\) as \(m,n\rightarrow\infty\). By Lemma 4.1, \(\{R_N^{(1)}\}_N\) is zero- distributed, hence by GLT 2<tbc>

\(\{R_N^{(1)}\}_N\sim_\mathrm{GLT}0.\)

<tbc>Moreover, we have \(U_{m+1}\otimes I_n=T_{m+1}(h_\xi)\otimes T_n(1)\), therefore applying GLT 2-7 leads to

\(\left\{C_N^{(1)}\right\}_N\sim_\mathrm{GLT}h_\xi(\theta_1).\) (6.12)

Concerning \(C_N^{(2)}\), we notice that<tbc>

\(C_N^{(2)}=\left[\begin{array}{ c c }
I_m\otimes\frac{\alpha_m}{\beta_n}G_n & \mathrm{O}_{mn\times n} \\
\mathrm{O}_{n\times mn} & \frac{\alpha_m}{\beta_n}G_n+\frac{\lambda-\alpha_m}{\beta_n}G_n
\end{array}\right]=I_{m+1}\otimes\frac{\alpha_m}{\beta_n}G_n+\underbrace{\left[\begin{array}{ c c }
\mathrm{O}_{mn} & \mathrm{O}_{mn\times n} \\
\mathrm{O}_{n\times mn} & \frac{\lambda-\alpha_m}{\beta_n}G_n
\end{array}\right]}_{=:R_N^{(2)}},\)

<tbc>in which once again \(\mathrm{rank}R_N^{(2)}=n=o(N)\) as \(m,n\rightarrow\infty\), so that<tbc>

\(\{R_N^{(2)}\}_N\sim_\mathrm{GLT}0.\)

<tbc>On the other hand, with the assumption that \(\frac{\alpha_m}{\beta_n}\rightarrow\nu\), by GLT 2 and GLT 7 we have<tbc>

\(\left\{I_{m+1}\otimes\frac{\alpha_m}{\beta_n}G_n\right\}_N=\left\{T_{m+1}(1)\otimes\frac{\alpha_m}{\beta_n}D_n(a)T_n(g_\eta)\right\}_N\sim_\mathrm{GLT}\nu a(x)g_\eta(\theta_2).\)

