<tbc>It should be remarked that the parameter \(\gamma\) has no influence on the convergence analysis of the proposed method, nor on the spectral properties of the preconditioned matrix. Nevertheless, this parameter proves to be effective in numerical experiments.

## 3 Eigenvalue analysis of \(\mathscr{P}_\text{\textbf{VBP}}^{-1}\mathscr{A}\)

**Theorem 2.** _Under the assumptions of Theorem 1, the eigenvalues of the preconditioned matrix_ \(\mathscr{P}_\text{\textit{VBP}}^{-1}\mathscr{A}\) _are real and positive, and lie in the interval_

\(\sigma(\mathscr{P}_\text{\textit{VBP}}^{-1}\mathscr{A})\subset\left[\frac{\lambda_\mathrm{min}(T)+\sigma_\mathrm{min}^2(W)/\lambda_\mathrm{max}(T)}{\alpha+\lambda_\mathrm{max}(T)},\frac{\lambda_\mathrm{max}(T)+\sigma_\mathrm{max}^2(W)/\lambda_\mathrm{min}(T)}{\alpha+\lambda_\mathrm{min}(T)}\right].\) (21)

_where_ \(\lambda_\mathrm{min}(T)\) _and_ \(\lambda_\mathrm{max}(T)\) _are the smallest and largest eigenvalues of T, respectively, and_ \(\sigma_\mathrm{min}(W)\) _and_ \(\sigma_\mathrm{max}(W)\) _are the smallest and largest singular value of W, respectively._

_Proof._ Let \(\zeta\) be an eigenvalue of the preconditioned matrix \(\mathscr{P}_\text{VBP}^{-1}\mathscr{A}\). Then, it can be expressed as \(\zeta=1-\lambda\), where \(\lambda\) is an eigenvalue of the iteration matrix L<sub>VBP</sub>. Using Eq. (18), we can write

\(\zeta=1-\frac{\alpha-b}{\alpha+c}=\frac{c+b}{c+\alpha},\) (22)

where _c=x_<sup>∗</sup>_Tx_ and _b=x_<sup>∗</sup>_WT_<sup>-1</sup>_Wx_.

Given that _T_ is symmetric positive definite, the definitions of the quadratic forms _c_ and _b_ ensure that \(\zeta\) is real and positive.

Under the assumptions stated in Theorem 1, the variables _c_ and _b_ are bounded as follows

\(\lambda_\mathrm{min}(T)\le c\le\lambda_\mathrm{max}(T),\text{and}\frac{\sigma_\mathrm{min}^2(W)}{\lambda_\mathrm{max}(T)}\le b\le\frac{\sigma_\mathrm{max}^2(W)}{\lambda_\mathrm{min}(T)}.\) (23)

To determine the bounds for \(\zeta\), we apply the inequalities from (23) to the expression in (22). Assuming \(\alpha>0\) and knowing _c\>_0, we can establish the lower bound by minimizing the numerator and maximizing the denominator<tbc>

\(\zeta\ge\frac{\lambda_\mathrm{min}(T)+\frac{\sigma_\mathrm{min}^2(W)}{\lambda_\mathrm{max}(T)}}{\alpha+\lambda_\mathrm{max}(T)}.\)

<tbc>Similarly, we obtain the upper bound by maximizing the numerator and minimizing the denominator

\(\zeta\le\frac{\lambda_\mathrm{max}(T)+\frac{\sigma_\mathrm{max}^2(W)}{\lambda_\mathrm{min}(T)}}{\alpha+\lambda_\mathrm{min}(T)}.\)

