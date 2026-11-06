In Figure 5, we demonstrate that even for this simple parabolic problem, the discrete spectrum of the differential operator induces stiffness that makes the specialized VSVO stiff solver extremely advantageous. Specifically we<tbc>

(a)
error against resolution
(b)
cost against resolution
10-1
103
10-3
102
wall time (s)
10-5
101
error
10-7
100
10-1
10-9
101
102
103
104
102
103
104
degrees of freedom
degrees of freedom
N
(c)
cost against error
(d)
102
103
104
100
diff-soup JIDA, GPU (cuDSS)
103
diff-soup JIDA, CPU (KLU)
wall time (s)
102
wall time (s)
101
10-1
100
10-1
10-2
10-8
10-7
10-6
10-5
10-4
103
104
error
Jacobian nonzeros
diff-soup JIDA (cuDSS)
diffrax Tsit5
exactly integrated grid system
diffrax Kvaerno5
diffrax Euler (CFL)
analytic series on the grid

Figure 5: The one-dimensional heat equation solved at rtol = atol = 10<sup>-9</sup> with `diff-soup` and `diffrax` on grids from _N_=2<sup>6</sup> to 2<sup>14</sup> interior nodes. A maximum wall time of 1800 s is imposed on every timed cell of the benchmark comparisons, indicated by the dotted gray horizontal line. All problems are solved on the GPU in Float64 precision unless indicated otherwise. (a) Relative _L_<sup>2</sup> trajectory error against the continuous solution, with the exactly integrated grid system (black dashed) as the \(O(\Delta x^2)\) spatial floor and the analytic series truncated to the grid’s modes (gray dotted). At the same tolerance, `diff-soup` keeps descending to the finest grid and finishes an order of magnitude below `Kvaerno5`, whose error saturates at the largest sizes. (b) wall time against resolution. `diff-soup` stays flat at a sub-second cost, while the `diffrax` lanes grow as power laws, the implicit `Kvaerno5` approaching cubic scaling at the largest sizes. (c) The work-precision diagram, in which `diff-soup` gains accuracy at nearly constant cost while every `diffrax` lane pays a growing cost for each gain in accuracy. (d) The same `diff-soup` solver on the CPU with the KLU sparse linear solver and on the GPU with `cuDSS`, plotted against the Jacobian nonzeros and the degrees of freedom _N_. The crossover where the CPU cost exceeds the fixed overhead of the GPU solver occurs near \(1.4\times 10^4\) nonzeros and 4770 degrees of freedom.

