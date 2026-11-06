If we set _U_<sub>D</sub> to 5_J_ and _U_<sub>T</sub> to 2_J_ we find that for _U_<sub>Q</sub>=1_J_ the overlap is _F_≈0.93 and the minimal gap is around 0.44_J_. These values were used for Figs. 2 and 3.

## B Derivation of the effective Hamiltonian

The derivation essentially follows App. C in Ref. \[40\], generalized to two dimensions and additionally including cavity-induced tunneling (see also e.g. Ref. \[54\]). Including the decay of the cavity fields through the mirrors with the rates \(\kappa_m\), the full open-system dynamics in the tight binding limit is given by the Lindblad equation

\(\dot{\rho}=-\frac{i}{\hbar}[\tilde{H},\rho]+\sum_m\kappa_m(2a_m\rho a_m^\dagger-a_m^\dagger a_m\rho-\rho a_m^\dagger a_m),\) (38)

where \(\tilde{H}\) is specified in Eq. (10). The important term for the following discussion discussion is the atom-light interaction _H_<sub>cav</sub> given in Eq. (11).

From this master equation we obtain the Heisenberg-Langevin equations of the cavity fields

\(\dot{a}_m=(i\tilde{\Delta}_{c,m}-\kappa_m)a_m-iN\eta_m\hat{\Theta}_m+\sqrt{2\kappa_m}\hat{\xi}_m\) (39)

with the quantum noise operator \(\hat{\xi}_m\) obeying \([\hat{\xi}_m(t),\hat{\xi}_m^\dagger(t')]=\delta(t-t')\).

Assuming that the cavity mode fields evolve on a much faster time scale than the atomic motion \((J/(\hbar|\tilde{\Delta}_{c,m}+i\kappa_m|)\checkmark 1)\), they can be approximated by their steady state on a coarse grained time scale \[40, 54, 57, 58\]. From the Heisenberg-Langevin equation, to zeroth order in \(J/(\hbar|\tilde{\Delta}_{c,m}+i\kappa_m|)\), we get

\(a_m^\mathrm{st}\equiv\frac{\eta_m}{\tilde{\Delta}_{c,m}+i\kappa_m}N\hat{\Theta}_m+\sqrt{\frac{2\kappa_m}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}}\hat{\xi}_m\) (40)

with \(\hat{\Theta}_m=\frac{1}{N}\sum_{i,j=1}^N\left(v_m^{ij}\hat{n}_{ij}+u_m^{ij}\hat{B}_{ij}\right)\). That is, at steady state the effect of the field can be expressed by atomic operators only.

We now substitute the cavity field operators by their corresponding steady-state approximations in

(a) Minimal Gap (b) Overlap | 10 xJ 10 8
0.5 8
0.8 0.4 6
0.3 6
0.6 4
0.2 4
0.4 UTJ 2
0.1 2
0.2 0
0.0 0.5 1.0 0.0 2.5 5.0 UQ/UD UQ/J

Figure 8: _Discussion of the impact of parameter values._ - (a) The minimal gap of the energy spectrum for the sweep as a function of the final parameters. _U_<sub>D</sub> is fixed to 5_J_ and _U_<sub>Q</sub> is varied. For the discussion on fidelity \[subplot (b)\] we choose _U_<sub>T</sub>=2_J_ which is indicated by the black line. The values of _U_<sub>T</sub> are non-zero to avoid degenerate ground states. We choose an instance with parameter values denoted by the red dot. (b) The overlap defined in Eq. (37). The black line indicates the fixed value of _U_<sub>D</sub> for subplot (a) and the red dot indicates the chosen set of parameters as before.

