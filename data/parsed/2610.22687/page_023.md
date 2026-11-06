## B. Timing and results

Seven configurations (all shown explicitly in Appendix C) are then run and compared with the PROCESS results in terms of iterations and timing on the CPU (AMD EPYC 9654, Snellius Genoa) in  III.

The Jacobian of the objective function is computed with automatic differentiation in all configurations; the nested solvers are differentiated using implicit differentiation provided by Optimistix \[61\] (requirement 4). The evaluation is one to two orders of magnitude faster and the `cottax` Jacobian computation is two to three orders of magnitude faster than the finite differences used in base PROCESS. To make a fair comparison between base PROCESS and the `cottax` port, the model columns in  III show the time spent within the model during the optimisation -- excluding the overhead from the driver (VMCON or SLSQP) remaining in plain Python<sup>2</sup>. The total model time is two to three orders of magnitude less in `cottax`.

The ported functions converge to (within reasonable tolerance) the same optimum as PROCESS in all configurations. Furthermore, the MDF (which is the most similar to PROCESS’s own architecture) converges in the same or a smaller number of iterations (using VMCON). The table also motivates requirement 3: no architecture outperforms every other in all cases.

III: Iterations and timings of `cottax` under each MDAO architecture, beside PROCESS itself, for the seven regression-suite configurations of Appendix C: five optimisation configurations (top) and two evaluation configurations (bottom). IDF is listed only for the two stellarator configurations, the only ones with an implicit model. Each row gives the size of the outer problem (number of design variables _n_, equality constraints _m_<sub>eq</sub> and inequality constraints _m_<sub>ineq</sub>), the number of graph nodes within the optimiser (excluding the nodes not in the optimiser cycle), and the number of iterations per driver (\(\unknown\): converged). The optimisation drivers are VMCON \[66\] and SLSQP \[67\]; for evaluation, the port uses a differentiable Newton method \[5, 61\] and PROCESS uses Powell’s hybrid method \[62, 68\]. The eval and jac columns give the wall time of one evaluation and one Jacobian; each driver’s time column gives the wall time of the whole solve, and the model column the part of it spent in the models (the difference is the driver-internal computation). _f_<sup>∗</sup> is the objective at the optimum.

The analysis can be batched arbitrarily on the GPU: although this is not necessarily an optimal workload for the GPU, the trivial parallelism can yield significant speedups for a large number of batched evaluations. This could be useful for uncertainty quantification or database generation, since each analysis is in principle a consistent analysis.

<sup>2</sup> To the best of our knowledge, there currently is no JAX-compatible constrained optimisation algorithm available that converges reliably with the problems shown here; it would be a useful addition to the ecosystem allowing JAX transformations on optimisers. The overhead of the `cottax` wrapping is near-zero; the time difference is due to driver-internal time, and is significantly more in VMCON (Python-based) than in SLSQP (Fortran-based).

\begin{tabular}{cccccccccccccc}
 & \multicolumn{5}{c}{} & \multicolumn{3}{c}{iterations} & \multicolumn{5}{c}{wall time (ms)} & \\
