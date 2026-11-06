<tbc>floating-point difference of the forward pass between the two GPUs, which moves a few markers and cost ties.

**Results on fold 2.** For every model: the finite-p output the report and the paper quote (the 20-step layer at p = 50 for the binary models, the converged solve at p = 20 from the predicted markers for the instance models) and the exact limit of the same costs (and markers), each on the 307-patch subset and on all 2523 patches. Instance metrics on the labels of the output (the 4-connected components of the thresholded output for the binary models).

**Paired limit - finite-p differences** on the same patches (bootstrap 95 % over patches; F1, PQ and AJI dataset-level, recomputed per resample):

**- The subset was representative of the comparisons, not of the absolute instance numbers.** The limit’s pixel-level scores are the same on the subset and on the fold (IoU within 0.008, BF<sub>2</sub> within 0.013, edge alignment within 0.008 for every model), but its instance metrics are 0.02-0.03 higher on the full fold for every model with learned costs (F1 +0.025 / +0.023 / +0.026 / +0.024 and PQ +0.022 / +0.023 / +0.022 / +0.021 for `rw\_learned`, `bce\_tuned`, `dist`, `dist\_sched10\_bg`; AJI +0.052 for `rw\_learned`, +0.022- 0.024 for the others). The reason is the subset, not the limit: the finite-p outputs of the same models lose the same amount on the 307 patches (layer F1 0.581 against 0.604 for `rw\_learned`, 0.766 against 0.791 for `dist`), because the 8 patches with the most touching-nuclei pixels, all crowded Colon, were added to the 300 evenly spaced ones and weigh heavily in the dataset-level counts. Every limit number quoted so far as an absolute instance score (F1, PQ, AJI) is therefore about 0.02 too low; the pixel-level numbers and the count errors stand.<tbc>

**- Every paired conclusion stands, with intervals two to three times narrower.** Limit minus finite-p on the 307 and on the 2523 patches agree<tbc>

\begin{tabular}{cccccccccccc}
model & output & patches & IoU & BF<sub>2</sub> & edge al. & `F100.5` & PQ & AJI & count err. & & \\
`rw\_img` (sec. 6;  2) & WS layer, 20 steps (p = 50) & 307 & 0.681 & 0.709 & 0.552 & 0.496 & 0.382 & 0.325 & 0.564 & & \\
 & & 2523 & 0.683 & 0.714 & 0.559 & 0.516 & 0.400 & 0.396 & 0.513 & & \\
 & exact limit & 307 & 0.181 & 0.254 & 0.796 & 0.194 & 0.150 & 0.109 & 0.675 & & \\
 & & 2523 & 0.174 & 0.251 & 0.804 & 0.209 & 0.163 & 0.128 & 0.676 & & \\
`rw\_learned` (sec. 6;  2) & WS layer, 20 steps (p = 50) & 307 & 0.704 & 0.745 & 0.571 & 0.581 & 0.460 & 0.397 & 0.336 & & \\
 & exact limit & 2523 & 0.709 & 0.752 & 0.579 & 0.604 & 0.482 & 0.456 & 0.337 & & \\
 & & 307 & 0.661 & 0.711 & 0.577 & 0.618 & 0.490 & 0.425 & 0.246 & & \\
 & & 2523 & 0.660 & 0.714 & 0.583 & 0.643 & 0.512 & 0.477 & 0.253 & & \\
`bce\_tuned` (sec. 11 / 11.1;  3) & WS layer, converged (p = 20) & 307 & 0.703 & 0.754 & 0.580 & 0.746 & 0.607 & 0.623 & 0.197 & & \\
 & exact limit & 2523 & 0.708 & 0.761 & 0.587 & 0.769 & 0.630 & 0.645 & 0.208 & & \\
 & & 307 & 0.692 & 0.736 & 0.578 & 0.742 & 0.594 & 0.608 & 0.197 & & \\
