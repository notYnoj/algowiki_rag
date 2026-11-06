The structure of the paper is as follows. Section 7.1 outlines the discretization of the regularized problem using a finite difference scheme for both space and time, and discusses the structural properties of the resulting linear system. In Section 7.2, we analyze the coefficient matrix sequence using GLT theory. Section 7.3 extends this analysis to the preconditioned matrix sequences. In Section 7.4, we conduct numerical experiments to evaluate the performance of the proposed preconditioner and we report a detailed analysis of the computational costs.

## 7.1 Discretization and matrix structures

In the current section, we present the discretization of the regularized problem (7.2) using a finite difference scheme \[130\]. We then carefully discuss the global structure of the resulting coefficient matrix.<br>
Let _n_<sub>1</sub>, _n_<sub>2</sub> and _m_ be positive integers and denote the corresponding spatial and temporal meshes as

\(x_i=i\Delta x,\Delta x=\frac{1}{n_1+1},i=0,1,\dots,n_1,\) (7.3)

\(y_j=j\Delta y,\Delta y=\frac{1}{n_2+1},j=0,1,\dots,n_2,\) (7.4)

\(t_s=s\Delta t,\Delta t=\frac{T}{m},s=0,1,\dots,m.\) (7.5)

The approximate values of the functions at the grid points are denoted as follows

\(u_{i,j}^s:=u(x_i,y_j,t_s),a_{i,j}:=a(x_i,y_j),f_{i,j}:=f_{\varepsilon,\lambda}(x_i,y_j),\)<br>
\(\varphi_{i,j}:=\varphi(x_i,y_j),\phi_{i,j}:=\phi_\varepsilon(x_i,y_j),q^s:=q(t_s).\)

To deal with the tempered fractional derivative, we use the _L_1 formula:<tbc>

\(^T\mathcal{D}_{L1}^{\xi,\rho} u(x_i,y_j,t_s)=\frac{(\Delta t)^{-\xi}}{\Gamma(2-\xi)}\left[b_0u_{i,j}^s-\sum_{l=1}^{s-1}(b_{s-l-1}-b_{s-l})e^{\rho(t_l-t_s)}u_{i,j}^l-b_{s-1}e^{\rho(t_0-t_s)}u_{i,j}^0\right],\)

<tbc>in which<tbc>

\(b_l=(l+1)^{1-\xi}-l^{1-\xi},l=0,1,\dots\)

<tbc>Denoting<tbc>

\(\alpha_m:=(\Delta t)^\xi\Gamma(2-\xi)=\left(\frac{T}{m}\right)^\xi\Gamma(2-\xi)\)

<tbc>and

\(\gamma_0:=b_0,\gamma_l:=b_l-b_{l-1}=(l+1)^{1-\xi}-2l^{1-\xi}+(l-1)^{1-\xi},l=1,\dots,m-1,\) (7.6)

and using \(t_s=s\Delta t\), the _L_1 approximation of the tempered fractional derivative is expressed as

\(^T\mathcal{D}_{L1}^{\xi,\rho} u(x_i,y_j,t_s)=\frac{1}{\alpha_m}\left[\gamma_0u_{i,j}^s+\sum_{l=1}^{s-1}\gamma_{s-l}e^{-(s-l)\rho\Delta t}u_{i,j}^l-b_{s-1}e^{-s\rho\Delta t}u_{i,j}^0\right].\) (7.7)

