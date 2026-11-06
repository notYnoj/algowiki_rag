<tbc>boundary after small-scale damage using surrounding context, but large-scale perturbations may result in stochastic boundary relocation. Because the system relies on local rules rather than global coordinates, it lacks the spatial prior required to fix the original interface during regeneration. At these larger scales, the system may also exhibit the stability trade-offs identified in our ablation study ( 2), such as localized texture divergence or a loss of structural coherence when damage exceeds the model’s recovery radius.

Two examples of regeneration of damaged grafted textures are illustrated in Fig. 6. It can be observed, that for the smaller damage patch (Fig. 6a left), the NCA succeeds in reconstructing the damage (Fig. 6a right), while for the second example of a larger patch (Fig. 6b left), the aforementioned drift phenomena can be easily observed (Fig. 6a right and 6b) right).

### 3.2. Comparison with alternative methodologies

Unlike standard NCAs that require a dedicated model for each target [18, 19, 20], our framework establishes a versatile many-to-one mapping. By leveraging genomic information, a single architecture can synthesize a diverse set of textures and perform robust damage recovery. This decoupling of the model from a specific target increases architectural efficiency and enables unique capabilities, such as texture grafting through the blending of genomic inputs.

Compared to GANs and CNNs, NCAs offer significant parameter efficiency (often _\<_10_k_ parameters) and spatial flexibility. While GANs and CNNs capture large-scale structures more effectively, they are resource-intensive and prone to tiling artifacts. NCAs generalize well from limited data and grow patterns to any scale without boundary blurring. However, their decentralized, local-rule-based nature limits global structural oversight and requires an iterative inference process, whereas GANs and CNNs provide faster, deterministic passes. Ultimately, NCAs serve as a lightweight, scalable solution for unstructured textures.

Recent grafting approaches often merge separate NCA instances via spatial masking [22]. While our model supports this, we propose a more efficient method using the genomic channel within a single automaton. Although this single- instance approach may exhibit boundary drift over time, a limitation which can be resolved by multi-instance masking,<tbc>

<tbc>our method achieves seamless transitions within a unified state space. Most significantly, conditioning a single NCA on a genomic manifold avoids the linear scaling of memory and computational costs inherent in maintaining multiple parallel instances.

## 4. CONCLUSIONS AND FUTURE WORK

Neural Cellular Automata represent a rapidly evolving class of models advancing research in both software and hardware. By modeling self-organization and regeneration, NCAs offer powerful applications in physics, robotics, and biology. These lightweight models excel at real-time texture synthesis and demonstrate impressive adaptability, allowing for seamless resizing as well as complex texture combinations and grafting.

This paper extends the work presented in [13] on multi- texture synthesis with NCAs by adapting the training procedure to enable robust texture regeneration for damaged regions. This self-regenerating capability is significant not only for computer graphics but also for any domain exploring the properties of self-organizing systems.

In addition to regeneration, we highlight the ability of genome-based NCAs to construct combined textures through grafting during inference without specialized retraining. Our results showcase high-quality grafted textures with fluid transitions across all tested samples. Nevertheless, specific configurations, such as texture pairs with significant scale disparities or structural conflicts (e.g., horizontal vs. vertical stripes, may produce unexpected results. Investigating these edge cases and the genomic manifold’s limits constitutes a key direction for future research.

A current limitation is that NCAs capture a texture’s stylistic essence rather than providing pixel-wise reproduction. Addressing this trade-off between fidelity and model size remains a challenge. Future research should investigate methods to enhance visual fidelity without significantly increasing parameter counts, perhaps via hierarchical or multi- scale architectures that capture broader structural features within a compact state space.

Scale-dependent recovery also remains a consideration; regeneration reliability decreases as the damage radius increases. Furthermore, genomic competition and circular drift can lead to the eventual replacement of "weaker" textures by dominant ones over extended evolution. These phenomena highlight the current boundaries of the genomic manifold and motivate further investigation into more robust spatial anchoring mechanisms.

Extending this methodology to 3D voxel or mesh-based NCAs could open new possibilities for procedural content generation. Finally, a rigorous theoretical analysis of boundary dynamics between conflicting genomes could provide deeper insights into the stability of multi-class self-organizing systems.

(a)
(b)

**Fig. 6.** Examples for regenerated grafted textures. In (a) the regenerated texture is obtained at step 300, in (b) at step 500.

