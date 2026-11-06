where \(\widetilde{\mathbf{N}}=\widetilde{\mathbf{N}}(m,\mathbf{n}):=(m+1)\nu(\mathbf{n})\) and

\(A_\widetilde{\mathbf{N}}:=\left[\begin{array}{ c c c c c }
\gamma_0I_\mathbf{n}+G_\mathbf{n} & \mathrm{O}_\mathbf{n} & \cdots & \mathrm{O}_\mathbf{n} & -\alpha_mq^1I_\mathbf{n} \\
\gamma_1e^{-\rho\Delta t}I_\mathbf{n} & \gamma_0I_\mathbf{n}+G_\mathbf{n} & \ddots & \vdots & -\alpha_mq^2I_\mathbf{n} \\
\vdots & \ddots & \ddots & \mathrm{O}_\mathbf{n} & \vdots \\
\gamma_{m-1}e^{-(m-1)\rho\Delta t}I_\mathbf{n} & \cdots & \gamma_1e^{-\rho\Delta t}I_\mathbf{n} & \gamma_0I_\mathbf{n}+G_\mathbf{n} & -\alpha_mq^mI_\mathbf{n} \\
\mathrm{O}_\mathbf{n} & \cdots & \mathrm{O}_\mathbf{n} & I_\mathbf{n} & \frac{\lambda}{\alpha_m}G_\mathbf{n}
\end{array}\right]\in\mathbb{C}^{\widetilde{\mathbf{N}}\times\widetilde{\mathbf{N}}},\)<br>
\(\mathbf{v}_\lambda:=\left[\begin{array}{ c }
\mathbf{u}^1 \\
\mathbf{u}^2 \\
\vdots \\
\frac{\mathbf{u}^m}{\mathbf{f}}
\end{array}\right]\in\mathbb{C}^\widetilde{\mathbf{N}},\mathbf{z}_\lambda:=\left[\begin{array}{ c }
b_0e^{-\rho\Delta t}\varphi \\
b_1e^{-2\rho\Delta t}\varphi \\
\vdots \\
\frac{b_{m-1}e^{-m\rho\Delta t}\varphi}{\phi}
\end{array}\right]\in\mathbb{C}^\widetilde{\mathbf{N}},\)

in which _I_**<sub>n</sub>** is the \(\mathbf{n}\times\mathbf{n}\) identity matrix, O**<sub>n</sub>** is the \(\mathbf{n}\times\mathbf{n}\) zero matrix, and

\(G_\mathbf{n}:=D_\mathbf{n}(a)\left(B_\mathbf{n}^x+B_\mathbf{n}^y\right).\) (7.17)

Moreover, setting<tbc>

\(U_m:=\left[\begin{array}{ c c c c c }
\gamma_0 & 0 & \cdots & 0 \\
\gamma_1e^{-\rho\Delta t} & \gamma_0 & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
\gamma_{m-1}e^{-\rho(m-1)\Delta t} & \cdots & \gamma_1e^{-\rho\Delta t} & \gamma_0
\end{array}\right],\)

<tbc>the coefficient matrix can be expressed into the compact form

\(A_\widetilde{\mathbf{N}}=\left[\frac{U_m\otimes I_\mathbf{n}+I_m\otimes G_\mathbf{n}}{\mathbf{e}_m^T\otimes I_\mathbf{n}}\right|\frac{-\alpha_m\mathbf{q}\otimes I_\mathbf{n}}{\frac{\lambda}{\alpha_m}G_\mathbf{n}}\right],\) (7.18)

in which

\(\mathbf{e}_m:=\left[\begin{array}{ c }
0 \\
\vdots \\
0 \\
1
\end{array}\right]\in\mathbb{R}^m,\mathbf{q}:=\left[\begin{array}{ c }
q^1 \\
q^1 \\
\vdots \\
q^m
\end{array}\right]\in\mathbb{R}^m.\)

## 7.2 GLT analysis

This section presents the spectral analysis of the coefficient matrix sequence via GLT theory to describe its asymptotic behavior. We first report the symbols of \(\{B_n^x\}_n\) and the time block {_U<sub>m</sub>}<sub>m</sub>_ given in Chapter 6, then analyze the space block {_G_**<sub>n</sub>**}**<sub>n</sub>**, and finally consider the full coefficient matrix sequence.

