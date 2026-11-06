<tbc>\(n\le 300,000\) (the subset where Ipopt’s sparse-direct KKT does not run out of memory on poorly-separable instances), each competitor capped at \(5\times\) NLF’s wall-clock ( 4.3). NLF converged on all 1,669; first-order failed on 481 (ill-conditioning, \(\kappa\sim N\)) and interior-point on 143 (fill-in). On the 90 graphs hard on both axes, neither competitor finished within budget. Where they converge, NLF is median \(2.6\times/4.2\times\) faster than Ipopt/L-BFGS and fastest-or-only on 85%. Timing protocol: all three solvers share one global precompilation pass, and NLF is then timed on a warm per-graph call; the competitors on their first per-graph call. This per-graph warm-up favours NLF by a small-graph-weighted margin that is negligible at scale, where NLF’s advantage is the genuine avoidance of direct fill-in (§4.4); the "within budget" counts use the \(5\times\)-NLF wall-clock cap and are a wall-clock criterion, not a claim the others cannot converge given more time.

**4.7. Inner-solver ablation: which near-linear engine.** The framework can use any near-linear inner solver (§3.1); we settle the default empirically. Holding<tbc>

(A) Per-edge: NLF flat (O(m)) vs Ipopt rising on random ( x m1.19)
(B) Ipopt wins on planar roads; NLF wins + Ipopt blows up on random
NLF road (real)
NLF random Ipopt road (real)
102
NLF road (real)
NLF random Ipopt road (real)
Iopt random
Iopt fails (NLF: 3.0s)
101
102
100
time per edge (us/edge)
total wall-clock (s)
10-1
10-2
101
10-3
10-4
102
103
104
105
102
103
104
105
edges m
edges m

(A) t = m1.02 over 1788 real graphs: genuine O(m)
(B) chord-Newton step count: flat in size and class
102
fit t = m1.02 slope 1 (O(m))
median 6 steps
600
101
500
NLF total wall-clock (s)
100
400
10-1
number of graphs
300
10-2
200
10-3
100
10-4
101
102
103
104
105
106
107
0
2
4
6
8
10
12
14
16
edges m
Chord Newton steps

Fig. 4.1. _Congestion (BPR) equilibrium, NLF vs. Ipopt, on real road networks (circles) and synthetic poorly-separable graphs (squares). (A)_ Per-edge _time: NLF is flat (near-_O(_m)) on both families; Ipopt is flat on roads but rises steeply on random graphs (_\(\propto m^{1.2}\) _per edge). (B) Total wall- clock: Ipopt wins on planar roads (cheap separators), is overtaken on random graphs by a margin that widens to_ \(45\times\)_, and fails (time limit) at_ \(m=2.4\times 10^5\) _where NLF finishes in_ 3.0_s._

Fig. 4.2. _NLF over the full real-world SuiteSparse corpus (_2,003 _graphs, all classes,_ \(10^2-1.8\times 10^7\) _edges,_ 100% _converged). (A) total wall-clock vs. m (log-log): the fit is_ \(t\propto m^{1.02}\) _over five decades (slope-_1 _reference dashed), empirically near-linear, per-edge cost flat at_ \(\approx 0.86\mu\)_s/edge median. (B) Newton step count: a flat distribution (median_ 6_, range_ 2-15)._

