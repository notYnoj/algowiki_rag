_2._ _If the discretization formulae used in Section 7.1 are replaced by high order finite elements in space of order p\>_1 _or by the isogeometric analysis with degree p and regularity k\<p_-1_, then we would end up with block multilevel matrix sequences, the dimensionality r of the GLT symbol would by either p<sup>d</sup> or_ (_p-k)<sup>d</sup> with d_=2_. Again the analysis given here can be performed almost verbatim with minimal technical changes, thanks to the uniform structure of the GLT axioms._

_Of course the directions indicated in 1) and 2) can be combined and even extended to higher space dimensionality with_ \(\Omega\subset\mathbb{R}^d\), \(d\ge 2\)_, so having the potential of providing a very general picture._

## 7.4 Numerical results and study of the computational cost

We evaluate the efficiency of the proposed preconditioner by measuring the number of GMRES iterations required for convergence. Let us consider the two-dimensional problem on the domain \(\Omega=(0,1)^2\) and \(t\in(0,T)\). We set<tbc>

\(T=1,a(x,y)=x+y,q(t)=t^2,\varphi(x,y)=0.\)

<tbc>To construct the noisy final data, we select the source function<tbc>

\(f(x,y)=xy\mathrm{sin}(\pi x)\mathrm{sin}(\pi y).\)

<tbc>and solve the linear system arising from the corresponding direct problem

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,y,t)+a(x,y)\left(^C\mathcal{D}_x^{\eta_1}+^C\mathcal{D}_y^{\eta_2}\right)u(x,y,t)=q(t)f(x,y), & (x,y,t)\in\Omega_T, \\
u(0,y,t)=0=u(1,y,t), & y\in(0,1),t\in(0,T), \\
u(x,0,t)=0=u(x,1,t), & x\in(0,1),t\in(0,T), \\
u(x,y,0)=\varphi(x,y), & x\in(0,1),y\in(0,1).
\end{array}\right.\)

<tbc>With the same discretization technique adopted in Section 7.1, we obtain the linear system<tbc>

\(\tilde{A}_{m,\mathbf{n}}\tilde{\mathbf{u}}=\tilde{\mathbf{b}},\)

<tbc>where

\(\tilde{A}_{m,\mathbf{n}}:=\left[\begin{array}{ c c c c }
\gamma_0I_\mathbf{n}+G_\mathbf{n} & \mathrm{O}_\mathbf{n} & \cdots & \mathrm{O}_\mathbf{n} \\
\gamma_1e^{-\rho\Delta t}I_\mathbf{n} & \gamma_0I_\mathbf{n}+G_\mathbf{n} & \ddots & \vdots \\
\vdots & \ddots & \ddots & \mathrm{O}_m \\
\gamma_{m-1}e^{-(m-1)\rho\Delta t}I_\mathbf{n} & \cdots & \gamma_1e^{-\rho\Delta t}I_\mathbf{n} & \gamma_0I_\mathbf{n}+G_\mathbf{n}
\end{array}\right]\in\mathbb{C}^{m\mathbf{n}\times m\mathbf{n}},\)<br>
\(\tilde{\mathbf{u}}:=\left[\begin{array}{ c }
\mathbf{u}^{(1)} \\
\mathbf{u}^{(2)} \\
\vdots \\
\mathbf{u}^{(m)}
\end{array}\right]\in\mathbb{C}^{m\mathbf{n}},\tilde{\mathbf{b}}:=\left[\begin{array}{ c }
b_0e^{-\rho\Delta t}\varphi+\alpha_mq^1\mathbf{f} \\
b_1e^{-2\rho\Delta t}\varphi+\alpha_mq^2\mathbf{f} \\
\vdots \\
b_{m-1}e^{-m\rho\Delta t}\varphi+\alpha_mq^m\mathbf{f}
\end{array}\right]\in\mathbb{C}^{m\mathbf{n}}.\)

