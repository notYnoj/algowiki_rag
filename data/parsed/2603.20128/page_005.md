<tbc>**Global Feature Extractor** (G<sub>**CNN**</sub>, Eqn. 9)**.** Global context is captured using a lightweight CNN with three convolutional layers (\[64, 64, 32\] channels), \(3\times 3\) kernels, and ReLU activations. An adaptive average pooling layer produces a 32-dimensional global feature vector.

**Two-Stage Fusion Network** (G<sub>**fuse**</sub>, Eqn. 10)**.** The fusion module first combines hierarchical features and camera embeddings via a four-layer MLP (64 neurons, Tanh activations). The intermediate fused representation is then merged with global LR features in a second four-layer MLP of the same configuration. Both stages use intermediate embeddings of size 32 for efficient integration of local and global information. For clarity and completeness, additional implementation details are provided in the supplementary materials.

## 4.2 . Comparison Experiments

**Benchmarks and Protocol.** We evaluate our approach on three widely used datasets for novel view synthesis (NVS) and super-resolution. **Blender**\[25\]: 8 synthetic scenes with diverse shapes and materials. We train on the training sets<tbc>

<tbc>and evaluate on the held-out, unseen test sets of all eight scenes. Input images are downsampled to \(100\times 100\) and \(200\times 200\), and results are reported for SR scales of \(\times 2\) and \(\times 4\). **LLFF**\[24\]: eight forward-facing real-world scenes. Following NeRF-SR \[33\], we train on the entire dataset due to the limited number of images per scene. Evaluation is conducted on SR novel views synthesized by different NeRF backbones. **DTU** \[15\]: a multi-view stereo benchmark with 124 indoor scenes captured under seven lighting conditions. We use 88 training scenes with \(128\times 128\) LR inputs and \(\times 4\) SR, and evaluate on 8 held-out DTU test set. **Metrics.** We employ standard metrics, including Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) \[40\], to comprehensively assess pixel accuracy, structural fidelity, and perceptual quality of SR results. For methods without SR, their outputs are bicubically upsampled to match target resolution. We also report _LR+Ours_ (downsampled HR ground-truth as LR input, super-resolved with ours) to indicate the attainable upper bound of our framework.

\begin{tabular}{ccccccccccccc}
\multirow{2}{*}{Methods} & \multicolumn{3}{c}{Blender\(\times 2\) (\(100\times 100\))} & \multicolumn{3}{c}{Blender\(\times 4\) (\(100\times 100\))} & \multicolumn{3}{c}{Blender\(\times 2\) (\(200\times 200\))} & \multicolumn{3}{c}{Blender\(\times 4\) (\(200\times 200\))} \\
 & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) \\
TensoRF \[4\] & 25.41 & 0.882 & 0.161 & 24.06 & 0.843 & 0.188 & 27.27 & 0.909 & 0.199 & 26.18 & 0.882 & 0.146 \\
Instant-NGP \[26\] & 26.34 & 0.916 & 0.157 & 24.83 & 0.872 & 0.229 & 28.29 & 0.934 & 0.109 & 27.07 & 0.904 & 0.159 \\
3DGS \[16\] & 27.57 & 0.935 & 0.124 & 25.59 & 0.887 & 0.213 & 29.49 & 0.949 & 0.087 & 27.86 & 0.916 & 0.147 \\
LR+Bicubic & 28.20 & **0.946** & 0.099 & 25.99 & <u>0.896</u> & 0.192 & 30.53 & <u>0.962</u> & 0.066 & 28.60 & <u>0.927</u> & 0.128 \\
NeRF-SR \[33\] & 28.74 & 0.924 & 0.066 & <u>28.07</u> & **0.921** & <u>0.071</u> & 30.82 & 0.953 & 0.055 & 28.46 & 0.921 & 0.076 \\
FastSR-NeRF \[19\] & 27.27 & 0.902 & 0.142 & 22.32 & 0.453 & 0.475 & 31.42 & 0.952 & 0.047 & **30.47** & **0.944** & 0.075 \\
SuperGaussian \[30\] & 26.39 & 0.915 & 0.090 & - & - & - & 29.91 & 0.947 & <u>0.035</u> & 28.44 & 0.923 & <u>0.067</u> \\
S2Gaussian \[32\] & - & - & - & - & - & - & - & - & - & - & 24.19 & 0.879 & 0.089 \\
TensoRF+Ours & 26.61 & 0.908 & 0.093 & 23.52 & 0.863 & 0.119 & 28.28 & 0.921 & 0.068 & 26.10 & 0.891 & 0.103 \\
Instant-NGP+Ours & 29.25 & <u>0.945</u> & 0.062 & 25.13 & 0.888 & 0.098 & 31.02 & 0.952 & 0.041 & 27.17 & 0.892 & 0.085 \\
3DGS+Ours & **29.43** & **0.946** & <u>0.051</u> & 25.80 & 0.893 & 0.085 & <u>32.17</u> & 0.940 & 0.041 & 27.14 & 0.892 & 0.076 \\
LR+Ours & <u>29.34</u> & 0.938 & **0.049** & **28.77** & **0.921** & **0.069** & **33.68** & **0.971** & **0.027** & <u>29.31</u> & 0.923 & **0.055** \\
\end{tabular}

