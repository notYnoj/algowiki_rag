<tbc>restricted to the _m_ longest edges of the tour. The main-table numbers use a full scan. During self-relabeling, the TSP tours of a relabel pass are repaired with 2-opt and canonicalized before the comparison with the stored label.

**Augmentations.** Two augmentations run on the fly. For MIS, peel augmentation removes a random number of label nodes one at a time, each with its closed neighborhood, so that training also sees the residual graphs that sequential peeling visits. For TSP, one of the eight symmetries of the square is applied with the tour orientation kept canonical (counterclockwise).

## C DATASETS AND REFERENCES

**MIS.** The ER-\[700-800\] and SATLIB graphs are those distributed with DIMES (Qiu et al., 2022). We label the ER training graphs with KaMIS (Lamm et al., 2017) at a 10-second budget per graph, which gives a mean set size of 44.52 on the training graphs and 44.63 on the test graphs. DIFUSCO and the papers that follow it compare against a longer KaMIS run on the test graphs with a mean size of 44.87 (24 seconds per graph), which  1 and Figures 2 and 3 use as the reference. The ablation table ( 7) reports gaps against our own test labels, 44.63, so its gaps are about half a point lower for the same set size. SATLIB labels are exact, computed with Gurobi (Gurobi Optimization, LLC, 2026). Their mean of 425.96 on the test graphs coincides with the KaMIS reference of those papers.

**TSP.** Training instances are drawn uniformly from the unit square and labeled with LKH-3 (Helsgaun, 2017) using 1000 trials and the best of 10 runs per instance. The test sets are the 128, 128, and 16 instances of Fu et al. (2021). The reference tours that ship with their public copies are not optimal. The tours attributed to Concorde (Applegate et al., 2006) are 0.23% and 0.47% above the optimum at _n_=500 and 1000, and the _n_=10000 file carries placeholder tours. We therefore recompute the references, with Concorde at _n_=500 and 1000 (certified optimal, mean lengths 16.5458 and 23.1181) and with LKH-3 at _n_=10000 (10,000 trials, best of 10 runs, mean length 71.7708, the LKH-3 value quoted in the literature). All gaps in  2 are against these references, and published lengths are re-expressed accordingly (Appendix E).

## D RUNTIME PROOL

All runtimes in s 1 and 2 are our own measurements on one RTX 4090 with the released code and checkpoints of each method, in the inference setting whose quality number the table quotes. For each compared method, we time the complete pipeline from the instance to the final solution, including heatmap generation, decoding, and any post-processing such as 2-opt, rewriting, or search,<tbc>

\begin{tabular}{cc}
Parameter & Value \\
Hidden size, heads, blocks & 512, 8, 2 \\
MLP expansion & 4 \\
Recursion _H_, _L_ & 3, 6 \\
Prefix tokens _P_ & 16 \\
Structure, MIS & Edge-biased attention, 12-step random-walk positional encoding \\
Structure, TSP & Self-attention, _L_<sub>pe</sub>=6 coordinate encoding \\
Successor head dimension _d<sub>s</sub>_ & 128 (TSP) \\
Training depth _D_ & 32 (MIS; 64 in the first ER stage), 16 (TSP) \\
Global batch size & 768 (ER, TSP-500), 384 (SATLIB), 512 (TSP-1000), 48 (TSP-10000) \\
Epochs, MIS & 10,000 (ER), 2000 (SATLIB) \\
Epochs, TSP & 500 (TSP-500), 1000 (TSP-1000), 2000 (TSP-10000) \\
Learning rate & AdamW 10<sup>-4</sup>, Muon \(2\cdot 10^{-3}\), 5000 warm-up steps, cosine to 1% \\
Weight decay, EMA rate & 0.1, 0.999 \\
Augmentation & Peel, prob. 0.9, depth \(\le 9\) (ER), \(\le 32\) (SATLIB); dihedral-8 (TSP) \\
Self-relabel pass, ER continuation & Every 200 epochs, _K_=4, _D_=16, _k_<sub>p</sub>=2 \\
\end{tabular}

5: Hyperparameters of the reported models. Epochs are passes over the training set, summed over all stages of a continued run. The self-relabeling continuation of  3 adds 3000 epochs with a 2000-step warm-up. Test-time _K_, _D_, \(\sigma\), \(\tau\), _k_<sub>p</sub>, and _m_ are given with each table.

