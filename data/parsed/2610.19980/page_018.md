<tbc>`exact\_grid` stores distinct integer lower-left anchors and one common integer side length, with initial anchors sampled without replacement from a grid and the initial side drawn from 1 to 4. Canonicalization removes translation and duplicates and keeps a common side, so the exact critical-line universe is easy to regenerate and audit. It is the least indirect of the three square representations, searching the actual coordinates and scale, at the cost of a large, rugged space with many plateaus. `fixed\_symmetry\_grid` stores distinct grid anchors at a fixed object count and a fixed common side (two in the final runs), reduced over all translations and the eight symmetries to a canonical coordinate list. Cardinality and side length are restored after every proposal, which makes representation comparisons clean at a fixed scale but prevents the search from moving between side-length regimes.

_Local-search operations._ `coord\_mutation` moves one square by at most one grid step, duplicates a nearby square, or deletes one. Representation-specific additions matter: with the incidence layout it can copy another square’s _x_- or _y_-coordinate; with the exact grid it also has line tightening, canonical shifting, a random restart, and a guided neighbor selector; and with the fixed- symmetry grid, fixed-count repair restores cardinality and re-canonicalizes. It is a plain coordinate mutation only in its simplest pairing. `sqstab\_local\_hillclimb`<tbc>

<tbc>augments the base moves with stabbing-aware proposals: copying or tightening a square onto another’s coordinate (optionally offset by the side length), adding or replacing a unique anchor, dropping a square, shifting to the origin, or restarting with fresh grid points and a resampled side. After the first proposal it builds a few nearby candidates and, for families up to about 48 squares, keeps the one with the best exact stabbing key; above that size it switches to the cheap greedy-cover- versus-frequency proxy to control cost. `symmetry\_ crossover\_hillclimb` uses the same 25-proposal shift, relocate, exchange, and symmetry portfolio, exactly scored. Acceptance is gated first by a nontriviality requirement - a candidate needing at least four lines is preferred to one with a smaller integer cover - and then by the exact gap; within the gate only nonworsening proposals are kept. The gate is an explicit search preference, not a target ratio or injected construction.

_Surrogates._ `greedy\_partial\_lp\_bitset` estimates the gap without solving any LP. It divides the size of a greedy line cover (an integer numerator) by a crude fractional lower bound, namely the number of squares divided by the largest number of squares any single line stabs; because a line that stabs many squares forces the fractional optimum up, this ratio bounds how good any cover can be. Incidence sets are stored as bitmasks, so the whole computation is fast, but the estimate can<tbc>

\begin{tabular}{ccccccccc}
Representation & Local search & Surrogate & Best & Gain & Epoch & h & Plat.(%) & _n_ \\
`fixed\_sym\_grid` & `coord\_mut` & `exact\_stab\_gap` & 1.5000 & 0.3333 & 1896 & 8.36 & 78.3 & 20 \\
`fixed\_sym\_grid` & `coord\_mut` & `greedy\_lp` & 1.3043 & 0.3043 & 8526 & 23.32 & 1.6 & 20 \\
`fixed\_sym\_grid` & `coord\_mut` & `incidence\_stats` & 1.2766 & 0.2766 & 249 & 0.18 & 97.0 & 20 \\
`fixed\_sym\_grid` & `sqstab\_hill` & `exact\_stab\_gap` & 1.3636 & 0.2098 & 2322 & 5.56 & 63.4 & 20 \\
`fixed\_sym\_grid` & `sqstab\_hill` & `greedy\_lp` & 1.3333 & 0.3333 & 2451 & 4.87 & 64.1 & 20 \\
`fixed\_sym\_grid` & `sqstab\_hill` & `incidence\_stats` & 1.2857 & 0.2857 & 2481 & 4.88 & 63.2 & 20 \\
`fixed\_sym\_grid` & `symmetry\_cross` & `exact\_stab\_gap` & 1.5000 & 0.3462 & 408 & 2.06 & 90.8 & 20 \\
`fixed\_sym\_grid` & `symmetry\_cross` & `greedy\_lp` & 1.5000 & 0.5000 & 309 & 2.66 & 92.9 & 20 \\
`fixed\_sym\_grid` & `symmetry\_cross` & `incidence\_stats` & 1.5000 & 0.3750 & 183 & 0.92 & 95.3 & 20 \\
`line\_sq\_inc` & `coord\_mut` & `exact\_stab\_gap` & 1.5000 & 0.5000 & 3915 & 11.18 & 40.2 & 21 \\
`line\_sq\_inc` & `coord\_mut` & `greedy\_lp` & 1.2500 & 0.1071 & 4587 & 16.21 & 21.8 & 24 \\
`line\_sq\_inc` & `coord\_mut` & `incidence\_stats` & 1.3333 & 0.3333 & 873 & 1.01 & 87.3 & 9 \\
`line\_sq\_inc` & `sqstab\_hill` & `exact\_stab\_gap` & 1.5000 & 0.5000 & 3003 & 9.29 & 48.9 & 21 \\
`line\_sq\_inc` & `sqstab\_hill` & `greedy\_lp` & 1.3636 & 0.2208 & 2103 & 6.05 & 62.4 & 24 \\
`line\_sq\_inc` & `sqstab\_hill` & `incidence\_stats` & 1.3333 & 0.3333 & 2781 & 7.03 & 54.7 & 15 \\
`line\_sq\_inc` & `symmetry\_cross` & `exact\_stab\_gap` & 1.4644 & 0.3532 & 273 & 11.67 & 58.5 & 28 \\
`line\_sq\_inc` & `symmetry\_cross` & `greedy\_lp` & 1.4141 & 0.4141 & 201 & 1.52 & 56.2 & 20 \\
`line\_sq\_inc` & `symmetry\_cross` & `incidence\_stats` & 1.4268 & 0.4268 & 615 & 20.80 & 8.7 & 20 \\
`sqstab\_grid` & `coord\_mut` & `exact\_stab\_gap` & 1.5000 & 0.3571 & 117 & 0.35 & 98.5 & 14 \\
`sqstab\_grid` & `coord\_mut` & `greedy\_lp` & 1.3636 & 0.2208 & 6777 & 23.68 & 0.8 & 20 \\
`sqstab\_grid` & `coord\_mut` & `incidence\_stats` & 1.3158 & 0.1158 & 147 & 0.14 & 98.0 & 10 \\
`sqstab\_grid` & `sqstab\_hill` & `exact\_stab\_gap` & 1.5000 & 0.3571 & 375 & 0.46 & 94.8 & 19 \\
`sqstab\_grid` & `sqstab\_hill` & `greedy\_lp` & 1.3462 & 0.3462 & 3087 & 6.68 & 55.5 & 22 \\
`sqstab\_grid` & `sqstab\_hill` & `incidence\_stats` & 1.3333 & 0.3333 & 0 & 0.00 & 100.0 & 9 \\
`sqstab\_grid` & `symmetry\_cross` & `exact\_stab\_gap` & **1.5385** & **0.4332** & **54** & **0.37** & **98.2** & **20** \\
`sqstab\_grid` & `symmetry\_cross` & `greedy\_lp` & 1.5000 & 0.5000 & 39 & 1.41 & 98.7 & 20 \\
`sqstab\_grid` & `symmetry\_cross` & `incidence\_stats` & 1.4407 & 0.4407 & 342 & 2.39 & 87.7 & 20 \\
\end{tabular}

5: Complete per-configuration results for unit-square stabbing (27 configurations). Best is the exact integrality gap \(\tau/\tau^*\); the remaining columns are as in  4. The top-scoring configuration is highlighted in bold.

