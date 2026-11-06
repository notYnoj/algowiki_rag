<tbc>More recent view synthesis techniques are based on 3D Gaussian Splatting (3DGS), which is a point-based representation that optimizes parameters of a 3D Gaussian along with a view-dependent color (parameterized using spherical harmonics) for each point. 3DGS is more suitable for direct geometry editing, since it is straightforward to move the position, orientation, and scale of any particle in the representation.

While Gaussian splatting has proved to be a powerful representation for numerous tasks, this paradigm has several limitations: (1) it often requires millions of Gaussian primitives to enable high rendering quality and accurate scene reconstructions, (2) it’s challenging to make appearance edits that are finer than the size of an individual Gaussian, and (3) free-form geometry deformation remains inconvenient without introducing geometry proxies.

Recent works tackle the first two issues by decoupling the appearance and geometry of Gaussian splatting. Texture-GS [27] learns a global UV mapping for all the ray-Gaussian intersections and stores features of these intersections on a 2D texture map. Instead of learning a global UV mapping with surface parameterization constraints (e.g., simple topologies), another line of works [3,16,18,22,23,30] learn a per-primitive texture map for each Gaussian, where the Gaussians are often restricted to be 2D surfels [5] so texture for each point on the surfel can easily be queried from the texture map with their 2D UV coordinates. Since the frequency of surface textures is often much higher than that of geometry, decoupling the resolutions of geometry and texture representations allows these methods to render scenes photo-realistically with only 5K points [3,16,22,27,30] and enables manipulation of the textures with fine-grained details [16,23,27].

However, none of these methods can perform simultaneous geometry deformation and texture editing. This limitation is rooted in the fundamental representation of Gaussian splatting, where each point is represented as a volume of space. In the case where per-primitive texture maps are learned, preserving textures after deformation requires not only the correct transformation (rotation, scaling) of each Gaussian but also accurate splitting or cloning of primitives to represent deformations that are finer than a Gaussian (as Gaussians are rigid and cannot be bent). Such a process is often intractable in practice. In the case where a global UV mapping is learned, in addition to the difficulties described above, the UV mapping must be correctly found for the new intersection points after deformation. The combination of these factors makes the simultaneous editing of texture and geometry for Gaussian splatting extremely difficult.

## 3 Preliminaries

We briefly introduce the relevant background on attention-based point representations and neural UV mappings, and establish the notation used throughout.

### 3.1 Attention-Based Point Renderers

Attention-based point renderers (like PAPR [31] and Pointtersect [2]) represent scenes as unstructured point clouds coupled with an attention interpola

