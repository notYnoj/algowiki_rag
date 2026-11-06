\(\eta\in(0,1)\), defined as<tbc>

\(^C\mathcal{D}_x^\eta u(x,t):=\frac{1}{\Gamma(1-\eta)}\int_0^x(x-\zeta)^{-\eta}\frac{\partial}{\partial\zeta}u(\zeta,t)\mathrm{d}\zeta.\)

<tbc>To address the ill-posedness in the sense of Hadamard of the inverse problem (6.1), we apply the so-called nonlocal or quasi-boundary value method, transforming it into a well-posed formulation. First, we observe that the measurement of the final time data is inevitably contaminated by noise, therefore we denote the noisy data as \(\phi_\varepsilon(x)\), where \(\varepsilon>0\) is the noise level, and assume that<tbc>

\(\|\phi-\phi_\varepsilon\|_{L^2}\le\varepsilon,\)

<tbc>where \(\|\cdot\|_{L^2}\) is the _L_<sup>2</sup> norm on (0,1). Applying the quasi-boundary value method leads to the following well-posed regularized problem

\(\left\{\begin{array}{ c c }
^T\mathcal{D}_t^{\xi,\rho} u(x,t)+a(x)^C\mathcal{D}_x^\eta u(x,t)=q(t)f_{\varepsilon,\lambda}(x), & x\in(0,1),t\in(0,T), \\
u(0,t)=u(1,t)=0, & t\in(0,T), \\
u(x,0)=\varphi(x), & x\in(0,1), \\
u(x,T)=\phi_\varepsilon(x)-\lambda a(x)^C\mathcal{D}_x^\eta f_{\varepsilon,\lambda}(x), & x\in(0,1),
\end{array}\right.\) (6.2)

where \(\lambda>0\) is a regularization parameter, \(f_{\varepsilon,\lambda}\) approximates _f(x_) and the solution _u(x,t_) represents an approximation of the solution of the original problem (6.1).

The remainder of this chapter is organized as follows. Section 6.1 provides the discretization of the regularized problem by using a finite difference scheme in space and time and presents the resulting linear system, emphasizing the structural features of the resulting matrices. In Section 6.2 the coefficient matrix sequence is studied via GLT tools, while in Section 6.3 the same type of analysis is performed for the preconditioned matrix sequences. In Section 6.4, numerical experiments are conducted to assess the effectiveness of the proposed preconditioner.

## 6.1 Discretization and matrix structures

We now present the discretization of the regularized problem (6.2), using a finite difference scheme [130]. Then we describe with care the global structure of the arising coefficient matrix.

Let _n_ and _m_ be positive integers and denote the corresponding spatial and temporal meshes as

\(x_i=i\Delta x,\Delta x=\frac{1}{n+1},i=0,1,\dots,n,\) (6.3)

\(t_j=j\Delta t,\Delta t=\frac{T}{m},j=0,1,\dots,m.\) (6.4)

To deal with the tempered fractional derivative, we use the _L_1 formula:

\(^T\mathcal{D}_{L1}^{\xi,\rho} u(x,t_j)=\frac{(\Delta t)^{-\xi}}{\Gamma(2-\xi)}\big[b_0u(x,t_j)-\sum_{l=1}^{j-1}\left(b_{j-l-1}-b_{j-l}\right)e^{\rho(t_l-t_j)}u(x,t_l)\)<br>
\(-b_{j-1}e^{\rho(t_0-t_j)}u(x,t_0)\big],\)

