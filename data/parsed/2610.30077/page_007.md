using the same clamped state for all four of \(b,c,A,\kappa\), for uniformity, although strictly the clamp only matters for \(A,\kappa\), whose specific forms would otherwise be singular. The parameters _b,c_ remain well behaved throughout the range for the coefficient forms used here and _G<sub>⋆</sub>_ uses the unclamped \(\phi^\star\) throughout, since \(f'\) and _E<sub>f</sub>_ do not develop singularities either. This is the step, previewed in Section 1.4, on which the rest of the paper turns: freezing all of \(b,c,A,\kappa\) at the same state, rather than at several different ones or at \(\phi^{n+1}\) itself, is exactly what preserves the coupled cross-diffusion structure of (1) intact, as Section 4 shows next.

**Assumption 1** (Frozen coercivity)**.** We assume that \(b_\star(x)-c_\star(x)^2/d_0\ge 0\) for all _x_. This is the same coercivity condition as (5), evaluated at the frozen, clamped state \(s=\phi_b^\star(x)\). For the benchmark coefficient set, the condition is satisfied with \(b_\star-c_\star^2/d_0=\varepsilon_b\) at every point. Thus, the coercivity margin is strictly positive and independent of the time step \(\Delta t\).

### 3.3 The discrete scheme

The scheme advances only the variables \(\phi\), _q_, and _r_, since these are the three quantities governed by evolution equations in (1). Accordingly, the scheme must retain their values at the previous two time levels. The chemical potential \(\mu\), by contrast, is defined algebraically by (1b) as an instantaneous function of \(\phi\) and, following the SAV reformulation, _r_, at the current time level. Since \(\mu\) has no independent evolution equation, its value is recomputed at each time step from the current values of these variables. Consequently, neither \(\mu^n\) nor \(\mu^{n-1}\) is required by the scheme, and neither appears in the formulation below.

Collecting the pieces above, the scheme is obtained from the continuous system (1) by three simultaneous replacements: every time derivative \(\partial_t\) is replaced by the BDF2 operator _D_<sub>2</sub>, every phase-dependent coefficient is replaced by its frozen value (8), and the SAV auxiliary equation for _r_ from Section 2 is adjoined as a fourth equation. We label the resulting four equations (S1)-(S4) (“S” for “scheme”) to keep them visually distinct from the continuous model’s (1a)-(1c). For \(n\ge 1\), given \((\phi^{n-1},q^{n-1},r^{n-1})\) and \((\phi^n,q^n,r^n)\), we find \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\) solving

\(D_2\phi^{n+1}=\nabla\cdot\big(b_\star\nabla\mu^{n+1}-c_\star\nabla(A_\star q^{n+1})\big),\) (S1)

\(\mu^{n+1}=-\gamma\Delta\phi^{n+1}+r^{n+1}G_\star,\) (S2)

\(D_2q^{n+1}=-\kappa_\star q^{n+1}-A_\star\nabla\cdot\big(c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})\big)+\varepsilon_q\Delta q^{n+1},\) (S3)

\(D_2r^{n+1}=\frac{1}{2}\big(G_\star,D_2\phi^{n+1}\big).\) (S4)

By construction, each equation is linear in the unknowns \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\), since all coefficients are evaluated using the frozen, already-known quantities in (8), rather than the unknown \(\phi^{n+1}\) itself. The only coupling that prevents the four equations from being block- diagonal arises in (S4), where the scalar unknown _r_<sup>_n_+1</sup> is coupled to all degrees of freedom of \(\phi^{n+1}\) through the single scalar quantity \(\big(G_\star,D_2\phi^{n+1}\big)\). Section 5 exploits this specific structure to avoid solving the full coupled system simultaneously.

BDF2 itself needs two prior levels to get started, so the very first step, from \((\phi^0,q^0,r^0)\) to \((\phi^1,q^1,r^1)\), cannot use (S1)-(S4) directly. We use a first-order backward-Euler (BE) self-starting step by default: a simpler, one-previous-level scheme whose local error is \(O(\Delta t^2)\), small enough that it does not degrade the second-order global rate of the rest of the trajectory (checked numerically, Section 7.2). A Richardson-extrapolated variant, built from two half-steps of BE, is also available for a formally second-order-accurate start.

## 4 The discrete energy identity

Discretising a dissipative system can destroy the property that makes it dissipative. A time- stepping scheme does not automatically inherit the energy decay of the continuous system it<tbc>

