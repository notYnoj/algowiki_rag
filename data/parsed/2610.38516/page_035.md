to leave the boundary decision to the WS layer and the learned cost head is a clean contour detector (`examples\_rw\_learned.png`). The 20-step layer is within 0.002 of the converged solve, so K = 20 is enough here.<tbc>

**-** **Deployment at p** \(=\infty\) **works, with a price.** The exact combinatorial PW on the learned costs, which nothing was ever trained with directly, loses 0.03 IoU and 0.03 BF<sub>2</sub> against the converged finite-p solve, and is perfectly binary. That is the train-at-finite-p / deploy-at-the-limit scheme of the note, demonstrated.<tbc>

**-** **The 256**<sup>2</sup> **repeat says the same.** Same recipe at 256 px (`results/ pets256/`):<tbc>

Parity with the plain U-Net on every metric, a 0.19 BF<sub>2</sub> gain of the WS layer over its own logits, and a 0.05 IoU price for the exact limit. Higher resolution did not open a gap; the boundary scores of both methods simply drop because the 1-2 px tolerance is now tighter relative to the trimap’s own boundary band.

## K U-Net with the WS layer as its last layer on real nuclei (PanNuke)

: `experiments/convert\_pannuke.py`, `experiments/exp\_unet\_seg.py` (dataset- agnostic version of `exp\_unet\_pets.py`, reusing its model and loss), `experiments/ seg\_metrics.py`, `experiments/plot\_pannuke.py`. Raw results, per-image metrics and figures: `results/pannuke/`.

**Data.** PanNuke (Gamper et al. 2019/2020), 256<sup>2</sup> H&E patches at 40\(\times\), 19 tissue types, semi-automatic instance labels. Train on fold 1 (2656 patches), test on all of fold 2 (2523 patches; Breast 749, Colon 468, HeadNeck 169, Adrenal 148, ...). Binary target = union of the five nucleus channels (17 % of the pixels; 23.7 nuclei per patch on average; 0.09 % of the pixels sit on an interface between two touching nuclei). Native 256 px, flips and 90\(^\circ\) rotations, otherwise the Pets recipe: small U-Net (32-64-128-256), Adam 1e-3 with cosine decay, 30 epochs, batch 16, p annealed 5 \(\rightarrow\) 50, K = 20 unrolled Jacobi-PCG steps, BCE on the WS layer output + 0.5 BCE on the logits. Training takes 11 s per epoch; evaluating fold 2 takes a few minutes, dominated by the CPU-side metrics.

**Metrics.** Pixel level as before (IoU, boundary F at 1, 2 and 3 px, accuracy in a 3-px band around the true boundary, fraction of pixels in (0.1, 0.9)). Instance level, on the 4-connected components of the thresholded output (4-adjacency is the graph the WS layer works on) against the instance masks: object-count error |n\_pred - n\_gt| / n\_gt, F1 of the matches at IoU \(\ge\) 0.5, panoptic quality PQ and AJI, all aggregated over the whole test set. Because the target is a<tbc>

\begin{tabular}{ccccccc}
variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & soft pixels \\
unet & sigmoid, thresholded at 0.5 & 0.842 & 0.364 & 0.503 & 0.685 & 18.7 % \\
rw\_learned & sigmoid, thresholded at 0.5 & 0.817 & 0.211 & 0.310 & 0.670 & 22.2 % \\
rw\_learned & WS layer, 20 steps & 0.844 & 0.359 & 0.498 & 0.678 & 17.8 % \\
rw\_learned & converged & 0.845 & 0.369 & 0.506 & 0.688 & 19.5 % \\
rw\_learned & PW limit (200) & 0.795 & 0.296 & 0.412 & 0.637 & 0 \\
\end{tabular}

