**Proof:** The inequality (5.21) is proved in \[69\]. To prove the inequality (5.22), consider<tbc>

\(\phi_{j,k}=\langle\phi(x,y),Y_{j,k}(x,y)\rangle=\frac{2}{\chi_{j,k}}\int_0^1\int_0^1\phi(x,y)Y_{j,k}(x,y)dxdy.\)

<tbc>Using integration by parts w.r.t _x_ followed by _y_, we obtain<tbc>

\(|\phi_{j,k}|\le\frac{2}{\chi_{j,k}\sqrt{\nu_j^k}\mu_k}\int_0^1\int_0^1\phi_{xy}(x,y)Y_{j,k}(x,y)dydx.\)

<tbc>Similarly, by integrating by parts twice w.r.t _x_ and once w.r.t _y_, we find<tbc>

\(|\phi_{j,k}|\le\frac{2}{\chi_{j,k}\nu_j^k\mu_k^2}\int_0^1\int_0^1\phi_{xyxy}(x,y)Y_{j,k}(x,y)dydx.\)

<tbc>Using Cauchy-Schwarz inequality, we deduce

\(|\phi_{j,k}|\le\frac{1}{\nu_j^k\mu_k^2}\|\phi_{xyxy}\|_{C^4([0,1]\times[0,1])},\)

where \(\|Y_{j,k}(x,y)\|_{C^4([0,1]\times[0,1])}\le 1\).

## 5.3 First-ISP

The aim of this section is to recover a space-dependent source term, namely _F(x,y,t_)=_f(x,y_) and _u(x,y,t_), from the systems (5.5)-(5.8) and (5.13).

### 5.3.1 Series solution construction for first-ISP

The series solution for first-ISP in relation to the system defined by Eqs. (5.5)-(5.8) and (5.13) can be written as follows

\(u(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty U_{j,k}(t)X_{j,k}(x,y),\) (5.23)

and

\(f(x,y)=\sum_{j=1}^\infty\sum_{k=1}^\infty f_{j,k}X_{j,k}(x,y),\) (5.24)

where _U<sub>j,k</sub>(t_) and _f<sub>j,k</sub>_, for \(j,k=1,2,\cdots\) , are the unknowns, governed by the differential equation system

\(_G\mathcal{D}_t^{(\varrho)}U_{j,k}(t)=-\lambda_{j,k}U_{j,k}(t)+f_{j,k}.\) (5.25)

Taking into account the Laplace transform of (5.25) and using the initial condition in (5.8), we obtain

\(U_{j,k}(t)=\psi_{j,k}\mathbf{W}_{j,k}(t)+f_{j,k}\mathbf{Z}_{j,k}(t),\) (5.26)

