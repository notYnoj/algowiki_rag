Here, |Q_<sub>b</sub>_| is the number of probe points in block _b_, \(R_b^\mathrm{rms}\) measures the average residual magnitude, and \(R_b^\mathrm{max}\) measures the largest observed residual.

A normalized residual indicator is constructed by combining these measures:

\(s_b=\omega\frac{R_b^\mathrm{rms}}{\mathrm{max}_{1\le j\le N_B}R_j^\mathrm{rms}+\varepsilon}+(1-\omega)\frac{R_b^\mathrm{max}}{\mathrm{max}_{1\le j\le N_B}R_j^\mathrm{max}+\varepsilon},\) (40)

where _s<sub>b</sub>_ is the indicator for block _b_, \(\omega\in[0,1]\) is a prescribed weighting parameter, and \(\varepsilon>0\) prevents division by zero. The index _j_ runs over all blocks in the region being refined. The two terms measure, respectively, the relative average residual and the relative peak residual.

The indicator determines the refinement level assigned to each block. For a three-level strategy, define

\(\gamma_b=\left\{\begin{array}{ c c }
\mathrm{high}, & s_b\ge s_\mathrm{high}, \\
\mathrm{mid}, & s_\mathrm{mid}\le s_b<s_\mathrm{high}, \\
\mathrm{low}, & s_b<s_\mathrm{mid},
\end{array}\right.\) (41)

where \(\gamma_b\) denotes the refinement level, and _s_<sub>mid</sub> and _s_<sub>high</sub> are prescribed thresholds satisfying \(0\le s_\mathrm{mid}<s_\mathrm{high}\).

The levels correspond to prescribed collocation budgets _N_<sub>low</sub>, _N_<sub>mid</sub>, and _N_<sub>high</sub>. The number of PDE collocation points assigned to block _b_, denoted by _N<sub>b</sub>_, is selected according to its refinement level \(\gamma_b\). The total number of PDE collocation points after refinement is therefore

\(N_p^\mathrm{ref}=\sum_{b=1}^{N_B}N_b,\) (42)

where \(N_p^\mathrm{ref}\) is the total refined collocation budget.

Additional implementation rules may be introduced to avoid abrupt spatial changes in collocation density, such as extending high-refinement assignments to neighboring blocks. The particular thresholds, point budgets, and neighboring- block rules are selected for the numerical problem under study.

Once the blockwise budgets are determined, the refined PDE collocation locations are generated within the corresponding blocks. Deterministic low-discrepancy sequences provide one means of constructing these point sets without introducing random sampling.

For a prescribed continuum-feature mean kernel, residual-guided collocation refinement modifies the discrete PDE constraints but does not change the analytical kernel itself. If the kernel representer sites coincide with the collocation locations, as in the nonlinear implementation considered here, enrichment also changes the number of kernel coefficients.

Residual-guided collocation may additionally be combined with prescribed changes in Gaussian kernel widths or center distributions. In that case, the discrete collocation representation and the underlying kernel parameters are both modified.

In the viscous Burgers experiment, residual-adaptive collocation forms part of the second stage of a predictor-corrector procedure. Residual indicators computed from the completed predictor determine the corrector collocation distribution. The corrector also employs narrower prescribed kernel widths, so the resulting accuracy improvement cannot be attributed to collocation adaptation alone.

The numerical values used for the residual weights, refinement thresholds, probe distributions, and collocation budgets are specified with the corresponding test problem.

## Residual-adaptive collocation settings

The two-stage Burgers computation uses a deterministic predictor followed by a residual-guided corrector. The spatial interval is divided into 20 equal blocks. For each time slab, the predictor uses 10 PDE collocation points per block, giving 200 points per slab.

The predictor residual is evaluated independently on a tensor-product probe grid within each block, using 11 spatial locations and 7 local-time locations. Spatial probe positions extend from 5% to 95% of the block width, while the local-time positions range from \(0.08\Delta t\) to \(0.96\Delta t\), where \(\Delta t\) is the slab duration. Thus, each block contains 77 residual probes.

The residual indicator in eq. 40 uses \(\omega=0.7\), assigning weights of 0.7 and 0.3 to the root-mean-square and maximum residual measures, respectively. The refinement thresholds in eq. 41 are prescribed as _s_<sub>mid</sub>=0.10 and _s_<sub>high</sub>=0.35.

To reduce abrupt changes in collocation density, high- and medium-refinement assignments are extended to immediately adjacent spatial blocks. The expansion does not wrap around the domain boundaries, and high-refinement assignments take precedence where the expanded regions overlap.

