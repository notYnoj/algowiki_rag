<tbc>baseline (full \(Kn\times Kn\) block solve, §6.3), and the same full-corpus robustness sweep as §4.5 (§6.5). The implementation is a modular layer over the single-commodity solver, which remains intact.

**6.1. tion: a vector edge law.** _K_ commodities ship demands \(\alpha d^1,\dots,\alpha d^K\) (\(\mathbf{1}^\top d^k=0\)) over one network; commodity _k_ has flow \(f^k\in\mathbb{R}^m\) and potential \(\phi^k\in\mathbb{R}^n\). Collect the per-edge flows into the vector \(\mathbf{f}_e=(f_e^1,\dots,f_e^K)\in\mathbb{R}^K\) and the per-edge potential gradients into \(\mathbf{g}_e=\big((B^\top\phi^1)_e,\dots,(B^\top\phi^K)_e\big)\). The modeling question is how the commodities couple through shared congestion. Three natural choices: the signed total \(\sum_kf_e^k\) (degenerate--collapses to single-commodity); the volume \(\sum_k|f_e^k|\) (classical but nonsmooth, forces a per-edge complementarity akin to the max-flow cut); and the Euclidean magnitude \(\|\mathbf{f}_e\|\) (smooth, strictly convex, reduces exactly to _K_=1). We take the third for this feasibility study; the volume-coupled and directed models remain future work (§7.1). The program is (2.3) with the congestion cost charged to the magnitude of the commodity-flow vector,

(6.1) \(min_{f^1,\dots,f^K}\sum_e\Phi_e\big(\|\mathbf{f}_e\|\big)\text{s.t.}Bf^k=\alpha d^k,k=1,\dots,K,\)

and stationarity gives, per edge, the _vector law_

(6.2) \(\mathbf{f}_e=\rho_e\big(\|\mathbf{g}_e\|\big)\frac{\mathbf{g}_e}{\|\mathbf{g}_e\|}:\)

the scalar law of (2.1) applied to the magnitude of the gradient vector and acting along it, so the _K_ gradient components share one congested conductance. At _K_=1, (6.2) _is_ (2.1). The system \(Bf^k=\alpha d^k\) with (6.2) is the stationarity of the convex energy \(E(\phi^1,\dots,\phi^K)=\sum_e\Psi_e(\|\mathbf{g}_e\|)-\alpha\sum_k(d^k)^\top\phi^k\), strictly convex modulo the _K_ per-commodity constants, so the equilibrium is unique. Physically the coupling turns on exactly where congestion does. On real capacity data at rush-hour load, commodity flows superpose to within solver tolerance (\(\lesssim 10^{-4}\) relative)--real networks place each edge in one of BPR’s two power-like regimes where path splits are load-independent--while the shared load inflates marginal costs by up to \(8.8\times\): the congestion externality is slowdown, not rerouting. Synthetic instances with random capacities do reroute (12-19% flow deviation), so the corpus sweep (§6.5) exercises the solver where commodities genuinely interact.

\begin{tabular}{cccccccc}
graph & class & _n_ & _F_<sup>∗</sup> & LAMG+ & approxChol & diagPCG & direct \\
`grid2` & 2D FEM & 3,296 & 3.003 & 11.4 & 0.75 & 12.3 & 0.24 \\
`airfoil1` & 2D FEM & 4,253 & 6.695 & 29.3 & 1.30 & 20.6 & 0.40 \\
`bodyy5` & aniso. FEM & 18,589 & 3.325 & 307 & 9.5 & 214 & 2.0 \\
`bcsstk38` & structural & 8,032 & 45.61 & stall & stall & stall & 4.0 \\
`circuit\_4` & circuit & 67,029 & 1.381 & 7.3 & 5.5 & 124 & 2.9 \\
`G2\_circuit` & circuit & 150,102 & 4.030 & 1579 & 50.1 & 3011 & OOM \\
\end{tabular}

5.2

_Inner-solver swap inside NLF’s max-flow continuation to F_<sup>∗</sup> _(wall-clock seconds; "stall"= did not converge within_ 120 _steps; "OOM"= exact factorization size-guarded at_ 150_k nodes). Every converging solver returns the_ identical _F_<sup>∗</sup>_, so the continuation is solver-agnostic; the operative choice is near-linear versus not. Representative subset; the bake-off script and its outputs are in the released artifact. On `bcsstk38` the stalled iterative solvers were arrested at_ 37.0_, far from the true F_<sup>∗</sup>=45.6 _the direct solve reaches._

