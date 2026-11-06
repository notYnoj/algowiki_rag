### O The two untried leads: an edge target on the cost head, and a Dice-band boundary loss

1 and 9). : `--w-edge`, `--edge-pos`, `--edge-seam` and `--loss boundary\_dice` in `experiments/exp\_unet\_seg.py`, `experiments/run\_leads.sh`; tables and statistics with `compare\_losses.py`, `seam\_stats.py` and `inst\_minarea.py`. Raw results, per-image metrics and figures: `results/pannuke/leads/{dice,edge\_bce,edge\_dice,edge\_gap\_p10}/`.

Of the three leads section 7 listed, the lower-p / cost-scale one was run in section 6.1 (p \(2\rightarrow 10\) with \(8\cdot\sigma\) edges is the best finite-p configuration, but the WS layer still blurs the seams half shut and its limit is lost). The two others:

**-** **Edge target on the cost head** (`--w-edge 1`). Section 6.1 ended on "supervising the cost head directly with the seam mask". Every grid edge whose two pixels carry different instance ids is a positive: nucleus / background boundaries (3 % of the edges) and the seams between touching nuclei (0.1 %), the latter weighted \(\times 5\) on top of the \(\times 10\) of all positives. BCE on the edge probability \(\sigma\)(h) averaged onto the edge (the cost divided by its scale), added with weight 1 to the segmentation loss. Three runs: binary target at p \(5\rightarrow 50\) with BCE (`edge\_bce`) and with the Dice-band loss (`edge\_dice`), and the gap target at p \(2\rightarrow 10\) with the \(8\cdot\sigma\) learnable-scale edges of section 6.1 (`edge\_gap\_p10`), to be read against that section's run without the target.<tbc>

**-** **Dice-band boundary loss** (`--loss boundary\_dice`, `dice/`). The band- weighted BCE of section 7’s boundary loss (\(\times 5\) within 3 px of the true boundary) plus 1 - soft Dice restricted to that band, instead of the boundary- F surrogate: it pays for filling the band correctly, and a dotted contour earns nothing. Both variants, binary target, p \(5\rightarrow 50\), so the comparison with section 7 is one-for-one.

**Results on all of fold 2** (2523 patches; the PW limit on the same 307 patches as before). Binary target, p \(5\rightarrow 50\), except the last block (gap target, p \(2\rightarrow 10\), \(8\cdot\sigma\) learnable-scale edges), whose comparison rows are section 6.1’s. Instance metrics on the raw 4-connected components; the min-area-filtered numbers follow.

**Instance metrics after removing components smaller than 8 px** (same filter as section 7, `results/pannuke/leads/minarea.json`):

\begin{tabular}{ccccccccccccccccc}
target, p & loss / cost head & variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & soft px & edge align. & `F100.5` & PQ & count err. \\
binary, \(5\rightarrow 50\) & bce (sec. 6) & unet & logits & 0.719 & 0.652 & 0.769 & 0.825 & 0.807 & 15.4 % & 0.577 & 0.656 & 0.531 & 0.275 \\
 & bce (sec. 6) & rw\_learned & WS layer, 20 steps & 0.709 & 0.628 & 0.752 & 0.813 & 0.799 & 16.1 % & 0.579 & 0.604 & 0.482 & 0.337 \\
 & bce (sec. 6) & rw\_learned & PW limit (307) & 0.661 & 0.591 & 0.711 & 0.788 & 0.771 & 0 & 0.577 & 0.618 & 0.498 & 0.246 \\
 & boundary\_dice & unet & logits & 0.697 & 0.632 & 0.737 & 0.786 & 0.836 & 14.2 % & 0.555 & 0.612 & 0.498 & 0.876 \\
 & boundary\_dice & rw\_learned & WS layer, 20 steps & 0.693 & 0.621 & 0.728 & 0.778 & 0.831 & 13.6 % & 0.546 & 0.595 & 0.482 & 0.878 \\
 & boundary\_dice & rw\_learned & converged & 0.690 & 0.621 & 0.728 & 0.778 & 0.833 & 14.3 % & 0.544 & 0.601 & 0.486 & 0.818 \\
 & boundary\_dice & rw\_learned & PW limit (307) & 0.658 & 0.591 & 0.695 & 0.748 & 0.815 & 0 & 0.518 & 0.633 & 0.502 & 0.487 \\
 & bce + edge target & rw\_learned & WS layer, 20 steps & 0.703 & 0.630 & 0.752 & 0.813 & 0.792 & 14.1 % & 0.554 & 0.446 & 0.355 & 1.25 \\
 & bce + edge target & rw\_learned & converged & 0.707 & 0.635 & 0.754 & 0.814 & 0.797 & 14.1 % & 0.558 & 0.435 & 0.347 & 1.11 \\
 & bce + edge target & rw\_learned & PW limit (307) & 0.684 & 0.624 & 0.744 & 0.802 & 0.783 & 0 & 0.569 & 0.501 & 0.395 & 0.489 \\
 & boundary\_dice + edge target & rw\_learned & WS layer, 20 steps & 0.690 & 0.608 & 0.715 & 0.767 & 0.830 & 13.9 % & 0.525 & 0.505 & 0.408 & 1.56 \\
 & boundary\_dice + edge target & rw\_learned & PW limit (307) & 0.646 & 0.553 & 0.662 & 0.721 & 0.807 & 0 & 0.495 & 0.428 & 0.339 & 1.40 \\
gap, \(2\rightarrow 10\), \(8\cdot\sigma\) & bce (sec. 6.1) & unet & logits & 0.717 & 0.651 & 0.768 & 0.825 & 0.806 & 15.5 % & 0.575 & 0.667 & 0.541 & 0.296 \\
 & bce (sec. 6.1) & rw\_learned & WS layer, 20 steps & 0.712 & 0.639 & 0.759 & 0.819 & 0.796 & 14.5 % & 0.585 & 0.678 & 0.548 & 0.225 \\
 & bce (sec. 6.1) & rw\_learned & converged & 0.716 & 0.639 & 0.760 & 0.820 & 0.801 & 14.8 % & 0.575 & 0.680 & 0.549 & 0.226 \\
 & bce (sec. 6.1) & rw\_learned & PW limit (307) & 0.508 & 0.496 & 0.582 & 0.620 & 0.671 & 0 & 0.669 & 0.523 & 0.435 & 0.555 \\
 & bce + edge target & rw\_learned & WS layer, 20 steps & 0.713 & 0.649 & 0.766 & 0.822 & 0.799 & 12.5 % & 0.582 & **0.723** & **0.587** & **0.207** \\
 & bce + edge target & rw\_learned & converged & **0.721** & **0.655** & **0.773** & **0.829** & **0.810** & 13.2 % & 0.569 & **0.724** & **0.588** & 0.214 \\
 & bce + edge target & rw\_learned & PW limit (307) & 0.637 & 0.612 & 0.718 & 0.763 & 0.746 & 0 & 0.625 & 0.682 & 0.562 & 0.334 \\
 & ground truth & binary / gap mask & 1 & 1 & 1 & 1 & 1 & 0 & 0.559 & 0.913 / 0.998 & 0.883 / 0.990 & 0.088 / 0.002 \\
\end{tabular}

