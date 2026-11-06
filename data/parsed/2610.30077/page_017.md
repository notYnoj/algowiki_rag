<tbc>extrapolated state, with no time-step restriction. The energy-dissipation identity also holds for the post-step spectral-filtering variant used in the physics study of Section 7.3, establishing the stability of the numerical method used to obtain these results. The per-step linear system is uniquely solvable for every \(\Delta t>0\). Numerically, the energy-dissipation identity holds to round-off at every time step, even for \(\varepsilon_q=0\) and across five orders of magnitude in _C_<sub>0</sub>. The method achieves second-order temporal convergence, including for the thin interface \(\gamma=10^{-3}\), and spectral accuracy in space for the smooth test problems considered. Compared with an independent nonlinear Newton-BDF2 solver, it requires 2.5-3.0\(\times\) fewer linear iterations and 1.7-2.0\(\times\) less wall time. Moreover, it provides a per-step solvability guarantee that the nonlinear scheme lacks. On the reference configuration of Section 7, run to 10<sup>4</sup> steps from an identical initial perturbation, the method reproduces the qualitative viscoelastic suppression of phase separation reported in the literature: the coupled system forms a persistent, still-evolving gel-like network that never fully separates into the pure phases, while an uncoupled (\(A\equiv 0\)) control instead forms discrete droplets that coarsen to a fully phase-separated state. A methodological note is itself relevant here: the scheme’s un-dealiased spectral discretisation can develop grid-scale aliasing noise from evaluating nonlinear coefficients on the collocation grid; an optional post-hoc spectral filter (provably stability-preserving, Remark 4.2) removes it and is used throughout. A multigrid preconditioner for the local _q_-block operator (whose cost this steeper coefficient set makes concretely visible rather than hypothetical) and a rigorous relative-energy error estimate in the style of [6] are left for future work.

## Declarations

### Acknowledgements.

We thank Mária Lukácová-Medvidová and Aaron Brunk for helpful discussions.

Φ morphology, reference coefficients, N=128, =
(each panel scaled to its own range)
t = 0.0
t = 1.0
t = 2.0
t = 3.0
t = 4.0
0.402
0.6
0.7
0.8
0.8
0.401
0.5
0.6
0.6
0.4
0.5
0.6
0.4
0.4
0.4
0.4
0.399
0.3
0.3
0.4
0.4
0.399
0.2
0.2
0.2
0.2
0.2
0.1
0.1
0.1
0.402
1.0
1.0
1.0
1.0
0.8
0.8
0.8
0.8
0.8
0.401
0.6
0.6
0.6
0.6
0.400
0.4
0.4
0.4
0.4
0.4
0.399
0.2
0.2
0.2
0.2
0.2
0.2
0.398
0.398

Figure 6: \(\phi\) morphology, reference coefficients, _N_=128, \(\Delta t=10^{-3}\), dealiased, at _t_=0,1,2,3,4 (the early, most rapidly evolving part of the _T_=10 run); _each panel is scaled to its own_ \(\phi\) _range_ (colour bars shown) so structure is visible at every time, including the tiny initial perturbation at _t_=0. Top: coupled model. Bottom: \(A\equiv 0\) control (Cahn-Hilliard dynamics). The control already shows large, fully-saturated droplets by _t_=1 and coarsens by Ostwald ripening from there (plateauing by _t_≈7-8, beyond this figure’s range); the coupled model instead organises much more slowly into an interconnected network that stays at intermediate \(\phi\) (never reaching the well minima) and is still visibly coarsening at _t_=10; the two models are already qualitatively different within the first time unit.

