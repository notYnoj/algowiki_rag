### 6.3 DCMCF exact solving

The DCMCF was solved using a branch-and-bound algorithm. The 4 relaxations presented above (BIG-M, S, T and CONVEX) were implemented and compared. s 1 shows, for each SND-lib instance, the respective performances of these formulations: either the solving time if an optimality gap of 0.1% was reached within 1 hour, or the optimality gap if it was above 0.1% after this time limit. For the randomly generated instances, the proportion of random instances solved after a given solving time or, for instances not solved after one hour, the residual gap, are shown in Figure 7.

The CONVEX formulation provides a tighter relaxation of the problem than the lighter BIG-M relaxation, at the expense of its solving time. These effects balance each other on instances of the SND-Lib, where the CONVEX formulation outperformed the BIG-M one (either in terms of gap after one hour or solving time if optimality is reached before that time limit) in 11 instances over 19. On the randomly generated instances, however, the lighter BIG-M relaxation proves more efficient on 77 of the 126 instances tested.

The S and T formulations provide good trade-offs between tightness and relaxation solving time, allowing them to outperform both the BIG-M (on 12 and 13 instances of the SND-Lib and 72 and 64 randomly-generated instances, respectively). The dominance of the S relaxation, illustrated in Figure 6, does not materialize when solving the exact DCMCF problem in a branch-and-bound scheme: the S relaxation is more efficient than T in 8 of the 19 SND-Lib instances and 72 of the 126 random instances.

## 7 Conclusion

The Delay-Constrained Multi-Commodity Flow (DCMCF) problem was known to be NP-hard. In this paper, we proved that the problem is strongly NP-hard, even in the case of three commodities that share the same source and destination, and where each commodity is allowed to use every possible path.

