<tbc>and was reproduced on a second GPU to 0.001. The gain is in detection, not in boundaries (equal segmentation quality): the baseline’s tuning on fold 3 raises its marker threshold and leaves 24.5% of the nuclei without a marker, whereas the layer keeps a low threshold and its solve, trained on its own markers, absorbs the spurious ones. From 25% on, the baseline is ahead again by 0.004-0.007 F<sub>1</sub> and 0.006-0.012 PQ, as with the full fold.

The 10% point was replicated for both methods with a second seed on the same subset and with a second random draw of 266 images ( 7). The margin is stable, \(0.017\pm 0.003\) F<sub>1</sub> and \(0.013\pm 0.002\) PQ, with the WS layer at F<sub>1</sub> 0.765 in every run, and the mechanism is the same in each replicate: the baseline leaves about 24% of the nuclei unmarked, the WS layer 14-16%, at equal segmentation quality. The larger fractions were run once. One caveat remains: the baseline at 10% over-fits mildly under the fixed number of steps, and early stopping could recover part of the margin.

## F Cost and accuracy of the two differentiation modes

This section supports the efficiency statements of Sect. 3. All timings are medians of seven runs after two warm-up runs on one NVIDIA A100 (40GB, PyTorch<tbc>

image
foreground prob. s
distance map d
markers (shared procedure)
relief / edge costs
final partition
ground truth
U-Net + watched (baseline) patch 1307
U-Net + WS layer patch 1307
U-Net + watched (baseline) patch 2442
U-Net + WS layer patch 2442

**Fig.5.** The two instance pipelines step by step on two fold-2 patches (112-px crops around touching nuclei). For each patch, the baseline (upper row) and the WS layer (lower row): the image, the foreground probability _s_, the distance map _d_, the markers extracted from _d_ by the shared procedure (each model with its own tuned parameters), the baseline’s relief _c-d_ and the WS layer’s learned edge costs, the final partition, and the ground truth.

