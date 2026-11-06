<tbc>networks (topology, capacities, free-flow times, BPR parameters, and the four heaviest origin-destination pairs all from the benchmark data, jointly scaled to a loaded rush hour, peak \(\|\mathbf{f}_e\|/c_e\approx 1.07\)), and corpus-protocol instances from other coupled-flow domains where flows share one network--internet AS topology, a power transmission grid, national road networks. Every instance converges to 10<sup>-9</sup> with a handful of chord steps and 1-3 hierarchy setups, from 38 edges to \(1.5\times 10^6\) (e.g. `roadNet-PA`, \(1.5\times 10^6\) edges, 26 steps, 2 setups).

**6.5. Corpus robustness and the cost of** _K_**.** The decisive test is the same full- corpus sweep as §4.5, repeated at _K_=4: the identical 2,003 real-world SuiteSparse graphs and instance protocol, with four well-separated demand dipoles per graph, each at the benchmark load. Every one of the 2,003 graphs converges to 10<sup>-9</sup> relative residual (Fig. 6.1), to \(m=1.8\times 10^7\) edges, at a flat median of 18 chord steps (range 9-51) and a median of 1 hierarchy setup (maximum 5; more than two on only 120 of 2,003, triggered by the refresh conditions of §3.1): the shared scalar hierarchy carries the coupled four-commodity system essentially as cheaply as it carries one. The fitted total cost is \(t\propto m^{1.04}\) over four decades, median 9.1 \(\mu\)s per edge. Joined per graph against the single-commodity sweep, the _K_=4 solve costs a median \(3.8\times\) the single- commodity solve (interquartile range \[3.0,5.6\])--the ≈_K_ per-step work with the setup amortized, as the cost accounting of §6.2 predicts.

The cost of _K_ is measured directly by sweeping \(K\in\{1,2,4,8\}\) with nested demand sets on FEM and road graphs to \(1.5\times 10^6\) edges (`olesnik0`, `srb1`, `roadNet-PA`):

\begin{tabular}{ccccccc}
Network & _n_ & _m_ & Newton steps & NLF steps & Setups & Deviation \\
SiouxFalls & 24 & 38 & 8 & 8 & 1 & \(5\times 10^{-15}\) \\
Anaheim & 416 & 634 & 9 & 16 & 1 & \(5\times 10^{-10}\) \\
Chicago-Sketch & 933 & 1475 & 9 & 19 & 1 & \(3\times 10^{-10}\) \\
Winnipeg & 1040 & 1595 & 6 & 19 & 1 & \(7\times 10^{-11}\) \\
\end{tabular}

(A) K = 4: t x m1.04 over 1788 real graphs
(B) step count: flat in size and class
103
single commodity (54)
500
median 18 steps
K = 4 commodities
fit t = m1.04
102
slope 1 (O(m))
400
NLF total wall-clock (s)
101
300
100
number of graphs
10-1
200
10-2
10-3
100
10-4
0
101
102
103
104
105
106
107
10
20
30
40
50
edges m
chord (continuation) steps

6.1

_Multicommodity validation on real road networks (TNTP), K_=4_. "Exact Newton" assembles the full_ \(Kn\times Kn\) _block linearization and re-solves it at every damped step (the reference); NLF is the block-diagonal chord with one frozen scalar hierarchy. Deviation is the relative_ \(\ell_2\) _distance between the two equilibria._

Fig. 6.1. _Multicommodity NLF (K_=4_) over the full real-world SuiteSparse corpus, mirroring the single-commodity sweep (grey, underneath). (A) Total wall-clock vs. edge count: all_ 2,003 _graphs converge,_ \(t\propto m^{1.04}\) _over four decades. (B) Chord-step count: flat in size and class, median_ 18_-- unchanged from the single-commodity solver._

