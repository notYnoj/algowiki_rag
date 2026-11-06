<tbc>map that softly transitions the mask. Here, the confidence map is calculated by measuring the cosine similarity between the viewing direction and the normal vector of the mesh faces. We apply differential denoising during texture synthesis, which only partially influences the masked regions. The confidence map controls the strength of the effect. This allows the side textures to blend smoothly with the front and back views.

**Remarks for Occlusion Inpainting.** It is important to note that the occlusion-specific UV map is only used for inpainting purposes. As this map captures a limited set of projections, it may introduce artifacts such as visible seams if used for final texturing. To generate the actual texture map, we utilize Blender’s smart UV projection \[7\], to ensure a consistent and high-quality texture across the entire mesh surface.

(a) Original Mesh
(b) Remeshed (quad)
(b) Remeshed (tri)

Figure 15. **Results of Our Remeshing Algorithm**. We employ a carefully designed remeshing scheme after geometry generation for better practical usage for broader applications. (a) shows the original polygonal mesh, (b) shows remeshed output of quadrilateral faces, and (c) shows remeshed output of triangular faces.

