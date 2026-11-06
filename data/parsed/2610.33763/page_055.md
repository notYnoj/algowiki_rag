## 5.1.1 Generalized Caputo-type fractional derivative

In this study, we utilize the generalized time-fractional derivative of Caputo-type as formulated by Kochubei \[76\], presented in the following form

\(_G\mathcal{D}_t^{(\varrho)}u(x,y,t):=\int_0^t\varrho(t-\tau)\frac{\partial}{\partial\tau}u(x,y,\tau)d\tau,\) (5.1)

where \(\varrho(t)\in L_{loc}^1(\mathbb{R}_+)\) represents a locally integrable, non-negative function commonly referred to as the memory kernel. The Laplace transform of \(\varrho(t)\), denoted \(\widehat{\varrho}(s)\), exists for all _s\>_0 and satisfies

\(\widehat{\varrho}(s)\in\mathbb{SF},\text{and}lim_{s\rightarrow\infty} s\widehat{\varrho}(s)=+\infty,\) (5.2)

where SF denotes the class of Stieltjes functions, as discussed in \[13\]. The class of SF includes all functions on R<sub>+</sub> that have the following representation

\(\widehat{\phi}(s)=\frac{a}{s}+b+\int_0^\infty\mathrm{e}^{-s\tau}\varphi(\tau)d\tau,s>0,\) (5.3)

where \(a,b\ge 0\), \(\varphi\) is the completely monotone function and the Laplace transform of \(\varphi\) exists for any _s\>_0. A function \(\phi\) defined on R<sub>+</sub> is said to be a complete Bernstein function (CBF) if and only if

\(\frac{\widehat{\phi}(s)}{s}\in\mathbb{SF},s>0.\) (5.4)

Assuming \(\widehat{\varrho}(s)\in\mathbb{SF}\) implies that \(\widehat{\varrho}(s)\) can be represented in the specific form given by Eq. (5.3). Therefore, the kernel \(\varrho(t)\) is completely monotone for _t\>_0 and can have an additional term \(b\delta(t)\), where \(b\ge 0\), and \(\delta(\cdot)\) denotes the Dirac delta function. Moreover, the condition \(\widehat{\varrho}(s)\in\mathbb{SF}\) is equivalent to the condition \(s\widehat{\varrho}(s)\in\mathbb{CBF}\), see Eq. (5.4).

## 5.1.2 Statement of the problem

In this work, we investigate a two-dimensional generalized diffusion equation with memory kernel of the form

\(_G\mathcal{D}_t^{(\varrho)}u(x,y,t)=u_{xx}(x,y,t)+u_{yy}(x,y,t)+F(x,y,t),(x,y,t)\in\Omega,\) (5.5)

within the domain<tbc>

\(\Omega:=(0,1)\times(0,1)\times(0,T],\)

<tbc>alongside the following boundary conditions

\(u(0,y,t)=0,u_x(1,y,t)-d\big(u_{xx}(1,y,t)+u_{yy}(1,y,t)\big)=0,\) (5.6)

\(y\in[0,1],t\in[0,T],d=const>0,\)<br>
\(u(x,0,t)=0,u_y(x,1,t)=0,x\in[0,1],t\in[0,T],\) (5.7)

and the initial condition

\(u(x,y,0)=\psi(x,y),y\in[0,1],x\in[0,1],\) (5.8)

where \(_G\mathcal{D}_t^{(\varrho)}\) is given by Eq. (5.1).

