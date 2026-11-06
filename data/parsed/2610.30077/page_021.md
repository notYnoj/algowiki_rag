Both are repeated here for convenience:

\(\big(\nabla\cdot F,g\big)=-\big(F,\nabla g\big),\big(\Delta u,g\big)=-\big(\nabla u,\nabla g\big).\)

A second recurring convention concerns the star subscript \((b_\star,c_\star,A_\star,\kappa_\star,G_\star)\), which indicates that a coefficient is evaluated at the extrapolated, already-known state \(\phi^\star\) or its clamped version \(\phi_b^\star\) (see Section 3). These coefficients are independent of the unknown \(\phi^{n+1}\) and are therefore fixed and known when the equations are solved. This property ensures that the scheme is linear in \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\). It also allows these coefficients to be moved in and out of inner products as appropriate. Finally, operators _D_<sub>2</sub> and _D_<sup>2</sup> (see (7)) are time-difference operators involving three consecutive time levels of a quantity, rather than spatial derivatives. Finally, \(\Phi(u,v):=\|u\|^2+\|2u-v\|^2\) is a specific combination of two time levels, introduced because it yields a telescoping identity under the BDF2 recursion, as shown in (13) below. It has no independent significance beyond this role.

## Exact equivalence of the SAV reformulation.

The SAV trick replaces the nonlinear term \(f'(\phi)\) in (1b) by the product \(rG(\phi)\) of a new unknown _r(t_) and a known function _G_, and supplies _r_ with its own evolution equation. This is only useful if the enlarged system has exactly the same solutions as the original one. We show this by proving that, along any solution of the enlarged system, _r(t_) is forced to always equal \(\sqrt{E_f(\phi(t))+C_0}\), which is exactly the value that makes \(rG(\phi)\) equal \(f'(\phi)\).

With \(r(t):=\sqrt{E_f(\phi(t))+C_0}\) and \(G(\phi):=f'(\phi)/\sqrt{E_f(\phi)+C_0}\) (so, by construction, \(r(t)G(\phi(t))=f'(\phi(t))\) whenever _r(t_) happens to take this particular value), the SAV system replaces (1b) by \(\mu=-\gamma\Delta\phi+rG(\phi)\), where _r_ is now an independent unknown, and appends the equation \(\dot{r}=\frac{1}{2}\big(G(\phi)\), \(\partial_t\phi\big)\) to determine it. We must check that this new equation for _r_ is actually consistent with the formula that motivated it. By the chain rule,

\(\frac{\mathrm{d}}{\mathrm{d}t}\sqrt{E_f(\phi(t))+C_0}=\frac{1}{2\sqrt{E_f(\phi(t))+C_0}}\big(f'(\phi),\partial_t\phi\big).\)

If, at some instant, \(r=\sqrt{E_f(\phi)+C_0}\) already holds, then also \(f'(\phi)=rG(\phi)\) at that instant (by definition of _G_), so the right-hand side above becomes exactly \(\frac{1}{2}\big(G(\phi),\partial_t\phi\big)\), precisely the right-hand side of the SAV system’s own equation for \(\dot{r}\). In other words: the function \(t\mapsto\sqrt{E_f(\phi(t))+C_0}\) and any solution _r(t_) of the SAV system satisfy the same differential equation for \(\dot{r}\) (with \(\phi(t)\) regarded as already determined), and they start from the same value at _t_=0, since _r_(0) is initialised as \(\sqrt{E_f(\phi(0))+C_0}\).

Two functions of _t_ with the same derivative at every instant and the same value at one instant must be equal for all time: their difference has derivative zero everywhere and value zero at _t_=0, so by the fundamental theorem of calculus the difference is zero everywhere. Hence \(r(t)\equiv\sqrt{E_f(\phi(t))+C_0}\) along any solution of the SAV system, and therefore \(r(t)G(\phi(t))\equiv f'(\phi(t))\) for all _t_: the SAV \(\mu\)-equation reduces identically to the original (1b), so every solution of the SAV system solves (1). Conversely, given any solution of (1), defining \(r(t):=\sqrt{E_f(\phi(t))+C_0}\) satisfies the SAV system’s _r_-equation automatically, by the same chain-rule computation run in reverse: the two systems have exactly the same solutions.

## Proof of Proposition 2.1.

We compute \(\frac{\mathrm{d}}{\mathrm{d}t}E\) directly from the definition of _E_ (2), substitute the two evolution equations (1a) and (1c) to eliminate \(\partial_t\phi,\partial_tq\), and then complete the square in the resulting cross term to reveal a manifestly non-negative quantity.

_Step 1: Differentiate E term by term._

Recall that \(E=\int_\Omega\big[\frac{\gamma}{2}|\nabla\phi|^2+f(\phi)+\frac{1}{2}q^2\big]\mathrm{d}x\). We differentiate each term in the integrand with respect to time. For smooth solutions, differentiation and integration over the fixed domain \(\Omega\) commute. For the first term, we use \(|\nabla\phi|^2=\nabla\phi\cdot\nabla\phi\). The product rule then gives<tbc>

