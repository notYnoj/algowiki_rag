it, extrapolated from the two previous time levels. This section makes both ingredients precise and states the resulting scheme. Then in Section 4, we show that combining them preserves the energy identity exactly.

## 3.1 Notation

We define the scalar product as \(\big(u,v\big):=\int_\Omega uv\mathrm{d}x\) and the norm as \(\|u\|^2:=\big(u,u\big)\). On the periodic box, with no boundary terms, we have

\(\big(\nabla\cdot F,g\big)=-\big(F,\nabla g\big),\) (6a)

\(\big(\Delta u,g\big)=-\big(\nabla u,\nabla g\big).\) (6b)

The second identity follows from the first by taking \(F=\nabla u\).

Time derivatives are approximated by BDF2, the second-order backward differentiation formula: a standard finite-difference rule that approximates \(\dot{u}(t_{n+1})\) using the current level together with the two preceding ones, _u_<sup>_n_+1</sup>_,u<sup>n</sup>,u_<sup>_n_-1</sup> (as opposed to the simpler, only first-order- accurate backward-Euler rule, which uses just _u_<sup>_n_+1</sup>_,u<sup>n</sup>_). Write \(t_n=n\Delta t\) for the time levels and _u<sup>n</sup>≈u(t<sub>n</sub>_) for a numerical approximation at level _n_; a superscript ⋆ will denote a quantity frozen at the extrapolated state \(\phi^\star\), introduced below. Specifically, we define the BDF2 first and second time differences

\(D_2u^{n+1}:=\frac{3u^{n+1}-4u^n+u^{n-1}}{2\Delta t},D^2u^{n+1}:=u^{n+1}-2u^n+u^{n-1}.\) (7)

_D_<sub>2</sub>_u_<sup>_n_+1</sup> is the actual BDF2 approximation to \(\dot{u}(t_{n+1})\), accurate to \(O(\Delta t^2)\); _D_<sup>2</sup>_u_<sup>_n_+1</sup> is not itself an approximation to anything, but a bookkeeping quantity that will appear naturally, in Section 4, as the non-negative remainder left over after telescoping a BDF2 term into a discrete energy difference.

## 3.2 Freezing the coefficients

The one remaining obstacle to a linear scheme is that \(b,c,A,\kappa\) (and, after Section 2’s reformulation, _G_) are themselves functions of \(\phi\). Evaluating them at the unknown \(\phi^{n+1}\) being solved for would make every equation below nonlinear in \(\phi^{n+1}\), exactly the nonlinearity a Newton-type solver would have to iterate on instead; evaluating them at an already known approximation to \(\phi(t_{n+1})\) keeps every equation linear in the actual unknowns, at the cost of a small, controllable extrapolation error. Since \(\phi^n,\phi^{n-1}\) are already known once we reach time level _n_+1, we define the extrapolation<tbc>

\(\phi^\star:=2\phi^n-\phi^{n-1},\)

<tbc>a new value recomputed at every step from the two preceding ones. So, \(\phi^\star\) depends on _n_ exactly as \(\phi^n\) does, but we write \(\phi^\star\) rather than \(\phi^{\star,n+1}\) purely to keep the notation light. \(\phi^\star\) approximates \(\phi(t_{n+1})\) to \(O(\Delta t^2)\), of the same order as that achieved by BDF2. However, using \(\phi^\star=\phi^n\) instead would only be accurate to \(O(\Delta t)\) and would degrade the scheme’s overall accuracy. For the specific coefficient forms of the benchmark problem (\[6\], given in full in Section 7), \(A(\phi)\sim\mathrm{cot}(\pi\phi)\) and \(\kappa(\phi)\) blow up as \(\phi\rightarrow 0,1\); to guard against \(\phi^\star\) straying outside the physically admissible range before the scheme has had a chance to correct it, we additionally clamp it to the interval \([\delta_c,1-\delta_c]\),<tbc>

\(\phi_b^\star:=\mathrm{clamp}(\phi^\star,\delta_c,1-\delta_c):=\mathrm{min}\big(\mathrm{max}(\phi^\star,\delta_c),1-\delta_c\big),\delta_c\sim 10^{-3}\)

<tbc>(a numerical safeguard only, verified inactive throughout the convergence regime studied below). Every phase-dependent coefficient is then frozen at this same argument,<tbc>

\(b_\star:=b(\phi_b^\star),c_\star:=c(\phi_b^\star),A_\star:=A(\phi_b^\star),\kappa_\star:=\kappa(\phi_b^\star),G_\star:=\frac{f'(\phi^\star)}{\sqrt{E_f(\phi^\star)+C_0}},\) (8)

