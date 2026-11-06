<tbc>_Primitive count._ Fig. 5 illustrates how reconstruction quality scales with the number of primitives, ranging from 1K to 4M. Our method improves over pier art across this entire range, excelling particularly in the low primitive count regime. For instance, we achieve performance comparable to previous methods using 1M primitives with only a third of that amount, offering more flexibility in the memory-speed-quality trade-off; Supplementary Fig. 1 shows a side-by- side comparison against 3DGUT-MCMC on _bonsai_ with only 10K primitives (+3.7dB PSNR on average). Tabs. 13 and 14 in the supplementary material explore the impact of varying the per-primitive feature dimension and the MLP architecture, respectively, to illustrate the resulting quality-speed trade-offs.

_Feature encoding._ We ablate the choice of feature encoding function applied to the interpolated features in the Supplementary Tab. 11, showing how our choice of harmonic functions provides the best results.

### 5.2 Other Applications

_Alternative primitive-based methods._ We demonstrate the generality of our approach by incorporating Neural Harmonic Textures into 2DGS \[24\] and Triangle

\begin{tabular}{cccccccccc}
 & \multicolumn{3}{c}{MipNeRF360} & \multicolumn{3}{c}{Tanks \& Temples} & \multicolumn{3}{c}{Deep Blending} \\
Method & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
Instant NGP-Big \[49\] & 25.59 & 0.695 & 0.375 & 21.92 & 0.740 & 0.342 & 24.96 & 0.815 & 0.459 \\
Mip-NeRF 360 \[2\] & 27.60 & 0.788 & 0.275 & 22.22 & 0.754 & 0.290 & 29.40 & 0.899 & 0.306 \\
ZipNeRF \[3\] & 28.55 & 0.829 & 0.218 & 23.64 & 0.836 & 0.179 & - & - & - \\
2DGS \[24\] & 27.22 & 0.804 & 0.275 & 22.85 & 0.827 & 0.244 & 29.56 & 0.904 & 0.325 \\
3DGS-MCMC \[28\] & 27.99 & 0.830 & 0.229 & 24.46 & 0.866 & 0.174 & 29.49 & 0.912 & 0.306 \\
3DGUT-MCMC \[28\] & 27.82 & 0.826 & 0.233 & 24.20 & 0.861 & 0.180 & 29.87 & 0.913 & 0.309 \\
Beta Splatting-MCMC \[37\] & 28.12 & 0.831 & 0.238 & 24.54 & 0.866 & 0.196 & 29.56 & 0.907 & 0.316 \\
Spherical Voronoi \[11\] & 28.56 & **0.835** & 0.228 & 24.80 & 0.871 & 0.172 & 30.34 & 0.914 & **0.299** \\
Triangle Splatting \[23\] & 27.00 & 0.808 & 0.231 & 23.05 & 0.843 & 0.191 & 28.92 & 0.891 & 0.308 \\
Textured Gaussians \[4\] & 27.35 & 0.827 & - & 24.26 & 0.854 & - & 28.33 & 0.891 & - \\
NeST \[80\] & 26.54 & 0.776 & 0.260 & - & - & - & - & - & - \\
Radiance Meshes \[41\] & 27.15 & 0.810 & 0.274 & 23.13 & 0.851 & 0.200 & 29.39 & 0.901 & 0.362 \\
Neural Harmonic Textures (Ours) & **28.74** & 0.834 & **0.216** & **25.68** & **0.882** & **0.141** & **30.94** & **0.919** & 0.302 \\
\end{tabular}

** 1:** Comparison on MipNeRF360 \[2\], Tanks & Temples \[30\], and Deep Blending \[21\], on Neural Field-style methods, primitive-based methods, and mixed neural field/primitive-based methods. For the MipNeRF360 datasets, we disable _gsplat_’s default downscaling and instead train and evaluate directly on the provided JPEG- compressed reference images following prior work. We measure the effect in Tab. 5. For our method, we use 64 features per primitive (16 per vertex), with a 128-wide \(\times\) 3 hidden layers MLP, which results in a roughly similar number of total parameters as previous primitive-based approaches on average. We use 2M primitives for indoor scenes and 5M for outdoors. To regularize training in high-parallax regimes (e.g., indoor datasets), we encode the central camera ray rather than the individual ray direction. Finally, to ensure similar training epochs, we train indoor datasets longer (45k iterations for ∼290 images) than outdoor (25k for ∼175 images), following Spherical Voronoi \[11\] (SV). Unlike SV, we do not fine-tune learning rates per dataset. Note that convergence of an MLP-based appearance model can be slower than SH-based ones.

