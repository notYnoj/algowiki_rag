in the cavity _NU_<sub>0_,m_</sub> \[24\].

Note that, for example by placing the optical lattice (_x-y_-plane) in a common anti-node of the standing wave cavity modes and exciting only TEM<sub>00</sub> modes, the atom-cavity coupling is uniform in space in our model. Thus the only spatial dependence in the cavity term is due to the pump fields.

_Generalized Bose-Hubbard Hamiltonian._ The atom-atom interactions are taken into account by introducing bosonic field operators \(\hat{\Psi}(x)\) with \(\tilde{H}=\int\mathrm{d}^2x\hat{\Psi}^\dagger(x)H_1\Psi(x)\) \[25, 55\]. Note that we do not include contact interactions since atoms never meet due to the initial condition we will use. We assume that the optical lattice with depths \(V_\mathrm{L}^x\) and \(V_\mathrm{L}^y\) is so deep, that the atoms are tightly bound at the potential minima and only the lowest vibrational state (Bloch band) is occupied. Moreover, the optical potential created by bias and cavity fields is comparably small, such that the form of the Bloch wave functions only depends on the optical lattice \[54\]. In this limit we can expand the bosonic field operators in a localized Wannier basis \(\hat{\Psi}(x)=\sum_{i,j}w_{2D}(x-x_{ij})b_{ij}\) with the lowest-band Wannier functions _w_<sub>2_D_</sub>(**_x_**) coming from Bloch wave functions of the lattice \[56\]. We split the resulting Hamiltonian in three terms

\(\tilde{H}=H_\mathrm{kin}+H_\mathrm{cav}+H_\mathrm{pot},\) (10)

which will be explained in the following.

As in the standard Bose-Hubbard model, one obtains a tunneling term _H_<sub>kin</sub> as in Eq. (2). Tunneling in _y_-direction is frozen out by ensuring \(V_\mathrm{L}^y\gg V_\mathrm{L}^x\). The other terms _H_<sub>cav</sub> and _H_<sub>pot</sub> originate from the weak cavity-pump interference fields and the bias fields introduced above and should resemble _H_<sub>pr</sub> \[Eq. (8)\]. In order to realize the sweep Eq. (1), the relative strength of these terms and the kinetic term has to be tuned, e.g. by ramping up the pump laser and bias field intensity (make _H_<sub>cav</sub> and _H_<sub>pot</sub> larger) or the lattice depth (make _H_<sub>kin</sub> smaller).

The cavity-related terms in Eq. (9) give rise to

\(H_\mathrm{cav}=-\hbar\sum_m\tilde{\Delta}_{c,m}a_m^\dagger a_m+\hbar\sum_mN\eta_m\left(\hat{\Theta}_m^\dagger a_m+a_m^\dagger\hat{\Theta}_m\right)\) (11)

with the order operator of cavity mode _m_

\(\hat{\Theta}_m=\frac{1}{N}\sum_{i,j=1}^N\left(v_m^{ij}\hat{n}_{ij}+u_m^{ij}\hat{B}_{ij}\right).\) (12)

The structure of the fields enters in the on-site and nearest neighbor atom-mode overlaps

\(v_m^{ij}=\int dxw^2(x-x_i)h_m(x,y_j)\) (13)

\(u_m^{ij}=\int dxw(x-x_i)h_m(x,y_j)w(x-x_{i+1})\) (14)

where _y<sub>j</sub>=ja_ with _j_=0_,...,N_-1 are the tube positions and _w(x_) the one-dimensional Wannier functions in _x_-direction. This is because for \(V_\mathrm{L}^y\gg V_\mathrm{L}^x\) we can approximate the _y_- dependence of the Wannier functions by a Dirac delta: \(w_{2D}(x)=w(x)\delta(y)\).

The last term _H_<sub>pot</sub> describes all extra fields responsible for local energy off-sets at certain sites that stem from the weak classical fields with the distribution \(\mathcal{F}(x,y)\) (\(V_\mathrm{bias}\checkmark V_\mathrm{L}^x\)). The off-sets ought to be calculated from the overlaps of fields and Wannier functions, analogously to \(v_m^{ij}\). Thus the fields have to be chosen such that the resulting Hamiltonian resembles Eq. (5). We do not detail the derivation further here and use _H_<sub>pot</sub> for numerical simulations.

_Atom-atom interaction Hamiltonian._ The main focus of this work is to show how to create the tailored all-to-all particle interactions via collective scattering. We derive this interaction by eliminating the cavity fields introduced in the previous section \[54, 57, 58\]. This can be done because the cavity fields decay through the mirrors with the rates \(\kappa_m\) and thus end up in a particular steady-state for each atomic configuration. Assuming that the atomic motion is much slower than the cavity field dynamics, i.e. \(J/\hbar\checkmark|\tilde{\Delta}_{c,m}+i\kappa_m|\), this steady-state is a good approximation at all times. The stationary cavity field amplitudes are given by

\(a_m^\mathrm{st}\equiv\frac{\eta_m}{\tilde{\Delta}_{c,m}+i\kappa_m}N\hat{\Theta}_m\) (15)

and thus replaced by atomic operators (see Appendix B).

In the coherent regime \(|\tilde{\Delta}_{c,m}|\gg\kappa_m\), the atom- light interaction is then described by an effective interaction Hamiltonian for the atoms \[28\]

\(H_\mathrm{cav}^\mathrm{eff}=\hbar\sum_m\frac{\tilde{\Delta}_{c,m}\eta_m^2}{\tilde{\Delta}_{c,m}^2+\kappa_m^2}N^2\hat{\Theta}_m^\dagger\hat{\Theta}_m.\) (16)

The collective, state-dependent scattering induces interactions between each pair of sites (_i,j_) and (_k,l_): Density-density interactions due to the

