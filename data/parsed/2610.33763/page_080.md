By gathering the equations for all the time levels and the regularization equation, we obtain the all-at-once linear system<tbc>

\(A_N\mathbf{v}_\lambda=\mathbf{z}_\lambda,\) (6.9)

<tbc>where _N=N(m,n_):=(_m_+1)_n_ and<tbc>

\(A_N:=\left[\begin{array}{ c c c c c }
H_n & \mathrm{O}_n & \cdots & \mathrm{O}_n & -\alpha_mq^{(1)}I_n \\
\gamma_1e^{-\rho\Delta t}I_n & H_n & \ddots & \vdots & -\alpha_mq^{(2)}I_n \\
\vdots & \ddots & \ddots & \mathrm{O}_n & \vdots \\
\gamma_{m-1}e^{-(m-1)\rho\Delta t}I_n & \cdots & \gamma_1e^{-\rho\Delta t}I_n & H_n & -\alpha_mq^{(m)}I_n \\
\mathrm{O}_n & \cdots & \mathrm{O}_n & I_n & \frac{\lambda}{\beta_n}G_n
\end{array}\right]\in\mathbb{C}^{N\times N},\)

\(\mathbf{v}_\lambda:=\left[\begin{array}{ c }
\mathbf{u}^{(1)} \\
\mathbf{u}^{(2)} \\
\vdots \\
\mathbf{u}^{(m)} \\
\mathbf{f}
\end{array}\right]\in\mathbb{C}^N,\mathbf{z}_\lambda:=\left[\begin{array}{ c }
b_0e^{-\rho\Delta t}\varphi \\
b_1e^{-2\rho\Delta t}\varphi \\
\vdots \\
b_{m-1}e^{-m\rho\Delta t}\varphi \\
\phi_\varepsilon
\end{array}\right]\in\mathbb{C}^N,\)

in which _I<sub>n</sub>_ is the \(n\times n\) identity matrix, O_<sub>n</sub>_ is the \(n\times n\) zero matrix, and<tbc>

\(H_n:=\gamma_0I_n+\frac{\alpha_m}{\beta_n}G_n,\text{\textit{with}}G_n:=D_n(a)B_n.\) (6.10)

<tbc>Moreover, setting<tbc>

\(U_m:=\left[\begin{array}{ c c c c }
\gamma_0 & 0 & \cdots & 0 \\
\gamma_1e^{-\rho\Delta t} & \gamma_0 & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
\gamma_{m-1}e^{-\rho(m-1)\Delta t} & \cdots & \gamma_1e^{-\rho\Delta t} & \gamma_0
\end{array}\right],\)

<tbc>the coefficient matrix can be expressed into the compact form<tbc>

\(A_N=\left[\frac{U_m\otimes I_n+I_m\otimes\frac{\alpha_m}{\beta_n}G_n}{\mathbf{e}_m^T\otimes I_n}\right],\) (6.11)

<tbc>in which<tbc>

\(\mathbf{e}_m:=\left[\begin{array}{ c }
0 \\
\vdots \\
0 \\
1
\end{array}\right]\in\mathbb{R}^m,\mathbf{q}:=\left[\begin{array}{ c }
q^{(1)} \\
q^{(2)} \\
\vdots \\
q^{(m)}
\end{array}\right]\in\mathbb{R}^m.\)

<tbc>For concluding the present section, two remarks are useful, the first for clarifying the approximation order of the used scheme and the second concerning the non singular character of the coefficient matrix _A<sub>N</sub>_.

