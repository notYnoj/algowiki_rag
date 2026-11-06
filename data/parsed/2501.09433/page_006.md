<tbc>following the setup in ImageDream \[49\], but modify it to treat the input view as the frontal view rather than estimating.

**Texture Generation.** We implement the entire texture generation mechanism for texture synthesis upon the SDXL \[32\]. We utilize pre-trained IP Adapter \[57\] layer and CLIP \[34\] for the image feature extractor, Depth-ControlNet \[61\] for a geometric guide. Appendix C.2 provides the additional implementation specifications.

## 4.2 . Qualitative Comparison

### 4.2.1 Comparison with State-of-the-Art Methods

We evaluate the proposed CaPa by comparing it with various state-of-the-art image-to-3D approaches. Specifically, we include SDS-based \[33\] technique: DreamCraft3D \[43\]; MVDiffusion with its corresponding normals for sparse neural reconstruction: Era3D \[18\] (an enhanced version of Wonder3D \[25\]), or Unique3D \[54\] for mesh optimization; and finally, the LRM-based method: SF3D \[3\]. Note that all assets were converted into a polygonal mesh using official codes to ensure consistency and fair evaluation.

**High-Fidelity Mesh with Consistent Multi-View Textures.** As shown in Figure 6, CaPa significantly outperforms existing state-of-the-art methods, especially in not just frontal view, but also in back and side views, where competitors typically exhibit substantial degradation. Compared to sparse view NeRF reconstruction methods like Era3D \[18\], CaPa demonstrates markedly superior texture quality. In relation to Unique3D \[54\], which generates assets through mesh optimization based on multi-view images and corresponding normals, CaPa exhibits significantly higher geometric stability (See the second asset). Finally, compared to the SDS- based method \[43\], CaPa consistently produces high-fidelity polygonal meshes while accelerating the generation process and improving texture quality across multiple views. These results highlight CaPa’s effectiveness and robustness in producing high-quality 3D assets, showcasing its advantages over current methodologies in the field.

To further validate the effectiveness of CaPa’s texture generation process, we compared the textured outputs of our mesh with results from SyncMVD \[24\] and FlashTex \[9\], a leading texturing method. As shown in Figure 5, CaPa successfully addresses the Janus problem. In contrast, previous methods demonstrate limited id-consistency and still exhibit the Janus problem, relying primarily on _textual_ input alone.

## 4.3 . Quantitative Comparison

We present the quantitative results in  1, using 50 randomly selected test images generated via GPT \[30\]. We report the CLIP \[34\] score and FID \[11\], evaluated by measuring the similarity between each input image and the corresponding rendered outputs across 30 random views, thereby<tbc>

<tbc>indirectly assessing multi-view consistency. As shown in the table, CaPa achieves significantly higher scores than SOTA techniques, demonstrating its capability to produce consistent textures while preserving alignment with the input.

## 4.4 . Ablation Study and Discussion

We conduct comprehensive ablation studies to substantiate the effectiveness of each design element within CaPa, showing the importance of each component when the generation of high-quality 3D assets. Figure 7 shows the ablation results of each component.

**Multi-View Guidance in 3D Latent Diffusion.** As shown in Figure 7 (a), the multi-view guidance for 3D latent diffusion provides more comprehensive information on 3D geometry, which is crucial for the stable generation of 3D assets. It enables smoother, higher-quality geometry generation and minimizes quality loss during the meshing.

**Janus Prevention of Spatially Decoupled Attention.** The proposed Spatially Decoupled Attention effectively addresses the Janus problem by independently guiding each view during texture generation. Figure 7 (b) shows the texture generation results of CaPa, both with and without Spatially Decoupled Attention, revealing the adapter’s substantial capability to prevent multi-face generation.

**Occlusion Inpainting.** In this section, we demonstrate that our novel 3D-aware occlusion inpainting significantly outperforms previous occlusion inpainting solutions. In comparison to UV-ControlNet \[59\] and automatic view-selection methods \[5\], our approach achieves more comprehensive<tbc>

\begin{tabular}{cccc}
Method & CLIP (I-I) \(\uparrow\) & FID \(\downarrow\) & Time \(\downarrow\) \\
Ours & **86.34** & **47.56** & ∼30 seconds \\
DreamCraft3D \[43\] & 77.61 & 75.66 & ∼3 hours \\
Unique3D \[54\] & <u>81.92</u> & <u>67.17</u> & ∼2 minutes \\
Era3D \[18\] & 66.81 & 89.18 & ∼10 minutes \\
SF3D \[3\] & 70.18 & 84.52 & ∼**10 seconds** \\
\end{tabular}

Ours (Texturing) -20 seconds
SyncMVD -6 minutes
FlashTex -2 minutes

Figure 5. **Comparison of Texturing Method.** Unlike prior works, CaPa effectively resolved the Janus problem with consistent ID.

1. **Quantitative results.** CaPa outperforms all the competitors by a significant margin in both CLIP score and FID score, with a reasonable generation time.

