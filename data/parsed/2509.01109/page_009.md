<tbc>textual features **f** within a single token **z**. Our two-stage design (first generate **g** then synthesize **f**), effectively addresses this issue, leading to significant enhancement over the baseline.

**Faster Training.** As illustrated in Fig. 7, our two-stage generator demonstrates significantly accelerated convergence compared to both the baseline and one-stage generator. Specifically, it achieves an FID-10K score of 25.48 within 100K iterations. In contrast, the SiT-XL/2 and one-stage generator reach scores of 25.41 and 26.20 after 300K and 500K iterations, respectively, indicating that our method is approximately 3\(\times\) and 5\(\times\) faster than them. This notable speed-up highlights the effectiveness of shape-texture decomposition in simplifying the optimization process. More results on training efficiency can be found in **Appendix**.

**Qualitative Analysis of Generation Process.** Fig. 8 provides a visual breakdown of the generation pipeline. Initially, **g**<sup>init</sup> captures a coarse structure but may include incomplete or misaligned regions in Gaussian maps. Our calibration algorithm addresses these issues and refines **g**<sup>init</sup> into a semantically coherent and spatially accurate layout \(\mathbf{g}_{cal}^{init}\). Leveraging this calibrated layout, the second stage generates Gaussian parameters **g** that can encode local texture orientation and scale. Consequently, the final image not only retains the global structure established by **g**<sup>init</sup> but also achieves rich details, exemplified by the synthesized dog/rabbit images. More results can be found in **Appendix**.

## 5 Conclusion

In this paper, we introduced **GPSToken**, a spatially-adaptive image tokenization approach for effective image representation and generation. Unlike conventional grid-based 2D/1D tokenizers, GPSToken<tbc>

\begin{tabular}{ccccc}
\multirow{2}{*}{**Method**} & \multicolumn{2}{c}{**Tokenizer**} & \multicolumn{2}{c}{**Generator**} \\
 & Params (M) & Tokens & Params (M) & FID \(\downarrow\) \\
\multicolumn{5}{c}{**Auto-regressive Models**} \\
MaskGIT \[3\] & 54.5 & 16\(\times\)16 & 227 & 6.18 \\
FlexTok \[1\] & - & 256 & 1,330 & 2.02 \\
TiTok-S128 \[38\] & 83.7 & 128 & 287 & 1.97 \\
TiTok-B64 \[38\] & 204.8 & 64 & 177 & 2.77 \\
SoftVQ \[6\] & 173.6 & 64 & 675 & 1.78 \\
\multicolumn{5}{c}{**Diffusion-based Models**} \\
ADM \[8\] & - & - & 23.24 & 3.94 \\
One-D-Piece \[24\] & 83.9 & 256 & - & 2.35 \\
DiT-XL/2 \[26\] & 83.6 & 32\(\times\)32 & 675 & 2.27 \\
SiT-XL/2<sup>+</sup> \[23\] & 83.6 & 32\(\times\)32 & 675 & 2.06 \\
REPA \[39\] & 83.6 & 32\(\times\)32 & 675 & 1.79 \\
D<sup>2</sup>iT \[16\] & - & \>256 & 687 & 1.73 \\
MAETok \[5\] & 173.9 & 128 & 675 & 1.67 \\
**Ours (one-stage)** & 127.8 & 128 & 675 & 2.13 \\
**Ours (two-stage)** & 127.8 & 128 & 33+675 & 1.50 \\
\end{tabular}

psnr: 19.26 ssim:0.600
psnr: 22.64 ssim:0.737
psnr: 26.03 ssim:0.834
psnr: 27.10 ssim:0.859
32 tokens
64 tokens
128 tokens (default)
256 tokens
GT

Figure 6: **Adjustable Token Count at Inference**. Token count can be adjusted at inference for better quality-efficiency trade-off, even beyond default training setting (128 tokens).

2: Comparisons on \(256\times 256\) class-conditional image generation. The top 2 methods are highlighted in red and blue. "<sup>+</sup>" indicates the baseline.

