<tbc>hort, 12 for replacement MISR and guillotine, and 20 for replacement unit-square stabbing, and mutation and repair keep the count within 8-24, 12-36, and 20-60 respectively, except for representations that explicitly preserve cardinality.

**Progress axes and metrics.** We retain three progress axes because they answer different questions: search generation (the most direct algorithmic-progress variable), elapsed time (the fairest resource comparison, since every configuration received the same wall-clock budget), and cumulative transformer-training epoch (an accounting axis over repeated short fits, not a single continuous learning curve). Per-configuration metrics are the best exact score, time-to-best, epoch-to-best, and the post-best plateau fraction.

**Exact solvers.** The exact oracles that gate certificate acceptance use only open-source solvers, with no commercial optimization license. MISR combines Bron- Kerbosch maximal-clique enumeration, SciPy’s HiGHS linear-programming backend for the fractional clique LP, and a custom bitset branch-and-bound maximum- independent-set solver; unit-square stabbing enumerates the finite critical-line universe, uses the same HiGHS backend for the fractional cover, and a custom branch-and-bound set-cover solver for the integer optimum; and guillotine hardness uses a custom recursive dynamic program over rectangle-subset bitmasks and all relevant cuts. Each linear program runs on a single HiGHS thread with no separate solver time limit, verification uses a numerical tolerance of 10<sup>-8</sup>, and the guillotine dynamic program uses exact discrete comparisons.

## 5.3 Results

**Good solutions are rare.** Exploring this space succeeds, but only sparsely.  2 reports, for each problem, the best configuration and its exact score together with the next-best and median scores over the 27 configurations. The complete per-configuration results, including the gain over the initial construction, the training epoch and elapsed time at which the best appeared, and the post-best plateau fraction, are given in Appendix B. The weakest configurations, which pair a generic coordinate representation with a cheap heuristic surrogate, never move beyond trivial or half-integral constructions, and for every problem the maximum is reached by a single configuration out of the 27. Good solutions are therefore rare: they occupy isolated points of the design space rather than a broad basin, and the median configuration lies well below the maximum ( 2).

The best constructions are small, exactly verified witnesses. For MISR the search attains an integrality<tbc>

<tbc>gap of 3/2: a family of twelve rectangles with clique- LP optimum \(\alpha^*=6\) and integer optimum \(\alpha=4\). For guillotine hardness it attains a destroyed fraction of 1/3: a packing of 9 rectangles from which an optimal recursive strategy preserves six and destroys three, found from scratch with no warm start. The strongest single outcome is for unit-square stabbing, where the search attains an integrality gap of 20/13≈1.54: a family of twenty congruent squares with set-cover LP optimum \(\tau^*=13/5\) against an integer optimum \(\tau=4\) (Figure 3). This is a major achievement, since it strictly exceeds the best lower bound of 3/2 previously known in the literature (Section 3) and is found automatically with an independently verified certificate. It is also a rare single-configuration outcome: of the 27 unit-square configurations, 9 reach exactly 3/2 and only this one exceeds it.

**Which combination unlocks each problem.** The winning configuration is problem-specific. The best combinations ( 2) keep the rectangle intersection graph sparse and score by the true LP/integer gap for MISR, operate on the line-square incidence guided by the exact stabbing gap for unit-square stabbing, and attack the recursive cut that would otherwise separate the packing for guillotine hardness. Figure 4 illustrates the effect component by component for unit- square stabbing: holding two components at their best choice and varying the third shows the surrogate as the sharpest lever, with the exact stabbing-gap surrogate climbing well above the cheap proxies. The analogous slices for MISR and guillotine hardness are given in Appendix C.

**Careful exploration and co-design.** Taken together, the exploration shows that no component is decisive on its own and that the component carrying a problem’s structural signal differs across problems: a<tbc>

\begin{tabular}{cccccc}
Problem & Best & Next & Median & _n_ & h \\
MISR & 3/2 & 1.400 & 1.300 & 12 & 3.12 \\
\multicolumn{6}{c}{`triangle\_free\_rect / sequence\_pair\_pivot / exact\_lp\_gap\_pressure`} \\
Unit-square & 20/13 & 1.500 & 1.414 & 20 & 0.37 \\
\multicolumn{6}{c}{`sqstab\_exact\_grid / symmetry\_crossover\_hillclimb / exact\_stab\_gap\_pressure`} \\
Guillotine & 1/3 & 0.273 & 0.250 & 9 & 5.81 \\
\multicolumn{6}{c}{`rect\_direct\_disjoint / witness\_breaking / depth\_limited\_dp`} \\
\end{tabular}

2: Best configuration for each problem among its 27. Best is the exact score (\(\alpha^*/\alpha\), \(\tau/\tau^*\), and 1-save _/n_, respectively); Next is the highest score among the other 26 configurations; Median is the median over all 27; _n_ is the object count and h the elapsed hours at the best construction. Complete per-configuration results are given in Appendix B.

