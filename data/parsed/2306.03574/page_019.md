<tbc>For the wave equation with variable diffusion coefficients given below in (3.1), we adopt the same discretization scheme as the one used in Section 1.

\(\left\{\begin{array}{ c c }
u_{tt}(x,t)=\nabla(a(x)\nabla u(x,t))+f(x,t), & (x,t)\in\Omega\times(0,T], \\
u=0, & (x,t)\in\partial\Omega\times(0,T], \\
u(x,0)=\psi_0,u_t(x,0)=\psi_1, & x\in\Omega\subset\mathbb{R}^d.
\end{array}\right.\) (3.1)

where _a(x_) is a known positive function. Similar to (1.2), the following time-space linear system is obtained from (3.1):

\(\left[\begin{array}{ c c c c c }
L_a &  &  &  &  \\
-2I_m & L_a &  &  &  \\
L_a & -2I_m & L_a &  &  \\
 & \ddots & \ddots & \ddots &  \\
 &  &  & L_a & -2I_m & L_a
\end{array}\right]\left[\begin{array}{ c }
\mathbf{u}^{(1)} \\
\mathbf{u}^{(2)} \\
\mathbf{u}^{(3)} \\
\vdots \\
\mathbf{u}^{(n)}
\end{array}\right]=\tau^2\left[\begin{array}{ c }
\mathbf{f}^{(0)}/2+\Psi_1/\tau+\Psi_0/\tau^2 \\
\mathbf{f}^{(1)}-L\Psi_0/\tau^2 \\
\mathbf{f}^{(2)} \\
\vdots \\
\mathbf{f}^{(n-1)}
\end{array}\right],\) (3.2)

where \(L_a=I_m-\frac{\tau^2}{2}\Delta_{a,h}\in\mathbb{R}^{m\times m}\) and \(\Delta_{a,h}\) is the central difference discretization of \(\nabla a(x)\nabla\). Clearly, the proposed preconditioner for the linear system (3.2) is not fast invertible since the spatial matrix cannot be diagonalized by the fast sine transform. To remedy this situation, we consider replacing the diffusion coefficient function _a_ with \(\bar{a}\) (i.e., the mean value of _a_ on the<tbc>

\begin{tabular}{cccccc}
\multirow{2}{*}{\(\tau\)} & \multirow{2}{*}{_h_} & \multirow{2}{*}{DoF} & \multicolumn{3}{c}{E\(_{\tau,h}\)} \\
 & & & MINRES-\(\mathcal{P}_\alpha\) & MINRES-P<sub>1</sub> & MINRES-_I<sub>mn</sub>_ \\
\multirow{4}{*}{2<sup>-4</sup>} & 2<sup>-4</sup> & 3600 & 3.04e-4 & 3.04e-4 & 3.04e-4 \\
 & 2<sup>-5</sup> & 15376 & 3.04e-4 & 3.05e-4 & 3.05e-4 \\
 & 2<sup>-6</sup> & 63504 & 3.05e-4 & 3.05e-4 & 3.05e-4 \\
 & 2<sup>-7</sup> & 258064 & 3.05e-4 & 3.05e-4 & 3.05e-4 \\
\multirow{4}{*}{2<sup>-5</sup>} & 2<sup>-4</sup> & 7200 & 7.67e-5 & 7.70e-5 & 7.70e-5 \\
 & 2<sup>-5</sup> & 30752 & 7.68e-5 & 7.71e-5 & 7.71e-5 \\
 & 2<sup>-6</sup> & 127008 & 7.69e-5 & 7.71e-5 & 7.71e-5 \\
 & 2<sup>-7</sup> & 516128 & 7.69e-5 & 7.71e-5 & 7.71e-5 \\
\multirow{4}{*}{2<sup>-6</sup>} & 2<sup>-4</sup> & 14400 & 1.87e-5 & 1.93e-5 & 1.93e-5 \\
 & 2<sup>-5</sup> & 61504 & 1.88e-5 & 1.93e-5 & 1.93e-5 \\
 & 2<sup>-6</sup> & 254016 & 1.88e-5 & 1.93e-5 & 1.93e-5 \\
 & 2<sup>-7</sup> & 1032256 & 1.88e-5 & 1.93e-5 & 1.93e-5 \\
\multirow{4}{*}{2<sup>-7</sup>} & 2<sup>-4</sup> & 28800 & 3.62e-6 & 4.83e-6 & 4.89e-6 \\
 & 2<sup>-5</sup> & 123008 & 3.62e-6 & 4.84e-6 & 4.99e-6 \\
 & 2<sup>-6</sup> & 508032 & 3.63e-6 & 4.84e-6 & 5.03e-6 \\
 & 2<sup>-7</sup> & 2064512 & 3.63e-6 & 4.84e-6 & 5.06e-6 \\
\end{tabular}

2: Errors of MINRES-\(\mathcal{P}_\alpha\), MINRES-P<sub>1</sub>, and MINRES-_I<sub>mn</sub>_ for Example 1.

