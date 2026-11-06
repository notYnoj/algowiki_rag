## 3 Ink3D

**Problem tion.** We adopt a geometry-first, texture-second paradigm for 3D asset generation. Given a reference image **_I_**, we first employ an off-the- shelf 3D reconstruction model \[54\] to estimate a white-mesh geometry G, which captures the object’s structural shape without texture. The objective of Ink3D is to generate a high-quality texture consistent with **_I_** and map it onto G, resulting in a fully textured 3D asset.

**Overview.** Ink3D consists of two key components:

1. _OrbitPainter_ (Section 3.1). OrbitPainter (Figure 2) is a conditional video generative model that incorporates a newly proposed Geometry-Aware Sparse Attention module (Section 3.2). Given the reference image **_I_** and the white- mesh geometry G, it synthesizes two orbit-scan videos of the object: a horizontal orbit video **_V_**_<sub>H</sub>_ and a vertical orbit video **_V_**_<sub>V</sub>_. These videos ensure comprehensive viewpoint coverage while maintaining appearance consistency with **_I_**, and geometry consistency with G.<tbc>

2. _TextureOptimizer_ (Section 3.3). TextureOptimizer (Figure 3) consolidates frames from the generated orbit videos to bake textures onto G. It explicitly mitigates geometric inconsistencies arising from imperfect video generation and resolves the challenges of dense multi-view texture fusion, resulting in a coherent and high-fidelity texture map.

### 3.1 OrbitPainter

**Training Data Pre-Processing.** As illustrated in Figure 2(a), given a textured 3D asset from the training set, we first randomly sample a viewpoint and apply random lighting, then render a static image as the reference image **_I_**. We subsequently predefine two camera orbit trajectories: a horizontal scan and a vertical scan. For each trajectory, we render multiple modalities to construct supervision signals.

- _Horizontal Scan._ Along the horizontal orbit trajectory, we render: (1) an RGB video \(\mathbf{V}_H^{RGB}\), (2) a surface-normal video \(\mathbf{V}_H^{Normal}\), and (3) a 3D- position video \(\mathbf{V}_H^{Pos}\). Note that each video consists of 61 frames by default and is rendered at a resolution of \(512\times 512\).<tbc>

**-** _Vertical Scan._ Similarly, along the vertical orbit trajectory, we render the corresponding RGB, surface-normal, and 3D-position videos: \(\mathbf{V}_V^{RGB}\), \(\mathbf{V}_V^{Normal}\), and \(\mathbf{V}_V^{Pos}\).

The horizontal and vertical scans provide complementary viewpoint coverage and multi-modal geometric supervision for training.

**Latent Extraction.** Since we adopt a latent video diffusion model as the backbone, we first encode all rendered videos into latent representations. Specifically, we extract latents from \(\{\mathbf{V}_H^{RGB},\mathbf{V}_H^{Normal},\mathbf{V}_H^{Pos},\mathbf{V}_V^{RGB},\mathbf{V}_V^{Normal},\mathbf{V}_V^{Pos}\}\). We employ the WAN 2.2 \[49\] video VAE encoder, which uses a spatial downsampling

