<tbc>implicit spatial offsets during radiance evaluation, resembling a multi-sampling behavior that helps recover fine structures while maintaining multi-view coherence. By integrating these token-augmented features within NGP’s efficient hash encoding, our method synthesizes high-fidelity HR renderings with strong generalization to unseen scenes. Our key contributions are:

• We propose **NGP-SR**, a 3D-aware super-resolution framework built on **feature-enhanced Neural Graphics Primitives**, which conditions radiance prediction jointly on spatial coordinates and multi-resolution **local patch texture tokens**.<tbc>

• We demonstrate that token-conditioned radiance learning can recover high-frequency details while promoting **multi-view consistency** from only LR inputs and camera poses, without requiring HR reference images.<tbc>

• We show strong **generalization to unseen scenes**, enabling direct HR synthesis for novel viewpoints from LR observations, with improved quality and efficiency over prior NeRF-based SR methods.

## 2 . Related Work

### Neural Radiance Fields (NeRF).

Since the introduction of NeRF \[25\], significant efforts have focused on improving its efficiency and applicability. Works such as MipNeRF \[2\], Zip-NeRF \[3\], and others \[12, 13, 20, 27, 39, 41\] tackled anti-aliasing and scale issues. Others extended NeRF to dynamic scenes \[23, 28, 31, 37\] and real-time rendering \[7, 9, 11, 29, 38\]. Instant-NGP \[26\] introduced multi-resolution hash encoding for near-instant reconstruction, while 3D Gaussian Splatting (3DGS) \[16\] utilized explicit primitives for real-time speeds. To avoid per-scene optimization, generalizable frameworks emerged. MVS- Gaussian \[21\] and GeFU \[22\] leverage multi-view stereo and geometry-aware fusion, respectively, while GDB- NeRF \[8\] utilizes depth-guided bundle sampling. However, these generalizable methods often compromise high- frequency detail for robustness, a limitation our method addresses.

### NeRF Super-Resolution.

NeRF-based SR must recover high-frequency detail while maintaining cross-view consistency, unlike conventional 2D SR \[6, 34, 35\]. Prior approaches use HR references \[14, 33\], per-scene latent optimization \[10\], or diffusion-based refinement \[17\], often incurring additional supervision, optimization cost, or inference overhead. FastSR-NeRF \[19\] improves efficiency with lightweight SR modules but is less effective at large magnification. Recent 3DGS SR methods adapt video/2D SR priors \[5, 30, 32\], but discrete primitives and pretrained priors can introduce overhead and reduce robustness across scenes/resolutions.

### Generalizable NeRFs.

Recent works on generalizable NeRFs aim to reconstruct novel scenes without per-scene optimization. MVSGaussian \[21\] integrates Gaussian splatting with multi-view stereo for fast reconstruction, but its explicit structure struggles to capture fine-grained HR details. GeFU \[22\] improves quality via geometry-aware fusion and refined rendering, yet still requires scene-specific refinements for consistent HR outputs. GDB-NeRF \[8\] introduces depth-guided bundle sampling for efficient generalization but does not address super-resolution, leaving high-frequency detail underrepresented. Overall, these methods achieve efficiency and generalization but fall short in producing high-resolution, view-consistent outputs directly from LR inputs--a gap our method addresses.

In contrast, we propose Generalizable NGP-SR, which leverages Neural Graphics Primitives (NGP) to reconstruct high-resolution radiance fields directly from LR inputs and camera poses. By learning high-frequency details in the 3D domain, our framework ensures multi-view consistency, generalizes to unseen scenes, and significantly improves both quality and efficiency compared to existing super- resolution and generalizable NeRF approaches.

## 3 . Generalizable NGP-SR Method

Given a set of low-resolution (LR) images \(\{\mathbf{I}_n^\text{LR}\}_{n=1}^N\) with corresponding camera poses \(\{\mathbf{C}_n\}_{n=1}^N\), our goal is to reconstruct a super-resolved radiance field. Once trained, the model can directly synthesize HR outputs for novel viewpoints with camera poses \(\{\mathbf{C}'_m\}\) not seen during training, given only their LR renderings. As illustrated in Fig. 1, our framework consists of three key components: **1) Hierarchical View-Texture Encoding:** Multi-scale LR image patches and their corresponding camera poses are encoded into fixed-length tokens. **2) Camera-Aware Feature Integration:** Camera poses are embedded into the feature generation process, allowing viewpoint-dependent representations that generalize across novel scenes and viewpoints. **3) Global Feature Fusion:** We integrate global LR image features to guide the decoding of HR signals, ensuring multi- view consistency and fine-grained detail.

Our design is inspired by VR-INR \[1\], which employs hierarchical encoding for video SR. Unlike VR-INR, which operates in purely spatial-temporal domains, our method explicitly incorporates 3D geometry through camera-aware integration and feature fusion, enabling generalizable high- resolution novel view synthesis.

### 3.1 . Hierarchical View-Texture Encoding

Given LR input images \(\mathbf{I}_n^\text{LR}\) and their associated camera poses **C**_<sub>n</sub>_, our goal is to construct compact, view-aware query tokens that serve as the foundation for 3D-consistent super-resolution.

