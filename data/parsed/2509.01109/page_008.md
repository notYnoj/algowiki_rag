**Effectiveness of Spatial Adaptivity.** GPSToken possesses spatial adaptivity (SA), enabling a region adaptive image representation. As shown in Fig. 4, with our SA initialization, the **g**_<sup>init</sup>_ is placed according to the regional complexity. More Gaussians are assigned to complex regions such as the human body, while sparse Gaussians are used in simpler regions. Based on this initialization, the refined **g** further adjusts its positions, shapes, and orientations to better align with local textures. It can be clearly observed that with SA enabled, the maps exhibit significantly lower errors in complex regions (Figs. 4(f-g)), while the errors in simple regions (_e.g._, background) remain largely unchanged. This demonstrates that our GPSToken improves the representation in complex areas without compromising the quality in simpler ones.

**User-Controllable Adjustment of** **g**_<sup>init</sup>_**.** Additionally, GPSToken supports manual adjustment of **g**_<sup>init</sup>_, allowing users to prioritize semantically important regions (_e.g._, faces or text). An example is shown in Fig. 5, where placing denser Gaussians in target areas results in clearer reconstructions.

**Adjustable Token Count at Inference.** GPSToken supports adjustable token count at inference (see Fig. 6). Unlike \[1, 24\], which only supports decreasing the number of tokens at inference, GPSToken can also increase the number of tokens for improved quality.

Please refer to **Appendix** for more results of GPSToken on generalization performance, efficiency, ablation studies, and visualizations.

## 4.3 Image Generation

**Comparison Results.** We compare our approach against state-of-the-art tokenizers for image generation, including MaskGIT \[3\], TiTok \[38\], FlexTok \[1\], SoftVQ \[6\], ADM \[8\], One-D-Piece \[24\], DiT \[26\], SiT \[23\], REPA \[39\], D<sup>2</sup>iT \[16\], and MAETok \[5\], on \(256\times 256\) class-conditional generation tasks. Quantitative results with classifier-free guidance \[14\] are reported in Tab. 2. Our two-stage generator with 128 tokens outperforms all competing methods, achieving an FID of 1.50, highlighting the effectiveness of GPSToken in providing a superior latent space for generative models, even with fewer tokens. With an equal number of tokens (128), MAETok \[5\] under-performs our GPSToken-based generator, suggesting that our Gaussian-parameterized tokenization offers distinct advantages. In contrast, the one-stage generator slightly under-performs the baseline. This discrepancy arises from the optimization challenges inherent in the composition of Gaussian parameters **g** and<tbc>

(a) inp
(b) (c) refined (d) GPSToken
(e) GPSToken w/o SA
(f) errors of (d)
(g) errors of (e)

