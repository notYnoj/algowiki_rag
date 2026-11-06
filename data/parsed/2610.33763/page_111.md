In the one-dimensional case, the model reduces to

\(\left\{\begin{array}{ c c }
\frac{\partial}{\partial t}u(x,t)=a(x)\mathcal{D}_x^\alpha u(x,t)+f(x,t), & (x,t)\in(L_1,R_1)\times(0,T], \\
u(x,t)=0, & x\in\partial(L_1,R_1),t\in[0,T], \\
u(x,0)=\phi(x), & x\in(L_1,R_1).
\end{array}\right.\) (8.2)

The chapter is organized as follows. Section 8.1 contains the structural and spectral analysis of the relevant matrix sequences. In Sections 8.2 and 8.3, we introduce suitable preconditioners and study their spectral behavior. Finally, in Section 8.4, we present spectral visualizations and numerical experiments, and discuss the numerical results.

## 8.1 Discretized problem and GLT analysis

In this section, we present the discretization of the variable-coefficient space-fractional diffusion equation (8.1), posed on the spatial domain \(\Omega=(L_1,R_1)\times(L_2,R_2)\subset\mathbb{R}^2\). The equation is first reformulated on a discrete space-time grid, leading to a sequence of linear systems governed by structured coefficient matrices that encode the nonlocal behavior of the model. We then analyze the spectral properties of these matrices using the GLT framework. In particular, we compute the GLT symbol of the resulting matrix sequence, which characterizes the asymptotic distribution of eigenvalues and singular values.

### 8.1.1 Discretization

We first treat the one-dimensional space setting and then the two-dimensional space setting.

### One-dimensional

Let _M_ and _N_ be positive integers representing the number of temporal steps and the number of interior spatial grid points, respectively. The spatial and temporal meshes are defined as

\(x_i=L_1+i\Delta x,\Delta x=\frac{(R_1-L_1)}{(N+1)},0\le i\le N+1,\)<br> \(t_m=m\Delta t,\Delta t=\frac{T}{M},0\le m\le M.\)

To approximate the left-sided Riemann-Liouville fractional derivative, we adopt the shifted Grünwald finite difference scheme [91], which is widely recognized for its improved stability and accuracy compared to the standard Grünwald approach. The continuous fractional operator \(\mathcal{D}_x^\alpha u(x,t)\) is discretized at each interior point _x<sub>i</sub>_ using the following expression

\(\mathcal{D}_x^\alpha u(x,t)\big|_{x=x_i,t=t_m}=\frac{1}{(\Delta x)^\alpha}\sum_{k=0}^{i+1}g_{i-k+1}^{(\alpha)}u(x_k,t_m)+\mathcal{O}(\Delta x),\) (8.3)

