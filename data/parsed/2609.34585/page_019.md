\begin{tabular}{ccc}
Factor & Variant & Gap % \\
\multicolumn{3}{c}{_MIS structure injection (one-shot, K_=1)} \\
 & 3-layer GNN encoder + self-attention & 20.2 \\
 & 6-layer GNN encoder + self-attention & 13.5 \\
 & No encoder + edge-biased attention (default) & 10.0 \\
\multicolumn{3}{c}{_MIS prefix tokens (same schedule, best checkpoint of the last training window)_} \\
 & _P_=0 & 15.0 \\
 & _P_=16 (default) & 10.0 \\
\multicolumn{3}{c}{_MIS decoding (same checkpoint, K_=10_, D_=32)} \\
 & One-shot greedy & 9.06 \\
 & Sequential peel, _k_<sub>p</sub>=2 & 2.67 \\
 & Sequential peel, _k_<sub>p</sub>=2, _K_=40, _D_=64 & 1.14 \\
\multicolumn{3}{c}{_MIS Gumbel noise on peeling (k_<sub>p</sub>=2, \(\sigma\)=0.7_, K_=4)} \\
 & Sequential peel, \(\tau\)=0 & 6.61 \\
 & Sequential peel, \(\tau\)=0.1 & 6.42 \\
 & Sequential peel, \(\tau\)=0.3 & 5.86 \\
 & Sequential peel, \(\tau\)=1.0 & 6.96 \\
\multicolumn{3}{c}{_MIS rollouts (k_<sub>p</sub>=2, \(\sigma\)=0.7)} \\
 & _K_=4 & 7.0 \\
 & _K_=100 & 1.97 \\
\multicolumn{3}{c}{_TSP-500 input encoding (same schedule, best in-run checkpoint)_} \\
 & Raw coordinates, self-attention & 15.89 \\
 & Raw coordinates, kNN edge-biased attention & 17.27 \\
 & _L_<sub>pe</sub>=6, self-attention (default) & 2.84 \\
 & _L_<sub>pe</sub>=6, kNN edge-biased attention & 3.20 \\
 & _L_<sub>pe</sub>=12, self-attention & 6.72 \\
\multicolumn{3}{c}{_TSP-500 decoding (same checkpoint, K_=10_, D_=16)} \\
 & Walk, one-shot (_K_=1, last step) & 8.44 \\
 & Walk, argmax & 2.76 \\
 & Walk, multi-start & 1.36 \\
 & Walk, multi-start + 2-opt (_m_=16) & 0.247 \\
 & Walk, multi-start + \(\tau\)=0.3 + full 2-opt & 0.169 \\
 & Insertion, raw & 0.611 \\
 & Insertion + full 2-opt (default) & 0.151 \\
\multicolumn{3}{c}{_TSP-10000 2-opt budget m (insertion, K_=4_, D_=16)} \\
 & _m_=16 & 2.73 \\
 & _m_=64 & 2.19 \\
 & _m_=256 & 1.91 \\
 & _m_=1024 & 1.77 \\
 & Full scan & 1.69 \\
\end{tabular}

7: Ablations, one factor at a time. MIS on ER-\[700-800\] (gap in % against our KaMIS labels, 44.63), TSP-500 (gap in % against Concorde), and TSP-10000 (gap in % against LKH-3). Each block varies one factor of the default configuration, with _K_, _D_, and \(\sigma\) as noted. The MIS decoding block uses the supervised checkpoint of  3 with \(\sigma=0.5\) and \(\tau=0\), and the rollout and Gumbel rows an earlier checkpoint with \(\sigma=0.7\), so their gaps are not directly comparable with  1.

