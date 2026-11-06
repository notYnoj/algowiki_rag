### 5.3 Novel View Synthesis

We compare PointGT for novel view synthesis to PAPR \[31\], Texture-GS \[27\], GSTex \[16\], NeST-Splatting \[30\], and Textured Gaussians \[3\] on the Blender \[13\] dataset and the DTU dataset \[5,9\].  2 shows quantitative results for novel view synthesis on the Blender and DTU datasets. We compare against baselines in two settings: (1) the original settings reported in prior works (no cap on the number of primitives), and (2) capping all methods at 5,000 primitives. As shown in  2, our method outperforms baselines in both settings.

### 5.4 Ablation Study

#### Evaluation of the Geometry Regularizers

We ablate the two regularizers described in Sec. 4.1.

#### On-ray regularizer.

Figure 6 shows the ablation of the on-ray loss (close-to-ray). We visualize the predicted surface points from a camera view, the same points in

\begin{tabular}{ccccccccc}
 & \multicolumn{4}{c}{**DTU** \[9\]} & \multicolumn{4}{c}{**NeRF Synthetic** \[13\]} \\
Method & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & # Pts & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & # Pts \\
\multicolumn{9}{c}{_Authors’ recommended primitive counts_} \\
Texture-GS \[27\] & 30.53 & 0.920 & 0.083 & 90k & 28.97 & 0.938 & 0.055 & 90k \\
GSTex \[16\] & 32.87 & 0.956 & 0.038 & 186k & 33.25 & 0.969 & 0.024 & 100k \\
Textured-Gaussian \[3\] & 33.61 & 0.970 & 0.056 & 240k & 33.24 & 0.967 & 0.043 & 190k \\
NeST Splatting \[30\] & **33.65** & 0.964 & 0.042 & 80k & 33.37 & 0.967 & 0.032 & 73k \\
PAPR \[31\] & 29.34 & 0.952 & 0.073 & 30k & 32.07 & 0.971 & 0.038 & 30k \\
Ours & 33.48 & **0.973** & **0.023** & 30k & **33.57** & **0.982** & **0.021** & 30k \\
\multicolumn{9}{c}{_Fixed primitive count (5k)_} \\
Texture-GS \[27\] & 26.81 & 0.833 & 0.206 & 5k & 19.29 & 0.795 & 0.213 & 5k \\
GSTex \[16\] & 28.92 & 0.932 & 0.072 & 5k & 30.20 & 0.897 & 0.149 & 5k \\
Textured-Gaussian \[3\] & 29.58 & 0.912 & 0.080 & 5k & 26.21 & 0.919 & 0.086 & 5k \\
NeST Splatting \[30\] & 32.68 & 0.966 & 0.056 & 5k & 30.48 & 0.958 & 0.057 & 5k \\
PAPR \[31\] & 24.87 & 0.846 & 0.040 & 5k & 30.38 & 0.963 & 0.048 & 5k \\
Ours & **33.25** & **0.970** & **0.024** & 5k & **31.01** & **0.976** & **0.039** & 5k \\
\end{tabular}

GSTex [16]
Ours
# Primitives = 1k
# Primitives = 5k
# Primitives = 60k

**Fig.5:** Texture editing compared with GSTex \[16\] with different number of primitives.

** 2:** Quantitative comparison of Novel-view Synthesis.

