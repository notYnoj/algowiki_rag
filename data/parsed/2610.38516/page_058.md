<tbc>and h at the edge of the grid, so the saved model was re-tuned on an extended grid (`dist\_ext`: thr \(\in\{0.1,0.15,0.2,0.3\}\), h \(\in\{0.2,0.3,0.4\}\), min area \(\in\{9,16\}\)): the fold-3 PQ is a plateau (0.646 for the first choice and for thr 0.2 / min area 9 / h 0.3, 0.640-0.645 for the eight best settings), and the two choices give the same fold 2 result (F1 0.791 / PQ 0.641 against 0.788 / 0.641). The first choice is reported below.

**The solver cap** (`maxit300`). Section 11’s training solve hit its 100-iteration cap from epoch 9 on. The same run with `--maxit 300` (BCE head, untuned thr 0.5 as in section 11, so the comparison is clean) never hits the cap: 112 / 215 / 227 iterations per batch over the three ten-epoch thirds, 778 s per epoch instead of 280 (6.5 h of training). Its validation curve (layer F1 / PQ on the first 200 test patches at epochs 4, 9, 14, 19, 24, 29, untuned markers) is 0.696 / 0.534, 0.703 / 0.546, 0.716 / 0.563, 0.710 / 0.559, 0.730 / 0.576, 0.705 / 0.551, against section 11’s 0.684 / 0.522, 0.727 / 0.571, 0.715 / 0.561, 0.738 / 0.581, 0.722 / 0.570, 0.720 / 0.564: the same curve within its epoch-to-epoch wobble, and the final losses agree to the third digit (cross-entropy 0.0876 against 0.0909, edge scale 2.09 against 1.99). On all of fold 2 its oracle equals section 11’s (F1 0.960 / PQ 0.806 against 0.959 / 0.805, paired +0.001) -- the costs are the same -- while its own markers are slightly worse (33.0 per patch, 72 / 17 / 10 %, 7.0 in background): F1 0.658 / PQ 0.536, -0.023 F1 \[-0.026, -0.019\] paired against section 11. Re-tuned on fold 3 (`maxit300\_tuned`, thr 0.4, min area 16 px) it reaches F1 0.770 / PQ 0.631, +0.001 F1 \[-0.001, +0.002\] / +0.001 PQ \[-0.000, +0.002\] paired against `bce\_tuned`. So the capped solve of section 11 cost nothing: an approximate forward solve with an implicit gradient of the approximately solved system trains the same costs as the converged one at 2.8 times the price, and the combined distance-head + 300-iteration run was not made.

**Results on all of fold 2** (2523 patches; limits on the 307 of section 6; the three rows of section 11 repeated for reference):

**Marker quality** (nuclei with exactly one / no / several predicted markers; markers in background per patch; markers per patch for 23.7 nuclei): section 11 73.2 / 17.4 / 9.5 %, 5.9, 30.5; `bce\_tuned` 77.7 / 21.1 / 1.2 %, 2.7, 21.7; `dist` 83.9 / 14.5 / 1.6 %, 3.6, 24.3 (with the fallback 85.4 / 12.6 / 2.0 %, 5.0, 26.2); `maxit300` 72.3 / 17.4 / 10.3 %, 7.0, 33.0. By crowding for `dist` (one / none / several, background per patch): fewer than 10 nuclei 83 / 14 / 2 %, 1.8; 10-30: 87 / 11 / 2 %, 3.5; 30-60: 84 / 14 / 2 %, 4.7; more than 60: 77 / 22 / 1 %, 6.6 (section 11: 69 / 19 / 12 %, 2.6; 75 / 15 / 11 %, 6.1; 74 / 16 / 9 %, 7.9; 69 / 26 / 6 %, 8.1).

**Paired per-patch differences** (bootstrap 95 % intervals; F1, PQ and AJI dataset-level, bootstrapped over patches):

\begin{tabular}{ccccccccccccc}
output & IoU & BF<sub>2</sub> & edge align. & `F100.5` & PQ & SQ & DQ & AJI & count err. & n\_pred & & & \\
U-Net (sec. 6), s \> 0.5, components & **0.719** & 0.769 & 0.577 & & 0.656 & 0.531 & - & - & 0.494 & 0.275 & & 23.0 & \\
U-Net + contour head, tuned marker watershed (sec. 10.1 b) & 0.718 & **0.774** & 0.568 & & 0.715 & 0.583 & 0.816 & 0.715 & **0.657** & 0.344 & & 27.2 & \\
sec. 11: layer, BCE marker head, thr 0.5, min area 1 & 0.706 & 0.759 & 0.585 & & 0.681 & 0.554 & 0.814 & 0.681 & 0.652 & 0.460 & & 28.6 & \\
`bce\_tuned`: the same model, thr 0.4, min area 16 (fold 3) & 0.708 & 0.761 & **0.587** & & 0.769 & 0.630 & **0.819** & 0.769 & 0.645 & **0.208** & & 21.7 & \\
`dist`: distance head, h 0.2, thr 0.2, min area 16 (fold 3) & 0.707 & 0.762 & 0.580 & & **0.791** & **0.641** & 0.811 & **0.791** & 0.653 & 0.239 & & 24.3 & \\
`dist`, + fallback markers & 0.704 & 0.760 & 0.582 & & 0.776 & 0.629 & - & - & 0.652 & 0.311 & & 25.7 & \\
`dist`, PW limit, learned costs (307) & 0.683 & 0.728 & 0.574 & & 0.758 & 0.603 & - & - & 0.611 & 0.255 & & 25.0 & \\
`dist`, layer, ground-truth markers (oracle) & 0.859 & 0.922 & 0.591 & & 0.959 & 0.805 & - & - & 0.857 & 0.020 & & 23.3 & \\
`maxit300`: BCE head, 300-iteration training solve, thr 0.5, min area 1 & 0.704 & 0.757 & 0.581 & & 0.658 & 0.536 & - & - & 0.652 & 0.542 & & 30.2 & \\
`maxit300\_tuned`: the same, thr 0.4, min area 16 (fold 3) & 0.707 & 0.760 & 0.584 & & 0.770 & 0.631 & 0.820 & 0.770 & 0.647 & 0.200 & & 21.6 & \\
\end{tabular}

