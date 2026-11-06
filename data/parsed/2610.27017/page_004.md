where the coefficients \(g_k^{(\gamma)}\) are given by the following lemma:

**Lemma 2.1.** \[16\] For \(\gamma\in(1,2)\), the following recurrence relation holds:<tbc>

\(g_k^{(\gamma)}=\left(1-\frac{\gamma+1}{k}\right)g_{k-1}^{(\gamma)}=\frac{(-1)^k}{k!}\gamma(\gamma-1)\cdots(\gamma-k+1),k=1,2,\cdots.\)

<tbc>Moreover, we have<tbc>

\(g_0^{(\gamma)}=1,g_1^{(\gamma)}=-\gamma<0,1>g_2^{(\gamma)}>g_3^{(\gamma)}>\cdots>0,\)

<tbc>and<tbc>

\(\sum_{k=0}^\infty g_k^{(\gamma)}=0,\text{or equivalently,}\gamma=\sum_{k=0k\neq 1}^\infty g_k^{(\gamma)}.\)

<tbc>To facilitate the subsequent analysis, we introduce a matrix \(T_N^\gamma\in\mathbb{R}^{N\times N}\) associated with \(\gamma\):

\(T_N^\gamma=-\left[\begin{array}{ c c c c c c c }
2g_1^{(\gamma)} & g_0^{(\gamma)}+g_2^{(\gamma)} & g_3^{(\gamma)} & \cdots & g_{N-1}^{(\gamma)} & g_N^{(\gamma)} \\
g_0^{(\gamma)}+g_2^{(\gamma)} & 2g_1^{(\gamma)} & g_0^{(\gamma)}+g_2^{(\gamma)} & \ddots & \cdots & g_{N-1}^{(\gamma)} \\
g_3^{(\gamma)} & g_0^{(\gamma)}+g_2^{(\gamma)} & 2g_1^{(\gamma)} & \ddots & \ddots & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & g_3^{(\gamma)} \\
g_{N-1}^{(\gamma)} & \cdots & \ddots & \ddots & 2g_1^{(\gamma)} & g_0^{(\gamma)}+g_2^{(\gamma)} \\
g_N^{(\gamma)} & g_{N-1}^{(\gamma)} & \cdots & g_3^{(\gamma)} & g_0^{(\gamma)}+g_2^{(\gamma)} & 2g_1^{(\gamma)}
\end{array}\right].\) (2.1)

According to Lemma 2.1, \(T_N^\gamma\) is a matrix that is strictly diagonally dominant, symmetric, and has all positive diagonal entries. Therefore, \(T_N^\gamma\) is a symmetric positive definite matrix. Let

\(\mathbf{u}^{(m)}=[u_{1,1}^{(m)},u_{2,1}^{(m)},\dots,u_{N,1}^{(m)},u_{1,2}^{(m)},u_{2,2}^{(m)},\dots,u_{N,2}^{(m)},\dots,u_{1,N}^{(m)},u_{2,N}^{(m)},\dots,u_{N,N}^{(m)}]^T,\)<br>
\(\mathbf{f}^{(m)}=[f_{1,1}^{(m)},f_{2,1}^{(m)},\dots,f_{N,1}^{(m)},f_{1,2}^{(m)},f_{2,2}^{(m)},\dots,f_{N,2}^{(m)},\dots,f_{1,N}^{(m)},f_{2,N}^{(m)},\dots,f_{N,N}^{(m)}]^T,\)<br>
\(D^{(m)}=\text{diag}(d_{1,1}^{(m)},d_{2,1}^{(m)},\dots,d_{N,1}^{(m)},d_{1,2}^{(m)},d_{2,2}^{(m)},\dots,d_{N,2}^{(m)},\dots,d_{1,N}^{(m)},d_{2,N}^{(m)},\dots,d_{N,N}^{(m)}).\)

We discretize (1.1) in the spatial direction using the shifted Grunwald formula and in the temporal direction using the backward Euler scheme to obtain the implicit finite-difference scheme:

\(d_{i,j}^{(m)}\frac{u_{i,j}^{(m)}-u_{i,j}^{(m-1)}}{\Delta t}-\frac{\sigma_{\gamma_1}}{\Delta x^{\gamma_1}}\left(\sum_{k=0}^{i+1}g_k^{(\gamma_1)}u_{i-k+1,j}^{(m)}+\sum_{k=0}^{N-i+2}g_k^{(\gamma_1)}u_{i+k-1,j}^{(m)}\right)-\frac{\sigma_{\gamma_2}}{\Delta y^{\gamma_2}}\left(\sum_{k=0}^{j+1}g_k^{(\gamma_2)}u_{i,j-k+1}^{(m)}+\sum_{k=0}^{N-j+2}g_k^{(\gamma_2)}u_{i,j+k-1}^{(m)}\right)=f_{i,j}^{(m)}.\)

Furthermore, we have<tbc>

\(D^{(m)}\frac{\mathbf{u}^{(m)}-\mathbf{u}^{(m-1)}}{\Delta t}+\left(\frac{\sigma_{\gamma_1}}{\Delta x^{\gamma_1}}I_N\otimes T_{\gamma_1}+\frac{\sigma_{\gamma_2}}{\Delta y^{\gamma_2}}T_{\gamma_2}\otimes I_N\right)\mathbf{u}^{(m)}=\mathbf{f}^{(m)}.\)

<tbc>Let \(\eta_1=\sigma_{\gamma_1}\frac{\Delta t}{\Delta x^{\gamma_1}},\eta_2=\sigma_{\gamma_2}\frac{\Delta t}{\Delta y^{\gamma_2}}\) . Consequently, we obtain

\(\left(D^{(m)}+\eta_1I_N\otimes T_N^{\gamma_1}+\eta_2T_N^{\gamma_2}\otimes I_N\right)\mathbf{u}^{(m)}=\Delta t\mathbf{f}^{(m)}+D^{(m)}\mathbf{u}^{(m-1)}.\) (2.2)

