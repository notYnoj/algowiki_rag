<tbc>sentation, the global symmetry proposal canonicalizes back to the same state and is neutral.

_Surrogates._ `exact\_lp\_gap\_pressure` calls the full MISR exact scorer for every candidate it ranks and orders the population primarily by the exact clique- LP-to-integer gap \(\alpha^*/\alpha\), the very quantity the study reports, breaking ties among candidates of equal gap in favor of a larger triangle-free lower bound. It is called a surrogate only because it decides which candidates are retained and trained on, not because it is approximate: it is the most tightly aligned of the three MISR signals, and also the most expensive, since each ranking call solves the same optimization as the verifier and so lowers the number of generations completed within the time budget. `triangle\_free\_exact\_gap\_ pressure` first applies a hard filter, pushing any candidate whose intersection graph contains a triangle to the bottom so that it is effectively discarded. Among the surviving triangle-free candidates it ranks by the exact gap, breaking ties in favor of a stronger triangle-free lower bound and a denser conflict graph (more intersection edges relative to the object count). Because the rejection happens in the ranking step rather than in the representation, this surrogate can enforce triangle- freeness even when paired with a representation, such as `fixed\_symmetry\_rectangles`, that does not. `graph\_`<tbc>

<tbc>`conflict\_proxy`<tbc>

<tbc>`proxy` avoids solving the clique LP and instead estimates promise from cheaper graph statistics: it rewards a high intersection-edge density relative to the exact independence number, that is, many conflicts packed against a small independent set, adds a term for the maximum clique size, and gives a bonus for triangle- freeness. The intuition is that large gaps tend to live in graphs that are dense in conflicts yet have a small independent set. It is cheaper than solving the LP but not a purely linear-time statistic, since computing the independence and clique numbers still needs combinatorial graph routines, and edge density alone need not predict the true clique-LP gap.

## D.2 Unit-square stabbing components

_Representations._ `line\_square\_incidence` builds a balanced abstract row-and-column layout first and maps it to square anchors, assigning each square an abstract row and column and jittering each axis with modest probability. The solver-facing state is the list of anchors, with the row and column labels recomputed from the geometry after each move, so the incidence payload guides initialization and structured moves rather than being a separate exact model. It starts near balanced line-incidence patterns, which makes hard covers more likely but can overproduce easy-to-stab grids. `sqstab\_`<tbc>

\begin{tabular}{ccccccccc}
Representation & Local search & Surrogate & Best & Gain & Epoch & h & Plat. (%) & _n_ \\
`fixed\_sym\_rect` & `coeff\_pivot` & `exact\_lp\_gap` & 1.2500 & 0.2500 & 564 & 0.42 & 92.9 & 12 \\
`fixed\_sym\_rect` & `coeff\_pivot` & `conflict\_proxy` & 1.2500 & 0.2500 & 2937 & 4.02 & 64.5 & 12 \\
`fixed\_sym\_rect` & `coeff\_pivot` & `tf\_exact\_gap` & 1.2500 & 0.2500 & 4770 & 8.90 & 42.7 & 12 \\
`fixed\_sym\_rect` & `seq\_pivot` & `exact\_lp\_gap` & 1.3333 & 0.3333 & 2256 & 9.12 & 73.0 & 12 \\
`fixed\_sym\_rect` & `seq\_pivot` & `conflict\_proxy` & 1.0000 & 0.0000 & 0 & 0.00 & 100.0 & 12 \\
`fixed\_sym\_rect` & `seq\_pivot` & `tf\_exact\_gap` & 1.2500 & 0.0000 & 0 & 0.00 & 100.0 & 12 \\
`fixed\_sym\_rect` & `symmetry\_cross` & `exact\_lp\_gap` & 1.3333 & 0.3333 & 12 & 0.30 & 99.8 & 12 \\
`fixed\_sym\_rect` & `symmetry\_cross` & `conflict\_proxy` & 1.2500 & 0.2500 & 3 & 0.00 & 99.9 & 12 \\
`fixed\_sym\_rect` & `symmetry\_cross` & `tf\_exact\_gap` & 1.2500 & 0.2500 & 3 & 0.00 & 99.9 & 12 \\
`qp\_rect` & `coeff\_pivot` & `exact\_lp\_gap` & 1.3333 & 0.3333 & 75 & 0.29 & 98.6 & 8 \\
`qp\_rect` & `coeff\_pivot` & `conflict\_proxy` & 1.3333 & 0.3333 & 192 & 0.33 & 97.2 & 8 \\
`qp\_rect` & `coeff\_pivot` & `tf\_exact\_gap` & 1.3333 & 0.3333 & 1104 & 2.11 & 84.1 & 8 \\
`qp\_rect` & `seq\_pivot` & `exact\_lp\_gap` & 1.3333 & 0.3333 & 510 & 1.19 & 92.2 & 8 \\
`qp\_rect` & `seq\_pivot` & `conflict\_proxy` & 1.3333 & 0.3333 & 1494 & 3.02 & 79.2 & 8 \\
`qp\_rect` & `seq\_pivot` & `tf\_exact\_gap` & 1.3333 & 0.3333 & 336 & 0.60 & 95.2 & 8 \\
`qp\_rect` & `symmetry\_cross` & `exact\_lp\_gap` & 1.2000 & 0.1167 & 0 & 0.02 & 99.9 & 12 \\
`qp\_rect` & `symmetry\_cross` & `conflict\_proxy` & 1.2000 & 0.2000 & 0 & 0.02 & 99.9 & 12 \\
`qp\_rect` & `symmetry\_cross` & `tf\_exact\_gap` & 1.3000 & 0.2167 & 63 & 0.91 & 95.8 & 12 \\
`triangle\_free` & `coeff\_pivot` & `exact\_lp\_gap` & 1.4000 & 0.4000 & 4782 & 14.48 & 25.1 & 14 \\
`triangle\_free` & `coeff\_pivot` & `conflict\_proxy` & 1.3333 & 0.3333 & 51 & 0.05 & 99.3 & 8 \\
`triangle\_free` & `coeff\_pivot` & `tf\_exact\_gap` & 1.3750 & 0.3750 & 156 & 0.15 & 97.5 & 11 \\
`triangle\_free` & `seq\_pivot` & `exact\_lp\_gap` & **1.5000** & **0.3750** & **1860** & **3.12** & **70.7** & **12** \\
`triangle\_free` & `seq\_pivot` & `conflict\_proxy` & 1.1250 & 0.1250 & 66 & 0.06 & 99.0 & 9 \\
`triangle\_free` & `seq\_pivot` & `tf\_exact\_gap` & 1.3750 & 0.3750 & 231 & 0.22 & 96.4 & 11 \\
`triangle\_free` & `symmetry\_cross` & `exact\_lp\_gap` & 1.2000 & 0.2000 & 0 & 0.00 & 100.0 & 12 \\
`triangle\_free` & `symmetry\_cross` & `conflict\_proxy` & 1.2000 & 0.2000 & 0 & 0.00 & 100.0 & 12 \\
`triangle\_free` & `symmetry\_cross` & `tf\_exact\_gap` & 1.2000 & 0.2000 & 0 & 0.01 & 100.0 & 12 \\
\end{tabular}

4: Complete per-configuration results for MISR (27 configurations). Best is the exact integrality gap \(\alpha^*/\alpha\); Gain is the improvement over the initial construction; Epoch and h are the cumulative training epoch and elapsed hours at the best construction; Plat. is the post-best plateau fraction; _n_ is the object count. The top-scoring configuration is highlighted in bold.

