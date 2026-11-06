<tbc>base representation, which has challenges for accurate surface reconstruction. When converting their representations into usable forms (_i.e., mesh_), quality degradation occurs, remaining a key bottleneck for downstream tasks.

To address these challenges, we introduce **CaPa**, a two- stage **_Carve-n-Paint_** framework designed to generate high- quality, clean 3D meshes efficiently. By decoupling geometry generation and texture synthesis, CaPa enhances both flexibility and performance at each stage, allowing for precise reconstruction of the mesh and detailed texture output.

In the geometry generation stage, CaPa leverages a 3D latent diffusion model. It focuses on producing an occupancy field that is not only structurally consistent across multiple views but also mesh-compatible. This process utilizes multi- view inputs to guide the generation, ensuring precise geometry that seamlessly integrates with the subsequent texture synthesis stage. The resulting high-quality mesh provides a stable foundation, crucial for achieving cohesive textures.

In the texture synthesis stage, we employ a novel _Spatially Decoupled Cross Attention_, which generates high- resolution textures (up to 4K). By isolating and processing view-specific features within a unified diffusion framework, this method effectively resolves multi-view inconsistencies, such as the Janus problem. Notably, its model-agnostic approach does not require architectural modifications or extensive retraining. This design integrates smoothly with large pre-trained models like SDXL [32], outperforming previous approaches. As a result, it produces geometry-aligned, cohesive, and high-fidelity textures as shown in Figure 1.

Additionally, to further enhance texture completeness, CaPa introduces a 3D-aware occlusion inpainting algorithm. This algorithm efficiently fills untextured regions by generating a UV map that preserves surface locality, enabling seamless inpainting while minimizing visible seams.

Comprehensive experiments validate the effectiveness of CaPa, demonstrating significant improvements in both texture fidelity and geometric stability over existing methods. CaPa consistently delivers high-fidelity polygonal meshes in a fraction of the time, setting a new standard for practical and scalable 3D asset generation.

The core contributions of this work are summarized as:

• **Mesh-Optimized 3D Generation Pipeline**: Separating geometry and texture generation, enabling effective meshing and enhancing the practicality of 3D asset generation.<tbc>

• **Spatially Decoupled Cross Attention**: A model-agnostic, training-free solution to generate 4K textures without additional training, super-resolution, and janus problem.<tbc>

• **3D-aware Fast Occlusion Inpainting**: A robust inpainting solution for handling occluded regions in 3D textures, reducing visible seams, and preserving texture fidelity.<tbc>

• **State-of-the-art Results**: CaPa achieves significantly higher texture and geometry fidelity, marking a major step forward in practical 3D asset generation.

## 2 . Related Work

### 2.1 . 3D Asset Generation

Given the recent advancements in neural rendering [29] and diffusion-based generative models, researchers have explored this success to the 3D generation area. A notable approach is Score-Distillation Sampling (SDS) [33, 48], which utilizes 2D diffusion priors to generate 3D assets. Several subsequent studies [19, 20, 43, 46, 50, 58] have provided a more robust theoretical foundation, post-processing, or better visual fidelity. Despite these advances, these methods’ reliance on Neural Radiation Fields (NeRF) as the underlying 3D representation results in slow generation times and poor quality after mesh conversion.

Another prominent limitation of SDS is the "Janus problem," where artifacts such as multiple faces appear. To mitigate this issue, researchers have explored enhancing diffusion models with a multi-view generation [23, 40, 49] by adjusting U-Net to interact across these views. Although these methods largely resolved the Janus problem, the SDS’s progressive updating still results in slower generation times. To accelerate the slow speed, certain studies [27, 54] have proposed generating normal maps from multi-view images and employing differentiable mesh updates or sparse view neural reconstruction. Nevertheless, this approach often leads to unstable geometry, or low-fidelity textures (refer to the second, third column of Figure 6).

### 2.2 . 3D-Native Reconstruction Models

Recently, Large Reconstruction Models (LRMs) [13, 41, 45, 51, 56, 60], a transformer models for directly generating 3D assets have emerged. LRMs predict the NeRF or Gaussian Splatting parameters directly through feed-forward inferences. These approaches significantly reduce generation times and produce 3D assets in near real-time. However, scaling these methods to higher resolutions remains challenging, with most state-of-the-art LRMs currently limited to low-fidelity outputs (see the fourth sample in Figure 1).

Recently, the research community has explored alternative approaches for 3D _shape_ generation through 3D latent diffusion, diverging from the LRM paradigm. Michelangelo [63] introduced VAE for 3D latent representation, establishing an aligned latent space for images, text, and 3D data. Several following works [52, 55, 62] enhance its geometry understanding and address its limitations in diversity. Concurrently, CLAY [62] demonstrated that 3D geometry generation, particularly using DiT [31] (Diffusion Transformer), could scale similar to other large foundational models in deep learning. However, these models focus primarily on shape generation. To synthesize textures, they rely on external texturing methods [4, 5, 24] or multi-view diffusion. Additionally, all the aforementioned methods are time-consuming, and aligning textures with generated shapes remains difficult.

