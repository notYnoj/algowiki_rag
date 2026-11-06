crucial factor in generating visually coherent 3D assets. However, when faced with certain edge cases, such as complex or highly occluded areas (_e.g._, the panda example), both methods (a) and (b) encounter challenges in filling occluded regions.

On the other hand, as demonstrated in Figure 13 (c), UV ControlNet shows its capability to fill all occlusions comprehensively in UV space, albeit at a reduced fidelity level. This trade-off reflects the inherent limitations of 3D-aware methods and automatic view selection when attempting to achieve high coverage in extreme cases. UV ControlNet achieves full occlusion fill by directly addressing gaps in the UV space, albeit with a reduction in texture detail, which may not be ideal for high-fidelity applications. In contrast, our 3D-aware inpainting offers superior texture fidelity and coherence across most scenarios. This trade-off between coverage and detail emphasizes the potential for future enhancements that balance high-quality inpainting with comprehensive occlusion handling.

## B.4 . Text-to-3D Results of CaPa

Lastly, Figure 14 demonstrates CaPa’s capabilities in generating high-quality 3D assets from textual prompts. Results across different object categories, including characters, common objects, and cultural artifacts, affirm CaPa’s generalization ability to maintain geometric stability and texture consistency in various shapes and surface types.

## C . Additional Details of CaPa

### C.1 . Mesh Extraction and Remeshing Algorithm

In 3D asset generation, obtaining a high-quality mesh is essential for downstream applications, as it allows the asset to be integrated effectively into various environments, such as rendering engines and simulation pipelines. While recent advancements in Neural Rendering, such as NeRF and Gaussian Splitting, these representations suffer from accurate surface reconstruction [10, 44]. As a result, extracting meshes from Gaussian Splitting or NeRF degrades mesh quality after a typical mesh conversion algorithm like Marching Cube [26].

In response, DMTet [38] and FlexiCubes [39] have addressed this problem by optimizing meshes through external learnable parameters for meshing. While these approaches significantly improve output mesh quality, the computational cost is intensive and still generates incomplete or suboptimal geometries.

### C.1.1 Initial Mesh Extraction

Unlike previous works with NeRF or Gaussian Splitting representation, our 3D diffusion model operates on occupancy fields that inherently align better with mesh extraction methods. This compatibility enables us to achieve cleaner, higher-fidelity geometry, avoiding the substantial quality loss common in meshing processes for NeRF and GS-based assets. We first extract the initial mesh of the generated occupancy field by leveraging the Marching Cube algorithm [26].

### C.1.2 Automated Remeshing Post-Processing

After the mesh conversion, we design an automated post-processing pipeline to obtain a cleaner topology. This post-processing enhances the geometric quality and accelerates the extraction process. Our pipeline begins by ensuring manifold properties of the generated mesh through a series of cleaning and remeshing steps. The mesh cleaning process enhances quality by removing unreferenced or isolated elements and repairing non-manifold components. Floater removal processes unreferenced vertices by merging duplicates and removing zero-area faces as well as small, isolated components. For non-manifold repair, faces connected to non-manifold edges are iteratively removed, starting with the smallest faces, to maintain 2-manifold properties. Our remeshing step offers flexibility by supporting both triangular and quadrilateral mesh options.

**Triangular Remeshing.** For triangular remeshing, following Botsch et al. [28], we iteratively refine the base mesh through isotropic remeshing to form equilateral triangles. This process involves alternating edge lengths and vertex valence equalization to generate a uniformly remeshed surface. Specifically, edge lengths are adjusted to a predefined target constant through edge splitting and collapsing, achieving uniform face sizes across the mesh. Then, vertex valence deviation is minimized toward 6 (or 4 at boundaries) by applying edge flips, thereby enhancing structural uniformity. Following these steps, an area-based tangential smoothing process is applied to preserve the surface shape. Each vertex is adjusted toward a centroid, calculated as<tbc>

