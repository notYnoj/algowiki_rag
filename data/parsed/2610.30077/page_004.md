round-off, convergence, agreement with independent solvers, cost, and the coupled-vs-uncoupled demonstration. Proofs are given as concise sketches in the main text; fuller derivations are collected in Appendix A.

## 2 The continuous energy law and its SAV reformulation

We first establish the energy-decay property of the continuous model (1), introduced in Section 1.2. We show not only that the energy _E_ decreases over time, but also derive an explicit decay rate in terms of the model’s coefficients. The numerical scheme in Section 3 will be designed to reproduce this decay rate exactly at the discrete level.

**Proposition 2.1.** _Let_ \((\phi,\mu,q)\) _solve_ (1)_. Then_ \(\frac{\mathrm{d}}{\mathrm{d}t}E=-\mathcal{D}\) _with_

\(\mathcal{D}=\int_\Omega\big[\big(b(\phi)-\frac{c(\phi)^2}{d_0}\big)|\nabla\mu|^2+\frac{1}{d_0}\big|c(\phi)\nabla\mu-d_0\nabla(A(\phi)q)\big|^2+\kappa(\phi)q^2+\varepsilon_q|\nabla q|^2\big]\mathrm{d}x,\) (3)

_and_ \(\mathcal{D}\ge 0\) _whenever_ \(b(\phi)d_0\ge c(\phi)^2\) _pointwise, the coercivity condition_ (5).

_Proof._ Differentiating _E_, substituting (1b), and integrating by parts gives \(\frac{\mathrm{d}}{\mathrm{d}t}E=\big(\mu,\partial_t\phi\big)+\big(q,\partial_tq\big)\). Pairing (1a) with \(\mu\) and (1c) with _q_ (that is, multiplying each equation by the stated function and integrating over \(\Omega\)), the two resulting cross terms are equal rather than cancelling, by the sign convention adopted in (1a). The elementary identity

\(b|u|^2-2c\left(u\cdot w\right)+d_0|w|^2=\big(b-\frac{c^2}{d_0}\big)|u|^2+\frac{1}{d_0}\big|cu-d_0w\big|^2\) (4)

applied pointwise with \(u=\nabla\mu\), \(w=\nabla(Aq)\) then gives (3). This continuous dissipation identity is already implicit in \[6, 9\]. We record it here, with the sign convention and coercivity threshold made explicit, as the baseline the discrete scheme of Section 3 is required to reproduce. Full proof in Appendix A.

The energy _E_ satisfies \(\frac{\mathrm{d}}{\mathrm{d}t}E=-\mathcal{D}\) but nothing guarantees \(\mathcal{D}\ge 0\) for an arbitrary choice of the coefficients \(b,c,A,\kappa\). Checking this directly is exactly what produces the one structural condition the coefficients must satisfy. The first two terms in the dissipation rate (3) form a quadratic expression in \(\nabla\mu\) and \(\nabla(A(\phi)q)\). By (4), this expression is non-negative for arbitrary values of these gradients if and only if

\(b(\phi)d_0\ge c(\phi)^2\text{for all admissible}\phi.\) (5)

The remaining terms in (3) are non-negative because \(\kappa(\phi)>0\) and \(\varepsilon_q>0\). Thus, the coercivity condition (5) guarantees that the continuous energy is non-increasing. This condition is Assumption (A1) of \[6\].

### 2.1 The SAV reformulation

Proposition 2.1 establishes the continuous energy law. We now focus on discretising (1). The only nonlinear term is \(f'(\phi)\) in the \(\mu\)-equation (1b), which comes from the double-well potential _f_. The scalar auxiliary variable (SAV) method removes this nonlinearity by introducing a scalar unknown _r(t_), a single real number at each time, rather than a new field over \(\Omega\). The resulting enlarged system has exactly the same solutions as the original system, but no longer contains \(f'(\phi)\) explicitly.

The construction starts by separating the part of the energy that is already at most quadratic from the part that carries the nonlinearity. Specifically, we write _E=E_<sub>lin</sub>+_E<sub>f</sub>_ with<tbc>

\(E_\mathrm{lin}:=\int_\Omega\big[\frac{\gamma}{2}|\nabla\phi|^2+\frac{1}{2}q^2\big]\mathrm{d}x,E_f:=\int_\Omega f(\phi)\mathrm{d}x.\)

