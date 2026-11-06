<tbc>decimals on every metric (row 2). This is largely built in: the foreground, hence the IoU and the number of objects, is held fixed, so the two can only differ in how they split touching nuclei, and at _p_=20 they split them the same way. At test time, then, the WS layer differs from the baseline through its foreground (which pixels the background label wins) and its markers, not through the split itself. Second, the WS layer’s markers in the baseline’s watershed and foreground (row 3) lose 0.015 F<sub>1</sub> and 0.011 PQ against the WS layer and gain 0.006 AJI: the baseline’s watershed turns the WS layer’s extra, spurious markers into objects, which the WS layer’s solve partly absorbs. Third, the baseline’s markers in the WS layer’s solve (row 5) do poorly (F<sub>1</sub> 0.705), because the solve was trained with the WS layer’s own denser markers and gives every nucleus without a marker to the background; the two halves of each method are tuned to each other.

### E Data efficiency

The multi-marker WS layer (trained from its own predicted markers, unmarked nuclei sent to the background) and the post-processing baseline (U-Net with a distance head and a marker watershed, tuned on fold 3) were trained on nested random subsets of fold 1 of 10, 25 and 50% (subset seed 0), with the number of epochs scaled so that every run makes the same number of gradient steps as the 30-epoch run on the full fold, and evaluated on all 2523 patches of fold 2 (Fig. 6). The last column gives the paired difference, layer minus baseline, with 95% bootstrap intervals.

The WS layer degrades more gracefully only at 10%: it loses 0.030 F<sub>1</sub> and 0.029 PQ with respect to the full fold where the baseline loses 0.049 and 0.049, and it leads on every metric; the margin is 2.5 times the seed spread of the layer<tbc>

\begin{tabular}{ccccccccc}
markers & final step & IoU & F<sub>1</sub>@0.5 & PQ & SQ & AJI & count err. \\
WS layer’s & WS layer’s solve & 0.715 & 0.795 & 0.649 & 0.816 & 0.668 & 0.182 \\
WS layer’s & watershed of the WS layer’s contour map, in its foreground & 0.715 & 0.795 & 0.649 & 0.816 & 0.668 & 0.182 \\
WS layer’s & baseline’s watershed of _c-d_ in {_s\>_0.5} & 0.726 & 0.780 & 0.638 & 0.818 & 0.674 & 0.203 \\
baseline’s & baseline’s watershed of _c-d_ in {_s\>_0.5} & 0.719 & 0.794 & 0.655 & 0.824 & 0.658 & 0.190 \\
baseline’s & WS layer’s solve & 0.620 & 0.705 & 0.576 & 0.817 & 0.597 & 0.291 \\
\end{tabular}

\begin{tabular}{ccccccccc}
training set & WS layer & \multicolumn{2}{c}{U-Net + dist. head + watershed} & U-Net + components & \multicolumn{2}{c}{layer - baseline, F<sub>1</sub> / PQ} & \\
10% (266) & 0.765 / 0.620 / 0.635 & 0.745 / 0.605 / 0.620 & 0.622 / 0.500 & +0.020 \[+0.017, +0.023\] / +0.015 \[+0.013, +0.017\] & \\
25% (664) & 0.785 / 0.640 / 0.659 & 0.789 / 0.646 / 0.662 & 0.653 / 0.530 & -0.004 \[-0.007, -0.001\] / -0.006 \[-0.008, -0.004\] & \\
50% (1328) & 0.787 / 0.641 / 0.663 & 0.794 / 0.653 / 0.666 & 0.659 / 0.536 & -0.007 \[-0.009, -0.004\] / -0.012 \[-0.014, -0.010\] & \\
100% (2656) & 0.795 / 0.649 / 0.668 & 0.794 / 0.655 / 0.658 & 0.664 / 0.539 & +0.001 \[-0.002, +0.004\] / -0.005 \[-0.007, -0.003\] & \\
\end{tabular}

** 5.** Markers \(\times\) final step on fold 2 (2523 patches). Rows 1 and 4 are the two methods of  3; row 2 replaces the WS layer’s solve by a plain marker watershed inside the WS layer’s own output foreground; row 3 uses the WS layer’s markers in the baseline’s watershed and foreground.

** 6.** Training-set size against F<sub>1</sub>@0.5 / PQ / AJI on fold 2.

