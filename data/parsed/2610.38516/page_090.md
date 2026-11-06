**- The implicit mode is the cheaper one in memory at any useful accuracy, and in time once** \(\text{\textbf{p}}\ge\text{\textbf{20.}}\) To come within the implicit layer’s 1e-3 the unrolled WS layer needs more than 50 steps at p = 20 and 50 (K = 50 is still 4 % and 19 % off), i.e. more than 1.27 GB and 50 ms for a batch of 16, against the implicit layer’s 92 MB and 44-69 ms. Unrolling 20 steps is cheaper (21 ms, 548 MB) but inaccurate.

**Experiment C (c): one training run per mode and seed. rw\_learned** with the section 6 recipe (fold 1 \(\rightarrow\) all of fold 2, p 5 \(\rightarrow\) 50, BCE on the WS layer + 0.5 BCE on the logits, 30 epochs, batch 16), seeds 0 and 1, unrolled (K = 20) against implicit (PCG to 1e-4, cap 1000, one adjoint solve; the evaluation’s converged solve and limit as in section 6). The unrolled seed-0 run is a rerun of section 6’s run with the current code; it reproduces it (IoU -0.001 \[-0.003, +0.001\], F1 +0.005 paired).

The converged solve gives the WS layer’s numbers to the third digit in both modes (`figures/summary.md`). Paired differences on all 2523 patches (bootstrap 95 % intervals; F1 and PQ dataset-level, bootstrapped over patches):

The implicit training solve needed 18-25 forward / 19-26 adjoint PCG steps per batch in the first epoch (p = 5), about 135 / 110 at epoch 10, 165-205 / 150 at epoch 20 and 210 / 220 at the end (p = 50); 3.4-3.8 % of the forward solves over the run reached the 1000-step cap (all late, at high p), so training took twice as long as the unrolled run (26 s against 13 s per epoch on the A100, 13 against 6.6 min in all).

**-** **Honest outcome: the implicit mode trains a better binary WS layer than 20 unrolled steps, on both seeds.** +0.008-0.009 IoU, +0.018-0.024 BF<sub>2</sub>, +0.035-0.055 F1 and +0.034-0.050 PQ, paired and clear of zero, against a seed-to-seed spread of at most 0.003 IoU and 0.015 F1 within either mode. With it the binary WS layer reaches the plain U-Net of section 6 on the pixel metrics (IoU -0.003 / -0.000, BF<sub>2</sub> +0.000 / +0.004) and has the lowest count error of the three (0.25 against 0.28), but stays 0.007-0.012 F1 / PQ behind on instances, and its AJI is lower than the unrolled WS layer’s (0.42-0.43 against 0.43-0.46). So section 6’s "the WS layer costs a little" was, on the pixel metrics, in good part the truncated solver: trained through the<tbc>

\begin{tabular}{ccccccccccccc}
run & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & `F100.5` & PQ & AJI & count err. & s / epoch & & \\
U-Net (sec. 6) & s \> 0.5 & 0.719 & 0.652 & 0.769 & 0.807 & 0.656 & 0.531 & 0.494 & 0.275 & - & & \\
unrolled, seed 0 & WS layer & 0.708 & 0.629 & 0.751 & 0.799 & 0.609 & 0.486 & 0.456 & 0.330 & 13.3 & & \\
unrolled, seed 1 & WS layer & 0.709 & 0.626 & 0.750 & 0.798 & 0.594 & 0.473 & 0.433 & 0.341 & 13.2 & & \\
implicit, seed 0 & WS layer & 0.716 & **0.652** & 0.770 & 0.804 & 0.644 & 0.519 & 0.419 & 0.256 & 26.1 & & \\
implicit, seed 1 & WS layer & **0.719** & **0.655** & **0.773** & 0.806 & 0.649 & 0.523 & 0.430 & **0.249** & & 26.1 & \\
unrolled, seed 0 / 1 & PW limit (307) & 0.668 / 0.620 & 0.597 / 0.566 & 0.719 / 0.676 & 0.775 / 0.745 & 0.630 / 0.575 & 0.501 / 0.456 & 0.440 / 0.353 & 0.246 / 0.298 & & \\
implicit, seed 0 / 1 & PW limit (307) & 0.602 / 0.604 & 0.573 / 0.582 & 0.677 / 0.684 & 0.730 / 0.736 & 0.595 / 0.611 & 0.486 / 0.498 & 0.282 / 0.352 & 0.417 / 0.394 & & \\
\end{tabular}

\begin{tabular}{ccccccccccccc}
comparison & IoU & \multicolumn{4}{c}{BF<sub>2</sub>} & \multicolumn{4}{c}{`F100.5`} & \multicolumn{4}{c}{PQ} \\
implicit - unrolled, seed 0 & +0.008 \[+0.005, +0.010\] & +0.018 \[+0.016, +0.020\] & +0.035 \[+0.032, +0.038\] & +0.034 \[+0.031, +0.036\] & +0.009 \[+0.007, +0.012\] & +0.024 \[+0.021, +0.026\] & +0.055 \[+0.052, +0.058\] & +0.050 \[+0.048, +0.053\] & +0.001 \[-0.003, +0.001\] & +0.002 \[-0.001, +0.004\] & +0.015 \[+0.013, +0.018\] & +0.013 \[+0.011, +0.015\] \\
implicit seed 0 - seed 1 & -0.003 \[-0.005, -0.001\] & -0.004 \[-0.006, -0.002\] & -0.005 \[-0.007, -0.002\] & -0.004 \[-0.006, -0.002\] & -0.004 \[-0.006, -0.002\] & -0.005 \[-0.007, -0.002\] & -0.004 \[-0.006, -0.002\] & -0.003 \[-0.005, -0.001\] & -0.004 \[-0.002, +0.003\] & -0.002 \[-0.002, +0.003\] & -0.003 \[-0.002, +0.003\] & -0.004 \[-0.002, +0.003\] & -0.003 \[-0.002, +0.002\] \\
implicit - U-Net (sec. 6), seed 0 & -0.003 \[-0.005, -0.001\] & +0.000 \[-0.002, +0.007\] & -0.007 \[-0.010, -0.004\] & -0.007 \[-0.010, -0.004\] & -0.007 \[-0.010, -0.005\] & -0.008 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] \\
implicit - U-Net (sec. 6), seed 1 & -0.000 \[-0.002, +0.002\] & +0.004 \[+0.002, +0.007\] & -0.007 \[-0.010, -0.004\] & -0.007 \[-0.010, -0.005\] & -0.008 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] & -0.009 \[-0.008, -0.009\] \\
\end{tabular}

