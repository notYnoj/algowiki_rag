the Heisenberg equation of the atomic annihilation operators

\(\dot{b}_{ij}=\frac{1}{i\hbar}[b_{ij},H_\mathrm{cav}]+\dots=-i\sum_m\frac{(N\eta_m)^2}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}\left[\tilde{\Delta}_{c,m}\left([b_{ij},\hat{\Theta}_m^\dagger]\hat{\Theta}_m+\hat{\Theta}_m^\dagger[b_{ij},\hat{\Theta}_m]\right)-i\kappa_m\left([b_{ij},\hat{\Theta}_m^\dagger]\hat{\Theta}_m-\hat{\Theta}_m^\dagger[b_{ij},\hat{\Theta}_m]\right)\right]-i\sum_m\frac{N\eta_m\sqrt{2\kappa_m}}{\sqrt{\tilde{\Delta}_{c,m}^2+\kappa_m^2}}\left([b_{ij},\hat{\Theta}_m^\dagger]\hat{\xi}_m+\hat{\xi}_m^\dagger[b_{ij},\hat{\Theta}_m]\right)\) (41)

where we only report terms including the cavity. At this point, ordering of atomic and field operators becomes important, since \(a_m^\mathrm{st}\propto\hat{\Theta}_m\) as opposed to _a<sub>m</sub>_ does not necessarily commute with atomic operators. Here we choose normal ordering, as already done in Eq. (11). The expression contains coherent terms proportional to \(\tilde{\Delta}_{c,m}\) and incoherent terms proportional to \(\kappa_m\).

For \(|\tilde{\Delta}_{c,m}|\gg\kappa_m\) we can neglect the incoherent part and the Heisenberg equation can be obtained from

\(\dot{b}_{ij}=\frac{1}{i\hbar}[b_{ij},H_\mathrm{cav}^\mathrm{eff}]+\dots\) (42)

Thus the dynamics in the coherent regime is described by the effective Hamiltonian \(H_\mathrm{cav}^\mathrm{eff}\) given in Eq. (16). Otherwise the Heisenberg equation is equivalent to the master equation (28).

The results can also be obtained by naively substituting _a<sub>m</sub>_ with \(a_m^\mathrm{st}\) directly in the Hamiltonian Eq. (11) or the master equation (38) with the given ordering.

Note that the effective Hamiltonian can also be written in the form

\(H_\mathrm{cav}^\mathrm{eff}=\hbar\sum_m\tilde{\Delta}_{c,m}(a_m^\mathrm{st})^\dagger a_m^\mathrm{st},\) (43)

which allows for a simple interpretation: For \(\tilde{\Delta}_{c,m}>0\) the lowest energy states tend to minimize the intensity of the cavity fields \(\langle(a_m^\mathrm{st})^\dagger a_m^\mathrm{st}\rangle\).

## C Harmonic approximation of potential wells

In this section we investigate the limit of a deep lattice in more detail. In Section 3.1 we presented results in the "infinitely" deep lattice limit, where the Wannier functions become delta functions. To gain more insight to deep but finite lattice depths, we use a harmonic approximation for the potential wells. The ground state wave function is then an approximation to the lowest-band Wannier function

\(w_\mathrm{har}(x)=\pi^{-\frac{1}{4}}a_0^{-\frac{1}{2}}e^{-\frac{x^2}{2a_0^2}}\) (44)

with the size _a_<sub>0</sub>=(_E_<sub>R</sub>_/V_<sub>L</sub>)<sup>1/4</sup>_/k_<sub>L</sub> \[55\].

With this the atom-mode overlap integrals \[Eq. (13)\] can be calculated analytically using running wave mode functions \[Eq. (18)\]. For the on-site term we obtain

\(v_m^{ij}=h_m(x_i,y_j)e^{-\left(\frac{k_m^x}{2k_\mathrm{L}}\right)^2}\sqrt{\frac{E_\mathrm{R}}{V_\mathrm{L}}}.\) (45)

It consists of the mode function at the lattice site and an exponential which reduces the overlap due to Gaussian smoothing of the mode function. As intuitively expected, the smoothing has a stronger effect for large mode wave numbers \(k_m^x\). For \(V_\mathrm{L}/E_\mathrm{R}\gg 1\), we obtain \(v_m^{i,j}=h_m(x_i,y_j)\), as in the main text.

For the off-site overlaps we obtain

\(u_m^{ij}=h_m((x_i+x_{i+1})/2,y_j)e^{-\left(\frac{k_m^x}{2k_\mathrm{L}}\right)^2}\sqrt{\frac{E_\mathrm{R}}{V_\mathrm{L}}}e^{-\frac{\pi^2}{4}}\sqrt{\frac{V_\mathrm{L}}{E_\mathrm{R}}}.\) (46)

