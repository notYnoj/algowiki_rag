## D FLOPs, Memory and Latency for Reconstruction Task

We provide profiling details on FLOPs, memory usage, latency, and throughput for the \(256\times 256\) image reconstruction task. As shown in  5, GPSToken incurs moderate computational cost. Although the FLOPs of GPSToken decoder are higher than those of VQVAE-f16 \[34\] and TiTok- B64 \[38\], its latency is competitive with GaussianToken \[9\] and significantly better than FlexTok \[1\], which employs a heavy autoregressive decoder. In terms of memory, GPSToken uses less GPU memory than FlexTok and GaussianToken during inference, and less training memory than VQVAE- f16, demonstrating favorable memory efficiency in both phases.

## E Ablation Studies on Spatial Adaptivity Designs

**Ablation Studies on Components.** As described in Sec. 3.2 of the main paper, our GPSToken employs spatially-adaptive token initialization ("Init.") followed by spatially-adaptive token refinement<tbc>

\begin{tabular}{cccccc}
**Token Count** & **Method** & **PSNR** \(\uparrow\) & **SSIM** \(\uparrow\) & **LPIPS** \(\downarrow\) & **rec. FID** \(\downarrow\) \\
\multicolumn{6}{c}{**COCO**} \\
\multirow{2}{*}{128} & MAETok & 22.67 & 0.623 & 0.101 & 8.91 \\
 & GPSToken-M128 & 23.47 & 0.657 & 0.083 & 4.72 \\
\multirow{2}{*}{256} & VAVAE & 25.01 & 0.736 & 0.052 & 6.01 \\
 & GPSToken-L256 & 27.41 & 0.794 & 0.035 & 2.23 \\
\multicolumn{6}{c}{**FFHQ**} \\
\multirow{2}{*}{128} & MAETok & 25.53 & 0.707 & 0.064 & 4.66 \\
 & GPSToken-M128 & 26.35 & 0.745 & 0.050 & 3.72 \\
\multirow{2}{*}{256} & VAVAE & 28.06 & 0.808 & 0.027 & 1.95 \\
 & GPSToken-L256 & 30.02 & 0.846 & 0.019 & 1.51 \\
\multicolumn{6}{c}{**STARE**} \\
\multirow{2}{*}{128} & MAETok & 32.98 & 0.818 & 0.051 & - \\
 & GPSToken-M128 & 34.75 & 0.868 & 0.036 & - \\
\multirow{2}{*}{256} & VAVAE & 36.32 & 0.896 & 0.019 & - \\
 & GPSToken-L256 & 37.60 & 0.915 & 0.014 & - \\
\multicolumn{6}{c}{**WHU\_RS19**} \\
\multirow{2}{*}{128} & MAETok & 21.73 & 0.506 & 0.195 & - \\
 & GPSToken-M128 & 23.20 & 0.560 & 0.127 & - \\
\multirow{2}{*}{256} & VAVAE & 23.57 & 0.619 & 0.142 & - \\
 & GPSToken-L256 & 26.33 & 0.731 & 0.064 & - \\
\end{tabular}

\begin{tabular}{ccccccc}
\multirow{2}{*}{**Method**} & \multicolumn{2}{c}{**FLOPs (G)**} & \multicolumn{2}{c}{**Memory (MB)**} & \multirow{2}{*}{**Latency

(ms)**} & \multirow{2}{*}{**Throughput

(sample/s)**} \\
 & Encoder & Decoder & Train & Inference & & \\
VQVAE-f16 & 556 & 1014 & 78222 & 2627 & 72 & 111.44 \\
TiTok-B64 & 220 & 973 & 45892 & 2359 & 96 & 83.44 \\
GPSToken-M128 & 383 & 2689 & 50793 & 2567 & 180 & 44.56 \\
GaussianToken & 1706 & 2285 & 60781 & 5352 & 181 & 44.32 \\
FlexTok & 283 & 7665 & - & 7275 & 2714 & 2.88 \\
\end{tabular}

4: Comparison of \(256\times 256\) image reconstruction on COCO, FFHQ, STARE, and WHU\_RS19. For STARE and WHU\_RS19, we only report PSNR, SSIM, and LPIPS, which are more appropriate for evaluating reconstruction quality on non-photorealistic images than metrics such as "rec. FID".

5: Comparison of computational cost, memory usage, latency, and throughput for generating \(256\times 256\) images on an A100 GPU. Batch size is 8 for inference and 16 for training. Latency is averaged over 20 runs. Throughput is measured in samples per second. Training memory for FlexTok is unavailable due to the lack of released training code.

