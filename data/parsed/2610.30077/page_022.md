<tbc>\(\frac{\mathrm{d}}{\mathrm{d}t}|\nabla\phi|^2=2,\nabla\phi\cdot\nabla\partial_t\phi\), where we have used the commutativity of time and spatial derivatives, \(\partial_t(\nabla\phi)=\nabla(\partial_t\phi)\). Multiplication by the prefactor \(\frac{\gamma}{2}\) yields \(\gamma,\nabla\phi\cdot\nabla\partial_t\phi\). For the second term, the chain rule gives \(\frac{\mathrm{d}}{\mathrm{d}t}f(\phi)=f'(\phi),\partial_t\phi\). For the third term, we obtain \(\frac{\mathrm{d}}{\mathrm{d}t}\big(\frac{1}{2}q^2\big)=q\partial_tq\). Integrating these pointwise derivatives over \(\Omega\) and expressing the resulting integrals as inner products,

\(\frac{\mathrm{d}}{\mathrm{d}t}E=\gamma\big(\nabla\phi,\nabla\partial_t\phi\big)+\big(f'(\phi),\partial_t\phi\big)+\big(q,\partial_tq\big).\) (15)

_Step 2: Combine the first two terms into_ \(\big(\mu,\partial_t\phi\big)\). Identity (6b), \(\big(\Delta u,g\big)=-\big(\nabla u,\nabla g\big)\), rearranges (swap the two sides and negate) to \(\big(\nabla u,\nabla g\big)=-\big(\Delta u,g\big)\) and applying this with \(u=\phi\), \(g=\partial_t\phi\), we get \(\big(\nabla\phi,\nabla\partial_t\phi\big)=-\big(\Delta\phi,\partial_t\phi\big)\). Multiplying by \(\gamma\) and using the bilinearity of the inner product, we obtain \(\gamma\big(\nabla\phi,\nabla\partial_t\phi\big)=-\gamma\big(\Delta\phi,\partial_t\phi\big)=\big(-\gamma\Delta\phi,\partial_t\phi\big)\). Adding the second term in (15) and using the additivity of the inner product, \(\big(a,c\big)+\big(b,c\big)=\big(a+b,c\big)\) with \(a=-\gamma\Delta\phi\), \(b=f'(\phi)\), \(c=\partial_t\phi\), we obtain<tbc>

\(\gamma\big(\nabla\phi,\nabla\partial_t\phi\big)+\big(f'(\phi),\partial_t\phi\big)=\big(-\gamma\Delta\phi+f'(\phi),\partial_t\phi\big).\)

<tbc>By (1b), \(-\gamma\Delta\phi+f'(\phi)=\mu\), so this equals \(\big(\mu,\partial_t\phi\big)\), and Step 1 becomes<tbc>

\(\frac{\mathrm{d}}{\mathrm{d}t}E=\big(\mu,\partial_t\phi\big)+\big(q,\partial_tq\big).\)

<tbc>_Step 3: Substitute_ \(\partial_t\phi\) _from_ (1a). Equation (1a) says \(\partial_t\phi=\nabla\cdot(b\nabla\mu-c\nabla(Aq))\). Substituting this expression for \(\partial_t\phi\) directly into \(\big(\mu,\partial_t\phi\big)\), we get<tbc>

\(\big(\mu,\partial_t\phi\big)=\big(\mu,\nabla\cdot(b\nabla\mu-c\nabla(Aq))\big).\)

<tbc>By the symmetry of the inner product, \(\big(\mu,\nabla\cdot F\big)=\big(\nabla\cdot F,\mu\big)\) for any flux _F_ and applying (6a), \(\big(\nabla\cdot F,g\big)=-\big(F,\nabla g\big)\), with \(F=b\nabla\mu-c\nabla(Aq)\) and \(g=\mu\), we obtain<tbc>

\(\big(\mu,\partial_t\phi\big)=-\big(b\nabla\mu-c\nabla(Aq),\nabla\mu\big).\)

<tbc>By the bilinearity of the inner product, we can expand the flux term as \(\big(b\nabla\mu-c\nabla(Aq),\nabla\mu\big)=\big(b\nabla\mu,\nabla\mu\big)-\big(c\nabla(Aq),\nabla\mu\big)\). Consequently,

\(\big(\mu,\partial_t\phi\big)=-\big(b\nabla\mu,\nabla\mu\big)+\big(c\nabla(Aq),\nabla\mu\big)=-\int_\Omega b|\nabla\mu|^2+\int_\Omega c\nabla\mu\cdot\nabla(Aq),\)

using \(\big(b\nabla\mu,\nabla\mu\big)=\int_\Omega b\nabla\mu\cdot\nabla\mu=\int_\Omega b|\nabla\mu|^2\) and the commutativity of the dot product, \(\nabla(Aq)\cdot\nabla\mu=\nabla\mu\cdot\nabla(Aq)\), inside the second integral.

_Step 4: Substitute_ \(\partial_tq\) _from_ (1c). Equation (1c) says \(\partial_tq=-\kappa q-A\nabla\cdot F+\varepsilon_q\Delta q\), with the flux \(F:=c\nabla\mu-d_0\nabla(Aq)\). Substituting into \(\big(q,\partial_tq\big)\) (testing (1c) with _g=q_) and distributing the inner product over the three terms of the sum (bilinearity in the second slot), we get

\(\big(q,\partial_tq\big)=\big(q,-\kappa q\big)+\big(q,-A\nabla\cdot F\big)+\big(q,\varepsilon_q\Delta q\big)=-\big(\kappa q,q\big)-\big(A\nabla\cdot F,q\big)+\varepsilon_q\big(\Delta q,q\big).\)

We can now consider the three terms on the right-hand side separately:

• The first is already a plain integral: \(-\big(\kappa q,q\big)=-\int_\Omega\kappa q^2\).<tbc>

• The third, by (6b) with _u=q,g=q_: \(\big(\Delta q,q\big)=-\big(\nabla q,\nabla q\big)=-\|\nabla q\|^2\), so \(\varepsilon_q\big(\Delta q,q\big)=-\varepsilon_q\|\nabla q\|^2\).<tbc>

• The second needs the same manoeuvre used repeatedly in Section 6-Section 7. At this point in the argument, \(A=A(\phi)\) is simply a known scalar field: it depends on neither \(\mu\) nor the unknown being tested against. So the product _Aq_ is itself a perfectly good test function.<tbc>

