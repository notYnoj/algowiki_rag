The additional condition in the first-ISP denotes the concentration of diffusive particles at time _T_ in a diffusion process and the final temperature distribution at time _T_ in heat conduction. The solution of first-ISP, expressed as {_u(x,y,t),f(x,y_)}, is termed regular if it satisfies the system (5.5)-(5.8) and the additional condition (5.13), with the requirements:

\(f(x,y)\in C([0,1]\times[0,1]);u(x,y,t)\in C(\overline{\Omega});\overline{\Omega}=[0,1]\times[0,1]\times[0,T];\)<br>
\(u_{xx}(\cdot,y,t)\in C^2([0,1]);u_{yy}(x,\cdot,t)\in C^2([0,1]);_G\mathcal{D}_t^{(\varrho)}u(x,y,\cdot)\in C([0,T]).\)

**In the second-ISP**, we consider the source term in the form _F(x,y,t_)=_w(t)f(x,y,t_), where _f(x,y,t_) is given. The objective of the second-ISP is to identify both _w(t_) and _u(x,y,t_) for the system defined by Eqs. (5.5)-(5.8). To ascertain _w(t_), we impose the following integral condition

\(\int_0^1\int_0^1u(x,y,t)dxdy=\mathcal{E}(t),t\in[0,T],\) (5.14)

where \(\mathcal{E}(t)\in AC([0,T])\) and AC denotes the space of absolutely continuous functions. The integral-type condition serves as essential information for recovering the source term. For instance, in diffusion processes, Eq. (5.5) describes the anomalous diffusion of particles in turbulent plasma, where E(_t_) represents the total concentration of particles. Similarly, in the case of heat conduction, E(_t_) corresponds to the total heat energy in a heated plate. The regular solution of second-ISP, represented as {_u(x,y,t),w(t_)}, meets the conditions:

\(u(x,y,t)\in C(\overline{\Omega});w(t)\in C([0,T]);u_{xx}(\cdot,y,t)\in C^2([0,1]);\)<br>
\(u_{yy}(x,\cdot,t)\in C^2([0,1]);_G\mathcal{D}_t^{(\varrho)}u(x,y,\cdot)\in C([0,T]).\)

## 5.2 Spectral problem

This section recalls the spectral analysis of the problem outlined in (5.5)-(5.8), as explored in \[71\]. Let us consider the spectral problem corresponding to (5.5)-(5.8)

\(\begin{array}{ c c c }
X_{xx}(x,y)+X_{yy}(x,y)+\lambda X(x,y)=0, &  \\
X(0,y)=X(1,y), & 
\end{array}\begin{array}{ c }
y\in[0,1] \\
X_x(1,y)-d\left(X_{xx}(1,y)+X_{yy}(1,y)\right)=0, & 
\end{array}\begin{array}{ c }
y\in[0,1],d>0, \\
X(x,0)=0, & 
\end{array}\right\}\) (5.15)

The eigenfunctions associated with this spectral problem are given by

\(X_{j,k}(x,y)=2sin\left(\sqrt{\nu_j^k}x\right)sin(\mu_ky),j=0,1,2,\dots,;k=1,2,\dots,\) (5.16)

with corresponding eigenvalues given by

\(\lambda_{j,k}=\nu_j^k+\mu_k^2,\)

where \(\mu_k=\frac{\pi}{2}(2k-1)\), and \(\nu_j^k\) denotes the roots of the characteristic equation

\(tan\left(\sqrt{s}\right)=\frac{\sqrt{s}}{d(s+\mu_k^2)},\) (5.17)

