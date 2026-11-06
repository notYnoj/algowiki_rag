<tbc>ity often relies on human perception. Many surveyed works include user studies to compare perceptual quality and user preference [PWMAZ24,RMA\*23,CSL\*23]. Despite the variety of quantitative metrics, user studies remain essential for evaluating perceptual realism and semantic satisfaction, though they are subjective and not perfectly reproducible. Common strategies to reduce bias include diversifying participants and evaluation tasks, randomizing presentation order, and carefully controlling comparison protocols. Typical study designs include pairwise A/B preference tests reporting the _win rate_ (\(\uparrow\)), ranking tasks reporting the _average rank_ (\(\downarrow\)), and absolute rating studies yielding a _mean opinion score_ (_MOS_) (\(\uparrow\)) [ITU19].

User studies are typically reported across multiple aspects: _overall quality_; _structural guidance alignment_ (respecting mesh semantics during texturing) [XZT\*24]; _stylistic guidance alignment_; _level of detail_ and _presence of artifacts_ [CKF\*23]; _seam visibility_; _diversity_; and _3D consistency_ across views [LXLW24]. In practice, user studies are most informative when interpreted alongside quantitative metrics.

In a field where no single metric is sufficient, a multifaceted evaluation strategy that combines distribution-level statistics, per- instance accuracy, semantic alignment, user studies, runtime analysis, and robustness tests across different inputs offers the most holistic view of a method’s performance. Each class of metrics captures a distinct aspect of the textured output, and together they reveal the complementary strengths and trade-offs of neural 3D texturing approaches in the literature.

## 6. Applications

Neural 3D mesh texturing supports a broad range of task settings and downstream applications. Research has progressively addressed complementary problem settings, including synthesizing textures from text [RMA\*23, CSL\*23] or images [PWMAZ24], estimating physically based (PBR) materials [CCL\*22, ZLX\*24], aligning category-level UVs [CYF22], completing missing appearance on partial scans [CPM20], localized texturing [DLAH24], and scene-scale texturing [WLX\*24, HYC\*25, YGC\*24]. Beyond benchmarking, these advances map naturally to practical use cases across content creation, telepresence, visualization, simulation, gaming, and fabrication, where the final output is often a UV- parameterized mesh--and increasingly a full PBR material stack-- whose appearance can be edited, relit, and rendered efficiently (Fig. 24):

\(\bullet\) **Asset creation for games, XR, and robotics.** Text- and image-guided pipelines generate high-quality textures on fixed meshes from high-level prompts or exemplars, accelerating look development, style exploration, and re-skinning; representative systems include prompt-driven and diffusion-guided UV synthesis [RMA\*23, CSL\*23, CKF\*23, LXLW24]. Outputs integrate with real-time engines via PBR material maps (albedo/roughness/normal, _etc._), enabling fast relighting and consistent deployment across platforms [CCL\*22, CCJJ23]. In practice, teams can use these models to produce on-brand variants (_e.g._, seasonal skins) while preserving decals and layout fidelity inherited from the mesh UVs [RMA\*23,CSL\*23]. More<tbc>

broadly, diversified textures on scene meshes are often used in simulation to improve sim-to-real transfer for perception and control in robotics [TFR\*17].<tbc>

\(\bullet\) **Digital humans and telepresence.** Neural textures for deformable meshes offer temporally stable, high-fidelity avatar rendering, reenactment, and appearance editing, making them relevant to telepresence and virtual production [TZN19]. Related pipelines transfer garment patterns and prints to clothed-body meshes while respecting canonical UVs or part correspondences, supporting virtual try-on and fashion prototyping [NKML25, ZWC\*24]. When PBR is required, texturing methods that estimate SVBRDF channels enable realistic relighting and integration into real or virtual environments [CCL\*22, ZLX\*24].<tbc>

\(\bullet\) **E-commerce and product visualization.** For product visualization, texturing techniques enable fabric, leather, or finish swaps on a single mesh, allowing customized previews and photoreal variants. Diffusion- and image-conditioned approaches can reduce manual authoring time while preserving brand constraints and UV semantics [PWMAZ24, YHK\*24].<tbc>

\(\bullet\) **3D stylization and look development.** Optimization and feedforward methods that modify appearance directly on 3D surfaces or meshes enable consistent, multi-view stylization (_e.g._, painterly, toon, or brand-specific styles) with artist-in-the-loop control; coupling semantic guidance (text/image) with structural cues (normals/depth) improves fidelity and geometry awareness for interactive authoring [MBOL\*22,HJN22,PWMAZ24].

## 7. Limitations

While 3D mesh texturing has advanced rapidly with the advent of diffusion-driven generative pipelines, several important challenges remain:

\(\bullet\) **Incomplete texturing from multi-view projection.** Methods that texture a mesh by iteratively projecting and inpainting from multiple rendered views--e.g., TEXTure, Text2Tex, and TexFusion--are effective and convenient because they leverage off-the-shelf, pre-trained text-to-image diffusion models and require little or no task-specific training. However, they inherently cover only camera-visible regions in each step; self-occluded or rarely visible areas may remain underspecified and require post-

Game Characters
Digital Humans

**Figure 24:** _Applications of 3D mesh texturing in games and VFX. Textures add material detail and realism to production assets such as game characters (left) and digital humans (right). Figure adapted from [Dem24, Wol17]._

