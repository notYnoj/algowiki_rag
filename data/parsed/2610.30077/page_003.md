## 1.3 Related work

Brunk, Egger, Habrich and Lukácová-Medvidová \[6\] (Correction \[11\]) give a rigorously analysed, fully nonlinear finite-element / variational-in-time discretisation of (1) with an exact energy identity and order-optimal error estimates via relative energy, and name the SAV route as future work for cheaper solves. Strasser, Tierra, Dünweg and Lukácová-Medvidová \[12, 13\] give linear, energy-stable schemes for the full hydrodynamic polymer–solvent model by a secant linearisation (not SAV), without an error analysis. Structural cousins include a Cahn–Hilliard/Allen–Cahn cross-kinetic coupling \[14\], viscoelastic Cahn–Hilliard models discretised by compactness-driven (not SAV, not linear) schemes \[15, 16\], and the nearest SAV scheme for any mechanically-coupled phase-field model, a Caginalp/elastic-solid system \[17\] structurally distinct from (1). The SAV approach itself \[7, 8, 18\] and the frozen-mobility-at-extrapolated-state device \[19\] are established for scalar gradient flows; single-auxiliary-variable SAV has been used for other coupled Cahn– Hilliard systems \[20, 21\]. To the best of our knowledge, no SAV, IEQ, or energy-quadratisation discretisation has previously been proposed for (1), or for any viscoelastic Cahn–Hilliard model with this cross-diffusion structure.

## 1.4 Contribution

For standard Cahn–Hilliard-type gradient flows, the SAV device separates the nonlinear free- energy term from the remaining linear operator by freezing it at an extrapolated state, and the resulting scheme’s energy stability then follows term by term. In (1), however, \(\phi\) and _q_ are coupled through the same phase-dependent cross-diffusion flux \(c(\phi)\nabla(A(\phi)q)\), entering the two equations with opposite sign: freezing _c_ and _A_ independently, or at the new-time solution, breaks the exact coupled-dissipation structure that produces the dissipation term (3) in the continuous energy law, and reintroduces a \(\Delta t\)-dependent remainder that would have to be absorbed by a stabilisation term or a step-size restriction. The observation underlying Theorem 4.1 below is that freezing all of \(b,c,A,\kappa\) at one common extrapolated state \(\phi^\star\) preserves this cross-diffusion structure exactly, so the SAV reformulation and the BDF2 energy identity combine with no such remainder and no restriction on \(\Delta t\).

The new contribution of this work is not the SAV device or the extrapolation device in isolation, but to show that they together survive the _coupled_ cross-diffusion dissipation structure of (1). Concretely:

(i) an SAV–BDF2 discretisation of the full coupled system, linear at every step, with a proof (Theorem 4.1) that the modified-energy identity (12) extends exactly to the coupled dissipation form with the \(A(\phi)\)-weighted test (holding for any time step \(\Delta t>0\), with no stabilisation term and no \(\|\phi^{n+1}-\phi^\star\|\) remainder), together with an extension (Remark 4.2) to the post-step spectral-filtering variant actually used for the physics study;<tbc>

(ii) a per-step solvability theorem (Theorem 5.1): the linear system (S1)–(S4) is uniquely solvable for every \(\Delta t>0\);<tbc>

(iii) numerical verification: the identity to round-off, second-order temporal accuracy at the physical \(\gamma=10^{-3}\), spectral spatial accuracy on the smooth test problems considered, agreement with an independent nonlinear solver, and a clean cost comparison.

The present work is complementary to that of Ref. \[6\], not an improvement on its analysis; we do not claim a rigorous error estimate.

### Outline.

Section 2 derives the continuous energy law and its SAV reformulation. Section 3 states the discrete scheme. Section 4 proves the discrete energy identity, the paper’s main result. Section 5 establishes solvability and mass conservation. Section 6 discusses accuracy and the Fourier–Galerkin implementation. Section 7 collects the numerical evidence: the identity to<tbc>