\begin{tabular}{ccccccccccccc}
\multirow{2}{*}{Methods} & \multicolumn{3}{c}{LLFF\(\times 2\) (\(100\times 100\))} & \multicolumn{3}{c}{LLFF\(\times 4\) (\(100\times 100\))} & \multicolumn{3}{c}{LLFF\(\times 2\) (\(200\times 200\))} & \multicolumn{3}{c}{LLFF\(\times 4\) (\(200\times 200\))} \\
 & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) \\
TensoRF \[4\] & 24.07 & 0.754 & 0.314 & 22.16 & 0.591 & 0.596 & 24.69 & 0.750 & 0.309 & 23.49 & 0.648 & 0.503 \\
Instant-NGP \[26\] & 22.17 & 0.667 & 0.335 & 20.90 & 0.543 & 0.479 & 21.47 & 0.616 & 0.332 & 20.81 & 0.571 & 0.428 \\
3DGS \[16\] & 23.20 & 0.735 & 0.307 & 21.52 & 0.581 & 0.580 & 23.76 & 0.748 & 0.294 & 22.73 & 0.654 & 0.478 \\
LR+Bicubic & 24.56 & 0.765 & 0.299 & 22.62 & 0.608 & 0.579 & 25.92 & 0.793 & 0.260 & 24.43 & 0.687 & 0.468 \\
NeRF-SR \[33\] & 26.24 & 0.838 & <u>0.123</u> & 24.07 & 0.713 & 0.252 & <u>27.15</u> & 0.837 & <u>0.122</u> & 25.44 & 0.745 & 0.208 \\
FastSR-NeRF \[19\] & 24.33 & 0.765 & 0.297 & 21.20 & 0.584 & 0.473 & 26.21 & 0.822 & 0.241 & 21.30 & 0.384 & 0.475 \\
3DSR \[5\] & 26.38 & <u>0.886</u> & 0.181 & 24.18 & <u>0.760</u> & 0.342 & 24.90 & <u>0.838</u> & 0.235 & <u>25.88</u> & <u>0.809</u> & 0.261 \\
S2Gaussian \[32\] & - & - & - & - & - & - & - & - & - & 20.45 & 0.654 & <u>0.139</u> \\
TensoRF+Ours & <u>26.46</u> & 0.805 & 0.181 & <u>25.34</u> & 0.751 & 0.190 & 27.07 & 0.809 & 0.170 & 24.49 & 0.718 & 0.213 \\
Instant-NGP+Ours & 23.31 & 0.719 & 0.171 & 22.30 & 0.689 & 0.206 & 21.74 & 0.646 & 0.155 & 20.92 & 0.588 & 0.264 \\
3DGS+Ours & 26.11 & 0.805 & 0.168 & 25.07 & 0.754 & <u>0.183</u> & 26.87 & 0.828 & 0.149 & 25.42 & 0.749 & 0.176 \\
LR+Ours & **30.32** & **0.892** & **0.072** & **29.29** & **0.847** & **0.112** & **32.90** & **0.934** & **0.040** & **29.61** & **0.874** & **0.074** \\
\end{tabular}

1. Comparison of SOTAs on Blender datasets with varying resolutions and scaling factors. The best results are highlighted in bold, and the second-best results are underlined.

2. Comparison of SOTAs on LLFF datasets with varying resolutions and scaling factors. The best results are highlighted in bold, and the second-best results are underlined.

