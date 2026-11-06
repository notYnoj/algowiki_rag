<tbc>Since _f_ is bounded below, we may fix a constant _C_<sub>0</sub> large enough that \(E_f(\phi)+C_0\ge C_1>0\) for every admissible \(\phi\) (any _C_<sub>0</sub>_\>_0 works for our benchmark, where \(f\ge 0\) already; we use _C_<sub>0</sub>=1); this positivity is needed so that the square root<tbc>

\(r(t):=\sqrt{E_f(\phi(t))+C_0},G(\phi):=\frac{f'(\phi)}{\sqrt{E_f(\phi)+C_0}}\)

<tbc>is always well defined. Here _r(t_) is a single scalar that tracks, at every instant, the size of the nonlinear part of the energy along the solution, and _G_ is a new coefficient function chosen for exactly one reason: by construction, \(rG(\phi)=f'(\phi)\) whenever _r_ happens to take the value \(\sqrt{E_f(\phi)+C_0}\). This suggests replacing the troublesome \(f'(\phi)\) in (1b) by the product \(rG(\phi)\) and treating _r_ as an independent unknown, governed by its own evolution equation,

\(\dot{r}=\frac{1}{2}\big(G(\phi),\partial_t\phi\big),\)

appended to the system. The evolution equation for _r_ follows directly from differentiating \(r=\sqrt{E_f(\phi)+C_0}\) using the chain rule (Appendix A). Consequently, if this relation holds initially, it is preserved throughout the evolution. Introducing _r_ also allows \(G(\phi)\) to be treated as a coefficient function, alongside _b,c,A_, and \(\kappa\). In the discrete scheme of Section 3, these coefficients are evaluated at the extrapolated state. This reformulation makes the \(\mu\)-equation linear in the joint unknowns \((\phi,\mu,q,r)\), regardless of the form of the double-well potential _f_.

This substitution is legitimate because the enlarged system has exactly the same solutions as the original (1). We show in Appendix A that the appended equation for _r_ forces \(r(t)\equiv\sqrt{E_f(\phi(t))+C_0}\) along every solution, given matching initial data, so that \(r(t)G(\phi(t))\equiv f'(\phi(t))\) identically and the SAV \(\mu\)-equation reduces back to (1b). Along any such solution the modified energy

\(\widetilde{E}:=E_\mathrm{lin}+r^2-C_0\)

is therefore identically equal to the true energy _E_, and satisfies a dissipation law of exactly the same completed-square form as before, \(\frac{\mathrm{d}}{\mathrm{d}t}\widetilde{E}=-\widetilde{\mathcal{D}}\le 0\), with \(\widetilde{\mathcal{D}}\) built from (3) in the same way, only with \(f'(\phi)\) replaced by \(rG(\phi)\) throughout. Note that _q_’s contribution to the energy, \(\frac{1}{2}q^2\), is already quadratic, so it needs no auxiliary variable of its own; only the single genuinely nonlinear piece _f_ is quadratised, and a single extra scalar _r_ suffices for the whole system, regardless of how finely \(\Omega\) is resolved.

One caveat carries forward to the numerical scheme and is worth flagging now. The identity \(r(t)\equiv\sqrt{E_f(\phi(t))+C_0}\) above holds exactly only because, in continuous time, two quantities that start out equal and change at the same rate at every instant must stay equal forever. Once time is replaced by discrete steps (Section 3), _r_<sup>_n_+1</sup> is no longer obtained from that continuous argument: it is computed by advancing a difference equation one step at a time, and nothing forces this step-by-step update to reproduce \(\sqrt{E_f(\phi^{n+1})+C_0}\) exactly. The two quantities, _r<sup>n</sup>_ and \(\sqrt{E_f(\phi^n)+C_0}\), can therefore differ by a small, controlled amount. This is exactly where the modified and true discrete energies can differ (Remark 4.3 discusses this in detail).

## 3 The SAV-BDF2 scheme

Section 2 established that the continuous, SAV-reformulated system dissipates its modified energy exactly, with no restriction on the coefficients beyond coercivity. Turning this into a usable numerical method needs two further ingredients: a way to approximate the time derivatives \(\partial_t\phi,\partial_tq,\dot{r}\) to second order in the step size \(\Delta t\), and a way to evaluate the phase-dependent coefficients \(b,c,A,\kappa,G\) without reintroducing the very nonlinearity the SAV device was meant to remove. The first is supplied by a standard second-order finite-difference formula in time, BDF2. The second is this paper’s central device, already previewed in Section 1.4: evaluate every coefficient not at the unknown new state \(\phi^{n+1}\), but at an already-known approximation to<tbc>