`dist` (sec. 11.1;  3) & WS layer, converged (p = 20) & 2523 & 0.696 & 0.743 & 0.586 & 0.765 & 0.617 & 0.630 & 0.207 & & \\
 & & 2523 & 0.697 & 0.748 & 0.575 & 0.766 & 0.618 & 0.629 & 0.255 & & \\
 & exact limit & 307 & 0.707 & 0.762 & 0.580 & 0.791 & 0.641 & 0.653 & 0.239 & & \\
 & & 2523 & 0.683 & 0.728 & 0.574 & 0.758 & 0.603 & 0.611 & 0.255 & & \\
`dist\_sched10\_bg` (sec. 11.5;  3) & WS layer, converged (p = 20) & 307 & 0.705 & 0.763 & 0.581 & 0.771 & 0.626 & 0.642 & 0.184 & & \\
 & & 2523 & 0.715 & 0.775 & 0.588 & 0.795 & 0.649 & 0.668 & 0.182 & & \\
 & exact limit & 307 & 0.625 & 0.691 & 0.622 & 0.700 & 0.564 & 0.554 & 0.286 & & \\
 & & 2523 & 0.630 & 0.697 & 0.625 & 0.724 & 0.585 & 0.578 & 0.274 & & \\
\end{tabular}

\begin{tabular}{cccccccccccc}
model & patches & IoU & BF<sub>2</sub> & \multicolumn{2}{c}{`F100.5`} & PQ & AJI & \multicolumn{2}{c}{count err.} & & \\
`rw\_img` & 307 & -0.500 & -0.524, -0.472 & -0.455 & -0.480, -0.428 & -0.302 & -0.332, -0.272 & -0.232 & -0.255, -0.209 & -0.216 & -0.294, -0.149 & +0.111 & -0.107, +0.283 \\
 & 2523 & -0.509 & -0.520, -0.498 & -0.464 & -0.474, -0.453 & -0.307 & -0.318, -0.296 & -0.237 & -0.246, -0.229 & -0.268 & -0.289, -0.246 & +0.163 & +0.107, +0.213 \\
`rw\_learned` & 307 & -0.043 & -0.056, -0.031 & -0.034 & -0.045, -0.022 & +0.037 & +0.017, +0.058 & +0.029 & +0.012, +0.047 & +0.028 & -0.017, +0.073 & -0.090 & +0.165, -0.027 \\
 & 2523 & -0.050 & -0.055, -0.044 & -0.038 & -0.044, -0.032 & +0.039 & +0.031, +0.047 & +0.031 & +0.024, +0.037 & +0.021 & +0.003, +0.038 & -0.083 & -0.114, -0.053 \\
`bce\_tuned` & 307 & -0.011 & -0.015, -0.007 & -0.017 & -0.022, -0.013 & -0.004 & -0.012, +0.004 & -0.013 & -0.019, -0.006 & -0.015 & -0.018, -0.012 & +0.000 & -0.001, +0.002 \\
 & 2523 & -0.012 & -0.017, -0.007 & -0.018 & -0.023, -0.013 & -0.004 & -0.010, +0.003 & -0.013 & -0.019, -0.007 & -0.015 & -0.020, -0.011 & -0.001 & -0.016, +0.015 \\
`dist` & 307 & -0.014 & -0.016, -0.012 & -0.029 & -0.023, -0.017 & -0.008 & -0.011, -0.005 & -0.016 & -0.018, -0.014 & -0.018 & -0.020, -0.016 & -0.000 & -0.001, +0.001 \\
 & 2523 & -0.015 & -0.020, -0.010 & -0.021 & -0.026, -0.016 & -0.006 & -0.011, -0.002 & -0.016 & -0.021, -0.012 & -0.018 & -0.022, -0.014 & -0.001 & -0.013, +0.012 \\
`dist\_sched10\_bg` & 307 & -0.080 & -0.094, -0.066 & -0.072 & -0.086, -0.058 & -0.071 & -0.083, -0.059 & -0.062 & -0.072, -0.053 & -0.088 & -0.098, -0.078 & +0.102 & +0.070, +0.130 \\
 & 2523 & -0.086 & -0.092, -0.079 & -0.078 & -0.085, -0.072 & -0.071 & -0.077, -0.066 & -0.064 & -0.069, -0.059 & -0.090 & -0.096, -0.084 & +0.093 & +0.076, +0.110 \\
\end{tabular}

