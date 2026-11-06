### Experimental record

The remaining sections reproduce the long-form experimental report of the research repository (`unrolling/finishing-layer-experiments.md`), lightly edited: every run, every table and the negative results, in the order in which they were done. Section numbers of the main text are not those of the report.

### H Conditioning study (hard seeds, 512<sup>2</sup>)

Cases: synthetic shapes with noise \(\sigma\in\{0.05,0.1\}\), 8-bit, costs c\_e = ((I\_u - I\_v)/255)<sup>2</sup>; seeds = ground truth eroded by r = 5 px (refinement regime) or r = 30 px, or a few scribbles (global regime); the `camera` image with Otsu labels eroded likewise. Reference x^p by a diagonally scaled sparse LU in float64 (flagged unreliable when its residual exceeds 1e-8, which happens for the noisy cases beyond p ≈ 500); limit x^\(\infty\) by the exact MSF + plateau algorithm on the integer costs. Figures: `results/conditioning/figures512/*.png`, table `summary.md`.

**Where the limit is reached, and what it costs** (refinement regime, r = 5):

\begin{tabular}{cccccccccc}
_p_ & IoU & BF<sub>2</sub> & F<sub>1</sub>@0.5 & PQ & SQ & AJI & count err. & px \(\neq x^\infty\) & fg px \(\neq x^\infty\) \\
5 & 0.628 & 0.630 & 0.691 & 0.508 & 0.735 & 0.600 & 0.231 & 6.51% & 39.0% \\
10 & 0.687 & 0.730 & 0.760 & 0.600 & 0.789 & 0.650 & 0.210 & 5.56% & 32.5% \\
20 (training) & 0.715 & 0.775 & 0.795 & 0.649 & 0.816 & 0.668 & 0.182 & 4.45% & 25.3% \\
35 & 0.692 & 0.752 & 0.781 & 0.635 & 0.813 & 0.644 & 0.190 & 3.01% & 17.9% \\
50 & 0.669 & 0.731 & 0.761 & 0.618 & 0.812 & 0.621 & 0.216 & 1.96% & 12.2% \\
100 & 0.641 & 0.706 & 0.735 & 0.595 & 0.810 & 0.590 & 0.258 & 0.70% & 4.6% \\
200 & 0.633 & 0.699 & 0.727 & 0.588 & 0.809 & 0.582 & 0.270 & 0.23% & 1.5% \\
500 & 0.630 & 0.697 & 0.724 & 0.586 & 0.809 & 0.579 & 0.274 & 0.047% & 0.32% \\
\(\infty\) (exact limit) & 0.630 & 0.697 & 0.724 & 0.585 & 0.809 & 0.578 & 0.274 & 0 & 0 \\
\end{tabular}

\begin{tabular}{ccccccc}
case & p & \(\kappa(\text{L}\text{\_U})\) & CG fp32 iters to 1e-3 & labels \(\neq\) x^\(\infty\) & edges carrying 90 % of the gradient \\
clean, \(\sigma\) = 0.05 & 10 & 1.8e2 & 39 & 0.7 % & 14 276 \\
 & 100 & 4.7e2 & 53 & 0 & 5 945 \\
 & 200 & 5.7e3 & 63 & 0 & 844 \\
 & 1000 & 2.3e17 & 173 & 0 & 7 \\
noisy, \(\sigma\) = 0.1 & 10 & 2.0e2 & 42 & 3.1 % & 14 645 \\
 & 100 & 1.5e10 & 89 & 2.2 % & 8 351 \\
 & 500 & 1.0e48 & 240 & 1.2 % & 681 \\
camera & 10 & 5.5e2 & 62 & 9.8 % & 23 602 \\
 & 100 & 1.7e7 & 104 & 5.5 % & 13 044 \\
 & 500 & 4.1e33 & 154 & 4.1 % & 5 503 \\
\end{tabular}

** 9.** Instance WS layer on fold 2 solved exactly at increasing _p_, costs and markers fixed. The last two columns give the pixels labelled unlike the limit, over all pixels and over the pixels that are foreground in either output.

