# The Power Watershed as a Differentiable Layer

41<tbc>

**-** **Boundary loss.** Per-pixel BCE with the pixels within 3 px of the true boundary weighted \(\times 5\) (band = max-pool minus min-pool of the target with a 7\(\times\)7 window), plus a differentiable boundary-F surrogate at a 2-px tolerance (Bokhovkin & Burnaev 2019: soft boundaries as the inner morphological gradient x - minpool<sub>3</sub>(x), precision and recall through max-pooled tolerance regions, loss = 1-2PR/(P+R)), weight 1.<tbc>

**-** **Instance loss (PanNuke only).** The 2-px seam between touching nuclei (pixels with a 4-neighbour in a different instance, 0.09 % of the pixels) is set to _background_ in the target, and the seam plus a 1-px flank is weighted \(\times 21\) in the BCE. This is the "target that leaves the interface pixels as background" of section 6: separating touching nuclei is now rewarded, where the binary union target punished it. Test metrics are still computed against the original binary mask and the instance masks.

**Results on all of fold 2** (2523 patches; the PW limit on the same 307 patches as section 6). The `bce` rows are section 6’s runs. Instance metrics on the raw 4-connected components, as before; see the next table for what they become after a minimum-area filter.

The raw logits of the `rw\_learned` models are in `results/pannuke\_losses/ summary.md`; as in section 6 they are speckle that the WS layer cleans up (215-387 components per patch).

**Instance metrics after removing components smaller than 8 px** (`experiments/inst\_minarea.py`, `results/pannuke\_losses/minarea.json`; 8 px is 1.5 % of the mean nucleus area, the filter is the same for every row; the raw rows above are min-area 1):

**Paired per-patch differences** (2523 patches, bootstrap 95 % intervals; `results/pannuke\_losses/summary.md` has the full list):

\begin{tabular}{cccccccccccccc}
loss & variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & soft px & edge align. & `F100.5` & PQ & count err. \\
bce & unet & sigmoid, thresholded at 0.5 & 0.719 & 0.652 & 0.769 & 0.825 & 0.807 & 15.4 % & 0.577 & 0.656 & 0.531 & 0.275 \\
bce & rw\_learned & WS layer, 20 steps & 0.709 & 0.628 & 0.752 & 0.813 & 0.799 & 16.1 % & 0.579 & 0.604 & 0.482 & 0.337 \\
bce & rw\_learned & converged & 0.710 & 0.630 & 0.751 & 0.812 & 0.805 & 16.2 % & 0.572 & 0.602 & 0.480 & 0.322 \\
bce & rw\_learned & PW limit (307) & 0.661 & 0.591 & 0.711 & 0.768 & 0.771 & 0 & 0.577 & 0.618 & 0.490 & 0.246 \\
boundary & unet & sigmoid, thresholded at 0.5 & **0.718** & **0.669** & **0.787** & **0.841** & **0.819** & 13.2 % & 0.569 & 0.286 & 0.232 & 4.42 \\
boundary & rw\_learned & WS layer, 20 steps & 0.714 & 0.656 & 0.778 & 0.835 & 0.816 & 13.2 % & 0.571 & 0.263 & 0.213 & 4.78 \\
boundary & rw\_learned & converged & 0.715 & 0.657 & 0.778 & 0.834 & 0.819 & 13.2 % & 0.566 & 0.285 & 0.231 & 4.23 \\
boundary & rw\_learned & PW limit (307) & 0.673 & 0.626 & 0.755 & 0.821 & 0.782 & 0 & 0.559 & 0.140 & 0.111 & 8.78 \\
instance & unet & sigmoid, thresholded at 0.5 & **0.719** & 0.651 & 0.769 & 0.827 & 0.807 & 17.0 % & 0.569 & **0.663** & **0.538** & 0.315 \\
instance & rw\_learned & WS layer, 20 steps & 0.699 & 0.617 & 0.744 & 0.807 & 0.791 & 18.3 % & 0.581 & 0.594 & 0.470 & 0.321 \\
instance & rw\_learned & converged & 0.701 & 0.619 & 0.742 & 0.804 & 0.799 & 17.8 % & 0.577 & 0.574 & 0.455 & 0.339 \\
instance & rw\_learned & PW limit (307) & 0.592 & 0.539 & 0.659 & 0.715 & 0.729 & 0 & 0.589 & 0.593 & 0.465 & 0.312 \\
ground truth & binary mask & & 1 & 1 & 1 & 1 & 1 & 0 & 0.559 & 0.913 & 0.883 & 0.088 \\
\end{tabular}

\begin{tabular}{cccccccccc}
loss & variant & output & IoU & `F100.5` & PQ & count err. & components / patch (raw \(\rightarrow\) filtered) & & \\
bce & unet & sigmoid, thresholded at 0.5 & 0.720 & 0.683 & 0.552 & 0.224 & 23.0 \(\rightarrow\) 21.2 & & \\
bce & rw\_learned & WS layer & 0.711 & 0.633 & 0.505 & 0.268 & 23.8 \(\rightarrow\) 21.6 & & \\
bce & rw\_learned & PW limit (307) & 0.661 & 0.618 & 0.490 & 0.246 & 20.8 \(\rightarrow\) 20.8 & & \\
boundary & unet & sigmoid, thresholded at 0.5 & 0.725 & **0.714** & **0.582** & 0.236 & 90.8 \(\rightarrow\) 22.1 & & \\
boundary & rw\_learned & WS layer & 0.722 & 0.682 & 0.553 & 0.252 & 93.5 \(\rightarrow\) 21.5 & & \\
boundary & rw\_learned & PW limit (307) & 0.684 & 0.598 & 0.475 & 0.275 & 160.7 \(\rightarrow\) 18.5 & & \\
instance & unet & sigmoid, thresholded at 0.5 & 0.719 & 0.696 & 0.565 & 0.226 & 24.1 \(\rightarrow\) 21.8 & & \\
instance & rw\_learned & WS layer & 0.701 & 0.617 & 0.488 & 0.278 & 22.4 \(\rightarrow\) 20.6 & & \\
instance & rw\_learned & PW limit (307) & 0.592 & 0.593 & 0.465 & 0.312 & 19.8 \(\rightarrow\) 19.8 & & \\
\end{tabular}

