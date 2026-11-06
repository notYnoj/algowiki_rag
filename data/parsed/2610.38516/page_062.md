<tbc>everything held fixed except the solve), and this model’s markers through the WS layer’s solve. The marker-quality count section 11.1 are computed for both sets of markers.

**Results on all of fold 2** (2523 patches; the reference rows repeated from sections 10.1 and 11.1):

**Marker quality** (nuclei with exactly one / no / several markers; markers in background per patch; markers per patch for 23.7 nuclei): `unet\_dist` 76.6 / 21.8 / 1.6 %, 1.6, 20.6; the `dist` layer 83.9 / 14.5 / 1.6 %, 3.6, 24.3 (recomputed here to the same digits); `bce\_tuned` 77.7 / 21.1 / 1.2 %, 2.7, 21.7. By crowding for `unet\_dist` (one / none / several, background per patch): fewer than 10 nuclei 72 / 26 / 2 %, 0.7; 10-30: 79 / 19 / 2 %, 1.6; 30-60: 77 / 21 / 2 %, 2.3; more than 60: 70 / 29 / 1 %, 3.2 (the WS layer: 83 / 14 / 2 %, 1.8; 87 / 11 / 2 %, 3.5; 84 / 14 / 2 %, 4.7; 77 / 22 / 1 %, 6.6). Inference: 0.8 ms U-Net forward plus 16 ms of post-processing per image on one CPU core (markers and all three watersheds), against 94 ms for the WS layer’s converged solve on the GPU.

**Paired per-patch differences** (bootstrap 95 % intervals; F1, PQ and AJI dataset-level, bootstrapped over patches):

By crowding (F1 / PQ / count error), `dist` layer vs `unet\_dist` watershed: fewer than 10 nuclei (486 patches) 0.689 / 0.553 / 0.64 vs 0.727 / 0.592 / 0.35; 10-30 (1383) 0.802 / 0.655 / 0.16 vs 0.809 / 0.672 / 0.15; 30-60 (525) 0.801 / 0.648 / 0.10 vs 0.803 / 0.660 / 0.14; more than 60 (129) 0.763 / 0.615 / 0.15 vs 0.754 / 0.613 / 0.23. Per tissue (IoU / F1 / PQ, `unet\_dist` vs `dist` layer): Breast (749) 0.717 / 0.825 / 0.665 vs 0.708 / 0.817 / 0.647; Colon (468) 0.696 / 0.708 / 0.564 vs 0.683 / 0.709 / 0.558; HeadNeck (169) 0.710 / 0.788 / 0.655 vs 0.701 / 0.784 / 0.647; Adrenal (148) 0.711 / 0.824 / 0.706 vs 0.709 / 0.823 / 0.696; Lung (53) 0.657 / 0.713 / 0.580 vs 0.690 / 0.764 / 0.612; the baseline has the higher F1 on 10 and the higher PQ on 14 of the 15 tissues with at least 50 patches. Figures: `results/pannuke\_instances/unet\_dist/figures/ training.png` (the validation curve of the post-processed output, F1 0.73 \(\rightarrow\) 0.81 on the first 200 test patches with the untuned default thresholds, is above the WS layer’s at every checkpoint; the logits reach IoU 0.720 on the same patches), `examples\_crop.png` (the same eight Colon crops as sections 11 and 11.1, with<tbc>

\begin{tabular}{ccccccccccccc}
output & IoU & BF<sub>2</sub> & edge align. & `F100.5` & PQ & SQ & DQ & AJI & count err. & n\_pred & & \\
U-Net (sec. 6), s \> 0.5, components & 0.719 & 0.769 & 0.577 & 0.656 & 0.531 & -- & -- & 0.494 & 0.275 & 23.0 & & \\
U-Net + contour head, tuned marker watershed (sec. 10.1 b) & 0.718 & 0.774 & 0.568 & 0.715 & 0.583 & 0.816 & 0.715 & 0.657 & 0.344 & 27.2 & & \\
`bce\_tuned` layer (sec. 11.1) & 0.708 & 0.761 & 0.587 & 0.769 & 0.630 & 0.819 & 0.769 & 0.645 & 0.208 & 21.7 & & \\
`dist` layer, converged (sec. 11.1) & 0.707 & 0.762 & 0.580 & 0.791 & 0.641 & 0.811 & 0.791 & 0.653 & 0.239 & 24.3 & & \\
`dist` layer, ground-truth markers (oracle) & 0.859 & 0.922 & 0.591 & 0.959 & 0.805 & 0.839 & 0.959 & 0.857 & 0.020 & 23.3 & & \\
`unet\_dist` s \> 0.5, component & 0.725 & 0.770 & 0.573 & 0.664 & 0.539 & 0.813 & 0.864 & 0.504 & 0.315 & 24.1 & & \\
`unet\_dist`: distance-head markers + watershed, tuned on fold 3 & 0.719 & 0.774 & **0.591** & **0.794** & **0.655** & **0.824** & **0.794** & 0.658 & **0.190** & 20.6 & & \\
`unet\_dist`: the same, watershed of c / of -d & 0.719 & 0.774 & 0.591 & 0.794 & 0.654 & 0.655 & 0.824 & 0.794 & 0.658 & 0.190 & 20.6 & \\
`unet\_dist`: the same + unmarked components kept & 0.725 & 0.777 & 0.574 & 0.780 & 0.637 & 0.817 & 0.780 & **0.666** & 0.202 & 23.9 & & \\
`unet\_dist` watershed from the ground-truth markers (oracle) & 0.774 & 0.827 & 0.586 & 0.867 & 0.708 & 0.816 & 0.867 & 0.765 & 0.066 & 22.2 & & \\
layer’s markers, `unet\_dist`’s foreground + watershed & 0.726 & 0.777 & 0.575 & 0.781 & 0.639 & 0.819 & 0.781 & 0.671 & 0.196 & 23.5 & & \\
layer’s markers, layer’s own foreground + watershed of its contour map & 0.707 & 0.762 & 0.580 & 0.791 & 0.641 & 0.811 & 0.791 & 0.653 & 0.239 & 24.3 & & \\
`unet\_dist`’s markers, layer’s solve & 0.637 & 0.678 & 0.569 & 0.736 & 0.579 & 0.787 & 0.736 & 0.609 & 0.192 & 20.5 & & \\
\end{tabular}

