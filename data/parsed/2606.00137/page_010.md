<tbc>UV atlas to match each target’s geometry while preserving consistent UV coordinates. This canonical UV space gives texels a more stable semantic correspondence across instances, helping disentangle texture from shape and pose. As a result, the network can learn category-level appearance priors efficiently, using the shared template as a strong inductive bias for texture prediction. Building on this idea of category-level canonicalization, _Henderson et al._ [HTL20] proposed one of the first fully generative models that learns both shape and texture directly from collections of unpaired 2D images. Unlike Kanazawa _et al._ [KTEM18], they omit UV maps entirely, representing texture as piecewise-constant per-face colors on a fixed-topology mesh while predicting vertex positions for geometry. This yields class-consistent face correspondences that enable joint sampling of plausible geometry and appearance from the image distribution, demonstrating that coherent textured shapes can emerge from 2D supervision alone. These methods collectively established that realistic texture generation can be achieved by learning to invert the rendering process using only 2D supervision.

**Texture Super-Resolution and Completion.** Another challenge for early neural texturing pipelines was the limited resolution of reconstructed textures. Richard _et al._ [RCO\*19] and Li _et al._ [LTT\*19] addressed this problem through learned texture upsampling and refinement networks. Their CNN-based models fuse multi-view imagery and low-resolution atlases to synthesize sharper, high-frequency texture details that conventional texture- fusion pipelines often fail to recover. In parallel, Chibane and PonsMoll [CPM20] proposed to complete missing texture regions using an implicit representation: their Implicit Feature Network (IF-Net) predicts per-point texture values conditioned on partial scans, enabling plausible inpainting of unseen surfaces consistent with the geometry. These works treat texture refinement as a learnable process, moving beyond simple interpolation (_e.g._, view-dependent texture sampling [DTM96]) or seam-hiding blends and global color optimization [ZK14, WMG14, PGB03].

**Neural Texture Representations in Function Space.** Oechsle _et al._ [OMN\*19] proposed _Texture Fields_ to represent texture as a continuous neural function that maps spatial queries to RGB color (Fig. 15). This implicit formulation reduces dependence on<tbc>

<tbc>fixed UV atlases and allows resolution-independent texture definition. Texture Fields can be trained jointly with shape representations and, in generative settings, combined with adversarial training [GPM\*14] to produce high-quality renderings. Recent successors have extended this idea toward neural material representations. For example, TexGaussian [XLH\*25] proposed an octree-based 3D Gaussian representation for feed-forward PBR material generation, predicting albedo, roughness, and metallic parameters from geometry-consistent 3D features.

**Adversarial and GAN-based Texture Synthesis.** Generative Adversarial Networks (GANs) became a prominent direction in early neural texturing pipelines. Huang _et al._ [HTD\*20] introduced an adversarial optimization framework for RGB-D scans, refining noisy vertex colors by enforcing photorealism through a learned patch discriminator. By jointly optimizing texture and geometry under differentiable rendering, they achieved sharper and more consistent results than traditional photometric blending. Yu _et al._ [YDPT21] learned texture generators for ShapeNet [CFG\*15] object collections using only untextured meshes and unaligned internet photos, relying on a common UV layout per class and adversarial 2D supervision. Their network learns to populate the UV map such that renders of the textured meshes match real photographs, establishing an early class-level neural texture generation framework. 3DStyleNet [YGS\*21] disentangles geometry and texture style in latent space, allowing independent control of shape and appearance and enabling style transfer across objects. SPSG [DST\*21] extends these ideas to full indoor RGB-D scenes through a self-supervised approach that hallucinates missing geometry and surface color for large 3D scans, demonstrating neural texturing at the scene level.

**Direct Surface Texture Generation.** Later works shifted toward generating textures directly on mesh surfaces without relying on explicit UV alignment. _Texturify_ [STM\*22] is a surface-based GAN that predicts per-face colors directly on the mesh (Fig. 16). It leverages a hierarchical 4-RoSy parameterization [HZY\*19] to define orientation-consistent face convolutions, combining a mesh-face encoder with a StyleGAN2-inspired [KLA\*20] decoder. Training uses multi-view differentiable rendering from random cameras and two discriminators: an image discriminator for overall realism and

3D Model
Z
G
P
t0
Y
B
X
R
Textured 3D Model
Texture Field
G
2D Image

Real Images
Mapping Network
Real
Latent 
Shape with Predicted Texture
D
Surface Feature Encoder
StyleGAN2 Generator
D
D
Input Shape
DiffRest
Rendered Images
Fake

**Figure 15:** _An overview of TextureFields. Given a 3D shape (and optionally a reference image), the method learns a continuous texture field_ \(\unknown\) _mapping surface points_ **p** _to colors_ **c**_, producing a textured mesh. Figure reproduced from [OMN_\*_19]._

**Figure 16:** _Training pipeline of Texturify. Given an untextured input mesh, a surface-feature encoder and a StyleGAN2- based [KLA_\*_20] generator predict a texture for the mesh. The textured mesh is then differentially rendered, and the resulting images are evaluated by two discriminators (a global discriminator DI and a patch-based discriminator DP) against real images; the adversarial loss trains all networks. Figure reproduced from [STM_\*_22]._

