### Denominator protection.

The denominators \(\Delta\lambda_{ij}\Delta\lambda_{ik}\) become small near the atmospheric resonance (\(\hat{A}\rightarrow 1\)). At resonance the minimum gap is<tbc>

\(\Delta\lambda_{31}^\mathrm{min}=\frac{\Delta m_{31}^2}{2E}\mathrm{sin}2\theta_{13}.\) (22)

<tbc>For the crustal benchmark the atmospheric resonance falls at _E_res≈12GeV (Section 9); at that energy, with \(\Delta m_{31}^2\approx 2.53\times 10^{-3}\mathrm{eV}^2\) and \(\mathrm{sin}2\theta_{13}\approx 0.29\),

\(|\Delta\lambda_{31}|_\mathrm{min}\approx\frac{2.53\times 10^{-3}\mathrm{eV}^2}{2\times 12\times 10^9\mathrm{eV}}\times 0.29\approx 3\times 10^{-14}\mathrm{eV}.\) (23)

The relative error from IEEE 754 double precision is bounded by

\(\frac{\delta\lambda}{|\Delta\lambda_{ij}|}\lesssim\epsilon_\mathrm{mach}\cdot\kappa_\mathrm{Vand},\kappa_\mathrm{Vand}\equiv\frac{\mathrm{max}_k|\lambda_k|}{|\Delta\lambda_{ij}|_\mathrm{min}},\) (24)

with \(\epsilon_\mathrm{mach}\approx 2.2\times 10^{-16}\). At the operating energies of all long-baseline experiments ( 2), which lie well below the crustal resonance at _E_res≈12GeV, the denominator \(|\Delta\lambda_{31}|\) is comparable to its vacuum value \(\Delta m_{31}^2\) and \(\kappa_\mathrm{Vand}=\mathcal{O}(1)\); the precision loss is at the level of \(\epsilon_\mathrm{mach}\) itself and is negligible for any foreseeable observable. The concern grows only as \(E\rightarrow E_\mathrm{res}\), where \(\kappa_\mathrm{Vand}\) rises; implementations should test \(|\Delta\lambda_{ij}|>\varepsilon_\mathrm{gap}\) before invoking Eq. (19), branching to the DMP approximation (Eq. 17) when the criterion fails. The matter Jarlskog invariant follows from the Naumov–Harrison–Scott identity \[29, 30\],

\(J_\mathrm{mat}=J\prod_{i>j}\frac{\Delta m_{ij}^2}{\Delta\lambda_{ij}},\) (25)

with _J=J_CP \(\mathrm{sin}\delta_\mathrm{CP}\) the vacuum invariant (Appendix B).

## 5.4 Oscillation Probability: General

With _V<sub>e</sub>_ and \(\lambda_i\),

\(P_{\alpha\beta}=\delta_{\alpha\beta}-4\sum_{i>j}\mathrm{Re}\big[V_{e\beta i}V_{e\alpha i}^*V_{e\beta j}^*V_{e\alpha j}\big]\mathrm{sin}^2\frac{\Delta\lambda_{ij}L}{4E}\)<br>
\(+2\sum_{i>j}\mathrm{Im}\big[V_{e\beta i}V_{e\alpha i}^*V_{e\beta j}^*V_{e\alpha j}\big]\mathrm{sin}\frac{\Delta\lambda_{ij}L}{2E}.\) (26)

In vacuum, \(V_e\rightarrow U\) and \(\Delta\lambda_{ij}\rightarrow\Delta m_{ij}^2\).

## 5.5 Iterative Refinement: Newton–Raphson and Halley

When two eigenvalues nearly coincide, \(\Delta_\mathrm{cubic}\rightarrow 0\) and cancellation may degrade the arccos evaluation; the Vandermonde condition number scales as \(\kappa_\mathrm{Vand}\sim\mathrm{max}_k\lambda_k/\mathrm{min}_{i\neq j}|\Delta\lambda_{ij}|\). As an alternative to Newton–Raphson, Halley’s method \[78\] has cubic convergence per step,

\(\lambda\rightarrow\lambda-\frac{2X(\lambda)X'(\lambda)}{2[X'(\lambda)]^2-X(\lambda)X''(\lambda)}.\) (27)

In the tested cases ( 4), a single Halley step from the DMP seed reaches machine precision, matching two Newton–Raphson steps; a comprehensive benchmark across the full parameter space is left to a dedicated numerical study.

