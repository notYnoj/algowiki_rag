terms containing \(\hat{n}_{ij}\hat{n}_{kl}\) and a modified tunneling amplitude due an occupation or a tunneling event somewhere else in the lattice due to \(\hat{n}_{ij}\hat{B}_{kl}\), \(\hat{B}_{ij}\hat{n}_{kl}\) and \(\hat{B}_{ij}\hat{B}_{kl}\). While the density-density interactions constitute the problem Hamiltonian [see Eq. (3)], the latter cavity-induced tunneling terms lead to non-local fluctuations which might help to speed up the annealing process [46].

Since the Wannier functions are localized at the lattice sites, the on-site overlaps \(v_m^{ij}\) tend to be much larger than the nearest-neighbor overlaps \(u_m^{ij}\). Thus density-density interactions are expected to be the dominant contribution to \(H_\mathrm{cav}^\mathrm{eff}\). As intuitively expected, the atoms localize stronger for deeper lattices, where analytical expressions for the overlaps can be obtained within a harmonic approximation of the potential wells leading to Gaussian Wannier functions with a width \(\propto(V_\mathrm{L}^x)^{-1/4}\). Apart from a correction factor due to this width, the on-site overlaps are given by the pump fields at the lattice sites. The nearest-neighbor overlaps correspond to the pump fields in between the lattice sites, but are exponentially suppressed (see Appendix C). Consequently, in the deep lattice limit (large \(V_\mathrm{L}^x\)) when the width tends to zero we get \(v_m^{ij}=h_m(x_i,y_j)\) and \(u_m^{ij}=0\) [28], and an interaction Hamiltonian [from Eq. (16)]

\(H_\mathrm{cav}^\mathrm{dl}=\hbar\sum_m\frac{\tilde{\Delta}_{c,m}\eta_m^2}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}\times\sum_{ijkl}h_m^*(x_i,y_j)h_m(x_k,y_l)\hat{n}_{ij}\hat{n}_{kl},\) (17)

which only depends on density operators, and hence does not include cavity induced-tunneling.

## 3.2 _N_-queens interaction

In this section we aim to find pump fields _h<sub>m</sub>(x,y_) such that the interaction Hamiltonian in the deep lattice limit Eq. (17) corresponds to the desired queens Hamiltonian _H_<sub>Q</sub> [Eq. (3)] containing the non-attacking conditions. Using these pump fields we later show numerically in Sec. 4, that the atom-atom interaction for realistic lattice depths [Eq. (16)], although slightly altered, still well resembles the queens interaction.

We consider three sets of _M_ parallel running wave laser beams with different propagation directions, each of which could be created by a frequency comb. The three directions are perpen

dicular to the lines along which queens should not align, that is along the _x_-direction and along the diagonals. We denote the corresponding wave vectors with \(\mathbf{k}_m^x=(k_m^0,0)^T\), \(\mathbf{k}_m^+=(k_m^0,k_m^0)^T\) and \(\mathbf{k}_m^-=(k_m^0,-k_m^0)^T\), respectively, with the wave numbers \(k_m^0\). Therefore the pump fields are given by

\(h_m(x,y)=e^{i\mathbf{k}_m\mathbf{x}},\) (18)

where **_x_**=(_x,y)<sup>T</sup>_ is the position vector and **_k_**_<sub>m</sub>_ is a wave vector in any of the three directions.

With running wave pump fields, Eq. (17) can be written as

\(H_\mathrm{cav}^\mathrm{dl}=U_\mathrm{Q}\sum_{ijkl}\tilde{A}_{ijkl}\hat{n}_{ij}\hat{n}_{kl}.\) (19)

This formally corresponds to _H_<sub>Q</sub> [Eq. (3)], where the quantities now have a physical meaning: The interaction matrix is given by

\(\tilde{A}_{ijkl}=\sum_mf_mcos(\mathbf{k}_m(\mathbf{x}_{ij}-\mathbf{x}_{kl}))\) (20)

with lattice site connection vectors **_x_**_<sub>ij</sub>_-**_x_**_<sub>kl</sub>_ and

\(f_mU_\mathrm{Q}=\hbar\frac{\tilde{\Delta}_{c,m}\eta_m^2}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}\) (21)

with \(\sum_{m=0}^{M-1}f_m=1\). The dimensionless parameters _f<sub>m</sub>_ capture the relative strengths of the modes, determining the shape of the interaction. They have to be chosen such that \(\tilde{A}\) approximates _A_ [Eq. (4)]. The overall strength of the interaction term is captured by the energy _U_<sub>Q</sub>, which can be easily tuned by the cavity detunings or the pump intensities to implement the parameter sweep in Eq. (1). For the following discussion we define an interaction function

\(\tilde{\mathcal{A}}(\mathbf{r})=\sum_mf_mcos(\mathbf{k}_m\mathbf{r})\) (22)

which returns the interaction matrix when evaluated at lattice site connection vectors \(\tilde{A}_{ijkl}=\tilde{\mathcal{A}}(\mathbf{x}_{ij}-\mathbf{x}_{kl})\).

We note that one set of parallel \(\mathbf{k}_m^\mu\) (\(\mu\in\{x,+,-\}\)) creates an interaction \(\tilde{\mathcal{A}}\) which is constant and infinite range (only limited by the laser beam waist) in the direction perpendicular to the propagation direction \(\mathbf{r}\perp\mathbf{k}_m^\mu\). Along the propagation direction \(\mathbf{r}\|\mathbf{k}_m^\mu\) instead, the interaction is shaped according to the sum of cosines, and can be modified by the choice of wave numbers \(k_m^\mu=|\mathbf{k}_m^\mu|\) and their relative strengths _f<sub>m</sub>_.

