## Problem tion

We consider the inverse source problem of identifying the source term _f(x,y_) from the space-time fractional diffusion equation

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,y,t)+a(x,y)\left(^C\mathcal{D}_x^{\eta_1}+^C\mathcal{D}_y^{\eta_2}\right)u(x,y,t)=q(t)f(x,y),(x,y,t)\in\Omega_T, \\
u(0,y,t)=0=u(1,y,t),y\in(0,1),t\in(0,T), \\
u(x,0,t)=0=u(x,1,t),x\in(0,1),t\in(0,T), \\
u(x,y,0)=\varphi(x,y),x\in(0,1),y\in(0,1), \\
u(x,y,T)=\phi(x,y),x\in(0,1),y\in(0,1),
\end{array}\right.\) (7.1)

where \(\Omega_T:=(0,1)\times(0,1)\times(0,T)\), \(^T\mathcal{D}_t^{\xi,\rho}\) denotes the tempered fractional derivative of order \(\xi\in(0,1)\) and \(\rho>0\) is the truncation parameter, _a(x,y_) is a continuous variable coefficient such that \(a(x,y)\neq 0\), \(^C\mathcal{D}_x^{\eta_1}\) and \(^C\mathcal{D}_y^{\eta_2}\) denote the Caputo fractional derivatives of orders \(\eta_1,\eta_2\in(0,1)\), _q(t_) is a given function, \(\varphi(x,y)\) is the initial condition, and \(\phi(x,y)\) is the final time datum.

The tempered fractional derivative in time variable of order \(\xi\in(0,1)\) is defined as follows<tbc>

\(^T\mathcal{D}_t^{\xi,\rho} u(x,y,t):=\frac{1}{\Gamma(1-\xi)}\int_0^te^{-\rho(t-\tau)}(t-\tau)^{-\xi}\frac{\partial}{\partial\tau}u(x,y,\tau)d\tau.\)

<tbc>The Caputo fractional derivative in the space variable of orders \(\eta\in(0,1)\) is defined as follows<tbc>

\(^C\mathcal{D}_x^\eta u(x,y,t)=\frac{1}{\Gamma(1-\eta)}\int_0^x(x-\zeta)^{-\eta}\frac{\partial}{\partial\zeta}u(x,y,\zeta)d\zeta,x>0,\)

<tbc>In practice, the measurement of the final time datum is inevitably affected by noise. Let us denote the noisy datum by \(\phi_\varepsilon(x,y)\), where \(\varepsilon>0\) represents the noise level. Assuming the noise is sufficiently small, we impose the condition<tbc>

\(\|\phi-\phi_\varepsilon\|_{L^2}\le\varepsilon,\)

<tbc>where \(\|\cdot\|_{L^2}\) is the _L_<sup>2</sup> norm on \((0,1)\times(0,1)\). Applying the quasi-boundary value method yields a class of parameter-dependent well-posed regularized problems

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,y,t)+a(x,y)\left(^C\mathcal{D}_x^{\eta_1}+^C\mathcal{D}_y^{\eta_2}\right)u(x,y,t)=q(t)f_{\varepsilon,\lambda}(x,y),(x,y,t)\in\Omega_T, \\
u(0,y,t)=0=u(1,y,t),y\in(0,1),t\in(0,T), \\
u(x,0,t)=0=u(x,1,t),x\in(0,1),t\in(0,T), \\
u(x,y,0)=\varphi(x,y),x\in(0,1),y\in(0,1), \\
u(x,y,T)=\phi_\varepsilon(x,y)-\lambda a(x,y)\left(^C\mathcal{D}_x^{\eta_1}+^C\mathcal{D}_y^{\eta_2}\right)f_{\varepsilon,\lambda}(x,y),x\in(0,1),y\in(0,1),
\end{array}\right.\) (7.2)

which approximate the original FDE in (7.1). Here, \(\lambda>0\) is a regularization parameter, \(f_{\varepsilon,\lambda}\) represents the regularized approximation of the source term _f(x,y_), and the solution \(u(x,y,t)\equiv u_{\varepsilon,\lambda}(x,y,t)\) provides an approximation to the original solution of problem (7.1). The regularization term \(\lambda a(x,y)\left(^C\mathcal{D}_x^{\eta_1}+^C\mathcal{D}_y^{\eta_2}\right)\) ensures that the reconstructed source term is stable and well-behaved, even in the presence of noise.

