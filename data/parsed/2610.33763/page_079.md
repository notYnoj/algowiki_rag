where _u<sub>xx</sub>_ denote the second partial derivative of _u_ with respect to _x_ and

\(\chi_\eta:=\frac{1}{2\Gamma(1-\eta)}\left[\frac{1}{4}+\frac{\eta}{(1-\eta)(2-\eta)}\right].\)

Substituting the fractional derivatives in problem (6.2) with their respective _L_1 approximations (6.6) and (6.7), and omitting the truncation errors, the finite difference scheme is constructed as follows: in (_x<sub>i</sub>,t<sub>j</sub>_) for _i_=1_,...,n_ and _j_=1_,...,m_ we have

\(\left\{\begin{array}{ c }
\frac{1}{\alpha_m}\left[\gamma_0u_i^{(j)}+\sum_{l=1}^{j-1}\gamma_{j-l}e^{-(j-l)\rho\Delta t}u_i^{(l)}-b_{j-1}e^{-j\rho\Delta t}u_i^{(0)}\right] \\
+\frac{a_i}{\beta_n}\left[\delta_0u_i^{(j)}+\sum_{k=1}^{i-1}\delta_{i-k}u_k^{(j)}-d_{i-1}u_0^{(j)}\right]=q^{(j)}f_i, \\
u_0^{(j)}=u_{n+1}^{(j)}=0, \\
u_i^{(0)}=\varphi_i, \\
u_i^{(m)}=\phi_{\varepsilon,i}-\lambda\frac{a_i}{\beta_n}\left[\delta_0f_i+\sum_{k=1}^{i-1}\delta_{i-k}f_k-d_{i-1}f_0\right],
\end{array}\right.\)

where

\(u_i^{(j)}:=u(x_i,t_j),a_i:=a(x_i),f_i:=f_{\varepsilon,\lambda}(x_i),\)<br>
\(\varphi_i:=\varphi(x_i),\phi_{\varepsilon,i}:=\phi_\varepsilon(x_i),q^{(j)}:=q(t_j).\)

By defining the corresponding vectors

\(\mathbf{u}^{(j)}:=\left[u_i^{(j)}\right]_{i=1}^n,\mathbf{a}:=\left[a_i\right]_{i=1}^n,\mathbf{f}:=\left[f_i\right]_{i=1}^n,\)<br>
\(\varphi:=\left[\varphi_i\right]_{i=1}^n,\varphi_\varepsilon:=\left[\phi_{\varepsilon,i}\right]_{i=1}^n,\)

we can write the numerical scheme in matrix form as

\(\left\{\begin{array}{ c }
\gamma_0\mathbf{u}^{(j)}+\sum_{l=1}^{j-1}\gamma_{j-l}e^{-(j-l)\rho\Delta t}\mathbf{u}^{(l)}+\frac{\alpha_m}{\beta_n}D_n(a)B_n\mathbf{u}^{(j)} \\
-\alpha_mq^{(j)}\mathbf{f}=b_{j-1}e^{-j\rho\Delta t}\varphi,j=1,\dots,m, \\
\mathbf{u}^{(m)}+\frac{\lambda}{\beta_n}D_n(a)B_n\mathbf{f}=\varphi_\varepsilon,
\end{array}\right.\)

where _D<sub>n</sub>(a_) is the diagonal sampling matrix of size _n_ associated to _a(x_), while _B<sub>n</sub>_ is the following lower triangular Toeplitz matrix

\(B_n:=\left[\begin{array}{ c c c c c c }
\delta_0 & 0 & \cdots & \cdots & 0 \\
\delta_1 & \delta_0 & 0 &  & \vdots \\
\delta_2 & \delta_1 & \delta_0 & \ddots & \vdots \\
\vdots & \ddots & \ddots & \ddots & 0 \\
\delta_{n-1} & \cdots & \delta_2 & \delta_1 & \delta_0
\end{array}\right].\)

