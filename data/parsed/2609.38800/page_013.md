<tbc>for optimizer selection. SPSA therefore offers a transparent baseline with stable quality, while CRVG’s call savings are valuable only when its depth-specific quality is retained.

A detailed, granular breakdown of resource exposures and comprehensive comparisons against external exact-statevector parameter-setting baselines are deferred to Appendix E. While local methods compare favorably with several Fourier and TQA techniques on matched support, optimized fixed-angle and interpolation approaches often lead at higher depths. These mixed results strengthen the practical case for SPSA as a simple local baseline rather than supporting the universal superiority of any stochastic optimizer.

## 5.5 MIS QAOA depth study

The MIS study repeats the three local methods on the same 36 instances at each QAOA depth. There is no exact MIS approximation-ratio normalization or external MIS parameter-setting baseline, so we use paired penalized-cost margins and the raw feasible-sample fractions in Fig. 4b. Lower penalized cost is better. Average and maximum feasible size are undefined when the final diagnostic sample contains no feasible string.

Depth three is the clear CRVG-favorable exception: best-of-CRVG wins 33 of 36 instances with median paired cost difference -0.438. The pattern reverses at depths one, five, and seven, where SPSA wins 24, 22, and 20 instances and the median paired differences favor SPSA. SPSA also retains full valid support for the feasible-size diagnostics at depths three, five, and seven; at depth seven its median feasible fraction is 68.6%, compared with 52.3% for non-recursive and 11.5% for recursive CRVG. This cross-depth consistency supports SPSA as the safer MIS default even though CRVG is compelling at depth three.

Figure 5b shows that both CRVG variants generally use fewer calls than SPSA (exhaustive resource tables are provided in Appendix E). The central selection tradeoff is therefore explicit: CRVG reduces sampled-objective exposure, but at three of four depths that reduction accompanies worse paired cost outcomes. When solution reliability across an unknown depth is prioritized over call count alone, the archive favors SPSA; when depth three is known to be representative, CRVG offers a favorable quality-resource combination.

Energy
Concentration
Output diversity
10 nodes
80
10 nodes
10 nodes
5.0
6
2.5
60
Bit-string entropy (bits)
0.0
40
4
-2.5
-5.0
20
2
-7.5
0
0
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
15 nodes
15 nodes
8
15 nodes
2
50
Bit-string entropy (bits)
0
40
7
Sampled mean energy
-2
30
-4
6
-6
20
5
-8
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

Figure 1: Selected EfficientSU2 MaxCut trajectories. Non-recursive CRVG reaches the lowest energy in the favorable 15-node example and concentrates the sampled output distribution, whereas recursive CRVG stalls. The instability of one CRVG variant and unequal logged endpoints make SPSA the more predictable baseline even though it is not best in this selected regime.

