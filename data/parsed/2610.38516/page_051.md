<tbc>against the gap target on all of fold 2, instance metrics on the raw 4-connected components; the WS layer rows are section 10’s `edge\_gap\_p10` run.

**After the 8-px min-area filter** (sections 7 and 10’s convention; 32 px in brackets):

**Paired per-patch differences** (2523 patches, bootstrap 95 % intervals; F1 and PQ are dataset-level, bootstrapped over patches):

Per tissue, converged WS layer against (b) (IoU / F1 / PQ): Breast (749) 0.722 / 0.753 / 0.600 vs 0.722 / 0.757 / 0.605; Colon (468) 0.697 / 0.614 / 0.483 vs 0.691 / 0.630 / 0.497; HeadNeck (169) 0.702 / 0.725 / 0.590 vs 0.682 / 0.688 / 0.565; Adrenal (148) 0.724 / 0.778 / 0.654 vs 0.719 / 0.712 / 0.605; the WS layer has the higher IoU on 9 and the higher F1 on 11 of the 15 tissues with \(\ge 50\) patches. By crowding (F1 / count error): fewer than 10 nuclei, layer 0.670 / 0.50 vs watershed 0.596 / 0.81; 10-30: 0.752 / 0.14 vs 0.719 / 0.27; 30-60: 0.718 / 0.14 vs 0.733 / 0.15; more than 60: 0.676 / 0.22 vs 0.700 / 0.13. Seam statistics (seam pixels background / seams cut entirely): contour-head U-Net logits 22 % / 15 %, (a) 68 % / 55 %, (b) 31 % / 17 %, (b’) 37 % / 17 %; the converged WS layer 23 % / 15 %, the 20-step layer 29 % / 19 %. Figures: `results/pannuke/leads/ unet\_edge/figures/examples\_unet\_edge\_crop.png` (the contour head is the same closed 2-3 px contour map as the WS layer’s cost head; (a) shaves every nucleus by that width; (b) splits the large blobs along the contours but leaves merged pairs whose distance transform has a single maximum, and over-splits elongated ones; (b’) cuts more and also along spurious contour fragments).

**-** **Honest outcome: the pixel-level advantage of section 10 does not survive, and the instance advantage survives only without post- processing.** Half of what the edge target gave the WS layer it gives the backbone: with the same contour head, the plain U-Net’s logits gain +0.003 IoU, +0.007 BF<sub>1</sub> and +0.005 BF<sub>2</sub> over the gap U-Net, paired, which is the same margin section 10 attributed to the converged WS layer. Layer against this U-Net the pixel differences are zero (+0.001 IoU with an interval through<tbc>

\begin{tabular}{cccccccccccc}
run & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & edge align. & `F100.5` & PQ & count err. \\
U-Net, gap target (sec. 6.1) & logits & 0.717 & 0.651 & 0.768 & 0.825 & 0.806 & 0.575 & 0.667 & 0.541 & 0.296 \\
U-Net + contour head, edge target & logits & 0.719 & **0.658** & **0.774** & 0.828 & 0.809 & 0.574 & 0.682 & 0.556 & 0.303 \\
 & (a) logits - contour & 0.655 & 0.495 & 0.707 & 0.811 & 0.749 & 0.512 & 0.665 & 0.492 & 0.415 \\
 & (b) watershed, seg. markers (12 px) & 0.718 & **0.658** & **0.774** & **0.829** & 0.809 & 0.568 & 0.715 & 0.583 & 0.344 \\
 & (b’) watershed, contour markers (25 px) & 0.717 & **0.660** & **0.775** & **0.830** & 0.808 & 0.566 & 0.693 & 0.566 & 0.416 \\
layer, edge target (sec. 10) & WS layer, 20 steps & 0.713 & 0.649 & 0.766 & 0.822 & 0.799 & 0.582 & 0.723 & 0.587 & **0.207** \\
 & converged & **0.721** & 0.655 & 0.773 & **0.829** & **0.810** & 0.569 & **0.724** & **0.588** & 0.214 \\
 & PW limit (307) & 0.637 & 0.612 & 0.718 & 0.763 & 0.746 & 0.625 & 0.682 & 0.562 & 0.334 \\
ground truth & gap mask & 1 & 1 & 1 & 1 & 1 & 0.553 & 0.998 & 0.990 & 0.002 \\
\end{tabular}

\begin{tabular}{cccccccc}
run & output & IoU & `F100.5` & PQ & count err. & components / patch (raw \(\rightarrow\) 8 px) & \\
U-Net, gap target (sec. 6.1) & logits & 0.719 & 0.700 (0.715) & 0.567 (0.581) & 0.220 & 24.0 \(\rightarrow\) 21.7 & \\
U-Net + contour head & logits & **0.724** & 0.723 (0.738) & 0.589 (0.602) & 0.214 & 25.2 \(\rightarrow\) 22.4 & \\
 & (b) watershed, seg. markers & 0.722 & **0.757** (0.774) & **0.618** (0.632) & 0.227 & 27.2 \(\rightarrow\) 24.3 & \\
 & (b’) watershed, contour markers & 0.720 & 0.753 (0.777) & 0.615 (0.636) & 0.241 & 30.3 \(\rightarrow\) 26.0 & \\
layer, edge target (sec. 10) & WS layer, 20 steps & 0.716 & 0.726 (0.733) & 0.589 (0.596) & **0.202** & 22.0 \(\rightarrow\) 21.8 & \\
\end{tabular}

\begin{tabular}{cccccccccccc}
comparison & IoU & BF<sub>1</sub> & \multicolumn{3}{c}{BF<sub>2</sub>} & band acc. & `F100.5` & \multicolumn{3}{c}{PQ} \\
U-Net + contour head, logits - gap U-Net & +0.003 & +0.001, +0.005 & +0.007 & +0.005, +0.009 & +0.005 & +0.003, +0.007 & +0.004 & +0.015 & +0.012, +0.018 & +0.015 & +0.012, +0.017 \\
converged WS layer - U-Net + contour head, logits & +0.001 & +0.001, +0.004 & +0.003 & +0.005, +0.000 & +0.000 & +0.003, +0.003 & +0.001 & +0.002 & +0.039, +0.045 & +0.033 & +0.030, +0.034 \\
converged WS layer - (b) watershed & +0.003 & +0.000, +0.006 & +0.004 & +0.006, +0.001 & +0.001 & +0.003, +0.002 & +0.002 & +0.009 & +0.005, +0.013 & +0.005 & +0.002, +0.008 \\
layer (20 steps) - (b) watershed & -0.005 & +0.007, -0.002 & +0.009 & +0.012, -0.006 & +0.008 & +0.011, -0.005 & +0.010 & +0.008 & +0.004, +0.012 & +0.004 & +0.001, +0.007 \\
after the 8-px filter: layer (20 steps) - U-Net + contour head, logits & & & & & & & & +0.004 & +0.001, +0.006 & +0.001 & +0.001, +0.003 \\
after the 8-px filter: layer (20 steps) - (b) watershed & & & & & & & & -0.031 & +0.034, -0.027 & -0.028 & +0.031, -0.025 \\
\end{tabular}

