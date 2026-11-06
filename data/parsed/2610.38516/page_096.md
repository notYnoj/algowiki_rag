<tbc>**Binary models**, same protocol (training p 50; the edge-target model’s thresholded output at low p is speckle, hence its count errors above 1):

Consistency: the exact solve at the training p equals the stored converged outputs. `dist\_sched10\_bg` at p = 20 gives 0.795 / 0.649 / 0.668 / 0.715 / 0.182, the jacobian evaluation of section 12.2. `rw\_learned` at p = 50 gives 0.710 / 0.602 / 0.480 / 0.366 / 0.322. `edge\_bce` at p = 50 gives 0.707 / 0.434 / 0.346 / 0.360 / 1.100 against 0.707 / 0.435 / 0.347 / 0.368 / 1.111: that model’s stored PCG solve differs from the exact one on 0.05 % of the pixels. The three limit rows equal the full-fold limits of section 12.2 (`edge\_bce` was not in 12.2; its 307-patch limit in section 10 was IoU 0.684 / F1 0.501).

Figure `results/pannuke\_p\_sweep/p\_sweep.png`: (a) the instance model’s F1, PQ, IoU and AJI against p on a log axis, with the limit drawn at the right edge (\(\infty\)) and the training p dashed; (b) the same for the two binary models; (c) the disagreement with the limit (log scale), with the training p ringed.

- **Instance model: accuracy peaks at the training p and falls monotonically to the limit; it is not flat.** From p = 5 to 20 every metric rises (F1 0.691 \(\rightarrow\) 0.795: at low p the solve is too soft to separate touching nuclei). Past the training p every metric falls: F1 0.781 at 35, 0.761 at 50, 0.735 at 100, 0.727 at 200, 0.724 at 500, and 0.724 at the limit. 85 % of the total loss (0.071 F1, 0.064 PQ, 0.090 AJI, 0.085 IoU) has happened by p = 100. The loss is in detection, not in the quality of the matched nuclei: SQ goes 0.816 \(\rightarrow\) 0.809, while the count error rises from 0.182 to 0.274. This is the temperature dependence of the costs section 11.5 diagnosed: trained from its own markers, the solve hedges at p = 20 (it vetoes weak markers through soft unaries and shares contested pixels), and a higher p removes the hedging. The costs are tuned to the training temperature. Nothing between the training p and the limit does better than the training p.<tbc>

**-** **Agreement with the limit increases smoothly with p but is total only asymptotically.** At the training p, 4.4 % of the pixels (25 % of the foreground) carry another label than the limit’s. At p = 100 it is 0.70 %<tbc>

\begin{tabular}{ccccccccccc}
p & IoU & BF<sub>2</sub> & `F1@0.5` & PQ & SQ & AJI & count err. & px \(\neq\) limit (of fg) & patches = limit \\
5 & 0.628 & 0.630 & 0.691 & 0.508 & 0.735 & 0.600 & 0.231 & 6.51 % (39.0 %) & 3.6 % \\
10 & 0.687 & 0.730 & 0.760 & 0.600 & 0.789 & 0.650 & 0.210 & 5.56 % (32.5 %) & 3.7 % \\
**20** (train) & **0.715** & **0.775** & **0.795** & **0.649** & **0.816** & **0.668** & **0.182** & 4.45 % (25.3 %) & 3.9 % \\
35 & 0.692 & 0.752 & 0.781 & 0.635 & 0.813 & 0.644 & 0.190 & 3.01 % (17.9 %) & 4.4 % \\
50 & 0.669 & 0.731 & 0.761 & 0.618 & 0.812 & 0.621 & 0.216 & 1.96 % (12.2 %) & 4.6 % \\
100 & 0.641 & 0.706 & 0.735 & 0.595 & 0.810 & 0.590 & 0.258 & 0.70 % (4.6 %) & 5.4 % \\
200 & 0.633 & 0.699 & 0.727 & 0.588 & 0.809 & 0.582 & 0.270 & 0.23 % (1.5 %) & 8.2 % \\
500 & 0.630 & 0.697 & 0.724 & 0.586 & 0.809 & 0.579 & 0.274 & 0.047 % (0.32 %) & 24.3 % \\
\(\infty\) (exact limit) & 0.630 & 0.697 & 0.724 & 0.585 & 0.809 & 0.578 & 0.274 & 0 & 100 % \\
\end{tabular}

\begin{tabular}{ccccccccccc}
p & `rw\_learned` IoU / BF<sub>2</sub> / F1 / PQ / AJI, count err. & px \(\neq\) limit (of fg) & `edge\_bce` IoU / BF<sub>2</sub> / F1 / PQ / AJI, count err. & px \(\neq\) limit (of fg) \\
5 & 0.707 / 0.751 / 0.556 / 0.443 / 0.506, 0.687 & 3.77 % (21.1 %) & 0.714 / 0.736 / 0.217 / 0.173 / 0.322, 4.26 & 2.84 % (15.5 %) \\
10 & 0.706 / 0.749 / 0.577 / 0.458 / 0.467, 0.505 & 3.91 % (21.7 %) & 0.712 / 0.728 / 0.180 / 0.144 / 0.330, 6.01 & 2.84 % (15.5 %) \\
20 & 0.706 / 0.748 / 0.586 / 0.464 / 0.419, 0.413 & 3.95 % (21.7 %) & 0.708 / 0.729 / 0.215 / 0.171 / 0.333, 4.72 & 2.68 % (14.7 %) \\
**50** (train) & 0.710 / 0.751 / 0.602 / 0.480 / 0.366, 0.322 & 3.47 % (19.1 %) & 0.707 / 0.753 / 0.434 / 0.346 / 0.360, 1.10 & 1.68 % (9.5 %) \\
100 & 0.707 / 0.752 / 0.630 / 0.504 / 0.395, 0.272 & 2.64 % (14.9 %) & 0.703 / 0.759 / 0.520 / 0.414 / 0.391, 0.540 & 0.94 % (5.5 %) \\
200 & 0.693 / 0.742 / 0.653 / 0.521 / 0.461, 0.252 & 1.69 % (9.9 %) & 0.697 / 0.758 / 0.529 / 0.420 / 0.408, 0.480 & 0.48 % (2.9 %) \\
500 & 0.673 / 0.725 / 0.651 / 0.518 / 0.478, 0.249 & 0.69 % (4.2 %) & 0.693 / 0.755 / 0.523 / 0.415 / 0.411, 0.486 & 0.16 % (0.95 %) \\
\(\infty\) & 0.660 / 0.714 / 0.643 / 0.512 / 0.477, 0.253 & 0 & 0.690 / 0.754 / 0.519 / 0.412 / 0.411, 0.500 & 0 \\
\end{tabular}

