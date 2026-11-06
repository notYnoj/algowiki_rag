<tbc>adopts a coarse-to-fine design that first diffuses appearance in surface point space to obtain a globally consistent prior, then projects it into UV space and refines a high-resolution texture atlas, helping reduce seams and UV-fragmentation artifacts. More recent feed- forward models continue to broaden this design space. For example, UniTEX [LLC\*25] moves beyond purely UV-based processing by lifting texture generation into a unified 3D functional space, while Material Anything [HWLW25] targets physically based material generation, predicting not only albedo but full PBR material maps for a given 3D object.

Feed-forward models have also explored alternative representations. UV-free Texture Diffusion [FZB24] bypasses UV maps entirely by operating on colored point clouds and using heat diffusion over the mesh surface. Its UV3-TeD framework models each surface as a point set with a learnable latent field, enabling texture generation directly on the mesh without a fixed UV parameterization and thereby avoiding seam- and distortion-related issues associated with UV maps. Likewise, Single-Mesh Diffusion [MEM24] learns field latents attached to mesh vertices and trains a diffusion model to generate these latent codes, which are then decoded to colors. Under a feed-forward generation setting for a given trained asset, this enables rapid, view-consistent synthesis of many texture variants when the geometry is known. Another notable work, AlignTex [ZXW\*25], addresses the challenge of generating textures that precisely match concept art or reference images of a 3D asset. It employs a diffusion-based two-stage pipeline with alignment losses and transformer-based conditioning to enforce pixel-level correspondence between multi-view artwork and the generated UV map, yielding pixel-precise rather than style-consistent texture synthesis.

Consequently, diffusion-based texturing has rapidly advanced from slow per-mesh optimization [PJBM23, WLW\*23] to fast feed-forward generation [HWLW25]. Iterative methods built on the idea of leveraging 2D diffusion models for 3D texture painting [CSL\*23, RMA\*23], and they remain attractive for their simplicity (no model retraining) and controllability (one can intervene at each view). However, they may still produce seams or inconsistent details, since each view is processed sequentially. Synchronized multi-view diffusion [LXLW24, CKF\*23] significantly alleviates this issue: by treating all views (or the UV map) as a joint diffusion task, these methods encourage the texture to evolve coherently across the surface. The cost is higher memory usage and, in some cases, the need for custom diffusion pipelines, but the ben<tbc>

<tbc>efit is improved quality on challenging cases (intricate objects, full scenes) where view-by-view approaches often struggle with misalignment. Feed-forward approaches [ZXW\*25] push this further by directly mapping text (and other inputs) to the texture domain, often without explicit view-by-view rendering during inference. This yields substantial speedups and opens the door to zero-shot and generative applications, such as texturing large numbers of objects with diversity.

A core challenge for feed-forward models is the distribution of training data. Large diffusion-based texture models are often trained on synthetic datasets or broad 3D asset collections (_e.g._, ShapeNet [CFG\*15] or Objaverse [DSS\*23, D\*23]), which may not fully reflect the visual richness of real-world textures. As a result, their outputs may still fall short of the photorealism of real imagery. For instance, a model trained purely on synthetic stylized assets might produce textures with a telltale "CGI" look. Current feed-forward models such as Material Anything [HWLW25] and TEXGen [HGZ\*24] already exhibit coherent results, but slight domain gaps remain in high-frequency detail and material realism. One promising direction is to combine the strengths of synthetic and real data, _e.g._, using large synthetic datasets to learn geometry- to-texture alignment while leveraging real image data to improve appearance realism and material properties. Some recent works have moved in this direction by incorporating real-image losses or conditioning signals: Material Anything [HWLW25] integrates rendering-based losses to encourage physical realism, while FabricDiffusion [ZWC\*24] uses real fashion photographs as inputs.

## 4.4. 3D Humans Texturization

Texturing human avatars merits separate discussion, since the underlying assumptions, constraints, and objectives differ from those of general object texturing. First, representation priors differ: many modern human texturing methods build on parametric body models (_e.g._, SMPL/SMPL-X [LMR\*15,PCG\*19]) with fixed topology and canonical UV atlases, providing consistent surface correspondences across poses [LMR\*15,PCG\*19]. In contrast, general object texturing often lacks such canonical parameterization.

Second, human identity and anatomy impose distinctive constraints: faces, hands, and skin carry fine-grained, identity-defining cues (freckles, lip color, _etc._) that must be preserved for realism and recognition. Accordingly, many methods incorporate face- specific priors or losses (_e.g._, a facial UV refinement network or an identity loss) to capture such high-frequency details [OLY\*17, DCX\*18, WZL\*19]. Moreover, several works segment the texture or mesh into semantic parts and apply part-specific models or losses [CSST21].

Third, the data and evaluation protocols are domain-specific: human texturing methods typically train on specialized datasets such as artist-modeled digital humans, 3D scans, or multi-view captures [LZT\*24, LIPM19], since fully paired ground-truth textures remain scarce. Evaluation also relies on human-centric metrics, including identity preservation (_e.g._, face-ID or person re- identification [WZL\*19]) and part-aware image fidelity measures such as PSNR or LPIPS computed on rendered views or aligned texture regions [CSST21].

X1
X mask
X1
Skip-Connections
Hybrid Blocks
Hybrid Blocks
VL
Diffusion Loss with v-prediction
Add noise
Rasterization
Projection
x0
a small bird
Condition Embedding
x0
S
Diffusion at the Time-step

**Figure 21:** _A feed-forward texturing pipeline (TEXGen). A diffusion U-Net denoises a latent UV texture atlas conditioned on rasterized mesh cues and text embeddings to generate a UV texture map in a single pass. Figure reproduced from [YYG\*24]._

