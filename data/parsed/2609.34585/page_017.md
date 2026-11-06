<tbc>on a subset of our test instances (8, 4, and 2 instances at _n_=500, 1000, and 10000 for TSP, and 8 graphs for MIS), and report the mean per instance after a warm-up instance or batch. Batched solvers (DRHG, SIL, LEHD, BQ-NCO, iSCO, ReSCO) are timed on batches of 2 to 8 instances, and the batch time is divided by the batch size, which overstates their per-instance cost relative to the batch sizes in their papers. MCTS pipelines run the search of Fu et al. (2021) at the time limit of the respective codebase. The limit is 0.1 seconds per city for DIFUSCO, DIMES, SoftDist, and the controls of Pan et al. (2026), and 0.04 seconds per city for Att-GCN and UTSP, so their runtime is set by that budget plus the heatmap time. Methods without public code (DISCO, CADO, HyCO, PCI, HyperNS) or without released weights for our benchmarks (DIMES on MIS, GFlowNets, LwD, DiffUCO, SDDS) have no runtime, as do settings that exceed the 24 GB memory of the card (T2T and Fast T2T sampling at _n_=10000). Our own TSP-10000 row exceeds the memory of the card as well, since its 40 rollouts do not fit in 24 GB at once. We run it on an RTX 5090 (340 seconds per instance) and scale the time by the 4090-to-5090 runtime ratio of TSP-1000 at the same _K_ and _D_ (4.43 to 4.13 seconds), which gives the 364 seconds in  2 with the unrounded timings. Our own runtimes use the full test sets in batches of 320 rollouts (for example, 32 instances at _K_=10 and 8 at _K_=40) and exclude the first batch, which includes compilation. The MIS _K_=200 point uses 6 graphs in batches of 2.  6 lists the parameter counts of the inference networks.

## E NOTES ON THE MAIN TABLES

**Sources of the quality numbers.** Every quality number of a compared method is the one reported in its own paper, in its main sampling setting. Where a paper does not cover one of our benchmarks but a compared paper evaluates the method on it, we use that number. DiffUCO and SDDS on ER- \[700-800\] are the re-implementations of Feng et al. (2026b), LwD’s ER number is the rerun of Qiu et al. (2022), and T2T and Fast T2T at _n_=10000 for TSP are evaluated by Zhao et al. (2025) and Ma et al. (2025). Zero heatmap and GT-Prior are the heatmap-free controls of Pan et al. (2026). For TSP, where a paper prints only the length or only the gap, the other is derived against our reference, and where it uses another reference, the gap is recomputed against ours.

**Own instance sets.** The dagger marks methods evaluated on their own generated instances of the same distribution, with the gap against their own reference run. Where a method’s code and checkpoints are released, we re-evaluate it on our test sets in the setting of its paper row and report that number without a dagger. These are COExpander with and without RLSA on both MIS benchmarks, and UDC, BQ-NCO, DRHG, and LEHD on TSP. Their full-set results agree with their own-instance numbers to within 0.1 points, except for COExpander with RLSA (45.27 against 44.98 on ER-\[700- 800\] and 425.45 against 425.32 on SATLIB) and DRHG at _n_=500 (0.23% against the reported 0.11%, with either released checkpoint). The remaining daggers are HyCO and GFlowNets on both MIS benchmarks, LwD on SATLIB, and PCI at _n_=500 and 1000, whose code or checkpoints are not released. Lengths and sizes on different instances are not directly comparable, so the gap is the number to compare.

**Type and Search columns.** In  1, S + RL combines supervised and reinforcement learning, as supervised pretraining followed by RL fine-tuning for CADO and as an RL constructor whose solution prefix is completed by a supervised diffusion model for HyCO. S + self is supervised train<tbc>

\begin{tabular}{ccc}
Method & MIS & TSP \\
Moco & 0.36M & 0.85M \\
T2T / Fast T2T & 1.34M & 5.33M \\
DIFUSCO / DISCO & - & 5.33M \\
CAM & 0.18M & 5.20M \\
UDC & 4.35M & 1.56M \\
DRHG & - & 2.65M \\
HyperNS (heatmap network only) & - & ∼11.1M \\
TRM4CO & 6.83M & 6.96M \\
\end{tabular}

6: Learned parameters of each network. Ours and Moco are counted from checkpoints; the others are derived from stated hyperparameters or official code, since no paper states its count.

