<tbc>+0.018/+0.024 BF<sub>2</sub>, +0.035/+0.055 F<sub>1</sub> and +0.034/+0.050 PQ, all with 95% bootstrap intervals clear of zero. The layer is then level with the thresholded U-Net on IoU and BF<sub>2</sub> and 0.007-0.012 behind on F<sub>1</sub> and PQ. Its exact limit, however, is worse than that of the unrolled runs: the costs learned with the true RW gradient at the end of the schedule are not closer to a watershed. An implicit epoch takes twice as long as an unrolled one (26s against 13s), as the number of iterations grows with _p_ along the schedule (about 20 at the start, 210 at the end; 3-4% of the forward solves reach the cap of 1000).

### G From the training temperature to the exact limit

The multi-marker WS layer trained from its own predicted markers ( 3) was evaluated on all 2523 patches of fold 2 with its costs, unaries and test markers<tbc>

\begin{tabular}{cccccccc}
run & output & IoU & BF<sub>2</sub> & edge al. & F<sub>1</sub>@0.5 & PQ & count err. \\
U-Net & thresholded & 0.719 & 0.769 & 0.577 & 0.656 & 0.531 & 0.275 \\
unrolled, seed 0 & layer & 0.708 & 0.751 & 0.580 & 0.609 & 0.486 & 0.330 \\
 & limit & 0.668 & 0.719 & 0.575 & 0.630 & 0.501 & 0.246 \\
unrolled, seed 1 & layer & 0.709 & 0.750 & 0.577 & 0.594 & 0.473 & 0.341 \\
 & limit & 0.620 & 0.676 & 0.574 & 0.575 & 0.456 & 0.298 \\
implicit, seed 0 & layer & 0.716 & 0.770 & 0.601 & 0.644 & 0.519 & 0.256 \\
 & limit & 0.602 & 0.677 & 0.650 & 0.595 & 0.486 & 0.417 \\
implicit, seed 1 & layer & 0.719 & 0.773 & 0.596 & 0.649 & 0.523 & 0.249 \\
 & limit & 0.604 & 0.684 & 0.643 & 0.611 & 0.498 & 0.394 \\
\end{tabular}

(a) multi-marker layer on the GPU, 2562
(b) peak GPU memory above the inputs
(c) exact K-label limit against the solve
101
batch 1, forward + backward
101
batch 16, forward + backward
exact limit, numpy, 1 CPU core exact limit, numba, 1 CPU core
converged solve, GPU, batch 1
102
peak memory per image (MB)
converged solve, GPU, batch 16, per image
102
ms per image
101
ms per image
101
U-Net forward, batch 1
100
U-Net forward, batch 16
same for both solver settings
101
1
2
4
8
16
32
64
128
1
2
4
8
16
32
64
128
1
2
4
8
16
32
64
128
markers K per image
markers K per image
markers K per image
panel (a)
training (1e-4, cap 100), batch 1: forward (solid), backward (dashed)
converged (1e-5), batch 1: forward (solid), backward (dashed)
training (1e-4, cap 100), batch 16: forward (solid), backward (dashed)
converged (1e-5), batch 16: forward (solid), backward (dashed)

**Fig.9.** Multi-marker WS layer against the number of markers _K_ per image: (a) time per image, training and converged settings, batch 1 and 16; (b) peak GPU memory per image; (c) the exact limit on one CPU core against the converged GPU solve.

** 8.** Binary WS layer with learned costs trained in the unrolled mode (_T_=20) or in the implicit mode, fold 1 to fold 2. The layer rows are on all 2523 patches, the exact-limit rows on 307 of them.

