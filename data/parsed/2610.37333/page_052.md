<tbc>with the Kozeny-Carman permeability \(\kappa_p=d_p^2\varepsilon^3/[150(1-\varepsilon)^2]\) and the Vortmeyer-Schuster wall porosity \(\varepsilon(\delta)=\varepsilon_b+(1-\varepsilon_b)e^{-N\delta/d_p}\) at the distance \(\delta\) from the nearest wall, for a particle diameter _d<sub>p</sub>=W/_6, a bulk porosity \(\varepsilon_b=0.4\), _N_=5 and \(\mu_\mathrm{eff}/\mu=8\), scaled to unit mean (Figure 14). The dispersion coefficients follow from particle Péclet numbers of 2 axially and 10 radially, the reactant enters through a Danckwerts flux condition at the inlet and leaves with zero gradient at the outlet, the walls carry no flux, and advection is discretized with central fluxes. The reaction uses \(\bar{k}=0.22U/W\) and _K_=0.05_c_<sub>in</sub>.

The true activity is a log-normal random field with correlation length 0.25_W_ and standard deviation 0.3 in ln_k_, multiplied by a smooth poisoning front that follows the velocity profile and by a cylindrical streak of low- activity pellets at 30% of the surrounding activity. The dataset was generated from an empty bed, saved at every cell at eight times from _t_=1 to 8 and corrupted with Gaussian noise of standard deviation 0.01_c_<sub>in</sub>. The WIRE network has three hidden layers of width 192 with wavelet parameters \(\omega_0=10\) and _s_<sub>0</sub>=5. The network was trained for 1200 steps on one NVIDIA L40S with the AdamW optimizer \[101\] in `optax` \[52\], every step integrating the model as a single trajectory from _t_=0 with `JNDF` and `cuDSS` in Float32 precision at rtol=10<sup>-5</sup> and atol=10<sup>-6</sup> and using the discrete checkpointed adjoint. The model, the truth, the data generation and the training scripts are in the companion repository named in the data availability statement.

Z
X
0.0
0.5
1.0
1.5
2.0
Ux/U

Figure 14: The superficial velocity profile _u<sub>x</sub>(y,z_) of the packed bed from Eq. (26), which channels the flow along the walls.

