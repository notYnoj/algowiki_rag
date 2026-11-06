<tbc>\(m=3.0\times 10^4\), \(45\times\) at \(m=1.2\times 10^5\), and at \(m=2.4\times 10^5\) Ipopt does not finish within its 120s CPU budget while NLF finishes in 3s.

**4.5. Robustness across the graph corpus.** The road networks above exercise NLF on real flow topologies; we now show it is robust across graph classes in full. We impose a single-commodity BPR congestion instance (random capacities and free- flow times, a far source-sink demand) on every graph of a 2,003 real-world SuiteSparse collection, each reduced to its largest connected component. This includes spanning structured grids, finite-element and circuit meshes, web, social, road, and citation networks with up to \(1.8\times 10^7\) edges.

Under this protocol (one BPR instance per graph, random capacities, a single far source-sink demand, stock settings) NLF converged on all 2,003 graphs to 10<sup>-9</sup> residual tolerance, with a Newton step count median of 6 and no size trend (Fig. 4.2B). The wall-clock fits \(t\propto m^{1.02}\) over the 1,788 graphs above 10<sup>3</sup> edges (Fig. 4.2A), per- edge cost flat at ≈0.86 \(\mu\)s/edge median (95th percentile 3.7 \(\mu\)s/edge). Three giants confirm the scaling beyond the sweep’s cap, to `hollywood-2009` at \(5.6\times 10^7\) edges.

**4.6. Comparison with other convex optimizers.** We compare three solver paradigms for the same convex BPR program: near-linear (NLF), sparse-direct (Ipopt), and matrix-free first-order (L-BFGS on the dual (2.2); on well-conditioned graphs L-BFGS also scales near-linearly and beats Ipopt, so that win is a fill-in effect any matrix-free method inherits). We ran all three on the 1,669 corpus graphs with

\begin{tabular}{cccccc}
network & _n_ & _m_ & NLF obj. & \(\|\Delta f\|/\|f\|\) & steps \\
Sioux Falls & 24 & 38 & 784.96 & \(3\cdot 10^{-9}\) & 7 \\
Anaheim & 416 & 634 & 1600.92 & \(6\cdot 10^{-12}\) & 9 \\
Chicago-Sketch & 933 & 1475 & 8178.62 & \(3\cdot 10^{-11}\) & 9 \\
Austin & 7388 & 10591 & 16615.74 & \(4\cdot 10^{-12}\) & 10 \\
Chicago-regional & 12979 & 20627 & 281.15 & \(2\cdot 10^{-11}\) & 9 \\
Sydney & 32956 & 38787 & 1198.98 & \(2\cdot 10^{-11}\) & 9 \\
\end{tabular}

\begin{tabular}{ccccc}
_m_ & NLF (s) & steps & Ipopt (s) & speed-up \\
12175 & 0.060 & 9 & 0.152 & \(2.5\times\) \\
29939 & 0.173 & 9 & 0.856 & \(4.9\times\) \\
59732 & 0.573 & 9 & 4.97 & \(8.7\times\) \\
119460 & 1.30 & 9 & 58.2 & \(45\times\) \\
239842 & 3.01 & 9 & -- (_\>_120s) & -- \\
\end{tabular}

4.1

_NLF (BPR congestion, near-linear inner) vs. Ipopt \[12\] on the_ undirected, single-commodity _Beckmann congestion program over real road-network topologies. Both solvers reach the_ same equilibrium of this program_; the objective matches to the tolerance, link flows to_ ∼10<sup>-10</sup>_. This is the undirected net-flow relaxation,_ not _the field’s directed origin-destination user equilibrium (§4)--it is an exact cross-check of two solvers on one identical convex program, so its objective value is not comparable to published directed-UE results for these networks. NLF’s step count shows no size trend. (Two further instances, Philadelphia and Berlin-Center, also match to_ 10<sup>-10</sup> _but need more steps under extreme capacity heterogeneity; omitted.)_

4.2

_Scaling on poorly-separable (Erdős-Rényi) graphs with BPR cost: NLF (_O(_m_) _near-linear inner) vs. Ipopt 3.14.19 (interior-point, MUMPS 5.9.0 sparse-direct KKT). Both reach the same optimum of the undirected congestion program. NLF’s step count shows no size trend; Ipopt is superlinear and exceeds the_ 120_s CPU budget on the largest instance ("--"). Speed-up=t_<sub>Ipopt</sub>_/t_<sub>NLF</sub>.

