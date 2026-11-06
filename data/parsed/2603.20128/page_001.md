# Generalizable NGP-SR: Generalizable Neural Radiance Fields Super-Resolution via Neural Graph Primitives

**Abstract**

_Neural Radiance Fields (NeRF) achieve photorealistic novel view synthesis but become costly when high- resolution (HR) rendering is required, as HR outputs demand dense sampling and higher-capacity models. Moreover, naively super-resolving per-view renderings in 2D often breaks multi-view consistency. We propose Generalizable NGP-SR, a 3D-aware super-resolution framework that reconstructs an HR radiance field directly from low- resolution (LR) posed images. Built on Neural Graphics Primitives (NGP), NGP-SR conditions radiance prediction on 3D coordinates and learned local texture tokens, enabling recovery of high-frequency details within the radiance field and producing view-consistent HR novel views without external HR references or post-hoc 2D up- sampling. Importantly, our model is generalizable: once trained, it can be applied to unseen scenes and rendered from novel viewpoints without per-scene optimization. Experiments on multiple datasets show that NGP- SR consistently improves both reconstruction quality and runtime efficiency over prior NeRF-based super-resolution methods, offering a practical solution for scalable high- resolution novel view synthesis. Our project page and code are available at `https://wanqiyuan.github.io/ Generalizable-NGP-SR/`.

### 1. Introduction

Neural Radiance Fields (NeRF) [25] have significantly advanced 3D scene reconstruction and novel view synthesis, enabling photorealistic rendering from sparse 2D images. Follow-up works extended NeRF to support anti- aliased multiscale representations [2, 39, 41], dynamic scene [18, 31, 37], real-time rendering [7, 9, 38], and inverse<tbc>

<tbc>rendering[36]. Despite these advances, NeRF’s rendering quality is highly dependent on high-resolution (HR) inputs, and producing HR images is computationally expensive due to dense sampling and large network capacity. A natural solution is super-resolution (SR), which reconstructs high- frequency details from low-resolution (LR) inputs. However, naive 2D SR applied to NeRF renderings often breaks multi-view consistency, leading to artifacts in novel views.

Existing NeRF-based SR methods attempt to mitigate this but face significant limitations. Optimization-based methods [10, 14, 33] often rely on HR reference images, limiting generalization, or struggle to maintain fine-detail consistency. While recent diffusion-based approaches [5, 17] improve perceptual fidelity, they introduce stochastic geometric hallucinations and incur high computational costs, rendering them impractical for real-time applications. Similarly, adaptations of 3D Gaussian Splatting (3DGS) for SR [30, 32] suffer from the overhead of discrete primitives and scalability issues at large magnification factors.

Furthermore, while generalizable NeRF frameworks [8, 21, 22] have emerged to enable fast reconstruction across diverse scenes, they typically prioritize geometry over texture fidelity, resulting in blurred outputs when scaling to high resolutions. This highlights a critical gap: the need for a framework that combines generalization with _3D- consistent super-resolution_ without the massive overhead of generative foundation models.

In this work, we propose **NGP-SR**, a novel framework that reconstructs high-resolution radiance fields directly from LR inputs and camera poses using Neural Graphics Primitives (NGP). Unlike prior methods that rely on 2D refinement or expensive generative priors, NGP-SR learns high-frequency details directly in 3D space. We achieve this by conditioning the radiance field on **texture tokens** extracted from multi-resolution local feature patches. These tokens provide patch-level context and effectively induce<tbc>

Wanqi Yuan <br>
Clemson University <br>
wanqiy@clemson.edu

Omkar Sharad Mayekar <br>
Clemson University <br>
omayeka@clemson.edu

Connor Pennington <br>
Clemson University <br>
cjpenni@clemson.edu

Nianyi Li <br>
Clemson University <br>
nianyil@clemson.edu

