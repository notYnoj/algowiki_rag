<tbc>adapts to the different scene scale and dataset sizes of outdoor and indoor datasets.

### Effect of reference image format.

As noted in Tab. 1, MipNeRF360 images are distributed as pre-downscaled, re-compressed JPEG files. The default _gsplat_ pipeline downscales and converts these to lossless PNGs before training and evaluation, which removes JPEG compression artifacts from the ground truth. In Tab. 5 we compare NHT results under both protocols. Training and evaluating directly on the original JPEG references yields slightly lower PSNR (-0.28dB), SSIM (-0.011), and higher LPIPS (+0.014) on average, as JPEG compression artifacts in the ground truth lower the effective quality ceiling.

### 1.1 Semantic Reconstruction

#### Semantic Reconstruction Details

For our semantic reconstruction task, following a similar setup to Feature 3DGS \[82\], we train a joint RGB and LSEG semantic

\begin{tabular}{ccccccccccccc}
 & \multicolumn{4}{c}{BBSplat} & \multicolumn{4}{c}{NHT (equal primitives)} & \multicolumn{4}{c}{NHT (∼ equal memory)} \\
Cap & PSNR\(\uparrow\) & LPIPS\(\downarrow\) & MB\(\downarrow\) & FPS\(\uparrow\) & PSNR\(\uparrow\) & LPIPS\(\downarrow\) & MB\(\downarrow\) & FPS\(\uparrow\) & PSNR\(\uparrow\) & LPIPS\(\downarrow\) & MB\(\downarrow\) & FPS\(\uparrow\) \\
15K & 24.35 & 0.416 & 13.2 & 86.9 & 24.54 & 0.448 & **2.5** & 222.2 & **26.29** & **0.358** & 9.0 & **245.4** \\
30K & 24.95 & 0.362 & 25.6 & 64.3 & 25.49 & 0.403 & **5.0** & **214.5** & **27.03** & **0.318** & 18.1 & 192.5 \\
60K & 26.10 & 0.294 & 50.2 & 55.0 & 26.40 & 0.358 & **9.9** & **211.3** & **27.64** & **0.283** & 36.3 & 165.4 \\
160K & 26.85 & 0.264 & 124.6 & 33.2 & 27.39 & 0.302 & **26.3** & **170.3** & **28.16** & **0.247** & 93.8 & 111.5 \\
300K & 27.09 & 0.255 & 215.5 & 17.3 & 27.83 & 0.273 & **49.3** & **137.8** & **28.36** & **0.232** & 161.6 & 84.0 \\
\end{tabular}

3DGUT-MCMC
23.97 dB / 0.724 / 0.548
Neural Harmonic Textures (Ours)
27.63 dB / 0.856 / 0.410

** 1:** Comparison with BBSplat \[59\] on MipNeRF360 (average over all 9 scenes). We follow BBSplat’s default training strategy and vary only the primitive cap; at 15k primitives we allocate 2k to the skybox following their supplement. Memory is reported after all compression schemes are applied. For NHT, primitive geometry is stored in `fp32` and vertex features plus MLP weights in `fp16`. Performance measured on an A100 80GB (Ampere).

**Fig.1:** Qualitative comparison on MipNeRF360 _bonsai_ with 10K Gaussians. Metrics are PSNR / SSIM / LPIPS averages over the test set. NHT recovers substantially more detail than 3DGUT-MCMC at equal primitive budget (+3.7dB PSNR).

