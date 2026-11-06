## The multi-marker layer.

Figure 9 times the instance layer at _p_=20 on 16 fold-2 patches with _K_ predicted markers kept (27 on average when all are kept). In the training setting (tolerance 10<sup>-4</sup>, at most 100 iterations; the cap is reached on these patches) the forward pass of a batch of 16 costs 41+20.3_K_ms for \(K\ge 8\), affine to within 0.5%, and the backward pass the same; at batch size 1 the time is flat up to _K_=16, since the GPU is then bound by kernel launches. Memory is 4.8MB per marker and image, 9.8GB for a batch of 16 at _K_=128. The converged setting used at evaluation (10<sup>-5</sup>) needs 190-470 iterations and is two to four times slower. The exact _K_-label limit on one CPU core (Numba) costs 29-51ms per patch for _K_ from 1 to 128, nearly independent of _K_ because it is one spanning forest with per-label solves only on plateaus; this is 2 to 7 times faster than the converged GPU solve at batch size 1. The U-Net itself costs 0.9ms per image at batch 16.

## Training in the two modes.

The binary WS layer with learned costs was retrained with the recipe of Sect. 4.3 (_p_ from 5 to 50, 30 epochs) in each mode and with two seeds ( 8). The implicit mode raises every metric of the layer; the paired differences against the unrolled run of the same seed are +0.008/+0.009 IoU,<tbc>

p = 5 (reference: 80 float64 steps)
p = 20 (reference: 151 float64 steps)
p = 50 (reference: 216 float64 steps)
101
10-1
relative error against the reference
10-3
10-5
unrolled, float32, edge-cost gradient
unrolled, float32, unkey gradient
unrolled, float64, edge-cost gradient
unrolled, float32, forward 4
10-9
implicit, tol 1e-4, cap 100 (39 + 29 it.), edge-cost gradient
implicit, tol 1e-5, cap 1000 (37 + 36 it.), edge-cost gradient
5
10
20
50
200
5
10
20
50
200
5
10
20
50
200
unrolled PCG steps K
unrolled PCG steps K
unrolled PCG steps K

(a) time, batch 16, 2562
(b) peak GPU memory, batch 16
unrolled K steps (any p)
unrolled K steps (any p)
implicit, tol 1e-4, p = 5 (30 + 29 it.)
implicit, tol 1e-4, p = 20 (62 + 63 it.)
implicit, tol 1e-4, p = 50 (92 + 109 it.)
forward + backward (ms per batch of 16)
peak memory above the inputs (MB)
102
103
101
102
5
10
20
50
200
5
10
20
50
200
unrolled PCG steps K
unrolled PCG steps K

**Fig.7.** Relative error of the gradient against a double-precision reference, as a function of the number of unrolled steps _T_, at _p_=5, 20 and 50. Horizontal lines: the implicit mode at two tolerances.

**Fig.8.** Binary WS layer, batch of 16: forward plus backward time and peak memory of _T_ unrolled steps against the implicit mode.

