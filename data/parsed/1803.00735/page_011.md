phasing rates

\(\frac{\hbar\Gamma_{\mu\nu}}{U_\mathrm{Q}}=\frac{\kappa}{\bar{\Delta}_c}N^2\sum_m|\theta_m^\mu-\theta_m^\nu|^2\) (32)

go to zero for \(\tilde{\Delta}_c/\kappa\gg 1\). Thus, as expected, the open system converges to the coherent Schrödinger dynamics in this limit (see Fig. 6(b)).

Note that the coherence between states creating similar fields is preserved much longer than for other states, which is expected to be important at the late stage of the sweep. For states with fixed similarity (e.g. one atom moved), \(|\theta_m^\mu-\theta_m^\nu|^2\) is on the order of _N_<sup>-2</sup>, and thus the dephasing rates do not scale with _N_ for such states.

## 5 Read-out

After the parameter sweep we need to determine if the obtained state is a solution or not. This can in principle be done by reading out the final atomic state with single site resolution using a quantum gas microscope [59, 60]. However, as we consider an open system with the cavity output fields readily available, we will show that by proper measurements on the output light we can directly answer this question without further additions. Note that after the sweep at the stage of the read-out, quantum coherences do not have to be preserved since the solution is a classical state. This gives the freedom to increase the lattice depth to some high value in the deep lattice regime to suppress further tunneling, and to increase the pump power or decrease the detunings in order to get a stronger signal at the detector.

### 5.1 Intensity measurement

For uniform cavity detunings, a state corresponding to the solution of the _N_-queens problem scatter less photons than all other states. Thus the measurement of the total intensity in principle allows one to distinguish a solution from other states. To illustrate this we consider the total rate of photons impinging on a detector scattered

by an atomic state \(|\psi\rangle\)

\(P(|\psi\rangle)=\sum_m2\kappa_m\langle(a_m^\mathrm{st})^\dagger a_m^\mathrm{st}\rangle=\sum_m\frac{2\kappa_m}{\bar{\Delta}_{c,m}}\frac{\tilde{\Delta}_{c,m}\eta_m^2N^2}{\bar{\Delta}_{c,m}^2+\kappa_m^2}\langle\hat{\Theta}_m^\dagger\hat{\Theta}_m\rangle\approx U_\mathrm{Q}\frac{\zeta}{\hbar}\sum_{ijkl}\tilde{A}_{ijkl}\langle\hat{n}_{ij}\hat{n}_{kl}\rangle=\frac{\zeta}{\hbar}\langle H_\mathrm{cav}^\mathrm{dl}\rangle.\text{(33)}\)

In the last line we assumed that \(\zeta=2\kappa_m/\bar{\Delta}_{c,m}\) does not depend on _m_ and a deep lattice.

Since _P_ is proportional to the energy expectation value, the ground state, i.e. the solution of the queens problem, causes a minimal photon flux at the detector \(P_0=3NU_\mathrm{Q}\zeta\). It stems from the on-site terms (_i,j_)=(_k,l_), where the factor 3 comes from the three pump directions. In contrast, each pair of queens violating the non- attacking condition in \(\tilde{A}\) leads to an increase of the photon flux by \(\Delta P=2U_\mathrm{Q}\zeta\). The two atoms create an energy penalty for one another, explaining the factor 2. The relative difference of the photon flux due to a state with _L_ attacking pairs and a solution is given by

\(\frac{L\Delta P}{P_0}=\frac{2L}{3N}.\) (34)

As this scales with 1_/N_ it is difficult to distinguish solutions from other states via measurement of the intensity for large _N_. Note that for non-uniform \(\kappa_m/\tilde{\Delta}_{c,m}\), photons from different modes have to be distinguished.

### 5.2 Field measurement

Measurement of the output field quadratures, for example by homodyne detection, gives insight about the absolute position of the atoms projected onto the pump laser propagation direction. For the three directions used in our setup, this yields the occupations of each column \(\langle\hat{N}_i^x\rangle\) and each diagonal \(\langle\hat{N}_i^+\rangle\) and \(\langle\hat{N}_i^-\rangle\). Since a solution of the queens problem has maximally one atom on each diagonal and exactly one atom on each column, it must fulfill

\(\langle\hat{N}_i^x\rangle=1\wedge\langle\hat{N}_i^+\rangle\le 1\wedge\langle\hat{N}_i^-\rangle\le 1.\) (35)

The output field quadratures can thus be used to determine if a classical final state is a solution or not, which is the answer to the blocked diagonals decision problem we aim to solve. The signatures

