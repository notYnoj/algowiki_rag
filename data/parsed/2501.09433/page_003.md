### 2.3 . Texture Generation

Numerous texture generation algorithms have recently been developed with the success of 2D generative diffusion models. Common approaches \[5, 35\] utilize iterative processes, first rendering depth maps and then generating corresponding images for multiple viewpoints. However, these methods mainly encounter multi-view consistency issues. Recognizing this challenge, recent approaches \[9, 17, 41, 59\] often focus on synchronized output within a limited number of views, typically 4 or 6 orthogonal viewpoints, to improve alignment throughout the entire model.

Despite these impressive results, the limited number of views inevitably yields occlusions, leading to incomplete textures. Aware of this problem, various strategies have been explored, especially for inpainting using ControlNet in UV space \[41, 59\]. However, these solutions frequently introduce locality biases in UV space, which do not accurately reflect the 3D once mapped onto a 2D Cartesian plane. As a result, such methods often produce degraded details in occluded areas, compromising texture coherence.

Concurrent work, MVPaint \[6\], has similarly identified these limitations, suggesting surface-based extrapolation as a potential solution. In contrast, we address this issue using 3D- aware occlusion inpainting, which preserves texture fidelity and enhances overall consistency.

## 3 . Methodology

This section introduces CaPa, a novel 3D asset generation framework. CaPa operates in two stages: (1) 3D geometry synthesis using multi-view guided 3D latent diffusion and (2) 2D texture generation via 2D latent diffusion. First, we generate a 3D geometry by leveraging multi-view guided 3D latent diffusion to capture structural details from diverse perspectives. Second, to create an initial texture, we synthesize four orthogonal view images along the generated mesh. The untextured regions, caused by occlusions, are then completed using a 3D-aware inpainting algorithm to ensure a seamless appearance across all surfaces. Both stages are aligned through shared multi-view images, ensuring consistent geometry and texture. Using a fully feed-forward approach, the entire 3D asset generation process is completed in less than 30 seconds. Figure 2 illustrates the CaPa pipeline.

### 3.1 . Geometry Generation via 3D Latent Diffusion

For 3D geometry generation, we leverage the recently proposed ShapeVAE to model the distribution of 3D geometry, while ensuring alignment with both image and text latent spaces. Using ShapeVAE, we train a 3D latent diffusion model \[36\] guided by multi-view (MV) images to achieve better alignment with texture generation. This MV- conditioned 3D latent diffusion model can efficiently generate high-quality 3D shapes, even under complex scenarios.

### 3.1.1 Latent Space for Geometry Representation

We adopt a perceiver-based encoder that captures essential 3D geometric features, in line with Michelangelo \[63\]. The encoder is trained to reconstruct neural fields from input point clouds, ensuring efficient representation learning.

**Shape Encoder.** Given a ground-truth 3D shape, we aim to encode it into a latent representation, **E**_<sub>s</sub>_. First, we sample points from the surface \(\mathbf{P}\in\mathbb{R}^{N\times 3}\), along with their corresponding normal vectors **n**. These points and normals are then processed using cross-attention mechanisms that incorporate Fourier encodings and spherical harmonics to capture fine geometric details.

**Shape Decoder.** The perceiver-based decoder D reconstructs the neural field from latent embeddings **E**_<sub>s</sub>_. Given a query point \(\mathbf{p}\in\mathbb{R}^3\) and **E**_<sub>s</sub>_, the decoder predicts the occupancy value for each point. The reconstruction process is optimized using binary cross-entropy (BCE) loss,

\(\mathcal{L}_\text{vae}=\mathbb{E}_{\mathbf{p}\in\mathbb{R}^3}\left[\text{BCE}\left(\hat{\mathcal{O}}(\mathbf{p}),\mathcal{D}\left(\mathbf{p}|\mathbf{E}_s\right)\right)\right]+\lambda_\text{kl}\mathcal{L}_\text{kl}\) (1)

where \(\hat{\mathcal{O}}(\mathbf{p})\) represents the occupancy prediction for the query point **p**, and L<sub>kl</sub> for KL divergence regularization.

### 3.1.2 Multi-View Guided 3D Latent Diffusion

Leveraging the learned latent space, we employ a 3D latent diffusion model to generate geometry. However, due to its reliance on the latent space learned by ShapeVAE, this model often demonstrates limited geometric understanding. Moreover, establishing a unified generation pipeline requires consistency between the generated shape and texture.

To address these challenges, we train a multi-view guided 3D latent diffusion model that incorporates richer geometric priors and maintains alignment between shape and texture. Specifically, we use an off-the-shelf MV diffusion model to generate a set of multi-view images \(\hat{\mathbf{I}}\) from the input condition (_e.g._, an image or text). This guidance provides stronger priors for 3D shape generation, ensuring improved alignment with texture synthesis in subsequent steps.

Finally, we train the multi-view guided 3D diffusion model \(\epsilon_\theta\). The training objective follows the standard reverse denoising process of latent diffusion \[12, 36, 42\]:

\(\mathcal{L}_{3\text{D-LDM}}:=\mathbb{E}_{\epsilon\sim\mathcal{N}(0,1),t}\left[\|\epsilon-\epsilon_\theta\left(\mathbf{E}_s,t,\tau_\theta(\hat{\mathbf{I}},\pi)\right)\|_2^2\right]\) (2)

where \(\tau_\theta\) extracts camera embeddings from the multi-view images \(\hat{\mathbf{I}}\) to incorporate camera-specific parameters \(\pi_i\).

After applying the Marching Cubes \[26\] to extract a 3D mesh from the occupancy field, we employ a robust remeshing process to ensure smooth and high-quality manifold geometry. We carefully design the post-processing<tbc>

