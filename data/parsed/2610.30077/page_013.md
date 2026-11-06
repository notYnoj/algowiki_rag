E_<sup>n</sup>_ decreases strictly at every step and mass is conserved to to within the GMRES tolerance at all three \(\Delta t\), including \(\Delta t=10^{-2}\) (Figure 2), exactly as Theorem 4.1 guarantees. But Figure 1 shows stability does not imply accuracy: the two finer \(\Delta t\) agree closely up to _t_≈3 before separating by _t_=10 (0.0704 vs. 0.0618, a 12% gap), while \(\Delta t=10^{-2}\) diverges from both much earlier and settles at _E_(10)=0.1199, roughly \(2\times\) the finer runs’ value, consistent with its markedly higher GMRES cost (median 675 iterations/step vs. 84 at \(\Delta t=10^{-4}\)) and clamp activity: the simple Fourier preconditioner is a poor approximation to the true operator once \(A(\phi)\)’s transition layer becomes comparably sharp to 1_/N_, so this coarse a \(\Delta t\) genuinely underresolves the coupled dynamics, even though the discrete energy identity itself holds throughout. Whether the residual gap between the two finer \(\Delta t\) is still-shrinking temporal error or reflects the coarsening dynamics’ own sensitive dependence on small perturbations once neighbouring domains begin to interact is not resolved here.

## 7.2 The energy identity, convergence, and independent solvers

Every algebraic identity used in the proofs above, including the sign-sensitive completing-the- square step, was additionally checked by independent computer-algebra verification, as a safeguard against hand-algebra slips.

We also checked numerically that the linear system (S1)-(S4) is not merely solvable in principle (Theorem 5.1) but well conditioned in practice. To quantify this, we assembled the matrix corresponding to the system of equations (S1)-(S4) explicitly (of size 2_N_<sup>2</sup>+1) on a small grid, _N_=13, and computed its singular values. The matrix depends on the solution only through the frozen coefficients, which are functions of \(\phi^\star\). To avoid depending on the states visited by a particular simulation, we drew \(\phi^\star\) at random, for three independent draws, and used step sizes \(\Delta t\in\{10^{-4},10^{-2},1,10^2\}\). Across all of these cases, the smallest singular value stays at \(\sigma_\mathrm{min}\unknown 4\times 10^{-4}\), and the condition number stays below \(2\times 10^6\). The matrix therefore is far from singular, and round-off errors are amplified at most by this factor.

Mass conservation (reference coefficients) (dense per-step log, N= 128, T= 10)
10-9
10-11
10-13
10-15
10-17
At = 1e - 2
At = 1e - 3
At = 1e - 4
0
2
4
6
8
10
t

Figure 2: Mass conservation |_M(t_)-_M_(0)| (dense per-step log, log scale), same three runs. All stay at or below 10<sup>-9</sup>, growing with the number of steps taken. Proposition 5.1 is an identity for the linear system (S1)-(S4) _as solved exactly_. Each GMRES solve leaves a residual up to the 10<sup>-10</sup> tolerance above, so this is the finite-precision floor on an otherwise exact conservation law, not machine round-off, and it accumulates mildly over the 10<sup>3</sup>-10<sup>5</sup> steps taken rather than staying fixed per step.

