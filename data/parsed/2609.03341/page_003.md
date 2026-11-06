- We extend PAPR to include a learned UV mapping from 3D points on objects to a learned 2D texture map. (Sec. 4.2)<tbc>

**-** We introduce two novel geometry regularizers that significantly improve the fidelity of PAPR’s geometry representation and demonstrate that these are crucial for effective UV mapping. (Sec. 4.1)<tbc>

**-** We propose a deformation-aware correspondence mechanism that explicitly maps deformed-space ray intersections back to canonical space via displacement fusion, preserving texture attachment under non-rigid edits. (Sec. 4.3)

### 2 Related Work

Editing the geometry and appearance of 3D assets is a core part of the computer graphics workflow for digital content creation. While there are many established techniques and tools for editing widely-used mesh-based representations, editing the 3D representations produced by recent view synthesis and 3D reconstruction methods is much more challenging.

The geometry of neural scene representations such as Neural Radiance Fields (NeRFs) [13] cannot be directly edited, so many works [8,15,24,26,28,29,32,34] have focused on associating NeRFs with proxy geometry which can be edited, and then converting this edited proxy geometry back into the NeRF representation. However, converting NeRFs to proxy geometry and back can introduce approximation errors, and the choice of proxy geometry can limit the types of edits that are possible.

On the other hand, the appearance of reconstructed NeRFs can be edited by optimizing UV mapping functions that map from 3D coordinates on the object to 2D texture coordinates [20,25]. In this work, we use ideas from Nuvo [20] to develop a UV mapping technique for point-based reconstruction techniques.

#### 2.1 3D Shape Deformation and Correspondence

Classical geometry processing has a rich history of editing 3D shapes, leveraging methods like As-Rigid-As-Possible (ARAP) deformation [19], Moving Least Squares (MLS), and embedded deformation graphs [21] to manipulate surface meshes or cages flexibly. While these approaches effectively manipulate geometry and preserve local structural rigidity, applying appearance edits to the deformed surfaces is relatively straightforward for meshes because texture coordinates (UVs) are explicitly attached to vertices and interpolate naturally across triangles.

However, projecting and interpolating high-resolution 2D textures onto unstructured, dynamically-weighted point clouds is fundamentally difficult. As point-based neural representations (like PAPR or 3DGS) lack explicit connectivity, the set of neighbors and attention weights used to define a surface point can shift non-rigidly under deformation. PointGT directly targets this novel problem of establishing canonical correspondence within dynamic attention fields to enable robust texture persistence.

