<tbc>Cholesky factorization, and a diagonally preconditioned CG--on max-flow instances spanning FEM, structural, and circuit graphs ( 5.2).

The result is modularity, not a winner: every inner solver that converges returns the identical _F_<sup>∗</sup> to solver tolerance, so the continuation is genuinely solver-agnostic. The distinction that matters is near-linear versus not: the exact factorization is fastest where it fits but exhausts memory past ∼150k poorly-separable nodes (`G2\_circuit`, `sccircuit`), exactly the regime where a near-linear inner solve is mandatory, while the diagonal-PCG baseline--no coarse correction--is typically up to two orders of magnitude slower and the least scalable. Among the near-linear solvers, approximate Cholesky and LAMG+ are interchangeable in robustness; approximate Cholesky often carries the smaller constant. The single stiff case (`bcsstk38`) is instructive: there _all_ iterative inner solves stall and only the exact factorization reaches _F_<sup>∗</sup>--the deflation removes the _global_ cut singularity but not the residual ill-conditioning of the deflated system, for which an exact inner solve is still required.

**6. Multicommodity congestion.** §4 established the formulation and the O(_m_) solver for a single commodity. This section extends both, end to end, to _K_ simultaneously routed commodities: a vector edge law that couples the commodities through shared congestion (§6.1), a solver that reuses Algorithm 3.1 and _one_ scalar inner setup (factor or hierarchy) for all _K_ commodities (§6.2), validation against an exact-Newton<tbc>

\begin{tabular}{ccccc}
graph & _n_ & _F_<sup>∗</sup> & grad_/F_<sup>∗</sup> & NLF_/F_<sup>∗</sup> \\
grid2d/16 & 256 & 4.973 & 0.20 & 1.0000 \\
grid3d/6 & 216 & 17.478 & 0.11 & 1.0000 \\
washington & 66 & 500.745 & 0.02 & 1.0000 \\
genrmf & 64 & 16.000 & 0.00 & 1.0000 \\
bottleneck & 40 & 1.000 & 1.00 & 1.0000 \\
\end{tabular}

(A) Per-edge cost flat near-O(m)
(B) O(1) continuation steps (flat in size)
14
grid2d
103
grid3d
12
random
102
10
time per edge (us/edge)
NLF grid2d
continuation steps to F
NLF grid3d
NLF random
8
mean = 6,7
101
NLF fit: t/m x m-0.11
Boykov-Kolmogorov
6
BK fit: t/m x m-0.08
100
4
2
10-1
0
102
103 edges m
104
102
103 edges m
104

5.1

_NLF recovers the true max-flow exactly; the gradient/electrical relaxation falls far short. F_<sup>∗</sup>_: LP over free flows and push-relabel agree to_ 10<sup>-4</sup>_; **washington** and **genrmf** are DIMACS-challenge generators \[22\]._

Fig. 5.1. _Max-flow scaling (whole algorithm, total wall-clock), on 2D/3D grids and random graphs to_ ∼10<sup>4</sup> _edges, all exact at F_<sup>∗</sup>_. (A)_ Per-edge _cost: nearly flat (_ \(t\propto m^{1.00}\)_, empirically_ O(_m)) at_ ≈1.4_ms/edge, the constant set by the per-step hierarchy rebuild; Boykov-Kolmogorov sits far below at_ \(\approx 0.17\mu s\)_/edge (calibration only). (B) The continuation is_ O(1)_: pseudo-arclength steps_

_are flat in size (mean_ 6.7_)._

