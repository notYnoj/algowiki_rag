<tbc>**Oxford-IIIT Pet, 128 px, boundary loss** (3669 test images; limit on 300; the `bce` rows are section 3’s runs, which did not compute BF<sub>3</sub>):

Paired, rw\_learned layer - unet under the boundary loss: IoU +0.000 \[-0.001, +0.002\], BF<sub>2</sub> +0.007 \[+0.005, +0.009\] (layer better on 55 % of the images); PW limit - unet on the 300 limit images: IoU -0.013 \[-0.020, -0.005\], BF<sub>2</sub> +0.008 \[-0.000, +0.017\].

Figures: `results/pannuke\_losses/losses.png` (the first table as a dot chart), `results/pets\_losses/losses.png`, and per loss the training curves and the example panels of section 6 (`results/pannuke\_losses/\<loss\>/figures/`).

- **Honest outcome: neither loss opened a gap in the WS layer’s favour on PanNuke.** The boundary loss narrowed it, from -0.009 to -0.005 IoU and from -0.017 to -0.009 BF<sub>2</sub> (both intervals still exclude zero; the WS layer wins on 43 % of the patches instead of 25 %), because it helped the WS layer model more than the U-Net (+0.026 vs +0.018 BF<sub>2</sub>, +0.017 vs +0.011 band accuracy). The instance loss widened it to -0.019 IoU. The U-Net stays the better nucleus segmenter under all three losses, on every tolerance and on the instance metrics, raw or filtered.<tbc>

**-** **The boundary loss does what it should, for both models.** +0.018 BF<sub>2</sub> and +0.011 band accuracy for the U-Net at unchanged IoU, +0.026 / +0.017 for the WS layer; the outputs are sharper (13 % soft pixels against 15-16 %). Its one pathology is worth recording: the soft boundary-F surrogate, which measures boundaries by a 1-px morphological gradient inside pooled tolerance regions, is satisfied as cheaply by a dotted line as by a solid one, and both models learned to sprinkle isolated pixels along the outer side of every contour (`boundary/figures/examples\_unet\_crop.png`). The raw instance numbers therefore collapse (91 components per patch, F1 0.29), but the dots are 1-4 px and a minimum-area filter of 8 px removes them, after which the boundary-trained U-Net is the best instance segmenter of the whole study<tbc>

\begin{tabular}{ccccccccc}
comparison & loss & IoU & \multicolumn{4}{c}{BF<sub>2</sub>} & band acc. & WS layer better on \\
rw\_learned layer - unet & bce & -0.009 \[-0.012, -0.007\] & -0.017 & \[-0.020, -0.014\] & -0.008 & 25 % / 19 % & & \\
rw\_learned layer - unet & boundary & -0.005 \[-0.007, -0.003\] & -0.009 & \[-0.011, -0.007\] & -0.003 & 43 % / 31 % & & \\
rw\_learned layer - unet & instance & -0.019 \[-0.022, -0.017\] & -0.025 & \[-0.028, -0.023\] & -0.015 & 18 % / 16 % & & \\
unet, loss - bce & boundary & -0.000 \[-0.003, +0.002\] & +0.018 & \[+0.015, +0.021\] & +0.011 & & & \\
unet, loss - bce & instance & -0.000 \[-0.002, +0.002\] & +0.000 & \[-0.001, +0.002\] & -0.001 & & & \\
rw\_learned layer, loss - bce & boundary & +0.004 \[+0.001, +0.007\] & +0.026 & \[+0.022, +0.029\] & +0.017 & & & \\
rw\_learned layer, loss - bce & instance & -0.010 \[-0.012, -0.008\] & -0.008 & \[-0.010, -0.006\] & -0.007 & & & \\
PW limit - converged (307) & boundary & -0.034 \[-0.040, -0.029\] & -0.013 & \[-0.016, -0.010\] & -0.033 & & & \\
PW limit - converged (307) & instance & -0.108 \[-0.122, -0.095\] & -0.076 & \[-0.088, -0.064\] & -0.065 & & & \\
\end{tabular}

\begin{tabular}{ccccccccc}
loss & variant & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & soft px \\
bce & unet & sigmoid, thresholded at 0.5 & 0.853 & 0.586 & 0.724 & - & 0.778 & 13.4 % \\
bce & rw\_learned & WS layer, 20 steps & 0.852 & 0.584 & 0.722 & - & 0.771 & 14.2 % \\
bce & rw\_learned & converged & 0.853 & 0.586 & 0.724 & - & 0.775 & 14.9 % \\
bce & rw\_learned & PW limit (300) & 0.822 & 0.561 & 0.695 & - & 0.749 & 0 \\
boundary & unet & sigmoid, thresholded at 0.5 & 0.864 & 0.629 & 0.769 & 0.837 & 0.787 & 7.6 % \\
boundary & rw\_learned & sigmoid, thresholded at 0.5 & 0.859 & 0.613 & 0.756 & 0.829 & 0.786 & 11.3 % \\
boundary & rw\_learned & WS layer, 20 steps & 0.864 & 0.634 & 0.776 & 0.844 & 0.787 & 9.1 % \\
boundary & rw\_learned & converged & **0.867** & **0.643** & **0.782** & **0.848** & **0.793** & 9.3 % \\
boundary & rw\_learned & PW limit (300) & 0.851 & 0.634 & 0.776 & 0.843 & 0.778 & 0 \\
\end{tabular}

