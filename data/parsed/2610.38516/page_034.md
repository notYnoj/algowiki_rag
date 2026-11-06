- **Truncation** (`truncation.png`, clean, aligned, \(\alpha\) = 0.1): 10 unrolled PCG steps at p = 50 agree with the converged solve on 99.9 % of the labels and reach the full boundary score; Jacobi needs about 50 steps for the same.

## J U-Net with the WS layer as its last layer, trained end to end (Oxford-IIIT Pet)

Binary pet / background from the trimap (border band counted as pet), 128<sup>2</sup>, small U-Net (32-64-128-256), Adam, 30 epochs, batch 16, horizontal flips. Variants:

- `unet`: BCE on the logits.<tbc>

- `rw\_img`: logits \(\rightarrow\) unary costs; edge costs = squared colour differences; the WS layer = 20 unrolled Jacobi-PCG steps in float32, p annealed geometrically from 5 to 50; BCE on the WS layer output plus 0.5 BCE on the logits.<tbc>

**-** `rw\_learned`: as `rw\_img`, but the edge costs come from a second head of the same U-Net (sigmoid, averaged onto the edges).

Test split (3669 images): IoU, boundary F-scores at 1 and 2 px, accuracy within 3 px of the true boundary, fraction of pixels in (0.1, 0.9). Every "thresholded at 0.5" row is the practitioner's pipeline, the network's sigmoid output cut at 0.5 (and, where instance metrics appear, its connected components); it is the baseline every layer row is to be read against. Section 9 adds the tuned-threshold version of it. For the RW variants the output is evaluated as trained (20 steps), converged at p = 50, and as the exact PW limit on 300 images (deployment at p = \(\infty\)).

Figures: `results/pets/figures/` (training curves, example panels with the learned edge costs).

- **Honest outcome at 128**<sup>2</sup>**: no gain over the plain U-Net.** The learned- cost variant matches the U-Net on every metric (0.853 vs 0.853 IoU, 0.724 vs 0.724 BF<sub>2</sub>); the image-gradient variant is worse, and its limit is useless (0.41 IoU): raw colour edges on photographs are not where pet boundaries are. The U-Net trained with BCE for 30 epochs is already nearly binary (13 % soft pixels), so there was little softness to remove at this resolution.<tbc>

**-** **What the WS layer does do.** Inside the trained model the WS layer adds about 0.085 BF<sub>2</sub> over its own logits (0.638 \(\rightarrow\) 0.722): the network learned<tbc>

\begin{tabular}{ccccccc}
variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & soft pixels \\
unet & sigmoid, thresholded at 0.5 & 0.853 & 0.586 & 0.724 & 0.778 & 13.4 % \\
rw\_img & sigmoid, thresholded at 0.5 & 0.838 & 0.500 & 0.633 & 0.768 & 12.6 % \\
rw\_img & WS layer, 20 steps & 0.840 & 0.508 & 0.681 & 0.742 & 18.0 % \\
rw\_img & converged & 0.842 & 0.508 & 0.681 & 0.749 & 18.9 % \\
rw\_img & PW limit (300) & 0.405 & 0.134 & 0.260 & 0.510 & 0.2 % \\
rw\_learned & sigmoid, thresholded at 0.5 & 0.840 & 0.498 & 0.638 & 0.765 & 15.2 % \\
rw\_learned & WS layer, 20 steps & 0.852 & 0.584 & 0.722 & 0.771 & 14.2 % \\
rw\_learned & converged & 0.853 & 0.586 & 0.724 & 0.775 & 14.9 % \\
rw\_learned & PW limit (300) & 0.822 & 0.561 & 0.695 & 0.749 & 0 \\
\end{tabular}

