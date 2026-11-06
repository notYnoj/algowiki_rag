## B Additional Ablation Results

We show ablation results for the proposed on-ray regularizer 5 and the deformation- aware correspondence 13 in Figure 12, in addition to Figure 7b. As shown, the proposed on-ray regularizer significantly reduces the artifacts of the texture editing, and the deformation-aware correspondence effectively boosts the editing fidelity.

## C Discussion of Other Gaussian Splatting Baselines

As noted in the main paper, we choose GSTex [16] as the primary baseline for simultaneous geometry and texture editing. Here we provide additional discussion and evidence for why the other baselines are limited in their ability to perform simultaneous geometry and texture editing.

Texture-GS [27] supports texture editing through a single-chart global texture map. However, this representation often struggles with complex geometries, resulting in texture maps that are insufficient for reliable texture-space editing in practice (see Figure 13). For a fair comparison, Figure 14 shows the comparison of simultaneous geometry and texture editing results on the ‘Butterfly’ scene from Objavese, where Texture-GS successfully generates a valid map. As shown, unlike Texture-GS, which suffers from broken surface continuity and loss of resolution after deformation, our method ensures that texture edits remain sharp and continuous.

UV mapping
Edited texture
Texture map
Edit 1
Edit 2

**Fig.11: Part duplication** on the Blossom scene. The duplicated geometry is shown under two different texture edits. _UV mapping_: checkerboard visualization of the learned charts; _Edited texture_: the rendered result; _Texture map_: the corresponding 2D texture map. The texture stays correctly attached to the duplicated parts through the canonical UV mapping.

