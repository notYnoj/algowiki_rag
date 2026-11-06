<tbc>well-conditioned systems), which agrees with the float64 implicit adjoint to 1e-9 and with central finite differences (float64, converged solves, h = 1e-5) to a median 3e-9-8e-9 on the entries with non-negligible gradient (the largest and random entries of the horizontal edge costs and of c1) and to 4e-8 along random directions. Compared: autograd through K unrolled PCG steps, K in {5, 10, 20, 50, 200}, in float32 (as trained) and float64; the implicit adjoint in float32 at the training tolerance (1e-4, caps 100 and 1000) and at 1e-5. Median over patches of the relative error \(\|\text{g}-\text{g}\text{\_}\text{ref}\|/\|\text{g}\text{\_}\text{ref}\|\) (cosine in brackets):

Float64 unrolling gives the same errors to three digits up to K = 20, and up to K = 50 at p = 20 and 50 (`grad\_vs\_unroll.png`): the error is truncation, not rounding; float32 rounding (about 1e-5) only shows at K = 50, p = 5 and at K = 200. The cosine is computed over all the edge (resp. unary) entries of a patch.

**Experiment C (b): cost against depth** (binary WS layer, float32, 256<sup>2</sup>, forward + backward):

Unrolled memory grows by 24 MB per step for a batch of 16 (1.5 MB, i.e. six 256<sup>2</sup> float32 tensors, per image and step) and does not depend on p; the implicit layer holds the solution and the inputs only, so its memory is independent of depth, tolerance and p (`unroll\_cost.png`). Time is the same at batch 1 and 16 (launch-bound: 0.33 ms per PCG step either way). The implicit layer costs about as much as 20 unrolled steps at p = 5 (22 against 21 ms) and two to three times more at p = 20-50 (44 and 69 ms), where it runs the 60-110 steps each way that convergence to 1e-4 needs.

**- Unrolling 20 steps does not give the Random Walker’s gradient at the p used in training.** At p = 5 the 20-step gradient is within 12 % of the true one (cosine 0.993); at p = 20 and 50 it is off by 90-93 % on the edge costs (cosine 0.75 and 0.67), while the 20-step forward solution is only 4-9 % off. Fewer steps are worse than useless (K = 5-10: relative errors 1.6-5, cosine 0.05-0.4). Within a few per cent takes 50 steps at p = 20 and between 50 and 200 at p = 50 (K = 50 is still 19 % off there). The unrolled gradient is of course the exact gradient of the 20-step map the network was trained with, so this is not a bug in sections 3-10; it says that those models were trained through a truncated solver whose output is close to the RW solution but whose derivative is not. The implicit adjoint at the training tolerance (1e-4) is within 0.04-0.16 % of the reference with 30-109 steps each way, and at 1e-5 within 3e-5-1e-4.

\begin{tabular}{ccccccccc}
p & unrolled K = 5 & K = 10 & K = 20 & K = 50 & K = 200 & implicit 1e-4 (steps fwd / adj.) & implicit 1e-5 \\
5, edge costs & 4.5 (0.26) & 5.3 (0.23) & 0.12 (0.993) & 2.2e-5 & 9.2e-6 & 1.6e-3 (30 / 29) & 1.1e-4 \\
5, unaries & 3.1 (0.44) & 2.9 (0.33) & 0.065 (0.998) & 1.3e-5 & 9.2e-6 & 7.5e-4 & 5.0e-5 \\
20, edge costs & 2.8 (0.15) & 1.8 (0.39) & 0.90 (0.75) & 0.043 (0.9985) & 2.7e-6 & 1.1e-3 (62 / 60) & 2.9e-5 \\
20, unaries & 1.9 (0.53) & 1.3 (0.75) & 0.50 (0.92) & 0.015 & 1.7e-6 & 5.7e-4 & 1.8e-5 \\
50, edge costs & 5.3 (0.05) & 2.4 (0.19) & 0.93 (0.67) & 0.19 (0.983) & 3.4e-6 & 3.6e-4 (92 / 109) & 3.2e-5 \\
50, unaries & 3.0 (0.28) & 1.6 (0.61) & 0.73 (0.87) & 0.078 (0.997) & 1.4e-6 & 1.8e-4 & 1.7e-5 \\
forward error of x, p = 5 / 20 / 50 & 0.10 / 0.33 / 0.56 & 0.022 / 0.15 / 0.28 & 7.7e-4 / 0.036 / 0.092 & 1.5e-7 / 2.1e-4 / 5.1e-3 & 2e-7 & 2-3e-5 & 1.5-2.7e-6 \\
\end{tabular}

\begin{tabular}{ccccccccc}
 & unrolled K = 5 & 10 & 20 & 50 & 200 & implicit 1e-4, p = 5 / 20 / 50 & & \\
time, batch 16 (ms) & 6 & 11 & 21 & 50 & 198 & 22 / 44 / 69 & & \\
peak memory, batch 16 (MB) & 188 & 308 & 548 & 1268 & 4869 & 92 at every p and tolerance & & \\
peak memory, batch 1 (MB) & 12 & 19 & 34 & 79 & 304 & 5.7 & & \\
\end{tabular}

