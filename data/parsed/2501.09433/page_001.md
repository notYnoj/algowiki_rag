# CaPa: Carve-n-Paint Synthesis for Efficient 4K Textured Mesh Generation

**Abstract**

_The synthesis of high-quality 3D assets from textual or visual inputs has become a central objective in modern generative modeling. Despite the proliferation of 3D generation algorithms, they frequently grapple with challenges such as multi-view inconsistency, slow generation times, low fidelity, and surface reconstruction problems. While some studies have addressed some of these issues, a comprehensive solution remains elusive. In this paper, we introduce **CaPa**, a carve-and-paint framework that generates high-fidelity 3D assets efficiently. CaPa employs a two-stage process, decoupling geometry generation from texture synthesis. Initially, a 3D latent diffusion model generates geometry guided by multi-view inputs, ensuring structural consistency across perspectives. Subsequently, leveraging a novel, model-agnostic Spatially Decoupled Attention, the framework synthesizes high-resolution textures (up to 4K) for a given geometry. Furthermore, we propose a 3D-aware occlusion inpainting algorithm that fills untextured regions, resulting in cohesive results across the entire model. This pipeline generates high-quality 3D assets in less than 30 seconds, providing ready-to-use outputs for commercial applications. Experimental results demonstrate that CaPa excels in both texture fidelity and geometric stability, establishing a new standard for practical, scalable 3D asset generation._

### 1. Introduction

The demand for scalable, high-quality 3D assets is rapidly growing across industries such as gaming, film, and VR/AR. While recent advancements in machine learning have led to remarkable achievements in text and image generation, extending these successes to 3D content creation has been challenging. The high-dimensional nature of 3D data, coupled with a scarcity of diverse and high-quality datasets, has constrained the progress of 3D generative models and created unique challenges in achieving efficiency and fidelity.

Despite these inherent obstacles, researchers have made considerable efforts to adapt generative techniques for 3D, resulting in unprecedented growth and exploration. A prominent approach involves lifting 2D diffusion models to 3D through Score Distillation Sampling (SDS) [33, 48]. However, SDS often encounters limitations such as the Janus problem (texture discrepancies across views), difficulties in achieving high-quality mesh, and prolonged generation times. These shortcomings arise largely because of the over- reliance on indirect 3D information from 2D models, which hampers both the efficiency and fidelity of generated outputs.

In response, recent advances in Large Reconstruction Models (LRM) [13, 60] have resolved the slow speed issue by leveraging autoregressive generative models [47]. While promising, these methods continue to face trade-offs, particularly in output quality. Moreover, most 3D generation methods rely on NeRF [29] or Gaussian Splatting [16] as their

<sup>∗</sup>corresponding author.

Ours ~ 30 seconds, 4K DreamCraft3D ~3 hours, 1K Unique3D SF3D ~ 2 minutes, 2K (w/ SR) ~ 10 seconds, 1K

Hwan Heo<br> Jeong A Wi<br> Jangyeong Kim<br> Junyoung Choi<br> Sangjun Ahn <sup>∗</sup>

Graphics AI Lab, NC Research

{hwanheo, jangyeongk, seongyeong2, jaywi, jychoi13, sjahn21}@ncsoft.com

Figure 1. Comparison of _mesh_ quality with state-of-the-art image-to-3D methods. **CaPa** can generate a hyper-quality _textured mesh_ in under 30 seconds, providing 3D assets ready for commercial applications such as games, movies, and VR/AR.

