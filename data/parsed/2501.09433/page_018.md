<tbc>a weighted average of neighboring vertices based on area. The gravity-weighted centroid **g**_<sub>i</sub>_ for each vertex **p**_<sub>i</sub>_ is given by:

\(\mathbf{g}_i:=\frac{1}{\sum_{p_j\in N(p_i)}A(p_j)}\sum_{p_j\in N(p_i)}A(p_j)\mathbf{p}_j,\) (6)

where _A(p<sub>j</sub>_) denotes the area associated with vertex **p**_<sub>j</sub>_, and _N(p<sub>i</sub>_) is the set of neighboring vertices of **p**_<sub>i</sub>_. This weighted average ensures that vertices with larger areas have a stronger influence, thereby smoothing the mesh more uniformly.

To ensure tangential smoothing on the surface, the update vector is projected back onto the tangent plane of **p**_<sub>i</sub>_ as follows:

\(\mathbf{p}_i\leftarrow\mathbf{p}_i+\lambda\left(\mathbf{I}-\mathbf{n}_i\mathbf{n}_i^T\right)(\mathbf{g}_i-\mathbf{p}_i),\) (7)

where **n**_<sub>i</sub>_ is the normal vector of **p**_<sub>i</sub>_, and \(\lambda\) is a damping factor used to avoid oscillations. This projection moves each vertex in the tangent direction toward its centroid, smoothing the mesh while preserving its overall shape.

**Quadrilateral Remeshing.** Following Jakob et al. \[53\], quadrilateral remeshing is designed to produce structured meshes composed of quadrilateral faces, offering a uniform and easily manageable layout ideal for various applications requiring high-quality surface control. This process is accomplished through two primary stages: 1) Orientation Field Optimization and 2) Position Field Optimization.

### 1) Orientation Field Optimization:

This initial step establishes directional alignment across the mesh surface by defining an orientation field. This field prescribes specific directional vectors at each vertex, effectively creating a structured "grid" on the surface. By aligning each edge along these pre-defined directions, the mesh gains a cohesive pattern that ensures smooth transitions across faces, an essential property for generating a clean quadrilateral structure.

### 2) Position Field Optimization:

Once edge orientations are set, the positions of vertices are optimized to achieve consistent spacing between edges, regulated by a global scale factor. This scale factor, provided by the user, enforces uniform edge lengths across the entire mesh, ensuring that each quadrilateral face remains similarly sized. Vertices are locally adjusted on a 2D tangent plane to fit within this structured layout, resulting in a smooth, evenly distributed quadrilateral grid.

By combining these two stages, the quadrilateral remeshing process yields a quadrilateral mesh that maintains both geometric coherence and structural regularity, making it suitable for applications demanding high fidelity and uniform surface representation. This approach allows for a stable, grid-like arrangement that balances surface alignment with positional consistency across the mesh. For further details on quadrilateral remeshing, we refer readers to the Instant Field-Alignment \[53\].

**Experimental Results.** Figure 15 illustrates the results before and after remeshing. In Figure 15 (b), the triangle remeshing outcome yields a highly regular mesh compared to Figure 15 (a), with uniformly distributed Voronoi regions around each vertex. Similarly, as shown in Figure 15 (c), each quadrilateral face is uniform, and the overall mesh contains fewer irregular vertices. These results demonstrate how post-processing forms a smooth and stable mesh structure.

In conclusion, our automated post-processing pipeline improves the uniformity and quality of generated meshes while significantly reducing processing time. Our approach yields visually superior, computationally efficient meshes through manifold enforcement, flexible remeshing techniques, and advanced texture unwrapping, optimizing the overall 3D asset generation workflow.

**C.2 . Texture Generation**

As mentioned in the main manuscript, we first render four orthogonal views of the generated mesh for texture synthesis. Then, we generate corresponding images for rendered inputs, by leveraging our novel spatially decoupled attention mechanism. In this stage, to achieve a state-of-the-art quality of texture generation, we have implemented our texture generative scheme on the SDXL \[32\]. We have utilized pre-trained IP Adapter \[57\] layer and CLIP \[34\] for the image feature extractor, Depth- ControlNet \[61\] for a geometric guide to align with the geometry. Notably, to generate texture efficiently, we have adopted the SDXL lightning model \[21\] baseline checkpoint of our texture generation and occlusion inpainting. With this diffusion pipeline, we have operated only 8 steps per inference with DPM-solver.

However, at this stage, directly applying textures from four views often results in visible seams where the views meet. In response, we leveraged a smoothing mechanism specifically for the side views, similar to the previous works \[1, 5, 17\]. When generating the side textures, we mask out the regions already visible in the front and back views, using a confidence<tbc>

