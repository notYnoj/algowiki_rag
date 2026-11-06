<tbc>are sensible: a block over winding-pack sizing, a block over plasma composition, and a block over poloidal field coil sizing.

To recover PROCESS optimisation mode, an optimiser conditional node is added with the design variables as unknowns and the objective and constraints as conditions: in this case, the plant pulse burn time is maximised and nineteen design variables are used (see Appendix C).

Then, as discussed in Section IIIE, an optimisation architecture can be defined in how the couplings in Figure 15 are cut and then resolved. First, everything is cut with minimal Gauss–Seidel (also in Figure 15). Then, in Figure 16, two choices are shown for combining and nesting: an MDF architecture and a SAND architecture (IDF has little meaning here because there are no implicit models and it would thus be the same as SAND).

As the costing models do not feature in the objective nor in the constraints, they are absent from the optimiser cycle and are therefore not iterated during optimisation. This was all fully automated: no hand-derived coupling or nesting was involved.

This exact same procedure is shown for the stellarator in Figures 17 to 19, with the same conclusion: it is almost entirely acyclic and only some small blocks are actually coupled.

These two configurations share only 70 models (out of 242 and 149 models) and have different objective functions and parametrisations (see Appendix C), showing that the coordination and automated MDAO architectures support an arbitrary model collection and parametrisation (requirements 1 and 2).

All diagrams are also available in HTML form for more detailed inspection at `https://timobogaarts.github.io/ process-dsm`.

build.wp_conductor_max_width
CUT
build.tf_outboard_mid
cicc_superconducting_tf_coil.tf_global_geometry
cicc_superconducting_tf_coil.superconducting_tf_wp_geometry
profiles.parameterisation.pedestal_on_axis_densities
profiles.density_profile
profiles.ne_profile_integral
profiles.parameterisation.pedestal_profile_values
CUT
fusion_rates
fusion_power_totals_mw
fusion_totals_no_beam
plasma_composition
plasma_inductance.volt_seconds
pf_coil.time_point_currents
pf_coil.waveform
pf_coil.sizes
CUT
pf_coil.inductance
pf_coil.turn_currents
pf_coil.volt_seconds
cs_coil.flux_swing
pulse.burn_time
tokamak
physics
fixed-point (u = g(u))

Figure 15: The strongly connected components (cycles) of Figure 14 and their minimal Gauss–Seidel cut to turn them into functionally acyclic blocks (which makes the entire graph functionally acyclic). Provenance is indicated by colour. The top cycle is a winding-pack toroidal coil sizer, the middle a plasma composition solver, and the last a poloidal field coil sizer.

