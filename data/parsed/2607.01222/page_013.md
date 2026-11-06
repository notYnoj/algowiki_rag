<tbc>geometry. Our primary comparison is with Trellis-2, a recently released state-of- the-art 3D generation model that supports both joint geometry–texture generation and texture synthesis conditioned on a given geometry and reference image. To ensure a fair comparison, we adopt the second mode of Trellis-2, where the model is provided with the same white-mesh geometry and reference image as inputs. As shown in  1, Ink3D significantly outperforms Trellis-2 and other competing methods in texture synthesis quality. This improvement highlights the advantage of introducing geometry-aware video generation into the texture creation pipeline, enabling Ink3D to synthesize richer and more detailed surface appearances. Additional qualitative results are provided in the supplementary material.

### 4.2 Ablation Studies

**3D Geometry Prior in OrbitPainter.** As introduced in Section 3.1, Orbit- Painter is trained with two conditioning priors: (1) a 2D texture appearance prior provided by the reference image, and (2) a 3D geometry prior provided by the white-mesh geometry. The latter prior goes beyond traditional image-to-video generation settings. To incorporate this 3D geometry prior, we introduce two additional conditioning signals: a surface-normal video and a 3D-position video. In  2, we compare our default model with two ablated variants: one without the surface-normal video prior and another without the 3D-position video prior. As shown in  2, removing either prior degrades the performance, with the removal of the 3D-position prior causing a particularly significant drop. This is because the 3D-position signal provides strong geometric guidance, helping OrbitPainter maintain geometry-consistent appearance across orbit-scan frames.

**Geometry-Aware Sparse Attention.** In Section 3.2, we introduce a Geometry- Aware Sparse Attention (GASA) layer, which operates in parallel with the full attention layer, as illustrated in Figure 2(b). GASA explicitly encourages the network to learn correspondences across frames by linking pixels that share the same original 3D location when re-projected into 3D space. In  2, we compare our default model with a variant that removes GASA. The observed performance drop demonstrates that better utilization of geometric priors improves geometry consistency across the generated orbit-scan frames, which in turn leads<tbc>

\begin{tabular}{ccccc}
Setting & FID\(\downarrow\) & CLIP-FID\(\downarrow\) & LPIPS\(\downarrow\) & CLIP-I\(\uparrow\) \\
Baseline & 103.7 & 195.6 & 0.2030 & 0.8980 \\
w/o Surface Normal & 113.9 & 218.3 & 0.2128 & 0.8841 \\
w/o 3D-Position & 149.2 & 361.5 & 0.2367 & 0.8282 \\
w/o GASA & 109.9 & 203.7 & 0.2077 & 0.8893 \\
\end{tabular}

** 2:** Ablation study on leveraging 3D geometry priors in OrbitPainter. Orbit- Painter incorporates geometry priors to generate geometry-consistent orbit-scan videos at two levels: (1) _input level_, by directly providing a 3D-position video and a surface- normal video as additional inputs; and (2) _network level_, by introducing the proposed Geometry-Aware Sparse Attention (GASA), which constrains attention to be performed among pixels corresponding to the same 3D location across frames.