Optimisation configuration & _n_ & _m_<sub>eq</sub> & _m_<sub>ineq</sub> & nodes & VMCON & SLSQP & eval & jac & VMCON & model & SLSQP & model & _f_<sup>∗</sup> \\
`stellarator\_helias` & & & & & & & & & & & & & \\
cottax MDF & 8 & 2 & 12 & 122 & \(\unknown\) 40 & \(\unknown\) 26 & 0.24 & 0.51 & 460 & 100 & 79 & 55 & 1.218 \\
cottax IDF & 11 & 5 & 12 & 120 & \(\unknown\) 47 & \(\unknown\) 16 & 0.24 & 0.54 & 550 & 110 & 53 & 29 & 1.218 \\
cottax SAND & 12 & 6 & 12 & 119 & \(\unknown\) 23 & \(\unknown\) 16 & 0.26 & 0.56 & 290 & 56 & 52 & 29 & 1.218 \\
PROCESS & 8 & 2 & 12 & - & \(\unknown\) 82 & - & 41 & 1100 & 180000 & 180000 & - & - & 1.215 \\
`helias\_5b` & & & & & & & & & & & & & \\
cottax MDF & 3 & 2 & 2 & 73 & \(\unknown\) 4 & \(\unknown\) 4 & 0.23 & 0.30 & 54 & 6.9 & 23 & 6.1 & 0.7642 \\
cottax IDF & 6 & 5 & 2 & 71 & \(\unknown\) 4 & \(\unknown\) 4 & 0.23 & 0.39 & 56 & 6.7 & 24 & 6.4 & 0.7642 \\
cottax SAND & 6 & 5 & 2 & 71 & \(\unknown\) 4 & \(\unknown\) 4 & 0.23 & 0.41 & 56 & 7.5 & 24 & 6.5 & 0.7642 \\
PROCESS & 3 & 2 & 2 & - & \(\unknown\) 4 & - & 44 & 440 & 3400 & 3100 & - & - & 0.7635 \\
`large\_tokamak\_nof` & & & & & & & & & & & & & \\
cottax MDF & 20 & 3 & 23 & 177 & \(\unknown\) 8 & \(\unknown\) 7 & 0.38 & 2.2 & 160 & 51 & 59 & 30 & 1.600 \\
cottax SAND & 26 & 9 & 23 & 173 & \(\unknown\) 9 & \(\unknown\) 9 & 0.37 & 2.2 & 190 & 67 & 77 & 50 & 1.600 \\
PROCESS & 20 & 3 & 23 & - & \(\unknown\) 8 & - & 21 & 1300 & 23000 & 22000 & - & - & 1.600 \\
`low\_aspect\_ratio\_DEMO` & & & & & & & & & & & & & \\
cottax MDF & 19 & 4 & 21 & 178 & \(\unknown\) 11 & \(\unknown\) 11 & 1.1 & 4.8 & 270 & 130 & 120 & 83 & -0.4063 \\
cottax SAND & 24 & 9 & 21 & 175 & \(\unknown\) 19 & \(\unknown\) 21 & 1.1 & 4.7 & 470 & 240 & 210 & 180 & -0.4063 \\
PROCESS & 19 & 4 & 21 & - & \(\unknown\) 16 & - & 27 & 1800 & 49000 & 48000 & - & - & -0.4063 \\
`st\_regression` & & & & & & & & & & & & & \\
cottax MDF & 14 & 3 & 15 & 154 & \(\unknown\) 10 & \(\unknown\) 11 & 0.35 & 1.1 & 160 & 41 & 55 & 30 & -16.59 \\
cottax SAND & 17 & 6 & 15 & 152 & \(\unknown\) 25 & \(\unknown\) 81 & 0.33 & 1.2 & 400 & 130 & 380 & 340 & -16.59 \\
PROCESS & 14 & 3 & 15 & - & \(\unknown\) 10 & - & 27 & 1200 & 25000 & 24000 & - & - & -16.59 \\
Evaluation configuration & _n_ & _m_<sub>eq</sub> & _m_<sub>ineq</sub> & nodes & Newton & Powell & eval & jac & Newton & model & Powell & model & \\
`large\_tokamak\_eval` & & & & & & & & & & & & & \\
cottax MDF & 2 & 2 & 0 & 34 & \(\unknown\) 3 & - & 0.17 & 0.23 & 11 & - & - & - & \\
PROCESS & 2 & 2 & 0 & - & - & \(\unknown\) 10 & 21 & 150 & - & - & 740 & 280 & \\
`spherical\_tokamak\_eval` & & & & & & & & & & & & & \\
cottax MDF & 3 & 3 & 0 & 38 & \(\unknown\) 2 & - & 0.17 & 0.27 & 9.7 & - & - & - & \\
PROCESS & 3 & 3 & 0 & - & - & \(\unknown\) 10 & 24 & 250 & - & - & 820 & 300 & \\
\end{tabular}

