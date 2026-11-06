As in the one-dimensional setting, we adopt the shifted Grünwald finite difference scheme \[91\] to approximate the left-sided Riemann-Liouville fractional derivatives. The continuous fractional operator \(\mathcal{D}_x^{\alpha_1}u(x,y,t)\) is discretized at each interior point _x<sub>i</sub>_ using the expression below

\(\mathcal{D}_x^{\alpha_1}u(x,y,t)\big|_{x=x_i,y=y_j,t=t_m}=\frac{1}{(\Delta x)^{\alpha_1}}\sum_{k=0}^{i+1}g_{i-k+1}^{(\alpha_1)}u(x_k,y_j,t_m)+\mathcal{O}(\Delta x),\) (8.17)

with related properties of \(g_k^{(\alpha_1)}\) already given in the one-dimensional setting in Proposition 8.1. Similarly, to discretize the \(\mathcal{D}_y^{\alpha_2}u(x,y,t)\) at each interior point _y<sub>j</sub>_, we deduce the following relation

\(\mathcal{D}_y^{\alpha_2}u(x,y,t)\big|_{x=x_i,y=y_j,t=t_m}=\frac{1}{(\Delta y)^{\alpha_2}}\sum_{l=0}^{j+1}g_{j-l+1}^{(\alpha_2)}u(x_i,y_l,t_m)+\mathcal{O}(\Delta y),\) (8.18)

with related properties of \(g_l^{(\alpha_2)}\) already given in the one-dimensional setting in Proposition 8.1.

Applying the spatial discretization (8.17)-(8.18) and the temporal discretization, we use the \(\theta\)-method \[101\] on (8.1), which yields the following time-stepping scheme

\(\frac{u_{i,j}^{(m+1)}-u_{i,j}^{(m)}}{\Delta t}=\theta a(x_i,y_j)\left(\frac{1}{(\Delta x)^{\alpha_1}}\sum_{k=0}^{i+1}g_k^{(\alpha_1)}u_{i-k+1,j}^{(m+1)}+\frac{1}{(\Delta y)^{\alpha_2}}\sum_{l=0}^{j+1}g_l^{(\alpha_2)}u_{i,j-l+1}^{(m+1)}\right)\)<br>
\(+(1-\theta)a(x_i,y_j)\left(\frac{1}{(\Delta x)^{\alpha_1}}\sum_{k=0}^{i+1}g_k^{(\alpha_1)}u_{i-k+1,j}^{(m)}+\frac{1}{(\Delta y)^{\alpha_2}}\sum_{l=0}^{j+1}g_l^{(\alpha_2)}u_{i,j-l+1}^{(m)}\right)+f_{i,j}^{m,\theta},\) (8.19)

where \(u_{i,j}^{(m)}\) approximates _u(x<sub>i</sub>,y<sub>j</sub>,t<sub>m</sub>_) and \(f_{i,j}^{(m,\theta)}=\theta f(x_i,y_j,t_{m+1})+(1-\theta)f(x_i,y_j,t_m)\). By defining the vectors

\(u_\mathbf{n}^{(m)}=\left[u_{i,j}^{(m)}\right]_{i=1,\dots,N_1,j=1,\dots,N_2}^T,f_\mathbf{n}^{(m,\theta)}=\left[f_{i,j}^{(m,\theta)}\right]_{i=1,\dots,N_1,j=1,\dots,N_2}^T,\mathbf{n}=N_1N_2\)

according to the lexicographic order and by multiplying both sides of (8.19) by \(\Delta t\) and simplifying, we obtain

\(u_\mathbf{n}^{(m+1)}-u_\mathbf{n}^{(m)}=\theta G_{\alpha,\mathbf{n}}u_\mathbf{n}^{(m+1)}+(1-\theta)G_{\alpha,\mathbf{n}}u_\mathbf{n}^{(m)}+\Delta tf_\mathbf{n}^{(m,\theta)},m=0,\dots,M-1,\) (8.20)

where

\(G_{\alpha,\mathbf{n}}=D_\mathbf{n}(a)U_{\alpha,\mathbf{n}}\in\mathbb{R}^{\mathbf{n}\times\mathbf{n}},\) (8.21)

\(U_{\alpha,\mathbf{n}}=\gamma_1\overline{G_{\alpha_1,n_1}}\otimes I_{n_2}+I_{n_1}\otimes\gamma_2\overline{G_{\alpha_2,n_2}}\in\mathbb{R}^{\mathbf{n}\times\mathbf{n}},\) (8.22)

\(\mathcal{D}_\mathbf{n}(a)=\text{diag}_{i=1,\dots,n_1j=1,\dots,n_2}(a\left(x_i,y_j\right))\in\mathbb{R}^{\mathbf{n}\times\mathbf{n}},\) (8.23)

with \(\overline{G_{\alpha_1,N_1}}\) and \(\overline{G_{\alpha_2,N_2}}\) defined as in (8.9). In terms of notations, notice that D**<sub>n</sub>**(_a_) coincides with _D_**<sub>n</sub>**(_a_) as in (4.1) with _d_=2_,r_=1 if the domain of definition of the function _a_ is \[0,1\]<sup>2</sup>. In general \([L_1,R_1]\times[L_2,R_2]\neq[0,1]^2\) and hence \(\mathcal{D}_\mathbf{n}(a)=D_\mathbf{n}(\hat{a})\)<tbc>

