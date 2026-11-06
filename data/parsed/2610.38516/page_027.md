<tbc>2.11, single precision), on 256<sup>2</sup> fold-2 patches; memory is the peak GPU allocation above the inputs. _T_ is the number of unrolled steps and _K_ the number of markers.

### Gradient accuracy.

We compare, on eight fold-2 patches and the binary WS layer with learned costs (Sect. 4.3), the gradient of the binary cross-entropy with respect to the edge costs and to the unaries against a reference: automatic differentiation through a double-precision PCG run to a relative residual of 10<sup>-12</sup>. Central finite differences on the converged solve agree with that reference to a median relative error below 10<sup>-8</sup>. Figure 7 gives the median relative error. The unrolled mode computes the exact gradient of the _truncated_ solver, as its double-precision curve shows, but that is not the gradient of the RW. At _p_=5, _T_=20 steps are already close (cosine 0.993); at _p_=20 and _p_=50 the same 20 steps leave a relative error of 0.9 (cosine 0.75 and 0.67), and _T_=50 and _T_=200 respectively are needed to fall below 5%. The implicit mode at the training tolerance (10<sup>-4</sup>, at most 100 iterations) stays within \(1.6\cdot 10^{-3}\) at every _p_, with 30, 62 and 92 forward iterations at _p_=5, 20 and 50 and as many adjoint ones.

### Time and memory, binary layer.

Unrolling stores every step for the backward pass: for a batch of 16 its memory grows by 24MB per step (0.55GB at _T_=20, 4.9GB at _T_=200) whatever _p_, while the implicit mode needs a constant 0.09GB (Fig. 8). In time, forward plus backward, the implicit mode at _p_=20 costs as much as about 45 unrolled steps, at _p_=50 as much as about 65.

\begin{tabular}{ccccccc}
run & WS layer & baseline & \multicolumn{4}{c}{layer - baseline, F<sub>1</sub> / PQ} \\
seed 0, draw 0 & 0.765 / 0.620 & 0.745 / 0.605 & +0.020 & \[+0.017, +0.023\] / +0.015 & \[+0.013, +0.017\] \\
seed 1, draw 0 & 0.765 / 0.620 & 0.749 / 0.609 & +0.015 & \[+0.012, +0.018\] / +0.011 & \[+0.009, +0.014\] \\
seed 0, draw 1 & 0.765 / 0.624 & 0.749 / 0.612 & +0.017 & \[+0.014, +0.020\] / +0.012 & \[+0.010, +0.014\] \\
\end{tabular}

0.800
0.650
0.775
0.625
0.750
0.600
F1@0.5 on fold 2
0.725
multi-marker WS layer
0.575
U-Net + distance head + marker watershed
PQ on fold 2
0.700
U-Net + connected components
0.550
0.675
0.525
0.650
0.500
0.625
266 (10 %)
664 (25 %)
1328 (50 %)
2656 (100 %)
266 (10 %)
664 (25 %)
1328 (50 %)
2656 (100 %)
training images (fold 1)
training images (fold 1)

**Fig.6.** PQ and F<sub>1</sub>@0.5 on fold 2 against the number of training images from fold 1.

** 7.** The 10% point replicated: F<sub>1</sub>@0.5 / PQ on fold 2 and the paired difference, WS layer minus baseline, with 95% bootstrap intervals.

