# The Power Watershed as a Differentiable Layer

71

<tbc>340-400 s against 184 s in section 11.3, which is the node, not the schedule: all three training jobs landed on ruche-gpu16, `dist\_sched20` is as slow before epoch 20 as after it, the same converged solve takes 158 ms per image there and 90 ms on ruche-gpu18 at the same PCG iteration count (the `bg` evaluation), the node threw a CUDA error on the third job, and the four grid jobs trained at 189-206 s per epoch on four other nodes.

**Results on fold 2** (the section 11.1 layer and the section 11.2 baseline for reference; markers = nuclei with one / none / several, background markers per patch; the oracle with ground-truth markers; the exact Power Watershed limit of the learned costs on the 307 limit patches):

Paired on fold 2 (F1 / PQ / AJI / IoU, bootstrap intervals in `compare\_11\_5. md`): `dist\_sched10` - `dist` +0.002 \[-0.001, +0.004\] / +0.004 \[+0.002, +0.006\] / +0.013 \[+0.012, +0.016\] / +0.010 \[+0.007, +0.013\]; `dist\_sched20` - `dist` +0.002 \[-0.000, +0.004\] / +0.004 \[+0.002, +0.005\] / +0.011 / +0.007; `dist\_ sched10` - `dist\_sched20` 0.000 / 0.000 / +0.003 / +0.003; `dist\_sched10\_bg` - `dist` +0.005 \[+0.002, +0.007\] / +0.008 \[+0.006, +0.010\] / +0.015 \[+0.013, +0.017\] / +0.009 \[+0.005, +0.012\], and `dist\_sched10\_bg` - `dist\_sched10` +0.003 \[+0.001, +0.005\] / +0.004 \[+0.002, +0.005\] / +0.002 / -0.001. Against the baseline, `unet\_dist` - `dist\_sched10` = +0.002 \[-0.001, +0.004\] / +0.009 \[+0.007, +0.011\] / -0.008 \[-0.010, -0.005\] / +0.002 \[-0.001, +0.005\], and `unet\_dist` - `dist\_sched10\_bg` = -0.001 \[-0.004, +0.002\] / +0.005 \[+0.003, +0.007\] / -0.009 \[-0.012, -0.007\] / +0.004 \[+0.001, +0.007\]. On the oracles, `dist\_sched10` - `dist` = -0.081 F1 / -0.079 PQ, `dist\_sched20` - `dist` = -0.057 / -0.060 and `dist\_sched10\_bg` - `dist` = -0.086 / -0.082; on the limit patches -0.065 / -0.044, -0.040 / -0.027 and -0.058 / -0.039.

**- The mismatch was real but small: closing it gains 0.004 PQ, 0.013 AJI, 0.010 IoU and a fifth of the count error, and nothing on F1.** Both schedules land on the same output (0.792 / 0.645), the longer one marginally ahead on AJI and IoU. The gains are where the diagnosis placed them: the solve now copes with the markers it is given. The fold-3 tuning table is flat in the minimum area (PQ 0.651 at 1, 4, 9 and 16 px, where the 11.1 model went 0.640 \(\rightarrow\) 0.646), so the tuning keeps the tiny markers and the test fold gets 4.3 background markers per patch instead of 3.6 at a lower count error (0.186 against 0.239); the fallback markers of section 11, which cost the 11.1 model 0.015 F1, now cost 0.002; and the sparse patches, where a spurious marker is a large share of the count, move most (\< 10 nuclei: F1 0.689 \(\rightarrow\) 0.704, PQ 0.553 \(\rightarrow\) 0.568, count error 0.64 \(\rightarrow\) 0.44; the three crowded bins within +0.007). A background marker still becomes an instance at test time, but a smaller and better-confined one.<tbc>

**- Giving the unmarked nuclei to the background is the better rule.** With `--mk-unmarked bg` the pixels of a nucleus without a marker are no<tbc>

\begin{tabular}{cccccccccccc}
run & training markers & F1 / PQ / AJI / IoU & \multicolumn{2}{c}{count err.} & \multicolumn{2}{c}{markers (fold-3 choice)} & \multicolumn{2}{c}{oracle F1 / PQ / limit F1 / PQ (307)} & & & \\
`dist` (11.1) & ground truth & 0.791 / 0.641 / 0.653 / 0.707 & 0.239 & 83.9 / 14.5 / 1.6 %, 3.6 & (thr 0.2, area 16, h 0.2) & 0.959 / 0.805 & 0.758 / 0.603 & & & \\
`dist\_sched10` & predicted from epoch 10 (all from 15) & 0.792 / 0.645 / 0.666 / 0.717 & 0.186 & 85.6 / 12.8 / 1.6 %, 4.3 & (thr 0.2, area 1, h 0.2) & 0.877 / 0.725 & 0.694 / 0.558 & & & \\
`dist\_sched20` & predicted from epoch 20 (all from 25) & 0.792 / 0.645 / 0.663 / 0.714 & 0.197 & 85.7 / 12.6 / 1.7 %, 4.3 & (thr 0.2, area 1, h 0.2) & 0.902 / 0.745 & 0.719 / 0.576 & & & \\
`dist\_sched10\_bg` & as `sched10`, unmarked nuclei \(\rightarrow\) background & **0.795** / **0.649** / **0.668** / **0.715** & **0.182** & 85.5 / 12.7 / 1.8 %, 4.3 & (thr 0.2, area 4, h 0.2) & 0.872 / 0.723 & 0.700 / 0.564 & & & \\
`unet\_dist` (11.2) & - (watershed) & 0.794 / 0.655 / 0.658 / 0.719 & 0.190 & 76.6 / 21.8 / 1.6 %, 1.6 & 0.867 / 0.708 & - & & & & \\
\end{tabular}

