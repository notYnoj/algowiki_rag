**– **The fixed point is rigid.** At the fixed point the losing unary of every pixel is down-weighted by \(\varepsilon^2\), so each pixel is locked to its label and the output’s sensitivity to the edge costs collapses onto 70-140 edges on the noisy scene, against 4000 for the annealed solution of the same quality; on the clean scene the two are comparable (1300 vs 1200-4000). This is the self-reinforcing nature of the scheme, the same thing that makes it sharp, and it is the price of losing the temperature: for training, the gradient should be taken after one or two reweighting steps or with a larger \(\varepsilon\), i.e. at finite temperature again, with the fully converged fixed point used only at deployment. Note that the ground-truth loss gradient is not the right measure here: it shrinks whenever the output is right.<tbc>

**– **Same failure mode, gentler.** With the image edge off the true boundary, the fixed point from p<sub>0</sub> = 10 degrades gracefully (0.87-0.89 against 0.96) because it sharpens the soft prediction rather than snapping to an edge; from \(p_0\ge 50\) it snaps like annealing does. The limit object also changes: the fixed point is a local minimiser of a nonconvex piecewise-constant energy, not the unique Power Watershed, and it has no quasi-linear combinatorial evaluation; deployment is a few linear solves.

### N PanNuke: the reweighted WS layer, and the thresholded U-Net done properly

Two additions to the PanNuke comparison of sections 6 and 7.

**The practitioner’s baseline with a tuned threshold.** Every "thresholded at 0.5" row above is what most practitioners deploy. The stronger form of the same baseline sweeps the threshold (`experiments/threshold\_sweep.py`, all of fold 2, results in `results/pannuke/threshold\_sweep\_*.json`):

Tuning the cut is worth 0.003 IoU at most; the 0.5 baseline is already the best case of that pipeline, and the same holds for the boundary-loss U-Net (best IoU at 0.5, best BF<sub>2</sub> at 0.6) and for the unrolled WS layer’s own output (best at 0.4, +0.002). The sweep also shows, in passing, what the WS layer does for the learned-cost model: its raw logits fall apart into 240-520 components per patch at any threshold, and the WS layer brings that back to 24, the true count.

**The reweighted WS layer trained end to end** (`--layer reweighted` in `experiments/exp\_unet\_seg.py`; results `results/pannuke\_reweighted/{bce,boundary}/`). Same recipe as section 6, but the WS layer is an implicit solve at the annealed base weights exp(-p c), p from 5 to 50, followed by two Cauchy reweighting steps (\(\varepsilon=0.1\), unaries included) during training, five at evaluation ("fixed point"). The "limit" row is not reported: the exact Power Watershed of the base costs

\begin{tabular}{cccccccc}
plain U-Net (BCE), threshold & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & instance F1 & PQ \\
0.3 & 0.711 & 0.633 & 0.753 & 0.815 & 0.601 & 0.483 \\
0.4 & 0.722 & 0.654 & 0.770 & 0.816 & 0.635 & 0.513 \\
0.5 & 0.719 & 0.652 & 0.769 & 0.807 & 0.656 & 0.531 \\
0.6 & 0.702 & 0.626 & 0.753 & 0.788 & 0.662 & 0.541 \\
0.7 & 0.666 & 0.569 & 0.712 & 0.755 & 0.648 & 0.525 \\
\end{tabular}

