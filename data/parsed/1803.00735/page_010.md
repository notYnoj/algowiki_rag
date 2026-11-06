consider the semi-classical Hamiltonian

\(H_\mathrm{cav}^\mathrm{class}=\hbar\sum_m\frac{N^2\tilde{\Delta}_{c,m}\eta_m^2}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}\)<br> \(\times\left(\hat{\Theta}_m^\dagger\langle\hat{\Theta}_m\rangle+\langle\hat{\Theta}_m^\dagger\rangle\hat{\Theta}_m-|\langle\hat{\Theta}_m\rangle|^2\right),\) (27)

where the expectation values have to be calculated self-consistently with the current atom state vector. This substitution amounts to considering only first order fluctuations around the mean of \(\hat{\Theta}_m\) in Eq. (16).

Consequently, the dynamics are described by a differential equation which is non-linear in the state vector \(|\psi\rangle\). We numerically solve this equation by self-consistently updating the expectation value in each time step. It turns out that even for very long sweep times, using classical fields does not lead to a solution of the queens problem. The time evolution for \(J\tau/\hbar=49\) is depicted in Fig. 5(b). The discrepancy shows the necessity of entangled light-matter states in our procedure.

## 4.3 Dephasing due to cavity field loss

Finally, motivated by experimental considerations, we consider the open system including photon decay through the cavity mirrors. This system can be described by a master equation for the atoms [54]

\(\dot{\rho}=-\frac{i}{\hbar}[H_\mathrm{kin}+H_\mathrm{cav}^\mathrm{eff},\rho]\)<br> \(+\sum_m\frac{N^2\eta_m^2\kappa_m}{\Delta_{c,m}^2+\kappa_m^2}\left(2\hat{\Theta}_m\rho\hat{\Theta}_m^\dagger-\{\hat{\Theta}_m^\dagger\hat{\Theta}_m,\rho\}\right),\) (28)

where curly brackets denote the anti-commutator (see Appendix B). The model is suitable for analyzing the dephasing close to the coherent regime before any steady state is reached.

More insight can be gained by rewriting it in the basis of scattering eigenstates \(|\nu\rangle\) with \(\hat{\Theta}_m|\nu\rangle=\theta_m^\nu|\nu\rangle\), which scatter a field \(\alpha_m^\nu=\frac{N\eta_m}{\tilde{\Delta}_{c,m}+i\kappa_m}\theta_m^\nu\). These states converge to the occupation states in the deep lattice limit. The time evolution for the matrix elements \(\rho_{\mu\nu}=\langle\mu|\rho|\nu\rangle\) reads

\(\dot{\rho}_{\mu\nu}=(-\Gamma_{\mu\nu}-i\Omega_{\mu\nu})\rho_{\mu\nu}\)<br> \(-i\frac{J}{\hbar}\sum_k\left(\langle\mu|\hat{B}|k\rangle\rho_{k\nu}-\langle k|\hat{B}|\nu\rangle\rho_{\mu k}\right)\) (29)

with the rates

\(\Omega_{\mu\nu}=\sum_m\tilde{\Delta}_{c,m}(|\alpha_m^\mu|^2-|\alpha_m^\nu|^2)\) (30)

\(\Gamma_{\mu\nu}=\sum_m\kappa_m|\alpha_m^\mu-\alpha_m^\nu|^2.\) (31)

While the energy gaps \(\hbar\Omega_{\mu\nu}\) describe the coherent dynamics we considered up to now, the dephasing rates \(\Gamma_{\mu\nu}\) stem from photon loss. Hence a superposition of two scattering eigenstates \(|\mu\rangle\) and \(|\nu\rangle\) looses its coherence depending on the difference of the scattered fields, or how distinguishable the states are by field measurement.

We now return to the example we had before, using uniform mode strengths _f<sub>m</sub>_=1_/M_, decay rates \(\kappa\) and detunings \(\tilde{\Delta}_c\). Figure 6 compares the coherent Schrödinger time evolution from Sec. 4.1, the mean-field approximation with classical cavity fields from Sec. 4.2 and the open system dynamics with dephasing. For the latter the master equation is approximated by using Monte-Carlo wave function simulations. As a measure of similarity between states we use the fidelity. For two mixed states it is defined as \(F(\rho,\sigma)=\mathrm{Tr}(\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}})\) and reduces to the overlap \(|\langle\psi|\phi\rangle|\) for pure states.

The open system dynamics is depicted for different detunings \(\tilde{\Delta}_c/\kappa\) while keeping _U_<sub>Q</sub> fixed. This can be achieved by adjusting the pump strength \(\eta\) correspondingly. In this case the de

(a) 1.00 (b) 0.75 0.50 Fsol (r) 0.25 0.00 0
20 40 0
200 400 Jt/h /k

Figure 6: _Comparison to open system dynamics. -_ (a) The figure shows the fidelity _F_<sub>sol</sub> between the solution and the instantaneous eigenstate (black dotted), and between solution and dynamical state from the time evolution using the Schrödinger equation (blue), classical fields (green) and the open system (red). The open system fidelity depends on \(\tilde{\Delta}_c/\kappa\), where we present results for the values 5,50,100,200,500,1000 (from light red to dark red). (b) The fidelity between solution and the final state after the sweep as a function of \(\tilde{\Delta}_c/\kappa\) for the curves of (a), where the colors are the same as in (a). The parameters used here are as in Fig. 5.

