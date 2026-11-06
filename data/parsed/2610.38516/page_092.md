<tbc>scorers from the other changes of section 14 (the permissive candidates and the primary rule for duplicates). : `--ds-score head|mlp|none` in `experiments/ exp\_instance\_pannuke.py` (`scorer\_strengths`, `candidate\_features`, `unit\_ strengths`, `scorer\_selftest`), the cases `dist\_dsh`, `dist\_dsm`, `dist\_dsn` of `ruche\_run.sh`, and `candidate\_auc.py`, which now also ranks by the strength channel and the scorer. Results: `results/pannuke\_instances/{dist\_dsh, dist\_dsm, dist\_dsn}/`, `compare\_16.md`.

**The three runs.** All three keep section 14’s recipe otherwise: candidates at thr 0.1 / h 0.1 / area 1 from epoch 10 (all images from 15), primary-overlap target for duplicates, unmarked nuclei to the background label, the strength entering as a\_k = (\(\sigma\)\_k s)^p, p 5 \(\rightarrow\) 20, 30 epochs, seed 0, fold 1 \(\rightarrow\) fold 2. Fold 3 chooses thr \(\in\{0.05,0.1,0.2\}\times\) h \(\in\{0.1,0.2\}\) (area 1) and \(\tau\in\{0,0.3,0.5,0.7,0.9\}\).

- `dist\_dsh` (`--ds-score head`): a fifth U-Net output channel g; \(\sigma\)\_k = sigmoid((mean of g over the candidate \(-\theta\)) / T). The distance channel gets no gradient from the solve; the shared trunk does, through g.<tbc>

- `dist\_dsm` (`--ds-score mlp`, the design proposed by the main session): a two-layer MLP (9 \(\rightarrow\) 32 \(\rightarrow\) 1, its own parameters only, output bias initialised at +4 so that \(\sigma\approx 0.98\) at the start) on nine features computed from the detached distance map d, foreground s and contour map c. The features: peak of d, relative prominence (peak - saddle) / peak, log area, mean s, mean c, whether the candidate has an adjacent candidate, and for the least-separated adjacent candidate the mean and maximum of c along the shared boundary and the relative depth of the d valley between the two peaks. log \(\sigma\)\_k = -softplus(-logit). No gradient from the strengths reaches the U-Net at all; the scorer learns only from the partition cross-entropy through the solve.<tbc>

**-** `dist\_dsn` (`--ds-score none`): every strength 1. Same candidates, same targets, no selection: the control.

**Checks.** The scorer’s gradient against central finite differences (`--ds-selftest --ds-score mlp`, the case of section 14 with the candidates’ real features from random maps, a test scorer with 8 hidden units and output bias 0.5): worst relative error 1.1e-8 over four random directions in its 89 parameters and on the output bias (`dist\_dsm/ds\_selftest\_mlp.txt`). The wiring check, on eight fold-1 patches, backpropagates the solve’s loss alone. With `head`, the distance channel’s output weights get a gradient of exactly 0 and the strength channel’s 0.19; with section 14’s scoring the distance channel gets 0.22. The sanity check proposed for the run itself, that the distance head stays at the 11.5 level, holds: its final MSE is 0.0085 (`head`), 0.0083 (`mlp`), 0.0082 (control) against 0.0082 for `dist\_sched10\_bg` and 0.0219 for section 14’s `dist\_ds`.

**Results on fold 2** (all 2523 patches; `compare\_16.md`):

\begin{tabular}{ccccccccccccc}
run & `F180.5` & PQ & SQ & DQ & AJI & IoU & count err. & markers one / none / several, bg per patch & oracle F1 / PQ & limit F1 / PQ (307) \\
`dist\_sched10\_bg` (11.5) & **0.795** & 0.649 & 0.816 & **0.795** & **0.668** & 0.715 & **0.182** & 85.5 / 12.7 / 1.8 %, 4.3 & 0.872 / 0.723 & 0.700 / 0.564 \\
`uns\_dist` (11.2) & 0.794 & **0.655** & **0.824** & 0.794 & 0.658 & **0.719** & 0.190 & 76.6 / 21.8 / 1.6 %, 1.6 & 0.867 / 0.708 & - & - \\
`dist\_dsh`: strength channel & 0.782 & 0.638 & 0.816 & 0.782 & 0.656 & 0.701 & 0.188 & 85.0 / 13.3 / 1.7 %, 4.1 & 0.917 / 0.751 & 0.099 / 0.082 \\
`dist\_dsm`: detached MLP scorer & 0.790 & 0.643 & 0.814 & 0.790 & 0.666 & 0.712 & 0.183 & 87.4 / 10.5 / 2.1 %, 6.4 & 0.927 / 0.758 & 0.157 / 0.128 \\
`dist\_dsn`: control, strengths 1 & 0.790 & 0.646 & 0.817 & 0.790 & 0.663 & 0.713 & **0.176** & 86.2 / 12.5 / 1.3 %, 4.8 & 0.856 / 0.704 & 0.611 / 0.502 \\
\end{tabular}

