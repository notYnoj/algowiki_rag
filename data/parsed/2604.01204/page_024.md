<tbc>feature field. Joint RGB and LSEG training uses the same approach, densification, and regularization as standard radiance-field training, with the differences being in the addition of semantic supervision losses and an expanded decoding head in our MLP. The deferred MLP is extended to predict both RGB (3 channels) and LSEG features (512 dimensions) via addition of an extra Pytorch linear layer. Rendering speed becomes bottlenecked by this linear layer, and more efficient fused alternatives or upsampling strategies could be explored in the future--we consider this a proof-of-concept implementation.

The total loss adds an LSEG term to the usual L<sub>1</sub>, D-SSIM, opacity and scale regularizers terms:

\(\mathcal{L}_\mathrm{LSEG}=\lambda_\mathrm{LSEG}\mathcal{L}_{\mathrm{L}_1}\left(\hat{f},f^*\right)+\lambda_\mathrm{cos}\left(1-\mathrm{cos}(\hat{f},f^*)\right),\) (1)

where \(\hat{f}\) and _f_<sup>∗</sup> are predicted and ground-truth LSEG feature maps, and _cos_ their cosine similarity. We compute these losses at the native LSEG resolution: the model renders at RGB resolution (high); then, we bilinearly downsample the predicted feature map to match the (lower-resolution) LSEG targets. Tab. 9 lists the LSEG-specific hyperparameters used in our final training. We largely kept the same configuration from our pure RGB radiance field experiments; further tuning for this specific use case may render higher performance.

\begin{tabular}{cccc}
Method (w/ MCMC) & MipNeRF360 & Tanks \& Temples & Deep Blending \\
3DGS + SH & 6.0 & 5.1 & 5.2 \\
3DGUT + SH & 7.1 & 5.8 & 6.0 \\
3DGUT + SV & 7.7 & 6.4 & 6.6 \\
3DGUT + NHT (Ours) & 14.5 & 9.4 & 10.6 \\
\end{tabular}

\begin{tabular}{cccccccccc}
 & \multicolumn{3}{c}{MipNeRF360} & \multicolumn{3}{c}{Tanks \& Temples} & \multicolumn{3}{c}{Deep Blending} \\
Method & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
3DGS-MCMC + SH & 28.21 & **0.841** & 0.214 & 24.46 & 0.866 & 0.174 & 29.49 & 0.912 & 0.306 \\
3DGUT-MCMC + SH & 28.08 & 0.837 & 0.218 & 24.20 & 0.861 & 0.180 & 29.87 & 0.913 & 0.309 \\
3DGUT-MCMC + NHT (Ours, 48F) & 28.65 & 0.834 & 0.212 & 25.41 & 0.878 & 0.156 & 30.67 & **0.918** & 0.302 \\
3DGUT-MCMC + NHT (Ours, 64F) & **28.68** & 0.832 & **0.211** & **25.64** & **0.879** & **0.154** & **30.69** & **0.918** & **0.301** \\
\end{tabular}

** 2:** Average wall-clock training time (minutes) to reach 30k iterations with 1M primitives, measured on an NVIDIA RTX 5090 and averaged per dataset. All methods are implemented in the same _gsplat_ \[76\] framework and use the same hyperparameters as in Tab. 2. NHT timings use our fused kernels.

** 3:** Standardized comparison on MipNeRF360 \[2\], Tanks & Temples \[30\], and Deep Blending \[21\]: 3DGS-MCMC, 3DGUT-MCMC, and ours with 48 and 64 features per primitive (48F, 64F). All methods use the same primitive count (matching the high-quality preset in 3DGS-MCMC, which replicates the number of primitives in each scene from original 3DGS), 30k iterations, and the same hyperparameters across all scenes. Extended version of Tab. 2 of the main paper. While our work particularly excels at extracting higher quality from less primitives, we still outperform previous works at high primitive counts across the board.

