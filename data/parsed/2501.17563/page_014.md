## 2.4 Approximation Ratio of the Root Rounding - Lower Bounds

So far we just disproved the first (and stronger) conjecture, and studied the integrality gap of the LP. In this section we return to the original problem of STTs, and consider the rounding in Definition 1.6. We disprove Conjecture 2 that claims it rounds to an optimal STT. The rounding scheme may have degrees of freedom, and we study it both when assuming the worst-case scenario (pick a worst choice) and in the best-case scenario (pick a best choice).

Interestingly, for all the seven small topologies (\(n\le 8\)) for which non-STT vertices were found, when solving the LP in a primary direction, there is a rounding that yields an optimal STT. At a first glance this suggests that there is hope to refine the rounding scheme to remove misleading degrees of freedom (of choosing which node to root at each iteration). However we show later in this section that in non-primary directions we are no longer guaranteed an optimal rounding. This "strongly" disproves Conjecture 2 by showing that the rounding scheme could be suboptimal regardless of the degrees of freedom in the rounding procedure.

3 summarizes our findings for the seven topologies with non-STT vertices. We show that every topology has directions for which even the best-case rounding is sub-optimal. We also show directions with large worst-case ratios, the largest that we found, though not by an exhaustive search or analysis, is \(\frac{263}{190}\approx 1.384\). This is a lower-bound on the approximation ratio of the root rounding approach.

In the remainder of this section we detail the following: Theorem 2.9 demonstrates an explicit<tbc>

\begin{tabular}{ccccc}
Topology _U_<sub>(_n,i_)</sub> & Direction & LP Value & STT Best Value & Integrality Gap \\
(7,3) & (3,2,0,2,3,3,10) & 29.5 & 30 & 60/59≈1.0169 \\
(8,4) & (9,5,0,6,11,17,5,9) & 93 & 95 & **95/93**≈**1.0215** \\
(8,5) & (16,2,3,6,7,13,34,5) & 121 & 122 & 122/121≈1.0083 \\
(8,6) & (55,1,3,4,14,29,34,8) & 200.5 & 201 & 402/401≈1.0025 \\
(8,11) & (3,2,0,2,3,0,3,10) & 29.5 & 30 & 60/59≈1.0169 \\
(8,12) & (11,1,0,1,2,6,1,2) & 28.5 & 29 & 58/57≈1.0175 \\
(8,13) & (7,1,1,1,7,7,2,7) & 49.5 & 50 & 100/99≈1.0101 \\
\end{tabular}

\begin{tabular}{cccccccc}
Topology _U_<sub>(_n,i_)</sub> & \multicolumn{3}{c}{Direction} & OPT STT & BC STT & WC STT & BC Ratio & WC Ratio \\
(7, 3) & (11, 7, 0, 10, 34, 7, 11) & \* & 184/80 & 186/80 & 220/80 & 1.0109 & 1.1957 \\
(8, 4) & (17, 9, 0, 10, 19, 29, 9, 17) & \* & 277/110 & 281/110 & 339/110 & **1.0144** & 1.2238 \\
(8, 5) & (13, 1, 2, 4, 5, 10, 25, 4) & \* & 154/64 & 155/64 & 178/64 & 1.0065 & 1.1558 \\
(8, 6) & (86, 1, 5, 6, 22, 46, 55, 13) & \* & 552/234 & 553/234 & 658/234 & 1.0018 & 1.192 \\
(8, 11) & (11, 7, 0, 7, 11, 0, 10, 34) & \* & 184/80 & 186/80 & 220/80 & 1.0109 & 1.1957 \\
(8, 12) & (32, 2, 0, 3, 7, 18, 3, 7) & \* & 160/72 & 162/72 & 188/72 & 1.0125 & 1.175 \\
(8, 13) & (48, 6, 5, 6, 48, 48, 15, 48)

\(+\epsilon\cdot(-1,1,1,1,-1,-1,-1,-1)\) & \*\* & \(\frac{558-\epsilon}{224-2\epsilon}\) & \(\frac{563-6\epsilon}{224-2\epsilon}\) & \(\frac{647-7\epsilon}{224-2\epsilon}\) & 1.0090 & 1.1595 \\
(8, 4) & (6, 3, 0, 5, 0, 18, 4, 5) & _p_ & 94/41 & 94/41 & 129/41 & 1 & 1.3723 \\
(8, 4) & (6.5, 3, 0, 5, 0, 18, 4, 5) & \(p'\) & 190/83 & 191/83 & 263/83 & 1.0053 & **1.3842** \\
(8, 13) & (10, 2, 1, 2, 35, 35, 2, 10) & _p_ & 216/97 & 216/97 & 283/97 & 1 & 1.3102 \\
\end{tabular}

2: For each topology with non-STT vertices, we show a primary direction (Definition 2.4) that maximizes the integrality gap among all primary directions. The largest gap overall is marked in bold.

3: For each topology whose LP finds non-STT vertices, we show directions and approximation ratios of the best-case (BC) and worst-case (WC) root rounding. The first 7 rows give one entry per topology with a direction in which even the best-case is sub-optimal. The next rows show additional directions for which the worst-case is among the largest that we found. Directions marked ∗/\*\* were found by the LP in Definition 2.10, _p_ marks primary directions that give large ratios, and \(p'\) marks a small variation to increase the largest gap we found among primary directions. Remark 2.11 explain why in the case of ∗\* we perturb the nice integer direction by \(\epsilon\).

