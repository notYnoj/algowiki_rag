<tbc>**Results on all of fold 2** (2523 patches; the PW limit on the same 307 patches as section 6). The first rows are section 6's runs. Instance metrics on the raw 4-connected components of the thresholded output.

Paired per-patch differences (2523 patches, bootstrap 95 % intervals), layer minus the U-Net trained on the same gap target: p 5 \(\rightarrow\) 50: IoU -0.012 \[-0.015, -0.009\], BF<sub>2</sub> -0.021; p 5 \(\rightarrow\) 20: -0.010, -0.021; p 5 \(\rightarrow\) 20 sharp: -0.011, -0.021; **p 2** \(\rightarrow\) **10 sharp: IoU** **-0.005 \[-0.007, -0.002\], BF**<sub>2</sub> **-0.009 \[-0.012, -0.007\]**, better than the U-Net on 33 % of the patches, and +0.007 IoU on the 486 patches with fewer than 10 nuclei (-0.010 on the 179 with more than 50). On HeadNeck (169 patches) the p 2 \(\rightarrow\) 10 layer is above the U-Net on every metric (IoU 0.697 vs 0.670, BF<sub>2</sub> 0.765 vs 0.741, F1 0.671 vs 0.649, PQ 0.547 vs 0.528). Limit minus converged on the 307 patches: -0.037 IoU at p = 50, -0.23 at p = 20, -0.20 at p = 10. The learnable edge scale went _down_, from 8 to 3.4 (p 5 \(\rightarrow\) 20) and 4.1 (p 2 \(\rightarrow\) 10), within the first six epochs and stayed there (`figures/training.png`; the dotted p axis there shows the 5 \(\rightarrow\) 50 schedule only).

**Does anything cut the seams? seam\_stats.json**: fraction of the 142 211 seam pixels of fold 2 predicted as background, and fraction of the 8999 seams (components of the touch mask) entirely background. U-Net, binary target: 15.1 % / 10.6 %; U-Net, gap target: 19.1 % / 13.0 %. Layer, gap target: 16.8 % / 11.9 % at p = 50, 18.5 % at p = 20, 19.9 % / 13.6 % at p = 10 with sharp edges. In every run the WS layer output cuts _fewer_ seam pixels than its own logits do (25-31 % for the logits), and the converged solve fewer still (11-18 %); at best the WS layer matches the U-Net. The crops (`figures/examples\_rw\_p10\_ sharp\_crop.png`, `examples\_unet\_gap\_crop.png`) show the same thing: at p 2 \(\rightarrow\) 10 the network's own logits are now a recognisable nucleus detector with dark seams (54 components per patch instead of 340 at p = 50), the WS layer blurs those seams half shut, and the exact limit floods whole crops into one component or none.

**-** **Honest outcome: the three changes together close half of the pixel- level gap and make the WS layer the best raw instance segmenter, but the WS layer still does not cut, and it still does not beat the U-Net.** The gap target on its own changes little (U-Net: F1 0.656 \(\rightarrow\) 0.667, seam pixels cut 15 \(\rightarrow\) 19 %; the WS layer at p 5 \(\rightarrow\) 50 is slightly _worse_ than under the binary target, -0.005 IoU paired). Lower p at the old parametrisation changes nothing at the pixel level. Only the lowest schedule<tbc>

\begin{tabular}{ccccccccccccc}
target & run & output & IoU & BF<sub>1</sub> & BF<sub>2</sub> & BF<sub>3</sub> & band acc. & soft px & `F100.5` & PQ & count err. \\
binary & unet (sec. 6) & sigmoid, thresholded at 0.5 & **0.719** & **0.652** & **0.769** & **0.825** & **0.807** & 15.4 % & 0.656 & 0.531 & 0.275 \\
binary & rw\_learned, p 5 \(\rightarrow\) 50 (sec. 6) & WS layer, 20 steps & 0.709 & 0.628 & 0.752 & 0.813 & 0.799 & 16.1 % & 0.604 & 0.482 & 0.337 \\
binary & rw\_learned, p 5 \(\rightarrow\) 50 (sec. 6) & PW limit (307) & 0.661 & 0.591 & 0.711 & 0.768 & 0.771 & 0 & 0.618 & 0.490 & 0.246 \\
gap & unet & sigmoid, thresholded at 0.5 & 0.717 & 0.651 & 0.768 & 0.825 & 0.806 & 15.5 % & 0.667 & 0.541 & 0.296 \\
gap & rw\_learned, p 5 \(\rightarrow\) 50 & WS layer, 20 steps & 0.705 & 0.624 & 0.747 & 0.809 & 0.797 & 16.4 % & 0.610 & 0.487 & 0.357 \\
gap & rw\_learned, p 5 \(\rightarrow\) 50 & PW limit (307) & 0.664 & 0.587 & 0.710 & 0.768 & 0.770 & 0 & 0.621 & 0.490 & 0.246 \\
gap & rw\_learned, p 5 \(\rightarrow\) 50 & WS layer, 20 steps & 0.707 & 0.625 & 0.748 & 0.810 & 0.797 & 15.8 % & 0.635 & 0.508 & 0.313 \\
gap & rw\_learned, p 5 \(\rightarrow\) 20 & PW limit (307) & 0.476 & 0.482 & 0.562 & 0.597 & 0.669 & 0 & 0.510 & 0.417 & 0.510 \\
gap & rw\_learned, p 5 \(\rightarrow\) 20, 8-\(\sigma\) edges & WS layer, 20 steps & 0.706 & 0.624 & 0.747 & 0.810 & 0.795 & 16.1 % & 0.625 & 0.499 & 0.295 \\
gap & rw\_learned, p 5 \(\rightarrow\) 20, 8-\(\sigma\) edges & PW limit (307) & 0.435 & 0.446 & 0.522 & 0.555 & 0.641 & 0 & 0.474 & 0.390 & 0.567 \\
gap & rw\_learned, p 2 \(\rightarrow\) 10, 8-\(\sigma\) edges & WS layer, 20 steps & 0.712 & 0.639 & 0.759 & 0.819 & 0.796 & 14.5 % & **0.678** & **0.548** & **0.225** \\
gap & rw\_learned, p 2 \(\rightarrow\) 10, 8-\(\sigma\) edges & converged & 0.716 & 0.639 & 0.760 & 0.820 & 0.801 & 14.8 % & **0.680** & **0.549** & 0.226 \\
gap & rw\_learned, p 2 \(\rightarrow\) 10, 8-\(\sigma\) edges & PW limit (307) & 0.508 & 0.496 & 0.582 & 0.620 & 0.671 & 0 & 0.523 & 0.435 & 0.555 \\
gap & ground truth & gap mask & 1 & 1 & 1 & 1 & 1 & 0 & 0.998 & 0.990 & 0.002 \\
\end{tabular}

