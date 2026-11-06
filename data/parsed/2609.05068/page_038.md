<tbc>We also introduced a new relaxation of the conditional delay constraints and showed that it dominates the relaxations based on disjunctive programming.<br>
Moreover, we described a non-trivial approximation algorithm based on the proposed relaxation and established a provable performance guarantee for it.<br>
In the process of developing lower-bound heuristics, we proved that the use of certain convex over-estimators does not provide any advantage in the broader context of conditional constraints. In other words, employing such a convex over-estimator when dealing with a constraint of the form \(xg(x,y)\le 0\), with \(x\ge 0\), is equivalent to either fixing _x_ to 0 or imposing the constraint \(g(x,y)\le 0\).

While this study improves the global understanding of the delay-constrained multi-commodity flow problem, several questions still remain open. For instance, the exact complexity of the problem with a single commodity remains unknown; further improvements to the problem’s relaxations could be investigated in order to develop tractable optimization methods for larger instances. Future work could also focus on developing approximation algo<tbc>

\begin{tabular}{cccccccc}
Instance & |_K_| & |_A_| & |_V_| & BIG-M & S & T & CONVEX \\
pdh & 24 & 68 & 11 & **(250)** & (960) & (582) & (614) \\
di-yuan & 22 & 84 & 11 & **(188)** & (462) & 0.6% & (603) \\
polska & 66 & 36 & 12 & 15.9% & 16.9% & **13.5%** & 16% \\
nobel-us & 91 & 42 & 14 & 29.6% & 74.3% & 58.5% & **21.3%** \\
abilene & 132 & 30 & 12 & 35.8% & 13.5% & **6.5%** & 29.4% \\
nobel-germany & 121 & 52 & 17 & 18.1% & 16.5% & **16.3%** & 17.5% \\
dfn-bwin & 90 & 90 & 10 & 7.9% & **6.6%** & 9.8% & 10.1% \\
atlanta & 210 & 22 & 15 & 55.4% & **34.5%** & 42.1% & 59.2% \\
dfn-gwin & 110 & 47 & 11 & 17.6% & 16.9% & 17.5% & **16.6%** \\
sun & 67 & 102 & 27 & 35.1% & 43% & **35%** & 54.5% \\
newyork & 240 & 98 & 16 & 104% & 104% & 104% & **99.6%** \\
france & 300 & 90 & 25 & 51% & 52.4% & **49.5%** & 50% \\
nobel-eu & 378 & 82 & 28 & 113.8% & **49.3%** & 58.2% & 50.9% \\
ta1 & 396 & 102 & 24 & 27.4% & **26.3%** & 26.9% & 26.8% \\
geant & 462 & 72 & 22 & 97.2% & 13.9% & **9.4%** & 98.8% \\
norway & 702 & 102 & 27 & 180.8% & **174.1%** & 180.8% & 180.8% \\
india35 & 595 & 160 & 35 & 179.7% & **158.4%** & 174.8% & 212.8% \\
germany50 & 662 & 88 & 50 & 128.6% & 128.6% & 128% & **80%** \\
cost266 & 1332 & 114 & 37 & 68.7% & 67.3% & **64.4%** & 68.6% \\
\end{tabular}

1: Branch-and-bound results for the SND-Lib instances

