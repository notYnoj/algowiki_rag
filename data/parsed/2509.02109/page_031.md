<tbc>Similarly, using Eq. (27), we compute the differential of \(\gamma\) w.r.t. \(\unknown=(\Sigma_k)\):

\(\frac{\partial\gamma}{\partial\unknown}(\theta,X)\in\mathcal{L}\left((S_d(\mathbb{R}))^K,\mathbb{R}^{n\times K}\right)\unknown\rightarrow\mathbb{R}^{n\times K\times K\times d\times d}:\) (34)

\(\left[\frac{\partial\gamma}{\partial\unknown}(\theta,X)\right]_{i,k,l,\cdot,\cdot}=\frac{w_kg_{i,k}}{2Z_i}\left(\delta_{k,l}-\frac{w_lg_{i,l}}{Z_i}\right)\left(-\Sigma_l^{-1}+\Sigma_l^{-1}(x_i-m_l)(x_i-m_l)^\top\Sigma_l^{-1}\right).\) (35)

Finally, Eq. (28) allows the computation of the differential of \(\gamma\) w.r.t._X_:

\(\frac{\partial\gamma}{\partial X}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{n\times d},\mathbb{R}^{n\times K}\right)\simeq\mathbb{R}^{n\times K\times n\times d}:\) (36)

\(\left[\frac{\partial\gamma}{\partial X}(\theta,X)\right]_{i,k,j,\cdot}=\frac{\delta_{i,j}w_kg_{i,k}}{Z_i}\left(-\Sigma_k^{-1}(x_i-m_k)+\frac{1}{Z_i}\sum_{l=1}^Kw_lg_{i,l}\Sigma_l^{-1}(x_i-m_l)\right).\) (37)

## A.6.3 Differential of _F_

We introduce the coordinate notation<tbc>

\(F(\theta,X)=(F_w(\theta,X),F_\mathbf{m}(\theta,X),F_\unknown(\theta,X))\in\triangle_K\times(\mathbb{R}^d)^K\times(S_d^{++}(\mathbb{R}))^K,\)

<tbc>hence the differentials of _F_ with respect to \(\theta\) and _X_ can be written "block-wise" as follows:<tbc>

\(\frac{\partial F}{\partial\theta}=\left(\begin{array}{ c c c }
\frac{\partial F_w}{\partial w} & \frac{\partial F_w}{\partial\mathbf{m}} & \frac{\partial F_w}{\partial\unknown} \\
\frac{\partial F_\mathbf{m}}{\partial w} & \frac{\partial F_\mathbf{m}}{\partial\mathbf{m}} & \frac{\partial F_\mathbf{m}}{\partial\unknown} \\
\frac{\partial F_\unknown}{\partial w} & \frac{\partial F_\unknown}{\partial\mathbf{m}} & \frac{\partial F_\unknown}{\partial\unknown}
\end{array}\right),\frac{\partial F}{\partial X}=\left(\begin{array}{ c }
\frac{\partial F_w}{\partial X} \\
\frac{\partial F_\mathbf{m}}{\partial X} \\
\frac{\partial F_\unknown}{\partial X}
\end{array}\right).\)

<tbc>**Differentials of** _F<sub>w</sub>_**.** We now compute the differentials of _F<sub>w</sub>_ whose expression we remind from Eq. (4):<tbc>

\(F_w:\left\{\begin{array}{ c c c }
\Theta\times\mathcal{X} & \longrightarrow & \triangle_K \\
(\theta,X) & \longmapsto & \left(\frac{1}{n}\sum_{i=1}^n\gamma_{i,k}(\theta,X)\right)_{k=1}^K.
\end{array}\right.\) (38)

<tbc>By Eq. (31), we have<tbc>

\(\frac{\partial F_w}{\partial w}(\theta,X)\in\mathcal{L}\left(\triangle_K^0,\triangle_K^0\right)\unknown\rightarrow\mathbb{R}^{K\times K}:\left[\frac{\partial F_w}{\partial w}(\theta,X)\right]_{k,l}=\frac{1}{n}\sum_{i=1}^n\frac{g_{i,k}}{Z_i}\left(\delta_{k,l}-\frac{w_kg_{i,l}}{Z_i}\right).\) (39)

<tbc>Likewise, Eq. (33) yields<tbc>

\(\frac{\partial F_w}{\partial\mathbf{m}}(\theta,X)\in\mathcal{L}\left((\mathbb{R}^d)^K,\triangle_K^0\right)\unknown\rightarrow\mathbb{R}^{K\times K\times d}:\) (40)

\(\left[\frac{\partial F_w}{\partial\mathbf{m}}(\theta,X)\right]_{k,l,\cdot}=\frac{1}{n}\sum_{i=1}^n\frac{w_kg_{i,k}}{Z_i}\left(\delta_{k,l}-\frac{w_lg_{i,l}}{Z_i}\right)\Sigma_l^{-1}(x_i-m_l).\) (41)

<tbc>Eq. (35) gives<tbc>

\(\frac{\partial F_w}{\partial\unknown}(\theta,X)\in\mathcal{L}\left((S_d(\mathbb{R}))^K,\triangle_K^0\right)\unknown\rightarrow\mathbb{R}^{K\times K\times d\times d}:\) (42)

\(\left[\frac{\partial F_w}{\partial\unknown}(\theta,X)\right]_{k,l,\cdot,\cdot}=\frac{1}{n}\sum_{i=1}^n\frac{w_kg_{i,k}}{2Z_i}\left(\delta_{k,l}-\frac{w_lg_{i,l}}{Z_i}\right)\left(-\Sigma_l^{-1}+\Sigma_l^{-1}(x_i-m_l)(x_i-m_l)^\top\Sigma_l^{-1}\right).\) (43)

<tbc>Finally, with Eq. (37), we obtain

\(\frac{\partial F_w}{\partial X}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{n\times d},\triangle_K^0\right)\unknown\rightarrow\mathbb{R}^{K\times n\times d}:\) (44)

\(\left[\frac{\partial F_w}{\partial X}(\theta,X)\right]_{k,i,\cdot}=\frac{w_kg_{i,k}}{nZ_i}\left(-\Sigma_k^{-1}(x_i-m_k)+\frac{1}{Z_i}\sum_{l=1}^Kw_lg_{i,l}\Sigma_l^{-1}(x_i-m_l)\right).\) (45)

