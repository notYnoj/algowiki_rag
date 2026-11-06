#### Tube coordinates.

Let a centerline have arc length _s_, curvature \(\kappa_c\), and torsion \(\tau_c\). Let \((\rho,\vartheta)\) be polar coordinates in the normal plane, with \(\vartheta\) measured from a direction that rotates relative to the principal normal by the accumulated torsion angle \(\vartheta_0(s)\), \(|\vartheta'_0|=|\tau_c|\). Germano showed that this choice removes the off-diagonal terms and gives the orthogonal metric \(ds^2=d\rho^2+\rho^2d\vartheta^2+H^2ds^2\), where \(H=1-\kappa_c\rho cos(\vartheta-\vartheta_0)\) \[19\]. Over a short segment, or for \(\tau_c=0\), \(\vartheta_0\) can be set to zero, which gives the factor _H_ of Sec. 4.5. The cross-sectional coefficients of Eq. (20) follow from this metric.

#### Spectral asymptotics.

For the Dirichlet Laplace-Beltrami operator on a two-dimensional domain, Weyl’s law states that the number of eigenvalues below \(\lambda\) grows as \(|\Omega|_g\lambda/(4\pi)\) \[21\]. Since \(|\Omega|_g=\int\sqrt{g}\) is unchanged by a change of coordinates, the high-frequency part of the spectrum does not depend on the coordinate map.

## B Supplementary analyses

This appendix collects analyses that support the main text but are not needed to follow it.

### B.1 Green’s-function interpretation

The sampling laws have a natural interpretation in terms of Green’s functions \[27\]. We regard _A_ as a single-particle Hamiltonian and define, for the basis vector \(|z\rangle_F\) and the source _b_,

\(G_{zb}^\mathrm{prop}(T)=-i\langle z|_Fe^{-iAT}|b\rangle,G_{zb}^R(\omega)=\langle z|_F(\omega-A+i0^+)^{-1}|b\rangle,\rho_{zb}(\omega)=2\pi\sum_\lambda a_\lambda(z)\delta(\omega-\lambda).\) (34)

Here \(\rho_{zb}\) is a cross spectral measure and _G_<sup>prop</sup> is a propagator matrix element. It is not a many-body greater Green’s function, which would require a specified state, field operators, and occupation factors. The resolvent interpretation is exact for the finite matrix without those statistical assumptions.

**Proposition 18** (Green’s-function form)**.** _The quantities of Sec. 3 are_

\(q(z)=\frac{1}{d}\sum_k\big|G_{zb}^\mathrm{prop}(T_k)\big|^2,q^\infty(z)=\mathrm{lim}_{\mathscr{T}\rightarrow\infty}\frac{1}{\mathscr{T}}\int_0^\mathscr{T}\big|G_{zb}^\mathrm{prop}(T)\big|^2dT,\hat{b}_z=\int\frac{d\omega}{2\pi}\rho_{zb}(\omega),\hat{x}_z=-G_{zb}^R(0)=\int\frac{d\omega}{2\pi}\frac{\rho_{zb}(\omega)}{\omega}.\text{(35)}\)

_Proof._ The first relation is Eq. (6). The second follows from \(G_{zb}^\mathrm{prop}(T)=-i\sum_\lambda a_\lambda(z)e^{-i\lambda T}\), since the cross terms with \(\lambda\neq\mu\) average to zero. Equation (36) follows from Eq. (7).

Proposition 18 gives the sampling theory a spectral meaning. The source is the zeroth moment of the cross spectral measure, equal to \(\langle z|_Fb\rangle\), rather than a unit-normalized diagonal spectral sum rule; cross spectral weights can have either sign or be complex. The solution is the static response, that is, the moment of order -1. A single state measures only the zeroth moment, which can vanish by cancellation. The dephased law \(q^\infty\) is the sum of squared cross amplitudes at distinct eigenvalues. It does not measure the signed spectral measure itself. A time window of length T resolves frequencies only to about \(2\pi/\mathscr{T}\) , and the moment of order -1 is dominated by the lowest poles. This motivates the upper time scale of Algorithm 2; actual dephasing requires resolution of the relevant eigenvalue differences, as in Lemma 9. On the other hand, the quantum device returns only intensities \(|G_{zb}^\mathrm{prop}|^2\). The method therefore locates the spectral weight but does not reconstruct the Green’s function, in contrast with the approach of Ref. \[28\].

