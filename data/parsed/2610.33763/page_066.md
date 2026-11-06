Since <sub>(1)</sub>_u(x_<sub>0</sub>_,y_<sub>0</sub>_,t_)=<sub>(2)</sub>_u(x_<sub>0</sub>_,y_<sub>0</sub>_,t_) for some \(x_0,y_0\in(0,1)\times(0,1)\), it follows that<tbc>

\(_{(1)}U_{j,k}(t)=_{(2)}U_{j,k}(t),\)

<tbc>and therefore<tbc>

\(_{(1)}f_{j,k}\mathbf{Z}_{j,k}(t)=_{(2)}f_{j,k}\mathbf{Z}_{j,k}(t),\Rightarrow(_{(1)}f_{j,k}-_{(2)}f_{j,k})\mathbf{Z}_{j,k}(t)=0.\)

<tbc>Applying the Laplace transform, we get

\(\frac{_{(1)}f_{j,k}-_{(2)}f_{j,k}}{s(s\widehat{\varrho}(s)+\lambda_{j,k})}=0,Res>0,\Rightarrow\frac{_{(1)}f_{j,k}-_{(2)}f_{j,k}}{\Delta+\lambda_{j,k}}=0,\) (5.51)

where \(\Delta=s\widehat{\varrho}(s)\).

By selecting the disk for _j_=1_,k_=1 such that \(\lambda_{1,1}\) lies within it, and applying the Cauchy Integral Theorem to Eq. (5.51), we obtain<tbc>

\(_{(1)}f_{1,1}=_{(2)}f_{1,1}.\)

<tbc>Similarly, by considering different disks for \(j,k=2,3,\cdots\) , we find that<tbc>

\(_{(1)}f_{j,k}=_{(2)}f_{j,k}.\)

<tbc>Therefore, we conclude that

\(_{(1)}f(x,y)=_{(2)}f(x,y).\)

## 5.4 Second-ISP

This section examines the second-ISP for the system described by Eqs. (5.5)-(5.8) and (5.14), incorporating the source term _F(x,y,t_)=_w(t)f(x,y,t_). We will discuss how to recover _w(t_) along with _u(x,y,t_), given the additional condition specified by (5.14).

### 5.4.1 Series solution construction for second-ISP

The solution to second-ISP for the system given by Eqs. (5.5)-(5.8) and (5.14) can be expressed as

\(u(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty U_{j,k}(t)X_{j,k}(x,y),\) (5.52)

Here, _U<sub>j,k</sub>(t_) for \(j,k\in\mathbf{N}\) are unknown that satisfy the following differential equation

\(_G\mathcal{D}_t^{(\varrho)}U_{j,k}(t)=-\lambda_{j,k}U_{j,k}(t)+w(t)f_{j,k}(t),\) (5.53)

Taking the Laplace transform of Eq. (5.53) and Applying the initial condition provided in (5.8), we derive<tbc>

\(U_{j,k}(t)=\psi_{j,k}\mathbf{W}_{j,k}(t)+w(t)f_{j,k}(t)*\mathbf{V}_{j,k}(t).\) (5.54)

