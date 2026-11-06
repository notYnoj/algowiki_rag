\begin{tabular}{cc}
\multicolumn{2}{c}{**Training**} \\
Color refinement phase & Last 3000 steps (geometry frozen, no reg.) \\
\multicolumn{2}{c}{**Loss \& regularization**} \\
SSIM weight \(\lambda\) (D-SSIM vs L<sub>1</sub>) & 0.1 \\
Opacity regularization \(\lambda_\alpha\) & 0.02 \\
Scale regularization \(\lambda_s\) & 0.005 \\
\multicolumn{2}{c}{**Learning rates (initial)**} \\
Positions (means) & \(1.6\times 10^{-4}\) \\
Scales & \(5\times 10^{-3}\) \\
Opacities & \(5\times 10^{-2}\) \\
Quaternions & \(1\times 10^{-3}\) \\
Deferred features & \(1.5\times 10^{-2}\) \\
Deferred MLP & \(6.8\times 10^{-4}\) \\
\multicolumn{2}{c}{**LR schedule**} \\
Positions & Exponential decay (final factor 0.01) \\
Features \& MLP & Cosine annealing (final factor 0.1) \\
\multicolumn{2}{c}{**EMA (deferred MLP)**} \\
Decay \(\gamma\) & 0.95 \\
Start step & 0 \\
\multicolumn{2}{c}{**Appearance (NHT)**} \\
Feature dim. per primitive & 16-64 \\
MLP hidden dim. \(\times\) layers & \(64-128\times 2-3\) \\
View encoding & Spherical harmonics (2nd degree) \\
\end{tabular}

\begin{tabular}{ccccc}
Dim & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & FPS\(\uparrow\) \\
4 & 27.18 & 0.809 & 0.288 & 165 \\
8 & 27.83 & 0.818 & 0.261 & 156 \\
16 & 28.22 & 0.826 & 0.246 & 142 \\
24 & 28.31 & 0.828 & 0.240 & 134 \\
32 & 28.39 & 0.829 & 0.237 & 133 \\
48 & 28.43 & 0.829 & 0.231 & 116 \\
64 & 28.48 & 0.828 & 0.230 & 105 \\
80 & 28.47 & 0.828 & 0.227 & 98 \\
\end{tabular}

\begin{tabular}{ccccc}
Size & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & FPS\(\uparrow\) \\
16\(\times\)2 & 28.16 & 0.824 & 0.240 & 97 \\
16\(\times\)4 & 28.03 & 0.820 & 0.244 & 98 \\
32\(\times\)2 & 28.25 & 0.825 & 0.238 & 97 \\
32\(\times\)4 & 28.23 & 0.824 & 0.237 & 101 \\
64\(\times\)2 & 28.38 & 0.827 & 0.234 & 102 \\
64\(\times\)4 & 28.36 & 0.826 & 0.233 & 102 \\
128\(\times\)2 & 28.47 & 0.828 & 0.230 & 106 \\
128\(\times\)4 & 28.50 & 0.828 & 0.229 & 103 \\
\end{tabular}

** 12:** Hyperparameters and optimization details for radiance field reconstruction (MipNeRF360, Tanks & Temples, Deep Blending). Values follow our _gsplat_ implementation \[75\].

** 13:** Ablating feature count _N_. Measured on an RTXA6000 Ada.

** 14:** Ablating MLP architecture (layer width \(\times\) hidden layer count). Measured on an RTXA6000 Ada.

