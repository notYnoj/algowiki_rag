<tbc>NLF’s outer method fixed (load-continuation chord-Newton, lazy refresh), we swap only the inner Laplacian solve and rerun the congestion corpus of §4.5 (one BPR instance each; over 1,800 graphs except the very largest graphs). The candidates are the two public O(_m_) solvers of §3.1, approximate Cholesky and LAMG+; we exclude sparse-direct, which is not near-linear--its separability crossover against an O(_m_) inner is the scaling result of §4.4, not an inner we would ship.

_Both converge on every graph, to the identical equilibrium:_ the dual energy agrees to floating-point precision and the link flows to \(\le 2\times 10^{-8}\) relative error. So robustness is therefore not a discriminator. Speed splits by graph class, both ways: approximate Cholesky is faster on 81% of graphs (median \(1.8\times\), up to \(43\times\)--its cheap factor wins on low-treewidth mesh and finite-element graphs) and LAMG+ on the other 19% (up to \(24\times\)--its hierarchy wins on the poorly-separable and structural graphs); the overall median is \(1.6\times\) in approximate Cholesky’s favour, with 39% of graphs within \(1.5\times\) either way ( 4.4). We therefore adopt the faster approximate Cholesky as the default and keep LAMG+ as a robust alternative: it wins wall-clock on the poorly-separable and structural minority, and at the saturating fold its cut-respecting aggregation (§3.1) gives a structurally clean near-singular solve with no fold-aware tuning, though approximate Cholesky’s constant is often smaller even there (§5.1).

Residual tolerance criterion sensitivity is mild ( 4.5): freezing the factor more aggressively trades a few extra outer steps for fewer setups until it over-freezes, and a looser inner forcing \(\eta\) costs outer steps; the stock (\(\text{refresh}=0.25,\eta=0.05\)) sits in the flat interior.

## 4.8. Cost as a function of the target accuracy.

The dependence on the requested solution accuracy \(\varepsilon\) is logarithmic. Each inner solve to relative residual \(\delta\) costs \(\mathcal{O}(mlog(1/\delta))\) (a bounded inner contraction gives \(\mathcal{O}(log(1/\delta))\) inner iterations). The outer iteration is a frozen chord-Newton with inexact-Newton forcing \(\eta_k\) tracking the nonlinear residual \(\|r_k\|\) (§3.1); its per-step cycle counts form a series dominated by the final solve (where \(\|r_k\|\rightarrow\varepsilon\)), the earlier looser steps adding only a bounded geometric tail, while the continuation and globalization run at a fixed, \(\varepsilon\)-independent

\begin{tabular}{ccc}
regime & graphs & outcome \\
both competitors converge (well-conditioned) & 1,137 & NLF \(\le\) both (median \(2.6\times/4.2\times\) faster than Ipopt/L-BFGS) \\
ill-conditioned (first-order degrades) & 389 & L-BFGS exceeds \(5\times\) NLF; NLF, Ipopt converge \\
poorly-separable (direct fills in) & 51 & Ipopt over budget (fill-in); NLF, L-BFGS converge \\
**both over budget** \(\Rightarrow\) **union** & 92 & **NLF is the only solver that finishes** \\
**total** & 1,669 & **NLF** 100% **converged; fastest-or- only on** 85% \\
\end{tabular}

4.3

_Three-paradigm robustness frontier across the SuiteSparse corpus_ (1,669 _graphs, undirected BPR congestion--the same convex program for all). NLF (multigrid-Newton) vs. Ipopt (interior- point/sparse-direct KKT) vs. L-BFGS-on-the-dual (matrix-free first-order); each competitor capped at_ \(5\times\) _the measured NLF wall-clock_ (1_s floor,_ 120_s ceiling). NLF converges on every graph and is the only paradigm that stays within budget on both axes. On_ 90 _graphs neither competitor finishes within the_ \(5\times\)_NLF budget, and Ipopt is additionally too large to run on_ 2 _more--a union of_ 92 _on which NLF alone finishes ("within budget" is a wall-clock criterion, not a claim the others cannot converge given more time)._

