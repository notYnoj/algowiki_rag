<tbc>overrate a candidate when the greedy cover is poor for incidental reasons or when the maximum-frequency bound is much weaker than the true fractional optimum. `exact\_stab\_gap\_pressure` calls the exact set-cover and fractional-LP scorer for each candidate and ranks primarily by the exact stabbing gap \(\tau/\tau^*\). Its small tie-breaks prefer, among candidates of equal gap, those with a larger integer cover (more genuinely required lines), a smaller fractional optimum, and a more spread- out LP support, that is, more nonzero line variables, which tends to signal a richer fractional structure. As with the exact MISR surrogate, "surrogate" names its role in population ranking rather than any loss of fidelity, and its cost is that each call solves the same problem as the verifier. `incidence\_statistics` scores from line-incidence summaries alone and never solves a cover. It takes the greedy cover size, divides it by one plus the spread (standard deviation) of how many squares each critical line stabs, so that balanced, uniform incidence is rewarded, and adds a small bonus for a large number of distinct critical-line patterns. It is the cheapest square surrogate but is easily misled, since combinatorial incidence diversity need not translate into a large exact gap.

## D.3 Guillotine components

_Representations._ `rect\_direct\_disjoint` initial<tbc>

<tbc>izes by turning random grid cells into disjoint unit rectangles, a deliberately neutral start that usually yields an easily separable packing. Repair clamps intervals, removes interior overlaps, refills to the minimum size, and canonicalizes coordinates; the local search is responsible for growing the simple cells into long bars and interlocking packings. `recursive\_obstruction\_grammar` instantiates one or more seven-rectangle spiral obstruction cores, adds disjoint filler rectangles, and canonicalizes. No certificate or target score is inserted and the coordinates vary (consecutive gaps sampled from small values, with random reflections and axis exchange), but the seven-rectangle spiral topology is a hand-designed prior, so this is an obstruction-family search rather than a neutral coordinate search. `fixed\_symmetry\_packing` samples disjoint rectangles in a dynamic square domain, with roughly 40% long horizontal bars, 40% long vertical bars, and 20% compact rectangles, rejecting overlaps. The object count is fixed and the family is canonicalized over all symmetries; unlike the grammar it embeds no fixed non-sliceable topology, its only prior being the bar-heavy shape distribution.

_Local-search operations._ `packing\_resize` is a geometry-first neighborhood of move, resize, add, and delete (with add upweighted) followed by disjointness repair. After the primary move it runs three guided trials that may close a projection gap, add a bridge or<tbc>

\begin{tabular}{ccccccccc}
Representation & Local search & Surrogate & Best & Gain & Epoch & h & Plat.(%) & _n_ \\
`fixed\_sym\_pack` & `pack\_resize` & `depth\_dp` & 0.2500 & 0.0833 & 24 & 0.17 & 99.1 & 12 \\
`fixed\_sym\_pack` & `pack\_resize` & `first\_cut` & 0.2500 & 0.0833 & 42 & 0.42 & 97.1 & 12 \\
`fixed\_sym\_pack` & `pack\_resize` & `k\_subset` & 0.2500 & 0.0833 & 15 & 0.17 & 99.2 & 12 \\
`fixed\_sym\_pack` & `symmetry\_cross` & `depth\_dp` & 0.1667 & 0.0000 & 0 & 13.24 & 43.7 & 12 \\
`fixed\_sym\_pack` & `symmetry\_cross` & `first\_cut` & 0.1667 & 0.0000 & 0 & 8.90 & 62.7 & 12 \\
`fixed\_sym\_pack` & `symmetry\_cross` & `k\_subset` & 0.1667 & 0.0000 & 0 & 24.01 & 0.0 & 12 \\
`fixed\_sym\_pack` & `witness\_break` & `depth\_dp` & 0.2500 & 0.0833 & 6 & 0.06 & 99.7 & 12 \\
`fixed\_sym\_pack` & `witness\_break` & `first\_cut` & 0.2500 & 0.0833 & 3 & 0.02 & 99.9 & 12 \\
`fixed\_sym\_pack` & `witness\_break` & `k\_subset` & 0.2500 & 0.0833 & 12 & 0.09 & 99.5 & 12 \\
`rect\_direct` & `pack\_resize` & `depth\_dp` & 0.2727 & 0.1061 & 345 & 1.92 & 89.5 & 11 \\
`rect\_direct` & `pack\_resize` & `first\_cut` & 0.2500 & 0.1324 & 2514 & 17.91 & 19.3 & 8 \\
`rect\_direct` & `pack\_resize` & `k\_subset` & 0.2353 & 0.0924 & 306 & 16.72 & 28.3 & 17 \\
`rect\_direct` & `symmetry\_cross` & `depth\_dp` & 0.1667 & 0.0000 & 0 & 24.01 & 0.0 & 12 \\
`rect\_direct` & `symmetry\_cross` & `first\_cut` & 0.1667 & 0.0000 & 0 & 24.01 & 0.0 & 12 \\
`rect\_direct` & `symmetry\_cross` & `k\_subset` & 0.1667 & 0.0000 & 0 & 24.01 & 0.0 & 12 \\
`rect\_direct` & `witness\_break` & `depth\_dp` & **0.3333** & **0.2083** & **858** & **5.81** & **74.1** & **9** \\
`rect\_direct` & `witness\_break` & `first\_cut` & 0.2727 & 0.0727 & 696 & 3.06 & 80.9 & 11 \\
`rect\_direct` & `witness\_break` & `k\_subset` & 0.2500 & 0.1250 & 66 & 2.74 & 87.2 & 8 \\
`obstruction\_grammar` & `pack\_resize` & `depth\_dp` & 0.2500 & 0.0000 & 0 & 0.00 & 100.0 & 8 \\
`obstruction\_grammar` & `pack\_resize` & `first\_cut` & 0.2500 & 0.0000 & 0 & 0.00 & 100.0 & 8 \\
`obstruction\_grammar` & `pack\_resize` & `k\_subset` & 0.2500 & 0.0000 & 0 & 0.00 & 100.0 & 8 \\
`obstruction\_grammar` & `symmetry\_cross` & `depth\_dp` & 0.1667 & 0.0000 & 0 & 0.00 & 100.0 & 12 \\
`obstruction\_grammar` & `symmetry\_cross` & `first\_cut` & 0.1667 & 0.0000 & 0 & 0.00 & 100.0 & 12 \\
`obstruction\_grammar` & `symmetry\_cross` & `k\_subset` & 0.1667 & 0.0000 & 0 & 0.00 & 100.0 & 12 \\
`obstruction\_grammar` & `witness\_break` & `depth\_dp` & 0.2667 & 0.0167 & 669 & 8.10 & 66.2 & 15 \\
`obstruction\_grammar` & `witness\_break` & `first\_cut` & 0.2727 & 0.0227 & 468 & 2.54 & 85.8 & 11 \\
`obstruction\_grammar` & `witness\_break` & `k\_subset` & 0.2609 & 0.0109 & 510 & 22.87 & 4.6 & 23 \\
\end{tabular}

6: Complete per-configuration results for guillotine hardness (27 configurations). Best is the exact destroyed fraction 1 - save _/n_; the remaining columns are as in  4. The top-scoring configuration is highlighted in bold.

