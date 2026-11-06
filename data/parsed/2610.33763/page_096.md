By defining the corresponding vectors<tbc>

\(\mathbf{u}^s:=\left[u_{i,j}^s\right]_{i=1,\dots,n_1,j=1,\dots,n_2},\mathbf{a}:=\left[a_{i,j}\right]_{i=1,\dots,n_1,j=1,\dots,n_2},\mathbf{f}:=\left[f_{i,j}\right]_{i=1,\dots,n_1,j=1,\dots,n_2},\)<br>
\(\varphi:=\left[\varphi_{i,j}\right]_{i=1,\dots,n_1,j=1,\dots,n_2},\varphi:=\left[\phi_{i,j}\right]_{i=1,\dots,n_1,j=1,\dots,n_2},\)

<tbc>Now, let **n**=_n_<sub>1</sub>_n_<sub>2</sub>, then we can write the numerical scheme in matrix form as<tbc>

\(\left\{\begin{array}{ c }
\gamma_0\mathbf{u}^s+\sum_{l=1}^{s-1}\gamma_{s-l}e^{-(s-l)\rho\Delta t}\mathbf{u}^l+D_\mathbf{n}(a)\left(B_\mathbf{n}^x+B_\mathbf{n}^y\right)\mathbf{u}^s-\alpha_mq^s\mathbf{f}=b_{s-1}e^{-s\rho\Delta t}\varphi, \\
s=1,\dots,m, \\
\mathbf{u}^m+\lambda D_\mathbf{n}(a)\left(B_\mathbf{n}^x+B_\mathbf{n}^y\right)\mathbf{f}=\varphi,
\end{array}\right.\)

<tbc>where _D_**<sub>n</sub>**(_a_) is the diagonal sampling matrix of size _M_ associated to _a(x,y_), while \(B_M^x\) are \(B_M^y\) are defined as follows<tbc>

\(B_\mathbf{n}^x=I_{n_2}\otimes\frac{\alpha_m}{\beta_{n_1}}B_{n_1}^x,\) (7.14)

<tbc>and<tbc>

\(B_\mathbf{n}^y=\frac{\alpha_m}{\beta_{n_2}}B_{n_2}^y\otimes I_{n_1}.\) (7.15)

<tbc>Here _B_<sub>_n_<sub>1</sub></sub> are _B_<sub>_n_<sub>2</sub></sub> are the following lower triangular Toeplitz matrices<tbc>

\(B_{n_1}^x:=\left[\begin{array}{ c c c c c c c c }
\delta_0 & 0 & \cdots & \cdots & \cdots & 0 \\
\delta_1 & \delta_0 & 0 & & & \vdots \\
\delta_2 & \delta_1 & \delta_0 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & 0 \\
\delta_{n_1-1} & \cdots & \delta_2 & \delta_1 & \delta_0
\end{array}\right],\)

<tbc>and<tbc>

\(B_{n_2}^y:=\left[\begin{array}{ c c c c c c c }
\sigma_0 & 0 & \cdots & \cdots & \cdots & 0 \\
\sigma_1 & \delta_0 & 0 & & & \vdots \\
\sigma_2 & \delta_1 & \delta_0 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & 0 \\
\sigma_{n_2-1} & \cdots & \delta_2 & \sigma_1 & \sigma_0
\end{array}\right].\)

<tbc>By gathering the equations for all the time levels and the regularization equation, we obtain the all-at-once linear system<tbc>

\(A_\widetilde{\mathbf{N}}\mathbf{v}_\lambda=\mathbf{z}_\lambda,\) (7.16)

