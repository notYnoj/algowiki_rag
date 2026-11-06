spatial grid points arranged in the lexicographic ordering.

Instead of solving the above equations for \(\mathbf{u}_m^{(k)}\) sequentially for _k_=1,2_,...,n_-1, we consider the following equivalent all-at-once system _mn_-by-_mn_ (real) nonsymmetric block Toeplitz system

\(\underbrace{\left[\begin{array}{ c c c c c }
L &  &  &  &  \\
-2I_m & L &  &  &  \\
L & -2I_m & L &  &  \\
 & \ddots & \ddots & \ddots &  \\
 &  &  & L & -2I_m & L
\end{array}\right]}_{=:\mathcal{T}}\underbrace{\left[\begin{array}{ c }
\mathbf{u}_m^{(1)} \\
\mathbf{u}_m^{(2)} \\
\mathbf{u}_m^{(3)} \\
\vdots \\
\mathbf{u}_m^{(n)} \\
\vdots \\
\mathbf{f}_m^{(n-1)}
\end{array}\right]}_{=:\mathbf{u}}=\tau^2\underbrace{\left[\begin{array}{ c }
\mathbf{f}_m^{(0)}/2+\Psi_1/\tau+\Psi_0/\tau^2 \\
\mathbf{f}_m^{(1)}-L\Psi_0/\tau^2 \\
\mathbf{f}_m^{(2)} \\
\vdots \\
\mathbf{f}_m^{(n-1)}
\end{array}\right]}_{=:\mathbf{f}},\) (1.2)

where \(L=I_m-\frac{\tau^2}{2}\Delta_h\in\mathbb{R}^{m\times m}\). Note that _I<sub>m</sub>_ denotes the \(m\times m\) identity matrix.

Throughout, the discrete negative Laplacian matrix \(-\Delta_h\) is assumed HPD and hence _L_ is HPD as well. Such an assumption is easily satisfied when a finite difference method is used on a uniform grid. In a more general case where the spatial domain is irregular and a finite element method is used \[8\], the identity matrix _I<sub>m</sub>_ and \(-\Delta_h\) are replaced by the mass matrix and stiffness matrix, respectively.

We remark that for solving the wave equation (1.1) one can apply other discretization schemes and thus obtain different linear systems other than (1.2). For example, \[7, 20, 23\] concern various time stepping methods while \[41\] adopts the Numerov method.

Thanks to the symmetrization technique proposed in \[36\], we consider to rewrite (1.2) as the following equivalent symmetric form<tbc>

\(\mathcal{YT}\mathbf{u}=\mathcal{Y}\mathbf{f},\) (1.3)

<tbc>where

\(\mathcal{YT}=\left[\begin{array}{ c c c c c }
 &  & L & -2I_m & L \\
 & \ddots & \ddots & \ddots &  \\
L & -2I_m & L &  &  \\
-2I_m & L &  &  &  \\
L &  &  &  &  \\
\end{array}\right],\) (1.4)

and \(\mathcal{Y}=Y_n\otimes I_m\) with \(Y_n\in\mathbb{R}^{n\times n}\) being the anti-identity matrix, i.e., \[_Y<sub>n</sub>_\]_<sub>j,k</sub>_=1 if and only if _j+k=n_+1 and \[_Y<sub>n</sub>_\]_<sub>j,k</sub>_=0 elsewhere. Clearly, the monolithic matrixYT is symmetric since _L_ is assumed symmetric.

For the symmetrized matrix VT given in (1.4), we know from \[11, Theorem 3.4\] and previous<tbc>

