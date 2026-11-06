# A linear, second-order, unconditionally energy-stable scalar-auxiliary-variable scheme for the CHQ viscoelastic phase-separation model

**Abstract**

The CHQ model describes viscoelastic phase separation in a polymer–solvent mixture: a Cahn–Hilliard equation for the polymer volume fraction \(\phi\) is two-way coupled, through a phase-dependent cross-diffusion flux, to a damped relaxation equation for a scalar bulk elastic stress _q_. We propose a scalar-auxiliary-variable (SAV) time discretisation of this system, combining the SAV reformulation of the double-well potential with a second-order backward differentiation formula (BDF2) and a second-order extrapolation of all phase-dependent mobilities: a linear, computationally cheaper complement to the reference scheme’s fully nonlinear Newton solve. The resulting method is (i) linear at every time step, with a coupling structure we prove has exactly one solution at every step, for every choice of time-step size; (ii) mass conserving, exactly, as an algebraic identity of the discrete equations themselves (the only drift ever seen numerically traces to the finite tolerance of the iterative linear solver, not a failure of the conservation property); and (iii) unconditionally stable for a modified discrete energy, via an exact one-step energy–dissipation identity. We show the energy identity extends to this filtered variant as well, with two explicit extra non-negative terms. Hence, the scheme actually producing the physics results is itself provably stable for the same energy. A Fourier–Galerkin implementation verifies that the energy identity holds at every time step to within floating-point round-off. It also confirms second-order temporal accuracy, including in the steep-interface regime, and agreement with an independently implemented nonlinear Newton–BDF2 solver. Compared with that independent nonlinear Newton–BDF2 solver, at equal grid resolution, the SAV method uses 2.5–3.0\(\times\) fewer linear-solver iterations and 1.7–2.0\(\times\) less wall-clock time.

### 1 Introduction

#### 1.1 The model

Phase separation in polymer solutions and melts is frequently accompanied by a pronounced viscoelastic response: the slower-relaxing polymer network resists deformation on the timescale of demixing, and the resulting elastic stress can dramatically alter, and in some cases arrest, the coarsening process compared to a simple binary fluid. The same coupling between phase separation and viscoelasticity is central to biomolecular condensates in living cells [1]. Condensates themselves age into viscoelastic, Maxwell-fluid-like materials rather than remaining simple liquids [2], and the surrounding chromatin network has been shown experimentally to slow the coalescence of nucleolar droplets by orders of magnitude relative to isolated liquid droplets, an arrest effect closely analogous to the elastic suppression of coarsening studied here [3]. More directly still, recent experiments show that tuning the viscoelastic properties of a nucleus-mimicking compartment controls the dynamics and liquid-to-solid transition of protein condensates [4]. This phenomenon, reviewed by Tanaka [5] and modelled by a hierarchy of increasingly reduced continuum descriptions,

<sup>∗</sup>Institute of Physics, Johannes Gutenberg University Mainz, Germany. `rbhola@uni-mainz.de` <sup>†</sup>Institute of Physics, Johannes Gutenberg University Mainz, Germany. `tevrugtm@uni-mainz.de`

Ritesh Bhola<sup>∗</sup>

Michael te Vrugt<sup>†</sup>

