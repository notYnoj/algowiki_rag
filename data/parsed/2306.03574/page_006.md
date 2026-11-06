With the diagonalization formulas, \(\mathcal{C}_\alpha\) (\(\alpha\in(0,1)\)) can be shown block diagonalizable as follows<tbc>

\(\mathcal{C}_\alpha=[(D_\alpha^{-1}\mathbb{F})\otimes I_m](\Lambda_{\alpha,1}\otimes L+\Lambda_{\alpha,2}\otimes I_m)[(\mathbb{F}^*D_\alpha)\otimes I_m].\) (1.7)

<tbc>Since _L_ is HPD, \(\Lambda_{\alpha,1}\otimes L+\Lambda_{\alpha,2}\otimes I_m\) is clearly diagonalizable. In other words, \(\mathcal{C}_\alpha\) is similar to a diagonalizable matrix and thus \(\mathcal{C}_\alpha\) itself is diagonalizable for \(\alpha\in(0,1)\). That means for \(\alpha\in(0,1)\) there exists an invertible matrix **X** and a diagonal matrix \(\mathrm{diag}(\mu_i)_{i=1}^{nm}\) such that<tbc>

\(\mathcal{C}_\alpha=\mathbf{X}^{-1}\mathrm{diag}(\mu_i)_{i=1}^{nm}\mathbf{X}.\)

<tbc>Thus, we can define a matrix square root of \(\mathcal{C}_\alpha\) for \(\alpha\in(0,1)\) as follows

\(\mathcal{C}_\alpha^{1/2}=\mathbf{X}^{-1}\mathrm{diag}(\sqrt{\mu_i})_{i=1}^{nm}\mathbf{X},\) (1.8)

where \(\sqrt{\mu_i}\) denotes the principal branch of complex square root of \(\mu_i\).

Consequently, we in this work propose the following HPD preconditioner for YT :

\(\mathcal{P}_\alpha=(\mathcal{C}_\alpha^{1/2})^T\mathcal{C}_\alpha^{1/2}.\) (1.9)

Then, instead of directly solving YT **u**=Y**f**, we employ the MINRES solver to solve the following equivalent preconditioned system

\(\mathcal{P}_\alpha^{-1}\mathcal{YT}\mathbf{u}=\mathcal{P}_\alpha^{-1}\mathcal{Yf}.\) (1.10)

For a real symmetric matrix **H**, denote by |**H**|, the positive semi-definite matrix obtained by replacing eigenvalues of **H** with its absolute value.

**Remark 1.** _When_ \(\alpha=1\), \(\mathcal{P}_\alpha=(\mathcal{C}_1^{1/2})^T\mathcal{C}_1^{1/2}=\sqrt{\mathcal{C}_1^T\mathcal{C}_1}=|\mathcal{C}_1|\) _reduces to the existing ABC preconditioner proposed in \[37\] for heat equations. However, as demonstrated by the numerical results in Section 3,_ P<sub>1</sub> _does not perform well for wave equations. The reason is that the eigenvalues of preconditioned matrix by the ABC preconditioner have outliers away from_ {-1,+1} _and the number of outliers is of_ O(_m), which means the iteration number needed for convergence increases as m increases. This is the motivation for proposing_ \(\mathcal{P}_\alpha\) _in this work. As will be shown, Theorem 13 gives choices of_ \(\alpha\in(0,1)\) _so that the MINRES solver for_ (1.10) _has a linear convergence rate independent of h and_ \(\tau\)_. With guidance of Theorem 13, results in Section 3 show that_ \(\mathcal{P}_\alpha\) _outperforms_ P<sub>1</sub> _for wave equations._

Ultimately, we will show that the preconditioned MINRES solver for the preconditioned system (1.10) achieves a convergence rate independent of \(\tau\) and _h_ and therefore independent of the matrix size.

This paper is organized as follows. We present our main results in Section 2 in which the<tbc>

