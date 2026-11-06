<tbc>is not the limit of this layer. Training costs 50 s per epoch against 11 s for the unrolled WS layer.

BCE loss, all of fold 2:

Boundary loss:

(Under the boundary loss every method produces many tiny components, which the instance metrics punish; section 7 has the min-area-filtered numbers.)

- **Same verdict on pixels, better on instances.** The reweighted WS layer matches the unrolled one on IoU and boundary scores and stays 0.01 below the plain thresholded U-Net. Where it differs is the instance side: with two steps it reaches the U-Net’s count error and nearly its F1 and PQ (0.646 / 0.518 against 0.656 / 0.531), well above the unrolled WS layer (0.604 / 0.482), and under the boundary loss it is the best method on all three instance numbers. The full fixed point has the highest edge alignment of anything measured on this dataset (0.628) and the U-Net’s PQ, but loses 0.03 IoU: it commits confidently, including where it is wrong, which is the rigidity of section 8 showing up in the metrics.<tbc>

- **Piecewise constant rather than binary on real images.** Five steps leave 7.7 % soft pixels under BCE and 3.9 % under the boundary loss, against 0.0-0.2 % on the synthetic scenes. The example crops (`figures/examples\_ rw\_learned\_crop.png`; the column titled "layer, 20 steps" is the 2-step layer and "PW limit" the base-cost limit) show what these are: not ramps but plateaus, whole nuclei or clusters sitting at one intermediate grey level. That is the \(\ell\)0-type energy doing exactly what it does on gain graphs: once the edges inside a region are reweighted to agree, the region’s value is set by its unaries as a block, and where those are balanced the block settles at a fraction. More steps or a smaller \(\varepsilon\) push it further along the same trade-off, more edge alignment for less IoU; a final threshold at 0.5 resolves the plateaus one way or the other.<tbc>

**-** **Taken together with sections 6-8:** on PanNuke a thresholded U-Net is a hard baseline that no variant of the WS layer beats at the pixel level, including with a tuned threshold on either side. The WS layer’s measurable contribution is at the instance level, where the reweighted version is the strongest form of it, and in edge alignment, which is label-free. Whether that is worth a layer that costs five times the training time is a question for a task where touching objects matter more than pixel IoU.

\begin{tabular}{ccccccccccc}
output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & soft px & edge align. & `F100.5` & PQ & count err. \\
plain U-Net, thresholded at 0.5 & **0.719** & **0.652** & **0.769** & **0.807** & 15.4 % & 0.577 & **0.656** & **0.531** & 0.275 \\
unrolled WS layer, 20 steps (section 6) & 0.709 & 0.628 & 0.752 & 0.799 & 16.1 % & 0.579 & 0.604 & 0.482 & 0.337 \\
reweighted WS layer, 2 steps (as trained) & 0.708 & 0.641 & 0.759 & 0.801 & 15.5 % & 0.594 & 0.646 & 0.518 & **0.269** \\
reweighted WS layer, 5 steps (fixed point) & 0.682 & 0.632 & 0.743 & 0.776 & 7.7 % & **0.628** & 0.653 & **0.531** & 0.303 \\
\end{tabular}

\begin{tabular}{ccccccccccc}
output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & band acc. & soft px & edge align. & `F100.5` & PQ & count err. \\
plain U-Net, thresholded at 0.5 & **0.718** & **0.669** & **0.787** & **0.819** & 13.2 % & 0.569 & 0.286 & 0.232 & 4.42 \\
unrolled WS layer, 20 steps (section 7) & 0.714 & 0.656 & 0.778 & 0.816 & 13.2 % & 0.571 & 0.263 & 0.213 & 4.78 \\
reweighted WS layer, 2 steps & 0.706 & 0.660 & 0.778 & 0.816 & 13.0 % & 0.590 & **0.364** & **0.295** & **2.98** \\
reweighted WS layer, 5 steps & 0.697 & 0.662 & 0.779 & 0.807 & 3.9 % & **0.603** & 0.317 & 0.258 & 3.58 \\
\end{tabular}

