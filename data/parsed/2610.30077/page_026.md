Collecting the three pieces,

\(\big(D_2q^{n+1},q^{n+1}\big)=-\int_\Omega\kappa_\star(q^{n+1})^2+\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}-d_0\int_\Omega|\nabla(A_\star q^{n+1})|^2-\varepsilon_q\|\nabla q^{n+1}\|^2.\) (19)

The term \(\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}\) appears in both (18) and (19). It is the discrete counterpart of the cross term that appears twice in the proof of Proposition 2.1. The reason is the same: (S1) and (S3) contain the same flux \(c_\star\nabla\mu^{n+1}-\dots\) with the same relative sign, which is fixed by the sign convention in (1a). As in Step 5 of the proof of Proposition 2.1, we write (18) and (19) one under the other and add them:

\(\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}=-\int_\Omega b_\star|\nabla\mu^{n+1}|^2+\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1},\)<br>
\(\big(D_2q^{n+1},q^{n+1}\big)=\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}-d_0\int_\Omega|\nabla(A_\star q^{n+1})|^2\)<br>
\(-\int_\Omega\kappa_\star(q^{n+1})^2-\varepsilon_q\|\nabla q^{n+1}\|^2,\)

the shared term occurs once in each line, so adding the two equations does not cancel it but doubles it:

\(\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}+\big(D_2q^{n+1},q^{n+1}\big)\)<br>
\(=-\int_\Omega b_\star|\nabla\mu^{n+1}|^2+2\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}\)<br>
\(-d_0\int_\Omega|\nabla(A_\star q^{n+1})|^2-\int_\Omega\kappa_\star(q^{n+1})^2-\varepsilon_q\|\nabla q^{n+1}\|^2.\) (20)

_Step 3: Complete the square._ The first three terms on the right of (20) are exactly \(-b_\star|u|^2+2c_\star(u\cdot w)-d_0|w|^2\) with \(u=\nabla\mu^{n+1}\), \(w=\nabla(A_\star q^{n+1})\), pointwise. By the identity (4) (derived explicitly above, in the proof of Proposition 2.1) with _b=b<sub>⋆</sub>,c=c<sub>⋆</sub>_,<tbc>

\(b_\star|u|^2-2c_\star(u\cdot w)+d_0|w|^2=\big(b_\star-\frac{c_\star^2}{d_0}\big)|u|^2+\frac{1}{d_0}|c_\star u-d_0w|^2,\)

<tbc>so negating both sides converts the first three terms of (20), pointwise at every \(x\in\Omega\), into \(-\big(b_\star-\frac{c_\star^2}{d_0}\big)|u|^2-\frac{1}{d_0}|c_\star u-d_0w|^2\). Substituting this into (20) and integrating over \(\Omega\),

\(\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}+\big(D_2q^{n+1},q^{n+1}\big)\)<br>
\(=-\int_\Omega\big[\big(b_\star-\frac{c_\star^2}{d_0}\big)|\nabla\mu^{n+1}|^2+\frac{1}{d_0}|c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})|^2\big]\mathrm{d}x\)<br>
\(-\int_\Omega\kappa_\star(q^{n+1})^2-\varepsilon_q\|\nabla q^{n+1}\|^2.\)

Collecting the four terms on the right-hand side under one integral, with an overall minus sign, gives exactly \(-\widetilde{\mathcal{D}}^{n+1}\) as defined in (11). The four integrands \(\big(b_\star-\frac{c_\star^2}{d_0}\big)|\nabla\mu^{n+1}|^2\), \(\frac{1}{d_0}|c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})|^2\), \(\kappa_\star(q^{n+1})^2\) and \(\varepsilon_q|\nabla q^{n+1}|^2\) are precisely the four summands in the definition of \(\widetilde{\mathcal{D}}^{n+1}\). Hence

\(\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}+\big(D_2q^{n+1},q^{n+1}\big)=-\widetilde{\mathcal{D}}^{n+1}.\) (21)

This identity has no remainder depending on \(\phi^{n+1}-\phi^\star\). A naive linearisation would freeze only some of the coefficients and evaluate the others at \(\phi^{n+1}\). Here, every coefficient on the right-hand side of (20) is frozen (it carries the subscript ⋆ and is independent of \(\phi^{n+1}\) and _q_<sup>_n_+1</sup>), so (4) applies exactly.

