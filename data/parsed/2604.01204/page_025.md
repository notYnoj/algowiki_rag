## Differences to RGB-only training.

Aside from the extra output head and loss terms, training proceeds as in the main paper: same optimizer, learning-rate schedules, EMA on the MLP, and color-refinement phase. The only architectural change is the increased output dimension (3 + 512 when fused, or a separate 512-dim linear layer). We do not use a separate training stage for LSEG; RGB and LSEG are optimized jointly from the start.

## PCA visualization.

LSEG feature maps are 512-dimensional and therefore not directly viewable. For qualitative inspection, we project both ground-truth and predicted features to RGB via PCA. The PCA basis is computed from the first image, then applied the to all frames. Fig. 3 shows example PCA visualizations. They allow a direct visual comparison of semantic structure and show that the predicted features align well with the target, while being substantially faster to generate and higher resolution than inferring the RGB frame only and running the LSEG model to obtain its feature map. Semantic scene reconstruction extracts detail from the multiple training views, improving the granularity of the semantic information available for downstream applications.

Finally, in Tab. 8 we ablate the feature dimensionality for the joint RGB and LSEG semantic reconstruction task.

\begin{tabular}{ccccccccccccc}
 & \multicolumn{3}{c}{3DGS-MCMC + SH} & \multicolumn{3}{c}{3DGUT-MCMC + SH} & \multicolumn{3}{c}{NHT (Ours, 48F)} & \multicolumn{3}{c}{NHT (Ours, 64F)} \\
Scene & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
\multicolumn{13}{c}{_MipNeRF360 - Outdoor_} \\
bicycle & **25.87** & **0.801** & **0.183** & 25.69 & 0.790 & 0.193 & 25.53 & 0.779 & 0.202 & 25.62 & 0.776 & 0.202 \\
garden & 28.11 & **0.880** & 0.107 & 27.84 & 0.874 & 0.111 & **28.33** & 0.878 & **0.102** & 28.23 & 0.876 & 0.103 \\
stump & **27.32** & **0.808** & **0.203** & 27.15 & 0.802 & 0.215 & 27.06 & 0.788 & 0.215 & 27.02 & 0.786 & 0.215 \\
treehill & **23.29** & **0.670** & 0.310 & 23.13 & 0.664 & 0.313 & 21.96 & 0.639 & 0.311 & 22.27 & 0.640 & **0.308** \\
flowers & **22.25** & **0.652** & **0.312** & **22.25** & 0.648 & 0.318 & 21.90 & 0.637 & 0.315 & 21.77 & 0.631 & **0.312** \\
\multicolumn{13}{c}{_MipNeRF360 - Indoor_} \\
room & 32.56 & 0.939 & 0.240 & 32.43 & 0.939 & 0.241 & **33.82** & 0.945 & 0.229 & 33.75 & **0.946** & **0.227** \\
counter & 29.53 & 0.925 & 0.219 & 29.55 & 0.925 & 0.220 & 30.80 & **0.931** & 0.205 & **30.92** & **0.931** & **0.203** \\
kitchen & 32.10 & 0.938 & 0.136 & 31.96 & 0.938 & 0.136 & 33.43 & **0.944** & 0.127 & **33.44** & **0.944** & **0.124** \\
bonsai & 32.84 & 0.955 & 0.216 & 32.76 & 0.955 & 0.215 & 34.99 & **0.963** & 0.202 & **35.07** & 0.962 & **0.201** \\
\multicolumn{13}{c}{_Tanks \& Temples_} \\
train & 22.48 & 0.832 & 0.221 & 22.19 & 0.826 & 0.229 & 23.88 & 0.856 & 0.198 & **24.33** & **0.858** & **0.194** \\
truck & 26.43 & 0.899 & 0.126 & 26.21 & 0.896 & 0.131 & 26.94 & **0.901** & 0.115 & **26.96** & **0.901** & **0.114** \\
\multicolumn{13}{c}{_Deep Blending_} \\
drjohnson & 29.25 & 0.910 & 0.310 & 29.13 & 0.910 & 0.315 & 30.06 & **0.916** & 0.308 & **30.09** & **0.916** & **0.306** \\
playroom & 29.72 & 0.913 & 0.301 & 30.60 & 0.916 & 0.302 & **31.28** & **0.920** & 0.297 & **31.28** & **0.920** & **0.296** \\
M360 Outdoor Avg & **25.37** & **0.762** & **0.223** & 25.21 & 0.756 & 0.230 & 24.96 & 0.744 & 0.229 & 24.98 & 0.742 & 0.228 \\
M360 Indoor Avg & 31.76 & 0.939 & 0.203 & 31.67 & 0.939 & 0.203 & 33.26 & **0.946** & 0.191 & **33.30** & **0.946** & **0.189** \\
M360 Total Avg & 28.21 & **0.841** & 0.214 & 28.08 & 0.837 & 0.218 & 28.65 & 0.834 & 0.212 & **28.68** & 0.832 & **0.211** \\
T\&T Avg & 24.46 & 0.866 & 0.174 & 24.20 & 0.861 & 0.180 & 25.41 & 0.879 & 0.157 & **25.65** & **0.879** & **0.154** \\
DB Avg & 29.49 & 0.912 & 0.306 & 29.87 & 0.913 & 0.309 & 30.67 & **0.918** & 0.302 & **30.69** & **0.918** & **0.301** \\
\end{tabular}

** 4:** Per-scene results for the standardized comparison (Tab. 3). All methods use the same primitive count (matching the baseline default), 30k iterations, and the same hyperparameters across all scenes.

