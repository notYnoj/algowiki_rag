and solve the linear system arising from the corresponding direct problem<tbc>

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,t)+a(x)^C\mathcal{D}_x^\eta u(x,t)=q(t)f(x), & x\in(0,1),t\in(0,T), \\
u(0,t)=u(1,t)=0, & t\in(0,T), \\
u(x,0)=\varphi(x), & x\in(0,1).
\end{array}\right.\)

<tbc>With the same discretization technique adopted in Section 6.1, we obtain the linear system<tbc>

\(\tilde{A}_{m,n}\mathbf{u}=\mathbf{b},\)

<tbc>where

\(\tilde{A}_{m,n}:=\left[\begin{array}{ c c c c }
H_n & \mathrm{O}_n & \cdots & \mathrm{O}_n \\
\gamma_1e^{-\rho\Delta t}I_n & H_n & \ddots & \vdots \\
\vdots & \ddots & \ddots & \mathrm{O}_n \\
\gamma_{m-1}e^{-(m-1)\rho\Delta t}I_n & \cdots & \gamma_1e^{-\rho\Delta t}I_n & H_n
\end{array}\right]\in\mathbb{C}^{mn\times mn},\)<br>
\(\mathbf{u}:=\left[\begin{array}{ c }
\mathbf{u}^{(1)} \\
\mathbf{u}^{(2)} \\
\vdots \\
\mathbf{u}^{(m)}
\end{array}\right]\in\mathbb{C}^{mn},\mathbf{b}:=\left[\begin{array}{ c }
b_0e^{-\rho\Delta t}\varphi+\alpha_mq^{(1)}\mathbf{f} \\
b_1e^{-2\rho\Delta t}\varphi+\alpha_mq^{(2)}\mathbf{f} \\
\vdots \\
b_{m-1}e^{-m\rho\Delta t}\varphi+\alpha_mq^{(n)}\mathbf{f}
\end{array}\right]\in\mathbb{C}^{nm}.\)

By solving this system, we construct final time data **u**<sup>(_m_)</sup>, which we perturb by adding a random quantity \(\varepsilon\delta(x)\), where \(\delta(x)\) is randomly selected in the interval (-1,1). In this way, we simulate the contamination of \(\phi(x)\) by noise, obtaining \(\varphi_\varepsilon\). Then, we apply the GMRES method to (6.9) and report in  6.1 the number of iterations and the CPU timings (see Remark 6.6) required by both the nonpreconditioned and preconditioned linear systems. We set the regularization parameter to \(\lambda=5\cdot 10^{-3}\), the noise level to \(\varepsilon=0.01\), and vary both fractional orders. The initial guess is the zero vector, the tolerance is `tol`=10<sup>-8</sup>, and the maximum number of iterations is equal to the size of the matrix, _N_=(_m_+1)_n_. The experiments are performed on Intel(R), Xeon(R), Silver 4114, CPU@2.20GHz.<br>
Comparing the columns corresponding to the preconditioned and nonpreconditioned linear system, we observe that, for each choice of the fractional orders, _P<sub>N</sub>_ is indeed effective in reducing the number of iterations, confirming the theoretical predictions. It also appears to be stable, maintaining good results as the problems sizes increase and across all choices of fractional orders. Indeed, _P<sub>N</sub>_ demonstrates the best performance when the iteration counts for the nonpreconditioned linear system are particularly high, i.e, for \(\xi=0.2\), \(\eta=0.8\).<br>
Furthermore, for each choice of \(\xi\) and \(\eta\), the convergence rate in the preconditioned framework seems to depend almost exclusively on the spatial discretization finesse: in fact, for each fixed _n_, the number of iterations does not vary significantly as we increase _m_. This is reasonable, considering that the number of outliers in the cluster at 1 of the preconditioned matrix depends only on _n_.<br>
Looking more in detail, we observe that the growth in the parameter _n_ is less than linear, i.e., less than a constant times the square root of the global size, when _n_ and<tbc>

