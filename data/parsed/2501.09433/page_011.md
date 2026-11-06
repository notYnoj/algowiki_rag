## Appendix

## A . Discussions and Limitations

In the main manuscript, we introduced CaPa, a carve-and-paint framework designed for fast, scalable, and high-fidelity 3D asset generation. While CaPa demonstrates significant practical advancements, some limitations remain.

**Understanding of Physically Based Rendering Material.** A notable limitation of the current CaPa pipeline is the lack of intrinsic support for Physically Based Rendering (PBR) materials. While CaPa is designed to generate high-quality textures, it does not inherently address PBR material understanding. Nonetheless, CaPa’s model-agnostic architecture allows for integration with external frameworks, making it compatible with recent material-aware diffusion models such as LightControlNet (as proposed in FlashTex \[9\]) and MaterialFusion \[22\]. By leveraging these material-oriented models, CaPa can be extended to facilitate PBR-aware asset generation, as illustrated in Figure 9.

In line with FlashTex and MaterialFusion, we utilized SDS optimization to generate PBR-aware 3D assets with material diffusion models. For additional information on SDS application for PBR separation, we refer readers to FlashTex \[9\] and MaterialFusion \[22\]. As demonstrated in Figure 9, CaPa exhibits adaptability in achieving PBR material understanding. However, we observed that SDS optimization often led to a decrease in the original texture fidelity and increased overall generation time, typically extending beyond 10 minutes per asset. Additionally, we found that the process sometimes produced a diffuse appearance that differed slightly from the originally generated texture.

Future work will focus on balancing material disentanglement with CaPa’s original objective of rapid generation, aiming to achieve efficient, high-quality, and PBR-compatible textured mesh generation. Building on CaPa’s base mesh and existing normal maps, one potential approach could involve training a diffusion model that takes normal map inputs to disentangle and separately generate diffuse, specular, and roughness maps. This would enable finer control over material properties, allowing CaPa to produce even more physically accurate textures while maintaining efficiency.

Original
Lighting 1
Lighting 2
Lighting 3
PBR-aware CaPa

Figure 9. **Result of the CaPa with PBR Understanding.** We demonstrate CaPa’s capability for disentangling physically based rendering (PBR) materials. The figure shows PBR-aware generation results under various lighting conditions: ‘city,’ ‘studio,’ and ‘night,’ using Blender’s default environment settings \[7\]. As shown, CaPa effectively adapts to different light environments, highlighting its potential for PBR-aware asset generation.

