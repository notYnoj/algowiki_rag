<tbc>truth averages 24; its output has 24), but a standalone U-Net trained with BCE for 30 epochs learns a similar sharpening by itself. Boundary- and seam-weighted losses, a gap target between touching nuclei, lower annealing ranges and an edge target on the cost head \[1, §L, O\] move these metrics by a few thousandths, with one exception: the edge target, a cross-entropy of the cost maps against the instance boundaries, brings the converged WS layer level with the thresholded U-Net on IoU (paired difference +0.002, 95% bootstrap interval \[-0.000,+0.005\]) and gives the best raw instance scores of the table. Training in the implicit mode, with the true RW gradient (Sect. 3), matters more: on both seeds every paired interval against the unrolled mode is clear of zero (F<sub>1</sub> +0.035 and +0.055), and the layer is level with the U-Net on IoU and BF<sub>2</sub>, 0.007-0.012 behind on F<sub>1</sub> and PQ; the exact limit of these costs is worse (IoU 0.60; Appendix F).

Finally, a U-Net given the same edge supervision through a contour channel, with a marker watershed run on that map afterwards, is level with the edge-target WS layer at the pixel level (last two rows); on raw instance scores the layer is slightly ahead, and after an 8-px minimum-area filter the watershed is.

## 4.4 Real images with labeled instances

The binary WS layer essentially discards the property that makes the PW distinctive. We now let each image carry its own label set, one marker per nucleus plus background, and let the WS layer compute the partition among them (Sect. 3): the U-Net predicts a foreground logit, the edge costs and a marker map; the loss is a per-pixel cross-entropy over this image’s markers against the instance mask, with _p_ annealed from 5 to 20. Each marker region _k_ attaches its pixels to label _k_ with _a<sup>k</sup>=s<sup>p</sup>_ and the background label attaches every pixel with (1-_s)<sup>p</sup>_. The loss is differentiable in the edge costs and the attachments, not in the choice of markers: extraction is a discrete step inside the network, run in training as at test time, and the marker map learns from its own regression loss only. Training markers are first the eroded ground-truth instances. Test markers come from a distance-to-boundary head that regresses, for every nucleus pixel, its normalised distance to the nucleus boundary as in Naylor et al. \[28\]. From<tbc>

\begin{tabular}{ccccccc}
output & IoU & BF<sub>2</sub> & edge al. & F<sub>1</sub>@0.5 & PQ & count err. \\
U-Net, thresholded & 0.719 & 0.769 & 0.577 & 0.656 & 0.531 & 0.275 \\
U-Net + WS layer, image-gradient costs & 0.683 & 0.714 & 0.559 & 0.516 & 0.400 & 0.513 \\
its exact limit & 0.174 & 0.251 & 0.804 & 0.209 & 0.163 & 0.676 \\
U-Net + WS layer, learned costs & 0.709 & 0.752 & 0.579 & 0.604 & 0.482 & 0.337 \\
its exact limit & 0.660 & 0.714 & 0.583 & 0.643 & 0.512 & 0.253 \\
trained in the implicit mode (mean of two seeds) & 0.717 & 0.772 & 0.599 & 0.647 & 0.521 & 0.253 \\
U-Net + WS layer, learned costs with edge target, converged & **0.721** & 0.773 & 0.569 & **0.724** & **0.588** & **0.214** \\
U-Net + contour head, marker watershed & 0.718 & **0.774** & 0.568 & 0.715 & 0.583 & 0.344 \\
\end{tabular}

** 2.** PanNuke fold 2, binary nucleus segmentation. "Thresholded" is the network’s sigmoid output cut at 0.5, with instances as connected components; a threshold sweep moves its IoU by at most 0.003. 95% bootstrap half-widths over the 2523 patches are 0.005-0.010 for IoU, BF<sub>2</sub>, edge alignment, F<sub>1</sub> and PQ, and 0.01-0.05 for the count error.

