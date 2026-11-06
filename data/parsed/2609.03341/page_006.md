<tbc>(bijectivity) losses and additional regularizers to learn the UV mappings; we refer readers to [20] for full details.

To enable texture editing and to encourage an even allocation of texture resolution over the scene, Nuvo also penalizes mapping distortion using conformal and stretch regularizers that operate on the differential of each chart’s 3D\(\rightarrow\)2D UV mapping [20]. These regularizers require the surface normal at each surface point to construct tangent-space directions, which are not explicitly available for raw attention-interpolated intersection points \(\mathbf{x}_i^\text{can}\). We therefore use a normal- free distortion loss in Sec. 4.2 that removes the need for surface normals.

## 4 Method

The goal of PointGT is to enable persistent texture edits under non-rigid deformation for point-based neural representations. While applying texture edits to deformed surfaces is relatively straightforward for meshes--where texture coordinates (UVs) are explicitly attached to vertices and interpolate naturally across triangles--point clouds lack this explicit connectivity. Consequently, maintaining a consistent mapping between the deformed geometry and a 2D texture map becomes fundamentally difficult, often causing texture edits to drift or break when the underlying points move non-rigidly.

To tackle this challenge, the choice of the underlying point-based representation is critical. As discussed, Gaussian Splatting-based methods struggle to preserve surface continuity under non-rigid deformations (Fig. 2, left), and may break continuous texture mapping. In contrast, attention-based renderers like PAPR [31] maintain surface continuity via smooth point interpolation (Fig. 2, right), providing the stable surface points required for consistent UV mapping.

Building upon this insight, PointGT introduces a framework for simultaneous geometry and texture editing. To ensure the attention-based surface points

Textured Splats
Featured Points (illustrated with RGB colors)
Non-rigid Deformation
Render by alpha blending
Non-rigid Deformation
Render by interpolating points with attention
No smooth surface anymore
Maintains surface continuity
Textured Gaussian Splattings
Ours

**Fig.2:** Comparison of geometry deformations of textured Gaussian splatting methods and PointGT. **Left:** Since each Gaussian is a linear primitive, these methods struggle to preserve surface smoothness under large non-rigid deformations. **Right:** PointGT maintains surface continuity after deformation by predicting ray-surface points via attention-based interpolation on a point cloud.

