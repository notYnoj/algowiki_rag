pipeline to address common meshing challenges, such as aliasing and non-manifold structures. This remeshing strategy also supports artist-preferred quadrilateral meshes and high-resolution UV-mapped textures. For a comprehensive discussion, please refer to Appendix C.1.

## 3.2 . Texture Generation for Input Geometry

For texture generation, we first render four orthogonal views of the generated mesh, which serve as the input for texture synthesis. Ensuring texture consistency across these multiple views is critical but inherently challenging, as traditional approaches often struggle with the Janus problem.

A conventional solution for multi-view texture generation involves using MVDiffusions with geometry-guidance ControlNet \[61\], as suggested in CLAY \[62\] and MVPaint \[6\]. However, these approaches encounter several limitations: the output resolution for each view in MVDiffusion models typically remains constrained to a low 256-pixel resolution, resulting in suboptimal visual fidelity. Additionally, existing MVDiffusions rely on modified U-Net \[37\] architectures that differ from the original 2D latent diffusion model \[36\], thus precluding the reuse of pre-trained ControlNet and necessitating resource-intensive retraining.

### 3.2.1 Spatially Decoupled Cross Attention

In response to these challenges, we introduce the _Spatially Decoupled Cross Attention_, a model-agnostic approach that amplifies multi-view information. To ensure texture<tbc>

<tbc>consistency, we first concatenate the rendered images into a single batch and synthesize textures for all views simultaneously. Feature channels are then replicated and assigned to view-specific guidance, allowing each channel to focus on its respective spatial region.

**View-Specific Feature Enhancement.** For a hidden feature \(h_t\in\mathbb{R}^{C\times W\times H}\) at time step _t_, we split the feature channels into positive _h<sub>f</sub>_ and negative components _h<sub>b</sub>_, both of size \(h_f,h_b\in\mathbb{R}^{C/2\times W\times H}\). These features are then replicated across the _N_ views:

\(\tilde{h}_t=\big[\underbrace{h_f,\dots,h_f}_N|\underbrace{h_b,\dots,h_b}_N\big]\in\mathbb{R}^{CN\times W\times H}.\) (3)

Then, we independently encode each low-quality multi-view guide image and combine them into a unified feature vector:

\(\tilde{g}=\big[g_f^1,\dots,g_f^N|g_b^1,\dots,g_b^N\big]\in\mathbb{R}^{CN\times F}.\) (4)

The combined feature \(\tilde{g}\), together with replicated hidden states \(\tilde{h}_t\), undergoes cross-attention,

\(Z=\text{XAttn}(\tilde{g},\tilde{h}_t)\) (5)

As a result of the attention, each channel group focuses on its designated view, preserving view-specific information. Finally, we aggregate the features corresponding only to the spatial region of the _i_-th view, ensuring that the guidance is attended to only in its respective region. Figure 3 illustrates the spatially decoupled attention mechanism.

3D Latent Diffusion
Es
Shape latent
MVDiffusion
Input
3D Geometry
Image1: Geometry Generation
Image2: Texture Generation
Back-Projecting
3D-Aware Occlusion Inpainting
2D Latent Diffusion w/ Spatially Decoupled Attention
Final Textured Mesh
High-Quality MV images w/o Janus
Rendered Input

Figure 2. **CaPa pipeline**. We first generate 3D geometry using a 3D latent diffusion model. Using the learned 3D latent space with ShapeVAE, we train a 3D Latent Diffusion Model that generates 3D geometries, guided by multi-view images to ensure alignment between the generated shape and texture. After the 3D geometry is created, we render four orthogonal views of the mesh, which serve as inputs for texture generation. To produce a high-quality texture while preventing the Janus problem, we utilize a novel, model-agnostic spatially decoupled attention. Finally, we obtain a hyper-quality textured mesh through back projection and a 3D-aware occlusion inpainting algorithm.

