<tbc>stage, GPS-tokens are mapped into \(64\times 642\)D feature maps. The decoder adopts the same architecture as the last three stages of the SDXL-VAE \[27\] decoder but with double channels. GPSToken-M128 utilizes 128 tokens, each with 16 channels, whereas GPSToken-L256 employs 256 tokens, each with 32 channels, to match the capacity of VAVAE \[37\]. GPSToken-S64 uses only 64 tokens, each with 16 channels, but incorporates 60 transformation blocks within the encoder.

For the _image generation task_, we adopt the official SiT-S and SiT-XL architectures \[23\] as our backbone models. Specifically, SiT-S is utilized for layout synthesis, while SiT-XL is employed for conditional layout-to-texture generation. To support layout conditions, we use MLPs to transform these conditions before adding them into each attention block in SiT-XL.

## C Generalization of GPSToken on Higher Resolutions and Other Datasets

**Higher Resolution.** We evaluate pre-trained GPSToken-M128 and GPSToken-L256 - originally trained on \(256\times 256\) images with 128 and 256 tokens, respectively - on \(512\times 512\) and \(1024\times 1024\) images from the ImageNet validation set. We compare with SDXL-VAE \[27\] and VQVAE-f16 \[11\], two public VAEs supporting reconstruction beyond training resolution. Following their practice, we scale the token count quadratically with resolution. For example, we use 512 and 2048 tokens for \(512\times 512\) and \(1024\times 1024\) inputs, respectively, when using GPSToken-M128.

As shown in  3, GPSToken shows strong generalization performance on resolution. Specifically, GPSToken-L256 achieves 32.00/0.887 (PSNR/SSIM) at \(512\times 512\) resolution and 37.71/0.955 at \(1024\times 1024\) resolution, outperforming SDXL-VAE in both settings. On the other hand, all methods show higher reconstruction performance at higher resolutions. GPSToken-M128 achieves a better "rec. FID" of 0.236 at \(1024\times 1024\) than that (0.367) at \(512\times 512\). This is because higher resolutions provide more pixels for the same content, increasing local redundancy and structural consistency. The denser pixel sampling makes fine details easier to recover, simplifying the reconstruction task despite the larger input size.

**More Datasets.** We further evaluate on additional datasets: COCO2017 \[22\] (natural images), FFHQ \[17\] (faces), STARE \[15\] (medical images), and WHU\_RS19 \[2\] (remote sensing). We compare GPSToken with VAVAE \[37\] (256 tokens, 2D) and MAETok \[5\] (128 tokens, 1D), representing the state of the art in 2D and 1D tokenization, respectively. As shown in  4, GPSToken consistently outperforms both methods across all metrics and datasets under the same token counts.

Specifically, GPSToken-L256 achieves higher PSNR than VAVAE (256 tokens): 27.41 vs. 25.01 on COCO, 30.02 vs. 28.06 on FFHQ, 37.60 vs. 36.32 on STARE, and 26.33 vs. 23.57 on WHU\_RS19. GPSToken-M128 also yields better LPIPS than MAETok (128 tokens): 0.083 vs. 0.101 on COCO, 0.050 vs. 0.064 on FFHQ, 0.036 vs. 0.051 on STARE, and 0.127 vs. 0.195 on WHU\_RS19. These results show that GPSToken performs well not only on natural images but also on other domains - including medical and remote sensing - demonstrating strong generalization, robustness, and versatility for a wide range of vision tasks.

\begin{tabular}{ccccccc}
\multirow{2}{*}{**Method**} & \multirow{2}{*}{**Tokens**} & \multicolumn{3}{c}{**sample-level**} & \multicolumn{2}{c}{**distribution-level**} \\
 & & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & rec. FID \(\downarrow\) & rec. sFID \(\downarrow\) \\
\multicolumn{7}{c}{\(512\times 512\)} \\
SDXL-VAE \[27\] & 64\(\times\)64 & 28.42 & 0.817 & 0.059 & 0.271 & 1.36 \\
VQVAE-f16 \[11\] & 32\(\times\)32 & 21.83 & 0.604 & 0.172 & 2.29 & 7.95 \\
GPSToken-M128 & 512 & 26.74 & 0.764 & 0.073 & 0.367 & 1.93 \\
GPSToken-L256 & 1024 & 32.00 & 0.887 & 0.039 & 0.175 & 0.699 \\
\multicolumn{7}{c}{\(1024\times 1024\)} \\
SDXL-VAE \[27\] & 128\(\times\)128 & 33.27 & 0.909 & 0.057 & 0.113 & 0.561 \\
VQVAE-f16 \[11\] & 64\(\times\)64 & 25.41 & 0.744 & 0.169 & 1.40 & 4.98 \\
GPSToken-M128 & 2048 & 31.22 & 0.873 & 0.072 & 0.236 & 1.24 \\
GPSToken-L256 & 4096 & 37.71 & 0.955 & 0.031 & 0.055 & 0.276 \\
\end{tabular}

3: Comparisons of \(512\times 512\) and \(1024\times 1024\) reconstruction task on Imagenet val set.

