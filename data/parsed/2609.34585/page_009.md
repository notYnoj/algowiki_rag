## 4 RELATED WORK

**Constructive policies.** Autoregressive policies build a solution one decision at a time (Vinyals et al., 2015; Kool et al., 2019; Kwon et al., 2020). LEHD (Luo et al., 2023) and BQ-NCO (Drakuli ́c et al., 2023) train on small instances and then generalize. GLOP (Ye et al., 2024), UDC (Zheng et al., 2024), DualOpt (Zhou et al., 2025), and H-TSP (Pan et al., 2023) reach larger instances by decomposition. HyperNS (Lu et al., 2026) instead guides a Lin–Kernighan search with a heatmap, and GOAL (Drakuli ́c et al., 2025) injects edges into attention as we do.

**Heatmap solvers and search.** Heatmap solvers score all variables in one pass and leave construction to a search. Att-GCN (Fu et al., 2021) pairs a learned heatmap with MCTS for large TSP instances, and DIMES (Qiu et al., 2022) makes the heatmap a differentiable policy. DIFUSCO (Sun & Yang, 2023) models the heatmap with a diffusion model, and T2T (Li et al., 2023), Fast T2T (Li et al., 2024), DISCO (Zhao et al., 2025), CADO (Song et al., 2026), DDEA (Salvà Soler & Raidl, 2026), and PCI (Basson & Preux, 2026) refine its training, sampling, or search. TRM4CO instead refines its prediction by recursion inside the network. Xia et al. (2024) and Pan et al. (2026) show that the search dominates the heatmap in these pipelines, and Böther et al. (2022) and Angelini & Ricci-Tersenghi (2023) reach a similar verdict for MIS. FrontierCO (Feng et al., 2026a) and the survey of Ba et al. (2026) find neural solvers behind tuned heuristics at scale.

**Unsupervised and self-improving solvers.** UTSP (Min et al., 2023), DiffUCO (Sanokowski et al., 2024), SDDS (Sanokowski et al., 2025), and CAM (Feng et al., 2026b) train without solver labels by optimizing relaxed objectives. Moco (Dernedde et al., 2025) learns a heatmap optimizer that spends its compute at test time. SIL (Luo et al., 2024) improves a constructive policy on its own solutions after local search. Samplers such as iSCO (Sun et al., 2023) and ReSCO (Li & Zhang, 2025) need no learning at all. Our self-relabeling is closest to SIL, with the recursive model’s own decoded solutions as labels and no relaxed objective.

**Recursive reasoning.** HRM (Wang et al., 2025) and TRM (Jolicoeur-Martineau, 2025; Sghaier et al., 2026) solve puzzles by latent recursion with adaptive halting. Looped Transformers reuse one block of layers to gain depth (Wang et al., 2026; Suleymanzade et al., 2026). To the best of our knowledge, we are the first to apply latent recursion to combinatorial optimization at this scale.

## 5 CONCLUSION

We have presented TRM4CO, a small recursive network with problem-specific encoding and decoding that is competitive with or better than search-heavy pipelines on MIS and TSP. Its key ingredient is test-time scaling in depth and in width on the same weights, which efficiently turns compute into solution quality. Self-relabeling improves the model further, on top of solver labels or without any. TRM4CO attacks the remaining gap between neural solvers and learning-free search from the perspective of recursive reasoning. Our backbone is general, but the encoder and decoder remain problem-specific, and reducing that dependence is the natural next step.

\begin{tabular}{ccc}
Run & Labels & Gap % \\
\multicolumn{3}{c}{_MIS ER-\[700-800\]_} \\
Supervised & KaMIS & 2.53 \\
Self-relabel continuation & KaMIS, then own & **1.11** \\
Self-relabel from scratch & Own only & 1.43 \\
\multicolumn{3}{c}{_TSP-500_} \\
Supervised & LKH-3 & **0.11** \\
Self-relabel from scratch & Own only & 2.26 \\
\end{tabular}

3: Self-relabeling. Test gap in % for MIS on ER-\[700-800\] against KaMIS, decoded with sequential peeling at the setting of  1 (_k_<sub>p</sub>=2, \(\tau=0.5\), _K_=10, _D_=32), and for TSP-500 against Concorde at the setting of  2 (_K_=40, _D_=32, 2-opt). The supervised rows train on solver labels, the continuation row trains on top of the supervised checkpoint, and the from-scratch rows start from random initialization without any solver labels.

