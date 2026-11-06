<tbc>damentals of 3D mesh representation in Sec. 2.1, introduce surface parameterization as a bridge from 3D surfaces to 2D texture domains in Sec. 2.2, summarize rendering and differentiable rendering in Sec. 2.3, discuss physically based rendering (PBR) and PBR materials in Sec. 2.4, and outline key learning paradigms relevant to neural mesh texturing--neural fields [XTS\*22], vision-language models [R\*21, LLXH22], VAEs [KW19], GANs [GPM\*14], and diffusion models [HJA20]--in Sec. 2.5. Together, these topics provide the foundation for the survey that follows.

## 2.1. Why 3D Meshes?

Triangle meshes are the dominant explicit representation for surfaces in computer graphics and vision [BKP\*10,AHH\*18,DSS\*23, KMJ\*19]. A mesh encodes geometry as a finite set of vertex positions together with a connectivity structure of edges and faces, which defines adjacency relations and surface topology (Fig. 2). In practice, triangle meshes support rich per-primitive attributes such as normals, colors, and material identifiers, making them a natural carrier for appearance information [AHH\*18]. From a texturing standpoint, this explicit representation is crucial: appearance channels can be deterministically associated with well-defined surface elements, and mesh connectivity supports the consistent propagation of these signals across the surface [BKP\*10].

Contrasting meshes with alternative shape encodings (Fig. 3) helps explain why they are the primary surface representation considered in this survey [BKP\*10]. Point-based and surfel models<tbc>

<tbc>capture geometry without explicit connectivity and are attractive for point- or splat-based rendering, but they do not provide a standard 2D surface parameterization for texture mapping [PZVBG00, RL00]. Volumetric grids--dense or sparse--have been widely used for image-to-shape prediction and 3D reconstruction, but become memory-bound at high resolutions and typically require isosurface extraction to yield deployable surfaces [CXG\*16,LC87]. Continuous implicit fields represent shapes as decision boundaries or signed-distance zero sets [MON\*19,PFS\*19], while radiance fields directly model view-dependent appearance in 3D space [MST\*20]. Although these formulations excel at reconstruction and novel- view synthesis, their outputs are often converted to triangle meshes (_e.g._, via marching cubes [LC87]) to interoperate with texture-map- based tools and rendering engines.

## 2.2. Mesh Parameterization

Mesh parameterization assigns each point on a surface a coordinate in a two-dimensional domain, defining a mapping from 3D surface space to 2D [SPR06] (Fig. 4). In practice, because general surfaces typically cannot be flattened into a single planar domain without introducing cuts and/or distortion, a triangle mesh is partitioned into a set of charts--connected surface patches--each mapped to a planar region; the collection of these charts, packed into one or more 2D texture images, forms an atlas. The resulting per-vertex UV coordinates define the texture parameterization and are interpolated per fragment during rendering. Charts meet along seams where the UV mapping is discontinuous. Parameterization also enables raster textures to be sampled and filtered during rendering. To improve filtering across scales, textures are typically stored in a mipmap hierarchy, which precomputes progressively downsampled versions of the image to reduce aliasing during minification [Wil83].

From a texturing standpoint, parameterization decouples geometry from appearance. Appearance attributes--such as albedo, normal, and roughness--can be stored in image space at resolutions largely independent of mesh tessellation and sampled consistently during rendering [YKSH19]. Once parameterized, texture resolu<tbc>

Vertices
Edges
Faces
Polygons
Surfaces
3D Model

Voxels
Points
Meshes
Signed Distance Field
Implicit surface
SDF 0
SDF < 0
-0.50-0.25 0.00 0.25 0.50
Signed distance value

28 charts
15 charts
26 charts
106 charts

**Figure 2:** _A 3D mesh is defined by vertices (points), edges (line segments), and faces (surface elements, often triangles or quads), which combine into surface patches that approximate the object’s geometry. Figure reproduced from [Lob09]._

**Figure 3:** _3D shape representations. Voxels discretize space, point clouds sample points, meshes encode surface connectivity, and SDFs represent shapes implicitly via a continuous signed distance function. Figure reproduced from [AFL23]._

**Figure 4:** _Mesh parameterization maps a 3D surface to a 2D domain (UV space) by partitioning it into charts and flattening each into a planar region. Example meshes (left) and UV layouts (right) show varying chart counts. Figure adapted from [WWS\*25]._

