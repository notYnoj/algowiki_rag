## 4.3 Multi-Motif Scaffolding

We tested the non-linear guidance potentials paired with TDS on the six multi-motif problems from the Genie2 benchmark. In our initial assessment, where 32 designs were produced for each problem, none of the methods succeeded, but some designs narrowly missed the success criteria. Our reference, conditionally trained model Genie2, solved four problems with less than 20 unique successes among 1000 samples for each problem. To match the same order of magnitude in samples, we chose the most promising method, TDS-rmsd, and produced 512 samples for problems 1PRW\_two and 3BIK+3BP5. Our choice is motivated by the observation that some TDS-rmsd designs in the two problems were successful when an alternate motif sequence was used. In our larger batch of samples, TDS-rmsd found one unique success in each problem. Fig. 4 summarises our findings.

First, we review our initial assessment, where there is an apparent dynamic between the distance approaches. We found that, independent of the number of motifs, TDS-dist was more likely to produce reflections when motifs had discontinuities, as indicated by its lower proportion of samples with correct handedness. TDS-frame-dist had fixed this issue in virtually all samples, only behind TDS-fape and TDS-rmsd, which maintained the correct handedness throughout. Unlike the latter two, TDS-frame-dist has an additional hyperparameter \(\eta_\mathrm{chiral}\) that scales the chiral contribution of the likelihood. We hypothesise that a good setting should account for the contiguity of motifs, but a principled choice is difficult to make a priori. For these reasons, TDS-fape and TDS-rmsd may be more suitable, as they work right out of the box.

In our attempt to scaffold two multi-motif problems with more samples, TDS-rmsd could only produce one unique success out of 512 generated backbones. Echoing our findings in the single-motif case, we attribute this to our fixed motif placements and the lack of sequence information in our inverse problem formulation, both of which are addressed by our baseline in Genie2. To put this in perspective, there are around one million possible motif placements for 1PRW\_two, varying between 120 and 200 residues in total length. With the goal of demonstrating the feasibility of our setup, we used the same placements as our initial assessment, which, from our metrics, had hinted at its suitability. A variable motif placement is especially crucial for 3BIK+3BP5, as nearly all designs were grouped in the same cluster. Moreover, without accounting for sequence information, we may need to sample far more to cover the subset of backbones that can be attained by folding an amino acid chain containing all the motifs’ sequences. This is evidenced by the higher number of successes among methods when the motif sequence is not fixed in the evaluation process (see App. D.2).

(A)
TDS-DIST
TDS-FRAME-DIST
TDS-FAPE
TDS-RMSD
(B)
Average scRMSD (4)
10
0
10
1PRW_two
scRMSD < 2A
0
scRMSD = 1.822A motif RMSD = 0.872A pLDDT = 82.877 pAE = 4.252
Average Max Motif RMSD (4)
10
0
25
Max Motif RMSD < 1A
0
3BIK+3BP5
Correct Helix Handedness (%) (7)
100
scRMSD = 0.901A motif RMSD = 0.926A pLDDT = 85.044 pAE = 2.939
0
1PRW_four 1PRW_two
3NTN
3BIK+3BP5
2B5I
4JHW+5WN9

Figure 4: **(A) Success metrics of sampling methods on the six multi-motif scaffolding benchmarks.** Thirty-two scaffolds are sampled for each problem. Values for a pass in each criterion are denoted by the dashed line. Error bars shown are one standard deviation from the mean. Only samples with correct handedness were considered. **(B) Examples of successful designs from the 512 samples generated via TDS-rmsd.** The motifs, in colour, are aligned with the scaffold, in white.

