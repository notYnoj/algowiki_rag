\begin{tabular}{cc}
Parameter & Value \\
LSEG output feature dimension & 512 \\
LSEG L<sub>1</sub> loss weight \(\lambda_\mathrm{LSEG}\) & 1.0 \\
LSEG cosine similarity weight \(\lambda_\mathrm{cos}\) & 0.1 \\
Per-primitive feature dim. (shared with RGB) & 80 \\
\end{tabular}

\begin{tabular}{ccccc}
 & Configuration & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS (Alex)\(\downarrow\) \\
 & Our Model & 28.49 & 0.828 & 0.153 \\
A) & No LR Scheduling & 28.37 & 0.829 & 0.147 \\
B) & No EMA on MLP Weights & 28.46 & 0.828 & 0.152 \\
D) & No Color Refinement Phase & 28.35 & 0.827 & 0.154 \\
E) & No Opacity Regularization & 27.85 & 0.806 & 0.181 \\
F) & No Scale Regularization & 28.50 & 0.828 & 0.153 \\
G) & No Direction Encoding & 28.11 & 0.816 & 0.155 \\
I) & No Direction Scaling & 28.35 & 0.822 & 0.158 \\
\end{tabular}

\begin{tabular}{cccc}
Encoding & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
None (identity) & 28.21 & 0.819 & 0.255 \\
ReLU & 28.19 & 0.819 & 0.255 \\
Cosine & 28.34 & 0.826 & 0.234 \\
Cosine \& Sine & **28.46** & **0.830** & **0.232** \\
\end{tabular}

** 9:** LSEG-specific hyperparameters used for joint RGB and semantic feature training.

** 10:** Ablation study on training strategies. The rows are _not_ additive, i.e. we only test one strategy at a time. All experiments on the MipNeRF360 dataset, using 64 features per primitive and a 128\(\times\)3 MLP. All MCMC baselines in Tab. 2 already use the same opacity regularizer; row E) ablates its removal from NHT. Note that the scale regularization (F) does not significantly affect reconstruction quality, but does improve render time.

** 11:** Ablating the choice of feature encoding function (MipNeRF360 dataset).

