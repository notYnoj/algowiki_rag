<tbc>`L17\_seed424`: The seed pool held a single solution at size 68, which the implementation pairs with the best solution at size 67 (Section IIB). The exchange of this one pair produced configurations at sizes 69 and 70, and a second pass found 2 solutions at size 70 (+2 atoms).

`L17\_seed46`: The seed pool held 4 solutions at size 67. Three passes reached size 69 and then 70, ending with 15491 solutions at size 70 (+3 atoms), all _strictly better_ than every seed.

The seeds are near-optimal configurations that happen to differ structurally in ways that, when recombined through cluster exchange, produce new configurations of size _k_+1 or larger. All 15511 solutions at the improved sizes passed independence, maximality, and target-cardinality validation (100% success rate). Except on `L12\_seed829`, these sizes remain below the certified optima ( I), so those configurations are maximal rather than maximum independent sets.

We emphasize that these improvements do not amount to recovery of the true optimum. Only `L12\_seed829` reaches its true optimum. The two `L17` instances end one atom short, and the three suboptimal `L16` instances do not improve ( I). These gaps are a direct consequence of the non-ergodicity discussed in Section IVC. Classical recombination thus extracts strictly more from a fixed quantum sample than the hardware reports on its own, but it does not close the gap to the optimum in general: the qReduMIS pipeline of Ref. [7] reaches all nine of these optima, and exact methods certify them (Section IIF). A local search from the same seeds reaches the same sizes on `L12\_seed829` and `L17\_seed46`, and one atom less on `L17\_seed424` at equal cost ( I, Section IVA).

That improvements occur only on hard instances is not coincidental. These are precisely the instances where quantum hardware leaves the largest gap to the optimum, and hence where recombination of near-optimal seeds has room to help. The size of the seed pool does not decide the outcome: `L17\_seed424` improved from a single seed at its best size, while `L16\_seed4392` did not improve from 20, nor `HP1435` from 107. What decides it is the mechanism of Section IIC. A size improvement requires a cluster that is imbalanced between the two parents, and the three instances that improved are exactly the three whose seed pairs contain one (17 of 2016 pairs for `L12\_seed829`, all 6 for `L17\_seed46`, and the single mixed-size pair of `L17\_seed424`). None of the 5671 pairs of `HP1435`, or of the pairs of the other four suboptimal instances, contains one.

## E. Manifold Coverage

Because the reference data set records the exact degeneracy _D_<sub>MIS</sub> of the ground-state manifold alongside the optimum size, the coverage achieved by the method can be measured directly rather than merely bounded. Figure 5 shows this for the 35 instances whose quantum seeds<tbc>

<tbc>already sit at the certified optimum, the only instances for which the question is well posed. The 8 excluded are the shortfall instances of Section IIF.

Coverage spans five orders of magnitude, from 0.001% to 100%, with a median of 26.2%. At the top of that range the non-ergodicity of the method is not a limitation at all: on six instances the recovered pool is provably the _complete_ ground-state manifold (`L3\_seed3849` 3/3, `L5\_seed4703` 2/2, `L7\_seed3799` 14/14, `L5\_seed2142` 16/16, `L9\_seed205` 36/36, and `L11\_seed4915` 36/36), and two further instances exceed 94% (`L8\_seed4578` 463/479, `L8\_seed4996` 447/474). For these, cluster exchange from the quantum seeds enumerates the manifold exhaustively rather than sampling it, as certified against the exact degeneracies of Section IIF. All eight lie at the small end of the test bed, spanning 7 to 97 atoms against a median of 115 across the instances plotted, which is the regime in which a few hundred measurements can cover a manifold outright.

Coverage falls steeply as the manifold grows (Spearman \(\rho=-0.79\), \(p=2\times 10^{-8}\)): the median is 100% for the seven instances with _D_<sub>MIS</sub>_\<_10<sup>2</sup> but only 1.1% for the sixteen with \(D_\mathrm{MIS}\ge 10^4\). The largest manifold belongs to `HP1478`, the instance with the highest amplifi<tbc>

Benchmark
106
Hard
Standard
Fit: N x t0.89 (R2 = 0.93)
105
Final solution count Ntotal
104
103
102
101
100
10-4
10-3
10-2
10-1
100
101
102
103
Cluster-update time t (s)

FIG. 6. Computational efficiency: cluster-update time versus final solution count. The one-off repair of the raw hardware samples is excluded here and is reported separately in the text, since its cost is set by the number of measurement shots rather than by the manifold recovered. All 43 instances completed their cluster-update phase in under 10 minutes on a standard laptop [15], with the largest manifold of approximately 2 million solutions requiring only 580 seconds. The 40 instances plotted exclude the three improvement instances, whose runs span two levels and are discussed separately (Section IIID). The base-10 log-log scale reveals a near-linear scaling, \(N_\mathrm{total}\propto t^{0.89}\) (_R_<sup>2</sup>=0.93; dashed line), with substantial residual scatter. The hard cutoff of 10<sup>5</sup> pair comparisons was never required.

