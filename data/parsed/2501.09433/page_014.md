## B . Additional Experiments

### B.1 . Additional Image-to-3D Results of CaPa

In Figure 10, we present additional image-to-3D asset generation results, with close-up renderings highlighting CaPa’s superior texture and geometric stability fidelity. Each row illustrates a detailed comparison between the base geometry and the final textured model, highlighting CaPa’s ability to produce cohesive and visually rich textures. Close-up views underscore the fidelity of fine details, such as the texture of the tiger’s skin, dragon’s scales, and intricate patterns on the bag. As shown, CaPa achieves state-of-the-art quality in texture coherence and structural consistency.

We present additional comparative experiments of state-of-the-art Image-to-3D asset generation methods in Figure 11. Consistent with Section 4 in the main manuscript, we validate CaPa against Unique3D \[54\], Era3D \[18\], DreamCraft3D \[43\], and SF3D \[3\]. Each row represents a different 3D asset (_e.g._, tiger, dragon, toy robot, and character model) with full-color renderings and corresponding grayscale meshes for each method. As shown in Figure 11, CaPa consistently delivers high- quality textures and detailed geometry within a significantly reduced runtime (around 30 seconds) compared to other methods. This comparison highlights the efficiency and fidelity balance achieved by our approach.

### B.2 . Impact of Spatially Decoupled Cross Attention on Janus Artifacts

### B.2.1 Qualitative Analysis

In this section, we present a qualitative comparison to demonstrate the effectiveness of the proposed spatially decoupled cross-attention mechanism in mitigating the Janus problem, a common issue in 3D asset generation when handling multi-view inputs. As seen in Figure 12, spatially decoupled cross attention markedly improves multi-view consistency and eliminates Janus artifacts, demonstrating the necessity of spatial decoupling when incorporating multi-view guidance. This mechanism thus enhances CaPa’s ability to generate high-quality 3D assets with accurate textures and structure across all views, supporting its robustness for diverse applications.

(a)
(b)
(c)

Figure 12. **Impact of Spatially Decoupled Cross Attention on Janus Artifacts**. In this additional figure, We demonstrate the capability of Janus prevention in the proposed spatially decoupled cross-attention mechanism. Each row depicts, (a) with spatially decoupled cross attention, (b) without spatially decoupled cross attention, and (c) a mesh rendering of the current view, respectively.

