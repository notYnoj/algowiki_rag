<tbc>control-flow choices.

We summarize the computational cost, memory footprint, accuracy, and stability concerns of the four sensitivity algorithms in  2. None of the four algorithms returns the exact gradient of Eq. (9), though the source of the error differs between the two families. The continuous methods approximate the gradient of the continuous problem to a tolerance, with error governed by the tolerances of the selected forward solver, sensitivity solver, and quadrature method\[84, 78\]. The discrete methods differentiate the frozen discretization selected by the forward solve exactly, to floating point precision, and their gradients deviate from that of the adaptive solution map by a term controlled by the local error tolerance.

\begin{tabular}{ccccc}
 & FSA & Forward AD & ASA & Reverse AD \\
Cost & \(O(n_\theta T(n))\). Tangents share the pencil factorization. & \(O(n_\theta T(n))\). Tangents batched into multi-RHS solves with `jax.vmap`. & \(O(T(n)+n_\theta)\). One backward solve plus quadrature. & \(O(T(n)+n_\theta)\). A constant recomputation overhead from checkpointing. \\
Memory & \(O(n_\theta n)\) live tangents. No trajectory storage. & \(O(n_\theta n)\) live tangents. No trajectory storage. & Dense interpolant of _O(n_<sub>steps</sub>_n_), or checkpoint- reduced. & \(O(\sqrt{n_\mathrm{steps}}n)\) checkpoints by default; budget prescribable. \\
Gradient computed & Continuous sensitivities, accurate to the integration tolerances. & Exact tangents of the realized discretization under frozen controls. & Continuous gradient, accurate to the forward, adjoint, and quadrature tolerances. & Exact gradient of the realized discretization under frozen controls. \\
Stiffness concerns & Inherits the stability of the forward solve. & Inherits the stability of the forward solve. & The adjoint system is itself stiff, and backward re- integration of the state is unstable. & Stable. Replays stored or recomputed forward states. \\
\end{tabular}

2: Comparison of the four sensitivity methods for the PDE-constrained optimization problem of Eq. (9). _T(n_) denotes the cost of one forward VSVO solve under the sparse methods of this section, so no entry incurs a dense cubic factorization. Costs and memory are reported in the state dimension _n_, the parameter count \(n_\theta\), and the user-prescribed step ceiling _n_<sub>steps</sub>. The discrete methods differentiate the realized discretization under frozen step size and order controls.

