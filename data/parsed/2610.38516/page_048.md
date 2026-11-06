<tbc>(IoU in this table is against the binary mask for every row.)

**Seam statistics** (`seam\_stats.json`, `limit\_seams.json`): fraction of the 142 211 seam pixels of fold 2 predicted as background / fraction of the 8999 seams entirely background; the limit on its 307 patches, with the other outputs on the same patches in brackets for comparison.

**Paired per-patch differences** (2523 patches, bootstrap 95 % intervals):

Per tissue, converged edge-target solve against the gap U-Net (IoU / BF<sub>2</sub> / F1 / PQ): Breast (749) 0.722 / 0.757 / 0.753 / 0.600 vs 0.720 / 0.755 / 0.704 / 0.560; Colon (468) 0.697 / 0.739 / 0.614 / 0.483 vs 0.693 / 0.737 / 0.562 / 0.444; HeadNeck (169) 0.702 / 0.777 / 0.725 / 0.590 vs 0.670 / 0.741 / 0.649 / 0.528; Adrenal (148) 0.724 / 0.785 / 0.778 / 0.654 vs 0.716 / 0.774 / 0.692 / 0.580. The converged solve has the higher IoU on 9 of the 15 tissue types with \(\ge\) 50 patches and the higher F1 on all of them. By crowding: +0.012 IoU on patches with fewer than 10 nuclei, +0.002 on all other bins; count error 0.50 vs 0.77 (\< 10 nuclei), 0.14 vs 0.20 (10-30), equal above 30.

Figures: `results/pannuke/leads/edge\_gap\_p10/figures/examples\_rw\_learned\_ crop.png` (the edge target makes the cost head a closed contour map, last column; the seams are in it), `edge\_bce/figures/examples\_rw\_learned\_crop.png` (the same at p = 50: the logits are now pure checkerboard and the 20-step layer shows horizontal streaks where the PCG has not converged inside closed contours; the exact limit separates the nuclei), `dice/figures/examples\_unet\_crop.png` (no dotted contours, but a softer output), `edge\_gap\_p10/cmp/losses.png`, `losses.png`.

**-** **Honest outcome: the edge target is the missing piece, and with it the WS layer beats the U-Net on PanNuke for the first time, by**<tbc>

\begin{tabular}{cccccccccc}
target, p & loss / cost head & variant & output & IoU & `F1@0.5` & PQ & count err. & components / patch (raw \(\rightarrow\) filtered) \\
binary, 5 \(\rightarrow\) 50 & bce (sec. 7) & unet & logits & 0.720 & 0.683 & 0.552 & 0.224 & 23.0 \(\rightarrow\) 21.2 \\
 & boundary (sec. 7) & unet & logits 0.725 & 0.714 & 0.582 & 0.236 & 90.8 \(\rightarrow\) 22.1 \\
 & boundary\_dice & unet & logits & 0.702 & 0.653 & 0.532 & 0.596 & 31.3 \(\rightarrow\) 27.7 \\
 & bce (sec. 7) & rw\_learned & WS layer & 0.711 & 0.633 & 0.505 & 0.268 & 23.8 \(\rightarrow\) 21.6 \\
 & boundary\_dice & rw\_learned & WS layer & 0.694 & 0.627 & 0.508 & 0.682 & 31.8 \(\rightarrow\) 28.9 \\
 & boundary\_dice & rw\_learned & PW limit (307) & 0.658 & 0.633 & 0.502 & 0.487 & 26.8 \(\rightarrow\) 26.8 \\
 & bce + edge target & rw\_learned & WS layer & 0.705 & 0.641 & 0.510 & 0.255 & 42.4 \(\rightarrow\) 22.3 \\
 & bce + edge target & rw\_learned & PW limit (307) & 0.684 & 0.575 & 0.454 & 0.304 & 30.2 \(\rightarrow\) 23.0 \\
 & boundary\_dice + edge target & rw\_learned & WS layer & 0.695 & 0.615 & 0.497 & 0.689 & 41.2 \(\rightarrow\) 29.5 \\
