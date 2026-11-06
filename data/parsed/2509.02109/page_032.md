## Differentials of _F_**<sub>m</sub>**.

We now turn to _F_**<sub>m</sub>**:

\(F_\mathbf{m}:\left\{\begin{array}{ c c }
\Theta\times\mathcal{X} & \longrightarrow\mathbb{R}^{K\times d} \\
(\theta,X) & \longmapsto\left(\frac{\sum_{i=1}^n\gamma_{i,k}(\theta,X)x_i}{\sum_{j=1}^n\gamma_{j,k}(\theta,X)}\right)_{k=1}^K.
\end{array}\right.\) (46)

For convenience we introduce \(\Gamma_k:=\sum_{i=1}^n\gamma_{i,k}\). The chain rule gives

\(\frac{\partial F_\mathbf{m}}{\partial w}(\theta,X)\in\mathcal{L}\left(\triangle_K^0,\mathbb{R}^{K\times d}\right)\unknown\rightarrow\mathbb{R}^{K\times d\times K}:\) (47)

\(\left[\frac{\partial F_\mathbf{m}}{\partial w}(\theta,X)\right]_{k,\cdot,l}=\frac{1}{\Gamma_k}\left(\sum_{i=1}^n\left[\frac{\partial\gamma}{\partial w}\right]_{i,k,l}x_i-\frac{1}{\Gamma_k}\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial w}\right]_{j,k,l}\sum_{i=1}^n\gamma_{i,k}x_i\right).\) (48)

We continue with the differential with respect to **m**:

\(\frac{\partial F_\mathbf{m}}{\partial\mathbf{m}}(\theta,X)\in\mathcal{L}\left(\mathbb{R}^{K\times d},\mathbb{R}^{K\times d}\right)\simeq\mathbb{R}^{K\times d\times K\times d}:\) (49)

\(\left[\frac{\partial F_\mathbf{m}}{\partial\mathbf{m}}(\theta,X)\right]_{k,\cdot,l,\cdot}=\frac{1}{\Gamma_k}\left(\sum_{i=1}^nx_i\left[\frac{\partial\gamma}{\partial\mathbf{m}}\right]_{i,k,l,\cdot}^\top-\frac{1}{\Gamma_k}\left(\sum_{i=1}^n\gamma_{i,k}x_i\right)\sum_{j=1}^n\left[\frac{\partial\gamma}{\partial\mathbf{m}}\right]_{j,k,l,\cdot}^\top\right).\) (50)

For the differential with respect to \(\unknown\), we require the notion of _outer product_ between two tensors, which we define below:

\(\forall A\in\mathbb{R}^{n_1\times\cdots\times n_N},B\in\mathbb{R}^{m_1\times\cdots\times m_M},A\otimes B:=(A_{i_1,\cdots,i_N}B_{j_1,\cdots,j_M})\in\mathbb{R}^{n_1\times\cdots\times n_N\times m_1\times\cdots\times m_M}.\) (51)

Note that in Eq. (50), we could have written \(x_i\otimes\left[\frac{\partial\gamma}{\partial\mathbf{m}}\right]_{i,k,l,\cdot}\) . We will need the following differentiation rule for the outer product:

**Lemma A.1.** Let \(A:\mathbb{R}^{p_1\times\cdots\times p_P}\longrightarrow\mathbb{R}^{n_1\times\cdots\times n_N}\) and \(B:\mathbb{R}^{k_1\times\cdots\times k_P}\longrightarrow\mathbb{R}^{m_1\times\cdots\times m_M}\) be differentiable. Then the differential of \(C:=A\otimes B\) is:<tbc>

\(\frac{\partial C}{\partial X}(X)\in\mathcal{L}(\mathbb{R}^{p_1\times\cdots\times p_P},\mathbb{R}^{n_1\times\cdots\times n_N\times m_1\times\cdots\times m_M})\simeq\mathbb{R}^{n_1\times\cdots\times n_N\times m_1\times\cdots\times m_M\times p_1\times\cdots\times p_P}:\) (52)

\(\left[\frac{\partial C}{\partial X}(X)\right]_{i_1,\cdots,i_N,j_1,\cdots,j_M,k_1,\cdots,k_P}=\left[\frac{\partial A}{\partial X}(X)\right]_{i_1,\cdots,i_N,k_1,\cdots,k_P}B_{j_1,\cdots,j_M}(X)\)<br>
\(+A_{i_1,\cdots,i_N}\left[\frac{\partial B}{\partial X}(X)\right]_{j_1,\cdots,j_M,k_1,\cdots,k_P},\) (53)

\(\frac{\partial C}{\partial X}(X)=\tau\left(\frac{\partial A}{\partial X}(X)\otimes B(X)\right)+A(X)\otimes\frac{\partial B}{\partial X}(X),\) (54)

where \(\tau\) is the transposition \((\tau(T))_{i_1,\cdots,i_N,j_1,\cdots,j_M,k_1,\cdots,k_P}=T_{i_1,\cdots,i_N,k_1,\cdots,k_P,j_1,\cdots,j_M}\). If _B=A_, then the formula can be written as<tbc>

\(\frac{\partial C}{\partial X}(X)=\tau\left(A(X)\otimes\frac{\partial A}{\partial X}(X)\right)+A(X)\otimes\frac{\partial A}{\partial X}(X).\) (55)

Note that in particular, the intuitive formula \(\partial(A\otimes B)=(\partial A)\otimes B+A\otimes(\partial B)\) does not hold. We<tbc>

