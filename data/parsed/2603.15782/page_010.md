**Theorem 8.** _Set_ \(\eta=\frac{\delta}{2R\rho^2}\) _and_ \(T=\lceil\frac{4R^2\rho^2lnn_\mathrm{max}}{\delta^2}\rceil\) _where_ \(n_\mathrm{max}=\mathrm{max}_{k\in\mathcal{K}}n_k\)_. Suppose that the algorithm does not fail during the first T iterations, and the spectral norms are bounded as_ \(\|N_k^{(t)}\|\le\rho\) _for all_ \(k\in\mathcal{K}\) _and_ \(t\in[T]\)_. Then optimal values of problems_ (3), (4) _are at least_ \(\alpha-\delta\cdot|\mathcal{K}|\).

Note that the standard MMWU framework is obtained by setting K=\[_K_\]={1}. In this case Theorem 8 reduces to (a special case of <sup>2</sup>) Theorem 4.6 in \[3\].

_Proof._ Since the constraints (3b), (3c) imply constraint \(-\mathtt{Tr}(X_k)\ge-R\), there exist coefficients \(\gamma_{ik}\) with \(\gamma_{ik}\ge 0\) for \(i\in\mathcal{I}\) such that for each \(k\in\mathcal{K}\) we have \(\sum_i\gamma_{ik}A_{ik}=-I\) and \(\sum_i\gamma_{ik}b_i\ge-R\). Define \(\bar{y}=\frac{1}{T}\sum_{t=1}^Ty^{(t)}\), and let _y_ be the vector with \(y_i=\bar{y}_i+\sum_{k\in\mathcal{K}}\gamma_{ik}\frac{\delta}{R}\) for each _i_. Clearly, we have \(y\in\mathbb{R}_{\ge 0}^{\mathcal{I}}\times\mathbb{R}^{\mathcal{T}^\prime}\).

Note that \(b^\top\bar{y}=\frac{1}{T}\sum_{t=1}^Tb^\top y^{(t)}\ge\alpha\). We can also write

\(b^\top y=b^\top\bar{y}+\sum_{k\in\mathcal{K}}\sum_ib_i\gamma_{ik}\frac{\delta}{R}\ge b^\top\bar{y}-\sum_{k\in\mathcal{K}}R\frac{\delta}{R}\ge\alpha-\delta\cdot|\mathcal{K}|\)

To prove the claim, it thus now suffices to show that vector _y_ is a feasible solution of the dual problem (4), i.e. that \(S_k(y)\unknown 0\) for each \(k\in[K]\).

Using the assumption before Algorithm 2, we obtain

\(S_k(y)=S_k(\bar{y})-\sum_i\gamma_{ik}\frac{\delta}{R}A_{ik}=S_k(\bar{y})+\frac{\delta}{R}I\forall k\in\mathcal{K}\)<br>
\(S_k(y)=S_k(\bar{y})\forall k\in[K]-\mathcal{K}\)

First, let us consider \(k\in\mathcal{K}\). Let us apply the standard MMWU regret bound \[3, Corollary 3.2\] with matrices \(P^{(t)}=\frac{1}{R}X_k^{(t)}\) and \(M^{(t)}=-\frac{1}{\rho}N_k^{(t)}\). We obtain

\(\sum_{t=1}^TM^{(t)}\bullet P^{(t)}\le\lambda_n\left(\sum_{t=1}^TM^{(t)}\right)+\eta\rho\cdot T+\frac{\mathrm{ln}n}{\eta\rho}\)

where _n=n<sub>k</sub>_ and \(\lambda_1(A)\ge\cdots\ge\lambda_n(A)\) denote eigenvalues of symmetric matrix _A_. Equivalently,

\(\frac{1}{\rho}\lambda_n\left(-\sum_{t=1}^TN_k^{(t)}\right)\ge\underbrace{-\frac{1}{R\rho}\sum_{t=1}^TN_k^{(t)}\bullet X_k^{(t)}}_{\ge 0}-\eta\rho T-\frac{\mathrm{ln}n}{\eta\rho}\)

By noting that \(-\sum_{t=1}^TN_k^{(t)}=TS_k(\bar{y})\) we obtain

\(\lambda_n(S_k(y))=\frac{1}{T}\lambda_n\left(TS_k(\bar{y})\right)+\frac{\delta}{R}\ge\frac{1}{T}\left(-\eta\rho^2T-\frac{\mathrm{ln}n}{\eta}\right)+\frac{\delta}{R}=\frac{\delta}{R}-\eta\rho^2-\frac{\mathrm{ln}n}{\eta T}\)

Using definitions of \(\eta\) and _T_, we conclude that the last expression is nonnegative, and hence \(S_k(y)\unknown 0\).

Now consider \(k\in[K]-\mathcal{K}\). We have \(S_k(y^{(t)})\unknown 0\) for each _t_ and hence \(S_k(y)=S_k(\bar{y})\unknown 0\).

<sup>2</sup>\[3, Theorem 4.6\] allows the oracle to set \(N_k^{(t)}=\sum_iy_iA_{ik}-F_k^{(t)}\) for some matrix \(F^{(t)}\unknown C_k\), instead of \(N_k^{(t)}=\sum_iy_iA_{ik}-C_k\). The same could be done in our case, but since our algorithm does not need this extra flexibility, for simplicity we state the theorem without this generalization.

