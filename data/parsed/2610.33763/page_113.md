with \(\gamma=\Delta t/(\Delta x)^\alpha\), D_<sub>N</sub>(a_)=diag(_a(x<sub>i</sub>_))<sub>_i_=1_,...,N_</sub> denoting the _N_-th diagonal sampling matrix and

\(\overline{G_{\alpha,N}}=\left[\begin{array}{ c c c c c }
g_1^{(\alpha)} & g_0^{(\alpha)} & 0 & \cdots & 0 \\
g_2^{(\alpha)} & g_1^{(\alpha)} & g_0^{(\alpha)} & \ddots & \vdots \\
\vdots & g_2^{(\alpha)} & g_1^{(\alpha)} & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & g_0^{(\alpha)} \\
g_N^{(\alpha)} & \ddots & \cdots & g_2^{(\alpha)} & g_1^{(\alpha)}
\end{array}\right]\in\mathbb{R}^{N\times N},\) (8.9)

denoting the Hessenberg Toeplitz matrix, that is

\((I_N-\theta G_{\alpha,N})u_N^{(m+1)}=(I_N+(1-\theta)G_{\alpha,N})u_N^{(m)}+\Delta tf_N^{(m,\theta)}.\) (8.10)

In terms of notations, notice that D_<sub>N</sub>(a_) coincides with _D<sub>N</sub>(a_) as in (4.1) with _d=r_=1 if the domain of definition of the function _a_ is \[0,1\]. In general \([L_1,R_1]\neq[0,1]\) and hence \(\mathcal{D}_N(a)=D_N(\hat{a})\) with \(\hat{a}(\hat{x})=a(L_1+(R_1-L_1)\hat{x})\) and \(x=L_1+(R_1-L_1)\hat{x}\), \(\hat{x}\in[0,1]\): this specification is useful for applying the GLT axioms when deducing the Weyl distributions of the related matrix sequences, as indicated in Remark 8.2. Equation (8.10) leads to the following all-at-once formulation linear system

\(\left[\begin{array}{ c c c c }
I_N-\theta G_{\alpha,N} &  &  &  \\
-(I_N+(1-\theta)G_{\alpha,N}) & I_N-\theta G_{\alpha,N} &  &  \\
 & \ddots & \ddots &  \\
 &  & -(I_N+(1-\theta)G_{\alpha,N}) & I_N-\theta G_{\alpha,N}
\end{array}\right]\left[\begin{array}{ c }
u_N^{(1)} \\
u_N^{(2)} \\
\vdots \\
u_N^{(M)}
\end{array}\right]\)<br>
\(=\left[\begin{array}{ c }
\Delta tf_N^{(1,\theta)}+(I_N+(1-\theta)G_{\alpha,N})u_N^{(0)} \\
\Delta tf_N^{(2,\theta)} \\
\vdots \\
\Delta tf_N^{(M,\theta)}
\end{array}\right].\) (8.11)

This system can be compactly expressed using Kronecker products in the following form

\(\bar{A}\bar{\mathbf{u}}=\bar{\mathbf{f}},\) (8.12)

where

\(\bar{A}=(I_M\otimes(I_N-\theta G_{\alpha,N})-Z_M\otimes(I_N+(1-\theta)G_{\alpha,N}))\in\mathbb{R}^{NM\times NM},\) (8.13)

\(Z_N=\left[\begin{array}{ c c c c }
0 &  &  &  \\
1 & 0 &  &  \\
 & \ddots & \ddots &  \\
 &  & 1 & 0
\end{array}\right]\in\mathbb{R}^{M\times M},\)

and \(\bar{\mathbf{u}},\bar{\mathbf{f}}\in\mathbb{R}^{NM\times 1}\). The coefficient matrix in (8.13) can therefore be expressed compactly using Kronecker products as

\(\bar{A}=H_{\theta,M}\otimes G_{\alpha,N}+H_M\otimes I_N.\)

