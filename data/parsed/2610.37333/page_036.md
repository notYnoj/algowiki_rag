<tbc>10<sup>4</sup> degrees of freedom. We demonstrate up to a \(50\times\) speedup over the next fastest solver at scale. This performance is explained by using GPUs to overcome the predominant bottlenecks in stiff implicit integration, namely Jacobian computation and factorization of the pencil matrix _W_.

In `diff-soup`, we employ a parallelized, sparse colored Jacobian computation \[70, 72\]. By contrast, all other compared solvers, except `DifferentialEquations.jl`, must be supplied an analytical sparse Jacobian, as done in this benchmark (Section 7.1). `DifferentialEquations.jl` supports sparse automatic differentiation by Jacobian coloring; however, it evaluates the colors serially and remains slower than the analytical Jacobian computation, as shown in  3.

On the CPU, the residual and automatic differentiation operations quickly become memory bound, so every color of the serial sweep costs a full residual evaluation, and the sparse autodiff Jacobian runs up to an order of magnitude slower than the analytical one. Batching offers at most a modest gain, since the cores are already saturated. To compensate, CPU codes can rely on<tbc>

\begin{tabular}{cccccc}
 & & \multicolumn{2}{c}{Brusselator, _N_=128} & \multicolumn{2}{c}{Cahn-Hilliard, _N_=64} \\
Computation & Device & Time (ms) & Ratio & Time (ms) & Ratio \\
_Residual evaluation_ & & & & & \\
`DifferentialEquations.jl` & CPU & 0.31 & - & 0.15 & - \\
`diff-soup` & CPU & 0.125 & - & 0.27 & - \\
`diff-soup` & GPU & 0.072 & - & 0.125 & - \\
_Analytical Jacobian_ & & & & & \\
`DifferentialEquations.jl` & CPU & 0.46 & - & 7.3 & - \\
`diff-soup` & CPU & 0.37 & - & 5.0 & - \\
`diff-soup` & GPU & 0.052 & - & 0.154 & - \\
_Sparse autodiff Jacobian_ & & & & & \\
`DifferentialEquations.jl`, & CPU & 4.6 & 10 & 10.4 & 1.4 \\
serial & & & & & \\
`diff-soup`, serial & CPU & 2.1 & 5.9 & 29 & 5.8 \\
`diff-soup`, batched & CPU & 0.99 & 2.7 & 30 & 6.0 \\
`diff-soup`, batched & GPU & 0.12 & 2.4 & 0.35 & 2.3 \\
\end{tabular}

3: Wall time of one residual evaluation, one analytical Jacobian assembly, and one sparse autodiff Jacobian assembly at the work-precision sizes of the two benchmark problems. Ratios are taken against the analytical Jacobian of the same framework on the same device, and the coloring uses 12 and 67 colors in `DifferentialEquations.jl` and 14 and 73 in `diff-soup` for the Brusselator and the Cahn-Hilliard problem, respectively.

