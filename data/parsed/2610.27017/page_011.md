Owing to<tbc>

\(\mathrm{lim}_{\theta\rightarrow 0}\frac{f_\gamma(\theta)}{-2\mathrm{cos}\left(\frac{\gamma\pi}{2}\right)|\theta|^\gamma}=1\)

<tbc>and<tbc>

\(\mathrm{lim}_{(\theta_1,\theta_2)\rightarrow(0,0)}\frac{\theta_1^2+\theta_2^2}{2-\mathrm{cos}\theta_1-\mathrm{cos}\theta_2}=2.\)

<tbc>Then

\(\mathrm{lim}_{(\theta_1,\theta_2)\rightarrow(0,0)}\frac{f_{\gamma_1,\gamma_2}(\theta_1,\theta_2)}{2-\mathrm{cos}\theta_1-\mathrm{cos}\theta_2}=+\infty.\)

Thus, the quotient cannot attain its infimum near the origin. Since it is continuous away from the origin, its infimum is attained on a compact subset of \([-\pi,\pi]^2\backslash\{(0,0)\}\). Therefore, the infimum may equivalently be written as a minimum.<br>
The Proof is completed.

Several properties obtained by applying positive diagonal matrix perturbations are presented below. If _A_ and _B_ are symmetric positive definite matrices, the notation \(A\le B\) means that _B-A_ is a nonnegative definite matrix.

**Lemma 3.4.** Let \(A=(a_{ij})\in\mathbb{R}^{n\times n}\) be a symmetric positive definite matrix , and let _B=A+D_, where _D_ is a nonnegative diagonal matrix. Then

\(\rho(\mathrm{diag}(B)^{-1}B)\le\rho(\mathrm{diag}(A)^{-1}A).\) (3.9)

_Proof._ We denote _D_<sub>0</sub>=diag(_A_). Let<tbc>

\(l=\rho(D_0^{-1}A)=\lambda_\mathrm{max}\big(D_0^{-\frac{1}{2}}AD_0^{-\frac{1}{2}}\big).\)

<tbc>Since \(\mathrm{tr}(D_0^{-\frac{1}{2}}AD_0^{-\frac{1}{2}})=n\), we have \(l\ge 1\) and<tbc>

\(D_0^{-\frac{1}{2}}AD_0^{-\frac{1}{2}}\le lI_n,\)

<tbc>i.e.,<tbc>

\(A\le lD_0.\) (3.10)

<tbc>Since \(D\ge 0\) and \(l\ge 1\), we have<tbc>

\(D\le lD.\) (3.11)

<tbc>Adding (3.10) and (3.11), we obtain<tbc>

\(A+D\le l(D_0+D).\) (3.12)

<tbc>Applying the congruence transformation induced by \((D+D_0)^{-\frac{1}{2}}\) to both sides of the above inequality yields

\((D+D_0)^{-\frac{1}{2}}(A+D)(D+D_0)^{-\frac{1}{2}}\le lI_n.\)

Taking the maximum eigenvalue on both sides of the above matrix inequality yields (3.9).<br>
The proof is complete.

