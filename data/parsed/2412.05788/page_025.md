## D Additional Results

### D.1 Hyperparameter Search

The hyperparameters of each method were chosen to maximise performance on two selected motif problems, 1PRW and 3IXT. In a discretised grid-search fashion, 16 backbones are sampled and evaluated for each parameter combination. A key hyperparameter we consider is the diffusion model’s _noise_ or _temperature scale_ \(\zeta\in(0,1]\) that scales the noise added to each step in the reverse process. A high \(\zeta\) leads to higher sample diversity, and a low \(\zeta\) typically yields higher sample quality. The Genie models have been shown to attain the best F1 designability-diversity score for unconditional generation at around \(\zeta=0.4\) (Lin and Alquraishi, 2023). However, the effect of this setting on the conditional samplers wrapped around the model is unclear. We tested three values \(\zeta=0.4,0.7,1.0\) to gauge the impact on sampler performance. The proposals of the samplers, all of which were Gaussian, had their standard deviation scaled by this value.

Fig. 7 shows that, for the replacement methods, lower values indeed improved the scRMSD but had different effects on motif RMSD depending on the motif. We suspect that with minimal noise, motifs common to backbones lying in the modes of the data distribution are easily scaffolded, whereas those outside are not. We chose \(\zeta=0.4\) for both replacement methods to prioritise a lower scRMSD, given the motif RMSD was already near the success threshold.

In reconstruction guidance, an additional hyperparameter we consider is the guidance scale \(\gamma\) that controls the strength of the conditional signal. For high \(\gamma\), the target distribution becomes more peaky, and the adherence to the conditional label is higher at the cost of diversity. We consider six values in \(\gamma=0,0.25,0.5,1.0,2.0,4.0\). Notably, \(\gamma=0\) is identical to BPF under a likelihood involving the reconstructed sample and the label. Fig. 8 shows results for TDS-mask and TDS-dist. For TDS-mask, we chose \(\gamma=1.0\) and \(\zeta=1.0\), one of the two with the best unique success rate but with the lower average scRMSD. Owing to the reflection-invariance of TDS-dist, higher guidance scales made it produce reflected motifs up to 50% of the time. We found this issue less pervasive with a smaller guidance scale, where the unconditional model, informed on handedness, makes a bigger contribution to the de-noising process. We therefore configured TDS-dist at \(\gamma=0.25\) and \(\zeta=0.4\). As for TDS-fape and TDS-rmsd, there were no issues whatsoever with reflected motifs. Fig. 9 shows their grid search metrics. We chose \(\gamma=0.5\) and \(\zeta=1.0\) for TDS-fape, as it had the highest unique<tbc>

FPSSMC
MCGDIFF
1PRW
3IXT
F1(1PRW, 3IXT)
0.05
Unique Scaffolding Success Rate (%)
5
20
0.00
0
0
0.05
Average scRMSD
8
7.5
7.5
6
5.0
5.0
0.85
1.5
1.0
Average Motif RMSD
0.80
1.0
0.75
0.8
5.0
5.0
5.0
Average ESS
2.5
2.5
2.5
0.4
0.7
1.0
0.4
0.7
1.0
0.4
0.7
1.0
Noise Scale '

Figure 7: **Noise scale grid search for FPSSMC and MCGDIFF**. The unique success rate and average values for two of the four designability criteria are shown. The right column depicts the F1 score between the values in the left and middle columns.

