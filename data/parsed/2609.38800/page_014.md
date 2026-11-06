## 5.6 Limitations and practical recommendation

The evidence uses one optimizer seed per instance, noisy best-of-trajectory selection, unequal realized call exposure, and simulator-specific wall time. Across-instance dispersion is not optimizer stochastic uncertainty. External MaxCut baselines are unmatched contextual results, while MIS has no corresponding external baseline. Output-energy variance measures sampled outcomes rather than gradient-estimator variance, and final MIS feasibility requires an additional diagnostic resampling.

The single-seed limitation is partially mitigated on one QOBLIB MIS instance (`ibm32`, 32 nodes): repeating non- recursive CRVG and SPSA over three seeds there, non-recursive CRVG’s mean repaired ratio (0.753) remains well above SPSA’s (0.387), so this particular quality gap is not an artifact of the single seed used elsewhere. This is one instance out of the many studied and does not by itself establish seed-robustness across the full evidence base.

Subject to these limitations, SPSA is the recommended default in the tested regimes: it is competitive across circuit families, avoids recursive CRVG’s pronounced depth-seven degradation, wins most MIS instances at three of four depths, and requires neither anchor scheduling nor selection between CRVG variants. CRVG should be treated as a targeted alternative when pilot experiments identify an amortizable regime, notably non-recursive CRVG with EfficientSU2, non-recursive CRVG for MaxCut at depth seven, and both CRVG variants for MIS at depth three. A confirmatory study should use paired initializations and multiple seeds, count every anchor and diagnostic circuit, stop at exact matched shot budgets, and measure estimator error against exact gradients on tractable instances.

## 5.7 A preliminary real-hardware check

The results above are entirely statevector or MPS simulation. As a first, deliberately small step toward the confirmatory study called for above, we evaluated already-converged parameters from the EfficientSU2 sweep directly on real IBM Quantum hardware, without any on-hardware re-optimization. We took the converged \(\theta\) from a single 18- node Erdős-Rényi instance (`000\_18nodes\_erdosrenyi30percent`, _p_=144 EfficientSU2 parameters, transpiled to `isa\_depth`=95) for SPSA and non-recursive CRVG at two seeds, and submitted one `SamplerV2` circuit evaluation<tbc>

Energy
Concentration
Output diversity
25
10 nodes
10 nodes
10 nodes
7.50
2
20
7.25
0
Bit-string entropy (bits)
15
7.00
Sampled mean energy
Output-energy variance
-2
10
6.75
-4
6.50
5
-6
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
2.5
15 nodes
35
8.0
15 nodes
15 nodes
7.9
0.0
30
Bit-string entropy (bits)
-2.5
25
7.8
Sampled mean energy
Output-energy variance
7.7
-5.0
20
7.6
-7.5
15
7.5
-10.0
10
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
0.0
0.5
1.0
1.5
Archived nominal shots (106)
Archived nominal shots (106)
Archived nominal shots (106)
SPSA
non-recursive CRVG
recursive CRVG

Figure 2: Selected QAOA MaxCut trajectories. The optimizer ordering changes with the ansatz: recursive CRVG recovers, while SPSA and non-recursive CRVG are close in best energy on the 15-node case. Non-recursive CRVG no longer has the output-variance and entropy advantage seen with EfficientSU2.

