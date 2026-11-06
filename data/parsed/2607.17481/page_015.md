<tbc>_Maximum performance ( 11)._ Each sweep above moves one constant and holds the rest at their defaults, so the fastest settings never meet in a single run. The maximum-performance configuration combines them, taking the fastest settings that jointly hold full recovery: anchor stride _s=_6, occupancy target \(\alpha=4\), and round cap _P_<sub>max</sub>=1. The radii stay at \((\Delta_m,\Delta_p)=(6,4)\) because a stride of six places non-anchor lengths up to three positions from the nearest anchor, and any \(\Delta_m\) below three would leave those lengths outside every completion box. The sieve width stays at _w=_8 because the width sweep shows no runtime response.  11 reports this configuration against the control, both measured in one session on a fresh instance of the benchmark machine type. The session is directly comparable to the sweeps. The control rerun reproduced every recovery, position, and value count of the sweep session from a byte-identical binary, and its total runtime moved by half a percent. The combined configuration recovers all 740 motifs at 5.9\(\times\) lower total runtime, 139s against 823s across the benchmark. Wafer 5M completes in 52.1s against 362s, and StarLightCurves 1M in 10.1s against 53.1s. Exact positions are 308 of 340 against the control’s 310. The cost of the speed is two positions and no motif.

A final configuration pushes the combination to the floor of the width range. Taking \(\alpha=4\) and _P_<sub>max</sub>=1 at the more aggressive stride _s=_8 and fixing _K=_4 trades the calibration’s collision headroom for speed on top of the quartered budget, the two thinnest margins in the design. The configuration recovers 740 of 740 motifs, at 104.3s total against the control’s 823s, a 7.9\(\times\) reduction. Wafer 5M completes in 38.2s against 362s. Exact positions are 292 of 340. This configuration was measured in its own session on a fresh instance of the same machine type from a byte-identical binary. Its outputs are deterministic (Prop. 5), and the control totals reproduced across sessions within half a percent.

4 condenses the study. The sweeps were run after every default was fixed and did not inform any default. Tuning constants from prior analysis of the benchmark datasets is not part of the study design. **Staying faithful to that design, we report the conservative configuration in  1, although the maximum- performance configuration of  11 delivers the same recovery at a further** 7.9\(\times\) **lower runtime.**

\begin{tabular}{ccccc}
Constant & Setting & Rec. & Pos. & Time \\
Anchor stride _s_ & 1 (dense) & 740 & 313 & 1.92\(\times\) \\
(§3.3) & 2<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
 & 4 & 740 & 305 & 0.58\(\times\) \\
 & 6 & 740 & 306 & 0.43\(\times\) \\
 & 8 & 740 & 306 & 0.37\(\times\) \\
Sieve width _w_ & 2 & 740 & 306 & 1.02\(\times\) \\
(§3.6) & 4 & 740 & 310 & 1.00\(\times\) \\
 & 8<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
 & 16 & 740 & 314 & 1.01\(\times\) \\
 & 32 & 740 & 323 & 1.02\(\times\) \\
Radii (\(\Delta_m,\Delta_p\)) & (2,1) & 740 & 308 & 1.05\(\times\) \\
(§3.6) & (3,2) & 740 & 308 & 1.02\(\times\) \\
 & (6,4)<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
 & (12,8) & 740 & 310 & 1.00\(\times\) \\
Round cap _P_<sub>max</sub> & 1 & 740 & 310 & 0.58\(\times\) \\
(§3.6) & 2 & 740 & 310 & 0.67\(\times\) \\
 & 4 & 740 & 310 & 0.81\(\times\) \\
 & 8<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
Occupancy \(\alpha\) & 4 & 740 & 306 & 0.74\(\times\) \\
(§3.4) & 8 & 740 & 306 & 0.83\(\times\) \\
 & 16<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
 & 32 & 740 & 319 & 1.34\(\times\) \\
 & 64 & 740 & 320 & 1.93\(\times\) \\
Spectral width _K_ & 4 & 740 & 315 & 0.81\(\times\) \\
(§3.2) & 8 & 740 & 310 & 0.87\(\times\) \\
 & 12 & 740 & 315 & 0.96\(\times\) \\
 & 16 & 740 & 316 & 1.00\(\times\) \\
 & calibrated<sup>⋆</sup> & 740 & 310 & 1.00\(\times\) \\
\end{tabular}

Anchor stride S
Sieve width w
Radii (A, Ap)
runtime (x def.)
2
1.93
1.00
1.01
1.00
1.00
1.00
1.02
1.03
1.02
1.00
1
0.57
0.42
0.97
1.00
1
2
4
6
8
2
4
8
16
32
(2,1)
(3,2)
(6,4)
(12,8)
Round cap P max
Occupancy a
Spectral width K
runtime (x def.)
2
1.94
1.34
1.00
1.00
1.00
1.00
1
0.80
0.83
0.81
0.86
0.95
0.58
0.67
0.80
0.74
0.83
0.81
0.86
0.95
1
2
4
8
4
8
16
32
64
4
8
12
16
cal.

**Figure 4: Runtime response to each design constant, aggregated over the 37 benchmark rows and normalized to the default configuration (star). Recovery is 740 of 740 at every plotted setting; only runtime responds.**

** 4: Summary of the parameter study. Each row changes one constant; all others stay at their defaults (⋆). Rec.: recovered motifs over all 37 rows (of 740). Pos.: exact-position matches on the seventeen exact-ground-truth rows (of 340). Time: summed runtime relative to the control.**

