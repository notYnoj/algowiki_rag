<tbc>to enforce view consistency and geometric alignment; (2) a texture-space synchronization module integrated within the denoising process to maintain cross-view coherence through latent space alignment; and (3) texture completion via multi-view back-projection with subsequent texture-space inpainting to address occlusion artifacts and generate seamless UV maps. This hierarchical approach ensures both geometric fidelity and photometric consistency throughout the texture generation pipeline.

In summary, the key contributions of this technical report are threefold:

• We present a comprehensive data curation pipeline that provides insights into 3D asset characteristics while enhancing generation fidelity.<tbc>

• We propose Step1X-3D, a 3D native generation framework that decouples geometry and texture synthesis. It produces topologically-sound meshes with geometrically-aligned textures, while enabling enhanced controllability through image and semantic inputs. The full framework - including base models, training code, and LoRA-based adaptation modules - will be open-sourced to benefit the 3D research community.<tbc>

• Extensive comparative experiments demonstrate that Step1x-3D surpasses existing open- source 3D generation approaches in asset quality while achieving performance comparable to proprietary state-of-the-art solutions.

## 2 Related work

### 2.1 Optimization-based 3D Generation

Optimization-based 3D generation is a framework where 3D representations and their optimization procedures are independently defined across distinct objects, enabling text-to-3D synthesis through input prompts. This approach incorporates diverse 3D representations, ranging from geometric primitives (e.g., voxels, meshes [4]) to advanced neural representations such as Neural Radiance Fields (NeRF) [54] and 3D Gaussian Splatting (3D GS) [32]. Text prompts are encoded into pre- trained models (e.g., CLIP [59], Stable Diffusion [62] and etc) to extract semantic-aligned 2D visual features, which supervise the multi-view consistency of rendered 3D representations via differentiable rendering pipelines. By iteratively optimizing geometric and appearance parameters through gradient- based alignment of 2D supervision, the framework achieves cross-modal (text-to-3D) consistence and produces 3D assets. These optimization-based 3D generation methods [30, 64, 58, 8, 97], while capable of processing arbitrary text prompts, suffer from limited support for image-conditioned inputs and inherent limitations such as prolonged optimization cycles, poor generalization of trained parameters and inferior generation quality. These shortcomings critically hinder their practical deployment and scalability in real-world applications.

### 2.2 Feed-forward 3D Generation

To enhance generation efficiency and quality, feed-forward 3D generation methods have emerged as a promising alternative. Specifically, feed-forward methods aim to fit 3D datasets comprising 3D representations (e.g., multi-view images, point cloud, NeRF, 3D GS and mesh), enabling direct 3D synthesis via forward propagation during inference without iterative optimization, thereby achieving order-of-magnitude acceleration compared to optimization-based approaches. Concurrently, advancements in 3D data availability and algorithmic innovations have driven qualitative leaps in generation fidelity and generalization capability. The evolution of feed-forward 3D generation can be categorized into two distinct paradigms: **_2D-lifting-to-3D generation paradigm_** and **_3D native generation paradigm_**.

#### 2D-lifting-to-3D Generation Paradigm

The 2D-lifting-to-3D paradigm introduces 2D priors into feedforward frameworks, analogous to optimization-based methods, allowing cross-modal knowledge transfer from large-scale 2D datasets. The 2D-lifting-to-3D paradigm is broadly divided into two categories, with the first focusing on single-stage 3D reconstruction from single image input through image embedding techniques (e.g., DINOv2 [56]) for feature extraction, followed by 3D geometry synthesis via Vision Transformer (ViT)[20] architectures. Representative methods include LRM [24], which reconstructs Neural Radiance Fields (NeRF) [54] from encoded image features, TGS [98] that<tbc>

