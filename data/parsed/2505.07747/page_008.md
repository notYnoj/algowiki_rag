<tbc>processing as illustrated in Fig. 4. In the dual-stream blocks, latent tokens and condition tokens are processed separately with their own QKV projections and MLPs, but they still interact through cross- attention. In contrast, single-stream blocks combine both types of tokens and process them jointly using parallel spatial and channel attention mechanisms. This hybrid approach allows flexible feature learning while maintaining efficient cross-modal interaction. Notably, to effectively introduce spatial position information in different noise patches, FLUX.1 employs rotary position encoding (RoPE) to encode spatial information within each noise patch. Since our ShapeVAE’s latent sets representation lacks explicit spatial correspondence, we remove positional embeddings for the latent sets S and retain only timestep embeddings for modulation purposes. For single-image conditioned shape generation, we leverage a pre-trained DINOv2 large image encoder [56] with registers [15] to extract conditional tokens from preprocessed 518\(\times\)518 resolution images - where we perform background removal, object centering/resizing, and white background filling to enhance effective resolution and minimize background interference. To capture both semantic and global image characteristics, we concatenate complementary features from CLIP-ViT-L/14 [64]. These combined features are then injected through parallel cross-attention mechanisms within each flow block, enabling simultaneous processing of both global and local visual information.

## 3.3 More flexible control for 3D generation

Building upon the structural advantages of our VAE with Diffusion framework - which mirrors contemporary text-to-image architectures - we achieve seamless transfer of 2D controllable generation techniques (e.g., ControlNet, IP-Adapter) and parameter-efficient adaptation methods like LoRA to 3D mesh synthesis. As demonstrated by CLAY [92] in exploring ControlNet-UNet combinations for 3D generation, we systematically implement these control mechanisms within our Step1x-3D framework and support diffusers community <sup>2</sup>. To efficiently incorporate conditional signals while preserving the pre-trained model’s generalization ability, we can introduce an additional Condition Branch using the ControlNet-like strategy or LoRA. During the current open-source phase, we implement LoRA for geometric shape control using label as reference examples. This lightweight solution achieves domain-specific fine-tuning with minimal resource overhead while preserving the original feature space integrity, resulting in controllable shape generation. We first annotate each mesh with geometric attributes, such as symmetry or level of geometric detail. Using these annotations, we can train an additional LoRA module rather than fine-tuning the entire network, enabling the model to utilize these labels for controlling object geometry. This LoRA adaptation exclusively to the Condition Branch, enabling efficient injection of conditional signals without compromising the pretrained model’s capabilities. We will also plan introduce updates in later stages to incorporate fine-tuning through skeleton, bounding box (bbox), caption, and IP-image conditions.

<sup>2</sup>https://huggingface.co/docs/diffusers/index

Optional Conditions
Double Stream Block
Timestep
Noisy Latent
"Caption..."
B-Box
Skeleton
Time
Noise
Image
Optional Cond.
Image
Text
Feed Forward
Cond. LoRA
MLP
MLP
MLP
MLP
MLP
MLP
LayerNorm + Scale & Shift + MLP
Double Stream Block x N
Cond. LoRA
Output Latent
Cond. Latent
Single Stream Block
Single Stream Block x N
Cond. LoRA
Noise Latent
Time
Output Latent
LayerNorm + Scale & Shift + MLP
Feed- Forward
Self- Attention
LayerNorm + Scale & Shift + MLP
3D Geometry
Cond. LoRA

Figure 4: **Step1X-3D geometry diffusion framework**. The framework enables seamless integration of diverse conditions, allowing fine-tuning for various downstream tasks.

