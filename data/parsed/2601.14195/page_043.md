<tbc>all agents rank roughly a quarter of the other agents. Still, on average, it is possible to find a maximum-cardinality matching where every agent is in fewer than two blocking pairs. When eliminating the maximum-cardinality requirement, the results greatly improve - with only a minor trade-off in size, more than half of the instances become solvable across all settings, and the expected maximum number of blocking pairs per agent becomes much fewer than 1.

For the smi instances, we also find that stable maximum-cardinality matchings are rare when preference lists are short - only around 0.2% of instances admit such matchings when _n_=100 and _l_=5, and none of the generated instances do when _n_=200 and _l_=5. However, the situation improves significantly when the preference list length increases. Notice the special case when _n_=50 and _l_=25: in the smi setting, this means that each side has \(\frac{n}{2}=25=l\) agents, so preference lists are complete and thus a stable perfect matching must always exist. We highlight that, as expected, the ratio of instances that admit stable maximum-cardinality matchings is higher for smi than for sri, but interestingly the average maximum number of blocking pairs per agent is larger when _l_=5; this is likely because the edges are more concentrated in smi instances compared to sri instances with the same number of agents and the same preference list length, so maximising for size might require a stronger sacrifice in stability.

Beyond average numbers, it might be interesting to know the maximum of the minimax number of blocking pairs per agent under the maximum-cardinality requirement. We show data for this (in the columns titled m-mm-bp), as well as the average time required to solve the ILP models to optimality, in  2. It is notable that the encountered worst case instances still have a small minimum maximum number of blocking pairs, certainly much fewer than the theoretical worst case instances that we constructed in Section 3.3, and that when eliminating the maximum-cardinality requirement, none of the 27,000 sri instances across the nine different settings required any agent to be in more than one blocking pair. The data in the table also shows that our ILP models can be solved very quickly in the parameter regimes that we considered. Naturally, the number of variables and constraints grows proportionally to the number of agents and the preference list lengths, and thus, the required time to solve the ILP models grows proportionally too. However, even when _l_=25, all sets of instances can be solved in fewer than 5 seconds on average.

Overall, we can draw two positive conclusions from these experiments: in practice, it is unlikely to encounter instances that require more than one blocking pair per agent when preference lists are sufficiently large, and our ILP formulations are a very viable option to solve our NP-hard optimisation problems of interest in practice, despite the strong intractability results that we encountered throughout this paper.

\begin{tabular}{ccccccccccc}
 & & \multicolumn{6}{c}{sri} & \multicolumn{3}{c}{smi} \\
 & & \multicolumn{3}{c}{Minimax-Max} & \multicolumn{3}{c}{Minimax} & \multicolumn{3}{c}{Minimax-Max} \\
 & & size & stable & a-mm-bp & size & stable & a-mm-bp & size & stable & a-mm-bp \\
\multirow{3}{*}{_n_=50} & _l_=5 & 25.00 & 4.30% & 0.96 & 23.48 & 77.37% & 0.23 & 24.89 & 6.03% & 1.01 \\
 & _l_=15 & 25.00 & 48.17% & 0.52 & 24.76 & 60.63% & 0.39 & 25.00 & 89.00% & 0.11 \\
 & _l_=25 & 25.00 & 66.30% & 0.34 & 24.98 & 67.17% & 0.33 & 25.00 & 100.00% & 0.00 \\
\multirow{3}{*}{_n_=100} & _l_=5 & 50.00 & 0.07% & 1.45 & 47.02 & 78.20% & 0.22 & 49.74 & 0.20% & 1.50 \\
 & _l_=15 & 50.00 & 13.20% & 1.08 & 49.40 & 51.77% & 0.48 & 50.00 & 21.07% & 0.90 \\
 & _l_=25 & 50.00 & 18.27% & 0.85 & 49.88 & 54.30% & 0.46 & 50.00 & 21.37% & 0.79 \\
\multirow{3}{*}{_n_=200} & _l_=5 & 100.00 & 0.00% & 1.68 & 94.03 & 77.97% & 0.22 & 99.38 & 0.00% & 1.80 \\
 & _l_=15 & 100.00 & 2.17% & 1.84 & 98.78 & 47.77% & 0.52 & 100.00 & 2.50% & 1.76 \\
 & _l_=25 & 100.00 & 6.67% & 1.61 & 99.66 & 41.47% & 0.59 & 100.00 & 5.70% & 1.61 \\
\end{tabular}

1: Experimental results: Averages