gap, 2 \(\rightarrow\) 10, 8\(\sigma\) & bce (sec. 6.1) & unet & logits & 0.719 & 0.700 & 0.567 & 0.220 & 24.0 \(\rightarrow\) 21.7 \\
 & bce (sec. 6.1) & rw\_learned & WS layer & 0.714 & 0.686 & 0.555 & 0.218 & 21.5 \(\rightarrow\) 21.0 \\
 & bce + edge target & rw\_learned & WS layer & 0.716 & **0.726** & **0.589** & **0.202** & 22.0 \(\rightarrow\) 21.8 \\
 & bce + edge target & rw\_learned & PW limit (307) & 0.638 & 0.682 & 0.562 & 0.334 & 16.1 \(\rightarrow\) 16.1 \\
\end{tabular}

\begin{tabular}{cccccccccc}
target, p & run & logits & WS layer, 20 steps & converged & PW limit (307) & \[logits / layer / converged on the same 307\] & & & \\
binary, 5 \(\rightarrow\) 50 & bce (sec. 6), unet & 15 % / 11 % & & & & & & & \\
 & bce (sec. 6), rw\_learned & 20 % / 11 % & 15 % / 11 % & 9 % / 8 % & 25 % / 17 % \[23 / 19 / 11 %\] & & & & \\
 & bce + edge target & 28 % / 3 % & 21 % / 10 % & 14 % / 6 % & 23 % / 9 % \[30 / 24 / 15 %\] & & & & \\
 & boundary\_dice, unet & 13 % / 8 % & & & & & & & \\
 & boundary\_dice, rw\_learned & 20 % / 11 % & 15 % / 9 % & 13 % / 8 % & & & & & \\
gap, 2 \(\rightarrow\) 10, 8\(\sigma\) & bce, unet (sec. 6.1) & 19 % / 13 % & & & & & & & \\
 & bce (sec. 6.1), rw\_learned & 32 % / 19 % & 20 % / 14 % & 18 % / 12 % & 57 % / 48 % \[31 / 22 / 20 %\] & & & & \\
 & bce + edge target & 42 % / 26 % & 29 % / 19 % & 23 % / 15 % & **52 % / 34 %** \[43 / 34 / 24 %\] & & & \\
\end{tabular}

\begin{tabular}{cccccccccc}
comparison & IoU & BF<sub>1</sub> & BF<sub>2</sub> & & band acc. & & first better on & & \\
gap target, p 2 \(\rightarrow\) 10, 8\(\sigma\), edge target: converged - gap U-Net & +0.004 \[+0.002,+0.007\] & +0.004 \[+0.002,+0.007\] & +0.005 \[+0.003,+0.008\] & +0.004 \[+0.004,+0.005\] & 50 % / 54 % & & & & \\
same: layer (20 steps) - gap U-Net & -0.003 \[-0.006,-0.001\] & -0.001 \[-0.004,+0.001\] & -0.002 \[-0.005,+0.000\] & -0.007 & & 36 % / 42 % & & & \\
same: converged, with - without the edge target (sec. 6.1) & +0.005 \[-0.003,+0.007\] & +0.016 \[+0.013,+0.018\] & +0.013 \[+0.011,+0.016\] & +0.009 & 58 % / 69 % & & & & \\
same: PW limit - converged (307) & -0.078 \[-0.091,-0.065\] & & -0.047 \[-0.058,-0.036\] & -0.058 & & 14 % & & & \\
binary, 5 \(\rightarrow\) 50, bce + edge target: layer - U-Net (bce) & -0.015 \[-0.018,-0.013\] & & -0.017 \[-0.020,-0.015\] & -0.015 & & 19 % / 23 % & & & \\
same: PW limit - converged (307) & -0.016 \[-0.020,-0.013\] & & +0.002 \[-0.002,+0.006\] & -0.008 & & 16 % / 44 % & & & \\
same: PW limit - U-Net (bce) (307) & -0.030 \[-0.039,-0.023\] & & -0.020 \[-0.028,-0.012\] & -0.019 & & 14 % / 27 % & & & \\
binary, boundary\_dice: layer - U-Net (same loss) & -0.005 \[-0.007,-0.002\] & & -0.009 \[-0.012,-0.007\] & -0.005 & & 28 % / 24 % & & & \\
binary, boundary\_dice: U-Net, dice - bce & -0.021 \[-0.026,-0.016\] & & -0.032 \[-0.037,-0.026\] & +0.028 \[+0.027,+0.030\] & 40 % / 35 % & & & & \\
\end{tabular}

