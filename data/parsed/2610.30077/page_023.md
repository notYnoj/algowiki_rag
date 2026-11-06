Concretely,<tbc>

\(\big(A\nabla\cdot F,q\big)=\int_\Omega A\big(\nabla\cdot F\big)q\mathrm{d}x=\int_\Omega(\nabla\cdot F)\left(Aq\right)\mathrm{d}x=\big(\nabla\cdot F,Aq\big),\)

since the three scalar factors \(A,\nabla\cdot F,q\) can be regrouped freely under the integral: ordinary multiplication of numbers is commutative and associative. Applying (6a) with _g=Aq_ gives \(\big(\nabla\cdot F,Aq\big)=-\big(F,\nabla(Aq)\big)\), so \(\big(A\nabla\cdot F,q\big)=-\big(F,\nabla(Aq)\big)\).

Substituting \(F=c\nabla\mu-d_0\nabla(Aq)\) and distributing the inner product over its two terms,

\(-\big(A\nabla\cdot F,q\big)=\big(F,\nabla(Aq)\big)=\big(c\nabla\mu-d_0\nabla(Aq),\nabla(Aq)\big)\)<br>
\(=\big(c\nabla\mu,\nabla(Aq)\big)-d_0\big(\nabla(Aq),\nabla(Aq)\big)=\int_\Omega c\nabla\mu\cdot\nabla(Aq)-d_0\|\nabla(Aq)\|^2.\)

Collecting the three pieces, we find<tbc>

\(\big(q,\partial_tq\big)=-\int_\Omega\kappa q^2+\int_\Omega c\nabla\mu\cdot\nabla(Aq)-d_0\int_\Omega|\nabla(Aq)|^2-\varepsilon_q\|\nabla q\|^2.\)

<tbc>_Step 5: Add Steps 3 and 4._ Writing the two results one under the other,<tbc>

\(\big(\mu,\partial_t\phi\big)=-\int_\Omega b|\nabla\mu|^2+\int_\Omega c\nabla\mu\cdot\nabla(Aq),\)<br>
\(\big(q,\partial_tq\big)=\int_\Omega c\nabla\mu\cdot\nabla(Aq)-d_0\int_\Omega|\nabla(Aq)|^2-\int_\Omega\kappa q^2-\varepsilon_q\|\nabla q\|^2,\)

<tbc>and adding column by column, we obtain

\(\frac{\mathrm{d}}{\mathrm{d}t}E=\big(\mu,\partial_t\phi\big)+\big(q,\partial_tq\big)=-\int_\Omega b|\nabla\mu|^2+2\int_\Omega c\nabla\mu\cdot\nabla(Aq)-d_0\int_\Omega|\nabla(Aq)|^2-\int_\Omega\kappa q^2-\varepsilon_q\|\nabla q\|^2.\)

This is the point where the sign of the coupling term in (1a) matters: it is chosen precisely so that testing both equations produces the same cross term twice, rather than two cross terms that would instead cancel each other (in which case the calculation below would not produce a sign-definite dissipation at all, and the coercivity condition (5) discussed in Section 2 above would not arise).

_Step 6: complete the square._ The first three terms on the right have the pointwise form \(-b|u|^2+2c(u\cdot w)-d_0|w|^2\) with \(u=\nabla\mu\), \(w=\nabla(Aq)\), exactly the configuration of identity (4), stated above in the proof of Proposition 2.1. The algebraic identity (4)

holds because expanding its right-hand side gives \(\big(b-\frac{c^2}{d_0}\big)|u|^2+\frac{1}{d_0}\big(c^2|u|^2-2cd_0(u\cdot w)+d_0^2|w|^2\big)=b|u|^2-\frac{c^2}{d_0}|u|^2+\frac{c^2}{d_0}|u|^2-2c(u\cdot w)+d_0|w|^2=b|u|^2-2c(u\cdot w)+d_0|w|^2\), since the two \(\frac{c^2}{d_0}|u|^2\) terms (one negative, one positive) cancel exactly. Negating both sides of this identity converts \(-b|u|^2+2c(u\cdot w)-d_0|w|^2\) pointwise, at every \(x\in\Omega\), into \(-\big(b-\frac{c^2}{d_0}\big)|u|^2-\frac{1}{d_0}|cu-d_0w|^2\).

_Step 7: assemble_ D. Substituting this pointwise rewriting into the first three terms of the result of Step 5, and integrating over \(\Omega\), gives<tbc>

\(\frac{\mathrm{d}}{\mathrm{d}t}E=-\int_\Omega\big[\big(b-\frac{c^2}{d_0}\big)|\nabla\mu|^2+\frac{1}{d_0}|c\nabla\mu-d_0\nabla(Aq)|^2\big]\mathrm{d}x-\int_\Omega\kappa q^2-\varepsilon_q\|\nabla q\|^2.\)

<tbc>Collecting all four terms under one integral, with an overall minus sign in front, reproduces exactly \(\frac{\mathrm{d}}{\mathrm{d}t}E=-\mathcal{D}\), with D as defined in (3). Term by term, the four summands match: \(\big(b-\frac{c^2}{d_0}\big)|\nabla\mu|^2\), \(\frac{1}{d_0}|c\nabla\mu-d_0\nabla(Aq)|^2\), \(\kappa q^2\), and \(\varepsilon_q|\nabla q|^2\) are precisely the four terms inside the integral defining D.<tbc>

