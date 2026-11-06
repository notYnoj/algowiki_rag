hoc fixes. Even with heuristics for next-best-view scheduling and partial texture masks, view-to-view inconsistency and residual holes are common failure modes [RMA\*23, CSL\*23, CKF\*23, LXLW24]. Recent formulations that synchronize multi-view denoising improve global consistency, but do not fully eliminate occlusion-driven gaps on challenging geometry [LXLW24].<tbc>

\(\bullet\) **Small and imperfect open-source datasets for textured assets.** Large-scale 3D repositories (e.g., Objaverse/Objaverse-XL) provide breadth and diversity, yet textures are heterogeneous in quality, licensing, and parameterization, and rarely include physically based (PBR) channels at scale [DSS\*23,D\*23]. Dedicated material datasets exist--from measured SVBRDFs to modern CC0 PBR collections--but they typically provide 2_D_ material assets (planar patches) rather than curated, high-quality, per- _mesh_ UV textures suitable for training texturing models end-to- end [MXZ\*23, VD24]. As a result, supervision remains limited for learning high-fidelity, mesh-aligned appearance.<tbc>

\(\bullet\) **Generalization and factorization of appearance.** Models trained on small or weakly curated datasets can bake view-dependent effects (specularities, shadows) into albedo and struggle to predict physically meaningful material maps (albedo/roughness/metalness) that generalize across objects and lighting. Progress in neural inverse rendering and reflectance decomposition underscores both the promise and the difficulty of robust, disentangled estimation under unknown illumination and complex geometry [ZSD\*21, BBJ\*21, MXZ\*23]. Foundational, broadly generalizable material estimators for in-the-wild meshes remain an open problem.<tbc>

\(\bullet\) **Computational cost and memory footprint.** High-resolution UVs (multi-UDIM, 8-16 K) and multi-view diffusion sampling are expensive in time and GPU memory. Although distillation and consistency-model techniques offer a path to reducing sampling steps, pipelines that couple high-resolution UV baking with multi-view regularization are still resource-intensive, especially in academic settings [LTH\*23, CKF\*23, CSL\*23].

## 8. Conclusion and Future Work

Neural 3D mesh texturing has rapidly developed into a vibrant research area, with growing impact on 3D asset creation for VFX, e-commerce, advertising, gaming, and related industries. Recent advances in diffusion models, vision-language priors, and differentiable rendering have significantly expanded the capabilities of automated texture generation, enabling workflows that are more scalable, expressive, and less reliant on manual intervention.

In this survey, we presented a comprehensive overview of this field, categorizing methods into foundational neural approaches, optimization-based methods, and accelerated diffusion- based pipelines, while analyzing their design choices in terms of supervision, guidance, and architectural patterns. Alongside a review of current datasets, evaluation strategies, and practical applications, we identified key limitations related to occlusion-aware synthesis, dataset quality, the generalization and factorization of physical appearance, and computational cost.

Looking ahead, future work in neural mesh texturing will likely expand along multiple directions, including greater scale, dynamic and deformable settings, and continued improvements in quality,<tbc>

<tbc>controllability, and interactivity, alongside related advances in part- aware 3D understanding [PVN\*25]. We outline a few concrete problems below:

\(\bullet\) **Texturing 3D scenes.** Compared with individual 3D objects, scenes exhibit greater geometric diversity and looser structural relationships among constituent objects. This added complexity makes scene-level texturing more challenging, particularly when enforcing appearance consistency across objects, materials, and spatial context.<tbc>

\(\bullet\) **Geometry-aware view planning and coverage.** Beyond heuristic camera schedules, optimization- or learning-based view planning that explicitly maximizes surface coverage and uncertainty reduction could mitigate self-occlusion while minimizing redundant renderings. Integrating coverage metrics with synchronized multi-view denoising may further reduce inconsistency [CSL\*23, LXLW24].<tbc>

\(\bullet\) **Dynamic textures and materials.** With video diffusion models maturing, generating temporally coherent animated textures (e.g., flowing patterns or wear over time) is a natural extension. Ensuring temporal stability across UV seams and under motion, including deforming meshes, poses new challenges in conditioning, regularization, and evaluation [KKW\*23].<tbc>

\(\bullet\) **Deformation- and correspondence-aware texturing for dynamic meshes.** Extending static pipelines to articulated or topology-varying meshes requires correspondence-robust mapping across frames or poses and appearance transport that respects stretch, compression, and contact. Combining deformation-aware parameterization with multi-view diffusion priors is a promising direction.<tbc>

\(\bullet\) **Scalability and speed.** Practical adoption benefits from faster sampling (few-step or distilled samplers), tile- and patch-based UV generation with seamless blending, and memory-efficient training and inference for multi-UDIM assets. Recent latent consistency approaches suggest a promising path toward substantial speedups while preserving fidelity [LTH\*23].<tbc>

\(\bullet\) **Faithful material decomposition and relightability.** Joint estimation of mesh-aligned albedo, normal, roughness, metallicity, and environment illumination remains difficult at scale. Hybrid pipelines that couple diffusion priors with physically motivated inverse rendering, and that train against measured or high- quality synthetic SVBRDF corpora, could yield more robust and relightable assets [ZSD\*21, BBJ\*21, MXZ\*23].

Last but not least, there is still a pressing need for curated, rights-cleared benchmarks of textured _meshes_ with high-resolution UVs and, ideally, PBR channels, paired with standardized metrics for multi-view consistency, seam visibility, and perceptual quality under novel lighting and viewpoints. Recent dataset efforts provide important building blocks, but they do not yet provide mesh- aligned supervision at scale [DSS\*23, MXZ\*23, VD24].

## References

