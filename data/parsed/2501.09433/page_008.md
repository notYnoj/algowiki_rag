FID and KID scores indicate better alignment and visual coherence. Our method achieves an FID of 55.23 and KID of 13.46, significantly outperforming UV-ControlNet, demonstrating its ability to preserve texture fidelity and semantic accuracy. While the automatic view-selection method \[5\] achieves slightly lower scores, it requires 20 seconds for iterative smoothing, resulting in blurred output. In contrast, our approach maintains sharpness and semantic fidelity while achieving faster, visually coherent textures.

### 4.5 . Scalability of CaPa

A major advantage of the Spatially Decoupled Attention in texture generation is its model-agnostic nature. Unlike previous MVDiffusion \[40, 49\], our texturing scheme can be directly applied to pre-existing large generative models and its variants, including LoRA \[14\] and ControlNet. Additionally, the pipeline supports flexible extensions, such as 3D inpainting via text prompts. We demonstrate CaPa’s scalability through 3D inpainting and LoRA integration examples. As shown in Figure 8, CaPa requires no additional training for 3D stylization, underscoring its scalability with a wide range of 2D generative communities.

### 4.6 . Supplementary Material

To further validate CaPa, we present additional results in Appendix B, including diverse image/text-to-3D outputs, com<tbc>

<tbc>parative experiments addressing Janus artifacts, and analysis of occlusion edge cases. Additionally, we discuss the limitations of our work in Appendix A. We kindly encourage readers to refer to these additional experiments.

## 5 . Conclusion

In this study, we propose CaPa, an efficient framework for high-quality 3D asset generation which separates 3D geometry from 2D texture synthesis. Using multi-view guided 3D latent diffusion of the occupancy field minimizes the quality loss during mesh extraction. For texture synthesis, a spatially decoupled cross-attention addresses the Janus problem without additional training. This model-agnostic solution integrates with large generative models like SDXL \[32\] and achieves superior fidelity of the texture output. Finally, we present a novel 3D-aware occlusion inpainting algorithm, capturing 3D locality in UV space such that 2D diffusion- based inpainting effectively fills the occlusion. All these stages are fully feed-forward, making the entire generation process complete in less than 30 seconds. In summary, CaPa offers high-fidelity 3D synthesis at practical speeds, enabling immediate use in downstream applications.

\begin{tabular}{cccc}
Method & FID \(\downarrow\) & KID \(\downarrow\) & Time \(\downarrow\) \\
Ours & **55.23** & **13.46** & ∼**5 sec.** \\
Automatic View-Selection \[5\] & <u>62.31</u> & <u>15.83</u> & ∼20 sec. \\
UV-ControlNet \[59\] & 128.71 & 37.38 & ∼**5 sec.** \\
\end{tabular}

w/o Multi-view Guidance
w/o Spatially Decoupled Attention
Input
Input Render
w/ Multi-view Guidance
w/ Spatially Decoupled Attention
UV-ControlNet
Automatic View Selection
Ours
(a) Multi-View Guidance
(b) Spatially Decoupled Attention
(c) 3D-Aware Occlusion Inpainting

Input
(a) Original
(b) Inpainting
(c) w/ LoRA

Figure 7. **Ablation Study.** (a) demonstrates that using multi-view guidance significantly increases the geometry quality. (b) shows our Spatially Decoupled Attention effectively resolves the Janus problem, achieving high-fidelity texture coherence, (c) reveals our occlusion inpainting outperforms previous inpainting methods like UV-ControlNet, presented in Paint3D \[59\].

2. **Quantitative Comparison of Occlusion Inpainting.** Our 3D-aware inpainting restores occlusions with minimal semantic drift and improves contextual alignment efficiently.

Figure 8. **Scalability of CaPa.** (a) Original result of CaPa. (b) 3D inpainting result using text-prompt ("orange sofa, orange pulp"). CaPa’s texture generation extends smoothly to 3D inpainting, stylizing the generated asset. (c) CaPa w/ LoRA \[14\] adaptation. The model-agnostic approach allows CaPa to leverage pre-trained LoRA (balloon style) without additional 3D-specific retraining.

