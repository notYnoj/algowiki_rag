least on the order of the lattice wave number \(\Delta k_\mathrm{BW}\unknown k_\mathrm{L}\).

## 4 Numerical justification of assumptions

We compare the ideal model Hamiltonian described in Sec. 2 [Eq. (1)] to the physically motivated tight-binding Hamiltonian for finite lattice depths introduced in Sec. 3 [Eq. (10)]. As for the ideal model in Fig. 2, we consider the time evolution during a slow linear sweep of _U_<sub>Q</sub>, _U_<sub>T</sub> and _U_<sub>D</sub> by numerically integrating the time- dependent Schrödinger equation. Physically, this sweep can be realized by ramping up the pump and the bias field intensities. Moreover, we show that evolving the system using a classical approximation for the cavity mode fields does not result in a solution to the _N_-queens problem, and address the effect of dephasing by photon loss with open system simulations.

In the following we use a realistic lattice depth of \(V_\mathrm{L}^x=10E_\mathrm{R}\) with the recoil energy \(E_\mathrm{R}=\hbar^2k_\mathrm{L}^2/(2m_\mathrm{A})\). For example, for rubidium <sup>87</sup>Rb and \(\lambda_\mathrm{L}=785.3\mathrm{nm}\) it is \(E_\mathrm{R}/\hbar=23.4\mathrm{kHz}\) [26]. The chosen lattice depth leads to a tunneling amplitude _J_≈0.02_E_<sub>R</sub>, which can be obtained from the band structure of the lattice. We consider our cavity model in Eq. (10) for _N_=5. The pump modes are as in Sec. 3.2 and Fig. 4. While in the limit of a deep lattice this would result in the ideal model interactions, here they depend on the overlaps between Wannier functions and pump modes [Eq. (13)] and are thus altered. In the following the overlaps are calculated with Wannier functions which where numerically obtained from the band structure of the lattice. It turns out, that the deviation from the ideal overlaps does not qualitatively change the interaction for the realistic parameters used.

### 4.1 Coherent dynamics

The energy spectrum of the Hamiltonian for finite lattice depths in Eq. (16) is shown in Fig. 3(b) and is qualitatively of the same form as for the ideal model in Fig. 3(a). In comparison the eigenvalue gaps tend to be smaller at the end of the sweep. This is because the on-site atom- mode overlaps decrease for shallower lattices and less localized atoms due to a smoothing of the

mode functions by the finite width Wannier functions (see Appendix C). Moreover, we consider the time evolution during the nearly adiabatic sweep for \(J\tau/\hbar=49\) for the same parameters by integrating the time-dependent Schrödinger equation. Snapshots of the site occupations \(\langle\hat{n}_{ij}\rangle\) for several times are shown in Fig. 5(a), where we observe a similar behavior as for the model in Fig. 2. This suggests that the system is robust against the errors introduced by the moderate lattice depth. Note that the physical Hamiltonian used here is non-stoquastic in the occupation basis due to cavity-induced tunneling.

### 4.2 Classical cavity fields

In the following we show that quantum correlations are crucial for the efficiency of the sweep. In particular, if we substitute the field operators \(a_m^\mathrm{st}\) by its expectation values representing classical cavity fields the solution is not found. We

(a) Jt/h = 0 Jt/h = 7 Jt/h = 14 Jt/h = 21 Site occupations (nij) 1.0 0.8 0.6 Jt/h = 28 Jt/h = 35 Jt/h = 42 Jt/h = 49 0.4 0.2 0.0 x
(b) Jt/h = 0 Jt/h = 7 Jt/h = 14 Jt/h = 21 Site occupations (nij) 1.0 0.8 0.6 Jt/h = 28 Jt/h = 35 Jt/h = 42 Jt/h = 49 0.4 0.2 y
0.0

Figure 5: _Comparison of the time evolution with quantum and classical fields._ - Lattice site occupations for a time evolution during a nearly adiabatic sweep using the cavity Hamiltonian including cavity-assisted tunneling for the same parameters as in Fig. 2. Subplot (a) shows the dynamics using the full quantum interaction Hamiltonian [Eq. (16)]. It closely resembles the results from the model Hamiltonian in Fig. 2. Subplot (b) shows the time evolution with the classical approximation of the cavity fields [Eq. (27)]. The state does not converge to the solution, also not for much larger sweep times. The modes for both cases where chosen as in Fig. 4(b).

