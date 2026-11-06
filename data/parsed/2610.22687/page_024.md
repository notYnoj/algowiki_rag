<tbc>In Figure 20 this batching is shown for an AMD EPYC 9654 CPU and an NVIDIA H100 GPU, showing that up to thousands of MDAs can be computed in the same time as a single evaluation on the GPU. Furthermore, for the stellarator, over two hundred thousand MDA Jacobians can be computed per second.

The computational speedup can in principle be obtained from a combination of four effects: compilation of all models, compilation of the graph, autodiff versus finite differences, and MDAO architecture changes. Finite differences have been tested using `cottax` and are almost identical for execution speed (as these problems are close to square and with a relatively low number of design variables, forward mode was used which has similar computational costs; reverse mode is also supported) and convergence (within a few iterations of automatic differentiation). To somewhat isolate the effect of the removal of the `cottax` machinery from the evaluation during compilation, it is also run in interpreted mode for `stellarator\_helias`, compiling each model individually while not compiling `cottax` execution itself (which thus runs in interpreted Python). This results in an evaluation of around 10 ms -- compilation of the graph orchestration (i.e. removing per-model JAX dispatch and `cottax` interpreted Python graph traversal) provides a large speedup (40\(\times\)) in this case (requirement 5). The remaining 30 ms difference compared to PROCESS is a combination of architecture changes and model-level JIT. Other configurations have similar absolute timing differences of around 10 ms between interpreted and compiled modes.

## C. Summary

The systems code PROCESS has been converted to a purely functional form that contains only the models (physics, engineering, and costing) themselves -- not the solvers or any other form of coordination.

These models have been wrapped in `cottax` and sequenced, showing that only three small components (\(\le\) 9 models) remain. For seven configurations (different models, parametrisations, and problem formulations, with less than half of the models shared between tokamaks and stellarators), the automated MDAO architecture definition runs and converges to the same values for two to three different MDAO architectures, demonstrating the required arbitrary design problems (requirement 1) and the automated coordination (requirement 2).

No single architecture is in all cases the best-performing, motivating the MDAO architecture flexibility (requirement 3).

Differentiation, required for the gradient-based optimisation of the drivers, is performed using automatic differentiation and implicit differentiation, demonstrating requirement 4 for PROCESS.

stellarator_helias
helias_5b
large_tokamak_nof
large_tokamak_eval
105
104
103
wall time (ms)
102
101
100
low_aspect_ratio_DEMO
spherical_tokamak_eval
st_regression
105
104
port, CPU (batched)
103
wall time (ms)
port, GPU (batched)
102
evaluation
101
Jacobian
100
100
101
102
103
104
105
100
101
102
103
104
105
100
101
102
103
104
105
N
N
N

Figure 20: Wall times for _N_ evaluations of the MDA within the MDF structure (i.e. resolving the coupling but not optimising) for all seven configurations for the batched port (using `vmap`) using CPU (blue circle, AMD EPYC 9654) and GPU (orange square, NVIDIA H100). Solid lines are evaluations, dashed lines Jacobians.

