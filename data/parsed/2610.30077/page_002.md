couples a Cahn-Hilliard-type phase-field equation to an evolution equation for the elastic stress through a cross-diffusion flux. This structure is numerically delicate: energy-stable schemes for the uncoupled Cahn-Hilliard equation do not automatically extend to the coupled system, and the reference discretisation for exactly this reduced model \[6\] requires a nonlinear solve at every time step. This paper shows that a linear scheme can retain the same unconditional energy stability.

The scalar auxiliary variable (SAV) approach \[7, 8\] is a general strategy for exactly this kind of question: introducing one extra scalar unknown that tracks the square root of the (shifted) nonlinear part of the energy turns the troublesome nonlinear term (the derivative \(f'(\phi)\) of the double-well potential in (1b) below) into a linear one, at the cost of solving one additional, cheap scalar equation each step. Applied to a single Cahn-Hilliard equation this already gives a linear, unconditionally energy-stable scheme with no step-size restriction and no extra stabilisation term added by hand, the usual efficiency case made for SAV schemes. It is, however, nontrivial to extend this to the viscoelastic phase separation model given by Equation 1 below, where the SAV-linearised equation for the density \(\phi\) and the equation for the stress _q_ are coupled through the same cross-diffusion flux (Section 1.4).

Following Spiller et al. \[9\], Zhou et al. \[10\], and Brunk et al. \[6\], we consider a model without hydrodynamics that has the polymer volume fraction \(\phi\), the chemical potential \(\mu\), and a single scalar bulk elastic variable _q_ as dynamical variables. We consider the following system on a periodic domain \(\Omega\subset\mathbb{R}^d\) for \(t\in(0,T)\):

\(\partial_t\phi=\nabla\cdot(b(\phi)\nabla\mu-c(\phi)\nabla(A(\phi)q))\big),\) (1a)

\(\mu=-\gamma\Delta\phi+f'(\phi),\) (1b)

\(\partial_tq=-\kappa(\phi)q-A(\phi)\nabla\cdot\big(c(\phi)\nabla\mu-d_0\nabla(A(\phi)q)\big)+\varepsilon_q\Delta q,\) (1c)

The analysis below is independent of the spatial dimension _d_, although our numerical experiments use _d_=2. We impose periodic boundary conditions to eliminate boundary terms in the integration-by-parts identities used in Section 3.1 and to match the Fourier spectral discretisation described in Section 6. At the continuous level, other boundary conditions that eliminate the same boundary terms, such as suitable no-flux conditions, would also suffice. Here, \(\gamma>0\) is the gradient-energy coefficient, \(d_0,\varepsilon_q>0\) are constants, and _f_ is a double-well potential bounded from below. The functions \(b,c,A,\kappa\) depend on the phase field \(\phi\) and satisfy \(b,\kappa>0\) and \(c,A\ge 0\).

## 1.2 Energy structure

Equations (1) describe a system relaxing towards thermodynamic equilibrium: \(\phi\) and _q_ evolve so as to decrease a single scalar quantity _E_, with the terms on the right of (1) acting as dissipative (frictional) driving forces whose strength is set by the state-dependent coefficients \(b(\phi),c(\phi),A(\phi)\), together with, for _q_, additional linear damping from the \(-\kappa(\phi)q\) and \(\varepsilon_q\Delta q\) terms in (1c). We define the energy as

\(E(\phi,q)=\int_\Omega\big[\frac{\gamma}{2}|\nabla\phi|^2+f(\phi)+\frac{1}{2}q^2\big]\mathrm{d}x,\) (2)

a sum of three physically distinct contributions: the interfacial energy \(\frac{\gamma}{2}|\nabla\phi|^2\), which penalises sharp changes in composition and so favours smooth, spread-out interfaces; the bulk free energy \(f(\phi)\), a double-well potential favouring the two pure phases \(\phi\approx 0,1\) and so driving phase separation; and the elastic energy \(\frac{1}{2}q^2\) stored in the polymer network, penalising deviations of the elastic variable _q_ away from its relaxed value _q_=0.

For sufficiently smooth solutions that are periodic in space, the energy satisfies a dissipation law, (<tbc>

<tbc>d<tbc>

<tbc>_E_=-D), as shown in Section 2. The dissipation rate is non-negative only under a suitable condition on the model coefficients. We derive this condition, called the coercivity condition, and establish the continuous energy law in Section 2.

