### 4.4 Per-Signal Surprise Ablation

We disentangle the three surprise signals on the real VLM using cached Qwen-3.5 scores and 10 seeds on BIOSSES and STS-B ( 4). Removing the Elo-gap term hurts most on both datasets, indicating that the human-derived ranking state-- initialized by Round-0 warm start--is the most useful signal. The VLM-confidence term is domain-dependent: it helps on STS-B, where the VLM pre-order is strong, but hurts on BIOSSES, where dropping it improves both \(\tau\) and inferred accuracy. The fixed composite is therefore a robust default rather than a tuned optimum; learned or agreement-dependent weights are a natural extension.

### 4.5 Controlled Simulation: Diagnostics and Ablations

To obtain multi-seed uncertainty estimates and ground-truth inferred-edge accuracy, we complement the fixed-VLM benchmarks with a controlled simulation in which the VLM annotator is replaced by a synthetic pointwise scorer whose agreement \(\alpha\) is tuned by noise \(\sigma_v\). We use _n_=200, the default budget, and report 10-seed means with 95% bootstrap CIs ( 5); absolute \(\tau\) values are not comparable to the VLM benchmarks.

\begin{tabular}{ccc}
Configuration & BIOSSES (\(\tau_\mathrm{VLM}\)=71.3) & STS-B (\(\tau_\mathrm{VLM}\)=77.9) \\
Full (0.4,0.3,0.3) & 80.0 \[79.4, 80.6\] & 76.0 \[75.6, 76.4\] \\
-VLM & **82.1** \[81.3, 82.8\] & 75.5 \[74.9, 76.1\] \\
-Elo & 76.8 \[76.2, 77.5\] & 71.5 \[71.2, 71.9\] \\
-Ent & 79.9 \[79.2, 80.5\] & **76.2** \[75.8, 76.6\] \\
VLM only & 76.8 \[76.2, 77.5\] & 71.5 \[71.2, 71.9\] \\
Elo only & **82.1** \[81.3, 82.8\] & 75.5 \[74.9, 76.1\] \\
Ent only & 76.2 \[75.8, 76.6\] & 70.0 \[69.5, 70.5\] \\
\end{tabular}

\begin{tabular}{ccccccc}
\(\sigma_v\) & \(\alpha\) & \(\tau\times\)100 (95% CI) & Inferred & Inf. acc & Fallback & \\
20 & 0.87 & 72.1 \[70.9, 73.2\] & 47% & 74.0% & 0% & \\
30 & 0.84 & 67.8 \[66.6, 69.1\] & 47% & 74.7% & 0% & \\
40 & 0.80 & 62.7 \[61.5, 63.9\] & 47% & 78.5% & 0% & \\
55 & 0.75 & 57.2 \[55.1, 59.5\] & 38% & 79.1% & 20% & \\
75 & 0.70 & 54.2 \[51.5, 56.8\] & 24% & 78.8% & 50% & \\
100 & 0.67 & 51.6 \[49.0, 53.8\] & 14% & 80.2% & 70% & \\
\end{tabular}

** 4.** Per-signal surprise ablation on the _real_ VLM (Qwen-3.5; 10 seeds, 95% bootstrap CIs). \(\tau\times\)100; best per column **bold**. Removing the Elo-gap term hurts most on both datasets; the VLM-confidence term helps on STS-B (strong VLM pre-order) but is harmful on BIOSSES, where Elo alone already captures the structure.

** 5.** Controlled simulation (synthetic annotator, _n_=200, 10 seeds). As calibration agreement \(\alpha\) decreases (via annotator noise \(\sigma_v\)), SGS degrades in a controlled way: the \(\alpha\)-gate fires more often and the automatic-resolution edge multiplier shrinks, while inferred edges stay well above chance. Brackets are 95% bootstrap CIs.

