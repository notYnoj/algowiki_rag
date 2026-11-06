<tbc>iterations, evaluation to 1e-5; 290 s per epoch, 2.4 h in all, 1 h for the evaluation (four solves per batch plus the CPU metrics).

**Test markers** are the 4-connected components of the thresholded marker map (0.5). Each ground-truth nucleus is counted as having exactly one, none or several predicted markers (a marker belongs to the nucleus holding the majority of its pixels), and markers in background are counted. A second variant ("fallback") adds a marker at the distance-transform maximum of every foreground component (s _\>_ 0.5, \(\ge\) 16 px) that has none. The oracle row runs the same trained costs from the ground-truth markers (eroded by 2 px): it bounds what better markers could give.

**Baselines and controls.** The plain U-Net + connected components of section 6 (binary target) and the contour-head U-Net with the tuned marker watershed of section 10.1 (the strongest pipeline so far), both re-used from their per-image files; within this model, its own foreground logits + components, the classical marker watershed (skimage) of the learned contour map inside s _\>_ 0.5 from the same predicted markers, the converged solve and the exact limit with image-gradient edge costs in place of the learned ones (the RMS colour difference across each edge, scaled per patch so that its 99th percentile equals the unary clamp 8: the marker-controlled watershed with the U-Net’s background as a soft seed), and the exact K-label limit of the learned costs on the 307 patches of section 6. Instance metrics are computed on the label maps themselves (argmax over the K + 1 labels; one predicted instance per label that wins at least one pixel), pixel metrics on the foreground (label _\>_ 0) against the binary mask, so they are comparable with section 6’s rows.

**Results on all of fold 2** (2523 patches; the limits on 307):

**Marker quality.** Fold 2 has 59 872 nuclei (23.7 per patch); the marker head gives 30.5 markers per patch. 73.2 % of the nuclei get exactly one marker, 17.4 % none, 9.5 % several; 5.9 markers per patch lie in background. With the fallback: 76.3 / 13.8 / 9.9 % and 8.2 background markers per patch. By crowding (one / none / several; background markers per patch): fewer than 10 nuclei 69 / 19 / 12 %, 2.6; 10–30: 75 / 15 / 11 %, 6.1; 30–60: 74 / 16 / 9 %, 7.9; more than 60: 69 / 26 / 6 %, 8.1.

**Paired per-patch differences** (bootstrap 95 % intervals; F1, PQ and AJI dataset-level, bootstrapped over patches):

\begin{tabular}{ccccccccccccc}
output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & edge align. & **F100.5** & PQ & AJI & count err. & n & pred \\
U-Net (sec. 6), s _\>_ 0.5, components & **0.719** & 0.652 & 0.769 & 0.807 & 0.577 & 0.656 & 0.531 & 0.494 & **0.275** & 23.0 & \\
U-Net + contour head (sec. 10.1), logits & **0.719** & **0.658** & **0.774** & **0.809** & 0.574 & 0.682 & 0.556 & 0.571 & 0.303 & 25.2 & \\
U-Net + contour head, tuned marker watershed (b) & 0.718 & **0.658** & **0.774** & **0.809** & 0.568 & **0.715** & **0.583** & **0.657** & 0.344 & 27.2 & \\
this model, s _\>_ 0.5, components & 0.575 & 0.408 & 0.580 & 0.691 & 0.402 & 0.024 & 0.017 & 0.168 & 52.7 & 723 & \\
this model, layer, converged, predicted markers & 0.796 & 0.643 & 0.759 & 0.735 & **0.585** & 0.681 & 0.554 & 0.652 & 0.460 & 28.6 & \\
this model, layer + fallback markers & 0.702 & 0.641 & 0.757 & 0.798 & 0.586 & 0.657 & 0.534 & 0.652 & 0.585 & 31.1 & \\
this model, layer, image-gradient costs & 0.487 & 0.203 & 0.351 & 0.592 & 0.248 & 0.355 & 0.218 & 0.470 & 0.529 & 29.9 & \\
this model, marker watershed on the contour map, same markers & 0.615 & 0.455 & 0.633 & 0.684 & 0.430 & 0.597 & 0.414 & 0.541 & 0.546 & 30.2 & \\
this model, PW limit, learned costs (307) & 0.690 & 0.613 & 0.736 & 0.781 & 0.579 & 0.661 & 0.526 & 0.612 & 0.426 & 29.8 & \\
this model, PW limit, image-gradient costs (307) & 0.479 & 0.202 & 0.341 & 0.589 & 0.241 & 0.335 & 0.204 & 0.451 & 0.507 & 31.5 & \\
this model, layer, ground-truth markers (oracle) & 0.859 & 0.796 & 0.922 & 0.858 & 0.591 & 0.959 & 0.805 & 0.858 & 0.020 & 23.3 & \\
ground truth instances & 1 & 1 & 1 & 1 & 0.559 & 1 & 1 & 1 & 0 & 23.7 & \\
\end{tabular}

\begin{tabular}{ccccccccccccc}
comparison & IoU & BF<sub>2</sub> & edge align. & **F100.5** & PQ & AJI & count err. & n & pred & & & \\
layer + U-Net (sec. 6) & -0.013 & -0.016, -0.010 & -0.011 & -0.014, -0.007 & +0.009 & +0.008, +0.010 & +0.024 & +0.018, +0.031 & +0.022 & +0.018, +0.029 & +0.158 & +0.143, +0.173 \\
layer + contour-head U-Net, watershed (b) & -0.012 & -0.015, -0.009 & -0.016 & -0.019, -0.012 & +0.018 & +0.017, +0.020 & -0.034 & -0.039, -0.036 & -0.029 & -0.033, -0.025 & -0.005 & -0.008, -0.003 \\
layer + marker watershed, same markers & +0.091 & & +0.126 & & +0.155 & & +0.084 & +0.081, +0.087 & +0.140 & & +0.111 & \\
layer + layer with image-gradient costs & +0.218 & & +0.407 & & +0.337 & & +0.325 & +0.317, +0.335 & +0.336 & & +0.182 & \\
layer + fallback - layer & -0.004 & -0.007, -0.001 & -0.002 & & -0.001 & & -0.024 & -0.025, -0.023 & -0.020 & & -0.000 & \\
layer, ground-truth markers - layer & +0.153 & +0.148, +0.158 & +0.163 & & +0.006 & & +0.278 & +0.272, +0.283 & +0.251 & & +0.206 & \\
307 patches: PW limit (learned) - layer & -0.008 & +0.011, -0.003 & +0.013 & -0.016, -0.009 & +0.003 & +0.004, +0.002 & +0.007 & +0.003, +0.016 & +0.003 & +0.006, -0.000 & -0.017 & -0.020, -0.015 \\
307 patches: PW limit (learned) - U-Net (sec. 6) & -0.024 & -0.031, -0.016 & -0.027 & & +0.011 & & +0.027 & +0.010, +0.043 & +0.017 & +0.003, +0.036 & +0.187 & \\
\end{tabular}

