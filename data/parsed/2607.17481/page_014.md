<tbc>Across the twenty rows the largest rank-wise relative gap is 10.8% (TwoLeadECG) and the largest absolute gap is 0.0102 (ECG200), both inside the §4 tolerances. Every reference motif in the table is therefore accounted for as a position match, a duplicate-window tie counted by value, or a near-miss within tolerance.

## E Parameter Study

This study reruns the complete benchmark of  1 while changing one design constant at a time. Every configuration covers all 37 reported rows, is scored against the same ground truth as §4, and runs on a c3-standard-44 instance with the fixed seed of the reference implementation, so every run is deterministic and every difference between configurations is caused by the changed constant. The control configuration is unmodified Panache; it reproduces  1 exactly, with 740 of 740 motifs recovered and 310 of 340 exact positions on the seventeen rows with exact Stumpy ground truth.

Every runtime in this study is a full-materialization time, the t. mat. accounting of  1. Each run executes the emit stage of §3.6 and writes every profile row, so that the complete output can be checked cell by cell against ground truth, which recovery scoring requires. The materialization work is identical in every configuration, so every ratio below divides two such runs, the shared cost cancels, and the ratio isolates the changed constant.

s 5-9 report every benchmark row under every setting. Cells follow the format of  1. Each cell gives the recovered top-20 motifs with their split into position and value matches, and the runtime in seconds.

**The most important takeaway of this section is that changing a design constant does not affect recovery. Only runtime responds.** All 22 single-constant settings recover 740 of 740 motifs,<tbc>

<tbc>and their exact-position count, out of 340, never differs from the control’s by more than 15. Figure 4 plots the runtime response.  4 summarizes the study.

_Anchor stride ( 5)._ Anchors index every _s_-th length and leave the remaining lengths to local completion (§3.3). Dense indexing (_s_=1) maintains a window and a directory at every length and recovers the same 740 motifs at \(1.92\times\) the total runtime; at Wafer 5M it takes 714 s against 363 s for the default. Coarser strides cut runtime further. At _s_=8 the benchmark completes at \(0.37\times\) the control (130 s at 5M) and still recovers every motif, with exact positions within 4 of the control. Recovery does not depend on the stride anywhere in the swept range; only cost does.

_Sieve width ( 6)._ The sieve evaluates each member of an over-budget bucket against its _w_ nearest neighbors in the projection order (§3.6). It costs at most 2% of total runtime at any width, so this sweep isolates quality. Every width recovers 740 of 740, and widths above the default add up to 13 exact positions (323 of 340 at _w_=32). The one visible per-row effect is StarLightCurves 64k, where _w_=2 yields 18 exact positions and \(w\ge 8\) yields all 20.

_Refinement radii ( 7)._ Local completion evaluates a box of \(\Delta_m\) lengths and \(\Delta_p\) starts around each seed (§3.6). Recovery and runtime are unchanged from (2,1) to (12,8), and positions move by at most two matches. Any radius that reaches the adjacent non- anchor lengths suffices. The neighborhood size is not a sensitive quantity.

_Refinement rounds ( 8)._ Refinement repeats until no cell improves, capped at _P_<sub>max</sub> rounds (§3.6). Exact positions are identical for every cap \(P_\mathrm{max}\ge 1\). Refinement converges in one round on every benchmark row, and later rounds only re-verify. A cap of one round completes the benchmark at \(0.58\times\) the control (200 s against 362 s at Wafer 5M). The default cap of eight is a safety margin for streams where one round does not suffice, not a tuned value.

_Occupancy target ( 9)._ The target \(\alpha\) sets the bucket size the directory maintains, and the verification budget is \(R=8\alpha\) (§3.4). \(\alpha\) is the one parameter exposed to the analyst, and this sweep bounds its risk in both directions. A quarter of the default verification budget (\(\alpha=4\), _R_=32) still recovers 740 of 740 at \(0.74\times\) runtime, and four times the default (\(\alpha=64\)) buys 10 additional exact positions at \(1.94\times\). Mis-setting the only exposed knob by a factor of four in either direction costs no motif.

_Spectral width ( 10)._ The width _K_ is the one constant the calibration of §3.2 sets from data, so this sweep overrides it with fixed widths across the admissible range, \(K\in\{4,8,12,16\}\), in a dedicated session on the same machine type. Proposition 2 states that no width can invalidate an output, and the sweep is the matching measurement for coverage. Recovery is 740 of 740 at every sampled width from the three-bin bound at _K_=4 to the full sixteen, exact positions stay within 6 of the control, and runtime falls as the width narrows, to \(0.81\times\) at _K_=4, where the looser bound performs \(1.41\times\) the exact evaluations but every slide, signature, and stored feature is cheaper. The width moves speed, never discovery. The implementation floors the width at 4, below which the _B_ signature bits would span too few feature dimensions to control bucket occupancy (§3.4).

\begin{tabular}{ccccccc}
Dataset & _n_ & pos & val & ref. best & max \(|\Delta\mathrm{d}|\) & max rel. \\
\multicolumn{7}{c}{_Full natural lengths (capped at 1M)_} \\
ItalyPowerDemand & 1,608 & 20 & 0 & 0.0432 & 3.3-10<sup>-6</sup> & _\<_ 0.1% \\
ECG200 & 9,600 & 16 & 4 & 0.1846 & 0.0102 & 5.3% \\
TwoLeadECG & 93,398 & 12 & 8 & 0.0413 & 0.0045 & 10.8% \\
Wafer & 152,000 & 0 & 20 & 0 & 0 & - \\
Earthquakes & 164,864 & 19 & 1 & 0 & 0 & - \\
ECG5000 & 630,000 & 8 & 12 & 0.0889 & 0.0063 & 7.0% \\
ChlorineConc. & 637,440 & 3 & 17 & 0 & 4.0-10<sup>-4</sup> & - \\
FordA & 660,000 & 13 & 7 & 0.0508 & 0.0049 & 8.3% \\
StarLightCurves & 1M & 1 & 19 & 0 & 9.3-10<sup>-4</sup> & - \\
Mallat & 1M & 0 & 20 & 0 & 0 & - \\
\multicolumn{7}{c}{_Wafer scaling (tiled beyond 152k)_} \\
Wafer & 8k & 17 & 3 & 0 & 0 & - \\
Wafer & 16k & 17 & 3 & 0 & 0 & - \\
Wafer & 32k & 19 & 1 & 0 & 0 & - \\
Wafer & 64k & 10 & 10 & 0 & 0 & - \\
Wafer (6 rows) & 128k-5M & 0 & 20 & 0 & 0 & - \\
\end{tabular}

** 3: Per-row composition of top-20 recovery on the** **†- rows: position matches (pos), value matches (val), best reference distance, and the largest rank-wise deviation between the emitted and reference top-20 value lists, absolute and relative. Relative deviation is reported over ranks with reference distance at least** 0.01**; "-" indicates that no rank meets this threshold. Rows with zero position matches have reference top-20 lists consisting entirely of distance-zero cells, where duplicate windows make position identity non-unique; on all of them the largest value deviation is below** 10<sup>-3</sup>**. The six Wafer rows from 128k to 5M have identical statistics and are shown as one line.**

