<tbc>encoding. Raw coordinates leave a gap \(5.6\times\) that of sinusoidal features at the scale of nearest- neighbor distances. However, a _k_-nearest-neighbor (kNN) edge bias, as on MIS, adds nothing, and a finer sinusoidal embedding hurts. Second, decoding composes with the recursion. On MIS, sequential peeling cuts the gap of the same checkpoint by two thirds, and more width and depth halve what remains. On TSP, the greedy walk strands nodes and recovers only half of the loss even with multi-start, whereas edge insertion cannot strand nodes, so its raw tours have half the gap of the multi-start walk, and one 2-opt pass brings them within 1% of optimal. Third, the prefix tokens provide global memory. Removing them raises the one-shot MIS gap by half at the same schedule, so a few registers that every node can attend to give the recursion a scratchpad that node tokens alone do not.

## 3.6 SELF-RELABELING AS SELF-SUPERVISION

We can generate and improve the labels throughout training by keeping the best solution (Section 2.3).  3 compares this with supervised training on ER-\[700-800\] and TSP-500, under the same decoding settings as s 1 and 2.

\begin{tabular}{ccccccccccc}
Dataset & & \multicolumn{3}{c}{TSP-500} & \multicolumn{3}{c}{TSP-1000} & \multicolumn{3}{c}{TSP-10000} \\
Method & Search & \multicolumn{3}{c}{Len. Gap % s/inst} & \multicolumn{3}{c}{Len. Gap % s/inst} & \multicolumn{3}{c}{Len. Gap % s/inst} \\
Concorde / LKH-3 (reference) & - & 16.55 & 0.00 & 18 & 23.12 & 0.00 & 187 & 71.77 & 0.00 & 1980 \\
\multicolumn{11}{c}{_General-purpose neural solvers (MIS and TSP)_} \\
DIMES (Qiu et al., 2022) & MCTS & 16.84 & 1.76 & 67 & 23.69 & 2.46 & 136 & 74.06 & 3.19 & 1219 \\
DIFUSCO (Sun \& Yang, 2023) & 2-opt & 16.65 & 0.57 & 2.9 & 23.45 & 1.43 & 12.4 & 73.89 & 2.95 & 266 \\
DIFUSCO & MCTS & 16.63 & 0.46 & 51 & 23.39 & 1.17 & 104 & 73.62 & 2.58 & 1076 \\
T2T (Li et al., 2023) & 2-opt & 16.61 & 0.37 & 4.4 & 23.30 & 0.78 & 11.0 & 73.81 & 2.84 & - \\
UDC (Zheng et al., 2024) & conquer & 16.82 & 1.66 & 1.8 & 23.53 & 1.78 & 2.7 & 74.71 & 4.09 & 1.9 \\
Fast T2T (Li et al., 2024) & 2-opt & 16.58 & 0.21 & 2.5 & 23.22 & 0.42 & 5.9 & 72.90 & 1.57 & - \\
Moco (Dernedde et al., 2025) & 2-opt & 16.62 & 0.40 & 98 & - & - & - & - & - & - \\
DISCO (Zhao et al., 2025) & 2-opt & - & - & - & - & - & - & 73.81 & 2.84 & - \\
COExpander (Ma et al., 2025) & 2-opt & 16.59 & 0.25 & 1.0 & 23.27 & 0.64 & 2.2 & 72.80 & 1.45 & 25 \\
CADO (Song et al., 2026) & 2-opt & 16.65 & 0.61 & - & 23.32 & 0.88 & - & 73.69 & 2.68 & - \\
CAM (Feng et al., 2026b) & 2-opt & 16.91 & 2.18 & 3.2 & 23.70 & 2.51 & 12.6 & - & - & - \\
HyCO (Li et al., 2026) & 2-opt & 16.74 & 1.17 & - & 23.64 & 2.26 & - & - & - & - \\
\multicolumn{11}{c}{_Learning-free methods_} \\
iSCO (Sun et al., 2023) & sampler & 16.64 & 0.54 & - & 23.33 & 0.91 & - & 74.02 & 3.14 & - \\
SoftDist (Xia et al., 2024) & MCTS & 16.78 & 1.44 & 50 & 23.63 & 2.20 & 101 & 74.03 & 3.13 & 1012 \\
Zero heatmap (Pan et al., 2026) & MCTS & 16.66 & 0.66 & 50 & 23.39 & 1.16 & 100 & 74.50 & 3.79 & 102 \\
GT-Prior (Pan et al., 2026) & MCTS & 16.63 & 0.50 & 50 & 23.31 & 0.85 & 100 & 73.31 & 2.13 & 101 \\
\multicolumn{11}{c}{_TSP-specific neural solvers (no MIS results)_} \\
Att-GCN (Fu et al., 2021) & MCTS & 16.97 & 2.54 & 20 & 23.86 & 3.22 & 40 & 74.93 & 4.39 & 401 \\
BQ-NCO (Drakulić et al., 2023) & beam search & 16.64 & 0.55 & 3.5 & 23.44 & 1.38 & 8.6 & - & - & - \\
UTSP (Min et al., 2023) & local search & 16.68 & 0.84 & 20 & 23.39 & 1.18 & 41 & - & - & - \\
LEHD (Luo et al., 2023) & RRC & 16.57 & 0.16 & 53.5 & 23.29 & 0.75 & 256 & - & - & - \\
GLOP (Ye et al., 2024) & revisers & 16.91 & 1.99 & 0.8 & 23.84 & 3.11 & 1.6 & 75.29 & 4.90 & 4.7 \\
SIL (Luo et al., 2024) & PRC & - & - & - & 23.31 & 0.81 & 349 & 73.32 & 2.00 & 1011 \\
DualOpt (Zhou et al., 2025) & LKH-3 + NN & - & - & - & 23.31 & 0.83 & 2.0 & 72.62 & 1.18 & 13.9 \\
DRHG (Li et al., 2025) & LNS & 16.58 & 0.23 & 25.8 & 23.19 & 0.29 & 52 & 72.85 & 1.33 & 106 \\
HyperNS (Lu et al., 2026) & LK search & - & - & - & 23.20 & 0.35 & - & **72.44** & **0.93** & - \\
PCI (Basson \& Preux, 2026) & 2-opt & 16.57<sup>†</sup> & 0.17<sup>†</sup> & - & 23.19<sup>†</sup> & 0.31<sup>†</sup> & - & - & - & - \\
\multicolumn{11}{c}{_TRM4CO (general-purpose; noise_ \(\sigma\)=0.2)} \\
TRM4CO (_K_=40, _D_=32) & 2-opt & **16.56** & **0.11** & 2.1 & **23.18** & **0.27** & 4.4 & 72.81 & 1.45 & 364 \\
\end{tabular}

2: TSP results on uniform instances. We report mean tour length, gap in % against Concorde (_n_=500,1000) and LKH-3 (_n_=10000), and seconds per instance on one RTX 4090. The Search column indicates the search procedure that produces each result, either post-processing after the network or a custom refinement loop (details in Appendix E). The meanings of "-", "<sup>†</sup>", and the reference solver time follow those of  1. Bold marks the lowest gap at each problem size.

