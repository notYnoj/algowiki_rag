# PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations

**Abstract.** We present PointGT, a point-based 3D representation that enables simultaneous editing of object geometry and appearance. Existing reconstruction and view synthesis techniques produce volumetric 3D representations that are high-quality and photorealistic, but are difficult to edit. In particular, recent efforts to enable texture editing for 3D Gaussian Splatting representations are not compatible with geometry edits and deformations. Our method combines a point-based representation that is well-suited for geometry deformations with a learned UV mapping technique that enables high-resolution texture editing. We show that PointGT enables fine-grained editing of both geometry and texture in point-based neural representations with high rendering quality. Project page: https://zvict.github.io/pointgt/.

**Keywords:** Point neural representation \(\cdot\) Geometry and texture editing

### 1 Introduction

Point-based radiance field representations, most notably 3D Gaussian Splatting (3DGS) [10], have emerged as a powerful approach to novel view synthesis and 3D reconstruction. These methods represent scenes as point clouds, where each point is associated with a volumetric primitive (_e.g._ a 3D Gaussian distribution) that has an opacity and a single view-dependent color. Rasterizing these volumetric primitives is efficient, so techniques such as 3DGS can quickly optimize large collections of primitives to represent detailed scenes.

However, since each Gaussian is assigned a single (view-dependent) color, 3DGS can only represent detailed appearance and textures by using many (often millions) of Gaussian primitives. This coupling of geometry and appearance resolution prevents scenes reconstructed by 3DGS from being easily edited. Editing appearance is difficult because the textures of reconstructed scenes cannot be

<sup>⋆</sup> Corresponding author.

Yanshu Zhang<sup>1⋆</sup> , George Shramko<sup>1</sup> , Pratul P. Srinivasan<sup>4</sup> , and Ke Li<sup>1,2,3</sup> <sup>1</sup> Simon Fraser University, Canada <sup>2</sup> Alberta Machine Intelligence Institute (Amii), Canada <sup>3</sup> Canadian Institute for Advanced Research (CIFAR), Canada <sup>4</sup> Google DeepMind, USA `{yanshu\_zhang, george\_shramko, keli}@sfu.ca pratul.srinivasan@gmail.com`

