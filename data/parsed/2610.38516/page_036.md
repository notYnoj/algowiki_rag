<tbc>binary mask, touching nuclei merge for every method; the row "ground truth / binary mask" (components of the true binary mask against the instances) is the ceiling any binary method can reach on these metrics. Label-free edge alignment: fraction of predicted boundary pixels within 1 px of a strong image edge (top 10 % of the colour-gradient magnitude after a \(\sigma=1\) px Gaussian). The same score for the ground-truth boundary calibrates it. The exact PW limit (\(\mathrm{p}=\infty\)) is computed on 307 patches: 300 evenly spaced through fold 2 plus the 8 patches with the most touching-nuclei pixels, which also serve as the example panels.

**A note on the limit’s cost.** With float32 costs quantised to 2<sup>-20</sup>, a 256<sup>2</sup> patch has about 200 000 plateaus of which 40 000 have 2-7 tied edges; the general plateau path of `power\_watershed` (sparse graph + connected components per plateau) made the exact limit cost 50-60 s per patch. A pure-Python route for plateaus of \(\le\) 64 edges, with the same semantics (checked bit-identical), brings it to 2 s per patch.

**Results on all of fold 2** (2523 patches; the PW limit on 307). Instance metrics on 4-connected components of the thresholded output; "count err." = mean |n\_pred - n\_gt| / n\_gt.

(The AJI of the raw logits is inflated by their hundreds of tiny components, which AJI only counts in the denominator by area; F1, PQ and the count error are the honest instance numbers.)

**Per tissue type** (the three most common in fold 2; `figures/summary.md` has the full tables, `rw\_learned.json` all 15 types with \(\ge\) 50 patches):

Paired per-patch differences (2523 patches, bootstrap 95 % intervals), `rw\_ learned` layer minus `unet`: IoU -0.009 \[-0.012, -0.007\], BF<sub>2</sub> -0.017 \[-0.020, -0.014\], band accuracy -0.008; the WS layer is better than the U-Net on 25 % of the patches. The gap grows with crowding: -0.004 IoU on patches with fewer than 10 nuclei, -0.016 on patches with more than 50. Within the trained<tbc>

\begin{tabular}{ccccccccccccc}
variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & soft px & edge align. & `F100.5` & PQ & AJI & count err. \\
unet & sigmoid, thresholded at 0.5 & **0.719** & **0.652** & **0.769** & **0.825** & **0.807** & 15.4 % & 0.577 & **0.656** & **0.531** & **0.494** & 0.275 \\
rw\_img & sigmoid, thresholded at 0.5 & 0.669 & 0.547 & 0.672 & 0.737 & 0.806 & 13.2 % & 0.481 & 0.303 & 0.240 & 0.529 & 5.01 \\
rw\_img & WS layer, 20 steps & 0.683 & 0.571 & 0.714 & 0.794 & 0.775 & 19.9 % & 0.559 & 0.516 & 0.400 & 0.396 & 0.513 \\
rw\_img & converged & 0.686 & 0.570 & 0.713 & 0.794 & 0.779 & 20.3 % & 0.548 & 0.531 & 0.411 & 0.336 & 0.441 \\
rw\_img & PW limit (307) & 0.181 & 0.217 & 0.254 & 0.273 & 0.540 & 0 & 0.796 & 0.194 & 0.150 & 0.109 & 0.675 \\
rw\_learned & sigmoid, thresholded at 0.5 & 0.674 & 0.560 & 0.684 & 0.749 & 0.800 & 17.7 % & 0.481 & 0.083 & 0.067 & 0.533 & 25.4 \\
rw\_learned & WS layer, 20 steps & 0.709 & 0.628 & 0.752 & 0.813 & 0.799 & 16.1 % & 0.579 & 0.604 & 0.482 & 0.456 & 0.337 \\
rw\_learned & converged & 0.710 & 0.630 & 0.751 & 0.812 & 0.805 & 16.2 % & 0.572 & 0.602 & 0.480 & 0.366 & 0.322 \\
rw\_learned & PW limit (307) & 0.661 & 0.591 & 0.711 & 0.768 & 0.771 & 0 & 0.577 & 0.618 & 0.490 & 0.425 & **0.246** \\
ground truth & binary mask & 1 & 1 & 1 & 1 & 1 & 0 & 0.559 & 0.913 & 0.883 & 0.701 & 0.088 \\
\end{tabular}

\begin{tabular}{ccccccccc}
tissue (n) & variant / output & IoU & BF<sub>2</sub> & edge align. & `F100.5` & PQ & count err. \\
Breast (749) & unet / logits & 0.722 & 0.756 & 0.585 & 0.690 & 0.547 & 0.198 \\
 & rw\_learned / layer & 0.713 & 0.738 & 0.589 & 0.635 & 0.498 & 0.313 \\
 & rw\_learned / PW limit (89) & 0.667 & 0.703 & 0.586 & 0.684 & 0.535 & 0.174 \\
 & ground truth / binary & 1 & 1 & 0.553 & 0.933 & 0.907 & 0.072 \\
Colon (468) & unet / logits & 0.698 & 0.738 & 0.558 & 0.547 & 0.431 & 0.274 \\
 & rw\_learned / layer & 0.681 & 0.711 & 0.565 & 0.495 & 0.384 & 0.319 \\
 & rw\_learned / PW limit (62) & 0.610 & 0.658 & 0.534 & 0.463 & 0.353 & 0.283 \\
 & ground truth / binary & 1 & 1 & 0.539 & 0.836 & 0.796 & 0.123 \\
HeadNeck (169) & unet / logits & 0.672 & 0.744 & 0.648 & 0.640 & 0.519 & 0.424 \\
 & rw\_learned / layer & **0.693** & **0.758** & 0.635 & 0.593 & 0.475 & 0.309 \\
 & ground truth / binary & 1 & 1 & 0.629 & 0.927 & 0.897 & 0.061 \\
\end{tabular}

