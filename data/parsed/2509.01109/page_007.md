<tbc>as default), and GPSToken-L256 (256 tokens). For more details about the training/inference and network architectures, please refer to **Appendix**.

**Evaluation Metrics.** We conduct all evaluations on the validation set of ImageNet. For _reconstruction_, we evaluate performance using both **sample-level** and **distribution-level** indices. At the sample level, we use PSNR, SSIM, and LPIPS \[40\], which measure the similarity between reconstructed and original images, as metrics. At the distribution level, we adopt FID \[13\] and sFID \[25\] to assess the overall distribution of reconstructed images. Specifically, we report "rec. FID" and "rec. sFID" to measure the distribution consistency between reconstructed and input images, while using standard "FID" and "sFID" to evaluate the alignment with natural image distributions. For image _generation_, we employ FID to assess generation quality.

## 4.2 Image Representation

**Comparison Results.** We evaluate the representation performance of GPSToken using the image reconstruction task. We compare GPSToken with existing 1D and 2D tokenization methods at \(256\times 256\) resolution, including SDXL-VAE \[11\], GaussianToken \[9\], VQVAE \[11\], MaskGiT- VAE \[3\], VAVAE \[36\], DCAE \[7\], TiToK \[38\], SoftVQ \[6\], FlexTok \[1\], One-D-Piece \[24\], and MAETok \[5\]. As shown in  1, GPSToken-L256 achieves significantly better performance than the competing methods across both sample-level and distribution-level metrics, even better than SDXL-VAE, which utilizes more tokens (1024 vs. 256) and is trained with a rich amount of additional data. Compared to SDXL-VAE, GPSToken-L256 improves PSNR by 3.26, SSIM by 0.082, and reduces LPIPS by 0.023. It also achieves a "rec. FID" of 0.22, a "rec. sFID" of 1.31, an FID of 1.65, and an sFID of 3.77, outperforming all competitors. Note that VAVAE \[36\] leverages vision foundation models to align latent features, yet it still lags behind GPSToken-L256.

On the other hand, GPSToken-M128 outperforms the competing methods using the same number of tokens on most metrics, obtaining a "rec. sFID" of 3.28 and LPIPS of 0.080. It also outperforms many methods that use more tokens. With only 64 tokens, GPSToken-S64 also demonstrates promising performance, achieving a "rec. FID" score of 1.31, highlighting the scalability of our approach.

\begin{tabular}{ccccccccccc}
\multirow{2}{*}{**Method**} & \multirow{2}{*}{**Tokens**} & \multirow{2}{*}{**Params

(M)**} & \multicolumn{3}{c}{**sample-level**} & \multicolumn{5}{c}{**distribution-level**} \\
 & & & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & rec. FID \(\downarrow\) & rec. sFID \(\downarrow\) & FID \(\downarrow\) & sFID \(\downarrow\) \\
\multicolumn{11}{c}{**2D Tokenization**} \\
SDXL-VAE \[27\] & 32\(\times\)32 & 83.6 & 25.55 & 0.727 & 0.066 & 0.73 & 2.42 & 2.35 & 3.89 \\
GaussianToken \[18\] & 32\(\times\)32 & 130.6 & 22.40 & 0.597 & 0.112 & 1.70 & 4.62 & 3.63 & 4.71 \\
VQVAE-f16 \[11\] & 16\(\times\)16 & 89.6 & 19.41 & 0.476 & 0.191 & 8.01 & 9.64 & 10.74 & 7.38 \\
MaskGIT-VAE \[3\] & 16\(\times\)16 & 54.5 & 18.11 & 0.427 & 0.202 & 3.79 & 5.81 & 5.19 & 4.56 \\
VAVAE \[36\] & 16\(\times\)16 & 69.8 & 25.76 & 0.742 & 0.050 & 0.27 & 1.72 & 1.74 & 3.91 \\
DCAE \[7\] & 8\(\times\)8 & 323.4 & 23.62 & 0.644 & 0.092 & 0.98 & 4.82 & 2.59 & 5.02 \\
\multicolumn{11}{c}{**1D Tokenization**} \\
SoftVQ \[6\] & 64 & 173.6 & 21.93 & 0.568 & 0.115 & 0.92 & 4.52 & 2.51 & 4.21 \\
TiTok-B64 \[38\] & 64 & 204.8 & 17.01 & 0.390 & 0.263 & 1.75 & 4.51 & 2.50 & 4.21 \\
TiTok-S128 \[38\] & 128 & 83.7 & 17.66 & 0.413 & 0.220 & 1.73 & 7.25 & 3.25 & 5.52 \\
MAETok \[5\] & 128 & 173.9 & 23.25 & 0.626 & 0.096 & 0.65 & 3.87 & 2.01 & 4.39 \\
FlexTok \[1\] & 256 & 949.7 & 17.69 & 0.475 & 0.257 & 4.02 & 8.00 & 4.88 & 6.12 \\
One-D-Piece \[24\] & 256 & 83.9 & 17.74 & 0.420 & 0.210 & 1.54 & 6.96 & 2.93 & 5.36 \\
MaskBit \[35\] & 256 & 54.5 & 21.07 & 0.539 & 0.142 & 1.29 & 4.72 & 3.08 & 4.09 \\
\multicolumn{11}{c}{**GPSToken**} \\
**S64** & 64 & 127.5 & 22.18 & 0.578 & 0.111 & 1.31 & 5.42 & 3.02 & 4.85 \\
**M128** & 128 & 127.8 & 24.06 & 0.657 & 0.080 & 0.65 & 3.28 & 2.18 & 3.96 \\
**L256** & 256 & 128.7 & 28.81 & 0.809 & 0.043 & 0.22 & 1.31 & 1.65 & 3.77 \\
\end{tabular}

1: Comparisons of \(256\times 256\) reconstruction task on Imagenet val set. The top 3 methods _trained only with ImageNet_ are highlighted in red, blue and green. Note that "SDXL-VAE" is trained with a rich amount of additional data other than Imagenet.

