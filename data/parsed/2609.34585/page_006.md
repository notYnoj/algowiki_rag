## 3.4 SCALING TEST-TIME COMPUTE

Figure 2 shows the contribution of the two scaling axes. On ER-\[700-800\], width matters more than depth. At _k_<sub>p</sub>=8 the gap falls steadily with _K_, while the curves for \(D\in\{16,32\}\) lie on top of each other. Finer peeling helps most. With _k_<sub>p</sub>=2 the gap is lower at every _K_ and crosses the KaMIS reference at both depths, since every peel round takes the best of _K_ fresh rollouts on the residual graph. Depth adds a small but consistent gain at _k_<sub>p</sub>=2. On TSP the gap after 2-opt falls with _K_ at both depths, and on TSP-1000 it is still falling at the largest width we ran. Overall cost is linear in \(K\times D\) because the rollouts run as one batched forward. Figure 3 places these points among the baselines. On TSP-500 the TRM4CO curve lies below every learned solver. On ER-\[700-800\] it reaches the lowest gap of the learned solvers without a sampler, but RLSA and COExpander with RLSA reach the same or lower gaps at a small fraction of the cost, so there the samplers dominate.

## 3.5 ABLATIONS

7 in Appendix F varies one factor at a time. First, the structure of a combinatorial optimization problem has to enter the network in an appropriate way. For MIS, that is the self-attention. A message-passing GNN encoder in front of the recursion leaves a one-shot gap up to twice that of the edge-biased attention from Eq. (2), which needs no encoder at all. For TSP, it is the input<tbc>

\begin{tabular}{cccccccc}
Dataset & & \multicolumn{3}{c}{ER-\[700-800\]} & \multicolumn{3}{c}{SATLIB} \\
Method & Type & Size & Gap % & s/inst & Size & Gap % & s/inst \\
KaMIS (reference) & heuristic & 44.87 & 0.00 & 24 & 425.96 & 0.00 & 4.5 \\
\multicolumn{8}{c}{_General-purpose neural solvers (MIS and TSP)_} \\
DIMES (Qiu et al., 2022) & RL & 42.06 & 6.26 & - & 423.28 & 0.63 & - \\
DIFUSCO (Sun \& Yang, 2023) & S & 41.12 & 8.36 & 7.4 & 425.13 & 0.19 & 1.6 \\
T2T (Li et al., 2023) & S + search & 41.37 & 7.80 & 9.0 & 425.22 & 0.17 & 1.5 \\
UDC (Zheng et al., 2024) & RL & 42.88 & 4.44 & 6.9 & - & - & - \\
Fast T2T (Li et al., 2024) & S + search & 41.73 & 7.00 & 0.92 & 425.23 & 0.17 & 1.4 \\
Moco (Dernedde et al., 2025) & U + search & 44.87 & 0.00 & 22.8 & 425.02 & 0.22 & 109 \\
DISCO (Zhao et al., 2025) & S & 42.21 & 5.93 & - & 425.06 & 0.21 & - \\
COExpander (Ma et al., 2025) & S & 42.56 & 5.15 & 1.2 & 425.28 & 0.16 & 1.3 \\
COExpander + RLSA & S + sampler & **45.27** & **-0.89** & 4.5 & 425.45 & 0.12 & 8.6 \\
CADO (Song et al., 2026) & S + RL & 43.62 & 2.79 & - & 425.43 & 0.12 & - \\
CAM (Feng et al., 2026b) & U & 44.16 & 1.58 & 0.2 & - & - & - \\
HyCO (Li et al., 2026) & S + RL & 42.38<sup>†</sup> & 5.55<sup>†</sup> & - & 425.40<sup>†</sup> & 0.13<sup>†</sup> & - \\
\multicolumn{8}{c}{_Learning-free methods_} \\
iSCO (Sun et al., 2023) & sampler & 45.15 & -0.62 & 55 & 424.16 & 0.42 & 87 \\
ReSCO (Li \& Zhang, 2025) & sampler & 45.24 & -0.82 & 73 & 424.21 & 0.41 & 258 \\
RLSA (Feng \& Yang, 2025) & sampler & 45.05 & -0.40 & 0.65 & - & - & - \\
\multicolumn{8}{c}{_MIS-specific neural solvers (no TSP results)_} \\
LwD (Ahn et al., 2020) & RL & 41.17 & 8.25 & - & 424.80<sup>†</sup> & 0.27<sup>†</sup> & - \\
GFFlowNets (Zhang et al., 2023) & U & 41.14<sup>†</sup> & 8.31<sup>†</sup> & - & 423.54<sup>†</sup> & 0.57<sup>†</sup> & - \\
DiffUCO (Sanokowski et al., 2024) & U & 43.98 & 1.98 & - & - & - & - \\
SDDS (Sanokowski et al., 2025) & U & 43.31 & 3.48 & - & - & - & - \\
RLNN (Feng \& Yang, 2025) & U & 43.34 & 3.41 & 0.26 & - & - & - \\
DDEA (Salvà Soler \& Raidl, 2026) & S + evolution & 44.13 & 1.65 & 396 & - & - & - \\
\multicolumn{8}{c}{_TRM4CO (general-purpose; noise_ \(\sigma=0.2\)_; peel k_<sub>p</sub>=2, _Gumbel noise_ \(\tau=0.5\) _on ER; one-shot on SATLIB)_} \\
TRM4CO (_K_=10, _D_=32) & S + self & 44.37 & 1.11 & 18.7 & **425.96** & **0.00** & 2.2 \\
TRM4CO (_K_=100, _D_=64) & S + self & 44.93 & -0.13 & 368 & - & - & - \\
TRM4CO (_K_=200, _D_=32) & S + self & 45.04 & -0.38 & 373 & - & - & - \\
\end{tabular}

1: MIS results. We list mean independent set size on ER-\[700-800\] and SATLIB, gap in % with respect to the KaMIS reference, and seconds per instance on one RTX 4090. Type: S = supervised, U = unsupervised, RL = reinforcement learning (details in Appendix E). "-" means that the number is not available, and "<sup>†</sup>" marks evaluation on the method’s own instances from the same distribution. The KaMIS time is measured on CPU. Bold marks the lowest gap on each benchmark.

