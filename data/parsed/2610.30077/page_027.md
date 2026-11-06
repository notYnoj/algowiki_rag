_Step 4: Telescoping the left-hand side._ Each of the three terms on the left of (21) has the form \(\big(D_2a^{n+1},a^{n+1}\big)\). For \(a=\nabla\phi\) and _a=q_ this holds directly. For _a=r_ it holds because _r_ is a scalar, so that 2_r_<sup>_n_+1</sup>_D_<sub>2</sub>_r_<sup>_n_+1</sup>=2\(\big(D_2r^{n+1},r^{n+1}\big)\). By the definition (7), \(2\Delta tD_2a^{n+1}=3a^{n+1}-4a^n+a^{n-1}\). Taking the inner product with _a_<sup>_n_+1</sup> and applying the G-stability identity (13) gives

\(2\Delta t\big(D_2a^{n+1},a^{n+1}\big)=\big(3a^{n+1}-4a^n+a^{n-1},a^{n+1}\big)=\frac{1}{2}\big[\Phi(a^{n+1},a^n)-\Phi(a^n,a^{n-1})\big]+\frac{1}{2}\|D^2a^{n+1}\|^2.\) (22)

Applying (22) with \(a=\nabla\phi\) and multiply the whole line by \(\gamma\) to get

\(2\Delta t\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)=\frac{\gamma}{2}\big[\Phi(\nabla\phi^{n+1},\nabla\phi^n)-\Phi(\nabla\phi^n,\nabla\phi^{n-1})\big]+\frac{\gamma}{2}\|\nabla D^2\phi^{n+1}\|^2.\) (23)

Applying (22) with _a=q_, we get

\(2\Delta t\big(q^{n+1},D_2q^{n+1}\big)=\frac{1}{2}\big[\Phi(q^{n+1},q^n)-\Phi(q^n,q^{n-1})\big]+\frac{1}{2}\|D^2q^{n+1}\|^2.\) (24)

Applying (22) with _a=r_ and then multiply the by 2 (matching the factor of 2 already present in 2_r_<sup>_n_+1</sup>_D_<sub>2</sub>_r_<sup>_n_+1</sup>) gives

\(2\Delta t\cdot 2r^{n+1}D_2r^{n+1}=\big[\Phi(r^{n+1},r^n)-\Phi(r^n,r^{n-1})\big]+\big(D^2r^{n+1}\big)^2.\) (25)

Adding (23),(24) and (25), the left-hand side is exactly \(2\Delta t\) times the left-hand side of (21), which by (21) equals \(2\Delta t(-\widetilde{\mathcal{D}}^{n+1})\), so

\(2\Delta t\big(-\widetilde{\mathcal{D}}^{n+1}\big)=\frac{1}{2}\big\{\gamma\big[\Phi(\nabla\phi^{n+1},\nabla\phi^n)-\Phi(\nabla\phi^n,\nabla\phi^{n-1})\big]+\big[\Phi(q^{n+1},q^n)-\Phi(q^n,q^{n-1})\big]\)<br>
\(+2\big[\Phi(r^{n+1},r^n)-\Phi(r^n,r^{n-1})\big]\big\}+\frac{\gamma}{2}\|\nabla D^2\phi^{n+1}\|^2+\frac{1}{2}\|D^2q^{n+1}\|^2+\big(D^2r^{n+1}\big)^2.\)

The curly-braced quantity is exactly 4(E<sup>_n_+1</sup>-E_<sup>n</sup>_) by the definition (10) of E_<sup>n</sup>_,

\(\mathcal{E}^{n+1}-\mathcal{E}^n=\frac{1}{4}\big\{\gamma\big[\Phi(\nabla\phi^{n+1},\nabla\phi^n)-\Phi(\nabla\phi^n,\nabla\phi^{n-1})\big]\)<br>
\(+\big[\Phi(q^{n+1},q^n)-\Phi(q^n,q^{n-1})\big]+2\big[\Phi(r^{n+1},r^n)-\Phi(r^n,r^{n-1})\big]\big\},\)

the constant -_C_<sub>0</sub> appearing identically inside E<sup>_n_+1</sup> and E_<sup>n</sup>_ having cancelled upon subtraction and

\(2\Delta t\big(-\widetilde{\mathcal{D}}^{n+1}\big)=\frac{1}{2}\cdot 4\big(\mathcal{E}^{n+1}-\mathcal{E}^n\big)+\frac{\gamma}{2}\|\nabla D^2\phi^{n+1}\|^2+\frac{1}{2}\|D^2q^{n+1}\|^2+\big(D^2r^{n+1}\big)^2\)<br>
\(=2\big(\mathcal{E}^{n+1}-\mathcal{E}^n\big)+\frac{\gamma}{2}\|\nabla D^2\phi^{n+1}\|^2+\frac{1}{2}\|D^2q^{n+1}\|^2+\big(D^2r^{n+1}\big)^2.\)

Dividing this last equation through by 2 and rearranging gives

\(\big(\mathcal{E}^{n+1}-\mathcal{E}^n\big)+\frac{1}{4}\big[\gamma\|\nabla D^2\phi^{n+1}\|^2+\|D^2q^{n+1}\|^2+2\big(D^2r^{n+1}\big)^2\big]=-\Delta t\widetilde{\mathcal{D}}^{n+1},\)

which, after moving \(-\Delta t\widetilde{\mathcal{D}}^{n+1}\) to the left, is exactly (12).

_Step 5: Non-negativity._ Each term in the definition (11) of \(\widetilde{\mathcal{D}}^{n+1}\) is the integral of a pointwise non-negative function:

• \(\big(b_\star-\frac{c_\star^2}{d_0}\big)|\nabla\mu^{n+1}|^2\ge 0\) by Assumption 1;<tbc>

• \(\frac{1}{d_0}|c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})|^2\ge 0\), since it is a square and _d_<sub>0</sub>_\>_0;<tbc>

• \(\kappa_\star(q^{n+1})^2\ge 0\), since \(\kappa_\star\ge 0\);<tbc>

• \(\varepsilon_q|\nabla q^{n+1}|^2\ge 0\), since \(\varepsilon_q\ge 0\).

Hence \(\widetilde{\mathcal{D}}^{n+1}\ge 0\), which completes the proof.

