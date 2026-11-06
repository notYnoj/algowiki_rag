Hence,<tbc>

\(w(t)=t\left(_{R-1-}\sum_{\xi=1}^n\beta_\xi\right).\)

<tbc>For the mono-FDE solution, we use \(\varrho(t)=\frac{t^{-\beta_1}}{\Gamma(1-\beta_1)}\) with _C_<sub>1</sub>(_t_) and _C_<sub>2</sub>(_t_) given by<tbc>

\(C_1(t)=\frac{\Gamma(1-\beta_1)\Gamma(2)t^{\beta_1}}{\Gamma(2-\beta_1)},C_2(t)=\Gamma(1-\beta_1)t^{2\beta_1}.\)

<tbc>Then, the solution takes the form<tbc>

\(f(x,y,t)=\left(\frac{\Gamma(2)}{\Gamma(2-\beta_1)}+\lambda_{1,1}t^{\beta_1}\right)2sin\left(\sqrt{\nu_1^1}x\right)sin(\mu_1y),\)<br>
\(u(x,y,t)=2tsin\left(\sqrt{\nu_1^1}x\right)sin(\mu_1y),\)

<tbc>with<tbc>

\(w(t)=t^{(1-\beta_1)}.\)

<tbc>The analytical results presented in this chapter establish a rigorous foundation for ISPs in a two-dimensional generalized diffusion equation. We have shown that these problems are severely ill-posed in the Hadamard sense, requiring regularization to restore stability. The series representations derived here, based on bi-orthogonal systems of eigenfunctions, provide explicit formulas for the solutions and highlight the challenges that arise when attempting to reconstruct unknown source coefficients from noisy observational data. In the following chapters, we shift our focus from the analytical treatment of ISPs to their numerical solution. The regularized formulations of these ISPs will be discretized using finite difference schemes, leading to large structured linear systems of the all-at-once type. The GLT framework, developed in Part I, will then become essential for understanding the spectral behavior of these systems and for designing efficient preconditioners that accelerate the convergence of Krylov subspace methods. In particular, Chapters 6 and 7 address the numerical solution of ISPs for space-time FDEs, building upon the regularization and analytical techniques introduced in this chapter.

