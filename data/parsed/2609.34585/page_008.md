**Labels beyond the solver.** Continuing the supervised MIS checkpoint with the labels replaced by its own better solutions cuts the test gap by more than half and gives our best checkpoint, the one behind  1. This indicates that self-relabeling can further improve a trained model, since it then trains on larger sets than those found by the solver for the initial training labels. The relabeling passes raise about 16% of the training instances above their KaMIS labels, by one node on average.

**No solver at all.** Starting from random initialization with no labels available, the model first seeds the initial labels with its own solution guesses and then hill-climbs on them. Once there is a signal, the model exploits it in training and keeps self-relabeling. On MIS its labels end up within one node of the KaMIS labels on average and match or beat them on 42% of the training graphs. Its test gap comes within one third of a point of the supervised continuation and is below that of the supervised checkpoint itself. On TSP-500 the label-free run closes most of the distance to the LKH-3 tours, from about 10% above them to less than 2%, but its test gap is still \(20\times\) that of the supervised model. Figure 5 in Appendix G traces the evolution of the training labels.

MIS ER-[700-800]
TSP
4
kp = 2, D = 16
kp = 8, D = 16
0.30
kp = 2, D = 32
kp = 8, D = 32
TSP-1000
3
Optimality gap (%)
Optimality gap (%)
0.25
2
D = 16
0.20
TSP-500
D = 32
1
0.15
KaMIS
0
0.10
10
20
40
100
200
5
10
20
40
100
Rollouts K
Rollouts K

MIS ER-[700-800]
TSP-500
DIFUSCO
CAM
Att-GCN
8
T2T
2.0
GLOP
Fast T2T
UDC
DIMES
SoftDist
6
1.0
UTSP
Learned solver
Optimality gap (%)
Zero heatmap
COExpander
Optimality gap (%)
UDC
Search / sampler
4
TRM4CO along K
DIFUSCO
BQ-NCO
RLNN
0.5
DIFUSCO+MCTS
T2T
Moco
2
COExpander
CAM
K = 10
DDEA
DRHG
20
0.2
Fast T2T
KaMIS
Moco
40
K = 5
LEHD
0
RLSA
10
20
40
100
COExp.+RLSA
iSCO
ReSCO
0.1
1
10
100
1000
1
10
100
Seconds per instance (1)
Seconds per instance (1)

Figure 2: Test-time scaling. Left: MIS on ER-[700-800], optimality gap against the number of rollouts _K_ (log scale) for sequential peeling with \(k_\mathrm{p}\in\{2,8\}\) nodes per round at depth \(D\in\{16,32\}\). Right: TSP-500 and TSP-1000, gap after 2-opt against _K_ for \(D\in\{16,32\}\).

Figure 3: Quality against wall-clock time. We plot optimality gap against seconds per instance on one RTX 4090 for ER-[700-800] (left) and TSP-500 (right). The MIS gap is measured against the KaMIS reference (dotted line) of  1, so negative values mean that the reference is beaten. Circles are learned solvers, triangles are pipelines dominated by search or sampling (MCTS, samplers, evolution), and stars are TRM4CO for increasing _K_ (_k_<sub>p</sub>=2 and _D_=32 on ER-[700-800], _D_=32 on TSP-500).

