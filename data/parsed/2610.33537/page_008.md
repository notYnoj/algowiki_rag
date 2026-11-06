## 3.1. Linearized model and the fast iterative method

Following \[30\], the moment equations for the linearized one-dimensional BGK model take the form

\(\mathbf{A}\frac{du}{dx}=\frac{1}{\varepsilon}\mathbf{Lu},\mathbf{u}=(u_0,u_1,\dots,u_M)^\mathsf{T},\varepsilon=\text{Kn},\) (26)

where \(M\ge 3\) and

\(\mathbf{A}=\left(\begin{array}{ c c c c c c }
0 & 1 &  &  &  &  \\
1 & 0 & 2 &  &  &  \\
1 & \ddots & \ddots &  &  &  \\
 & \ddots & \ddots & M &  &  \\
 &  &  & 1 & 0
\end{array}\right),\mathbf{L}=\text{diag}(0,0,0,-1,\dots,-1).\) (27)

The first three rows of (26), describing the evolution of the primary macroscopic quantities, are

\(\frac{d}{dx}\left(\mathbf{A}_hU+\mathbf{b}u_3\right)=\mathbf{0},\) (28)

where

\(\mathbf{U}=\left(u_0,u_1,u_2\right)^\mathsf{T},\mathbf{A}_h=\left(\begin{array}{ c c c c }
0 & 1 & 0 \\
1 & 0 & 2 \\
0 & 1 & 0
\end{array}\right),\mathbf{b}=\left(\begin{array}{ c }
0 \\
0 \\
3
\end{array}\right).\) (29)

With first-order spatial discretization using the HLL flux, the moment system (26) becomes

\(\frac{\mathbf{A}}{2\Delta x}\left(\mathbf{u}_{j+1}-\mathbf{u}_{j-1}\right)-\frac{C_{M+1}}{2\Delta x}\left(\mathbf{u}_{j+1}-2\mathbf{u}_j+\mathbf{u}_{j-1}\right)=\frac{1}{\varepsilon}\mathbf{Lu}_j.\) (30)

The corresponding discretization of (28) is given by the first three rows of this system, with _u_<sub>3</sub> held fixed during the hydrodynamic stage.

We focus on the FIM method for (30), with SGS iterations applied to both the moment and hydrodynamic stages, and assume that the relaxation parameter \(\omega\) is independent of \(\varepsilon\). Define \(\nu=\omega C_{M+1}/\Delta x\) with \(0<\nu<1\), and let \(\mathbf{u}_j^{(n)}\) be the approximate solution in the _j_th grid cell after _n_ FIM iterations. The next FIM iteration is defined by the following steps:

1. Moment SGS: \(\gamma_1\) implicit-explicit SGS (IMEX-SGS) iterations in the moment stage, defined by<tbc>

• Initialize \(\mathbf{u}_j^{(n,0)}=\mathbf{u}_j^{(n)}\), then perform the following two sweeps for each \(s=0,1,\dots,\gamma_1-1\):<tbc>

• Forward sweep: in increasing order of _j_, solve for \(\mathbf{u}_j^{(n,s+1/2)}\) from<tbc>

\(\left(\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}\right)\mathbf{u}_j^{(n,s+1/2)}=(1-\nu)\mathbf{u}_j^{(n,s)}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{u}_{j-1}^{(n,s+1/2)}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{u}_{j+1}^{(n,s)};\) \(\text{(31)}\)

• Backward sweep: in decreasing order of _j_, solve for \(\mathbf{u}_j^{(n,s+1)}\) from<tbc>

\(\left(\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}\right)\mathbf{u}_j^{(n,s+1)}=(1-\nu)\mathbf{u}_j^{(n,s+1/2)}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{u}_{j-1}^{(n,s+1/2)}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{u}_{j+1}^{(n,s+1)}.\) \(\text{(32)}\)

2. Hydrodynamic SGS: \(\gamma_2\) Hydro-SGS iterations in the hydrodynamic stage, defined by<tbc>

• Set \(\mathbf{U}_j^{(n,0)}=(\mathbf{u}_{j,0}^{(n,\gamma_1)},\mathbf{u}_{j,1}^{(n,\gamma_1)},\mathbf{u}_{j,2}^{(n,\gamma_1)})^\mathsf{T}\), then perform the following two sweeps for each \(\ell=0,1,\dots,\gamma_2-1\):<tbc>

• Forward sweep: in increasing order of _j_, solve for \(\mathbf{U}_j^{(n,\ell+1/2)}\) from<tbc>

\(\mathbf{U}_j^{(n,\ell+1/2)}=(1-\nu)\mathbf{U}_j^{(n,\ell)}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{U}_{j-1}^{(n,\ell+1/2)}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{U}_{j+1}^{(n,\ell)}-\frac{\nu}{2C_{M+1}}\mathbf{b}\left(\mathbf{u}_{j+1,3}^{(n,\gamma_1)}-\mathbf{u}_{j-1,3}^{(n,\gamma_1)}\right);\) \(\text{(33)}\)

