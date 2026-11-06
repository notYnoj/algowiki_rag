in which<tbc>

\(b_l=(l+1)^{1-\xi}-l^{1-\xi},l=0,1,\dots\)

<tbc>Denoting<tbc>

\(\alpha_m:=(\Delta t)^\xi\Gamma(2-\xi)=\left(\frac{T}{m}\right)^\xi\Gamma(2-\xi)\)

<tbc>and

\(\gamma_0:=b_0,\gamma_l:=b_l-b_{l-1}=(l+1)^{1-\xi}-2l^{1-\xi}+(l-1)^{1-\xi},l=1,\dots,m-1,\) (6.5)

and using \(t_j=j\Delta t\), the _L_1 approximation of the tempered fractional derivative is expressed as

\(^T\mathcal{D}_{L1}^{\xi,\rho} u(x,t_j)=\frac{1}{\alpha_m}\left[\gamma_0u(x,t_j)+\sum_{l=1}^{j-1}\gamma_{j-l}e^{-(j-l)\rho\Delta t}u(x,t_l)-b_{j-1}e^{-j\rho\Delta t}u(x,t_0)\right].\) (6.6)

The following error estimate holds, see \[140, page 10\]. Assuming that \(u(\cdot,t)\in C^2(0,T)\). For \(t_j\in(0,T)\), we have

\(\left|^T\mathcal{D}_t^{\xi,\rho} u(x,t)|_{t=t_j}-^T\mathcal{D}_{L1}^{\xi,\rho} u(x,t_j)\right|\le\chi_\xi\big[\rho^2max_{t_0\le t\le t_j}|u(x,t)|+2\rho max_{t_0\le t\le t_j}|u_t(x,t)|\)<br>
\(+\Delta t^{2-\xi} max_{t_0\le t\le t_j}|u_{tt}(x,t)|\big],\)

where _u<sub>t</sub>_ and _u<sub>tt</sub>_ denote the first and second partial derivative of _u_ with respect to _t_, and

\(\chi_\xi:=\frac{1}{2\Gamma(1-\xi)}\left[\frac{1}{4}+\frac{\xi}{(1-\xi)(2-\xi)}\right].\)

To discretize the CFD, we exploit the spatial counterpart of the _L_1 formula:

\(^C\mathcal{D}_{L1}^\eta u(x_i,t)=\frac{1}{\beta_n}\left[\delta_0u(x_i,t)+\sum_{k=1}^{i-1}\delta_{i-k}u(x_k,t)-d_{i-1}u(x_0,t)\right],\) (6.7)

where<tbc>

\(\beta_n:=(\Delta x)^\eta\Gamma(2-\eta)=\left(\frac{1}{n+1}\right)^\eta\Gamma(2-\eta)\)

<tbc>and

\(d_k:=(k+1)^{1-\eta}-k^{1-\eta},k=0,1,\dots\delta_0:=d_0,\delta_k:=d_k-d_{k-1}=(k+1)^{1-\eta}-2k^{1-\eta}+(k-1)^{1-\eta},k=1,\dots,n-1.\) (6.8)

The corresponding error estimate takes the form, see \[130, page 32\]. Assume that \(u(x,\cdot)\in C^2(0,1)\). For \(x_i\in(0,1)\), we have<tbc>

\(\left|^C\mathcal{D}_x^\eta u(x,t)|_{x=x_i}-^C\mathcal{D}_{L1}^\eta u(x_i,t)\right|\le\chi_\eta\Delta x^{2-\eta} max_{0\le x\le x_i}|u_{xx}(x,t)|,\)

