## Proof of the G-stability identity (13).

This identity is not new. It is the Nevanlinna-Odeh multiplier for BDF2 \[23\], the standard tool for proving G-stability \[22\] of multistep methods. We include its proof because it is used repeatedly above. The identity is purely algebraic: it holds for any three elements _x,y,z_ of the same space and does not use the model equations. Its role is to rewrite a term of the form \(\big(\)3_x_-4_y+z,x_\(\big)\), which arises whenever a BDF2 formula is tested against its newest level, as a telescoping difference of \(\Phi\) plus a non-negative remainder. This telescoping turns the step-by-step computation into a statement that the energy decreases monotonically. The identity is verified by expanding both sides into inner products and comparing coefficients.

Let _x=a_<sup>_n_+1</sup>, _y=a<sup>n</sup>_, _z=a_<sup>_n_-1</sup>, where _a_ denotes any of the quantities \(\nabla\phi\), _q_, _r_. Both sides of (13) can be written in terms of the six quantities \(\|x\|^2\), \(\big(\)_x,y_\(\big)\), \(\|y\|^2\), \(\big(\)_y,z_\(\big)\), \(\|z\|^2\), \(\big(\)_x,z_\(\big)\). Using \(\|u-v\|^2=\|u\|^2-2\big(u,v\big)+\|v\|^2\), we obtain<tbc>

\(\|2x-y\|^2=4\|x\|^2-4\big(x,y\big)+\|y\|^2,\)<br>
\(\|2y-z\|^2=4\|y\|^2-4\big(y,z\big)+\|z\|^2,\)<br>
\(\|x-2y+z\|^2=\|x\|^2+4\|y\|^2+\|z\|^2-4\big(x,y\big)+2\big(x,z\big)-4\big(y,z\big).\)

<tbc>The last line follows by expanding \(\big(\)_x_-2_y+z_, _x_-2_y+z_\(\big)\): the squared terms give \(\|x\|^2+4\|y\|^2+\|z\|^2\), and the cross terms give \(2\big(x,-2y\big)+2\big(x,z\big)+2\big(-2y,z\big)=-4\big(x,y\big)+2\big(x,z\big)-4\big(y,z\big)\). Inserting these expressions into the right-hand side of (13) yields

\(\frac{1}{2}\big[\Phi(x,y)-\Phi(y,z)\big]+\frac{1}{2}\|x-2y+z\|^2=\frac{1}{2}\big[(\|x\|^2+\|2x-y\|^2)-(\|y\|^2+\|2y-z\|^2)\big]\)<br>
\(+\frac{1}{2}\|x-2y+z\|^2\)<br>
\(=\frac{1}{2}\big[5\|x\|^2-4\big(x,y\big)-4\|y\|^2+4\big(y,z\big)-\|z\|^2\big]\)<br>
\(+\frac{1}{2}\big[\|x\|^2+4\|y\|^2+\|z\|^2-4\big(x,y\big)+2\big(x,z\big)-4\big(y,z\big)\big]\)<br>
\(=3\|x\|^2-4\big(x,y\big)+\big(x,z\big).\)

In the last step, all terms involving \(\|y\|^2\), \(\big(\)_y,z_\(\big)\) and \(\|z\|^2\) cancel between the two brackets. On the other hand, by the symmetry of the inner product,

\(\big(3x-4y+z,x\big)=3\|x\|^2-4\big(x,y\big)+\big(x,z\big).\)

The two sides of (13) therefore coincide, which proves the identity.

## Proof of Theorem 4.1.

The strategy mirrors the continuous proof of Proposition 2.1. It consists of three steps.

(i) _Testing._ We test (S1) with \(\mu^{n+1}\), (S2) with \(D_2\phi^{n+1}\) and (S3) with _q_<sup>_n_+1</sup>. The mixed term \(\int_\Omega c_\star\nabla\mu^{n+1}\cdot\nabla(A_\star q^{n+1})\) then appears in both the \(\phi\)- and the _q_-equation. Adding the two results yields the same doubled cross term as in the continuous proof.<tbc>

(ii) _Dissipation._ We apply the pointwise identity (4) to this expression. It turns the sum of the spatial terms into \(-\widetilde{\mathcal{D}}^{n+1}\), which is non-negative.<tbc>

(iii) _Telescoping._ We apply the algebraic G-stability identity (13) to each BDF2 term \(\big(\)_D_<sub>2</sub>_a_<sup>_n_+1</sup>, _a_<sup>_n_+1</sup>\(\big)\) with \(a=\nabla\phi,q,r\). Each term becomes a difference of consecutive values of \(\Phi\), plus a non-negative remainder.

Collecting the three resulting telescoping differences reproduces E<sup>_n_+1</sup>-E_<sup>n</sup>_, giving exactly (12).

_Step 1: Eliminate_ \(\mu^{n+1}\) _between_ (S1) _and_ (S2). Take the inner product of (S2) (\(\mu^{n+1}=-\gamma\Delta\phi^{n+1}+r^{n+1}G_\star\)) with \(D_2\phi^{n+1}\), i.e. multiply both sides of (S2) by \(D_2\phi^{n+1}\) and integrate over \(\Omega\):<tbc>

\(\big(\mu^{n+1},D_2\phi^{n+1}\big)=-\gamma\big(\Delta\phi^{n+1},D_2\phi^{n+1}\big)+r^{n+1}\big(G_\star,D_2\phi^{n+1}\big).\)

