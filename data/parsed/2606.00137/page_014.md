<tbc>parallelizing view synthesis, such methods can reduce runtime and improve consistency, since texture evolves jointly across views and overlapping boundary regions are encouraged to agree [CMZ\*25]. One of the first such approaches, TexFusion [CKF\*23], introduced multi-view latent fusion in which the diffusion denoiser operates on several rendered views concurrently, and the predicted 2D latent features are aggregated onto a shared latent texture map. The final RGB texture is then recovered by optimizing an intermediate neural color field on decoded renders of that latent texture, yielding globally coherent results without the long per-object optimization used in earlier SDS-based pipelines.

Building on this idea, GenesisTex [GJL\*24] performs diffusion directly in texture space, maintaining one latent texture map per viewpoint during denoising and dynamically aligning them to ensure cross-view coherence. It further introduces style-consistency mechanisms and latent alignment to enforce a unified appearance across viewpoints. A related method, MVPaint [CMZ\*25], also generates all views simultaneously using synchronized multi-view diffusion, but follows this with 3D inpainting and UV-space refinement to fill unobserved regions and reduce cross-view inconsistencies, producing seamless high-resolution textures.

Many other recent works adopt synchronized diffusion to improve multi-view consistency. TexPainter [ZPZ\*24] enforces multi- view consistent text-to-texture synthesis using a pre-trained latent diffusion model by jointly denoising multiple views. At each DDIM step, the predicted noiseless states are decoded to images, fused in color space into a common texture, and the fusion objective is back-propagated to the view latents, relaxing sequential dependencies and improving cross-view consistency and quality (Fig. 20). RomanTex [FYY\*25] improves geometry- and image- aligned multi-view diffusion for texturing via a 3D-aware rotary positional embedding and a decoupled attention design (reference attention plus multi-view attention), strengthening cross-view coherence before baking to UV space. VCD-Texture [LYC\*24] goes further by introducing a 3D-2D collaborative denoising framework that aggregates multi-view 2D latent features into 3D space and rasterizes them back to produce more consistent 2D predictions. This coupling yields highly stable textures, as the 2D diffusion is continuously guided by a holistic 3D representation and vice versa. MaterialMVP [HYY\*25a] extends synchronized multi-view diffusion<tbc>

<tbc>to _PBR_ outputs by jointly generating view-consistent albedo and metallic–roughness maps, using consistency-regularized training to suppress illumination artifacts and multi-channel aligned attention to keep the predicted maps spatially aligned. Meanwhile, GenesisTex2 [LZZ\*25] extends GenesisTex [GJL\*24] with improved stability and quality by introducing local attention reweighting in the diffusion model’s self-attention layers, ensuring that spatially corresponding patches across views remain strongly correlated. It further merges latent features across views at multiple stages to enforce consistency without compromising diversity.

More recently, SeqTex [YYS\*25] leverages video diffusion priors to strengthen cross-view coherence in synchronized texturing. It formulates mesh texturing as _sequence generation_ and jointly models multi-view renderings and UV textures using geometry- informed attention. By coupling view-space and UV-space generation within a unified framework, it produces complete UV texture maps end-to-end and reduces reliance on post-hoc baking or fusion.

Overall, synchronized approaches demonstrate that parallel multi-view generation greatly enhances texture consistency. By jointly denoising all views through shared latent variables or cross- view interactions, these methods substantially reduce seams. However, UV-space fusion can behave like an averaging operation: if applied too strongly throughout the full denoising trajectory, it can suppress high-frequency details and yield over-smoothed (blurry) textures [LXLW24]. As a result, synchronization is often emphasized in early (high-noise) timesteps to align global layout and color, and relaxed in later timesteps to preserve fine details; but once coupling is weakened, per-view updates can drift and residual inconsistencies may still arise, especially in low-overlap or occluded regions, often motivating downstream 3D/UV refinement (_e.g._, MVPaint [CMZ\*25]). The main trade-off is higher memory consumption--since multiple views are diffused simultaneously-- and, in some cases, the need for custom synchronization mechanisms or additional guidance modules (_e.g._, GenesisTex [GJL\*24], FlexiTex [JYZ\*25]). Nevertheless, synchronization leverages the diffusion model’s global coherence to produce seamless textures that are difficult to achieve with strictly view-by-view strategies [CSL\*23,RMA\*23].

**Feed-Forward Texturing.** To avoid per-instance optimization, one solution is to train a diffusion model that directly generates the full texture representation in a single pass, without requiring view- by-view rendering during inference. Many current feed-forward texturing methods operate in UV space, allowing occluded regions to be textured since the full surface is visible to the model. This design avoids view-by-view processing and stitching, but typically requires large datasets of textured 3D objects [DSS\*23,D\*23], which have only recently become available (Fig. 21).

TEXGen [YYG\*24] is a 700M-parameter diffusion model trained to generate \(1024\times 1024\) UV maps for meshes across diverse categories. Its architecture interleaves 2D convolutions on the UV map with self-attention over a 3D point-cloud representation of the mesh, injecting 3D structural awareness into 2D texture generation. Once trained, TEXGen can synthesize diverse, high- resolution textures in a single forward pass conditioned on text or reference images. Related feed-forward diffusion models also couple 3D and UV-space reasoning: Point-UV Diffusion [YDL\*23]<tbc>

C
Denoised Views
Noised Views
Diffusion Process
C
C
Color-Fused Texture Image
DDIM
Decoder
Renderer
Decoder
L diff
Blend
Zi 0.M
Zi 0.M
DDIM
Decoder
Renderer
Decoder

**Figure 20:** _An overview of a synchronized multi-view texturing pipeline. Per-view diffusion denoising is coupled through a_ Blend _module that fuses per-view textures into a shared texture image, improving cross-view consistency. Figure reproduced from [ZPZ\*24]._

