<tbc>clipped to valid ranges. Every cell (_m,i_) or (_m,j_) that improves is overwritten with the new exact value and stores its improving partner as a _hint_. Because a non-anchor length carries no index neighbor of its own, a cell draws the neighbor _j_ it re-cuts from the hash index when its length is anchored and from this stored hint otherwise, the "index or hint" of the emit refinement loop. The seeds are re-selected after every round, so a discovery spreads one radius at a time. No round rescans the series or any length row. A seed costs at most \((2\Delta_m+1)(2\Delta_p+1)^2\) exact distance computations per round. At most _P_<sub>max</sub> rounds run, stopping earlier once no cell improves. Refinement therefore performs a fixed constant of work per seed, independent of both _n_ and _L_ (Figure 2C). Distances below \(\varepsilon_0\) are reported as exactly zero. Otherwise, values identical up to rounding noise would order arbitrarily in the final top-_k_ sort. No distance is interpolated. Every written cell comes from the raw windows at its own length, so Proposition 1 applies to the final output.

This completes the algorithm. The evaluated set \(\mathcal{S}=\mathcal{S}_\mathrm{stream}\cup\mathcal{S}_\mathrm{hot}\cup\mathcal{S}_\mathrm{local}\) is now assembled, and Panache reports the top-_k_ cells of the induced profile (_P_<sup>S</sup>_,I_<sup>S</sup>) under the _m/_2 overlap rule of §2 as the discovered motifs.

## 3.7 Complexity and Memory

Per sample, each anchor spends _O(K_) on the sliding state, _O(BK_) on the signature, and at most _R_ candidate inspections. If a fraction \(\varphi\) of inspected candidates reaches exact evaluation, the online work is \(O\big(n|A|\big(BK+R(K+\varphi m)\big)\big)\) for \(|A|=\lceil L/s\rceil\). The emit stage adds

\(\sum_{C\in\mathcal{H}}O(|C|\mathrm{log}|C|+|C|wm)+O\big(P_\mathrm{max}M(2\Delta_m+1)(2\Delta_p+1)^2m\big)\)

over the hot classes H and the _M_ seeds refined per round. For a fixed length interval and configuration, the online work is linear in _n_ and the emit stage is bounded by _O(n_(log_n+wm_)), so the total runtime is near-linear in the series length. Memory is _O(n|A_|(_K+B_)+_nL+n_), covering the cached features, signatures and hash metadata, profile rows, and retained raw samples. A materialized pan-profile has \(\Theta(nL)\) cells, so space linear in _n_ applies to any method that produces this object; the feature cache dominates the constants. At the largest reported run (\(n=5\times 10^6\), _L_=51, |_A_|=26, _K_=16), the feature cache is approximately 15.6 GB and peak memory is 23.3 GB in the streaming pass and 35.5 GB at full materialization ( 1, §6).

\begin{tabular}{ccccccccccccc}
 & & \multicolumn{5}{c}{**Panache**} & \multicolumn{5}{c}{baselines: wall time (s); (recovered/20) where scored} \\
