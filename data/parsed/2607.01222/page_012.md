<tbc>textures. The model is initialized from Wan-2.2-14B \[49\]. The geometry-aware spatial attention module is initialized using the weights of the corresponding full-attention layers. During training, we adopt LoRA-style fine-tuning with a rank of 32. Optimization is performed using the AdamW \[35\] optimizer with a learning rate of 1e-4. The model is trained for 45k iterations with a batch size of 1 on 8\(\times\) NVIDIA A100 GPUs. Unless otherwise specified, we generate two orbit-scan videos for each object: one with horizontal camera rotation and one with vertical rotation. Each video has a resolution of 512 \(\times\) 512 and contains 61 frames. Additional implementation details are provided in the appendix.

**Evaluation Data.** We select 85 high-quality samples from the Texverse \[65\] dataset. As our focus is on generating highly complex textures, the original assets in Texverse do not sufficiently meet this requirement. Therefore, for each sample we retain only its geometry and discard the original texture. We then render the frontal-view projection of the white mesh and feed it into the commercial image generation model Nano Banana to synthesize a reference image with complex textures. As a result, for each of the 85 samples we obtain a pair consisting of a white-mesh geometry and a corresponding reference image that exhibits rich and complex textures.

**Evaluation Metrics.** For each of the 85 samples, we provide its ground-truth geometry and the reference texture image to our method as well as the compared methods to generate textured 3D assets. We then render the front-view projection of each generated asset and compute several image-level metrics against the reference image. Specifically, we report _FID_, _CLIP-FID_, _LPIPS_, and _CLIP-I_. FID measures the Fréchet distance between the feature distributions of generated images and reference images in the Inception feature space, reflecting overall visual quality and realism. CLIP-FID replaces the Inception features with CLIP features, providing a metric that better captures semantic alignment with the reference. LPIPS measures perceptual similarity between two images based on deep features, reflecting low-level visual fidelity. Finally, CLIP-I computes the cosine similarity between CLIP image embeddings of the generated image and the reference image, evaluating semantic consistency between them.

## 4.1 Main Results

1 presents a quantitative comparison between Ink3D and several representative open-source approaches capable of generating textures given a white-mesh

\begin{tabular}{ccccc}
Method & FID\(\downarrow\) & CLIP-FID\(\downarrow\) & LPIPS\(\downarrow\) & CLIP-I\(\uparrow\) \\
Paint3D \[61\] & 146.0 & 570.6 & 0.3417 & 0.7980 \\
TEXGEN \[59\] & 123.7 & 291.8 & 0.2280 & 0.8409 \\
SeqTex \[60\] & 148.3 & 387.9 & 0.2601 & 0.8052 \\
Trellis-2 \[54\] & 120.4 & 223.9 & 0.2714 & 0.8694 \\
Ink3D (Ours) & 103.7 & 195.6 & 0.2029 & 0.8979 \\
\end{tabular}

** 1:** Quantitative comparison of texture synthesis quality. Our primary competitor is Trellis-2, a recently released state-of-the-art 3D generation model. Ink3D significantly outperforms Trellis-2 and other existing open-source approaches in texture synthesis.

