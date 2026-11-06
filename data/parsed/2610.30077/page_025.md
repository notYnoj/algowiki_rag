By (6b), we have \(-\gamma\big(\Delta\phi^{n+1},D_2\phi^{n+1}\big)=\gamma\big(\nabla\phi^{n+1},\nabla D_2\phi^{n+1}\big)\) and since _D_<sub>2</sub> is only a fixed linear combination of a field’s values at three time levels (it never touches the spatial variable), it commutes with the spatial gradient, \(\nabla D_2\phi^{n+1}=D_2\nabla\phi^{n+1}\). This is the commutation hypothesis of Theorem 4.1. So<tbc>

\(\big(\mu^{n+1},D_2\phi^{n+1}\big)=\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+r^{n+1}\big(G_\star,D_2\phi^{n+1}\big).\)

<tbc>Equation (S4) \((D_2r^{n+1}=\frac{1}{2}\big(G_\star,D_2\phi^{n+1}\big))\), multiplied by 2, says \(\big(G_\star,D_2\phi^{n+1}\big)=2D_2r^{n+1}\), so<tbc>

\(\big(\mu^{n+1},D_2\phi^{n+1}\big)=\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}.\) (16)

<tbc>Separately, take the inner product of (S1) with \(\mu^{n+1}\), i.e. test (S1) with \(g=\mu^{n+1}\), and use (6a) to get<tbc>

\(\big(D_2\phi^{n+1},\mu^{n+1}\big)=-\int_\Omega b_\star|\nabla\mu^{n+1}|^2+\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}.\) (17)

<tbc>The left-hand sides of (16) and (17) are equal by the symmetry of the inner product. So, equating the right-hand sides of (16) and (17) yields

\(\gamma\big(\nabla\phi^{n+1},D_2\nabla\phi^{n+1}\big)+2r^{n+1}D_2r^{n+1}=-\int_\Omega b_\star|\nabla\mu^{n+1}|^2+\int_\Omega c_\star\nabla(A_\star q^{n+1})\cdot\nabla\mu^{n+1}.\) (18)

This single equation has eliminated \(\mu^{n+1}\) from appearing on its own and it enters only through \(\nabla\mu^{n+1}\) on the right, exactly as in the continuous proof above.

_Step 2: Bring in the q-equation._ Take the inner product of (S3) with _q_<sup>_n_+1</sup> (test (S3) with _g=q_<sup>_n_+1</sup>). Write \(F:=c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})\) for the flux inside the divergence in (S3), so that (S3) reads \(D_2q^{n+1}=-\kappa_\star q^{n+1}-A_\star\nabla\cdot F+\varepsilon_q\Delta q^{n+1}\). Distributing the inner product over the three terms on the right (bilinearity in the second slot),<tbc>

\(\big(D_2q^{n+1},q^{n+1}\big)=-\big(\kappa_\star q^{n+1},q^{n+1}\big)-\big(A_\star\nabla\cdot F,q^{n+1}\big)+\varepsilon_q\big(\Delta q^{n+1},q^{n+1}\big).\)

<tbc>Again, we consider the three terms on the right-hand side separately:

• The first is already a plain integral: \(-\big(\kappa_\star q^{n+1},q^{n+1}\big)=-\int_\Omega\kappa_\star(q^{n+1})^2\).<tbc>

• The third, by (6b) with _u=g=q_<sup>_n_+1</sup>: \(\big(\Delta q^{n+1},q^{n+1}\big)=-\big(\nabla q^{n+1},\nabla q^{n+1}\big)=-\|\nabla q^{n+1}\|^2\), so \(\varepsilon_q\big(\Delta q^{n+1},q^{n+1}\big)=-\varepsilon_q\|\nabla q^{n+1}\|^2\).<tbc>

• For the second term, we use the same regrouping as in the proof of Proposition 2.1. Since _A<sub>⋆</sub>_ is a known function of _x_ (it is frozen), _A<sub>⋆</sub>q_<sup>_n_+1</sup> is an admissible test function. Indeed,<tbc>

\(\big(A_\star\nabla\cdot F,q^{n+1}\big)=\int_\Omega A_\star(\nabla\cdot F)q^{n+1}\mathrm{d}x=\int_\Omega(\nabla\cdot F)\left(A_\star q^{n+1}\right)\mathrm{d}x=\big(\nabla\cdot F,A_\star q^{n+1}\big).\)

Applying (6a) with _g=A<sub>⋆</sub>q_<sup>_n_+1</sup> gives<tbc>

<tbc>\(\big(A_\star\nabla\cdot F,q^{n+1}\big)=-\big(F,\nabla(A_\star q^{n+1})\big).\)<tbc>

<tbc>With \(F=c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})\), this yields<tbc>

\(-\big(A_\star\nabla\cdot F,q^{n+1}\big)=\big(F,\nabla(A_\star q^{n+1})\big)\)<br>
\(=\int_\Omega c_\star\nabla\mu^{n+1}\cdot\nabla(A_\star q^{n+1})-d_0\int_\Omega|\nabla(A_\star q^{n+1})|^2.\)

