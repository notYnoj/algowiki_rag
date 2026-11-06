## 3.2. Spatial Discretization

Suppose that a uniform spatial discretization with step size \(\Delta x=(\check{a}-\hat{a})/(N+1)\) is adopted, with \(N\in\mathbb{N}^+\). Under this discretization, we consider the following specific form of the operator \(\mathcal{L}=a(x)_aD_x^\alpha u(x,t)\), as introduced in \[31\]. The operator is approximated using the left sided Riemann-Liouville fractional derivative, discretized by means of the shifted Grünwald scheme, which leads to a nonsymmetric Toeplitz matrix having the following form<tbc>

\(\overline{G_{\alpha,N}}=\left[\begin{array}{ c c c c c }
g_1^{(\alpha)} & g_0^{(\alpha)} & 0 & \cdots & 0 \\
g_2^{(\alpha)} & g_1^{(\alpha)} & g_0^{(\alpha)} & \ddots & \vdots \\
\vdots & g_2^{(\alpha)} & g_1^{(\alpha)} & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & g_0^{(\alpha)} \\
g_N^{(\alpha)} & \cdots & \cdots & g_2^{(\alpha)} & g_1^{(\alpha)}
\end{array}\right]\in\mathbb{R}^{N\times N}.\)

<tbc>The spatially varying diffusion coefficient _a(x_) is incorporated through pointwise sampling D_<sub>N</sub>(a_)=diag(_a(x<sub>i</sub>_))<sub>_i_=1_,...,N_</sub> In terms of notations, notice that D_<sub>N</sub>(a_) coincides with _D<sub>N</sub>(a_) as in (4) with _d=r_=1, provided that the domain of _a_ is \[0,1\]. In general \([a_1,b_1]\neq[0,1]\) and hence \(\mathcal{D}_N(a)=D_N(\hat{a})\) with \(\hat{a}(\hat{x})=a(a_1+(b_1-a_1)\hat{x})\) and \(x=a_1+(b_1-a_1)\hat{x}\), \(\hat{x}\in[0,1]\). This rescaling is useful for applying the GLT axioms when deducing the Weyl distributions of the related matrix sequences. Consequently, the overall spatial discretization matrix can be written as

\(\frac{1}{(\Delta x)^\alpha}\mathcal{D}_N(a)\overline{G_{\alpha,N}},\) (6)

Since the construction of the discretizations and the analysis of the associated matrix properties have already been carried out in detail in \[31\], we omit further technical details here and directly employ the resulting matrix formulation in the subsequent analysis.

## 3.3. All At Once system

By combining the spatial discretizations matrix with the temporal discretization scheme given in (5), for _t=t<sub>m</sub>_ fixed and _x<sub>i</sub>_, _i_=1_,...,N_ we have

\(\frac{1}{\Gamma(2-\beta)(\Delta t)^\beta}\left[\ell_0^{(\beta)}\mathbf{u}_N^{(m)}+\sum_{j=1}^{m-1}\ell_j^{(\beta)}\mathbf{u}_N^{(m-j)}+\ell_m^{(\beta)}\psi_N\right]=\frac{1}{(\Delta x)^\alpha}\mathcal{D}_N(a)\overline{G_{\alpha,N}}\mathbf{u}_N^{(m)}+\mathbf{f}_N^{(m)}\)

where \(\mathbf{u}_N^{(m)}=[u_i^{(m)}]_{i=1,\dots,N}^T\) represents the numerical approximation of the solution _u(x,t<sub>m</sub>_) at the in terior grid points _x<sub>i</sub>_, _i_=1_,...,N_, and accordingly the vectors \(\mathbf{f}_N^{(m)}=[f(x_i,t_m)]_{i=1,\dots,N}^T\), and \(\psi_N=[\psi(x_i)]_{i=1,\dots,N}^T\).

The discretized form of problem (1) can be written as the following all at once linear system, compactly expressed using Kronecker products in the following form<tbc>

\(\mathcal{A}_{N,M}\mathbf{u}:=\left(B_M\otimes I_N-I_M\otimes\gamma\mathcal{D}_N(a)\overline{G_{\alpha,N}}\right)\mathbf{u}=\mathbf{f},\) (7)

<tbc>with \(\mathbf{u}=[\mathbf{u}_N^{(1)},\dots,\mathbf{u}_N^{(M)}]^T\) and where the lower triangular Toeplitz matrix \(B_M\in\mathbb{R}^{M\times M}\) denotes the<tbc>

