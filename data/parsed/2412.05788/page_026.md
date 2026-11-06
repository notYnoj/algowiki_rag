<tbc>success rate and the lowest average scRMSD and motif RMSD between the two motifs. For TDS-RMSD, several had high unique success rates, but we chose \(\gamma=2.0\) and \(\zeta=0.4\), which yielded the lowest scRMSD.

With TDS-frame-dist, an additional parameter \(\eta_\mathrm{chiral}\) is available to scale the chiral contribution of the rotation deviations to the likelihood. When \(\eta_\mathrm{chiral}=0\), we retrieve back TDS-dist. Due to the large parameter space, we limit our search to a fixed temperature value of \(\zeta=0.4\) to match TDS-dist. As shown in Fig. 10, a non-zero rotation scale indeed corrected for reflections from as little as \(\eta_\mathrm{chiral}=0.5\). However, as with 1PRW, there was a range of values between 0.5 and 4.0 where the rotation contribution was too weak, increasing the motif RMSD as it attempted to steer the trajectory away from solutions that meet the distance constraints to those with the correct handedness. When the scale was too large, solutions had the correct handedness but incorrect distances, leading to malformed backbones. Here, the scRMSD was at its highest. We found that the values \(\eta_\mathrm{chiral}=32.0\) and \(\gamma=0.25\) balance this trade-off but remark that the optimal value differed in the case of both motifs. For example, zero chiral contribution was necessary for motif problem 3IXT.

In summary, however, we acknowledge that our approach to hyperparameter tuning is limited. In particular, optimising for two select motifs is not guaranteed to generalise to other motif problems with different sizes, contiguity, and frequency in the data distribution. Where we can, we highlight possible reasons for our observations to help make more informed choices in the future. Furthermore, the computational expense of the procedure could not permit larger sample sizes in tuning nor a separate search for hyperparameters in the multi-motif case. Our results can certainly be improved, and the demonstrated albeit limited success in select multi-motif problems points to the feasibility of zero-shot approaches.

TDS-DIST, noise = 0.4
TDS-MASK, noise = 0.4
TDS-DIST, noise = 0.7
TDS-MASK, noise = 0.7
TDS-DIST, noise = 1.0
TDS-MASK, noise = 1.0
1PRW
3IXT
F1(1PRW, 3IXT)
30
Unique Scaffolding Success Rate (%)
5
15
20
10
0
10
5
100
100
100
Correct Helix Handedness Rate (%)
50
75
90
10
7.5
5.0
5
5.0
2.5
1.5
1.5
1.25
Average Motif RMSD
1.0
1.00
1.0
0.75
5.0
4
4
Average ESS
2.5
2
2
0.0
0.25
0.5
1.0
2.0
4.0
0.0
0.25
0.5
1.0
2.0
4.0
0.0
0.25
0.5
1.0
2.0
4.0
Guidance Scale γ

Figure 8: **Hyperparameter grid search for TDS-dist and TDS-mask**. The rates at which unique success and right-handed helices were achieved are reported. Average values for two of the four designability criteria are also shown. The right column depicts the F1 score between the values in the left and middle columns. TDS-dist with \(\gamma=4.0\) is not shown in problem 1PRW, as it had numerical overflows in its backbone coordinates.

