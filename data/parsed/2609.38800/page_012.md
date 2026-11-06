## 5.2 Selected MaxCut trajectories

Figures 1 and 2 report selected trajectories to illustrate convergence behavior (exact numerical endpoints and extended 10-node trajectory data are deferred to Appendix E). "Variance" is the variance of sampled output energies at a stored parameter vector, not gradient-estimator variance. The horizontal coordinate is the archived nominal shot count and should not be read as exact matched exposure.

The EfficientSU2 example is a genuine favorable case for non-recursive CRVG: at 15 nodes it reaches best energy -9.34, versus -7.09 for SPSA, and ends with lower sampled-energy variance and entropy. This behavior does not transfer uniformly. Under QAOA, SPSA and non-recursive CRVG are nearly tied at -9.11 and -9.16, while recursive CRVG reaches -10.29. The reversal across circuit families argues for SPSA when robustness and minimal tuning are more important than exploiting a favorable, pre-identified CRVG regime.

## 5.3 Cross-instance and synthetic-noise evidence

Figure 3 consolidates relative converged performance and synthetic-noise stability. Negative best-CRVG-minus-SPSA energy margins favor the best CRVG variant. The clean comparison in panel (a) contains a substantial CRVG-favorable EfficientSU2 subset, but QAOA is much more balanced, consistent with the 16-14 split in  3. Because best- of-CRVG gives two variants an opportunity to beat one SPSA run, a near-balanced split is conservative evidence for SPSA’s competitiveness. The lower panels use separate clean and noisy instance pools under depolarizing and readout channels; they show that both optimizer families remain operational under the archived noise model, not the causal effect of noise on group medians.

## 5.4 MaxCut QAOA depth and parameter setting

Figure 4a compares the three local MaxCut methods over 36 paired instances per depth. Quality is non-monotone with depth. Best-of-CRVG beats SPSA on 13, 22, 21, and 23 instances at depths one, three, five, and seven, respectively. Yet the method-level medians show why SPSA remains a strong default: at depth three all methods are nearly equal (0.883, 0.881, and 0.879 for SPSA, non-recursive CRVG, and recursive CRVG), SPSA has the highest median at depth five, and recursive CRVG degrades sharply at depth seven. Non-recursive CRVG’s depth-seven median of 0.863 versus SPSA’s 0.843 is an important exception.

Figure 5a isolates solution quality from resource exposure. At depth one, non-recursive CRVG uses more calls than SPSA (\(1.09\times\)), while offering the same median ratio. At depths three, five, and seven it uses about \(0.79\times\) the calls. Recursive CRVG uses still fewer calls, but its depth-seven quality loss demonstrates that lower exposure is not sufficient<tbc>

\begin{tabular}{cccccc}
Study & Instances & Nodes & Ansatz & Simulator & Seed \\
EfficientSU2 benchmark & 30 & 11-30 & EfficientSU2 & statevector/MPS & 42 \\
EfficientSU2 noise subset & 5 & 12-16 & EfficientSU2 & statevector & 42 \\
QAOA benchmark & 30 & 10-17 & QAOA & statevector & 42 \\
QAOA noise subset & 10 & 10-17 & QAOA & statevector & 42 \\
Selected MaxCut trajectories & 2 & 10-15 & EfficientSU2/QAOA & statevector & 42 \\
QAOA depth comparison & 144 & 10-20 & QAOA depths 1/3/5/7 & finite-shot/exact statevector & 42 \\
MIS QAOA depth comparison & 144 & 10-20 & QAOA depths 1/3/5/7 & finite-shot statevector & 42 \\
Selected MIS trajectories & 4 & 14-18 & EfficientSU2 & statevector & 42 \\
\end{tabular}

\begin{tabular}{ccccccc}
Study & _n_ & CRVG wins & Ties & SPSA wins & Median margin & Simulator \\
EfficientSU2 benchmark & 30 & 20 & 0 & 10 & -0.781 & statevector/MPS \\
EfficientSU2 noise subset & 5 & 5 & 0 & 0 & -1.316 & statevector \\
QAOA benchmark & 30 & 16 & 0 & 14 & -0.008 & statevector \\
QAOA noise subset & 10 & 6 & 0 & 4 & -0.014 & statevector \\
\end{tabular}

2: Frozen experiment artifacts used in this report. Each row is descriptive evidence from archived outputs, not a newly executed benchmark. Noise subsets use depolarizing and readout channels and are unpaired with the clean sets.

3: Instance-level comparison of the best CRVG variant with SPSA. A negative margin favors CRVG. Counts summarize one optimizer seed per instance and are not uncertainty estimates. Clean and noisy rows contain different, unpaired instances.

