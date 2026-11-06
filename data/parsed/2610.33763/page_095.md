To discretize the Caputo fractional derivative with respect to _x_, we exploit the _L_1 formula:<tbc>

\(^c\mathcal{D}_{L1}^{\eta_1}u(x_i,y_j,t_s)=\frac{1}{\beta_{n_1}}\left[\delta_0u_{i,j}^s+\sum_{k_1=1}^{i-1}\delta_{i-k_1}u_{k_1,j}^s-d_{i-1}u_{0,j}^s\right],\) (7.8)

<tbc>where<tbc>

\(\beta_{n_1}:=(\Delta x)^{\eta_1}\Gamma(2-\eta_1)=\left(\frac{1}{n_1+1}\right)^{\eta_1}\Gamma(2-\eta_1)\) (7.9)

<tbc>and<tbc>

\(d_{k_1}:=(k_1+1)^{1-\eta_1}-k_1^{1-\eta_1},k_1=0,1,\dots\)<br>
\(\delta_0:=d_0,\)<br>
\(\delta_{k_1}:=d_{k_1}-d_{k_1-1}=(k_1+1)^{1-\eta_1}-2k_1^{1-\eta_1}+(k_1-1)^{1-\eta_1},k_1=1,\dots,n_1-1.\) (7.10)

<tbc>Now, we proceed to discretize the Caputo fractional derivative with respect to _y_ by employing the _L_1 approximation formula<tbc>

\(^c\mathcal{D}_{L1}^{\eta_2}u(x_i,y_j,t_s)=\frac{1}{\beta_{n_2}}\left[\sigma_0u_{i,j}^s+\sum_{k_2=1}^{j-1}\sigma_{j-k_2}u_{i,k_2}^s-c_{j-1}u_{i,0}^s\right],\) (7.11)

<tbc>where<tbc>

\(\beta_{n_2}:=(\Delta x)^{\eta_2}\Gamma(2-\eta_2)=\left(\frac{1}{n_2+1}\right)^{\eta_2}\Gamma(2-\eta_2)\) (7.12)

<tbc>and<tbc>

\(c_{k_2}:=(k_2+1)^{1-\eta_2}-k_2^{1-\eta_2},k_2=0,1,\dots\)<br>
\(\sigma_0:=c_0,\)<br>
\(\sigma_{k_2}:=c_{k_2}-c_{k_2-1}=(k_2+1)^{1-\eta_2}-2k_2^{1-\eta_2}+(k_2-1)^{1-\eta_2},k_2=1,\dots,n_2-1.\) (7.13)

<tbc>Substituting the fractional derivatives in problem (7.2) with their respective _L_1 approximations (7.7) and (7.8) and (7.11), and omitting the truncation errors, the finite difference scheme is constructed as follows:<tbc>

\(\left\{\begin{array}{ c }
\frac{1}{\alpha_m}\left[\gamma_0u_{i,j}^s+\sum_{l=1}^{s-1}\gamma_{s-l}e^{-(n-l)\rho\Delta t}u_{i,j}^l-b_{s-1}e^{-s\rho\Delta t}u_{i,j}^0\right]+\frac{a_{i,j}}{\beta_{n_1}}\left[\delta_0u_{i,j}^s+\sum_{k_1=1}^{i-1}\delta_{i-k_1}u_{k_1,j}^s \\
-d_{i-1}u_{0,j}^s\right]+\frac{a_{i,j}}{\beta_{n_2}}\left[\sigma_0u_{i,j}^s+\sum_{k_2=1}^{j-1}\sigma_{j-k_2}u_{i,k_2}^s-c_{j-1}u_{j,0}^s\right]=q^sf_{i,j}, \\
u_{0,j}^s=u_{n_1+1,j}^s=0,u_{i,0}^s=u_{i,n_2+1}^s=0, \\
u_{i,j}^0=\varphi_{i,j}, \\
u_{i,j}^m=\phi_{i,j}-\lambda\frac{a_{i,j}}{\beta_{n_1}}\left[\delta_0f_{i,j}+\sum_{k_1=1}^{i-1}\delta_{i-k_1}f_{k_1,j}-d_{i-1}f_{0,j}\right]-\lambda\frac{a_{i,j}}{\beta_{n_2}}\left[\sigma_0f_{i,j}+\sum_{k_2=1}^{j-1}\sigma_{j-k_2}f_{i,k_2} \\
-c_{j-1}f_{i,0}\right].
\end{array}\right.\)

