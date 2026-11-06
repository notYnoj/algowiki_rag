\begin{tabular}{cccc}
Scene & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
\multicolumn{4}{c}{_M360 Outdoor (5M, 25k iters, per-ray)_} \\
garden & 28.06 & 0.875 & 0.108 \\
bicycle & 25.53 & 0.782 & 0.203 \\
stump & 27.10 & 0.797 & 0.206 \\
treehill & 23.09 & 0.652 & 0.298 \\
flowers & 22.08 & 0.642 & 0.304 \\
\multicolumn{4}{c}{_M360 Indoor (2M, 45k iters, center ray)_} \\
bonsai & 35.09 & 0.957 & 0.222 \\
counter & 30.83 & 0.925 & 0.220 \\
kitchen & 33.40 & 0.940 & 0.138 \\
room & 33.43 & 0.936 & 0.250 \\
\multicolumn{4}{c}{_Tanks \& Temples (2.5M, 40k iters, center ray)_} \\
truck & 26.91 & 0.900 & 0.112 \\
train & 24.45 & 0.865 & 0.169 \\
\multicolumn{4}{c}{_Deep Blending (2M, 30k iters, center ray)_} \\
drjohnson & 30.43 & 0.918 & 0.309 \\
playroom & 31.45 & 0.921 & 0.296 \\
M360 Outdoor Avg & 25.17 & 0.749 & 0.224 \\
M360 Indoor Avg & 33.19 & 0.940 & 0.207 \\
**M360 Total** & **28.74** & **0.834** & **0.216** \\
**T\&T Avg** & **25.68** & **0.882** & **0.141** \\
**DB Avg** & **30.94** & **0.919** & **0.302** \\
\end{tabular}

\begin{tabular}{ccccccc}
Dim & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & LSEG<sub>P</sub>\(\uparrow\) & LSEG<sub>C</sub>\(\uparrow\) & FPS\(\uparrow\) \\
4 & 23.81 & 0.853 & 0.254 & 44.33 & 0.988 & 76 \\
8 & 25.40 & 0.876 & 0.200 & 47.10 & 0.994 & 75 \\
16 & 26.06 & 0.885 & 0.178 & 48.23 & 0.995 & 72 \\
32 & 26.34 & 0.887 & 0.166 & 48.68 & 0.996 & 72 \\
64 & 26.42 & 0.887 & 0.163 & 48.79 & 0.996 & 70 \\
\end{tabular}

** 7:** Per-scene results of NHT (Ours) with split training configurations on MipNeRF360 \[2\], Tanks & Temples \[30\], and Deep Blending \[21\]. We adapt primitive count and training length per dataset to accommodate different dataset sizes and spatial scales, but keep the same learning rates and other hyperparameters. Indoor datasets benefit from encoding the central camera ray, instead of per-ray directions, due to their high parallax, acting as a regularization on ray orientation. Trained and evaluated on the original JPEG-compressed reference images.

** 8:** Feature dimensionality ablation for joint RGB + LSEG reconstruction on the _truck_ scene (Tanks & Temples). LSEG<sub>P</sub> and LSEG<sub>C</sub> denote PSNR and cosine similarity of the 512-dim semantic features, respectively. Measured on an RTX A6000 Ada.

