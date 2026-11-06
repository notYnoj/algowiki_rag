<tbc>pairs sharing a seed are not independent. Higher \(\bar{\Delta}\) indicates that quantum hardware produced structurally varied seeds spanning a broader region of the solution space.

A strong positive correlation is visible between the initial mean Hamming distance \(\bar{\Delta}\) and the amplification factor (Spearman \(\rho=0.85\) across the 35 instances that admit at least one seed pair, five being excluded because only a single one of their returned solutions lies at the optimum size). Much of it reflects manifold size. Over the 30 instances that also appear in Figure 5, \(\bar{\Delta}\) correlates with _D_MIS at \(\rho=0.96\), and at fixed _D_MIS the partial rank correlation between \(\bar{\Delta}\) and _A_ is 0.00. Diversity does not predict coverage either (\(\rho=-0.84\)), because diverse seed pools come from large manifolds, where the recovered fraction is small.

Note that the relationship is not deterministic: some instances with moderate initial diversity achieve high amplification, and vice versa, indicating that graph topology and the specific positions of disagreement clusters<tbc>

<tbc>also play important roles. A larger symmetric difference breaks into more exchangeable components and so yields more candidates per pair, but how many of them are new depends on the graph.

## D. Classical Post-Processing Improves on Quantum Hardware for Hard Instances

For the nine hard instances we can compare our results directly against the exact reference optima of Section IIF. This comparison establishes two facts. First, quantum hardware failed to reach the true optimum on six of the nine hard instances, falling short by 1 to 4 atoms ( I), and on the other three it returned only a single solution at the optimum. These six account for most of the eight shortfalls across the whole dataset (Section IIF). The difficulty of these instances is that unassisted quantum annealing does not sample the ground-state manifold fairly. Second, classical Houdayer post-processing of the quantum seeds discovered strictly larger configurations on three of these nine instances (`L12\_seed829`, `L17\_seed424`, `L17\_seed46`), by one atom for `L12\_seed829`, reaching its optimum, and by two and three atoms for the two `L17` instances. These three cases are gains in solution quality. On the other three suboptimal hard instances (`L16\_seed2871`, `L16\_seed4392`, and `L16\_seed798`) cluster exchanges yielded no improvement.

`L12\_seed829`: The seed pool held 64 solutions at size 35. Houdayer exploration of these seeds discovered solutions at size 36, the certified optimum, and a second pass from them recovered all 18 configurations of the ground- state manifold (_D_MIS=18).

\begin{tabular}{cccccc}
Instance & Seed & Houdayer & LS & True & Gap \\
L12\_seed829 & 35 & 36 & 36 & 36 & 0 \\
L12\_seed2922 & 35 & 35 & 35 & 35 & 0 \\
L14\_seed2480 & 47 & 47 & 47 & 47 & 0 \\
L15\_seed3591 & 54 & 54 & 54 & 54 & 0 \\
L16\_seed2871 & 63 & 63 & 63 & 64 & -1 \\
L16\_seed4392 & 61 & 61 & 61 & 62 & -1 \\
L16\_seed798 & 60 & 60 & 60 & 61 & -1 \\
L17\_seed424 & 68 & 70 & 69 & 71 & -1 \\
L17\_seed46 & 67 & 70 & 70 & 71 & -1 \\
\end{tabular}

100
10
Manifold recovered f (%)
1
0.1
0.01
nseed < 10
10 < nseed < 100
0.001
nseed > 100
100
102
104
106
108
Exact ground-state degeneracy DMIS

FIG. 5. Fraction of the exact ground-state manifold recovered, against the manifold’s size. The reference data set records not only the optimum size but the exact degeneracy _D_MIS \[7, 17\], so coverage can be measured as _N_total_/D_MIS rather than bounded. Only the 35 instances whose seed pool already sits at the certified optimum are shown; the 8 excluded are the shortfall instances of Section IIF, whose recovered solutions are not ground states, so coverage of the ground-state manifold is undefined for them. For the Benchmark instances, which have no reference entry, _D_MIS is computed exactly by transfer-matrix dynamic programming over the lattice columns, a method validated against all 121 reference instances whose atom positions are distributed with the dataset (121 of 121 exact matches in both optimum size and degeneracy). Marker shape bins the size _n_seed of the quantum seed pool, the second factor controlling the recovered fraction _f_. A joint fit over both predictors gives \(f\propto D_\text{MIS}^{-0.58\pm 0.04}n_\text{seed}^{1.40\pm 0.12}\) with _R_<sup>2</sup>=0.89: at fixed seed pool _f_ falls with manifold size, while at fixed manifold size it rises with the number of seeds.

TABLE I. All nine hard instances, comparing the largest independent set in the seed pool ("Seed"), after Houdayer post-processing of those seeds ("Houdayer"), and after local search from the same seeds with the same number of candidate evaluations ("LS", Section IVA), against the exact optimum ("True"), certified as described in Section IIF. The seed pool misses the true optimum on six instances, and on the other three holds a single solution at it. Houdayer cluster updates improve on the seeds on three, reaching the true optimum on `L12\_seed829` and coming within one atom of it on the two `L17` instances. The residual gap ("Gap") is Houdayer minus True, i.e., the shortfall of the best post-processed solution against the true optimum (Section IVC).

