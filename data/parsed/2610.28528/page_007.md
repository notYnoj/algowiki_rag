<tbc>of Ref. \[19\] illustrates the distinction for two paradigmatic spin-glass instances, where a manifold made of many disconnected components in configuration space limits what any recombination move can reach, while a connected one does not.

The adaptive stopping criterion distributed efficiently across instances: 38 of 43 reached exhaustive pairwise exploration, while 5 saturated before processing all pairs, indicating early convergence on large manifolds. The maximum number of pairs processed in any pass was 16539, well below the 10<sup>5</sup> pair hard cutoff, confirming that the saturation heuristic reliably identifies manifold boundaries without wasting computation time. We stress that "exhaustive" here refers to processing every pair _within the given seed pool_. Such coverage still explores only the manifold region reachable from those seeds (Section IVC), and does not imply discovery of the complete ground-state manifold or of the global optimum.

## B. Amplification Patterns Across Problem Types

Amplification behavior differs systematically across the three instance families, reflecting distinct relationships between quantum seed quality and manifold structure.

**Benchmark instances** with a hardness parameter \(H\in\{1.478,14.12,125.5,1435\}\), 137 atoms each, span a wide range of amplification. We retain the labels of Ref. \[7\], which suppress the decimal point of _H_, so that `HP1478` denotes _H_=1.478 while `HP1435` denotes _H_=1435, and _H_ is quoted at each mention below. Am<tbc>

<tbc>plification ranges from 2.7\(\times\) to 11923\(\times\). The low end is set by instance `HP125`, for which quantum hardware returned only 3 seeds, leaving little structural diversity for cluster exchanges to exploit. The other three instances all amplify by at least 79\(\times\). Across all 43 instances, amplification shows no significant correlation with _H_ (Spearman \(\rho=-0.03\), _p_=0.86), and coverage over the 35 instances of Section IIIE shows none either (\(\rho=-0.17\), _p_=0.33). Within this family the pattern is nonmonotonic: for the easiest instance, `HP1478` (_H_=1.478, QAA success rate 35.2% \[7\]), the algorithm achieves the highest amplification of any instance in the dataset, expanding 165 quantum solutions to 1967339 configurations, yet the hardest instance, `HP1435` (_H_=1435, QAA success rate close to 0%), still achieves 1104\(\times\) amplification from 107 initial solutions, albeit at size 44, one atom below its true optimum of 45, so that the amplification enlarges a sub- optimal manifold, while the intermediate-hardness `HP125` (_H_=125.5) amplifies by only a factor 2.7\(\times\). Amplification is thus governed less by hardness per se than by the size of the accessible degenerate manifold, the structure of the ground-state manifold, and the size of the quantum seed pool. In this case `HP1478` combines a low-hardness, large-manifold landscape with a rich seed pool (165 solutions), whereas `HP125` is limited by its small initial seed pool (3 solutions). As such, having more solution candidates, even at less-than-optimal MIS sizes, might help in the amplification process.

**Hard instances** (115 - 231 atoms) span the widest range of amplification: the six instances whose size did not change (shown in Figure 2) amplify by 2.5\(\times\) to 6366\(\times\) (`L16\_seed4392`, 20 seeds to 127329 configurations). They<tbc>

105
Benchmark
Hard
Standard test bed
104
Amplification factor A
103
102
101
100
10-1
HP1412
HP1435
HP1478
HP1478
L12_seed2922
L15_seed3591
L16_seed2871
L16_seed798
L16_seed4392
L5_seed3849
L5_seed4703
L7_seed3799
L9_seed205
L8_seed4996
L8_seed4578
L12_seed1370
L14_seed2358
L13_seed2894
L11_seed4915
L14_seed1590
L14_seed1961
L13_seed4503
L14_seed1518
L16_seed1334
L13_seed1751
L15_seed1098
L14_seed2012
L12_seed928
L16_seed2635
L12_seed4838
L16_seed4816
L13_seed1569
L13_seed1374
L14_seed2867
L14_seed2763
Problem instance

FIG. 2. Amplification across the 40 problem instances whose best independent-set size did not change under post-processing; the three instances where classical post-processing found a strictly larger independent set are shown separately in  I. The bar chart shows the amplification from initial quantum solutions to the final post-Houdayer solution pool on a base-10 log scale. Instances are grouped by type (Benchmark, hard, and standard). Across the full 43-instance dataset, amplification factors range from 1.0\(\times\) to 11923\(\times\) with a median of 24.3\(\times\).

