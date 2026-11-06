**Corollary 3.2.** Under the conditions of Corollary 3.1, there exists a constant \(\beta\) independent of the time _m_ such that the prolongation operator defined by (3.2) satisfies (3.8).

_Proof._ By Theorem 3.2, there exists a positive constant \(\beta_0\), such that<tbc>

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,A_N}^2\le\beta_0\|e^h\|_{1,A_N}^2,\forall e^h\in\mathbb{R}^n.\)

<tbc>By the uniform boundedness of _d(x,y,t_), there exists a positive constant \(\hat{d}\) such that<tbc>

\(d(x,y,t)\le\hat{d}\text{for all}(x,y,t)\in\Omega\times(0,T).\)

<tbc>It follows from Lemma 3.5 that

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,A_N^{(m)}}^2\le\beta_0\left(1+\frac{\hat{d}}{\eta_1a_0}\right)\|e^h\|_{1,A_N^{(m)}}^2,\forall e^h\in\mathbb{R}^n.\)

Let \(\beta=\beta_0\left(1+\frac{\hat{d}}{\eta_1a_0}\right)\). Then \(\beta\) does not depend on the time instant _m_.

The proof is completed.

**Theorem 3.3.** Let \(A_N^{(m)}\) be given by (2.4). If the coefficient function _d(x,y,t_) is nonnegative and uniformly bounded, _G_ is the weighted Jacobi method with \(\omega\in(0,\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty})\), and \(I_H^h\) is as in (3.2), then the TGM method converges.

**Corollary 3.3.** Under the conditions of Theorem 3.3, \(\omega\in(0,1]\) serves as a sufficient condition for the convergence of the TGM with weighted Jacobi as the smoother when solving (2.4).

_Proof._ We only need to prove that<tbc>

\(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}>1\)

<tbc>for any \((\gamma_1,\gamma_2)\in(1,2)\). A direct calculation gives

\(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}=\frac{-4g_1^{(\gamma_1)}-4\frac{\eta_2}{\eta_1}g_1^{(\gamma_2)}}{\left\|f_{\gamma_1}(\theta_1)+\frac{\eta_2}{\eta_1}f_{\gamma_2}(\theta_2)\right\|_\infty}=\frac{4\gamma_1+4\frac{\eta_2}{\eta_1}\gamma_2}{2^{\gamma_1+1}+\frac{\eta_2}{\eta_1}2^{\gamma_2+1}}>1.\)

The Proof is completed.

The above corollary indicates that regardless of how the conditions of equation (1.1) vary, as long as the relaxation parameter \(\omega\in(0,1]\), the TGM is always convergent, which provides a conservative but safe interval for parameter selection. Furthermore, the surface of \(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\) corresponding to different values of \((\gamma_1,\gamma_2)\) when _N_=64 is shown in Figure 1. It can be observed that the surface representing the values of \(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\) lies strictly above the light blue plane, and \(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\) achieves an approximate maximum value of 1.0615 when \((\gamma_1,\gamma_2)=(1.445,1.445)\). In the following, we use an example to show that the choice of \(\omega\) will significantly affect the iteration efficiency of the TGM.

**Example 3.1.** Consider a two-dimensional Riesz space fractional diffusion equation with _T_=1 and \(\Omega=(0,1)^2\). The exact solution is taken as<tbc>

\(u=e^{-t}(x-x^2)^2(y-y^2)^2,\)

