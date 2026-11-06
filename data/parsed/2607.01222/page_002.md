<tbc>To convert these views into coherent textures, we introduce TextureOptimizer, a neural baking module that integrates dense multi-view observations while mitigating geometry inconsistencies arising from video generation. By decoupling geometry and texture synthesis and leveraging large-scale pretrained video priors, Ink3D enables significantly richer and more faithful texture generation than prior approaches.

**Keywords:** Texture generation \(\cdot\) Video generative models

## 1 Introduction

Recent years have witnessed remarkable progress in 3D generation [13-16,22, 24,25,29,30,53-56,60,64,65,67]. Inspired by the success of 2D image synthesis [7,42,52], mainstream approaches [25,54,55,67] largely adopt the latent diffusion paradigm: a 3D asset is first encoded into a compact latent space using a variational autoencoder, after which a diffusion model [13,22,53-55] is trained to model the distribution in this latent space, enabling high-quality 3D synthesis. This design has substantially advanced geometric modeling, producing plausible shapes with increasingly refined structural details.

However, despite impressive geometric quality, existing 3D generation models often struggle to synthesize _extremely complex textures_. Typical failure cases include text-rich surfaces (e.g., logos, signage, printed words), intricate clothing patterns (e.g., plaid fabrics, embroidery, layered motifs), or high-frequency decorative details. The underlying reason is straightforward: high-quality 3D training data are scarce and expensive to construct. In contrast, large-scale image and video data on the Internet exceed 3D datasets by several orders of magnitude, often reaching billions of samples. Consequently, image and video generative models [7,49,52] pretrained on such massive corpora demonstrate superior visual modeling capability and remarkable generalization, especially for fine-grained appearance and texture-rich content.

These observations inspire us to _decouple geometry and texture modeling_. Instead of forcing a single 3D generative model to learn both structure and appearance from limited 3D data, we first generate a high-quality _white-mesh_ geometry using an existing 3D generation model [54], and then leverage powerful visual generative models [49] to synthesize texture information. Finally, the generated texture is refined and baked onto the underlying geometry, producing a fully textured 3D asset.

In this work, we introduce **Ink3D**, a framework that integrates 3D generation with large-scale video generative models. Ink3D can synthesize extremely complex textures, as illustrated in Figure 1. Given a reference image, Ink3D first employs an off-the-shelf 3D generation model [54] to reconstruct the corresponding white-mesh geometry. Texture synthesis is then performed through a dedicated two-stage pipeline:

_OrbitPainter_. OrbitPainter is a conditional video generative model designed to produce dense multi-view observations of the object. Conditioned on the reference image, it generates two _360-degree orbit-scan videos_: one with horizontal<tbc>

