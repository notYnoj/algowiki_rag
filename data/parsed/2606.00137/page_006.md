where \(\sigma\) denotes volume density and **c** the view-dependent color (Fig. 7). Images are rendered via volumetric integration along camera rays [MST\*20].

Despite their strengths, neural fields present several challenges for texturing. Training and optimization can remain computationally expensive, and the learned signal may entangle lighting and material properties unless these factors are explicitly modeled, causing baked textures to capture specular highlights or shadows as albedo. In practice, neural fields and mesh-based textures are often complementary: fields excel at recovering and regularizing fine- scale appearance from images, while meshes and UV maps provide an editable and interoperable substrate for downstream use.

## 2.5.2. Vision Language Models

Vision–language models (VLMs) are neural networks trained on paired image–text data to align visual content with natural language. In contrast to vision-only encoders (which map images to features) or language-only models (which operate purely over text), VLMs learn shared cross-modal representations that support semantic alignment between modalities. In neural 3D mesh

texturing, VLMs are especially valuable because they provide (i) open-vocabulary guidance for text-driven appearance synthesis, (ii) multi-view scoring of renders that links textual intent to visual fidelity, and (iii) region- or phrase-level grounding to target specific mesh parts.

A foundational instance is _CLIP_ [R\*21], which learns dual encoders for images and text using a symmetric contrastive objective over large-scale web image–text pairs (Fig. 8). By maximizing cosine similarity for matched image–text embeddings and minimizing it for mismatched pairs, CLIP induces a shared embedding space that supports robust zero-shot recognition and has become a widely used source of supervision for text-driven stylization and texture transfer [MBOL\*22, CCL\*22, KXBP22]. _GLIP_ [LZZ\*22] extends this cross-modal alignment toward object detection and phrase grounding, producing region-aware, language-conditioned visual representations. _BLIP_ [LLXH22] further introduces a multimodal encoder–decoder framework that supports both understanding- oriented objectives (e.g., image–text matching) and generation tasks such as captioning and VQA.

## 2.5.3. Variational Autoencoders

Variational autoencoders (VAEs) [KW14] are latent-variable generative models that pair an encoder \(q_\emptyset(\mathbf{z}|\mathbf{x})\) with a decoder \(p_\emptyset(\mathbf{x}|\mathbf{z})\) and are trained by maximizing the evidence lower bound (ELBO) [JGJS99,NH98,BKM17] (Fig. 9). For a single observation \(\mathbf{x}\in\mathcal{X}\) and a latent code \(\mathbf{z}\in\mathbb{R}^d\) with prior _p_(**z**), the ELBO is

\(\mathcal{L}_\mathrm{ELBO}(\theta,\phi;\mathbf{x})=\mathbb{E}_{q_\emptyset(\mathbf{z}|\mathbf{x})}\big[\mathrm{log}p_\emptyset(\mathbf{x}|\mathbf{z})\big]-\mathrm{KL}\big(q_\emptyset(\mathbf{z}|\mathbf{x})\|p(\mathbf{z})\big),\)

where \(\mathrm{KL}(\cdot)\) denotes the Kullback–Leibler divergence [KL51]. After training, generation proceeds by ancestral sampling: one first draws **z**∼_p_(**z**) (_e.g.,_ N(**0**,**I**)) and then samples \(\mathbf{x}\sim p_\emptyset(\mathbf{x}|\mathbf{z})\).

VAEs offer a continuous latent space that supports interpolation, sampling, and, in conditional variants, controllable generation and editing. However, standard VAEs often produce overly smooth samples and can suffer from posterior collapse. Although more expressive priors and approximate posteriors [RM15, KSJ\*16] can improve results, VAEs generally fall short of GANs [GPM\*14] and diffusion models [RBL\*22] in perceptual fidelity.

5D Input Position + Direction Output Color + Density (x,y,z,0,0) (RGB)
Ray 1=
F
Ray 2
(a)
(b)

Pepper the aussie pup
Text Encoder
T1
T2
T3
TN
I1
I1 T1
I1 T2
I1 T3
I1 TTN
I2
I2 T1
I2 T2
I2 T3
I2 TTN
Image Encoder
I3
I3 T1
I3 T2
I3 T3
I3 TTN
IN
IN T1
IN T2
IN T3
IN TN

Input
Ideally they are identical.
Reconstructed input
Probabilistic Encoder
Mean
Sampled latent vector
Z
Probabilistic Decoder
x'
O
Std. dev
Z = μ + O E
An compressed low dimensional representation of the input.
E ~ N(0, I)

**Figure 7:** _An overview of Neural Radiance Fields (NeRFs). Images are synthesized by sampling 5D coordinates--3D position_ (_x,y,z_) _and viewing direction_ \((\theta,\phi)\)_--along camera rays (a) and feeding them to a neural network that outputs color_ (_R,G,B_) _and volume density_ \(\sigma\) _(b). Figure adapted from [MST\*20]._

**Figure 8:** _CLIP jointly trains image and text encoders using a contrastive loss to match paired images and texts within a batch. Figure adapted from [R\*21]._

**Figure 9:** _An overview of variational autoencoders (VAEs). A probabilistic encoder_ \(q_\emptyset(\mathbf{z}|\mathbf{x})\) _maps an input_ **x** _to a Gaussian latent distribution parameterized by_ \((\mu,\sigma)\)_; a latent sample_ \(\mathbf{z}=\mu+\sigma\odot\epsilon\) _with_ \(\epsilon\sim\mathcal{N}(\mathbf{0},\mathbf{I})\) _is then decoded by_ \(p_\emptyset(\mathbf{x}|\mathbf{z})\) _to reconstruct_ \(\mathbf{x}'\approx\mathbf{x}\)_. The model is trained by maximizing the evidence lower bound (ELBO) L<sub>ELBO</sub> (see Sec. 2.5.3). Figure reproduced from [Wen18]._

