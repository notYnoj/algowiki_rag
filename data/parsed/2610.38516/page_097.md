(4.6 %), at 200 0.23 %, at 500 0.047 % (0.32 % of the foreground, 24 % of the patches identical). The decrease is roughly a power law, about p^-1.5 to p^-1.7 between 50 and 500, and on the patches tried it reaches 0 at p ≈3000. Pixel agreement runs ahead of the metrics: at p = 200 the outputs differ on 0.23 % of the pixels, and F1 / PQ are within 0.003 of the limit's.<tbc>

- **Binary models: pixel accuracy is flat up to the training p, then falls to the limit; instance accuracy rises past the training p. rw\_learned’s** IoU stays at 0.706-0.710 from p = 5 to 100 and falls to 0.693 / 0.673 / 0.660 at 200 / 500 / \(\infty\). Its F1 and PQ rise steadily up to p = 200 (\(0.602\rightarrow 0.653\), \(0.480\rightarrow 0.521\)), above the limit's 0.643 / 0.512. The edge-target model goes the same way, more sharply: its thresholded output is speckle below its training p (count error 4-6) and is at its best at p = 200 (F1 0.529 / PQ 0.420 against 0.434 / 0.346 at p = 50). For both, the exact limit is within 0.01 F1 of the best finite p: only p = 200-500 beat it, by at most 0.01 F1. This is section 6's finding as a curve: higher p removes the faint spurious blobs that thresholding a soft output leaves, and merges touching nuclei along the way, so detection improves while the pixel boundaries degrade. Agreement converges more slowly than for the instance model (0.69 % / 0.16 % of the pixels at p = 500), because the sigmoid edge costs are \(\le 1\), so p\(\cdot\Delta\)c is smaller at equal p.<tbc>

**- **For the paper.** Between the training p and the limit, the learned instance costs lose accuracy monotonically, and most of the loss is complete by p ≈100, where the finite-p labels already agree with the limit on 99.3 % of the pixels. There is no hidden optimum at larger p, and deploying the limit costs exactly the measured 0.07 F1 of section 11.5. The finite-p curve was computed with the exact elimination above: the Jacobi-PCG used for training and evaluation does not converge beyond p ≈50 on these costs, which bounds the usable annealing range of this solver independently of accuracy.

**Section 1 check with the exact solver** (`cond\_exact.py`, the 512<sup>2</sup> cases of section 1 with hard seeds: the edges from free pixels to seeds become attachments to the seeds' labels; about 1 s per solve). The label column of the section 1 table (and of the paper's  1) is confirmed to 0.001 % wherever the LU reference was flagged reliable. Free pixels differing from x\(^\infty\), exact (stored LU where it existed):

The LU went wrong exactly where its residual flag fired. Section 1’s reading, a few per cent of the free pixels still differing at p = 500 on noisy and natural images, holds: on 8-bit squared costs the smallest cost gaps are 1/65025, so the noisy image still differs on 0.13 % of the free pixels at p = 5000 and `camera` on 1.2 %.

\begin{tabular}{cccccccccc}
case & p = 10 & 100 & 200 & 500 & 1000 & 2000 & 5000 & & \\
clean, \(\sigma\) = 0.05 & 0.677 % (0.677) & 0.004 % (0.004) & 0 & 0 & 0 & 0 & 0 & & 0 \\
noisy, \(\sigma\) = 0.1 & 3.073 % (3.073) & 2.167 % (2.167) & 1.682 % & 1.147 % (1.147) & 0.593 % (0.921, flagged) & 0.122 % (9.354, flagged) & 0.126 % & & \\
camera & 9.823 % (9.823) & 5.516 % (5.516) & 5.130 % & 4.073 % (4.073) & 2.693 % (2.751, flagged) & 1.986 % (9.258, flagged) & 1.174 % & & \\
astronaut & 14.62 % & 10.66 % & 8.55 % & 6.069 % (6.069, flagged) & 4.678 % (6.391, flagged) & 3.402 % (42.16, flagged) & 1.735 % & & \\
\end{tabular}