Dataset & _n_ & time (s) & top-20 (pos+val) & memory & t. mat. & mem. mat. & Scamp & Scamp-GPU & Stumpy & SCRUMP & STIMP & L-Stumpi & Attimo \\
\multicolumn{13}{c}{_Recovery suites - UCR (per-dataset length ranges)_} \\
ECG200 & 8k & 0.06 & 20/20 (16+4) & 37 MB & 0.14 & 32 MB & 0.17 & 0.85 & 4.80 (20) & 8.32 (20) & 8.29 & 50.1 & 20.8 (18) \\
ItalyPowerDemand & 1,600 & 0.01 & 20/20 (20+0) & 37 MB & 0.02 & 37 MB & 0.04 & 0.21 & 0.52 (20) & 0.91 (20) & 0.90 & 4.83 & 8.48 (20) \\
Wafer & 8k & 0.08 & 20/20 (19+1) & 37 MB & 0.25 & 51 MB & 0.29 & 1.20 & 7.45 (20) & 12.8 (20) & 13.0 & 81.6 & 117 (20) \\
Earthquakes & 8k & 0.07 & 20/20 (20+0) & 37 MB & 0.25 & 64 MB & 0.30 & 1.16 & 7.13 (20) & 12.8 (20) & 13.0 & 81.9 & 1,052 (20) \\
StarLightCurves & 8k & 0.08 & 20/20 (20+0) & 100 MB & 0.23 & 133 MB & 0.29 & 1.22 & 7.76 (20) & 12.7 (20) & 12.9 & 83.6 & 20.5 (20) \\
ChlorineConcentration & 8k & 0.08 & 20/20 (20+0) & 37 MB & 0.22 & 65 MB & 0.25 & 1.18 & 7.18 (20) & 12.8 (20) & 13.0 & 84.8 & 10.4 (20) \\
TwoLeadECG & 8k & 0.07 & 20/20 (20+0) & 37 MB & **0.15** & 42 MB & 0.14 & 0.64 & 4.62 (20) & 7.73 (20) & 7.87 & 49.8 & 7.38 (20) \\
ECG5000 & 8k & 0.06 & 20/20 (20+0) & 37 MB & 0.14 & 38 MB & 0.15 & 0.62 & 4.61 (20) & 7.93 (20) & 8.02 & 49.1 & 9.29 (20) \\
FordA & 8k & 0.06 & 20/20 (20+0) & 37 MB & 0.20 & 55 MB & 0.25 & 1.16 & 7.54 (20) & 13.2 (20) & 13.4 & 81.6 & 166 (20) \\
Mallat & 8k & 0.07 & 20/20 (15+5) & 44 MB & 0.21 & 70 MB & 0.26 & 1.29 & 7.79 (20) & 13.0 (20) & 13.0 & 85.3 & 295 (20) \\
\multicolumn{13}{c}{_Recovery suite - 64k, lengths 30-80_} \\
ChlorineConcentration & 64k & 1.05 & 20/20 (20+0) & 305 MB & 2.27 & 451 MB & 6.04 & 6.04 & - & - & - & - & - \\
Earthquakes & 64k & 1.01 & 20/20 (20+0) & 305 MB & 2.68 & 458 MB & 6.07 & 5.29 & - & - & - & - & - \\
ECG5000 & 64k & 0.80 & 20/20 (12+8) & 202 MB & 2.08 & 364 MB & 6.19 & 5.93 & - & - & - & - & - \\
FordA & 64k & 0.70 & 20/20 (15+5) & 203 MB & 1.97 & 363 MB & 6.13 & 5.74 & - & - & - & - & - \\
Mallat & 64k & 0.96 & 20/20 (17+3) & 317 MB & 4.03 & 490 MB & 6.29 & 6.18 & - & - & - & - & - \\
StarLightCurves & 64k & 0.92 & 20/20 (20+0) & 365 MB & 2.20 & 530 MB & 6.30 & 5.99 & - & - & - & - & - \\
Wafer & 64k & 0.78 & 20/20 (16+4) & 198 MB & 1.99 & 359 MB & 6.34 & 5.36 & - & - & - & - & - \\
\multicolumn{13}{c}{_Full natural lengths (capped at 1M)_} \\
ItalyPowerDemand & 1,608 & 0.01 & 20/20<sup>†</sup> (20+0) & 37 MB & 0.02 & 37 MB & 0.04 & 0.15 & - & - & - & - & - \\
ECG200 & 9,600 & 0.07 & 20/20<sup>†</sup> (16+4) & 37 MB & 0.17 & 38 MB & 0.25 & 0.81 & - & - & - & - & - \\
TwoLeadECG & 93,398 & 1.20 & 20/20<sup>†</sup> (12+8) & 273 MB & 2.38 & 407 MB & 7.34 & 4.55 & - & - & - & - & - \\
Wafer & 152k & 2.88 & 20/20<sup>†</sup> (0+20) & 634 MB & 5.98 & 1.0 GB & 31.7 & 11.7 & - & - & - & - & - \\
Earthquakes & 164,864 & 3.65 & 20/20<sup>†</sup> (19+1) & 793 MB & 7.06 & 1.2 GB & 35.0 & 11.4 & - & - & - & - & - \\
ECG5000 & 630k & 10.7 & 20/20<sup>†</sup> (8+12) & 1.8 GB & 19.6 & 2.8 GB & 299 & 39.5 & - & - & - & - & - \\
ChlorineConcentration & 637,440 & 17.0 & 20/20<sup>†</sup> (3+17) & 2.7 GB & 31.8 & 4.2 GB & 473 & 67.5 & - & - & - & - & - \\
FordA & 660k & 18.1 & 20/20<sup>†</sup> (13+7) & 3.1 GB & 33.6 & 4.7 GB & 501 & 79.2 & - & - & - & - & - \\
StarLightCurves & 1M & 20.7 & 20/20<sup>†</sup> (1+19) & 4.6 GB & 53.1 & 7.2 GB & 1,213 & 144 & - & - & - & - & - \\
Mallat & 1M & 23.7 & 20/20<sup>†</sup> (0+20) & 4.6 GB & 35.9 & 7.1 GB & 1,213 & 143 & - & - & - & - & - \\
\multicolumn{13}{c}{_Length scaling - Wafer (tiled beyond 152k), lengths 30-80_} \\
Wafer & 8k & 0.07 & 20/20<sup>†</sup> (17+3) & 65 MB & 0.24 & 94 MB & 0.31 & 1.11 & - & - & - & - & - \\
Wafer & 16k & 0.14 & 20/20<sup>†</sup> (17+3) & 91 MB & 0.41 & 139 MB & 0.73 & 1.97 & 16.3 & 27.1 & 27.9 & 167 & 30.9 \\
Wafer & 32k & 0.32 & 20/20<sup>†</sup> (19+1) & 140 MB & 0.89 & 227 MB & 2.04 & 3.23 & 34.0 & 57.5 & 60.5 & 335 & 106 \\
Wafer & 64k & 0.82 & 20/20<sup>†</sup> (10+10) & 240 MB & 2.03 & 400 MB & 6.44 & 5.77 & 75.3 & 122 & 134 & 667 & 186 \\
Wafer & 128k & 2.17 & 20/20<sup>†</sup> (0+20) & 567 MB & 4.75 & 889 MB & 22.3 & 10.2 & - & - & - & - & - \\
Wafer & 256k & 5.80 & 20/20<sup>†</sup> (0+20) & 1.2 GB & 15.0 & 1.8 GB & 83.9 & 24.1 & - & - & - & - & - \\
Wafer & 512k & 13.4 & 20/20<sup>†</sup> (0+20) & 2.4 GB & 30.4 & 3.6 GB & 316 & 59.7 & - & - & - & - & - \\
Wafer & 1M & 28.5 & 20/20<sup>†</sup> (0+20) & 4.6 GB & 62.7 & 7.1 GB & 1,204 & 148 & - & - & - & - & - \\
Wafer & 2M & 62.2 & 20/20<sup>†</sup> (0+20) & 9.3 GB & 133 & 14.1 GB & 4,744 & 451 & - & - & - & - & - \\
Wafer & 5M & 172 & 20/20<sup>†</sup> (0+20) & 23.3 GB & 363 & 35.5 GB & 28,638 & 2,299 & - & - & - & - & - \\
\end{tabular}

** 1: Complete benchmark table. Panache columns: time (s) and memory measure the streaming pass; top-20 (pos+val) is the recovered motifs split into position and value matches; t. mat. and mem. mat. are time and memory charged with full materialization (protocol in §4). Unmarked recovery uses exact Stumpy fixed-exclusion ground truth,** <sup>†</sup> **the exact Scamp-GPU reference. Baselines: wall time for the identical multi-length task. Dashes: unscored or cost-bounded, not failed.**

