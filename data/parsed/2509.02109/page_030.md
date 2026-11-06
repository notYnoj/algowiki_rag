## A.6 Explicit Differential Expressions

### A.6.1 Differential of Gaussian Density

First, we compute the explicit differential of

\(g:\left\{\begin{array}{ c c }
\mathbb{R}^d\times S_d^{++}(\mathbb{R})\times\mathcal{X} & \longrightarrow \\
(m,\Sigma,X) & \longmapsto\left(\frac{1}{(2\pi)^{d/2}\mathrm{det}(\Sigma)^{1/2}}\mathrm{exp}\left(-\frac{1}{2}(x_i-m)^\top\Sigma^{-1}(x_i-m)\right)\right)_{i=1}^n,
\end{array}\right.\) (24)

where we wrote \(X=(x_1,\cdots,x_n)\). We first compute the differential with respect to _m_:

\(\frac{\partial g}{\partial m}(m,\Sigma,X)\in\mathcal{L}(\mathbb{R}^d,\mathbb{R}^n)\simeq\mathbb{R}^{n\times d}:\left[\frac{\partial g}{\partial m}(m,\Sigma,X)\right]_{i,\cdot}=\Sigma^{-1}(x_i-m)g_{m,\Sigma}(x_i).\) (25)

For the differential with respect to \(\Sigma\), we remark that \(T_\Sigma S_d^{++}(\mathbb{R})=S_d(\mathbb{R})\), and use \[PP08, Equation 49\] stating that \(\partial_A\mathrm{det}A=(\mathrm{det}A)A^{-\top}\) and \[PP08, Equation 61\] which states \(\partial_Aa^\top A^{-1}b=-A^{-\top} ab^\top A^{-\top}\), which yields:

\(\frac{\partial g}{\partial\Sigma}(m,\Sigma,X)\in\mathcal{L}(S_d(\mathbb{R}),\mathbb{R}^n)\unknown\rightarrow\mathbb{R}^{n\times d\times d}:\) (26)

\(\left[\frac{\partial g}{\partial\Sigma}(m,\Sigma,X)\right]_{i,\cdot,\cdot}=\frac{g_{m,\Sigma}(x_i)}{2}\left(-\Sigma^{-1}+\Sigma^{-1}(x_i-m)(x_i-m)^\top\Sigma^{-1}\right).\) (27)

Finally, the differential with respect to the data _X_ reads

\(\frac{\partial g}{\partial X}(m,\Sigma,X)\in\mathcal{L}(\mathbb{R}^{n\times d},\mathbb{R}^n)\simeq\mathbb{R}^{n\times n\times d}:\left[\frac{\partial g}{\partial\Sigma}(m,\Sigma,X)\right]_{i,j,\cdot}=-\delta_{i,j}g_{m,\Sigma}(x_i)\Sigma^{-1}(x_i-m).\) (28)

### A.6.2 Differential of \(\gamma\)

We now compute the differential of the function

\(\gamma:\left\{\begin{array}{ c c }
\underbrace{\triangle_K\times(\mathbb{R}^d)^K\times(S_d^{++}(\mathbb{R}))^K}_\Theta & \longrightarrow \\
(\underbrace{w,(m_k),(\Sigma_k)}_\theta & \longmapsto\left(\frac{w_kg_{m_k,\Sigma_k}(x_i)}{\sum_lw_lg_{m_l,\Sigma_l}(x_i)}\right)_{i,k}
\end{array}\right..\) (29)

For notational convenience, we introduce

\(\forall(i,k)\in\unknown 1,n\unknown\times\unknown 1,K\unknown,g_{i,k}:=g_{m_k,\Sigma_k}(x_i),Z_i:=\sum_{k^\prime} w_{k^\prime} g_{i,k^\prime}.\) (30)

First, the tangent space of the simplex is the same everywhere: \(T_w\triangle_K=\triangle_K^0:=(\unknown_K)^\perp\), and the differential with respect to _w_ is

\(\frac{\partial\gamma}{\partial w}(\theta,X)\in\mathcal{L}\left(\triangle_K^0,\mathbb{R}^{n\times K}\right)\unknown\rightarrow\mathbb{R}^{n\times K\times K}:\left[\frac{\partial\gamma}{\partial w}(\theta,X)\right]_{i,k,l}=\frac{g_{i,k}}{Z_i}\left(\delta_{k,l}-\frac{w_kg_{i,l}}{Z_i}\right).\) (31)

Using Eq. (25), we compute the differential of \(\gamma\) w.r.t. **m**=(_m<sub>k</sub>_):

\(\frac{\partial\gamma}{\partial\mathbf{m}}(\theta,X)\in\mathcal{L}\left((\mathbb{R}^d)^K,\mathbb{R}^{n\times K}\right)\simeq\mathbb{R}^{n\times K\times K\times d}:\) (32)

\(\left[\frac{\partial\gamma}{\partial\mathbf{m}}(\theta,X)\right]_{i,k,l,\cdot}=\frac{w_kg_{i,k}}{Z_i}\left(\delta_{k,l}-\frac{w_lg_{i,l}}{Z_i}\right)\Sigma_l^{-1}(x_i-m_l).\) (33)

