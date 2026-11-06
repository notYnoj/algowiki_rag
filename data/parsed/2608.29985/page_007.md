<tbc>We now claim that \(x\neq 0\). Indeed, if _x_=0, then the second equation in (15) reduces to _Ty_=0. Since _T_ is positive definite, it is nonsingular, and therefore _y_=0. Consequently, **u**=0, which contradicts the assumption that **u** is an eigenvector.

So we assume that \(\lambda\neq 0\) and \(x\neq 0\). In this case, from the second relation of Eq. (15), we get<tbc>

\(y=-T^{-1}Wx.\)

<tbc>Substituting _y_ in the first equation of (15) yields<tbc>

\(\alpha x-WT^{-1}Wx=\lambda(Tx+\alpha x).\) (16)

<tbc>Now, multiplying both sides of relation (16) from the left by the vector _x_<sup>∗</sup> , we obtain<tbc>

\(\alpha x^*x-x^*WT^{-1}Wx=\lambda(x^*Tx+\alpha x^*x).\) (17)

<tbc>Equation (17) yields

\(\lambda=\frac{\alpha-b}{\alpha+c}.\) (18)

where _c=x_<sup>∗</sup>_Tx_ and _b=x_<sup>∗</sup>_WT_<sup>-1</sup>_Wx_. For the convergence condition to hold, we must have \(|\lambda|<1\). Hence, from (18), we conclude that

\(\alpha>\frac{b-c}{2}.\)

Thus, the proof is complete.

**Remark 1.** _Since the values of c and b defined in Theorem 1 are positive and non-negative, respectively, it follows that all eigenvalues of the iteration matrix are real. Therefore, under condition_ (12)_, we have_ \(-1<\lambda<1\)_. Furthermore, if_

\(\alpha>\frac{1}{2}\left(\lambda_\mathrm{max}(WT^{-1}W)-\lambda_\mathrm{min}(T)\right),\) (19)

_then condition_ (12) _holds and the method converges. Moreover, we have_

\(x^*WT^{-1}Wx=\frac{(Wx)^*T^{-1}(Wx)}{(Wx)^*(Wx)}\cdot(x^*W^2x)\)<br>
\(\le\lambda_\mathrm{max}(T^{-1})\cdot\lambda_\mathrm{max}(W^2)\)<br>
\(=\frac{\sigma_\mathrm{max}^2(W)}{\lambda_\mathrm{min}(T)}.\)

_Therefore, by Eq._ (12)_, if_ \(\alpha>\mathrm{max}\{0,\beta\}\) _with_

\(\beta=\frac{1}{2}\left(\frac{\sigma_\mathrm{max}^2(W)}{\lambda_\mathrm{min}(T)}-\lambda_\mathrm{min}(T)\right),\) (20)

_the convergence of the method is guaranteed._

