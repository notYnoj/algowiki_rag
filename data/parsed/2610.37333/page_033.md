_v_=3. Under these conditions, the system exhibits stiffness from the diffusion term, the nonlinearity, and the oscillatory behavior visible in Figure 6.

To stress-test the solvers, we select the fourth-order Cahn-Hilliard problem coupled to mechanical equilibrium, inspired by the elastic precipitate benchmark of the PFHub phase-field community \[94, 98\], defined as follows:

\(\frac{\partial\eta}{\partial t}=\nabla\cdot(M\nabla\mu),0=\mu-f'_\mathrm{bulk}(\eta)-\frac{\partial f_\mathrm{el}}{\partial\eta}+\kappa\nabla^2\eta,0=\nabla\cdot\sigma,\sigma=C(\eta):\left(\varepsilon-\varepsilon^0(\eta)\right),\text{(20)}\)

where \(\eta\) is the conserved order parameter, \(\mu\) is its chemical potential, _M_ is the mobility, _f_<sub>bulk</sub> is the bulk free energy, \(\kappa\) is the gradient energy coefficient, \(\varepsilon=\mathrm{sym}(\nabla\mathbf{u})\) is the strain of the displacement **u**, \(\varepsilon^0(\eta)\) is the dilatational misfit strain of the transformed phase, \(C(\eta)\) is the stiffness interpolated between the two phases, and _f_<sub>el</sub> is the elastic energy density. We use an initial condition of two cosine modes with wavelengths near the most unstable wavelength, and integrate the system for \(t\in[0,36]\) s on a \(50\times 50\) nm square domain. This problem is an index-1 DAE with both local differential and algebraic states, and it exhibits significant stiffness due to the fourth-order spatial derivative, the nonlinearity, and the unstable spatial modes shown in Figure 7. The full problem statement and its parameters are given in Section 7.1.

(a)
t= 0
t= 2.51
t= 5.03
t= 7.49
t= 10
1.5
>
1.0
0.5
(b)
3.5
>
3.0
2.5

Figure 6: Solution of the two-dimensional Brusselator benchmark, the species _u_ (a) and _v_ (b) on a \(128\times 128\) grid at five times from _t_=0 to 10, each row on its own color scale.

