<tbc>Splatting \[23\]. Our method is readily adapted to these 2D primitives by simply replacing the bounding tetrahedra with virtual triangles (2DGS) or directly anchoring feature vectors to explicit triangle geometry (Triangle Splatting), therefore using three feature vectors per primitive instead of four. The results are shown in Tab. 3, with further details in the Supplementary.

## Semantic field reconstruction.

Our method can easily model higher dimensional data as well. By simply expanding the decoding head of our MLP, we can fit signals of arbitrary dimension. As the rest of the MLP layers remain small, and the size of feature vectors remains the same, the model is forced to exploit potential correlations between dimensions. A particularly challenging case is semantic scene reconstruction, where fields are upwards of 512-dimensional. 3DGS-based methods relying on high-dimensional explicit features generally struggle with such scale, even when paired with feature upsampling networks. We thus test<tbc>

\begin{tabular}{ccccccccccccc}
 & \multicolumn{4}{c}{MipNeRF360} & \multicolumn{4}{c}{Tanks \& Temples} & \multicolumn{4}{c}{Deep Blending} \\
Method (w/ MCMC) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & FPS\(\uparrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & FPS\(\uparrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & FPS\(\uparrow\) \\
3DGS + SH & 27.94 & 0.829 & 0.246 & **251** & 24.25 & 0.861 & 0.188 & **294** & 29.98 & 0.912 & 0.317 & **331** \\
3DGUT + SH & 27.93 & 0.828 & 0.247 & 201 & 23.99 & 0.859 & 0.192 & 245 & 30.21 & 0.913 & 0.318 & 282 \\
3DGUT + SV & 28.15 & 0.823 & 0.248 & 202 & 24.18 & 0.861 & 0.187 & 242 & 30.29 & 0.912 & 0.320 & 267 \\
3DGUT + NHT (Ours) & **28.46** & **0.830** & **0.232** & 140 & **24.79** & **0.875** & **0.169** & 226 & **30.88** & **0.918** & **0.311** & 240 \\
\end{tabular}

\begin{tabular}{cccc}
Method & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
Triangle Splatting & 27.00 & **0.808** & 0.231 \\
Triangle Splatting + NHT & **27.52** & 0.807 & **0.227** \\
2DGS & 27.48 & 0.816 & 0.263 \\
2DGS + NHT & **28.27** & **0.820** & **0.238** \\
3DGUT-MCMC & 27.93 & 0.828 & 0.247 \\
3DGUT-MCMC + NHT & **28.46** & **0.830** & **0.232** \\
\end{tabular}

28
26
PSNR (dB)
24
NHT (Ours)
22
3DGS-MCMC
3DGUT-MCMC
20
1
10
100
1,000
Primitive Count (thousands)

** 2:** Quantitative results of our approach and baselines on the MipNeRF360 \[2\], Tanks & Temples \[30\], and Deep Blending \[21\] datasets, comparing our method against Spherical Voronoi \[11\] (SV) and regular SH models. We isolate the effect of our approach by implementing all methods in the same framework (_gsplat_ \[76\] with its default downsampling), using the same number of primitives (1M), training for the same number of iterations (30k), allocating the same number of parameters per primitive for appearance (48) and using the same hyperparameters for all scenes. Our method uses a 128\(\times\)3 hidden MLP. All MCMC-based methods share the same opacity and scale regularizers from 3DGS-MCMC \[28\]. We improve reconstruction quality while still managing real-time performance (RTX A6000 Ada).

** 3:** Generality of NHT: we apply it to different primitive-based representations, evaluated on MipNeRF360 \[2\]. Triangle Splatting methods use JPEG references as in its source implementation. We would like to note that our results for Triangle Splatting are just a proof-of-concept and were not extensively optimized.

**Fig.5:** Our method outperforms 3DGS and 3DGUT at all primitive counts. The improvement is particularly pronounced in the low- primitive regime (\(\le 100k\)), with deltas upwards of 2dB of PSNR.

