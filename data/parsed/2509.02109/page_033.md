<tbc>now compute the differential with respect to \(\unknown\):

\(\frac{\partial F_\mathbf{m}}{\partial\unknown}(\theta,X)\in\mathcal{L}\left((S_d(\mathbb{R}))^K,\mathbb{R}^{K\times d}\right)\unknown\rightarrow\mathbb{R}^{K\times d\times K\times d\times d}:\) (56)

\(\left[\frac{\partial F_\mathbf{m}}{\partial\unknown}(\theta,X)\right]_{k,\cdot,l,\cdot,\cdot}=\frac{1}{\Gamma_k}\left(\sum_{i=1}^nx_i\otimes\left[\frac{\partial\gamma}{\partial\unknown}\right]_{i,k,l,\cdot,\cdot}-\frac{1}{\Gamma_k}\left(\sum_{i=1}^n\gamma_{i,k}x_i\right)\otimes\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial\unknown}\right]_{j,k,l,\cdot,\cdot}\right).\) (57)

The differential with respect to _X_ is slightly different due to the product with _x<sub>i</sub>_ in Eq. (46):

\(\frac{\partial F_\mathbf{m}}{\partial X}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{n\times d},\mathbb{R}^{K\times d}\right)\simeq\mathbb{R}^{K\times d\times n\times d}:\) (58)

\(\left[\frac{\partial F_\mathbf{m}}{\partial X}(\theta,X)\right]_{k,\cdot,i,\cdot}=\frac{1}{\Gamma_k}\left(\gamma_{i,k}I_d+\sum_{h=1}^nx_h\left[\frac{\partial\gamma}{\partial X}\right]_{h,k,i,\cdot}^\top-\frac{1}{\Gamma_k}\left(\sum_{h=1}^n\gamma_{h,k}x_h\right)\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial X}\right]_{j,k,i,\cdot}^\top\right).\) (59)

## Differential of \(F_\unknown\).

We finish with the computation of the differentials of

\(F_\unknown:\left\{\begin{array}{ c c }
\Theta\times\mathcal{X} & \longrightarrow \\
(\theta,X) & \longmapsto
\end{array}\left(\frac{\sum_{i=1}^n\gamma_{i,k}(\theta,X)(x_i-F_\mathbf{m}(\theta,X)_k)(x_i-F_\mathbf{m}(\theta,X)_k)^\top}{\sum_{j=1}^n\gamma_{j,k}(\theta,X)}\right)_{k=1}^K.\) (60)

For convenience, let \(F_{m_k}:=[F_\mathbf{m}(\theta,X)]_{k,\cdot,\cdot}\). We first compute the differential with respect to _w_:

\(\frac{\partial F_\unknown}{\partial w}(\theta,X)\in\mathcal{L}\left(\triangle_K^0,(S_d(\mathbb{R}))^K\right)\unknown\rightarrow\mathbb{R}^{K\times d\times d\times K}:\) (61)

\(\left[\frac{\partial F_\unknown}{\partial w}(\theta,X)\right]_{k,\cdot,\cdot,l}=\frac{1}{\Gamma_k}\sum_{i=1}^n\left[\frac{\partial\gamma}{\partial w}\right]_{i,k,l}(x_i-F_{m_k})(x_i-F_{m_k})^\top\)<br>
\(-\frac{1}{\Gamma_k^2}\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial w}\right]_{j,k,l}\sum_{i=1}^n\gamma_{i,k}(x_i-F_{m_k})(x_i-F_{m_k})^\top\)<br>
\(-\frac{1}{\Gamma_k}\sum_{i=1}^n\gamma_{i,k}\left(\left[\frac{\partial F_\mathbf{m}}{\partial w}\right]_{k,\cdot,l}(x_i-F_{m_k})^\top+(x_i-F_{m_k})\left[\frac{\partial F_\mathbf{m}}{\partial w}\right]_{k,\cdot,l}^\top\right).\) (62)

For the differential with respect to **m**, we will use Lemma A.1:

\(\frac{\partial F_\unknown}{\partial\mathbf{m}}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{K\times d},(S_d(\mathbb{R}))^K\right)\unknown\rightarrow\mathbb{R}^{K\times d\times d\times K\times d}:\) (63)

\(\left[\frac{\partial F_\unknown}{\partial\mathbf{m}}(\theta,X)\right]_{k,\cdot,\cdot,l,\cdot}=\frac{1}{\Gamma_k}\sum_{i=1}^n(x_i-F_{m_k})(x_i-F_{m_k})^\top\otimes\left[\frac{\partial\gamma}{\partial\mathbf{m}}\right]_{i,k,l,\cdot}\)<br>
\(-\frac{1}{\Gamma_k^2}\left(\sum_{i=1}^n\gamma_{i,k}(x_i-F_{m_k})(x_i-F_{m_k})^\top\right)\otimes\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial\mathbf{m}}\right]_{j,k,l,\cdot}\)<br>
\(-\frac{1}{\Gamma_k}\sum_{i=1}^n\gamma_{i,k}\left\{\tau_{1,2}\left((x_i-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial\mathbf{m}}\right]_{k,\cdot,l,\cdot}\right)+(x_i-F_{m_k})\otimes\left[\frac{\partial F_\mathbf{m}}{\partial\mathbf{m}}\right]_{k,\cdot,l,\cdot}\right\}.\) (64)

