- On the clean image the labels of the limit are reached at p≈100 while \(\kappa\) is still a few hundred and CG to a loose tolerance needs about 50 iterations: a comfortable training window. The gradient support has already shrunk by half there and is gone by p≈500 (the zero-temperature collapse of the note).<tbc>

- On noisy or natural images x^p approaches the limit only slowly (a few per cent of the free pixels still differ at p = 500) while \(\kappa\) explodes far beyond anything CG can resolve; the float64 LU itself fails beyond p≈500-1000. The central tension of the note is real there: the last few per cent of agreement with the limit are not reachable by a finite-p solve. They have to come from deploying the combinatorial limit (section 3 measures what that costs).<tbc>

- The CG iteration count to a loose tolerance grows much more slowly than \(\sqrt{\kappa}\) because the ill-conditioning sits in near-isolated pixels that barely affect the residual; Jacobi preconditioning helps by one to two orders of magnitude in \(\kappa\).<tbc>

- Natural images are the hard case. On `astronaut` (Otsu labels eroded by 5 px) x^p still disagrees with the limit on 15 % of the free pixels at p = 10, 11 % at p = 100 and 6 % at p = 500, where the float64 reference already fails; the textures give \(\kappa\approx 5\)e9 at p = 100. The PW limit of a raw-gradient graph on a photograph is simply far from any finite-p solution, which is the same message as the Pets results below: on photographs the edge costs have to be learned.<tbc>

**- Resolution does not change the cost in the refinement regime.** At 1024<sup>2</sup> with the same 5-px erosion, CG needs 39 / 44 / 54 iterations to 1e-3 at p = 10 / 100 / 200, against 39 / 53 / 63 at 512<sup>2</sup>: the work is set by the width of the band, not by the image. In the global regime (r = 30) it grows with the image (160-205 at 1024<sup>2</sup> against 245-260 at 512<sup>2</sup> for a band that is relatively narrower). Truncation at 1024<sup>2</sup>, clean, p = 100: 20 CG steps disagree with the converged solve on 0.01 % of the labels, 50 Jacobi steps on 0.8 %. Figures: `results/conditioning/figures1024/`.

**Truncation** (label disagreement with the converged x^p after K steps):

- In the refinement regime (band of 10 px) 20 unrolled CG steps suffice on clean images, plain Jacobi needs ten times more. In the global regime (r = 30, scribbles) no truncation works: the note's "match the application to the method's weakness" is confirmed quantitatively.

**Cost transform** (`figures\_transforms/`, four 512<sup>2</sup> cases, squared cost vs \(|\Delta\mathrm{I}|\) vs dense rank of the distinct values; all three share the same limit). The transform only moves the p scale. Measured at equal agreement with the limit, it does not buy a cheaper solve: on the clean refinement case the squared cost<tbc>

\begin{tabular}{cccccccc}
case, p = 100 & CG K=10 & CG K=20 & CG K=50 & Jacobi K=10 & Jacobi K=50 & Jacobi K=200 \\
clean, r = 5 & 1.2 % & 0.04 % & 0 & 24 % & 1.3 % & 0.01 % \\
noisy, r = 5 & 18 % & 2.9 % & 0.5 % & 25 % & 13 % & 0.6 % \\
camera, r = 5 & 20 % & 11 % & 3 % & 52 % & 18 % & 7 % \\
clean, r = 30 & 25 % & 23 % & 16 % & 26 % & 25 % & 23 % \\
\end{tabular}

