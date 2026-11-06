<tbc>in a single pass, these methods typically require many optimization and denoising steps per shape. Even with accelerations such as _latent-space distillation/optimization_ [MRP\*23] or _efficient differentiable rendering_ [LHK\*20,NDVZJ19,JSRV22,RRN\*20], texturing a single model can still take several minutes, making these approaches costly, especially for time-sensitive or large-scale applications without substantial compute. Nonetheless, optimization- based texturing opened a new frontier: by leveraging powerful 2D priors, it enables automatic texture generation at a level of detail and semantic richness that was previously difficult to achieve. Ongoing research seeks to reduce runtimes through _better initialization and staged pipelines_ [LGT\*23], _parallelism across views_, and _hybrid learning-optimization designs_ that combine generative priors with render-and-backprop refinement [DOW\*24, YHK\*24]. At the same time, work on _creative control—e.g._, localized edits and procedural/material parameter optimization--has expanded user control over where and how edits are applied [DLAH24, ZPX\*24, GZD\*23]. In this sense, combining differentiable rendering with powerful vision-language and diffusion priors remains a compelling paradigm for high-quality 3D mesh texturing.

## 4.3. Accelerated Diffusion-based Texturing

Early works demonstrated that 2D diffusion models can be used to optimize 3D textures (_e.g._, by score distillation [PJBM23]). While these optimization-based methods achieve impressive results, they come at the cost of lengthy per-object optimization (often tens of minutes). The need for faster, more scalable approaches motivated a new class of methods that avoid costly test-time optimization by instead using diffusion models in one of three ways: (1) iterative view-by-view painting with a frozen 2D diffusion prior, (2) synchronized multi-view generation that diffuses all views concurrently, or (3) feed-forward texture synthesis in which a custom diffusion model directly outputs a full texture map.

**Iterative Texturing.** A widely adopted pipeline "paints" the mesh one view at a time in a loop: (i) render the current viewpoint with geometric cues (_e.g._, depth or normals); (ii) use a pretrained image diffusion model to synthesize an image consistent with the current view and prompt; (iii) back-project the synthesized colors onto the UV map using visibility; and (iv) update a per-texel progression mask before moving to the next view [RMA\*23, CSL\*23]. Dynamic keep/refine/generate masks guide denoising toward un<tbc>

<tbc>painted or low-confidence regions while protecting already generated high-quality textures, progressively covering the UV space across multiple views [RMA\*23, CSL\*23] (Fig. 19). Many implementations also include a final seam-refinement pass to clean residual discontinuities along chart boundaries [CSL\*23]. In practice, this iterative scheme can yield high-quality textures without fine-tuning the diffusion backbone, although minor seams, color drift, or incomplete coverage may remain across view boundaries [RMA\*23, CSL\*23].

Several works build on the iterative painting paradigm for specialized scenarios. EASI-Tex [PWMAZ24] targets single- image texture transfer: given a reference photo, it uses an IP- Adapter [YZL\*23] to diffuse the photo’s texture onto a 3D shape. It also showed that geometric edges yield more structurally accurate textures than depth or normals. Paint3D [ZCQ\*24] follows a coarse-to-fine strategy: it first samples a pretrained diffusion model to obtain a coarse texture, then uses custom UV-space diffusion models to upsample, inpaint missing regions, and remove baked-in lighting. In the interest of speed, Make-A-Texture [XGF\*25] optimizes the diffusion model and introduces a specialized backprojection algorithm that generates a full texture in only 3 seconds, trading some detail for significant speed gains. Iterative pipelines have also been adapted to complex scenes: InstanceTex [YGC\*24] textures multi-object scenes instance by instance while aiming to maintain global coherence, whereas RoomTex [WLX\*24] unwraps indoor scenes into panoramas for an initial global pass, then iteratively inpaints each object with panoramic guidance to mitigate inter-object style inconsistencies. Despite these advances, iterative methods can still exhibit minor seams or blur due to view-wise generation, though they remain far faster and more practical than per- mesh optimization, requiring a fixed number of diffusion denoising steps per view instead of long gradient-based optimization.

**Synchronized Texturing.** Another approach is to generate all views simultaneously. Synchronized multi-view texturing methods perform a joint diffusion process across multiple camera views, sampling all views together at each denoising step and aggregating their latent updates onto a common texture representation to promote globally consistent results [CKF\*23, LXLW24, SXSX25]. By<tbc>

Colorful polo shirt
Superman emblem
Tie-dye apron
Muay Thai shorts

textured mesh
preset viewpoint
render & generate
reader & generate
mesh
mesh
preset viewpoint
mesh
texture
back-project
texture
generated texture
Generation

**Figure 18:** _Given a text prompt, 3D Paintbrush predicts both the target region and corresponding texture on the input mesh, enabling spatially controlled texturing. Figure adapted from [DLAH24]._

**Figure 19:** _An overview of an iterative texturing pipeline. The mesh is rendered from preset viewpoints, a text-to-image model generates view-consistent appearances, and the results are back-projected to update the texture map, iterating across views. Figure adapted from [CSL\*23]._

