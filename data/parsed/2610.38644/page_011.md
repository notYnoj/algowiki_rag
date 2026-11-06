The corrector uses the blockwise collocation budgets

\(N_\mathrm{low}=10,N_\mathrm{mid}=20,N_\mathrm{high}=30.\) (43)

The residual normalization and refinement decisions are performed separately for each time slab. Consequently, the corrector collocation count varies with the residual distribution.

Collocation points in both stages are generated using a deterministic two-dimensional Halton sequence with bases 2 and 3. Within each spatial block, the first _N<sub>b</sub>_ Halton points are mapped to the corresponding spatial and local-time intervals, where _N<sub>b</sub>_ is the prescribed blockwise point budget.

The Stage 2 corrector combines this residual-guided collocation enrichment with narrower prescribed global and local Gaussian kernel widths. The kernel representer sites coincide with the PDE collocation locations in both stages.

## 2.6 Sequential space-time-slab formulation

For time-dependent PDEs, CFKS can be applied sequentially over consecutive space-time slabs rather than constructing a single kernel approximation over the entire temporal domain. This strategy reduces the size of the individual space-time problems and allows the solution to be advanced through a sequence of local temporal intervals.

Let \(\Omega_x\) denote the spatial domain and [_t_<sub>0</sub>_,T_] the temporal interval, where _t_<sub>0</sub> is the initial time and _T_ is the final time. The temporal interval is partitioned into _N<sub>T</sub>_ consecutive slabs,

\(I_n=[t_n,t_{n+1}],n=0,\dots,N_T-1,\) (44)

where _n_ is the slab index, _N<sub>T</sub>_ denotes the total number of slabs, and the partition points satisfy

\(t_0<t_1<\cdots<t_{N_T}=T.\) (45)

The duration of slab _n_ is \(\Delta t_n=t_{n+1}-t_n>0\).

Within each slab, the physical time coordinate is replaced by the local coordinate

\(\tau=t-t_n,0\le\tau\le\Delta t_n,\) (46)

where \(\tau=0\) and \(\tau=\Delta t_n\) correspond to the beginning and end of the current slab, respectively.

The CFKS approximation on slab _n_ is denoted by \(u_n(\mathbf{x},\tau)\), where **x** represents the spatial coordinates. The governing PDE is enforced at selected collocation points within the corresponding space-time region \(\Omega_x\times(0,\Delta t_n]\). The same continuum-feature kernel formulation developed in the preceding sections applies to each slab.

The local coordinate system permits the same analytical mean-kernel construction to be used across different slabs. When the slab durations, local collocation configurations, and prescribed kernel parameters are identical, the corresponding kernel matrices and analytical derivative evaluations may also be reused.

### Sequential transfer of the solution

The initial condition for each slab is obtained from the prescribed initial data or from the terminal solution of the preceding slab.

Let _u_<sub>init</sub>(**x**) denote the prescribed initial profile at time _t_<sub>0</sub>. The sequential transfer condition is

\(u_n(\mathbf{x},0)=\left\{\begin{array}{ c c }
u_\mathrm{init}(\mathbf{x}), & n=0, \\
u_{n-1}(\mathbf{x},\Delta t_{n-1}), & n>0,
\end{array}\right.\) (47)

where \(u_{n-1}(\mathbf{x},\Delta t_{n-1})\) represents the terminal profile of the preceding slab.

Thus, each local space-time problem receives its initial data from the preceding time interval. The solution is advanced sequentially until the final time is reached.

The incoming profile may be imposed through discrete initial constraints or incorporated analytically into a constraint- compatible trial representation. In either case, the local approximation is constructed to match the prescribed incoming data according to the chosen constraint-enforcement procedure.

In numerical implementations, the terminal profile may be transferred directly or represented through an interpolation procedure. When interpolation is used, the incoming profile is an approximation of the preceding terminal solution, and the transfer accuracy becomes part of the overall temporal discretization error.

Within each slab, the CFKS representation remains global over the spatial domain. The temporal decomposition therefore does not introduce artificial spatial interfaces or require spatial domain decomposition.

