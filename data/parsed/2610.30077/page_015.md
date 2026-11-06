<tbc>between the solver and its own forcing-term construction would not be caught by either. As a check on the underlying right-hand side itself, we therefore also compare against an independently implemented nonlinear Newton-BDF2 solver that treats \(f'(\phi^{n+1})\) fully implicitly, with no SAV device at all. We run both schemes from the same initial condition on a generic, well-conditioned coefficient set,

\(c(\phi)=0.4+0.2cos\phi,b(\phi)=\frac{c(\phi)^2}{1.2}+0.2,A(\phi)=0.5+0.3sin\phi,\)<br>
\(\kappa(\phi)=0.6+0.3\phi^2,f(\phi)=(\phi-0.3)^2(\phi-0.7)^2,\)

with _d_<sub>0</sub>=1.2, \(\gamma=0.3\), \(\varepsilon_q=0.15\) (deliberately distinct from the reference configuration of  1, and free of its steep \(A(\phi)\) transition, to test that agreement is not special to that one coefficient choice), on a \(19\times 19\) grid to _T_=0.12, at five step sizes \(\Delta t\in\{8,4,2,1,0.5\}\times 10^{-3}\). The max-norm difference between the two schemes’ \(\phi\) fields shrinks consistently at order 2.04,2.02,2.00,2.01 across all four successive halvings (Figure 5), and the difference between their true energies shrinks at a matching \(O(\Delta t^2)\) rate, exactly as expected since both schemes are independently second-order accurate approximations of the same dynamics, so their pairwise difference should vanish at this same rate.

## Cost against the nonlinear scheme.

At \(\gamma=0.20\) (linearly stable, so both schemes compute the same solution), the SAV scheme uses \(2.5-3.0\times\) fewer linear iterations and \(1.7-2.0\times\) less wall time than Newton-BDF2 at _N_=64-128, at substantially less memory (no Jacobian storage). The underlying reason for this advantage is structural, not just an empirical count: the linear SAV system is unconditionally solvable at each step (Theorem 5.1), whereas Newton additionally requires its nonlinear iteration to actually converge; in the linearly stable regime tested here this requirement costs little in practice (Newton converges in 2-3 iterations even at \(\Delta t\sim 0.1\)), but it is a requirement the SAV scheme simply does not have. The simple Fourier preconditioner does degrade at very large \(\Delta t\) and at a steep \(A(\phi)\). The headline demonstration and physics study below, both run at this steeper coefficient set, show this cost directly rather than avoiding it: up to 845 GMRES iterations per step at the coarsest \(\Delta t\) tested (Section 7.1). This is a preconditioner limitation ((12) stays at round-off throughout), underscoring that a multigrid preconditioner for this regime is a genuine priority, not merely a theoretical concern, for future work.

MMS temporal convergence (reference coeffs, = 0.3, N=40)
Backward-Euler startup Richardson startup slope 2
10-5
10-6
10-7
10-8
10-4
10-3
At

Figure 4: Temporal convergence order measured by the method of manufactured solutions (MMS), reference coefficients, both startups, against a slope-2 reference.

